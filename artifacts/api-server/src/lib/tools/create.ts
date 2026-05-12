import type { TaskResult } from "@workspace/db";

export interface CreateOptions {
  count: number;
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

// Decoded from Python _c5 / _c6
const FB_REG_URL = "https://x.facebook.com/reg";
const FB_SUBMIT_URL = "https://www.facebook.com/reg/submit/";

// Exact name pool from Python
const SINGLE_NAMES = [
  "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Kristine","Michelle","Sheila",
  "Maricel","Marites","Maribel","Marjorie","Jennifer","Jenny","Jessa","Jessica","Janine",
  "Katherine","Catherine","Kathleen","Karen","Karla","Camille","Bianca","Patricia","Patty",
  "Aileen","Eileen","Irene","Iris","Hazel","Cherry","Lovely","Honey","Princess","Angelica",
  "Bernadette","Rowena","Rosalie","Roselyn","Rosalinda","Lourdes","Teresa","Carmela","Carmen",
  "Liza","Elizabeth","Beth","Isabel","Bella","Andrea","Andi","Alexandra","Alexa","Nina",
  "Mina","Rina","Jocelyn","Jocelle","Jhoanna","Joan","Joanne","Joanna","Johanna","May","Mae",
  "Mylene","Myra","Myrna","Melanie","Melisa","Melissa","Marissa","Mariz","Pauline","Paula",
  "Paulina","Regina","Rhea","Rochelle","Sharon","Samantha","Sandra","Sarah","Sophia","Sofia",
  "Stephanie","Tiffany","Vanessa","Veronica","Vina","Yvonne","Leah","Lia","Louise","Luisa",
  "Lorraine","Lorna","Lani","Mika","Mikaela","Janelle","Janella","Janice","Joyce","Judy",
  "Judith","Julie","Juliana","Juliet","Julienne","Faith","Hope","Charity","Heaven","Blessy",
  "Precious","Lovelyn","Shaira","Aira","Kyra","Rachelle","Rachel","Reina","Selena","Selina",
  "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Johnny","Jonathan","Nathan","Michael",
  "Miguel","Daniel","David","Andrew","Andre","Anthony","Antonio","Albert","Alfred","Brian",
  "Bryan","Benjamin","Carlo","Carlos","Christian","Christopher","Chris","Cedric","Cesar",
  "Dennis","Diego","Dominic","Edward","Edgar","Emmanuel","Eric","Erwin","Francis","Frank",
  "Gabriel","Gilbert","Henry","Ian","Ivan","James","Jasper","Jerome","Joel","Joshua",
  "Kenneth","Kevin","Kyle","Lawrence","Leo","Leonard","Lester","Louis","Lucas","Marco",
  "Martin","Matthew","Melvin","Nathaniel","Noel","Oliver","Patrick","Raymond","Richard",
  "Robert","Ronald","Ryan","Samuel","Sebastian","Steven","Stephen","Thomas","Timothy","Victor",
];

// Exact get_bd_phone() from Python: +88{prefix}{8 digits}
function getBdPhone(): string {
  const prefixes = ["017", "019", "018", "016", "015", "013", "014"];
  const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
  const digits = Array.from({ length: 8 }, () => Math.floor(Math.random() * 10)).join("");
  return `+88${prefix}${digits}`;
}

// Exact get_pass() from Python
function getPass(): string {
  const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const digits = "0123456789";
  const specials = "!@#$%^&*()_+=";
  const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  const n_len = 5 + Math.floor(Math.random() * 3);
  let n = Array.from({ length: n_len }, () => letters[Math.floor(Math.random() * letters.length)]).join("");
  n = Math.random() > 0.5 ? n.charAt(0).toUpperCase() + n.slice(1).toLowerCase() : n.toLowerCase();

  const s = Array.from({ length: 2 + Math.floor(Math.random() * 2) }, () => specials[Math.floor(Math.random() * specials.length)]).join("");
  const d = Array.from({ length: 2 + Math.floor(Math.random() * 3) }, () => digits[Math.floor(Math.random() * digits.length)]).join("");
  const e = Array.from({ length: 2 + Math.floor(Math.random() * 3) }, () => letters[Math.floor(Math.random() * letters.length)]).join("");
  const u = Array.from({ length: 1 + Math.floor(Math.random() * 2) }, () => upper[Math.floor(Math.random() * upper.length)]).join("");

  const parts = [n, s, d, e, u].sort(() => Math.random() - 0.5);
  return parts.join("");
}

const MOBILE_UA_LIST = [
  "Mozilla/5.0 (Linux; Android 10; CPH2461 Build/TKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X6823) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2211133G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A515F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
];

function randomUA(): string {
  return MOBILE_UA_LIST[Math.floor(Math.random() * MOBILE_UA_LIST.length)];
}

// Simple cookie jar — mirrors Python requests.Session() behavior
class CookieJar {
  private jar: Map<string, string> = new Map();

  absorb(setCookieHeaders: string[]): void {
    for (const header of setCookieHeaders) {
      const [kv] = header.split(";");
      if (!kv) continue;
      const eqIdx = kv.indexOf("=");
      if (eqIdx === -1) continue;
      const k = kv.substring(0, eqIdx).trim();
      const v = kv.substring(eqIdx + 1).trim();
      if (k) this.jar.set(k, v);
    }
  }

  toString(): string {
    return [...this.jar.entries()].map(([k, v]) => `${k}=${v}`).join("; ");
  }

  toDict(): Record<string, string> {
    return Object.fromEntries(this.jar);
  }

