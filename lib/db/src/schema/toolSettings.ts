import { pgTable, text, serial, boolean, integer, timestamp } from "drizzle-orm/pg-core";

export const toolSettingsTable = pgTable("tool_settings", {
  id: serial("id").primaryKey(),
  showOk: boolean("show_ok").notNull().default(true),
  showFail: boolean("show_fail").notNull().default(true),
  showNoCp: boolean("show_no_cp").notNull().default(true),
  showNoLimit: boolean("show_no_limit").notNull().default(true),
  notifyEvery: integer("notify_every").notNull().default(10),
  maxConcurrentTasks: integer("max_concurrent_tasks").notNull().default(1),
  shareDelay: integer("share_delay").notNull().default(1000),
  crckDelay: integer("crck_delay").notNull().default(500),
  createDelay: integer("create_delay").notNull().default(2000),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
  updatedBy: text("updated_by"),
});

export type ToolSettings = typeof toolSettingsTable.$inferSelect;
