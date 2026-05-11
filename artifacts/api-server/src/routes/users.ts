import { Router, type IRouter } from "express";
import { eq, count, sql } from "drizzle-orm";
import { db, usersTable } from "@workspace/db";
import { requireAuth } from "../middlewares/requireAuth";
import { computeExpiry, hashPassword } from "../lib/auth";
import {
  ListUsersQueryParams,
  RegisterUserBody,
  GetUserParams,
  DeleteUserParams,
  ApproveUserParams,
  ApproveUserBody,
  RejectUserParams,
  RejectUserBody,
  UpdateUserAccessParams,
  UpdateUserAccessBody,
} from "@workspace/api-zod";

const router: IRouter = Router();

router.get("/users", requireAuth, async (req, res): Promise<void> => {
  const parsed = ListUsersQueryParams.safeParse(req.query);
  if (parsed.success && parsed.data.status) {
    const users = await db
      .select()
      .from(usersTable)
      .where(eq(usersTable.status, parsed.data.status))
      .orderBy(sql`${usersTable.registeredAt} DESC`);
    res.json(users.map(sanitizeUser));
    return;
  }
  const users = await db
    .select()
    .from(usersTable)
    .orderBy(sql`${usersTable.registeredAt} DESC`);
  res.json(users.map(sanitizeUser));
});

router.get("/users/pending", requireAuth, async (_req, res): Promise<void> => {
  const users = await db
    .select()
    .from(usersTable)
    .where(eq(usersTable.status, "pending"))
    .orderBy(sql`${usersTable.registeredAt} DESC`);
  res.json(users.map(sanitizeUser));
});

router.get("/users/stats", requireAuth, async (_req, res): Promise<void> => {
  const [total]    = await db.select({ count: count() }).from(usersTable);
  const [pending]  = await db.select({ count: count() }).from(usersTable).where(eq(usersTable.status, "pending"));
  const [approved] = await db.select({ count: count() }).from(usersTable).where(eq(usersTable.status, "approved"));
  const [rejected] = await db.select({ count: count() }).from(usersTable).where(eq(usersTable.status, "rejected"));

  res.json({
    total:    total?.count    ?? 0,
    pending:  pending?.count  ?? 0,
    approved: approved?.count ?? 0,
    rejected: rejected?.count ?? 0,
  });
});

router.post("/users/register", async (req, res): Promise<void> => {
  const parsed = RegisterUserBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const existing = await db
    .select()
    .from(usersTable)
    .where(eq(usersTable.telegramId, parsed.data.telegramId));

  if (existing.length > 0) {
    res.status(409).json({ error: "User already registered", user: sanitizeUser(existing[0]!) });
    return;
  }

  const [user] = await db
    .insert(usersTable)
    .values({
      telegramId:       parsed.data.telegramId,
      telegramUsername: parsed.data.telegramUsername ?? null,
      firstName:        parsed.data.firstName ?? null,
      lastName:         parsed.data.lastName  ?? null,
      status: "pending",
    })
    .returning();

  res.status(201).json(sanitizeUser(user!));
});

router.get("/users/:id", requireAuth, async (req, res): Promise<void> => {
  const raw    = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const params = GetUserParams.safeParse({ id: parseInt(raw!, 10) });
  if (!params.success) { res.status(400).json({ error: params.error.message }); return; }
  const [user] = await db.select().from(usersTable).where(eq(usersTable.id, params.data.id));
  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.json(sanitizeUser(user));
});

router.delete("/users/:id", requireAuth, async (req, res): Promise<void> => {
  const raw    = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const params = DeleteUserParams.safeParse({ id: parseInt(raw!, 10) });
  if (!params.success) { res.status(400).json({ error: params.error.message }); return; }
  const [user] = await db.delete(usersTable).where(eq(usersTable.id, params.data.id)).returning();
  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.sendStatus(204);
});

