import crypto from "crypto";
import jwt from "jsonwebtoken";
import { db, settingsTable } from "@workspace/db";
import { eq } from "drizzle-orm";
import { logger } from "./logger";

const JWT_SECRET = process.env.JWT_SECRET ?? "brutetg_admin_jwt_secret_change_in_prod";
const DEFAULT_USERNAME = process.env.ADMIN_USERNAME ?? "admin";
const DEFAULT_PASSWORD = process.env.ADMIN_PASSWORD ?? "admin321";

export function hashPassword(password: string): string {
  return crypto.createHash("sha256").update(password + "brutetg_salt").digest("hex");
}

export function generateToken(username: string): string {
  return jwt.sign({ username, role: "admin" }, JWT_SECRET, { expiresIn: "24h" });
}

export function verifyToken(token: string): { username: string; role: string } | null {
  try {
    return jwt.verify(token, JWT_SECRET) as { username: string; role: string };
  } catch {
    return null;
  }
}

export async function initAdminCredentials(): Promise<void> {
  const existing = await db
    .select()
    .from(settingsTable)
    .where(eq(settingsTable.key, "admin_username"));

  if (existing.length === 0) {
    await db.insert(settingsTable).values([
      { key: "admin_username", value: DEFAULT_USERNAME },
      { key: "admin_password_hash", value: hashPassword(DEFAULT_PASSWORD) },
    ]);
    logger.info("Admin credentials initialized");
  }
}

export async function getAdminCredentials(): Promise<{ username: string; passwordHash: string }> {
  const [usernameRow] = await db
    .select()
    .from(settingsTable)
    .where(eq(settingsTable.key, "admin_username"));
  const [passwordRow] = await db
    .select()
    .from(settingsTable)
    .where(eq(settingsTable.key, "admin_password_hash"));

  return {
    username: usernameRow?.value ?? DEFAULT_USERNAME,
    passwordHash: passwordRow?.value ?? hashPassword(DEFAULT_PASSWORD),
  };
}

export async function setAdminCredentials(username: string, passwordHash: string): Promise<void> {
  await db
    .update(settingsTable)
    .set({ value: username })
    .where(eq(settingsTable.key, "admin_username"));
  await db
    .update(settingsTable)
    .set({ value: passwordHash })
    .where(eq(settingsTable.key, "admin_password_hash"));
}

export function computeExpiry(opts: {
  permanent: boolean;
  durationDays?: number | null;
  durationHours?: number | null;
  durationMinutes?: number | null;
  durationSeconds?: number | null;
}): Date | null {
  if (opts.permanent) return null;
  const now = new Date();
  const ms =
    ((opts.durationDays ?? 0) * 86400 +
      (opts.durationHours ?? 0) * 3600 +
      (opts.durationMinutes ?? 0) * 60 +
      (opts.durationSeconds ?? 0)) *
    1000;
  if (ms <= 0) return null;
  return new Date(now.getTime() + ms);
}
