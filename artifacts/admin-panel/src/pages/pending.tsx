import { useState } from "react";
import {
  usePendingUsers,
  useApproveUser,
  useRejectUser,
  User,
} from "@/hooks/use-users";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Skeleton } from "@/components/ui/skeleton";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import {
  CheckCircle2,
  XCircle,
  Clock,
  Loader2,
  UserCheck,
  Infinity,
  CalendarDays,
  RefreshCw,
} from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogDescription,
} from "@/components/ui/dialog";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useQueryClient } from "@tanstack/react-query";

// ── Schema ────────────────────────────────────────────────────────────────────
const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
  expiryDate: z.string().optional(),
});

type ApproveForm = z.infer<typeof approveSchema>;

// ── Helper ────────────────────────────────────────────────────────────────────
function daysFromNow(dateStr: string): number {
  return Math.max(1, Math.ceil((new Date(dateStr).getTime() - Date.now()) / (1000 * 60 * 60 * 24)));
}

function buildPayload(values: ApproveForm) {
  const base = {
    accessUsername: values.accessUsername,
    accessPassword: values.accessPassword,
  };
  if (values.permanent || !values.expiryDate) {
    return { ...base, permanent: true };
  }
  return { ...base, durationDays: daysFromNow(values.expiryDate) };
}

