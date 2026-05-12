import type { TaskResult } from "@workspace/db";

export interface ShareOptions {
  cookies: string;
  postUrl: string;
  count: number;
  delay: number;
  onResult: (result: TaskResult) => Promise<void>;
  signal: AbortSignal;
}

export async function runShare(opts: ShareOptions): Promise<void> {
  const { cookies, postUrl, count, delay, onResult, signal } = opts;

  const cookieMap = parseCookies(cookies);
  const token = cookieMap["xs"] ?? cookieMap["c_user"] ?? "";
  const userId = cookieMap["c_user"] ?? "";

  if (!userId || !token) {
    await onResult({
      line: postUrl,
      status: "fail",
      detail: "Invalid cookies: missing c_user or xs",
      timestamp: new Date().toISOString(),
    });
    return;
  }

  for (let i = 0; i < count; i++) {
    if (signal.aborted) break;

    try {
      const result = await shareSinglePost(cookies, postUrl, userId);
      await onResult({
        line: postUrl,
        status: result.success ? "ok" : "fail",
        detail: result.detail,
        timestamp: new Date().toISOString(),
      });
    } catch (err) {
      await onResult({
        line: postUrl,
        status: "fail",
        detail: err instanceof Error ? err.message : "Unknown error",
        timestamp: new Date().toISOString(),
      });
    }

    if (i < count - 1 && !signal.aborted) {
      await sleep(delay);
    }
  }
}

async function shareSinglePost(
  cookies: string,
  postUrl: string,
  _userId: string
): Promise<{ success: boolean; detail: string }> {
  const headers = {
    "User-Agent":
      "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    Cookie: cookies,
    "Content-Type": "application/x-www-form-urlencoded",
    Origin: "https://m.facebook.com",
    Referer: "https://m.facebook.com/",
    "Accept-Language": "en-US,en;q=0.9",
  };

  const dtsg = await getDtsg(cookies);

  const body = new URLSearchParams({
    fb_dtsg: dtsg,
    story_fbid: extractPostId(postUrl),
    target_post_id: extractPostId(postUrl),
    composer_session_id: generateSessionId(),
    privacy: JSON.stringify({ base_state: "FRIENDS" }),
    message: "",
    has_multi_photo_drafts: "0",
    action_type_params: JSON.stringify({ composer_type: "share_story" }),
  });

  const res = await fetch("https://m.facebook.com/share/surfaceapi/", {
    method: "POST",
    headers,
    body: body.toString(),
    signal: AbortSignal.timeout(15000),
  });

  if (res.ok) {
    const text = await res.text();
    const success = text.includes("success") || res.status === 200;
    return { success, detail: success ? "Shared successfully" : "Share may have failed" };
  }

  return { success: false, detail: `HTTP ${res.status}` };
}

async function getDtsg(cookies: string): Promise<string> {
  try {
    const res = await fetch("https://m.facebook.com/", {
      headers: {
        Cookie: cookies,
        "User-Agent":
          "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 Chrome/112.0.0.0 Mobile Safari/537.36",
      },
      signal: AbortSignal.timeout(10000),
    });
    const html = await res.text();
    const match = html.match(/"DTSGInitialData".*?"token":"([^"]+)"/);
    return match?.[1] ?? "AQHO";
  } catch {
    return "AQHO";
  }
}

function extractPostId(url: string): string {
  const patterns = [
    /\/posts\/(\d+)/,
    /story_fbid=(\d+)/,
    /\/(\d{15,})/,
    /pfbid([A-Za-z0-9]+)/,
  ];
  for (const p of patterns) {
    const m = url.match(p);
    if (m) return m[1];
  }
  return url.split("/").filter(Boolean).pop() ?? "0";
}

function parseCookies(raw: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const part of raw.split(";")) {
    const [k, ...v] = part.trim().split("=");
    if (k) out[k.trim()] = v.join("=").trim();
  }
  return out;
}

function generateSessionId(): string {
  return Array.from({ length: 32 }, () =>
    Math.floor(Math.random() * 16).toString(16)
  ).join("");
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
