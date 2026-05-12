const BASE_URL = "/api";

function getToken() {
  return localStorage.getItem("admin_token");
}

function authHeaders(): Record<string, string> {
  const token = getToken();
  const headers: Record<string, string> = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = `Bearer ${token}`;
  return headers;
}

async function request<T>(method: string, path: string, body?: unknown): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: authHeaders(),
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data: any;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = {};
  }
  if (!res.ok) throw new Error(data.error || "Request failed");
  return data as T;
}

export interface TgUser {
  id: number;
  tgId: string;
  username: string | null;
  firstName: string | null;
  lastName: string | null;
  status: "pending" | "approved" | "rejected";
  registeredAt: string;
  approvedAt: string | null;
  note: string | null;
}

export interface LogEntry {
  id: number;
  tool: string;
  userId: string;
  username: string | null;
  action: string;
  status: string;
  message: string;
  createdAt: string;
}

export const api = {
  login: (username: string, password: string) =>
    request<{ success: boolean; username: string; token: string }>("POST", "/auth/login", { username, password }),
  logout: () => request<{ success: boolean }>("POST", "/auth/logout"),
  me: () => request<{ id: number; username: string }>("GET", "/auth/me"),
  changePassword: (currentPassword: string, newPassword: string) =>
    request<{ success: boolean; message: string }>("POST", "/auth/change-password", { currentPassword, newPassword }),

  getBotStatus: () => request<{ enabled: boolean; running: boolean; botToken: string }>("GET", "/bot/status"),
  toggleBot: (enabled: boolean) =>
    request<{ enabled: boolean; running: boolean; botToken: string }>("POST", "/bot/toggle", { enabled }),
  getBotStats: () =>
    request<{ totalUsers: number; totalRequests: number; au2FmRequests: number; fbCloneRequests: number; nikaSharerRequests: number }>("GET", "/bot/stats"),

  getLogs: (limit = 50, tool?: string) => {
    const params = new URLSearchParams({ limit: String(limit) });
    if (tool) params.set("tool", tool);
    return request<{ logs: LogEntry[]; total: number }>("GET", `/logs?${params}`);
  },

  getTgUsers: () => request<{ users: TgUser[]; total: number }>("GET", "/users"),
  approveTgUser: (id: number) => request<{ success: boolean; user: TgUser }>("POST", `/users/${id}/approve`),
  rejectTgUser: (id: number, note?: string) =>
    request<{ success: boolean; user: TgUser }>("POST", `/users/${id}/reject`, { note }),
  deleteTgUser: (id: number) => request<{ success: boolean }>("DELETE", `/users/${id}`),
};
