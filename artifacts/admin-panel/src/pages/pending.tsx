import { useState } from "react";
import {
  usePendingUsers,
  useApproveUser,
  useRejectUser,
  User,
} from "@/hooks/use-users";
import { Button } from "@/components/ui/button";
import { CheckCircle2, XCircle, Clock, Loader2, UserCheck } from "lucide-react";
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
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Skeleton } from "@/components/ui/skeleton";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
});

function UserCard({ user, onApprove, onReject, rejecting }: {
  user: User;
  onApprove: (user: User) => void;
  onReject: (user: User) => void;
  rejecting: boolean;
}) {
  const initials = [user.firstName?.[0], user.lastName?.[0]]
    .filter(Boolean)
    .join("")
    .toUpperCase() || "?";

  return (
    <div
      data-testid={`card-pending-${user.id}`}
      className="bg-white rounded-xl border border-border shadow-sm hover:shadow-md transition-shadow overflow-hidden"
    >
      <div className="p-5">
        <div className="flex items-start gap-4">
          <Avatar className="h-11 w-11 flex-shrink-0">
            <AvatarFallback className="text-sm font-bold bg-amber-100 text-amber-700">
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
              <div className="flex items-center gap-1.5 text-xs text-muted-foreground flex-shrink-0 bg-gray-50 rounded-md px-2 py-1 border border-border">
                <Clock className="h-3 w-3" />
                <span>{new Date(user.registeredAt).toLocaleDateString()}</span>
              </div>
            </div>
            <div className="mt-3 flex flex-wrap gap-2 text-xs text-muted-foreground">
              <span className="bg-gray-50 border border-border rounded-md px-2 py-0.5 font-mono">
                ID: {user.telegramId}
              </span>
              {user.notes && (
                <span className="bg-gray-50 border border-border rounded-md px-2 py-0.5">
                  {user.notes}
                </span>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className="px-5 py-3.5 bg-gray-50/50 border-t border-border flex items-center gap-2 justify-end">
        <Button
          variant="outline"
          size="sm"
          className="h-8 text-xs border-red-200 text-red-600 hover:bg-red-50 hover:text-red-700 hover:border-red-300 gap-1.5"
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

export default function Pending() {
  const { data: pendingUsers, isLoading } = usePendingUsers();
  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();
  const { toast } = useToast();
  const [rejectingId, setRejectingId] = useState<number | null>(null);
  const [approveUser, setApproveUser] = useState<User | null>(null);

  const form = useForm<z.infer<typeof approveSchema>>({
    resolver: zodResolver(approveSchema),
    defaultValues: { accessUsername: "", accessPassword: "", permanent: true },
  });

  const openApprove = (user: User) => {
    form.reset({
      accessUsername: user.telegramUsername || String(user.telegramId),
      accessPassword: Math.random().toString(36).slice(-10),
      permanent: true,
    });
    setApproveUser(user);
  };

  const submitApprove = (values: z.infer<typeof approveSchema>) => {
    if (!approveUser) return;
    approveMutation.mutate(
      { id: approveUser.id, data: values },
      {
        onSuccess: () => {
          toast({ title: "User approved", description: `@${approveUser.telegramUsername} now has access.` });
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
      <div className="flex items-start justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Pending Requests</h1>
          <p className="text-sm text-muted-foreground mt-0.5">
            {isLoading
              ? "Loading..."
              : pendingUsers?.length === 0
              ? "No pending requests"
              : `${pendingUsers?.length} user${pendingUsers?.length !== 1 ? "s" : ""} waiting for review`}
          </p>
        </div>
      </div>

      {isLoading ? (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} className="bg-white rounded-xl border border-border p-5 space-y-3">
              <div className="flex gap-3">
                <Skeleton className="h-11 w-11 rounded-full flex-shrink-0" />
                <div className="flex-1 space-y-2">
                  <Skeleton className="h-4 w-32" />
                  <Skeleton className="h-3 w-24" />
                </div>
              </div>
              <div className="flex gap-2 justify-end pt-2">
                <Skeleton className="h-8 w-20" />
                <Skeleton className="h-8 w-20" />
              </div>
            </div>
          ))}
        </div>
      ) : !pendingUsers || pendingUsers.length === 0 ? (
        <div className="bg-white rounded-xl border border-border shadow-sm py-20 text-center">
          <UserCheck className="h-10 w-10 text-green-400 mx-auto mb-3" />
          <h3 className="text-base font-semibold text-foreground">All caught up</h3>
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

      <Dialog open={!!approveUser} onOpenChange={(o) => !o && setApproveUser(null)}>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Approve User</DialogTitle>
            <DialogDescription>
              Set access credentials for{" "}
              <span className="font-medium text-foreground">
                @{approveUser?.telegramUsername || approveUser?.telegramId}
              </span>
            </DialogDescription>
          </DialogHeader>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(submitApprove)} className="space-y-4 pt-2">
              <FormField
                control={form.control}
                name="accessUsername"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Access Username</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono text-sm" data-testid="input-access-username" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="accessPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Access Password</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono text-sm" data-testid="input-access-password" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="permanent"
                render={({ field }) => (
                  <FormItem className="flex items-start space-x-3 space-y-0 rounded-lg border border-border p-4 bg-gray-50/50">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        data-testid="checkbox-permanent"
                      />
                    </FormControl>
                    <div className="space-y-0.5 leading-none">
                      <FormLabel className="text-sm font-medium cursor-pointer">Permanent access</FormLabel>
                      <p className="text-xs text-muted-foreground">Credentials will not expire</p>
                    </div>
                  </FormItem>
                )}
              />
              <DialogFooter className="gap-2">
                <Button type="button" variant="outline" onClick={() => setApproveUser(null)}>
                  Cancel
                </Button>
                <Button
                  type="submit"
                  disabled={approveMutation.isPending}
                  className="bg-green-600 hover:bg-green-700 text-white"
                  data-testid="button-confirm-approve"
                >
                  {approveMutation.isPending ? (
                    <><Loader2 className="h-4 w-4 mr-2 animate-spin" /> Approving...</>
                  ) : (
                    "Approve access"
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
