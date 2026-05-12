import { Router, type IRouter, type Request } from "express";
import { db } from "@workspace/db";
import { botUsersTable, tasksTable, toolSettingsTable } from "@workspace/db";
import { eq, count, and, gte, sql, desc } from "drizzle-orm";
import { createSession, invalidateSession, getSessionToken, requireAdmin } from "../lib/session";
import { sendMessage } from "../lib/telegram";
import { invalidateSettingsCache } from "../lib/settings";
import { stopTask } from "../lib/taskRunner";
import {
  AdminLoginBody,
  ApproveUserParams,
  RejectUserParams,
  RejectUserBody,
  DeleteBotUserParams,
} from "@workspace/api-zod";

const ADMIN_USERNAME = "admin";
const ADMIN_PASSWORD = "admin000";

const router: IRouter = Router();

router.post("/admin/login", async (req, res) => {
  const parse = AdminLoginBody.safeParse(req.body);
  if (!parse.success) { res.status(400).json({ error: "Invalid request body" }); return; }
  const { username, password } = parse.data;
  if (username !== ADMIN_USERNAME || password !== ADMIN_PASSWORD) {
    res.status(401).json({ error: "Invalid username or password" }); return;
  }
  const token = await createSession(username);
  res.setHeader("Set-Cookie", `session=${token}; Path=/; HttpOnly; SameSite=Lax; Max-Age=86400`);
  res.json({ username, authenticated: true, token });
});

router.post("/admin/logout", async (req, res) => {
  const token = getSessionToken(req);
  if (token) await invalidateSession(token);
  res.setHeader("Set-Cookie", "session=; Path=/; Max-Age=0");
  res.json({ success: true, message: "Logged out" });
});

router.get("/admin/me", requireAdmin, async (req, res) => {
  const adminReq = req as Request & { adminUser?: { username: string } };
  res.json({ username: adminReq.adminUser?.username ?? "admin", authenticated: true });
});

router.get("/admin/stats", requireAdmin, async (_req, res) => {
  const todayStart = new Date();
  todayStart.setHours(0, 0, 0, 0);

  const [totalResult, pendingResult, approvedResult, rejectedResult, todayResult, tasksResult] = await Promise.all([
    db.select({ count: count() }).from(botUsersTable),
    db.select({ count: count() }).from(botUsersTable).where(eq(botUsersTable.status, "pending")),
    db.select({ count: count() }).from(botUsersTable).where(eq(botUsersTable.status, "approved")),
    db.select({ count: count() }).from(botUsersTable).where(eq(botUsersTable.status, "rejected")),
    db.select({ count: count() }).from(botUsersTable).where(gte(botUsersTable.createdAt, todayStart)),
    db.select({ count: count() }).from(tasksTable).where(eq(tasksTable.status, "running")),
  ]);

  res.json({
    total: totalResult[0].count,
    pending: pendingResult[0].count,
    approved: approvedResult[0].count,
    rejected: rejectedResult[0].count,
    todayRegistrations: todayResult[0].count,
    runningTasks: tasksResult[0].count,
  });
});

router.get("/admin/users", requireAdmin, async (req, res) => {
  const { status, search } = req.query as { status?: string; search?: string };
  let query = db.select().from(botUsersTable).$dynamic();
  if (status && status !== "all") {
    const validStatuses = ["pending", "approved", "rejected"] as const;
    if (validStatuses.includes(status as typeof validStatuses[number])) {
      query = query.where(eq(botUsersTable.status, status as typeof validStatuses[number]));
    }
  }
  const users = await query.orderBy(sql`${botUsersTable.createdAt} DESC`);
  let filtered = users;
  if (search) {
    const s = search.toLowerCase();
    filtered = users.filter(u =>
      u.firstName.toLowerCase().includes(s) ||
      (u.username ?? "").toLowerCase().includes(s) ||
      (u.lastName ?? "").toLowerCase().includes(s) ||
      u.telegramId.includes(s)
    );
  }
  res.json(filtered.map(u => ({
    ...u,
    createdAt: u.createdAt.toISOString(),
    updatedAt: u.updatedAt?.toISOString() ?? null,
    expiresAt: u.expiresAt?.toISOString() ?? null,
  })));
});

