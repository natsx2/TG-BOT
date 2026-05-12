import { Router, type IRouter } from "express";
import { db } from "@workspace/db";
import { botUsersTable, tasksTable } from "@workspace/db";
import { eq, desc } from "drizzle-orm";
import { sendMessage } from "../lib/telegram";
import { startTask, stopTask, getActiveTask } from "../lib/taskRunner";
import { logger } from "../lib/logger";

const router: IRouter = Router();

interface TelegramFrom {
  id: number;
  is_bot: boolean;
  first_name: string;
  last_name?: string;
  username?: string;
}

interface TelegramMessage {
  message_id: number;
  from?: TelegramFrom;
  chat: { id: number; type: string };
  text?: string;
}

interface TelegramCallbackQuery {
  id: string;
  from: TelegramFrom;
  message?: { chat: { id: number }; message_id: number };
  data?: string;
}

interface TelegramUpdate {
  update_id: number;
  message?: TelegramMessage;
  callback_query?: TelegramCallbackQuery;
}

// user states for multi-step input
const userStates = new Map<string, { step: string; data: Record<string, string> }>();

router.post("/bot/webhook", async (req, res) => {
  const update = req.body as TelegramUpdate;
  res.json({ success: true });

  try {
    if (update.callback_query) {
      await handleCallback(update.callback_query);
      return;
    }
    if (!update.message) return;

    const msg = update.message;
    const chatId = msg.chat.id;
    const from = msg.from;
    const text = (msg.text ?? "").trim();

    if (!from || from.is_bot) return;

    const telegramId = String(from.id);
    const firstName = from.first_name;
    const lastName = from.last_name;
    const username = from.username;

    if (text.startsWith("/start")) {
      await handleStart(chatId, telegramId, firstName, lastName, username);
    } else if (text.startsWith("/register")) {
      await handleRegister(chatId, telegramId, firstName, lastName, username, text);
    } else if (text.startsWith("/status")) {
      await handleStatus(chatId, telegramId);
    } else if (text.startsWith("/help")) {
      await handleHelp(chatId, telegramId);
    } else if (text.startsWith("/library")) {
      await handleLibrary(chatId, telegramId);
    } else if (text.startsWith("/tasks")) {
      await handleTasks(chatId, telegramId);
    } else if (text.startsWith("/agent")) {
      await handleAgent(chatId, telegramId);
    } else if (text.startsWith("/stop")) {
      await handleStop(chatId, telegramId);
    } else if (text.startsWith("/share")) {
      await handleToolStart(chatId, telegramId, "share", text);
    } else if (text.startsWith("/crck")) {
      await handleToolStart(chatId, telegramId, "crck", text);
    } else if (text.startsWith("/create")) {
      await handleToolStart(chatId, telegramId, "create", text);
    } else if (text.startsWith("/cancel")) {
      userStates.delete(telegramId);
      await sendMessage(chatId, "❌ Operation cancelled. Use /library to see available tools.");
    } else {
      await handleTextInput(chatId, telegramId, text);
    }
  } catch (err) {
    logger.error({ err }, "Webhook handler error");
  }
});

async function getApprovedUser(telegramId: string) {
  const rows = await db
    .select()
    .from(botUsersTable)
    .where(eq(botUsersTable.telegramId, telegramId))
    .limit(1);
  if (!rows.length) return null;
  const user = rows[0];
  if (user.status !== "approved") return null;
  if (user.expiresAt && new Date() > user.expiresAt) return null;
  return user;
}

