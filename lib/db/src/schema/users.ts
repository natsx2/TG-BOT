import { pgTable, text, serial, timestamp } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod/v4";

export const usersTable = pgTable("bot_users", {
  id: serial("id").primaryKey(),
  telegramId: text("telegram_id").notNull().unique(),
  telegramUsername: text("telegram_username"),
  firstName: text("first_name"),
  lastName: text("last_name"),
  status: text("status").notNull().default("pending"),
  accessUsername: text("access_username"),
  accessPassword: text("access_password"),
  expiresAt: timestamp("expires_at", { withTimezone: true }),
  registeredAt: timestamp("registered_at", { withTimezone: true }).notNull().defaultNow(),
  approvedAt: timestamp("approved_at", { withTimezone: true }),
  approvedBy: text("approved_by"),
  notes: text("notes"),
});

export const insertUserSchema = createInsertSchema(usersTable).omit({
  id: true,
  registeredAt: true,
  approvedAt: true,
  expiresAt: true,
});

export type InsertUser = z.infer<typeof insertUserSchema>;
export type BotUser = typeof usersTable.$inferSelect;
