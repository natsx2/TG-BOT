import { Router, type IRouter } from "express";
import { requireAuth } from "../middlewares/requireAuth";

const router: IRouter = Router();

// In-memory ring buffer — 500 most recent events
const MAX_LOGS = 500;

interface ActivityEntry {
  id: number;
  ts: string;
  tgId: string;
  username: string;
  tool: string;
  event: string;
  detail: string;
  ok: boolean;
}

let _counter = 1;
const _logs: ActivityEntry[] = [];

function pushLog(entry: Omit<ActivityEntry, "id" | "ts">): ActivityEntry {
  const log: ActivityEntry = {
    id: _counter++,
    ts: new Date().toISOString(),
    ...entry,
  };
  _logs.push(log);
  if (_logs.length > MAX_LOGS) _logs.shift();
  return log;
}

// POST /api/activity — called by the bot to log an event
router.post("/activity", async (req, res): Promise<void> => {
  const { tgId, username, tool, event, detail, ok } = req.body ?? {};
  if (!tool || !event) {
    res.status(400).json({ error: "tool and event are required" });
    return;
  }
  const log = pushLog({
    tgId: String(tgId ?? ""),
    username: String(username ?? ""),
    tool: String(tool),
    event: String(event),
    detail: String(detail ?? ""),
    ok: Boolean(ok ?? true),
  });
  res.status(201).json(log);
});

// GET /api/activity — admin panel fetches logs
router.get("/activity", requireAuth, async (req, res): Promise<void> => {
  const limit = Math.min(parseInt(String(req.query.limit ?? "100"), 10), 500);
  const since = req.query.since ? parseInt(String(req.query.since), 10) : 0;
  const filtered = _logs.filter((l) => l.id > since).slice(-limit);
  res.json({ logs: filtered, total: _logs.length });
});

export default router;