async function handleStart(
  chatId: number,
  telegramId: string,
  firstName: string,
  lastName?: string,
  username?: string
): Promise<void> {
  const rows = await db
    .select()
    .from(botUsersTable)
    .where(eq(botUsersTable.telegramId, telegramId))
    .limit(1);

  if (!rows.length) {
    await sendMessage(
      chatId,
      `👋 <b>Welcome, ${firstName}!</b>\n\n` +
      `🔐 This bot requires registration.\n\n` +
      `<b>How to get started:</b>\n` +
      `1️⃣ Use /register to submit your request\n` +
      `2️⃣ Wait for admin approval\n` +
      `3️⃣ Once approved, access tools via /library\n\n` +
      `📋 Check your status anytime with /status`,
      {
        reply_markup: {
          inline_keyboard: [[{ text: "📝 Register Now", callback_data: "action:register" }]],
        },
      }
    );
    return;
  }

  const user = rows[0];
  if (user.status === "approved") {
    const expired = user.expiresAt && new Date() > user.expiresAt;
    if (expired) {
      await sendMessage(chatId, `⏰ <b>Access Expired</b>\n\nHi ${firstName}, your access has expired. Contact an admin to renew.`);
      return;
    }
    await sendMessage(
      chatId,
      `✅ <b>Welcome back, ${firstName}!</b>\n\n` +
      `Your account is active. Use the tools below:`,
      {
        reply_markup: {
          inline_keyboard: [
            [{ text: "📚 Library", callback_data: "menu:library" }, { text: "📋 My Tasks", callback_data: "menu:tasks" }],
            [{ text: "🤖 Agent", callback_data: "menu:agent" }, { text: "❓ Help", callback_data: "menu:help" }],
          ],
        },
      }
    );
  } else if (user.status === "pending") {
    await sendMessage(chatId, `⏳ <b>Pending Approval</b>\n\nHi ${firstName}, your registration is under review.\n\nYou'll be notified once approved.`);
  } else {
    await sendMessage(chatId, `❌ <b>Access Rejected</b>\n\nYour registration was rejected.\n\nUse /register to re-apply.`);
  }
}

async function handleRegister(
  chatId: number,
  telegramId: string,
  firstName: string,
  lastName?: string,
  username?: string,
  text?: string
): Promise<void> {
  const rows = await db
    .select()
    .from(botUsersTable)
    .where(eq(botUsersTable.telegramId, telegramId))
    .limit(1);

  if (rows.length > 0 && rows[0].status === "approved") {
    await sendMessage(chatId, `✅ Already approved! Use /library to access tools.`);
    return;
  }
  if (rows.length > 0 && rows[0].status === "pending") {
    await sendMessage(chatId, `⏳ Already pending review. Use /status to check.`);
    return;
  }

  const bio = text && text.length > "/register".length ? text.slice("/register".length).trim() : undefined;

  if (rows.length > 0) {
    await db.update(botUsersTable).set({
      status: "pending", firstName, lastName: lastName ?? null,
      username: username ?? null, bio: bio ?? null, updatedAt: new Date(), rejectionReason: null,
    }).where(eq(botUsersTable.telegramId, telegramId));
  } else {
    await db.insert(botUsersTable).values({
      telegramId, firstName, lastName: lastName ?? null,
      username: username ?? null, status: "pending", bio: bio ?? null,
    });
  }

  await sendMessage(
    chatId,
    `📝 <b>Registration Submitted!</b>\n\n` +
    `👤 Name: ${firstName}${lastName ? " " + lastName : ""}\n` +
    `🔗 Username: ${username ? "@" + username : "Not set"}\n` +
    `🆔 ID: <code>${telegramId}</code>\n\n` +
    `You'll receive a notification when reviewed.`
  );
}