router.patch("/users/:id/approve", requireAuth, async (req, res): Promise<void> => {
  const raw    = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const params = ApproveUserParams.safeParse({ id: parseInt(raw!, 10) });
  if (!params.success) { res.status(400).json({ error: params.error.message }); return; }
  const body   = ApproveUserBody.safeParse(req.body);
  if (!body.success) { res.status(400).json({ error: body.error.message }); return; }

  // Support direct expiresAt date string from frontend
  let expiresAt: Date | null = null;
  if ((req.body as any).expiresAt) {
    expiresAt = new Date((req.body as any).expiresAt);
  } else {
    expiresAt = computeExpiry({
      permanent:       body.data.permanent ?? false,
      durationDays:    body.data.durationDays,
      durationHours:   body.data.durationHours,
      durationMinutes: body.data.durationMinutes,
      durationSeconds: body.data.durationSeconds,
    });
  }

  const [user] = await db
    .update(usersTable)
    .set({
      status:         "approved",
      approvedAt:     new Date(),
      approvedBy:     body.data.approvedBy ?? "admin",
      notes:          body.data.notes ?? null,
      accessUsername: body.data.accessUsername,
      accessPassword: hashPassword(body.data.accessPassword),
      expiresAt,
    })
    .where(eq(usersTable.id, params.data.id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.json(sanitizeUser(user));
});

router.patch("/users/:id/reject", requireAuth, async (req, res): Promise<void> => {
  const raw    = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const params = RejectUserParams.safeParse({ id: parseInt(raw!, 10) });
  if (!params.success) { res.status(400).json({ error: params.error.message }); return; }
  const body   = RejectUserBody.safeParse(req.body ?? {});
  const [user] = await db
    .update(usersTable)
    .set({
      status:     "rejected",
      approvedAt: new Date(),
      approvedBy: body.success ? (body.data.approvedBy ?? "admin") : "admin",
      notes:      body.success ? (body.data.notes ?? null) : null,
    })
    .where(eq(usersTable.id, params.data.id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.json(sanitizeUser(user));
});

// Revoke access — clears credentials, sets back to pending
router.patch("/users/:id/revoke", requireAuth, async (req, res): Promise<void> => {
  const raw = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const id  = parseInt(raw!, 10);
  if (isNaN(id)) { res.status(400).json({ error: "Invalid user id" }); return; }

  const [user] = await db
    .update(usersTable)
    .set({
      status:         "pending",
      accessUsername: null,
      accessPassword: null,
      expiresAt:      null,
      approvedAt:     null,
      approvedBy:     null,
      notes:          "Access revoked by admin",
    })
    .where(eq(usersTable.id, id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.json(sanitizeUser(user));
});

router.patch("/users/:id/access", requireAuth, async (req, res): Promise<void> => {
  const raw    = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;
  const params = UpdateUserAccessParams.safeParse({ id: parseInt(raw!, 10) });
  if (!params.success) { res.status(400).json({ error: params.error.message }); return; }
  const body   = UpdateUserAccessBody.safeParse(req.body);
  if (!body.success) { res.status(400).json({ error: body.error.message }); return; }

  // Support direct expiresAt from frontend
  let expiresAt: Date | null = null;
  if ((req.body as any).expiresAt) {
    expiresAt = new Date((req.body as any).expiresAt);
  } else {
    expiresAt = computeExpiry({
      permanent:       body.data.permanent ?? false,
      durationDays:    body.data.durationDays,
      durationHours:   body.data.durationHours,
      durationMinutes: body.data.durationMinutes,
      durationSeconds: body.data.durationSeconds,
    });
  }

  const updateFields: Record<string, unknown> = {};
  if (body.data.accessUsername != null) updateFields.accessUsername = body.data.accessUsername;
  if (body.data.accessPassword != null) updateFields.accessPassword = hashPassword(body.data.accessPassword);
  if (body.data.permanent !== undefined || expiresAt !== null) updateFields.expiresAt = expiresAt;

  const [user] = await db
    .update(usersTable)
    .set(updateFields)
    .where(eq(usersTable.id, params.data.id))
    .returning();

  if (!user) { res.status(404).json({ error: "User not found" }); return; }
  res.json(sanitizeUser(user));
});

function sanitizeUser(user: typeof usersTable.$inferSelect) {
  const { accessPassword: _pw, ...safe } = user;
  return safe;
}

export default router;
