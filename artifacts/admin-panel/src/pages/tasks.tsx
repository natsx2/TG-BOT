import React, { useState } from "react";
import { useListTasks, useStopTask, getListTasksQueryKey } from "@workspace/api-client-react";
import { Shell } from "@/components/layout/Shell";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { useToast } from "@/hooks/use-toast";
import { useQueryClient } from "@tanstack/react-query";
import { Square, RefreshCw, Activity } from "lucide-react";
import { format } from "date-fns";

type TaskStatus = "running" | "done" | "stopped" | "failed";
type ToolName = "share" | "crck" | "create";

export default function Tasks() {
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [toolFilter, setToolFilter] = useState<string>("all");
  const [search, setSearch] = useState("");
  const { toast } = useToast();
  const queryClient = useQueryClient();

  const taskParams = {
    status: statusFilter !== "all" ? statusFilter : undefined,
    toolName: toolFilter !== "all" ? toolFilter : undefined,
  };
  const { data: tasks, isLoading, refetch } = useListTasks(
    taskParams,
    { query: { queryKey: getListTasksQueryKey(taskParams), refetchInterval: 5000 } }
  );

  const stopMutation = useStopTask();

  const handleStop = (id: number) => {
    stopMutation.mutate({ id }, {
      onSuccess: () => {
        toast({ title: "Task stopped" });
        refetch();
      }
    });
  };

  const filtered = tasks?.filter(t => !search || t.telegramId.includes(search)) ?? [];

  const statusBadge = (s: TaskStatus) => {
    switch (s) {
      case "running": return <Badge className="bg-blue-500/20 text-blue-400 border-blue-500/30">⚙️ Running</Badge>;
      case "done": return <Badge className="bg-green-500/20 text-green-400 border-green-500/30">✅ Done</Badge>;
      case "stopped": return <Badge className="bg-yellow-500/20 text-yellow-400 border-yellow-500/30">🛑 Stopped</Badge>;
      case "failed": return <Badge className="bg-red-500/20 text-red-400 border-red-500/30">❌ Failed</Badge>;
    }
  };

  const toolBadge = (t: ToolName) => {
    switch (t) {
      case "share": return <Badge variant="outline" className="text-blue-400 border-blue-400/30">🔵 SHARE</Badge>;
      case "crck": return <Badge variant="outline" className="text-red-400 border-red-400/30">🔴 CRCK</Badge>;
      case "create": return <Badge variant="outline" className="text-green-400 border-green-400/30">🟢 CREATE</Badge>;
    }
  };

  return (
    <Shell>
      <div className="max-w-7xl mx-auto space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-foreground">Task Monitor</h1>
            <p className="text-muted-foreground mt-1">Live task tracking across all users.</p>
          </div>
          <Button variant="outline" onClick={() => refetch()} className="gap-2">
            <RefreshCw className="h-4 w-4" /> Refresh
          </Button>
        </div>

        <div className="flex flex-wrap gap-3 bg-card p-4 rounded-lg border border-border">
          <Input
            placeholder="Filter by Telegram ID..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="max-w-xs bg-background border-border"
          />
          <div className="flex gap-2 flex-wrap">
            {(["all", "running", "done", "stopped", "failed"] as const).map(s => (
              <Button key={s} size="sm" variant={statusFilter === s ? "default" : "outline"}
                onClick={() => setStatusFilter(s)} className="capitalize">
                {s}
              </Button>
            ))}
          </div>
          <div className="flex gap-2 flex-wrap">
            {(["all", "share", "crck", "create"] as const).map(t => (
              <Button key={t} size="sm" variant={toolFilter === t ? "default" : "outline"}
                onClick={() => setToolFilter(t)} className="uppercase">
                {t}
              </Button>
            ))}
          </div>
        </div>

        <div className="bg-card rounded-lg border border-border overflow-hidden">
          <Table>
            <TableHeader className="bg-secondary/50">
              <TableRow className="border-border hover:bg-transparent">
                <TableHead>ID</TableHead>
                <TableHead>Tool</TableHead>
                <TableHead>Telegram ID</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Results</TableHead>
                <TableHead>Started</TableHead>
                <TableHead className="text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {isLoading ? (
                <TableRow><TableCell colSpan={7} className="text-center py-8 text-muted-foreground">Loading tasks...</TableCell></TableRow>
              ) : !filtered.length ? (
                <TableRow>
                  <TableCell colSpan={7} className="text-center py-16">
                    <Activity className="h-12 w-12 mx-auto text-muted-foreground/50 mb-4" />
                    <p className="text-lg font-medium text-foreground">No tasks found</p>
                    <p className="text-muted-foreground">Tasks will appear here when users run tools.</p>
                  </TableCell>
                </TableRow>
              ) : (
                filtered.map(task => (
                  <TableRow key={task.id} className="border-border hover:bg-secondary/30">
                    <TableCell className="font-mono text-muted-foreground">#{task.id}</TableCell>
                    <TableCell>{toolBadge(task.toolName as ToolName)}</TableCell>
                    <TableCell className="font-mono text-sm text-foreground">{task.telegramId}</TableCell>
                    <TableCell>{statusBadge(task.status as TaskStatus)}</TableCell>
                    <TableCell>
                      <div className="flex gap-2 text-sm">
                        <span className="text-green-400">✅{task.totalOk}</span>
                        <span className="text-red-400">❌{task.totalFail}</span>
                        <span className="text-yellow-400">⚠️{task.totalNoCp}</span>
                      </div>
                    </TableCell>
                    <TableCell className="text-muted-foreground text-sm">
                      {format(new Date(task.createdAt), "MMM d, HH:mm")}
                    </TableCell>
                    <TableCell className="text-right">
                      {task.status === "running" && (
                        <Button size="sm" variant="destructive" onClick={() => handleStop(task.id)}
                          disabled={stopMutation.isPending} className="gap-1">
                          <Square className="h-3 w-3" /> Stop
                        </Button>
                      )}
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </div>
      </div>
    </Shell>
  );
}