async function handleStatus(chatId: number, telegramId: string): Promise<void> {
  const rows = await db.select().from(botUsersTable).where(eq(botUsersTable.telegramId, telegramId)).limit(1);
  if (!rows.length) {
    await sendMessage(chatId, `📋 Not registered yet. Use /register to apply.`);
    return;
  }
  const user = rows[0];
  const emoji: Record<string, string> = { pending: "⏳", approved: "✅", rejected: "❌" };
  const label: Record<string, string> = { pending: "Pending Review", approved: "Approved ✅", rejected: "Rejected ❌" };
  let msg =
    `📋 <b>Account Status</b>\n\n` +
    `${emoji[user.status]} ${label[user.status]}\n` +
    `👤 ${user.firstName}${user.lastName ? " " + user.lastName : ""}\n` +
    `🆔 <code>${user.telegramId}</code>\n` +
    `📅 Joined: ${user.createdAt.toDateString()}`;

  if (user.expiresAt) {
    const expired = new Date() > user.expiresAt;
    msg += `\n⏰ Access ${expired ? "Expired" : "Expires"}: ${user.expiresAt.toDateString()}`;
  }
  if (user.status === "rejected" && user.rejectionReason) {
    msg += `\n\n❗ Reason: ${user.rejectionReason}`;
  }
  if (user.status === "rejected") {
    msg += `\n\nUse /register to re-apply.`;
  }
  await sendMessage(chatId, msg);
}

async function handleHelp(chatId: number, telegramId: string): Promise<void> {
  const user = await getApprovedUser(telegramId);
  const toolCommands = user
    ? `\n\n<b>🛠 Tools (Approved Only)</b>\n` +
      `/share — Facebook Post Sharer\n` +
      `/crck — Account Checker\n` +
      `/create — Account Creator\n` +
      `/stop — Stop running task\n`
    : "";

  await sendMessage(
    chatId,
    `🤖 <b>Bot Commands</b>\n\n` +
    `<b>📌 General</b>\n` +
    `/start — Start the bot\n` +
    `/register — Submit registration\n` +
    `/status — Check your status\n` +
    `/help — This message\n` +
    `/library — Tool library\n` +
    `/tasks — Your task history\n` +
    `/agent — Bot assistant` +
    toolCommands
  );
}

async function handleLibrary(chatId: number, telegramId: string): Promise<void> {
  const user = await getApprovedUser(telegramId);
  if (!user) {
    await sendMessage(chatId, `🔒 <b>Access Denied</b>\n\nYou need to be approved to access the library.\n\nUse /register to apply.`);
    return;
  }

  await sendMessage(
    chatId,
    `📚 <b>Tool Library</b>\n\n` +
    `Select a tool to use:\n\n` +
    `🔵 <b>SHARE</b> — Facebook post sharer\n` +
    `🔴 <b>CRCK</b> — Account checker/cracker\n` +
    `🟢 <b>CREATE</b> — Account creator\n\n` +
    `Tap a button to start:`,
    {
      reply_markup: {
        inline_keyboard: [
          [
            { text: "🔵 SHARE", callback_data: "tool:share" },
            { text: "🔴 CRCK", callback_data: "tool:crck" },
            { text: "🟢 CREATE", callback_data: "tool:create" },
          ],
          [{ text: "📋 My Tasks", callback_data: "menu:tasks" }],
        ],
      },
    }
  );
}

async function handleTasks(chatId: number, telegramId: string): Promise<void> {
  const user = await getApprovedUser(telegramId);
  if (!user) {
    await sendMessage(chatId, `🔒 Access denied. Use /register to apply.`);
    return;
  }

  const tasks = await db
    .select()
    .from(tasksTable)
    .where(eq(tasksTable.telegramId, telegramId))
    .orderBy(desc(tasksTable.createdAt))
    .limit(10);

  if (!tasks.length) {
    await sendMessage(chatId, `📋 <b>My Tasks</b>\n\nNo tasks yet. Use /library to start a tool.`);
    return;
  }

  const statusEmoji: Record<string, string> = {
    running: "⚙️", done: "✅", stopped: "🛑", failed: "❌",
  };

  let msg = `📋 <b>My Tasks (Last 10)</b>\n\n`;
  for (const t of tasks) {
    msg += `${statusEmoji[t.status] ?? "❓"} <b>#${t.id}</b> ${t.toolName.toUpperCase()} — ${t.status}\n`;
    msg += `   ✅${t.totalOk} ❌${t.totalFail} ⚠️${t.totalNoCp} | ${t.createdAt.toDateString()}\n`;
  }

  const hasRunning = getActiveTask(telegramId);
  const keyboard = hasRunning ? [[{ text: "🛑 Stop Running Task", callback_data: "action:stop" }]] : [];

  await sendMessage(chatId, msg, { reply_markup: { inline_keyboard: keyboard } });
}

