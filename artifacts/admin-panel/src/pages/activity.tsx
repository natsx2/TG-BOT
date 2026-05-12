import { useState, useEffect, useRef } from "react";
import { useAuth } from "@/hooks/use-auth";
import { API_BASE } from "@/lib/api";
import {
  Activity,
  RefreshCw,
  CheckCircle2,
  XCircle,
  Bot,
  Zap,
  Filter,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface LogEntry {
  id: number;
  ts: string;
  tgId: string;
  username: string;
  tool: string;
  event: string;
  detail: string;
  ok: boolean;
}

const TOOL_COLORS: Record<string, string> = {
  AU2:     "bg-indigo-500/10 text-indigo-400 border-indigo-500/30",
  FBCLONE: "bg-orange-500/10 text-orange-400 border-orange-500/30",
  SPAM:    "bg-purple-500/10 text-purple-400 border-purple-500/30",
  NIKA:    "bg-purple-500/10 text-purple-400 border-purple-500/30",
  AUTH:    "bg-slate-500/10 text-slate-400 border-slate-500/30",
};

const POLL_INTERVAL = 3000;

function ToolBadge({ tool }: { tool: string }) {
  const cls = TOOL_COLORS[tool] ?? "bg-muted/60 text-muted-foreground border-border";
  return (
    <Badge variant="outline" className={`text-[11px] font-semibold px-2 py-0 ${cls}`}>
      {tool}
    </Badge>
  );
}

function StatusDot({ ok }: { ok: boolean }) {
  return ok ? (
    <CheckCircle2 className="h-3.5 w-3.5 text-green-500 flex-shrink-0" />
  ) : (
    <XCircle className="h-3.5 w-3.5 text-red-500 flex-shrink-0" />
  );
}

function LogRow({ entry }: { entry: LogEntry }) {
  const time = new Date(entry.ts);
  const timeStr = time.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
  const dateStr = time.toLocaleDateString([], { month: "short", day: "numeric" });

  return (
    <div className="flex items-start gap-3 px-4 py-2.5 hover:bg-muted/40 transition-colors border-b border-border last:border-0">
      <StatusDot ok={entry.ok} />
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 flex-wrap">
          <ToolBadge tool={entry.tool} />
          <span className="text-sm font-medium text-foreground truncate">{entry.event}</span>
          {entry.detail && (
            <span className="text-xs text-muted-foreground truncate max-w-xs">{entry.detail}</span>
          )}
        </div>
        <div className="flex items-center gap-2 mt-0.5">
          <span className="text-[11px] text-muted-foreground">
            {entry.username || entry.tgId || "—"}
          </span>
          <span className="text-[11px] text-muted-foreground">·</span>
          <span className="text-[11px] text-muted-foreground" title={time.toISOString()}>
            {dateStr} {timeStr}
          </span>
        </div>
      </div>
    </div>
  );
}

export default function ActivityPage() {
  const { token } = useAuth();
  const [logs, setLogs]           = useState<LogEntry[]>([]);
  const [total, setTotal]         = useState(0);
  const [loading, setLoading]     = useState(true);
  const [autoRefresh, setAutoRefresh] = useState(true);
  const [toolFilter, setToolFilter]   = useState("all");
  const lastIdRef    = useRef(0);
  const timerRef     = useRef<ReturnType<typeof setInterval> | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  async function fetchLogs(since = 0, append = false) {
    try {
      const res = await fetch(
        `${API_BASE}/activity?since=${since}&limit=200`,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      if (!res.ok) return;
      const data: { logs: LogEntry[]; total: number } = await res.json();
      if (data.logs.length > 0) {
        lastIdRef.current = Math.max(...data.logs.map((l) => l.id));
        setLogs((prev) => {
          const combined = append ? [...prev, ...data.logs] : data.logs;
          return combined.slice(-500);
        });
      }
      setTotal(data.total);
    } catch {
      // ignore network errors during polling
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchLogs(0, false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (timerRef.current) clearInterval(timerRef.current);
    if (!autoRefresh) return;

    timerRef.current = setInterval(() => {
      fetchLogs(lastIdRef.current, true);
    }, POLL_INTERVAL);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [autoRefresh]);

  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    const nearBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 120;
    if (nearBottom) el.scrollTop = el.scrollHeight;
  }, [logs]);

  const displayed = toolFilter === "all"
    ? logs
    : logs.filter((l) => l.tool === toolFilter);

  const tools = Array.from(new Set(logs.map((l) => l.tool))).sort();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Activity Log</h1>
          <p className="text-sm text-muted-foreground mt-0.5">
            Real-time bot activity — {total} total events
          </p>
        </div>

        <div className="flex items-center gap-2">
          <Select value={toolFilter} onValueChange={setToolFilter}>
            <SelectTrigger className="h-8 text-xs w-36 bg-card border-border">
              <Filter className="h-3 w-3 mr-1.5 text-muted-foreground" />
              <SelectValue />
            </SelectTrigger>
            <SelectContent className="bg-card border-border">
              <SelectItem value="all">All Tools</SelectItem>
              {tools.map((t) => (
                <SelectItem key={t} value={t}>{t}</SelectItem>
              ))}
            </SelectContent>
          </Select>

          <Button
            variant={autoRefresh ? "default" : "outline"}
            size="sm"
            className="h-8 text-xs gap-1.5"
            onClick={() => setAutoRefresh((v) => !v)}
          >
            <Zap className={`h-3 w-3 ${autoRefresh ? "text-yellow-300" : ""}`} />
            {autoRefresh ? "Live" : "Paused"}
          </Button>

          <Button
            variant="outline"
            size="sm"
            className="h-8 w-8 p-0 border-border"
            onClick={() => fetchLogs(0, false)}
          >
            <RefreshCw className="h-3.5 w-3.5" />
          </Button>
        </div>
      </div>

      <div className="bg-card rounded-xl border border-border shadow-sm overflow-hidden">
        <div className="flex items-center gap-2 px-4 py-3 border-b border-border bg-muted/30">
          <Activity className="h-4 w-4 text-muted-foreground" />
          <span className="text-sm font-semibold text-foreground">Events</span>
          {autoRefresh && (
            <span className="flex items-center gap-1 text-[11px] text-green-500 ml-auto">
              <span className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse inline-block" />
              Live
            </span>
          )}
          {!autoRefresh && (
            <span className="text-[11px] text-muted-foreground ml-auto">Paused</span>
          )}
        </div>

        <div
          ref={containerRef}
          className="overflow-y-auto"
          style={{ maxHeight: "calc(100vh - 280px)", minHeight: "300px" }}
        >
          {loading ? (
            <div className="flex items-center justify-center py-16 text-muted-foreground text-sm">
              Loading activity logs...
            </div>
          ) : displayed.length === 0 ? (
            <div className="flex flex-col items-center justify-center py-16 text-center">
              <Bot className="h-8 w-8 text-muted-foreground/30 mb-2" />
              <p className="text-sm font-medium text-foreground">No activity yet</p>
              <p className="text-xs text-muted-foreground mt-0.5">
                Logs will appear here as the bot runs tools
              </p>
            </div>
          ) : (
            <div className="divide-y divide-border">
              {[...displayed].reverse().map((entry) => (
                <LogRow key={entry.id} entry={entry} />
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
