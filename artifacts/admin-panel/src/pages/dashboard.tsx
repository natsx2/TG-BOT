import { useStats, usePendingUsers } from "@/hooks/use-users";
import {
  Users,
  Clock,
  CheckCircle2,
  XCircle,
  ArrowRight,
  TrendingUp,
  Bot,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { Link } from "wouter";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

function StatCard({
  title,
  value,
  icon: Icon,
  color,
  loading,
}: {
  title: string;
  value?: number;
  icon: React.ElementType;
  color: string;
  loading: boolean;
}) {
  return (
    <div className="bg-white rounded-xl border border-border p-5 shadow-sm hover:shadow-md transition-shadow">
      <div className="flex items-center justify-between mb-3">
        <p className="text-sm font-medium text-muted-foreground">{title}</p>
        <div className={`w-9 h-9 rounded-lg flex items-center justify-center ${color}`}>
          <Icon className="h-4.5 w-4.5" />
        </div>
      </div>
      {loading ? (
        <Skeleton className="h-8 w-16" />
      ) : (
        <p className="text-3xl font-bold tracking-tight text-foreground">
          {value ?? 0}
        </p>
      )}
    </div>
  );
}

function UserRow({ user }: { user: any }) {
  const initials = [user.firstName?.[0], user.lastName?.[0]]
    .filter(Boolean)
    .join("")
    .toUpperCase() || user.telegramUsername?.[0]?.toUpperCase() || "?";

  return (
    <div
      data-testid={`row-pending-${user.id}`}
      className="flex items-center justify-between py-3 px-4 hover:bg-gray-50 transition-colors"
    >
      <div className="flex items-center gap-3 min-w-0">
        <Avatar className="h-8 w-8 flex-shrink-0">
          <AvatarFallback className="text-xs bg-amber-100 text-amber-700 font-semibold">
            {initials}
          </AvatarFallback>
        </Avatar>
        <div className="min-w-0">
          <p className="text-sm font-medium text-foreground truncate">
            {user.firstName} {user.lastName}
          </p>
          <p className="text-xs text-muted-foreground truncate">
            @{user.telegramUsername || "unknown"} &bull; ID {user.telegramId}
          </p>
        </div>
      </div>
      <div className="flex items-center gap-3 flex-shrink-0 ml-4">
        <p className="text-xs text-muted-foreground hidden sm:block">
          {new Date(user.registeredAt).toLocaleDateString()}
        </p>
        <Badge
          variant="outline"
          className="text-amber-600 border-amber-200 bg-amber-50 text-xs"
          data-testid={`badge-pending-${user.id}`}
        >
          Pending
        </Badge>
      </div>
    </div>
  );
}

export default function Dashboard() {
  const { data: stats, isLoading: statsLoading } = useStats();
  const { data: pending, isLoading: pendingLoading } = usePendingUsers();

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Overview</h1>
          <p className="text-sm text-muted-foreground mt-0.5">
            Monitor access requests and user activity
          </p>
        </div>
        <div className="flex items-center gap-2 text-xs text-muted-foreground bg-white border border-border rounded-lg px-3 py-1.5">
          <Bot className="h-3.5 w-3.5" />
          <span>Bot Active</span>
          <span className="w-1.5 h-1.5 rounded-full bg-green-500 inline-block" />
        </div>
      </div>

      <div className="grid gap-4 grid-cols-2 lg:grid-cols-4">
        <StatCard
          title="Total Users"
          value={stats?.total}
          icon={Users}
          color="bg-blue-50 text-blue-600"
          loading={statsLoading}
        />
        <StatCard
          title="Pending Review"
          value={stats?.pending}
          icon={Clock}
          color="bg-amber-50 text-amber-600"
          loading={statsLoading}
        />
        <StatCard
          title="Approved"
          value={stats?.approved}
          icon={CheckCircle2}
          color="bg-green-50 text-green-600"
          loading={statsLoading}
        />
        <StatCard
          title="Rejected"
          value={stats?.rejected}
          icon={XCircle}
          color="bg-red-50 text-red-600"
          loading={statsLoading}
        />
      </div>

      <div className="bg-white rounded-xl border border-border shadow-sm overflow-hidden">
        <div className="flex items-center justify-between px-5 py-4 border-b border-border">
          <div className="flex items-center gap-2">
            <TrendingUp className="h-4 w-4 text-muted-foreground" />
            <h2 className="text-sm font-semibold text-foreground">Pending Requests</h2>
            {(stats?.pending ?? 0) > 0 && (
              <Badge className="text-xs bg-amber-100 text-amber-700 border-0 rounded-full px-2">
                {stats?.pending}
              </Badge>
            )}
          </div>
          <Button variant="ghost" size="sm" asChild className="text-xs text-muted-foreground hover:text-foreground h-7">
            <Link href="/pending" data-testid="link-view-all-pending">
              View all
              <ArrowRight className="h-3.5 w-3.5 ml-1" />
            </Link>
          </Button>
        </div>

        <div className="divide-y divide-border">
          {pendingLoading ? (
            Array.from({ length: 3 }).map((_, i) => (
              <div key={i} className="flex items-center gap-3 py-3 px-4">
                <Skeleton className="h-8 w-8 rounded-full" />
                <div className="flex-1 space-y-1.5">
                  <Skeleton className="h-3.5 w-36" />
                  <Skeleton className="h-3 w-24" />
                </div>
              </div>
            ))
          ) : !pending || pending.length === 0 ? (
            <div className="py-12 text-center">
              <CheckCircle2 className="h-8 w-8 text-green-400 mx-auto mb-2" />
              <p className="text-sm font-medium text-foreground">All clear</p>
              <p className="text-xs text-muted-foreground mt-0.5">No pending requests right now</p>
            </div>
          ) : (
            pending.slice(0, 6).map((user) => (
              <UserRow key={user.id} user={user} />
            ))
          )}
        </div>
      </div>
    </div>
  );
}