  has(key: string): boolean {
    return this.jar.has(key);
  }

  get(key: string): string | undefined {
    return this.jar.get(key);
  }
}

// Extract ALL input field names+values from HTML (mirrors Python extractor using BeautifulSoup)
function extractFormFields(html: string): Record<string, string> {
  const fields: Record<string, string> = {};
  const re = /<input([^>]*)>/gi;
  let m: RegExpExecArray | null;
  while ((m = re.exec(html)) !== null) {
    const attrs = m[1];
    const nameMatch = attrs.match(/name=["']([^"']+)["']/i);
    const valueMatch = attrs.match(/value=["']([^"']*)["']/i);
    const typeMatch = attrs.match(/type=["']([^"']+)["']/i);
    const t = typeMatch?.[1]?.toLowerCase() ?? "";
    if (nameMatch?.[1] && !["button", "image", "reset"].includes(t)) {
      fields[nameMatch[1]] = valueMatch?.[1] ?? "";
    }
  }
  return fields;
}

// Mirrors Python check_facebook_profile_picture(uid)
// Returns true if "scontent" in 302 redirect Location
async function checkFbLive(uid: string): Promise<boolean> {
  try {
    const res = await fetch(`https://graph.facebook.com/${uid}/picture?type=normal`, {
      method: "GET",
      headers: {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
      },
      redirect: "manual",
      signal: AbortSignal.timeout(10000),
    });
    if (res.status === 302) {
      const loc = res.headers.get("location") ?? "";
      return loc.includes("scontent");
    }
    return false;
  } catch {
    return false;
  }
}

async function createFBAccount(): Promise<{
  status: "ok" | "fail" | "no_cp" | "no_limit";
  detail: string;
}> {
  const ua = randomUA();
  const name = SINGLE_NAMES[Math.floor(Math.random() * SINGLE_NAMES.length)];
  const phone = getBdPhone();
  const password = getPass();

  // Exact birthday range from Python: day 20-28, month 5-12, year 1990-2001
  const day = String(20 + Math.floor(Math.random() * 9));
  const month = String(5 + Math.floor(Math.random() * 8));
  const year = String(1990 + Math.floor(Math.random() * 12));

  const cookieJar = new CookieJar();

  // Step 1: GET registration page (mirrors Python _ses.get(_c5))
  const getHeaders: Record<string, string> = {
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
      headers: getHeaders,
      redirect: "follow",
      signal: AbortSignal.timeout(15000),
    });
    const setCookies = regRes.headers.getSetCookie?.() ?? [];
    cookieJar.absorb(setCookies);
    const html = await regRes.text();
    formFields = extractFormFields(html);
  } catch {
    return { status: "fail", detail: "❌ Failed to load registration page" };
  }

  // Exact encpass format from Python
  const encpass = `#PWD_BROWSER:0:${Math.floor(Date.now() / 1000)}:${password}`;

  // Exact payload from Python createfb_method_3
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
    fb_dtsg: formFields["fb_dtsg"] ?? "",
    jazoest: formFields["jazoest"] ?? "",
    lsd: formFields["lsd"] ?? "",
  };

  // Exact headers from Python (hdr + hdr2 merged)
  const submitHeaders: Record<string, string> = {
    "Host": "m.facebook.com",
    "Connection": "keep-alive",
    "User-Agent": ua,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate",
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
    "content-type": "application/x-www-form-urlencoded",
    "cookie": cookieJar.toString(),
  };

  // Step 2: POST submit (mirrors Python _ses.post(_c6, data=_pl, headers=_mhdr))
  try {
    const subRes = await fetch(FB_SUBMIT_URL, {
      method: "POST",
      headers: submitHeaders,
      body: new URLSearchParams(payload).toString(),
      redirect: "follow",
      signal: AbortSignal.timeout(20000),
    });
    const setCookies = subRes.headers.getSetCookie?.() ?? [];
    cookieJar.absorb(setCookies);
    const responseUrl = subRes.url;
    const html = await subRes.text();

    // Also parse Set-Cookie from response body / inline cookies
    const inlineC = html.match(/c_user=(\d+)/);
    if (inlineC && !cookieJar.has("c_user")) {
      cookieJar.absorb([`c_user=${inlineC[1]}`]);
    }

    const cookies = cookieJar.toDict();

    // Mirrors Python: if "c_user" in _cki
    if (cookies["c_user"]) {
      const uid = cookies["c_user"];
      // Mirrors Python: check_facebook_profile_picture — verify live
      const isLive = await checkFbLive(uid);
      const cookieStr = Object.entries(cookies).map(([k, v]) => `${k}=${v}`).join(";");

      if (isLive) {
        return {
          status: "ok",
          detail: `✅ OK | UID: ${uid} | ${name} | ${phone} | ${password}\n${cookieStr}`,
        };
      } else {
        // Account created but not live (still count as CP)
        return {
          status: "no_cp",
          detail: `⚠️ CP | UID: ${uid} | ${name} | ${phone} | ${password}`,
        };
      }
    }

    // Mirrors Python: elif "checkpoint" in _cki
    if (cookies["checkpoint"] || responseUrl.includes("checkpoint") || html.includes("checkpoint")) {
      return {
        status: "no_cp",
        detail: `⚠️ CP | ${name} | ${phone} | ${password}`,
      };
    }

    return {
      status: "fail",
      detail: `❌ FAIL | ${name} | ${phone} | ${password}`,
    };
  } catch (e) {
    return {
      status: "fail",
      detail: `❌ Error: ${e instanceof Error ? e.message : "Submit failed"}`,
    };
  }
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
