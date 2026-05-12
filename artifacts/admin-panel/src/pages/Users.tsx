import { useState, useEffect, useCallback } from "react";
import { api } from "@/lib/api";

interface TgUser {
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

function StatusBadge({ status }: { status: string }) {
  const styles: Record<string, string> = {
    pending: "bg-yellow-500/15 text-yellow-400 border border-yellow-500/20",
    approved: "bg-green-500/15 text-green-400 border border-green-500/20",
    rejected: "bg-red-500/15 text-red-400 border border-red-500/20",
  };
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${styles[status] ?? "bg-muted text-muted-foreground"}`}>
      {status.charAt(0).toUpperCase() + status.slice(1)}
    </span>
  );
}

function fmt(d: string) {
  return new Date(d).toLocaleString();
}

export default function Users() {
  const [users, setUsers] = useState<TgUser[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState<"all" | "pending" | "approved" | "rejected">("all");
  const [actionLoading, setActionLoading] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await api.getTgUsers();
      setUsers(data.users);
    } catch (e: any) {
      setError(e.message || "Failed to load users");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { load(); }, [load]);

  const approve = async (id: number) => {
    setActionLoading(id);
    try {
      await api.approveTgUser(id);
      await load();
    } catch (e: any) {
      setError(e.message || "Failed to approve");
    } finally {
      setActionLoading(null);
    }
  };

  const reject = async (id: number) => {
    setActionLoading(id);
    try {
      await api.rejectTgUser(id);
      await load();
    } catch (e: any) {
      setError(e.message || "Failed to reject");
    } finally {
      setActionLoading(null);
    }
  };

  const remove = async (id: number) => {
    if (!confirm("Delete this user?")) return;
    setActionLoading(id);
    try {
      await api.deleteTgUser(id);
      await load();
    } catch (e: any) {
      setError(e.message || "Failed to delete");
    } finally {
      setActionLoading(null);
    }
  };

  const filtered = filter === "all" ? users : users.filter(u => u.status === filter);

  const counts = {
    all: users.length,
    pending: users.filter(u => u.status === "pending").length,
    approved: users.filter(u => u.status === "approved").length,
    rejected: users.filter(u => u.status === "rejected").length,
  };

  return (
    <div className="space-y-5">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-foreground">Telegram Users</h1>
          <p className="text-sm text-muted-foreground mt-0.5">Manage user access to the bot</p>
        </div>
        <button
          onClick={load}
          disabled={loading}
          className="flex items-center gap-2 px-3 py-2 bg-secondary text-secondary-foreground rounded-lg text-sm hover:bg-secondary/80 disabled:opacity-50"
        >
          <svg className={`w-4 h-4 ${loading ? "animate-spin" : ""}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh
        </button>
      </div>

      {error && (
        <div className="p-3 rounded-lg bg-destructive/10 border border-destructive/20 text-destructive text-sm">
          {error}
        </div>
      )}

      {/* Stats */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
        {(["all", "pending", "approved", "rejected"] as const).map(s => (
          <button
            key={s}
            onClick={() => setFilter(s)}
            className={`p-3 rounded-lg border text-left transition-colors ${
              filter === s
                ? "border-primary bg-primary/10"
                : "border-border bg-card hover:border-primary/40"
            }`}
          >
            <div className="text-xs text-muted-foreground capitalize">{s}</div>
            <div className={`text-2xl font-bold mt-1 ${
              s === "pending" ? "text-yellow-400" :
              s === "approved" ? "text-green-400" :
              s === "rejected" ? "text-red-400" :
              "text-foreground"
            }`}>{counts[s]}</div>
          </button>
        ))}
      </div>

      {/* Table */}
      <div className="rounded-lg border border-border bg-card overflow-hidden">
        {loading ? (
          <div className="flex items-center justify-center py-12">
            <div className="w-5 h-5 border-2 border-primary border-t-transparent rounded-full animate-spin" />
          </div>
        ) : filtered.length === 0 ? (
          <div className="text-center py-12 text-muted-foreground text-sm">
            No {filter === "all" ? "" : filter} users found.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border bg-muted/30">
                  <th className="text-left px-4 py-3 text-muted-foreground font-medium">User</th>
                  <th className="text-left px-4 py-3 text-muted-foreground font-medium">Telegram ID</th>
                  <th className="text-left px-4 py-3 text-muted-foreground font-medium">Status</th>
                  <th className="text-left px-4 py-3 text-muted-foreground font-medium">Registered</th>
                  <th className="text-right px-4 py-3 text-muted-foreground font-medium">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {filtered.map(u => (
                  <tr key={u.id} className="hover:bg-muted/20 transition-colors">
                    <td className="px-4 py-3">
                      <div className="font-medium text-foreground">
                        {[u.firstName, u.lastName].filter(Boolean).join(" ") || "Unknown"}
                      </div>
                      {u.username && (
                        <div className="text-xs text-muted-foreground">@{u.username}</div>
                      )}
                    </td>
                    <td className="px-4 py-3 text-muted-foreground font-mono text-xs">{u.tgId}</td>
                    <td className="px-4 py-3"><StatusBadge status={u.status} /></td>
                    <td className="px-4 py-3 text-muted-foreground text-xs">{fmt(u.registeredAt)}</td>
                    <td className="px-4 py-3">
                      <div className="flex items-center gap-2 justify-end">
                        {u.status !== "approved" && (
                          <button
                            onClick={() => approve(u.id)}
                            disabled={actionLoading === u.id}
                            className="px-2.5 py-1 bg-green-500/15 text-green-400 border border-green-500/20 rounded text-xs hover:bg-green-500/25 disabled:opacity-50 transition-colors"
                          >
                            {actionLoading === u.id ? "..." : "Approve"}
                          </button>
                        )}
                        {u.status !== "rejected" && (
                          <button
                            onClick={() => reject(u.id)}
                            disabled={actionLoading === u.id}
                            className="px-2.5 py-1 bg-red-500/15 text-red-400 border border-red-500/20 rounded text-xs hover:bg-red-500/25 disabled:opacity-50 transition-colors"
                          >
                            {actionLoading === u.id ? "..." : "Reject"}
                          </button>
                        )}
                        <button
                          onClick={() => remove(u.id)}
                          disabled={actionLoading === u.id}
                          className="p-1 text-muted-foreground hover:text-destructive rounded transition-colors disabled:opacity-50"
                          title="Delete"
                        >
                          <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                          </svg>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