async function handleAgent(chatId: number, telegramId: string): Promise<void> {
  await sendMessage(
    chatId,
    `🤖 <b>Agent Panel</b>\n\n` +
    `I'm your tool assistant. Here's what I can do:\n\n` +
    `📊 <b>SHARE</b> — Share Facebook posts using your cookie\n` +
    `🔍 <b>CRCK</b> — Check email:password combos\n` +
    `🏗 <b>CREATE</b> — Auto-create Facebook accounts\n\n` +
    `<b>Quick Commands:</b>\n` +
    `/library — Browse all tools\n` +
    `/tasks — View your task history\n` +
    `/stop — Stop a running task\n\n` +
    `<b>Tips:</b>\n` +
    `• Each tool runs in the background\n` +
    `• You get live results as they come in\n` +
    `• Use /stop anytime to cancel\n` +
    `• Admins can customize output display`,
    {
      reply_markup: {
        inline_keyboard: [
          [{ text: "📚 Open Library", callback_data: "menu:library" }],
          [{ text: "📋 View Tasks", callback_data: "menu:tasks" }],
        ],
      },
    }
  );
}

async function handleStop(chatId: number, telegramId: string): Promise<void> {
  const stopped = stopTask(telegramId);
  if (stopped) {
    await sendMessage(chatId, `🛑 <b>Task stopping...</b>\n\nYour running task has been signalled to stop. Final results will be sent shortly.`);
  } else {
    await sendMessage(chatId, `ℹ️ No running task to stop. Use /library to start a tool.`);
  }
}

async function handleToolStart(
  chatId: number,
  telegramId: string,
  tool: "share" | "crck" | "create",
  text: string
): Promise<void> {
  const user = await getApprovedUser(telegramId);
  if (!user) {
    await sendMessage(chatId, `🔒 <b>Access Denied</b>\n\nYou must be approved to use this tool.\n\nUse /register to apply.`);
    return;
  }

  if (tool === "share") {
    userStates.set(telegramId, { step: "share_cookies", data: {} });
    await sendMessage(chatId,
      `🔵 <b>SHARE Tool</b>\n\n` +
      `Step 1/3: Send your Facebook <b>cookie string</b>\n\n` +
      `<i>Example: c_user=123; xs=abc; datr=xyz</i>\n\n` +
      `Send /cancel to abort.`
    );
  } else if (tool === "crck") {
    userStates.set(telegramId, { step: "crck_combos", data: {} });
    await sendMessage(chatId,
      `🔴 <b>CRCK Tool</b>\n\n` +
      `Send your combos (one per line):\n\n` +
      `<code>email@example.com:password123\nemail2@example.com:pass456</code>\n\n` +
      `Max 500 combos per run. Send /cancel to abort.`
    );
  } else if (tool === "create") {
    userStates.set(telegramId, { step: "create_count", data: {} });
    await sendMessage(chatId,
      `🟢 <b>CREATE Tool</b>\n\n` +
      `How many accounts to create? (1–50)\n\n` +
      `Send /cancel to abort.`
    );
  }
}

