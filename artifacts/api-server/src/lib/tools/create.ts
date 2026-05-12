import type { TaskResult } from "@workspace/db";

export interface CreateOptions {
  count: number;
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

const FB_REG_URL = "https://x.facebook.com/reg";
const FB_SUBMIT_URL = "https://www.facebook.com/reg/submit/";

const SINGLE_NAMES = [
  "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Michelle","Sheila",
  "Maricel","Marites","Jennifer","Jenny","Jessica","Katherine","Karen","Camille",
  "Bianca","Patricia","Aileen","Irene","Hazel","Cherry","Lovely","Princess",
  "Elizabeth","Isabel","Bella","Andrea","Alexandra","Nina","Mika","Janelle",
  "Janice","Joyce","Julie","Juliana","Faith","Hope","Rachel","Sarah","Sophia",
  "Stephanie","Tiffany","Vanessa","Veronica","Louise","Lorraine","Lani",
  "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Jonathan","Nathan","Michael",
  "Daniel","David","Andrew","Anthony","Carlo","Carlos","Christian","Christopher",
  "Dennis","Diego","Edward","Francis","Gabriel","Henry","Ian","James","Joel",
  "Joshua","Kenneth","Kevin","Kyle","Lawrence","Leo","Lucas","Marco","Martin",
  "Matthew","Patrick","Raymond","Richard","Robert","Ronald","Ryan","Samuel",
  "Thomas","Victor","Vincent","William","Xavier","Marcus","Blake","Logan","Mason",
];

const MOBILE_UA_LIST = [
  "Mozilla/5.0 (Linux; Android 10; CPH2461 Build/TKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X6823) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2211133G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A515F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36",
];

function randomUA(): string {
  return MOBILE_UA_LIST[Math.floor(Math.random() * MOBILE_UA_LIST.length)];
}

function randomName(): string {
  return SINGLE_NAMES[Math.floor(Math.random() * SINGLE_NAMES.length)];
}

function randomPhone(): string {
  const prefixes = ["017", "019", "018", "016", "015", "013", "014"];
  const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
  const suffix = Array.from({ length: 7 }, () => Math.floor(Math.random() * 10)).join("");
  return prefix + suffix;
}

function randomPassword(): string {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789@#$!";
  const len = 8 + Math.floor(Math.random() * 4);
  return Array.from({ length: len }, () => chars[Math.floor(Math.random() * chars.length)]).join("");
}

function extractFormField(html: string, name: string): string {
  const patterns = [
    new RegExp(`name="${name}"[^>]*value="([^"]*)"`, "i"),
    new RegExp(`name='${name}'[^>]*value='([^']*)'`, "i"),
    new RegExp(`value="([^"]*)"[^>]*name="${name}"`, "i"),
    new RegExp(`"${name}":"([^"]*)"`, "i"),
  ];
  for (const p of patterns) {
    const m = html.match(p);
    if (m?.[1] !== undefined) return m[1];
  }
  return "";
}

function extractAllFormFields(html: string): Record<string, string> {
  const fields: Record<string, string> = {};
  const inputRe = /<input[^>]+>/gi;
  let m: RegExpExecArray | null;
  while ((m = inputRe.exec(html)) !== null) {
    const tag = m[0];
    const nameMatch = tag.match(/name="([^"]+)"/i) ?? tag.match(/name='([^']+)'/i);
    const valMatch = tag.match(/value="([^"]*)"/i) ?? tag.match(/value='([^']*)'/i);
    if (nameMatch?.[1]) {
      fields[nameMatch[1]] = valMatch?.[1] ?? "";
    }
  }
  return fields;
}

