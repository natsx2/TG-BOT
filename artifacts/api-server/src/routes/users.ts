import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { botUsersTable } from "@workspace/db";
import { requireAuth } from "../middlewares/requireAuth";
import { logger } from "../lib/logger";
import { eq, sql } from "drizzle-orm";

const router: IRouter = Router();

router.post("/register", async (req, res) => {
  const body = req.body as {
    telegramId?: string;
    username?: string;
    telegramUsername?: string;
    firstName?: string;
    lastName?: string;
  };

  if (!body.telegramId || !body.firstName) {
    res.status(400).json({ error: "telegramId and firstName are required" });
    return;
  }

  const { telegramId, firstName, lastName } = body;
  const username = body.username || body.telegramUsername || undefined;

  const existing = await db
    .select()
    .from(botUsersTable)
    .where(eq(botUsersTable.telegramId, telegramId))
    .limit(1);

  if (existing.length > 0) {
    res.status(409).json({ success: true, status: existing[0].status, user: existing[0] });
    return;
  }

  const [user] = await db
    .insert(botUsersTable)
    .values({ telegramId, username, firstName, lastName, status: "pending" })
    .returning();

  logger.info({ telegramId, username }, "New bot user registered");
  res.status(201).json({ success: true, status: "pending", user });
});

router.get("/status/:telegramId", async (req, res) => {
  const { telegramId } = req.params;
  const [user] = await db
    .select()
    .from(botUsersTable)
    .where(eq(botUsersTable.telegramId, telegramId))
    .limit(1);

  if (!user) {
    res.json({ found: false, status: "unregistered" });
    return;
  }

  res.json({ found: true, status: user.status, user });
});

router.get("/", requireAuth, async (_req, res) => {
  const users = await db
    .select()
    .from(botUsersTable)
    .orderBy(sql`${botUsersTable.createdAt} DESC`);
  res.json({ users, total: users.length });
});

export default router;