router.post("/admin/users/:id/approve", requireAdmin, async (req, res) => {
  const parse = ApproveUserParams.safeParse({ id: Number(req.params.id) });
  if (!parse.success) { res.status(400).json({ error: "Invalid user ID" }); return; }

  const [user] = await db.update(botUsersTable)
    .set({ status: "approved", updatedAt: new Date(), rejectionReason: null })
    .where(eq(botUsersTable.id, parse.data.id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }

  await sendMessage(user.telegramId,
    `✅ <b>Registration Approved!</b>\n\nCongratulations! You now have full access to all tools.\n\nUse /library to browse available tools.`
  );

  res.json({ ...user, createdAt: user.createdAt.toISOString(), updatedAt: user.updatedAt?.toISOString() ?? null, expiresAt: user.expiresAt?.toISOString() ?? null });
});

router.post("/admin/users/:id/reject", requireAdmin, async (req, res) => {
  const paramParse = RejectUserParams.safeParse({ id: Number(req.params.id) });
  if (!paramParse.success) { res.status(400).json({ error: "Invalid user ID" }); return; }
  const bodyParse = RejectUserBody.safeParse(req.body);
  const reason = bodyParse.success ? (bodyParse.data.reason ?? null) : null;

  const [user] = await db.update(botUsersTable)
    .set({ status: "rejected", updatedAt: new Date(), rejectionReason: reason })
    .where(eq(botUsersTable.id, paramParse.data.id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }

  const reasonText = reason ? `\n\n<b>Reason:</b> ${reason}` : "";
  await sendMessage(user.telegramId,
    `❌ <b>Registration Rejected</b>\n\nYour registration has been rejected.${reasonText}\n\nContact support or use /register to re-apply.`
  );

  res.json({ ...user, createdAt: user.createdAt.toISOString(), updatedAt: user.updatedAt?.toISOString() ?? null, expiresAt: user.expiresAt?.toISOString() ?? null });
});

router.delete("/admin/users/:id", requireAdmin, async (req, res) => {
  const parse = DeleteBotUserParams.safeParse({ id: Number(req.params.id) });
  if (!parse.success) { res.status(400).json({ error: "Invalid user ID" }); return; }
  const [deleted] = await db.delete(botUsersTable).where(eq(botUsersTable.id, parse.data.id)).returning();
  if (!deleted) { res.status(404).json({ error: "User not found" }); return; }
  res.json({ success: true, message: "User deleted" });
});

router.post("/admin/users/:id/expiry", requireAdmin, async (req, res) => {
  const id = Number(req.params.id);
  const body = req.body as { expiresAt?: string | null };
  const expiresAt = body.expiresAt ? new Date(body.expiresAt) : null;
  const [user] = await db.update(botUsersTable)
    .set({ expiresAt, updatedAt: new Date() })
    .where(eq(botUsersTable.id, id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }

  if (expiresAt) {
    await sendMessage(user.telegramId,
      `⏰ <b>Access Expiry Set</b>\n\nYour bot access will expire on:\n<b>${expiresAt.toDateString()}</b>\n\nContact admin to renew.`
    );
  }

  res.json({ ...user, createdAt: user.createdAt.toISOString(), updatedAt: user.updatedAt?.toISOString() ?? null, expiresAt: user.expiresAt?.toISOString() ?? null });
});

router.get("/admin/tasks", requireAdmin, async (req, res) => {
  const { telegramId, status, toolName } = req.query as { telegramId?: string; status?: string; toolName?: string };

  let query = db.select().from(tasksTable).$dynamic();

  const conditions = [];
  if (telegramId) conditions.push(eq(tasksTable.telegramId, telegramId));
  if (status && ["running","done","stopped","failed"].includes(status)) {
    conditions.push(eq(tasksTable.status, status as "running" | "done" | "stopped" | "failed"));
  }
  if (toolName && ["share","crck","create"].includes(toolName)) {
    conditions.push(eq(tasksTable.toolName, toolName as "share" | "crck" | "create"));
  }

  if (conditions.length > 0) query = query.where(and(...conditions));

  const tasks = await query.orderBy(desc(tasksTable.createdAt)).limit(100);

  res.json(tasks.map(t => ({
    ...t,
    createdAt: t.createdAt.toISOString(),
    updatedAt: t.updatedAt?.toISOString() ?? null,
    completedAt: t.completedAt?.toISOString() ?? null,
  })));
});

router.post("/admin/tasks/:id/stop", requireAdmin, async (req, res) => {
  const id = Number(req.params.id);
  const task = await db.select().from(tasksTable).where(eq(tasksTable.id, id)).limit(1);
  if (!task.length) { res.status(404).json({ error: "Task not found" }); return; }

  const stopped = stopTask(task[0].telegramId);
  res.json({ success: true, stopped });
});

router.get("/admin/settings", requireAdmin, async (_req, res) => {
  const rows = await db.select().from(toolSettingsTable).limit(1);
  if (!rows.length) {
    const [inserted] = await db.insert(toolSettingsTable).values({}).returning();
    res.json({ ...inserted, updatedAt: inserted.updatedAt.toISOString() });
    return;
  }
  const s = rows[0];
  res.json({ ...s, updatedAt: s.updatedAt.toISOString() });
});

interface SettingsUpdate {
  showOk?: boolean;
  showFail?: boolean;
  showNoCp?: boolean;
  showNoLimit?: boolean;
  notifyEvery?: number;
  maxConcurrentTasks?: number;
  shareDelay?: number;
  crckDelay?: number;
  createDelay?: number;
}

router.put("/admin/settings", requireAdmin, async (req, res) => {
  const body = req.body as SettingsUpdate;

  const rows = await db.select().from(toolSettingsTable).limit(1);

  let updated;
  if (!rows.length) {
    [updated] = await db.insert(toolSettingsTable).values({ ...body, updatedAt: new Date(), updatedBy: "admin" }).returning();
  } else {
    [updated] = await db.update(toolSettingsTable)
      .set({ ...body, updatedAt: new Date(), updatedBy: "admin" })
      .where(eq(toolSettingsTable.id, rows[0].id))
      .returning();
  }

  invalidateSettingsCache();
  res.json({ ...updated!, updatedAt: updated!.updatedAt.toISOString() });
});

export default router;