async function createFBAccount(): Promise<{
  status: "ok" | "fail" | "no_cp" | "no_limit";
  detail: string;
}> {
  const ua = randomUA();
  const name = randomName();
  const phone = randomPhone();
  const password = randomPassword();
  const day = String(20 + Math.floor(Math.random() * 8));
  const month = String(5 + Math.floor(Math.random() * 8));
  const year = String(1990 + Math.floor(Math.random() * 12));

  const hdrs: Record<string, string> = {
    "Host": "m.facebook.com",
    "Connection": "keep-alive",
    "User-Agent": ua,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
  };

  let formFields: Record<string, string> = {};
  try {
    const regRes = await fetch(FB_REG_URL, {
      headers: hdrs,
      signal: AbortSignal.timeout(15000),
      redirect: "follow",
    });
    const html = await regRes.text();
    formFields = extractAllFormFields(html);
  } catch {
    return { status: "fail", detail: "❌ Failed to load registration page" };
  }

  const encpass = `#PWD_BROWSER:0:${Math.floor(Date.now() / 1000)}:${password}`;

  const payload: Record<string, string> = {
    ccp: "2",
    reg_instance: formFields["reg_instance"] ?? "",
    submission_request: "true",
    reg_impression_id: formFields["reg_impression_id"] ?? "",
    ns: "1",
    logger_id: formFields["logger_id"] ?? "",
    firstname: name,
    lastname: name,
    birthday_day: day,
    birthday_month: month,
    birthday_year: year,
    reg_email__: phone,
    sex: "1",
    encpass,
    submit: "Sign Up",
    fb_dtsg: formFields["fb_dtsg"] ?? extractFormField(formFields.toString?.() ?? "", "fb_dtsg"),
    jazoest: formFields["jazoest"] ?? "",
    lsd: formFields["lsd"] ?? "",
  };

  const submitHdrs: Record<string, string> = {
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://mbasic.facebook.com/reg/",
    "sec-ch-ua": "",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": ua,
    "content-type": "application/x-www-form-urlencoded",
  };

  let cookies: Record<string, string> = {};
  let responseUrl = "";
  try {
    const subRes = await fetch(FB_SUBMIT_URL, {
      method: "POST",
      headers: submitHdrs,
      body: new URLSearchParams(payload).toString(),
      signal: AbortSignal.timeout(20000),
      redirect: "follow",
    });
    responseUrl = subRes.url;
    const setCookieHeaders = subRes.headers.getSetCookie?.() ?? [];
    for (const c of setCookieHeaders) {
      const [kv] = c.split(";");
      const [k, ...v] = (kv ?? "").split("=");
      if (k?.trim()) cookies[k.trim()] = v.join("=").trim();
    }
    if (!Object.keys(cookies).length) {
      const text = await subRes.text();
      const cookieMatch = text.match(/c_user=(\d+)/);
      if (cookieMatch) cookies["c_user"] = cookieMatch[1];
      if (text.includes("checkpoint") || responseUrl.includes("checkpoint")) {
        return { status: "no_cp", detail: `⚠️ CP | ${name} | ${phone} | ${password}` };
      }
    }
  } catch {
    return { status: "fail", detail: `❌ Submit failed | ${phone}` };
  }

  if (cookies["c_user"]) {
    const uid = cookies["c_user"];
    const cookieStr = Object.entries(cookies).map(([k, v]) => `${k}=${v}`).join("; ");
    return {
      status: "ok",
      detail: `✅ OK | UID: ${uid} | ${name} | ${phone}:${password}\n<code>${cookieStr.substring(0, 120)}</code>`,
    };
  }

  if ("checkpoint" in cookies || responseUrl.includes("checkpoint")) {
    return { status: "no_cp", detail: `⚠️ CP | ${name} | ${phone} | ${password}` };
  }

  return { status: "fail", detail: `❌ FAIL | ${name} | ${phone} | ${password}` };
}

export async function runCreate(opts: CreateOptions): Promise<void> {
  const { count, delay, onResult, signal } = opts;

  for (let i = 0; i < count; i++) {
    if (signal.aborted) break;

    try {
      const result = await createFBAccount();
      await onResult({
        line: `Account #${i + 1}`,
        status: result.status,
        detail: result.detail,
        timestamp: new Date().toISOString(),
      });
    } catch (err) {
      await onResult({
        line: `Account #${i + 1}`,
        status: "fail",
        detail: `❌ Error: ${err instanceof Error ? err.message : "Unknown"}`,
        timestamp: new Date().toISOString(),
      });
    }

    if (i < count - 1 && !signal.aborted) await sleep(delay || 1000);
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