async function handleTextInput(chatId: number, telegramId: string, text: string): Promise<void> {
  const state = userStates.get(telegramId);
  if (!state) {
    await sendMessage(chatId, `Use /help to see available commands.`);
    return;
  }

  const user = await getApprovedUser(telegramId);
  if (!user) {
    userStates.delete(telegramId);
    await sendMessage(chatId, `🔒 Access denied. Use /register to apply.`);
    return;
  }

  if (state.step === "share_cookies") {
    state.data["cookies"] = text;
    state.step = "share_posturl";
    userStates.set(telegramId, state);
    await sendMessage(chatId, `Step 2/3: Send the <b>Facebook post URL</b> to share:\n\n<i>Example: https://www.facebook.com/photo?fbid=123456</i>`);
  } else if (state.step === "share_posturl") {
    state.data["postUrl"] = text;
    state.step = "share_count";
    userStates.set(telegramId, state);
    await sendMessage(chatId, `Step 3/3: How many times to share? (1–1000)`);
  } else if (state.step === "share_count") {
    const count = Math.min(parseInt(text) || 1, 1000);
    const { cookies, postUrl } = state.data;
    userStates.delete(telegramId);

    const result = await startTask(
      telegramId, user.id, "share",
      `${cookies}||${postUrl}||${count}`
    );

    if ("error" in result) {
      await sendMessage(chatId, `❌ ${result.error}`);
    } else {
      await sendMessage(chatId,
        `🔵 <b>SHARE Started! [#${result.taskId}]</b>\n\n` +
        `📌 Post: <code>${postUrl.substring(0, 50)}</code>\n` +
        `🔁 Count: ${count}\n\n` +
        `Results will appear as they come in.\nUse /stop to cancel.`
      );
    }
  } else if (state.step === "crck_combos") {
    const lines = text.split("\n").filter(Boolean);
    if (lines.length === 0) {
      await sendMessage(chatId, `❌ No combos found. Send in format email:password`);
      return;
    }
    userStates.delete(telegramId);

    const result = await startTask(telegramId, user.id, "crck", text);
    if ("error" in result) {
      await sendMessage(chatId, `❌ ${result.error}`);
    } else {
      await sendMessage(chatId,
        `🔴 <b>CRCK Started! [#${result.taskId}]</b>\n\n` +
        `📦 Loaded: ${lines.length} combos\n\n` +
        `Results appear live. Use /stop to cancel.`
      );
    }
  } else if (state.step === "create_count") {
    const count = Math.min(Math.max(parseInt(text) || 1, 1), 50);
    userStates.delete(telegramId);

    const result = await startTask(telegramId, user.id, "create", String(count));
    if ("error" in result) {
      await sendMessage(chatId, `❌ ${result.error}`);
    } else {
      await sendMessage(chatId,
        `🟢 <b>CREATE Started! [#${result.taskId}]</b>\n\n` +
        `🏗 Creating ${count} accounts...\n\n` +
        `Results appear live. Use /stop to cancel.`
      );
    }
  }
}

async function handleCallback(cq: TelegramCallbackQuery): Promise<void> {
  const chatId = cq.message?.chat.id;
  if (!chatId) return;
  const telegramId = String(cq.from.id);
  const data = cq.data ?? "";

  const { answerCallbackQuery } = await import("../lib/telegram");
  await answerCallbackQuery(cq.id);

  if (data === "menu:library" || data === "action:library") {
    await handleLibrary(chatId, telegramId);
  } else if (data === "menu:tasks") {
    await handleTasks(chatId, telegramId);
  } else if (data === "menu:agent") {
    await handleAgent(chatId, telegramId);
  } else if (data === "menu:help") {
    await handleHelp(chatId, telegramId);
  } else if (data === "action:register") {
    const from = cq.from;
    await handleRegister(chatId, telegramId, from.first_name, from.last_name, from.username);
  } else if (data === "action:stop") {
    await handleStop(chatId, telegramId);
  } else if (data === "tool:share") {
    await handleToolStart(chatId, telegramId, "share", "/share");
  } else if (data === "tool:crck") {
    await handleToolStart(chatId, telegramId, "crck", "/crck");
  } else if (data === "tool:create") {
    await handleToolStart(chatId, telegramId, "create", "/create");
  }
}

export default router;
