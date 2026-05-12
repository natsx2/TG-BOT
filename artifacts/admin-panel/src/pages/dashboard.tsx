import React from "react";
import { Link } from "wouter";
import { useQueryClient } from "@tanstack/react-query";
import {
  useGetAdminStats,
  getGetAdminStatsQueryKey,
  useListBotUsers,
  getListBotUsersQueryKey,
  useApproveUser,
  useRejectUser
} from "@workspace/api-client-react";
import { Shell } from "@/components/layout/Shell";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { useToast } from "@/hooks/use-toast";
import { Users, UserCheck, UserX, Clock, Activity, Check, X, Zap } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";

export default function Dashboard() {
  const queryClient = useQueryClient();
  const { toast } = useToast();

  const { data: stats, isLoading: statsLoading } = useGetAdminStats({
    query: { queryKey: getGetAdminStatsQueryKey() }
  });

  const { data: recentUsers, isLoading: usersLoading } = useListBotUsers(
    { status: "all" },
    { query: { queryKey: getListBotUsersQueryKey({ status: "all" }) } }
  );

  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();

  const handleApprove = (id: number) => {
    approveMutation.mutate(
      { id },
      {
        onSuccess: () => {
          toast({ title: "User Approved", description: "The user has been granted access." });
          queryClient.invalidateQueries({ queryKey: getGetAdminStatsQueryKey() });
          queryClient.invalidateQueries({ queryKey: getListBotUsersQueryKey() });
        },
        onError: () => {
          toast({ variant: "destructive", title: "Action Failed", description: "Failed to approve user." });
        }
      }
    );
  };

  const handleReject = (id: number) => {
    rejectMutation.mutate(
      { id, data: { reason: "Rejected by admin from quick actions" } },
      {
        onSuccess: () => {
          toast({ title: "User Rejected", description: "The user request has been denied." });
          queryClient.invalidateQueries({ queryKey: getGetAdminStatsQueryKey() });
          queryClient.invalidateQueries({ queryKey: getListBotUsersQueryKey() });
        },
        onError: () => {
          toast({ variant: "destructive", title: "Action Failed", description: "Failed to reject user." });
        }
      }
    );
  };

  const pendingUsers = recentUsers?.filter(u => u.status === "pending").slice(0, 5) || [];

  return (
    <Shell>
      <div className="max-w-6xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold text-foreground">System Overview</h1>
          <p className="text-muted-foreground mt-1">Real-time statistics and pending actions.</p>
        </div>

        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <StatCard
            title="Total Users"
            value={stats?.total}
            loading={statsLoading}
            icon={<Users className="h-4 w-4 text-primary" />}
          />
          <StatCard
            title="Pending Approval"
            value={stats?.pending}
            loading={statsLoading}
            icon={<Clock className="h-4 w-4 text-yellow-500" />}
          />
          <StatCard
            title="Approved"
            value={stats?.approved}
            loading={statsLoading}
            icon={<UserCheck className="h-4 w-4 text-green-500" />}
          />
          <StatCard
            title="Today's Registrations"
            value={stats?.todayRegistrations}
            loading={statsLoading}
            icon={<Activity className="h-4 w-4 text-blue-400" />}
          />
          <StatCard
            title="Running Tasks"
            value={(stats as { runningTasks?: number } | undefined)?.runningTasks}
            loading={statsLoading}
            icon={<Zap className="h-4 w-4 text-purple-400" />}
          />
        </div>

        <div className="grid gap-6 md:grid-cols-2">
          <Card className="col-span-1 border-border bg-card">
            <CardHeader className="flex flex-row items-center justify-between">
              <div>
                <CardTitle>Action Required</CardTitle>
                <p className="text-sm text-muted-foreground mt-1">Pending user registrations</p>
              </div>
              <Link href="/users/pending">
                <Button variant="outline" size="sm">View All</Button>
              </Link>
            </CardHeader>
            <CardContent>
              {usersLoading ? (
                <div className="space-y-4">
                  {[1, 2, 3].map(i => <Skeleton key={i} className="h-16 w-full" />)}
                </div>
              ) : pendingUsers.length === 0 ? (
                <div className="text-center py-8 text-muted-foreground border border-dashed border-border rounded-lg">
                  <UserCheck className="h-8 w-8 mx-auto mb-3 opacity-50" />
                  <p>All caught up. No pending requests.</p>
                </div>
              ) : (
                <div className="space-y-4">
                  {pendingUsers.map(user => (
                    <div key={user.id} className="flex items-center justify-between p-4 rounded-lg border border-border bg-background">
                      <div className="flex items-center gap-3">
                        <Avatar className="h-10 w-10 border border-border">
                          <AvatarFallback className="bg-primary/20 text-primary">
                            {user.firstName[0]}
                          </AvatarFallback>
                        </Avatar>
                        <div>
                          <p className="font-medium text-foreground">{user.firstName} {user.lastName}</p>
                          <p className="text-sm text-muted-foreground">@{user.username || user.telegramId}</p>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <Button 
                          size="icon" 
                          variant="outline" 
                          className="text-green-500 hover:text-green-600 hover:bg-green-500/10 border-green-500/20"
                          onClick={() => handleApprove(user.id)}
                          disabled={approveMutation.isPending || rejectMutation.isPending}
                        >
                          <Check className="h-4 w-4" />
                        </Button>
                        <Button 
                          size="icon" 
                          variant="outline"
                          className="text-red-500 hover:text-red-600 hover:bg-red-500/10 border-red-500/20"
                          onClick={() => handleReject(user.id)}
                          disabled={approveMutation.isPending || rejectMutation.isPending}
                        >
                          <X className="h-4 w-4" />
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </Shell>
  );
}

function StatCard({ title, value, loading, icon }: { title: string, value?: number, loading: boolean, icon: React.ReactNode }) {
  return (
    <Card className="border-border bg-card">
      <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
        <CardTitle className="text-sm font-medium text-muted-foreground">{title}</CardTitle>
        {icon}
      </CardHeader>
      <CardContent>
        {loading ? (
          <Skeleton className="h-8 w-20" />
        ) : (
          <div className="text-3xl font-bold text-foreground">{value ?? 0}</div>
        )}
      </CardContent>
    </Card>
  );
}
