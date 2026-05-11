#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BruteTG — Telegram Bot with Admin-Approved Access
Keep-alive: pings /api/healthz every 14 min so Render never sleeps.
"""

import os
import sys
import logging
import threading
import time
import requests
from functools import wraps
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)

# ─── Config ────────────────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_BASE  = os.environ.get("API_BASE_URL", "http://localhost:80/api")
SELF_URL  = os.environ.get("SELF_URL", "")   # e.g. https://your-app.onrender.com/api/healthz

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

# ─── Conversation states ────────────────────────────────────────────────────────
(
    STATE_IDLE,
    STATE_AWAIT_USERNAME,
    STATE_AWAIT_PASSWORD,
    STATE_AUTHENTICATED,
) = range(4)

# ─── In-memory sessions  (telegramId → {username, verified, expiresAt}) ────────
sessions: dict[str, dict] = {}


# ─── Keep-alive thread ─────────────────────────────────────────────────────────
def keep_alive():
    """Ping the health endpoint every 14 minutes so Render free tier stays awake."""
    ping_url = SELF_URL or f"{API_BASE}/healthz"
    while True:
        time.sleep(14 * 60)
        try:
            r = requests.get(ping_url, timeout=15)
            log.info("Keep-alive ping → %s  status=%s", ping_url, r.status_code)
        except Exception as exc:
            log.warning("Keep-alive ping failed: %s", exc)


# ─── API helpers ───────────────────────────────────────────────────────────────
def api(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{API_BASE}{path}"
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except requests.RequestException as exc:
        log.error("API request failed: %s", exc)
        raise


def register_user(tg_id, tg_username, first, last):
    return api("POST", "/users/register", json={
        "telegramId": tg_id,
        "telegramUsername": tg_username or "",
        "firstName": first or "",
        "lastName": last or "",
    })


def check_status(tg_id):
    return api("GET", f"/bot/status/{tg_id}")


def verify_credentials(tg_id, username, password):
    return api("POST", "/bot/verify", json={
        "telegramId": tg_id,
        "accessUsername": username,
        "accessPassword": password,
    })


# ─── Decorators ────────────────────────────────────────────────────────────────
def requires_auth(func):
    @wraps(func)
    async def wrapper(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        tg_id = str(update.effective_user.id)
        if not sessions.get(tg_id, {}).get("verified"):
            await update.message.reply_text(
                "You are not authenticated.\n"
                "Send /start to register or log in."
            )
            return ConversationHandler.END
        return await func(update, ctx)
    return wrapper


# ─── Main keyboard ─────────────────────────────────────────────────────────────
def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Tools Menu"), KeyboardButton("My Status")],
            [KeyboardButton("Log Out")],
        ],
        resize_keyboard=True,
    )


# ─── /start ────────────────────────────────────────────────────────────────────
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    user  = update.effective_user
    tg_id = str(user.id)
    name  = user.first_name or "User"

    sessions.pop(tg_id, None)

    await update.message.reply_text(
        f"Welcome to BruteTG, {name}!\n\n"
        "Checking your registration status..."
    )

    try:
        r = check_status(tg_id)
    except Exception:
        await update.message.reply_text("Could not reach the server. Please try again later.")
        return STATE_IDLE

    if r.status_code == 404:
        try:
            reg = register_user(tg_id, user.username, user.first_name, user.last_name)
        except Exception:
            await update.message.reply_text("Registration failed. Try again later.")
            return STATE_IDLE

        if reg.status_code not in (201, 409):
            await update.message.reply_text(
                f"Registration error ({reg.status_code}). Contact admin."
            )
            return STATE_IDLE

        await update.message.reply_text(
            "Registration submitted!\n\n"
            "An admin will review and approve your account.\n"
            "Once approved you will receive credentials to log in.\n\n"
            "Use /status to check your approval status anytime."
        )
        return STATE_IDLE

    data   = r.json()
    status = data.get("status")

    if status == "pending":
        await update.message.reply_text(
            "Your account is pending admin approval.\n"
            "Use /status to check again."
        )
        return STATE_IDLE

    if status == "rejected":
        await update.message.reply_text(
            "Your access request was rejected.\n"
            "Contact the admin for more information."
        )
        return STATE_IDLE

    if status == "approved":
        await update.message.reply_text(
            "Your account is approved!\n\n"
            "Please enter your bot username:"
        )
        return STATE_AWAIT_USERNAME

    await update.message.reply_text(f"Unknown status: {status}. Contact admin.")
    return STATE_IDLE


# ─── Login flow ─────────────────────────────────────────────────────────────────
async def recv_username(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["login_username"] = update.message.text.strip()
    await update.message.reply_text("Now enter your bot password:")
    return STATE_AWAIT_PASSWORD


async def recv_password(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = ctx.user_data.get("login_username", "")
    password = update.message.text.strip()

    try:
        await update.message.delete()
    except Exception:
        pass

    try:
        r = verify_credentials(tg_id, username, password)
    except Exception:
        await update.message.reply_text("Server error. Try again.")
        return STATE_IDLE

    if r.status_code != 200:
        err = r.json().get("error", "Invalid credentials or expired access.")
        await update.message.reply_text(
            f"Access denied: {err}\n\nUse /start to try again."
        )
        return STATE_IDLE

    result = r.json()
    sessions[tg_id] = {
        "verified": True,
        "username": username,
        "expiresAt": result.get("expiresAt"),
    }

    expiry_msg = ""
    if result.get("expiresAt"):
        expiry_msg = f"\nAccess expires: {result['expiresAt'][:10]}"

    await update.message.reply_text(
        f"Authenticated successfully, {username}!{expiry_msg}\n\n"
        "Use /menu to see available tools.",
        reply_markup=main_keyboard(),
    )
    return STATE_AUTHENTICATED


# ─── /status ───────────────────────────────────────────────────────────────────
async def cmd_status(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = str(update.effective_user.id)
    try:
        r = check_status(tg_id)
    except Exception:
        await update.message.reply_text("Cannot reach server.")
        return

    if r.status_code == 404:
        await update.message.reply_text("You are not registered. Send /start to register.")
        return

    data      = r.json()
    status    = data.get("status", "unknown")
    session   = sessions.get(tg_id)
    logged_in = "Yes" if session and session.get("verified") else "No"

    msg = (
        f"Telegram ID: {tg_id}\n"
        f"Approval status: {status.upper()}\n"
        f"Logged in: {logged_in}"
    )
    if session and session.get("expiresAt"):
        msg += f"\nExpires: {session['expiresAt'][:19]}"
    await update.message.reply_text(msg)


# ─── /menu ──────────────────────────────────────────────────────────────────────
async def cmd_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("Not authenticated. Use /start to log in.")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("AU2 FM Maker", callback_data="tool_au2")],
        [InlineKeyboardButton("FB Clone", callback_data="tool_fbclone")],
        [InlineKeyboardButton("NIKA Post Sharer", callback_data="tool_nika")],
        [InlineKeyboardButton("My Status", callback_data="tool_status")],
    ])
    await update.message.reply_text("Select a tool:", reply_markup=keyboard)


# ─── /help ──────────────────────────────────────────────────────────────────────
async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "BruteTG — Available commands:\n\n"
        "/start   — Register or log in\n"
        "/status  — Check your approval status\n"
        "/menu    — Open the tools menu (requires login)\n"
        "/au2     — AU2 FM Maker tool\n"
        "/fbclone — FB Clone tool\n"
        "/nika    — NIKA Post Sharer tool\n"
        "/logout  — Log out of your session\n"
        "/help    — Show this help message"
    )


# ─── Keyboard button handler ────────────────────────────────────────────────────
async def handle_keyboard(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    text  = update.message.text
    tg_id = str(update.effective_user.id)

    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("Not authenticated. Use /start.")
        return

    if text == "Tools Menu":
        await cmd_menu(update, ctx)
    elif text == "My Status":
        await cmd_status(update, ctx)
    elif text == "Log Out":
        sessions.pop(tg_id, None)
        await update.message.reply_text(
            "Logged out. Send /start to log in again.",
            reply_markup=ReplyKeyboardRemove(),
        )


# ─── Inline callback handler ────────────────────────────────────────────────────
async def handle_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    tg_id = str(query.from_user.id)

    if not sessions.get(tg_id, {}).get("verified"):
        await query.edit_message_text("Session expired. Use /start to log in.")
        return

    data = query.data

    if data == "tool_au2":
        await query.edit_message_text(
            "AU2 FM Maker — Premium Edition\n\n"
            "Features:\n"
            "- Facebook account creator\n"
            "- 2FA manager\n"
            "- Cookie extractor\n\n"
            "Send /au2 to start."
        )
    elif data == "tool_fbclone":
        await query.edit_message_text(
            "FB Clone Tool\n\n"
            "Features:\n"
            "- Clone Facebook profiles\n"
            "- Batch operations\n\n"
            "Send /fbclone to start."
        )
    elif data == "tool_nika":
        await query.edit_message_text(
            "NIKA Post Sharer\n\n"
            "Features:\n"
            "- Share posts across groups\n"
            "- Thread pool executor\n\n"
            "Send /nika to start."
        )
    elif data == "tool_status":
        session = sessions.get(tg_id, {})
        expiry  = session.get("expiresAt", "Permanent")
        if expiry and expiry != "Permanent":
            expiry = expiry[:19]
        await query.edit_message_text(
            f"Logged in as: {session.get('username', 'N/A')}\n"
            f"Expires: {expiry}"
        )
    elif data.startswith("au2_back"):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("AU2 FM Maker", callback_data="tool_au2")],
            [InlineKeyboardButton("FB Clone", callback_data="tool_fbclone")],
            [InlineKeyboardButton("NIKA Post Sharer", callback_data="tool_nika")],
            [InlineKeyboardButton("My Status", callback_data="tool_status")],
        ])
        await query.edit_message_text("Select a tool:", reply_markup=keyboard)


# ─── Tool commands (auth-gated) ─────────────────────────────────────────────────
@requires_auth
async def cmd_au2(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Create Account", callback_data="au2_create")],
        [InlineKeyboardButton("Manage 2FA", callback_data="au2_2fa")],
        [InlineKeyboardButton("Extract Cookies", callback_data="au2_cookie")],
        [InlineKeyboardButton("Back to Menu", callback_data="au2_back")],
    ])
    await update.message.reply_text(
        "AU2 FM Maker — Premium Edition\n\n"
        "Choose an action:",
        reply_markup=keyboard,
    )


@requires_auth
async def cmd_fbclone(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "FB Clone Tool started.\n\n"
        "Send a Facebook profile URL to clone.\n\n"
        "Example: https://facebook.com/username\n\n"
        "Type /menu to go back."
    )


@requires_auth
async def cmd_nika(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "NIKA Post Sharer started.\n\n"
        "Send a post URL followed by group IDs to begin sharing.\n\n"
        "Format:\n"
        "URL: https://facebook.com/post/...\n"
        "Groups: group1,group2,group3\n\n"
        "Type /menu to go back."
    )


# ─── /logout ───────────────────────────────────────────────────────────────────
async def cmd_logout(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    sessions.pop(tg_id, None)
    await update.message.reply_text(
        "Logged out successfully. Send /start to log in again.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


# ─── Fallback for unknown text (in conversation) ────────────────────────────────
async def fallback_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text(
            "Use /start to register or log in.\n"
            "Type /help for a list of commands."
        )
    else:
        await update.message.reply_text(
            "Unknown command. Use /menu to see tools or /help for commands."
        )


# ─── Main ──────────────────────────────────────────────────────────────────────
def main():
    if not BOT_TOKEN:
        log.error("BOT_TOKEN environment variable is not set!")
        sys.exit(1)

    # Start keep-alive thread
    t = threading.Thread(target=keep_alive, daemon=True)
    t.start()
    log.info("Keep-alive thread started")

    app = Application.builder().token(BOT_TOKEN).build()

    # Conversation handler for login flow
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", cmd_start)],
        states={
            STATE_IDLE: [
                CommandHandler("start", cmd_start),
                CommandHandler("status", cmd_status),
                CommandHandler("help", cmd_help),
            ],
            STATE_AWAIT_USERNAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, recv_username),
            ],
            STATE_AWAIT_PASSWORD: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, recv_password),
            ],
            STATE_AUTHENTICATED: [
                CommandHandler("menu", cmd_menu),
                CommandHandler("status", cmd_status),
                CommandHandler("logout", cmd_logout),
                CommandHandler("au2", cmd_au2),
                CommandHandler("fbclone", cmd_fbclone),
                CommandHandler("nika", cmd_nika),
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    handle_keyboard,
                ),
            ],
        },
        fallbacks=[CommandHandler("logout", cmd_logout)],
        allow_reentry=True,
    )

    app.add_handler(conv)
    app.add_handler(CallbackQueryHandler(handle_callback))

    # Global command handlers (work outside conversation)
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("menu", cmd_menu))
    app.add_handler(CommandHandler("au2", cmd_au2))
    app.add_handler(CommandHandler("fbclone", cmd_fbclone))
    app.add_handler(CommandHandler("nika", cmd_nika))
    app.add_handler(CommandHandler("logout", cmd_logout))

    # Catch-all for any text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback_message))

    log.info("BruteTG bot is starting polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
