import { useState } from "react";
import {
  useUsers,
  useApproveUser,
  useRejectUser,
  useDeleteUser,
  useUpdateUserAccess,
  useRevokeAccess,
  User,
} from "@/hooks/use-users";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogDescription,
} from "@/components/ui/dialog";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Checkbox } from "@/components/ui/checkbox";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Skeleton } from "@/components/ui/skeleton";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  CheckCircle2,
  XCircle,
  Trash2,
  Search,
  MoreHorizontal,
  Users,
  Loader2,
  RefreshCw,
  ShieldOff,
  Pencil,
  Clock,
  Infinity,
  AlertTriangle,
} from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { useQueryClient } from "@tanstack/react-query";

// ── Schemas ──────────────────────────────────────────────────────────────────
const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
  expiryDate: z.string().optional(),
});

const editAccessSchema = z.object({
  accessUsername: z.string().min(1),
  accessPassword: z.string().optional(),
  permanent: z.boolean().default(true),
  expiryDate: z.string().optional(),
});

const STATUS_TABS = ["all", "pending", "approved", "rejected"] as const;

// ── Helpers ───────────────────────────────────────────────────────────────────
function expiryStatus(expiresAt?: string | null): "permanent" | "active" | "expiring" | "expired" {
  if (!expiresAt) return "permanent";
  const exp = new Date(expiresAt);
  const now = new Date();
  if (exp < now) return "expired";
  const diff = exp.getTime() - now.getTime();
  if (diff < 3 * 24 * 60 * 60 * 1000) return "expiring";
  return "active";
}

function formatDate(d?: string | null) {
  if (!d) return "—";
  return new Date(d).toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
}

function daysFromNow(dateStr: string): number {
  return Math.ceil((new Date(dateStr).getTime() - Date.now()) / (1000 * 60 * 60 * 24));
}

function buildExpiryPayload(permanent: boolean, expiryDate?: string) {
  if (permanent) return { permanent: true };
  if (expiryDate) return { durationDays: Math.max(1, daysFromNow(expiryDate)) };
  return { permanent: true };
}

// ── Sub-components ────────────────────────────────────────────────────────────
function StatusBadge({ status }: { status: User["status"] }) {
  if (status === "pending")
    return <Badge variant="outline" className="text-amber-500 border-amber-400/40 bg-amber-400/10 text-xs">Pending</Badge>;
  if (status === "approved")
    return <Badge variant="outline" className="text-green-500 border-green-400/40 bg-green-400/10 text-xs">Approved</Badge>;
  return <Badge variant="outline" className="text-red-500 border-red-400/40 bg-red-400/10 text-xs">Rejected</Badge>;
}

function ExpiryBadge({ expiresAt }: { expiresAt?: string | null }) {
  const status = expiryStatus(expiresAt);
  if (status === "permanent")
    return (
      <span className="inline-flex items-center gap-1 text-xs text-green-500 font-medium">
        <Infinity className="h-3 w-3" /> Permanent
      </span>
    );
  if (status === "expired")
    return (
      <span className="inline-flex items-center gap-1 text-xs text-red-500 font-medium">
        <AlertTriangle className="h-3 w-3" /> Expired {formatDate(expiresAt)}
      </span>
    );
  if (status === "expiring")
    return (
      <span className="inline-flex items-center gap-1 text-xs text-amber-500 font-medium">
        <Clock className="h-3 w-3" /> Expiring {formatDate(expiresAt)}
      </span>
    );
  return (
    <span className="inline-flex items-center gap-1 text-xs text-blue-500 font-medium">
      <Clock className="h-3 w-3" /> {formatDate(expiresAt)}
    </span>
  );
}

