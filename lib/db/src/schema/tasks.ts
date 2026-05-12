import { pgTable, text, serial, timestamp, pgEnum, integer, jsonb } from "drizzle-orm/pg-core";
import { botUsersTable } from "./botUsers";

export const taskStatusEnum = pgEnum("task_status", ["running", "done", "stopped", "failed"]);
export const toolNameEnum = pgEnum("tool_name", ["share", "crck", "create"]);

export const tasksTable = pgTable("tasks", {
  id: serial("id").primaryKey(),
  userId: integer("user_id").references(() => botUsersTable.id, { onDelete: "cascade" }),
  telegramId: text("telegram_id").notNull(),
  toolName: toolNameEnum("tool_name").notNull(),
  status: taskStatusEnum("status").notNull().default("running"),
  inputData: text("input_data"),
  results: jsonb("results").$type<TaskResult[]>().default([]),
  totalOk: integer("total_ok").notNull().default(0),
  totalFail: integer("total_fail").notNull().default(0),
  totalNoCp: integer("total_no_cp").notNull().default(0),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at"),
  completedAt: timestamp("completed_at"),
});

export interface TaskResult {
  line: string;
  status: "ok" | "fail" | "no_cp" | "no_limit";
  detail?: string;
  timestamp: string;
}

export type Task = typeof tasksTable.$inferSelect;
