import { logger } from "./logger";

const BOT_TOKEN = process.env.BOT_TOKEN ?? process.env.TELEGRAM_BOT_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}`;

export async function sendMessage(chatId: string | number, text: string, options?: {
  parse_mode?: "HTML" | "Markdown" | "MarkdownV2";
  reply_markup?: object;
}): Promise<void> {
  if (!BOT_TOKEN) {
    logger.warn("BOT_TOKEN not set, skipping sendMessage");
    return;
  }
  try {
    const response = await fetch(`${TELEGRAM_API}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: chatId,
        text,
        parse_mode: options?.parse_mode ?? "HTML",
        reply_markup: options?.reply_markup,
      }),
    });
    if (!response.ok) {
      const err = await response.text();
      logger.error({ chatId, err }, "Telegram sendMessage failed");
    }
  } catch (err) {
    logger.error({ err, chatId }, "Failed to send Telegram message");
  }
}

export async function answerCallbackQuery(callbackQueryId: string, text?: string): Promise<void> {
  if (!BOT_TOKEN) return;
  try {
    await fetch(`${TELEGRAM_API}/answerCallbackQuery`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ callback_query_id: callbackQueryId, text }),
    });
  } catch (err) {
    logger.error({ err }, "Failed to answer callback query");
  }
}

export async function setWebhook(webhookUrl: string): Promise<void> {
  if (!BOT_TOKEN) {
    logger.warn("BOT_TOKEN not set, skipping setWebhook");
    return;
  }
  try {
    const response = await fetch(`${TELEGRAM_API}/setWebhook`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        url: webhookUrl,
        allowed_updates: ["message", "callback_query"],
      }),
    });
    const data = await response.json() as { ok: boolean; description?: string };
    if (!data.ok) {
      logger.error({ description: data.description }, "Failed to set webhook");
    } else {
      logger.info({ webhookUrl }, "Telegram webhook set");
    }
  } catch (err) {
    logger.error({ err }, "Failed to set Telegram webhook");
  }
}

export async function setBotCommands(): Promise<void> {
  if (!BOT_TOKEN) return;
  try {
    await fetch(`${TELEGRAM_API}/setMyCommands`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        commands: [
          { command: "start", description: "🚀 Start / login" },
          { command: "status", description: "📋 Check your account status" },
          { command: "menu", description: "🔥 Open tools menu" },
          { command: "au2", description: "🔨 AU2 FM Maker (FB account creator)" },
          { command: "fbclone", description: "🔓 FB Clone brute crack" },
          { command: "spam", description: "📤 Spam Share (cookie post sharer)" },
          { command: "stop", description: "🛑 Stop running tool" },
          { command: "logout", description: "🚪 Log out" },
          { command: "help", description: "❓ Show help" },
        ],
      }),
    });
  } catch (err) {
    logger.error({ err }, "Failed to set bot commands");
  }
}

export async function deleteWebhook(): Promise<void> {
  if (!BOT_TOKEN) return;
  await fetch(`${TELEGRAM_API}/deleteWebhook`, { method: "POST" });
}