// ── Expiry picker sub-form ────────────────────────────────────────────────────
function ExpiryFields({ control, watch }: { control: any; watch: any }) {
  const permanent = watch("permanent");
  return (
    <div className="space-y-3">
      <FormField
        control={control}
        name="permanent"
        render={({ field }) => (
          <FormItem className="flex items-center space-x-3 space-y-0 rounded-lg border border-border p-3 bg-muted/30">
            <FormControl>
              <Checkbox checked={field.value} onCheckedChange={field.onChange} data-testid="checkbox-permanent" />
            </FormControl>
            <div className="leading-none">
              <FormLabel className="text-sm font-medium cursor-pointer flex items-center gap-1.5">
                <Infinity className="h-3.5 w-3.5" /> Permanent access
              </FormLabel>
              <p className="text-xs text-muted-foreground mt-0.5">Credentials will never expire</p>
            </div>
          </FormItem>
        )}
      />
      {!permanent && (
        <FormField
          control={control}
          name="expiryDate"
          render={({ field }) => (
            <FormItem>
              <FormLabel className="text-sm">Expiry Date</FormLabel>
              <FormControl>
                <Input
                  type="date"
                  {...field}
                  min={new Date().toISOString().split("T")[0]}
                  className="text-sm bg-background text-foreground"
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
      )}
    </div>
  );
}

// ── Main component ────────────────────────────────────────────────────────────
export default function UsersPage() {
  const { data: users, isLoading } = useUsers();
  const [search, setSearch]             = useState("");
  const [filter, setFilter]             = useState<(typeof STATUS_TABS)[number]>("all");
  const [approveUser, setApproveUser]   = useState<User | null>(null);
  const [editUser, setEditUser]         = useState<User | null>(null);
  const [confirmDelete, setConfirmDelete] = useState<User | null>(null);
  const [confirmRevoke, setConfirmRevoke] = useState<User | null>(null);

  const approveMutation     = useApproveUser();
  const rejectMutation      = useRejectUser();
  const deleteMutation      = useDeleteUser();
  const updateAccessMutation = useUpdateUserAccess();
  const revokeAccessMutation = useRevokeAccess();
  const { toast }           = useToast();
  const queryClient         = useQueryClient();

  const approveForm = useForm<z.infer<typeof approveSchema>>({
    resolver: zodResolver(approveSchema),
    defaultValues: { accessUsername: "", accessPassword: "", permanent: true, expiryDate: "" },
  });

  const editForm = useForm<z.infer<typeof editAccessSchema>>({
    resolver: zodResolver(editAccessSchema),
    defaultValues: { accessUsername: "", accessPassword: "", permanent: true, expiryDate: "" },
  });

  const openApprove = (user: User) => {
    approveForm.reset({
      accessUsername: user.telegramUsername || String(user.telegramId),
      accessPassword: Math.random().toString(36).slice(-10),
      permanent: true,
      expiryDate: "",
    });
    setApproveUser(user);
  };

  const openEdit = (user: User) => {
    const isPermanent = !user.expiresAt;
    editForm.reset({
      accessUsername: user.accessUsername || "",
      accessPassword: "",
      permanent: isPermanent,
      expiryDate: user.expiresAt ? new Date(user.expiresAt).toISOString().split("T")[0] : "",
    });
    setEditUser(user);
  };

  const submitApprove = (values: z.infer<typeof approveSchema>) => {
    if (!approveUser) return;
    const expiryPayload = buildExpiryPayload(values.permanent, values.expiryDate);
    approveMutation.mutate(
      {
        id: approveUser.id,
        data: {
          accessUsername: values.accessUsername,
          accessPassword: values.accessPassword,
          ...expiryPayload,
        },
      },
      {
        onSuccess: () => {
          toast({ title: "User approved", description: `@${approveUser.telegramUsername || approveUser.telegramId} now has access.` });
          setApproveUser(null);
        },
        onError: (err: any) =>
          toast({ title: "Approval failed", description: err.message, variant: "destructive" }),
      }
    );
  };

  const submitEdit = (values: z.infer<typeof editAccessSchema>) => {
    if (!editUser) return;
    const expiryPayload = buildExpiryPayload(values.permanent, values.expiryDate);
    const data: any = {
      accessUsername: values.accessUsername,
      ...expiryPayload,
    };
    if (values.accessPassword) data.accessPassword = values.accessPassword;

    updateAccessMutation.mutate(
      { id: editUser.id, data },
      {
        onSuccess: () => {
          toast({ title: "Access updated" });
          setEditUser(null);
        },
        onError: (err: any) =>
          toast({ title: "Update failed", description: err.message, variant: "destructive" }),
      }
    );
  };

  const handleReject = (user: User) => {
    rejectMutation.mutate(
      { id: user.id, data: { notes: "Rejected by admin" } },
      {
        onSuccess: () => toast({ title: "User rejected" }),
        onError: (err: any) => toast({ title: "Action failed", description: err.message, variant: "destructive" }),
      }
    );
  };

  const handleDelete = (user: User) => {
    deleteMutation.mutate(user.id, {
      onSuccess: () => { toast({ title: "User deleted" }); setConfirmDelete(null); },
      onError: (err: any) => toast({ title: "Action failed", description: err.message, variant: "destructive" }),
    });
  };

  const handleRevoke = (user: User) => {
    revokeAccessMutation.mutate(user.id, {
      onSuccess: () => {
        toast({ title: "Access revoked", description: `${user.telegramUsername || user.telegramId} moved back to pending.` });
        setConfirmRevoke(null);
      },
      onError: (err: any) =>
        toast({ title: "Failed", description: err.message, variant: "destructive" }),
    });
  };

  const filtered = users?.filter((u) => {
    if (filter !== "all" && u.status !== filter) return false;
    if (search) {
      const s = search.toLowerCase();
      return (
        u.telegramUsername?.toLowerCase().includes(s) ||
        u.firstName?.toLowerCase().includes(s) ||
        u.lastName?.toLowerCase().includes(s) ||
        String(u.telegramId).includes(s) ||
        u.accessUsername?.toLowerCase().includes(s)
      );
    }
    return true;
  });

  return (
    <div className="space-y-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Users</h1>
          <p className="text-sm text-muted-foreground mt-0.5">Manage all registered Telegram users and their access</p>
        </div>
        <Button
          variant="outline"
          size="sm"
          className="h-8 gap-1.5 text-xs"
          onClick={() => queryClient.invalidateQueries({ queryKey: ["users"] })}
          data-testid="button-refresh-users"
        >
          <RefreshCw className="h-3.5 w-3.5" /> Refresh
        </Button>
      </div>

      <div className="bg-card rounded-xl border border-border shadow-sm overflow-hidden">
        <div className="p-4 border-b border-border space-y-3">
          <div className="flex flex-col sm:flex-row gap-3">
            <div className="relative flex-1 max-w-sm">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              <Input
                className="pl-9 h-9 text-sm bg-background text-foreground"
                placeholder="Search name, username, ID, access..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                data-testid="input-search-users"
              />
            </div>
            <div className="flex gap-1 p-1 bg-muted rounded-lg self-start">
              {STATUS_TABS.map((tab) => (
                <button
                  key={tab}
                  onClick={() => setFilter(tab)}
                  data-testid={`filter-${tab}`}
                  className={`px-3 py-1 rounded-md text-xs font-medium capitalize transition-colors ${
                    filter === tab
                      ? "bg-background text-foreground shadow-sm"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                >
                  {tab}
                  {tab !== "all" && (
                    <span className="ml-1 text-[10px] text-muted-foreground">
                      {users?.filter((u) => u.status === tab).length ?? 0}
                    </span>
                  )}
                </button>
              ))}
            </div>
          </div>
        </div>

        <Table>
          <TableHeader>
            <TableRow className="hover:bg-transparent border-border">
              <TableHead className="w-10 pl-4 text-muted-foreground">#</TableHead>
              <TableHead className="text-muted-foreground">User</TableHead>
              <TableHead className="hidden md:table-cell text-muted-foreground">Telegram ID</TableHead>
              <TableHead className="text-muted-foreground">Status</TableHead>
              <TableHead className="hidden lg:table-cell text-muted-foreground">Access</TableHead>
              <TableHead className="hidden xl:table-cell text-muted-foreground">Expiry</TableHead>
              <TableHead className="hidden lg:table-cell text-muted-foreground">Registered</TableHead>
              <TableHead className="text-right pr-4 text-muted-foreground">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              Array.from({ length: 5 }).map((_, i) => (
                <TableRow key={i} className="border-border">
                  <TableCell colSpan={8} className="py-3"><Skeleton className="h-8 w-full" /></TableCell>
                </TableRow>
              ))
            ) : !filtered || filtered.length === 0 ? (
              <TableRow className="border-border">
                <TableCell colSpan={8} className="text-center py-16">
                  <Users className="h-8 w-8 text-muted-foreground/40 mx-auto mb-2" />
                  <p className="text-sm text-muted-foreground">No users found</p>
                </TableCell>
              </TableRow>
            ) : (
              filtered.map((user, idx) => {
                const initials = [user.firstName?.[0], user.lastName?.[0]]
                  .filter(Boolean).join("").toUpperCase() || "?";
                return (
                  <TableRow key={user.id} data-testid={`row-user-${user.id}`}
                    className="hover:bg-muted/40 border-border">
                    <TableCell className="pl-4 text-xs text-muted-foreground font-mono">{idx + 1}</TableCell>
                    <TableCell>
                      <div className="flex items-center gap-2.5">
                        <Avatar className="h-8 w-8 flex-shrink-0">
                          <AvatarFallback className="text-xs font-semibold bg-primary/10 text-primary">
                            {initials}
                          </AvatarFallback>
                        </Avatar>
                        <div className="min-w-0">
                          <p className="text-sm font-medium truncate text-foreground">
                            {user.firstName} {user.lastName}
                          </p>
                          <p className="text-xs text-muted-foreground truncate">
                            @{user.telegramUsername || "—"}
                          </p>
                        </div>
                      </div>
                    </TableCell>
                    <TableCell className="hidden md:table-cell font-mono text-xs text-muted-foreground">
                      {user.telegramId}
                    </TableCell>
                    <TableCell><StatusBadge status={user.status} /></TableCell>
                    <TableCell className="hidden lg:table-cell">
                      {user.accessUsername ? (
                        <span className="font-mono text-xs text-foreground bg-muted px-1.5 py-0.5 rounded">
                          {user.accessUsername}
                        </span>
                      ) : (
                        <span className="text-xs text-muted-foreground">—</span>
                      )}
                    </TableCell>
                    <TableCell className="hidden xl:table-cell">
                      {user.status === "approved" ? (
                        <ExpiryBadge expiresAt={user.expiresAt} />
                      ) : (
                        <span className="text-xs text-muted-foreground">—</span>
                      )}
                    </TableCell>
                    <TableCell className="hidden lg:table-cell text-xs text-muted-foreground">
                      {formatDate(user.registeredAt)}
                    </TableCell>
                    <TableCell className="text-right pr-4">
                      <div className="flex items-center justify-end gap-1">
                        {user.status === "pending" && (
                          <>
                            <Button size="icon" variant="ghost"
                              className="h-8 w-8 text-green-500 hover:text-green-400 hover:bg-green-500/10"
                              onClick={() => openApprove(user)} title="Approve"
                              data-testid={`button-approve-${user.id}`}>
                              <CheckCircle2 className="h-4 w-4" />
                            </Button>
                            <Button size="icon" variant="ghost"
                              className="h-8 w-8 text-red-500 hover:text-red-400 hover:bg-red-500/10"
                              onClick={() => handleReject(user)} title="Reject"
                              data-testid={`button-reject-${user.id}`}>
                              <XCircle className="h-4 w-4" />
                            </Button>
                          </>
                        )}
                        {user.status === "approved" && (
                          <Button size="icon" variant="ghost"
                            className="h-8 w-8 text-blue-500 hover:text-blue-400 hover:bg-blue-500/10"
                            onClick={() => openEdit(user)} title="Edit Access"
                            data-testid={`button-edit-${user.id}`}>
                            <Pencil className="h-4 w-4" />
                          </Button>
                        )}
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <Button size="icon" variant="ghost"
                              className="h-8 w-8 text-muted-foreground hover:text-foreground"
                              data-testid={`button-more-${user.id}`}>
                              <MoreHorizontal className="h-4 w-4" />
                            </Button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align="end" className="w-44 bg-card border-border">
                            {user.status === "pending" && (
                              <>
                                <DropdownMenuItem
                                  className="text-green-500 focus:text-green-500 focus:bg-green-500/10 cursor-pointer"
                                  onClick={() => openApprove(user)}>
                                  <CheckCircle2 className="h-4 w-4 mr-2" /> Approve
                                </DropdownMenuItem>
                                <DropdownMenuItem
                                  className="text-red-500 focus:text-red-500 focus:bg-red-500/10 cursor-pointer"
                                  onClick={() => handleReject(user)}>
                                  <XCircle className="h-4 w-4 mr-2" /> Reject
                                </DropdownMenuItem>
                                <DropdownMenuSeparator className="bg-border" />
                              </>
                            )}
                            {user.status === "approved" && (
                              <>
                                <DropdownMenuItem
                                  className="text-blue-500 focus:text-blue-500 focus:bg-blue-500/10 cursor-pointer"
                                  onClick={() => openEdit(user)}>
                                  <Pencil className="h-4 w-4 mr-2" /> Edit Access
                                </DropdownMenuItem>
                                <DropdownMenuItem
                                  className="text-amber-500 focus:text-amber-500 focus:bg-amber-500/10 cursor-pointer"
                                  onClick={() => setConfirmRevoke(user)}>
                                  <ShieldOff className="h-4 w-4 mr-2" /> Remove Access
                                </DropdownMenuItem>
                                <DropdownMenuSeparator className="bg-border" />
                              </>
                            )}
                            {user.status === "rejected" && (
                              <>
                                <DropdownMenuItem
                                  className="text-green-500 focus:text-green-500 focus:bg-green-500/10 cursor-pointer"
                                  onClick={() => openApprove(user)}>
                                  <CheckCircle2 className="h-4 w-4 mr-2" /> Approve
                                </DropdownMenuItem>
                                <DropdownMenuSeparator className="bg-border" />
                              </>
                            )}
                            <DropdownMenuItem
                              className="text-red-500 focus:text-red-500 focus:bg-red-500/10 cursor-pointer"
                              onClick={() => setConfirmDelete(user)}>
                              <Trash2 className="h-4 w-4 mr-2" /> Delete User
                            </DropdownMenuItem>
                          </DropdownMenuContent>
                        </DropdownMenu>
                      </div>
                    </TableCell>
                  </TableRow>
                );
              })
            )}
          </TableBody>
        </Table>

        {filtered && filtered.length > 0 && (
          <div className="px-4 py-3 border-t border-border bg-muted/30">
            <p className="text-xs text-muted-foreground">
              Showing {filtered.length} of {users?.length ?? 0} users
            </p>
          </div>
        )}
      </div>

      {/* Approve Dialog */}
      <Dialog open={!!approveUser} onOpenChange={(o) => !o && setApproveUser(null)}>
        <DialogContent className="sm:max-w-md bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">Approve User</DialogTitle>
            <DialogDescription className="text-muted-foreground">
              Set access credentials for{" "}
              <span className="font-medium text-foreground">
                @{approveUser?.telegramUsername || approveUser?.telegramId}
              </span>
            </DialogDescription>
          </DialogHeader>
          <Form {...approveForm}>
            <form onSubmit={approveForm.handleSubmit(submitApprove)} className="space-y-4 pt-2">
              <FormField control={approveForm.control} name="accessUsername"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">Access Username</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono text-sm bg-background text-foreground" data-testid="input-access-username" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField control={approveForm.control} name="accessPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">Access Password</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono text-sm bg-background text-foreground" data-testid="input-access-password" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <ExpiryFields control={approveForm.control} watch={approveForm.watch} />
              <DialogFooter className="gap-2">
                <Button type="button" variant="outline" onClick={() => setApproveUser(null)} className="border-border text-foreground">Cancel</Button>
                <Button type="submit" disabled={approveMutation.isPending}
                  className="bg-green-600 hover:bg-green-700 text-white" data-testid="button-confirm-approve">
                  {approveMutation.isPending ? <><Loader2 className="h-4 w-4 mr-2 animate-spin" />Approving...</> : "Approve Access"}
                </Button>
              </DialogFooter>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      {/* Edit Access Dialog */}
      <Dialog open={!!editUser} onOpenChange={(o) => !o && setEditUser(null)}>
        <DialogContent className="sm:max-w-md bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">Edit Access</DialogTitle>
            <DialogDescription className="text-muted-foreground">
              Update credentials or expiry for{" "}
              <span className="font-medium text-foreground">
                @{editUser?.telegramUsername || editUser?.telegramId}
              </span>
            </DialogDescription>
          </DialogHeader>
          <Form {...editForm}>
            <form onSubmit={editForm.handleSubmit(submitEdit)} className="space-y-4 pt-2">
              <FormField control={editForm.control} name="accessUsername"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">Access Username</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono text-sm bg-background text-foreground" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField control={editForm.control} name="accessPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-foreground">New Password <span className="text-muted-foreground font-normal">(leave blank to keep)</span></FormLabel>
                    <FormControl>
                      <Input {...field} placeholder="Leave blank to keep current" className="font-mono text-sm bg-background text-foreground" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <ExpiryFields control={editForm.control} watch={editForm.watch} />
              <DialogFooter className="gap-2">
                <Button type="button" variant="outline" onClick={() => setEditUser(null)} className="border-border text-foreground">Cancel</Button>
                <Button type="submit" disabled={updateAccessMutation.isPending} className="bg-blue-600 hover:bg-blue-700 text-white">
                  {updateAccessMutation.isPending ? <><Loader2 className="h-4 w-4 mr-2 animate-spin" />Saving...</> : "Save Changes"}
                </Button>
              </DialogFooter>
            </form>
          </Form>
        </DialogContent>
      </Dialog>

      {/* Revoke Access Confirm */}
      <Dialog open={!!confirmRevoke} onOpenChange={(o) => !o && setConfirmRevoke(null)}>
        <DialogContent className="sm:max-w-sm bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">Remove Access?</DialogTitle>
            <DialogDescription className="text-muted-foreground">
              This will revoke all credentials for{" "}
              <span className="font-medium text-foreground">
                @{confirmRevoke?.telegramUsername || confirmRevoke?.telegramId}
              </span>{" "}
              and move them back to pending. They cannot log in until re-approved.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter className="gap-2 mt-2">
            <Button variant="outline" onClick={() => setConfirmRevoke(null)} className="border-border text-foreground">Cancel</Button>
            <Button
              disabled={revokeAccessMutation.isPending}
              onClick={() => confirmRevoke && handleRevoke(confirmRevoke)}
              className="bg-amber-600 hover:bg-amber-700 text-white">
              {revokeAccessMutation.isPending ? <><Loader2 className="h-4 w-4 mr-2 animate-spin" />Revoking...</> : "Remove Access"}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Delete Confirm */}
      <Dialog open={!!confirmDelete} onOpenChange={(o) => !o && setConfirmDelete(null)}>
        <DialogContent className="sm:max-w-sm bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">Delete User?</DialogTitle>
            <DialogDescription className="text-muted-foreground">
              This will permanently remove{" "}
              <span className="font-medium text-foreground">
                @{confirmDelete?.telegramUsername || confirmDelete?.telegramId}
              </span>{" "}
              and all their data. This cannot be undone.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter className="gap-2 mt-2">
            <Button variant="outline" onClick={() => setConfirmDelete(null)} className="border-border text-foreground">Cancel</Button>
            <Button variant="destructive" disabled={deleteMutation.isPending}
              onClick={() => confirmDelete && handleDelete(confirmDelete)}
              data-testid="button-confirm-delete">
              {deleteMutation.isPending ? <><Loader2 className="h-4 w-4 mr-2 animate-spin" />Deleting...</> : "Delete User"}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
