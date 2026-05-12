import type { TaskResult } from "@workspace/db";

export interface CreateOptions {
  count: number;
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

const TEMP_MAIL_API = "https://api.internal.temp-mail.io/api/v3/email";
const FB_REG_URL = "https://www.facebook.com/reg/submit/";

export async function runCreate(opts: CreateOptions): Promise<void> {
  const { count, delay, onResult, signal } = opts;

  for (let i = 0; i < count; i++) {
    if (signal.aborted) break;

    try {
      const result = await createAccount();
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
        detail: err instanceof Error ? err.message : "Creation failed",
        timestamp: new Date().toISOString(),
      });
    }

    if (i < count - 1 && !signal.aborted) await sleep(delay);
  }
}

async function createAccount(): Promise<{
  status: "ok" | "fail" | "no_cp" | "no_limit";
  detail: string;
}> {
  const email = await getTempEmail();
  if (!email) {
    return { status: "fail", detail: "Failed to get temp email" };
  }

  const { firstName, lastName, dob } = generateIdentity();
  const password = generatePassword();

  const regParams = new URLSearchParams({
    firstname: firstName,
    lastname: lastName,
    reg_email__: email,
    reg_email_confirmation__: email,
    reg_passwd__: password,
    birthday_day: String(dob.day),
    birthday_month: String(dob.month),
    birthday_year: String(dob.year),
    sex: Math.random() > 0.5 ? "1" : "2",
    referrer: "",
    asked_to_login: "0",
    terms: "on",
    nhc: "0",
    locale: "en_US",
    reg_instance: generateInstance(),
    notou: "1",
    websubmit: "1",
    qsstamp: "",
  });

  const res = await fetch(FB_REG_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
      Origin: "https://www.facebook.com",
      Referer: "https://www.facebook.com/",
      "Accept-Language": "en-US,en;q=0.9",
    },
    body: regParams.toString(),
    signal: AbortSignal.timeout(20000),
  });

  const text = await res.text();

  if (text.includes("checkpoint") || text.includes("Confirm Your Email") || res.url.includes("checkpoint")) {
    return {
      status: "no_cp",
      detail: `📧 ${email} | 🔒 ${password} | Checkpoint`,
    };
  }

  if (text.includes("home.php") || res.url.includes("home.php") || res.url.includes("?sk=")) {
    return {
      status: "ok",
      detail: `✅ ${email}:${password} | ${firstName} ${lastName}`,
    };
  }

  if (text.includes("email already") || text.includes("already registered")) {
    return { status: "fail", detail: `Email already used: ${email}` };
  }

  return {
    status: "fail",
    detail: `${email}:${password} | HTTP ${res.status}`,
  };
}

async function getTempEmail(): Promise<string | null> {
  try {
    const res = await fetch(`${TEMP_MAIL_API}/new`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({}),
      signal: AbortSignal.timeout(10000),
    });
    const data = await res.json() as { email?: string };
    return data.email ?? null;
  } catch {
    return `user${Date.now()}@gmail.com`;
  }
}

function generateIdentity() {
  const firstNames = ["James","Emma","Liam","Olivia","Noah","Ava","Lucas","Sophia","Mason","Isabella","Ethan","Mia","Logan","Charlotte","Aiden","Amelia"];
  const lastNames = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Wilson","Anderson","Taylor","Thomas","Moore","Jackson","Martin"];
  return {
    firstName: firstNames[Math.floor(Math.random() * firstNames.length)],
    lastName: lastNames[Math.floor(Math.random() * lastNames.length)],
    dob: {
      day: Math.floor(Math.random() * 28) + 1,
      month: Math.floor(Math.random() * 12) + 1,
      year: Math.floor(Math.random() * (2000 - 1970)) + 1970,
    },
  };
}

function generatePassword(): string {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789@#$!";
  return Array.from({ length: 12 }, () =>
    chars.charAt(Math.floor(Math.random() * chars.length))
  ).join("");
}

function generateInstance(): string {
  return Array.from({ length: 16 }, () =>
    Math.floor(Math.random() * 16).toString(16)
  ).join("");
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
