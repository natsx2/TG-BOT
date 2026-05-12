import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { tgUsersTable, botStatsTable } from "@workspace/db/schema";
import { z } from "zod";
import { requireAuth } from "../middlewares/auth";
import { logger } from "../lib/logger";
import { eq, sql } from "drizzle-orm";

const router: IRouter = Router();

router.post("/register", async (req, res) => {
  const schema = z.object({
    tgId: z.string(),
    username: z.string().optional(),
    firstName: z.string().optional(),
    lastName: z.string().optional(),
  });

  const parsed = schema.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: "Invalid request" });
    return;
  }

  const { tgId, username, firstName, lastName } = parsed.data;

  const existing = await db.select().from(tgUsersTable).where(eq(tgUsersTable.tgId, tgId)).limit(1);

  if (existing.length > 0) {
    res.json({ success: true, status: existing[0].status, user: existing[0] });
    return;
  }

  const [user] = await db
    .insert(tgUsersTable)
    .values({ tgId, username, firstName, lastName, status: "pending" })
    .returning();

  await db
    .update(botStatsTable)
    .set({
      totalUsers: sql`${botStatsTable.totalUsers} + 1`,
      updatedAt: new Date(),
    });

  logger.info({ tgId, username }, "New TG user registered");
  res.json({ success: true, status: "pending", user });
});

router.get("/status/:tgId", async (req, res) => {
  const { tgId } = req.params;
  const [user] = await db.select().from(tgUsersTable).where(eq(tgUsersTable.tgId, tgId)).limit(1);

  if (!user) {
    res.json({ found: false, status: "unregistered" });
    return;
  }

  res.json({ found: true, status: user.status, user });
});

router.get("/", requireAuth, async (_req, res) => {
  const users = await db.select().from(tgUsersTable).orderBy(sql`${tgUsersTable.registeredAt} DESC`);
  res.json({ users, total: users.length });
});

function parseId(raw: string | string[]): number {
  const id = parseInt(Array.isArray(raw) ? raw[0] : raw);
  return isNaN(id) ? -1 : id;
}

router.post("/:id/approve", requireAuth, async (req, res) => {
  const id = parseId(req.params.id);
  if (id < 0) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  const [user] = await db
    .update(tgUsersTable)
    .set({ status: "approved", approvedAt: new Date() })
    .where(eq(tgUsersTable.id, id))
    .returning();

  if (!user) {
    res.status(404).json({ error: "User not found" });
    return;
  }

  logger.info({ id, tgId: user.tgId }, "TG user approved");
  res.json({ success: true, user });
});

router.post("/:id/reject", requireAuth, async (req, res) => {
  const id = parseId(req.params.id);
  if (id < 0) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  const schema = z.object({ note: z.string().optional() });
  const parsed = schema.safeParse(req.body);
  const note = parsed.success ? parsed.data.note : undefined;

  const [user] = await db
    .update(tgUsersTable)
    .set({ status: "rejected", note: note ?? null })
    .where(eq(tgUsersTable.id, id))
    .returning();

  if (!user) {
    res.status(404).json({ error: "User not found" });
    return;
  }

  logger.info({ id, tgId: user.tgId }, "TG user rejected");
  res.json({ success: true, user });
});

router.delete("/:id", requireAuth, async (req, res) => {
  const id = parseId(req.params.id);
  if (id < 0) {
    res.status(400).json({ error: "Invalid id" });
    return;
  }

  await db.delete(tgUsersTable).where(eq(tgUsersTable.id, id));
  res.json({ success: true });
});

export default router;
