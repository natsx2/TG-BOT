import type { TaskResult } from "@workspace/db";

export interface ShareOptions {
  cookies: string;
  postUrl: string;
  count: number;
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

const NIKA_UA_LIST = [
  "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.11.118;]",
  "Mozilla/5.0 (Linux; Android 13; Google Pixel 6a Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/340.0.0.15.119;]",
  "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.12.120;]",
  "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190821.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.13.121;]",
  "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/341.0.0.16.122;]",
  "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.10.117;]",
];

function randomUA(): string {
  return NIKA_UA_LIST[Math.floor(Math.random() * NIKA_UA_LIST.length)];
}

function parseCookieString(raw: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const part of raw.split(";")) {
    const [k, ...v] = part.trim().split("=");
    if (k?.trim()) out[k.trim()] = v.join("=").trim();
  }
  return out;
}

function cookieObjToHeader(obj: Record<string, string>): string {
  return Object.entries(obj).map(([k, v]) => `${k}=${v}`).join("; ");
}

async function extractToken(cookieStr: string): Promise<string | null> {
  const cookieObj = parseCookieString(cookieStr);
  const cookieHeader = cookieObjToHeader(cookieObj);
  try {
    const res = await fetch("https://business.facebook.com/business_locations", {
      headers: {
        "user-agent": randomUA(),
        "referer": "https://www.facebook.com/",
        "host": "business.facebook.com",
        "origin": "https://business.facebook.com",
        "upgrade-insecure-requests": "1",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "content-type": "text/html; charset=utf-8",
        "cookie": cookieHeader,
      },
      signal: AbortSignal.timeout(15000),
    });
    const html = await res.text();
    const match = html.match(/EAAG[A-Za-z0-9]+/);
    return match ? match[0] : null;
  } catch {
    return null;
  }
}

async function sharePost(
  token: string,
  cookieObj: Record<string, string>,
  link: string
): Promise<{ success: boolean; uid: string | null; error: string | null }> {
  const ua = randomUA();
  const isVideo = /video|reel|watch/i.test(link);
  const headers: Record<string, string> = {
    "authority": "graph.facebook.com",
    "cache-control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "user-agent": ua,
    "accept": "application/json",
  };
  if (isVideo) {
    headers["content-type"] = "application/x-www-form-urlencoded";
    headers["sec-fetch-mode"] = "cors";
    headers["sec-fetch-site"] = "cross-site";
  }

  const url = `https://graph.facebook.com/v18.0/me/feed?link=${encodeURIComponent(link)}&published=0&access_token=${token}`;
  const cookieHeader = cookieObjToHeader(cookieObj);

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: { ...headers, cookie: cookieHeader },
      signal: AbortSignal.timeout(25000),
    });
    const text = await res.text();
    let data: Record<string, unknown> = {};
    try { data = JSON.parse(text) as Record<string, unknown>; } catch { /**/ }

    if ("id" in data) {
      const id = data["id"] as string;
      const uid = id.includes("_") ? id.split("_")[0] : id;
      return { success: true, uid, error: null };
    }
    if ("error" in data) {
      const err = (data["error"] as Record<string, unknown>)?.["message"] as string ?? "Unknown error";
      return { success: false, uid: null, error: err };
    }
    return { success: false, uid: null, error: `HTTP ${res.status}` };
  } catch (e) {
    return { success: false, uid: null, error: e instanceof Error ? e.message : "Network error" };
  }
}

export async function runShare(opts: ShareOptions): Promise<void> {
  const { cookies, postUrl, count, delay, onResult, signal } = opts;

  const token = await extractToken(cookies);
  if (!token) {
    await onResult({
      line: postUrl,
      status: "fail",
      detail: "❌ Token extraction failed. Check your cookie — must contain c_user, xs etc.",
      timestamp: new Date().toISOString(),
    });
    return;
  }

  const cookieObj = parseCookieString(cookies);
  const failedTokens = new Set<string>();
  const accountShares: Record<string, number> = { [token]: 0 };

  for (let i = 0; i < count; i++) {
    if (signal.aborted) break;
    if (failedTokens.has(token)) {
      await onResult({
        line: postUrl,
        status: "fail",
        detail: "❌ Token suspended/blocked",
        timestamp: new Date().toISOString(),
      });
      break;
    }

    if ((accountShares[token] ?? 0) >= 60) {
      await sleep(10000);
      accountShares[token] = 0;
    }

    const result = await sharePost(token, cookieObj, postUrl);
    accountShares[token] = (accountShares[token] ?? 0) + 1;

    if (result.success) {
      await onResult({
        line: postUrl,
        status: "ok",
        detail: `✅ Shared | UID: ${result.uid}`,
        timestamp: new Date().toISOString(),
      });
    } else {
      const msg = result.error?.toLowerCase() ?? "";
      const isFatal = ["rate limit","suspended","blocked","checkpoint","temporarily blocked","account disabled"].some(k => msg.includes(k));
      if (isFatal) {
        failedTokens.add(token);
        await onResult({
          line: postUrl,
          status: "fail",
          detail: `❌ Account suspended/blocked: ${result.error}`,
          timestamp: new Date().toISOString(),
        });
        break;
      }
      await onResult({
        line: postUrl,
        status: "fail",
        detail: `❌ ${result.error}`,
        timestamp: new Date().toISOString(),
      });
    }

    if (i > 0 && i % 60 === 0 && !signal.aborted) {
      await sleep(10000);
    } else if (i < count - 1 && !signal.aborted) {
      await sleep(delay || 100);
    }
  }
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
