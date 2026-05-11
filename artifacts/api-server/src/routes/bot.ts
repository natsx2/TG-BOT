import { Router, type IRouter } from "express";
import { eq } from "drizzle-orm";
import { db, usersTable } from "@workspace/db";
import { hashPassword } from "../lib/auth";
import {
  CheckUserStatusParams,
  VerifyBotUserBody,
} from "@workspace/api-zod";

const router: IRouter = Router();

router.get("/bot/status/:telegramId", async (req, res): Promise<void> => {
  const raw = Array.isArray(req.params.telegramId)
    ? req.params.telegramId[0]
    : req.params.telegramId;

  const params = CheckUserStatusParams.safeParse({ telegramId: raw });
  if (!params.success) {
    res.status(400).json({ error: params.error.message });
    return;
  }

  const [user] = await db
    .select()
    .from(usersTable)
    .where(eq(usersTable.telegramId, params.data.telegramId));

  if (!user) {
    res.status(404).json({ error: "User not registered" });
    return;
  }

  res.json({
    telegramId: user.telegramId,
    status: user.status,
    registered: true,
  });
});

router.post("/bot/verify", async (req, res): Promise<void> => {
  const parsed = VerifyBotUserBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const { telegramId, accessUsername, accessPassword } = parsed.data;

  const [user] = await db
    .select()
    .from(usersTable)
    .where(eq(usersTable.telegramId, telegramId));

  if (!user) {
    res.status(401).json({ error: "User not registered" });
    return;
  }

  if (user.status !== "approved") {
    res.status(401).json({ error: `Access denied. Status: ${user.status}` });
    return;
  }

  if (!user.accessUsername || !user.accessPassword) {
    res.status(401).json({ error: "No credentials set. Contact admin." });
    return;
  }

  if (
    user.accessUsername !== accessUsername ||
    user.accessPassword !== hashPassword(accessPassword)
  ) {
    res.status(401).json({ error: "Invalid credentials" });
    return;
  }

  if (user.expiresAt && new Date(user.expiresAt) < new Date()) {
    res.status(401).json({ error: "Access has expired. Contact admin to renew." });
    return;
  }

  res.json({
    valid: true,
    telegramId: user.telegramId,
    expiresAt: user.expiresAt?.toISOString() ?? null,
    message: "Access granted",
  });
});

export default router;
