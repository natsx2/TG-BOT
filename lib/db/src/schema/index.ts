import { pgTable, text, serial, boolean, timestamp, integer } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";

export const adminTable = pgTable("admin", {
  id: serial("id").primaryKey(),
  username: text("username").notNull().unique(),
  password: text("password").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export const botConfigTable = pgTable("bot_config", {
  id: serial("id").primaryKey(),
  botEnabled: boolean("bot_enabled").notNull().default(true),
  botToken: text("bot_token").notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export const botLogsTable = pgTable("bot_logs", {
  id: serial("id").primaryKey(),
  tool: text("tool").notNull(),
  userId: text("user_id").notNull(),
  username: text("username"),
  action: text("action").notNull(),
  status: text("status").notNull().default("info"),
  message: text("message").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const botStatsTable = pgTable("bot_stats", {
  id: serial("id").primaryKey(),
  totalUsers: integer("total_users").notNull().default(0),
  totalRequests: integer("total_requests").notNull().default(0),
  au2FmRequests: integer("au2_fm_requests").notNull().default(0),
  fbCloneRequests: integer("fb_clone_requests").notNull().default(0),
  nikaSharerRequests: integer("nika_sharer_requests").notNull().default(0),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export const tgUsersTable = pgTable("tg_users", {
  id: serial("id").primaryKey(),
  tgId: text("tg_id").notNull().unique(),
  username: text("username"),
  firstName: text("first_name"),
  lastName: text("last_name"),
  status: text("status").notNull().default("pending"),
  registeredAt: timestamp("registered_at").defaultNow().notNull(),
  approvedAt: timestamp("approved_at"),
  note: text("note"),
});

export const insertAdminSchema = createInsertSchema(adminTable).omit({ id: true, createdAt: true, updatedAt: true });
export const insertBotConfigSchema = createInsertSchema(botConfigTable).omit({ id: true, updatedAt: true });
export const insertBotLogSchema = createInsertSchema(botLogsTable).omit({ id: true, createdAt: true });
export const insertTgUserSchema = createInsertSchema(tgUsersTable).omit({ id: true, registeredAt: true, approvedAt: true });

export type Admin = typeof adminTable.$inferSelect;
export type BotConfig = typeof botConfigTable.$inferSelect;
export type BotLog = typeof botLogsTable.$inferSelect;
export type BotStats = typeof botStatsTable.$inferSelect;
export type TgUser = typeof tgUsersTable.$inferSelect;
export type InsertBotLog = typeof botLogsTable.$inferInsert;
export type InsertTgUser = typeof tgUsersTable.$inferInsert;