// ── User Card ─────────────────────────────────────────────────────────────────
function UserCard({
  user,
  onApprove,
  onReject,
  rejecting,
}: {
  user: User;
  onApprove: (user: User) => void;
  onReject: (user: User) => void;
  rejecting: boolean;
}) {
  const initials =
    [user.firstName?.[0], user.lastName?.[0]].filter(Boolean).join("").toUpperCase() || "?";
  const regDate = new Date(user.registeredAt).toLocaleDateString("en-US", {
    month: "short", day: "numeric", year: "numeric",
  });

  return (
    <div
      data-testid={`card-pending-${user.id}`}
      className="bg-card rounded-xl border border-border shadow-sm hover:shadow-md transition-shadow overflow-hidden"
    >
      <div className="p-5">
        <div className="flex items-start gap-4">
          <Avatar className="h-11 w-11 flex-shrink-0">
            <AvatarFallback className="text-sm font-bold bg-amber-400/20 text-amber-600 dark:text-amber-400">
              {initials}
            </AvatarFallback>
          </Avatar>
          <div className="flex-1 min-w-0">
            <div className="flex items-start justify-between gap-2">
              <div className="min-w-0">
                <p className="font-semibold text-foreground truncate">
                  {user.firstName} {user.lastName}
                </p>
                <p className="text-sm text-muted-foreground truncate">
                  @{user.telegramUsername || "—"}
                </p>
              </div>
              <div className="flex items-center gap-1.5 text-xs text-muted-foreground flex-shrink-0 bg-muted/60 rounded-md px-2 py-1 border border-border">
                <Clock className="h-3 w-3" />
                <span>{regDate}</span>
              </div>
            </div>
            <div className="mt-3 flex flex-wrap gap-2">
              <span className="text-xs bg-muted/60 border border-border rounded-md px-2 py-0.5 font-mono text-muted-foreground">
                ID: {user.telegramId}
              </span>
              {user.notes && (
                <span className="text-xs bg-muted/60 border border-border rounded-md px-2 py-0.5 text-muted-foreground">
                  {user.notes}
                </span>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className="px-5 py-3.5 bg-muted/30 border-t border-border flex items-center gap-2 justify-end">
        <Button
          variant="outline"
          size="sm"
          className="h-8 text-xs border-red-300/60 text-red-500 hover:bg-red-500/10 hover:border-red-400/60 gap-1.5"
          onClick={() => onReject(user)}
          disabled={rejecting}
          data-testid={`button-reject-${user.id}`}
        >
          {rejecting ? (
            <Loader2 className="h-3.5 w-3.5 animate-spin" />
          ) : (
            <XCircle className="h-3.5 w-3.5" />
          )}
          Reject
        </Button>
        <Button
          size="sm"
          className="h-8 text-xs bg-green-600 hover:bg-green-700 text-white gap-1.5"
          onClick={() => onApprove(user)}
          data-testid={`button-approve-${user.id}`}
        >
          <CheckCircle2 className="h-3.5 w-3.5" />
          Approve
        </Button>
      </div>
    </div>
  );
}

// ── Main Page ─────────────────────────────────────────────────────────────────
export default function Pending() {
  const { data: pendingUsers, isLoading } = usePendingUsers();
  const approveMutation = useApproveUser();
  const rejectMutation  = useRejectUser();
  const { toast }       = useToast();
  const queryClient     = useQueryClient();
  const [rejectingId, setRejectingId]   = useState<number | null>(null);
  const [approveUser, setApproveUser]   = useState<User | null>(null);

  const form = useForm<ApproveForm>({
    resolver: zodResolver(approveSchema),
    defaultValues: {
      accessUsername: "",
      accessPassword: "",
      permanent: true,
      expiryDate: "",
    },
  });

  const permanent = form.watch("permanent");

  const openApprove = (user: User) => {
    form.reset({
      accessUsername: user.telegramUsername || String(user.telegramId),
      accessPassword: Math.random().toString(36).slice(-10),
      permanent: true,
      expiryDate: "",
    });
    setApproveUser(user);
  };

  const submitApprove = (values: ApproveForm) => {
    if (!approveUser) return;
    approveMutation.mutate(
      { id: approveUser.id, data: buildPayload(values) },
      {
        onSuccess: () => {
          toast({
            title: "✅ User approved",
            description: `@${approveUser.telegramUsername || approveUser.telegramId} now has access.`,
          });
          setApproveUser(null);
        },
        onError: (err: any) =>
          toast({ title: "Approval failed", description: err.message, variant: "destructive" }),
      }
    );
  };

  const handleReject = (user: User) => {
    setRejectingId(user.id);
    rejectMutation.mutate(
      { id: user.id, data: { notes: "Rejected by admin" } },
      {
        onSuccess: () => {
          toast({ title: "User rejected" });
          setRejectingId(null);
        },
        onError: (err: any) => {
          toast({ title: "Action failed", description: err.message, variant: "destructive" });
          setRejectingId(null);
        },
      }
    );
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Pending Requests</h1>
          <p className="text-sm text-muted-foreground mt-0.5">
            {isLoading
              ? "Loading requests..."
              : pendingUsers?.length === 0
              ? "No pending requests right now"
              : `${pendingUsers?.length} user${pendingUsers?.length !== 1 ? "s" : ""} waiting for review`}
          </p>
        </div>
        <Button
          variant="outline"
          size="sm"
          className="h-8 gap-1.5 text-xs"
          onClick={() => queryClient.invalidateQueries({ queryKey: ["users"] })}
          data-testid="button-refresh-pending"
        >
          <RefreshCw className="h-3.5 w-3.5" /> Refresh
        </Button>
      </div>

      {/* Content */}
      {isLoading ? (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} className="bg-card rounded-xl border border-border p-5 space-y-3">
              <div className="flex gap-3">
                <Skeleton className="h-11 w-11 rounded-full flex-shrink-0" />
                <div className="flex-1 space-y-2">
                  <Skeleton className="h-4 w-32" />
                  <Skeleton className="h-3 w-24" />
                </div>
              </div>
              <Skeleton className="h-6 w-full rounded-md" />
              <div className="flex gap-2 justify-end pt-2">
                <Skeleton className="h-8 w-20" />
                <Skeleton className="h-8 w-20" />
              </div>
            </div>
          ))}
        </div>
      ) : !pendingUsers || pendingUsers.length === 0 ? (
        <div className="bg-card rounded-xl border border-border shadow-sm py-20 text-center">
          <UserCheck className="h-10 w-10 text-green-400 mx-auto mb-3" />
          <h3 className="text-base font-semibold text-foreground">All caught up!</h3>
          <p className="text-sm text-muted-foreground mt-1">
            No pending access requests at this time
          </p>
        </div>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {pendingUsers.map((user) => (
            <UserCard
              key={user.id}
              user={user}
              onApprove={openApprove}
              onReject={handleReject}
              rejecting={rejectingId === user.id}
            />
          ))}
        </div>
      )}

      {/* Approve Dialog */}
      <Dialog open={!!approveUser} onOpenChange={(o) => !o && setApproveUser(null)}>
        <DialogContent className="sm:max-w-md bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">Approve User</DialogTitle>
            <DialogDescription className="text-muted-foreground">
              Set credentials and access duration for{" "}
              <span className="font-semibold text-foreground">
                @{approveUser?.telegramUsername || approveUser?.telegramId}
              </span>
            </DialogDescription>
          </DialogHeader>

          <Form {...form}>
            <form onSubmit={form.handleSubmit(submitApprove)} className="space-y-4 pt-1">
              {/* Username */}
              <FormField
                control={form.control}
                name="accessUsername"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">Access Username</FormLabel>
                    <FormControl>
                      <Input
                        {...field}
                        className="font-mono text-sm bg-background text-foreground border-border"
                        data-testid="input-access-username"
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Password */}
              <FormField
                control={form.control}
                name="accessPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">Access Password</FormLabel>
                    <FormControl>
                      <Input
                        {...field}
                        className="font-mono text-sm bg-background text-foreground border-border"
                        data-testid="input-access-password"
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Permanent toggle */}
              <FormField
                control={form.control}
                name="permanent"
                render={({ field }) => (
                  <FormItem className="flex items-center space-x-3 space-y-0 rounded-lg border border-border p-3 bg-muted/30">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        data-testid="checkbox-permanent"
                      />
                    </FormControl>
                    <div className="leading-none">
                      <FormLabel className="text-sm font-medium cursor-pointer flex items-center gap-1.5 text-foreground">
                        <Infinity className="h-3.5 w-3.5" />
                        Permanent access
                      </FormLabel>
                      <p className="text-xs text-muted-foreground mt-0.5">
                        Credentials never expire
                      </p>
                    </div>
                  </FormItem>
                )}
              />

              {/* Expiry date (only if not permanent) */}
              {!permanent && (
                <FormField
                  control={form.control}
                  name="expiryDate"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-foreground flex items-center gap-1.5">
                        <CalendarDays className="h-3.5 w-3.5" />
                        Expiry Date
                      </FormLabel>
                      <FormControl>
                        <Input
                          type="date"
                          {...field}
                          min={new Date().toISOString().split("T")[0]}
                          className="text-sm bg-background text-foreground border-border"
                          data-testid="input-expiry-date"
                        />
                      </FormControl>
                      <p className="text-xs text-muted-foreground">
                        Access will be revoked after this date
                      </p>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              )}

              <DialogFooter className="gap-2 pt-1">
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => setApproveUser(null)}
                  className="border-border text-foreground"
                >
                  Cancel
                </Button>
                <Button
                  type="submit"
                  disabled={approveMutation.isPending}
                  className="bg-green-600 hover:bg-green-700 text-white"
                  data-testid="button-confirm-approve"
                >
                  {approveMutation.isPending ? (
                    <>
                      <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                      Approving...
                    </>
                  ) : (
                    <>
                      <CheckCircle2 className="h-4 w-4 mr-2" />
                      Approve Access
                    </>
                  )}
                </Button>
              </DialogFooter>
            </form>
          </Form>
        </DialogContent>
      </Dialog>
    </div>
  );
}
