import { useStats, usePendingUsers } from "@/hooks/use-users";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Users, Clock, CheckCircle, XCircle } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Link } from "wouter";

export default function Dashboard() {
  const { data: stats, isLoading: statsLoading } = useStats();
  const { data: pending, isLoading: pendingLoading } = usePendingUsers();

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">System Overview</h2>
        <p className="text-muted-foreground font-mono text-sm mt-1">Real-time status of access requests.</p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Users</CardTitle>
            <Users className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold font-mono">{statsLoading ? "-" : stats?.total}</div>
          </CardContent>
        </Card>
        <Card className="border-primary/50 bg-primary/5">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-primary">Pending Review</CardTitle>
            <Clock className="h-4 w-4 text-primary" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold font-mono text-primary">{statsLoading ? "-" : stats?.pending}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Approved</CardTitle>
            <CheckCircle className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold font-mono">{statsLoading ? "-" : stats?.approved}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Rejected</CardTitle>
            <XCircle className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold font-mono">{statsLoading ? "-" : stats?.rejected}</div>
          </CardContent>
        </Card>
      </div>

      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-bold tracking-tight">Recent Pending Requests</h3>
          <Link href="/pending" className="text-sm text-primary hover:underline font-mono">View All Pending</Link>
        </div>
        <Card>
          <div className="divide-y border-t border-border">
            {pendingLoading ? (
              <div className="p-4 text-center text-sm text-muted-foreground font-mono">Loading data...</div>
            ) : pending?.length === 0 ? (
              <div className="p-4 text-center text-sm text-muted-foreground font-mono">No pending requests.</div>
            ) : (
              pending?.slice(0, 5).map(user => (
                <div key={user.id} className="p-4 flex items-center justify-between hover:bg-muted/50 transition-colors">
                  <div className="space-y-1">
                    <p className="text-sm font-medium leading-none">
                      {user.firstName} {user.lastName} <span className="text-muted-foreground font-mono">@{user.telegramUsername}</span>
                    </p>
                    <p className="text-xs text-muted-foreground font-mono">
                      ID: {user.telegramId} | Requested: {new Date(user.registeredAt).toLocaleString()}
                    </p>
                  </div>
                  <Badge variant="outline" className="text-yellow-500 border-yellow-500/20 bg-yellow-500/10">PENDING</Badge>
                </div>
              ))
            )}
          </div>
        </Card>
      </div>
    </div>
  );
}
