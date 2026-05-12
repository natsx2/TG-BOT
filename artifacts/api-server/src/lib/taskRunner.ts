import { db } from "@workspace/db";
import { tasksTable } from "@workspace/db";
import { eq } from "drizzle-orm";
import type { TaskResult } from "@workspace/db";
import { sendMessage } from "./telegram";
import { runShare } from "./tools/share";
import { runCrck } from "./tools/crck";
import { runCreate } from "./tools/create";
import { logger } from "./logger";
import { getSettings } from "./settings";

const activeControllers = new Map<string, AbortController>();

export function getActiveTask(telegramId: string): boolean {
  return activeControllers.has(telegramId);
}

export function stopTask(telegramId: string): boolean {
  const ctrl = activeControllers.get(telegramId);
  if (!ctrl) return false;
  ctrl.abort();
  activeControllers.delete(telegramId);
  return true;
}

export async function startTask(
  telegramId: string,
  userId: number,
  toolName: "share" | "crck" | "create",
  inputData: string
): Promise<{ taskId: number } | { error: string }> {
  if (activeControllers.has(telegramId)) {
    return { error: "You already have a running task. Use /stop to cancel it first." };
  }

  const [task] = await db
    .insert(tasksTable)
    .values({
      userId,
      telegramId,
      toolName,
      status: "running",
      inputData,
      results: [],
      totalOk: 0,
      totalFail: 0,
      totalNoCp: 0,
    })
    .returning();

  const ctrl = new AbortController();
  activeControllers.set(telegramId, ctrl);

  runTaskInBackground(task.id, telegramId, toolName, inputData, ctrl.signal);

  return { taskId: task.id };
}

async function runTaskInBackground(
  taskId: number,
  telegramId: string,
  toolName: "share" | "crck" | "create",
  inputData: string,
  signal: AbortSignal
): Promise<void> {
  const settings = await getSettings();
  const results: TaskResult[] = [];
  let totalOk = 0;
  let totalFail = 0;
  let totalNoCp = 0;
  let totalProcessed = 0;

  const onResult = async (result: TaskResult) => {
    results.push(result);
    totalProcessed++;

    if (result.status === "ok") totalOk++;
    else if (result.status === "fail") totalFail++;
    else if (result.status === "no_cp") totalNoCp++;

    await db
      .update(tasksTable)
      .set({
        results,
        totalOk,
        totalFail,
        totalNoCp,
        updatedAt: new Date(),
      })
      .where(eq(tasksTable.id, taskId));

    const shouldShow =
      (result.status === "ok" && settings.showOk) ||
      (result.status === "fail" && settings.showFail) ||
      (result.status === "no_cp" && settings.showNoCp) ||
      (result.status === "no_limit" && settings.showNoLimit);

    const isInterval = totalProcessed % settings.notifyEvery === 0;

    if (shouldShow) {
      const emoji =
        result.status === "ok" ? "✅" :
        result.status === "no_cp" ? "⚠️" :
        result.status === "no_limit" ? "♾️" : "❌";

      await sendMessage(
        telegramId,
        `${emoji} <code>${escapeHtml(result.line.substring(0, 50))}</code>\n<i>${escapeHtml(result.detail ?? "")}</i>`
      );
    }

    if (isInterval && !signal.aborted) {
      await sendMessage(
        telegramId,
        `📊 <b>Progress [#${taskId}]</b>\n` +
        `✅ OK: <b>${totalOk}</b>  ❌ Fail: <b>${totalFail}</b>  ⚠️ No-CP: <b>${totalNoCp}</b>\n` +
        `Processed: ${totalProcessed}`
      );
    }
  };

  try {
    if (toolName === "share") {
      const [cookies, postUrl, countStr] = inputData.split("||");
      await runShare({
        cookies: cookies?.trim() ?? "",
        postUrl: postUrl?.trim() ?? "",
        count: Math.min(parseInt(countStr ?? "1") || 1, 1000),
        delay: settings.shareDelay,
        onResult,
        signal,
      });
    } else if (toolName === "crck") {
      const uids = inputData.split("\n").map(l => l.trim()).filter(Boolean);
      await runCrck({
        uids,
        delay: settings.crckDelay,
        onResult,
        signal,
      });
    } else if (toolName === "create") {
      const count = Math.min(parseInt(inputData.trim()) || 1, 50);
      await runCreate({
        count,
        delay: settings.createDelay,
        onResult,
        signal,
      });
    }

    const finalStatus = signal.aborted ? "stopped" : "done";

    await db
      .update(tasksTable)
      .set({
        status: finalStatus,
        results,
        totalOk,
        totalFail,
        totalNoCp,
        updatedAt: new Date(),
        completedAt: new Date(),
      })
      .where(eq(tasksTable.id, taskId));

    activeControllers.delete(telegramId);

    const toolLabel = toolName.toUpperCase();
    const msg =
      finalStatus === "stopped"
        ? `🛑 <b>${toolLabel} Task #${taskId} Stopped</b>\n\n` +
          `✅ OK: <b>${totalOk}</b>\n❌ Fail: <b>${totalFail}</b>\n⚠️ No-CP: <b>${totalNoCp}</b>\nTotal: ${totalProcessed}`
        : `🏁 <b>${toolLabel} Task #${taskId} Complete</b>\n\n` +
          `✅ OK: <b>${totalOk}</b>\n❌ Fail: <b>${totalFail}</b>\n⚠️ No-CP: <b>${totalNoCp}</b>\nTotal: ${totalProcessed}`;

    await sendMessage(telegramId, msg);
  } catch (err) {
    logger.error({ err, taskId }, "Task runner error");
    activeControllers.delete(telegramId);

    await db
      .update(tasksTable)
      .set({
        status: "failed",
        results,
        totalOk,
        totalFail,
        totalNoCp,
        updatedAt: new Date(),
        completedAt: new Date(),
      })
      .where(eq(tasksTable.id, taskId));

    await sendMessage(telegramId, `❌ <b>Task #${taskId} failed unexpectedly.</b>\nUse /tasks to see details.`);
  }
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}
