import { useState } from "react";
import {
  useUsers,
  useApproveUser,
  useRejectUser,
  useDeleteUser,
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
} from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { useQueryClient } from "@tanstack/react-query";

const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
});

const STATUS_TABS = ["all", "pending", "approved", "rejected"] as const;

function StatusBadge({ status }: { status: User["status"] }) {
  if (status === "pending")
    return (
      <Badge variant="outline" className="text-amber-600 border-amber-200 bg-amber-50 text-xs font-medium">
        Pending
      </Badge>
    );
  if (status === "approved")
    return (
      <Badge variant="outline" className="text-green-600 border-green-200 bg-green-50 text-xs font-medium">
        Approved
      </Badge>
    );
  return (
    <Badge variant="outline" className="text-red-600 border-red-200 bg-red-50 text-xs font-medium">
      Rejected
    </Badge>
  );
}

export default function UsersPage() {
  const { data: users, isLoading } = useUsers();
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState<(typeof STATUS_TABS)[number]>("all");
  const [approveUser, setApproveUser] = useState<User | null>(null);
  const [confirmDelete, setConfirmDelete] = useState<User | null>(null);

  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();
  const deleteMutation = useDeleteUser();
  const { toast } = useToast();
  const queryClient = useQueryClient();

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
    rejectMutation.mutate(
      { id: user.id, data: { notes: "Rejected by admin" } },
      {
        onSuccess: () =>
          toast({ title: "User rejected", description: `@${user.telegramUsername} has been rejected.` }),
        onError: (err: any) =>
          toast({ title: "Action failed", description: err.message, variant: "destructive" }),
      }
    );
  };

  const handleDelete = (user: User) => {
    deleteMutation.mutate(user.id, {
      onSuccess: () => {
        toast({ title: "User deleted" });
        setConfirmDelete(null);
      },
      onError: (err: any) =>
        toast({ title: "Action failed", description: err.message, variant: "destructive" }),
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
        String(u.telegramId).includes(s)
      );
    }
    return true;
  });

  return (
    <div className="space-y-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-foreground">Users</h1>
          <p className="text-sm text-muted-foreground mt-0.5">
            Manage all registered Telegram users
          </p>
        </div>
        <Button
          variant="outline"
          size="sm"
          className="h-8 gap-1.5 text-xs"
          onClick={() => queryClient.invalidateQueries({ queryKey: ["users"] })}
          data-testid="button-refresh-users"
        >
          <RefreshCw className="h-3.5 w-3.5" />
          Refresh
        </Button>
      </div>

      <div className="bg-white rounded-xl border border-border shadow-sm overflow-hidden">
        <div className="p-4 border-b border-border space-y-3">
          <div className="flex flex-col sm:flex-row gap-3">
            <div className="relative flex-1 max-w-sm">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              <Input
                className="pl-9 h-9 text-sm"
                placeholder="Search by name, username, ID..."
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
                      ? "bg-white text-foreground shadow-sm"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                >
                  {tab}
                  {tab !== "all" && (
                    <span className="ml-1.5 text-[10px] text-muted-foreground">
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
            <TableRow className="hover:bg-transparent">
              <TableHead className="w-12 pl-4">#</TableHead>
              <TableHead>User</TableHead>
              <TableHead className="hidden md:table-cell">Telegram ID</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="hidden lg:table-cell">Access</TableHead>
              <TableHead className="hidden lg:table-cell">Registered</TableHead>
              <TableHead className="text-right pr-4">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              Array.from({ length: 5 }).map((_, i) => (
                <TableRow key={i}>
                  <TableCell colSpan={7} className="py-3">
                    <Skeleton className="h-8 w-full" />
                  </TableCell>
                </TableRow>
              ))
            ) : !filtered || filtered.length === 0 ? (
              <TableRow>
                <TableCell colSpan={7} className="text-center py-16">
                  <Users className="h-8 w-8 text-muted-foreground/40 mx-auto mb-2" />
                  <p className="text-sm text-muted-foreground">No users found</p>
                </TableCell>
              </TableRow>
            ) : (
              filtered.map((user, idx) => {
                const initials = [user.firstName?.[0], user.lastName?.[0]]
                  .filter(Boolean)
                  .join("")
                  .toUpperCase() || "?";
                return (
                  <TableRow
                    key={user.id}
                    data-testid={`row-user-${user.id}`}
                    className="hover:bg-gray-50/50"
                  >
                    <TableCell className="pl-4 text-xs text-muted-foreground font-mono w-12">
                      {idx + 1}
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center gap-2.5">
                        <Avatar className="h-8 w-8 flex-shrink-0">
                          <AvatarFallback className="text-xs font-semibold bg-blue-50 text-blue-600">
                            {initials}
                          </AvatarFallback>
                        </Avatar>
                        <div className="min-w-0">
                          <p className="text-sm font-medium truncate">
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
                    <TableCell>
                      <StatusBadge status={user.status} />
                    </TableCell>
                    <TableCell className="hidden lg:table-cell text-xs text-muted-foreground">
                      {user.accessUsername ? (
                        <span className="font-mono text-foreground">{user.accessUsername}</span>
                      ) : "—"}
                    </TableCell>
                    <TableCell className="hidden lg:table-cell text-xs text-muted-foreground">
                      {new Date(user.registeredAt).toLocaleDateString()}
                    </TableCell>
                    <TableCell className="text-right pr-4">
                      <div className="flex items-center justify-end gap-1">
                        {user.status === "pending" && (
                          <>
                            <Button
                              size="icon"
                              variant="ghost"
                              className="h-8 w-8 text-green-600 hover:text-green-700 hover:bg-green-50"
                              onClick={() => openApprove(user)}
                              title="Approve"
                              data-testid={`button-approve-${user.id}`}
                            >
                              <CheckCircle2 className="h-4 w-4" />
                            </Button>
                            <Button
                              size="icon"
                              variant="ghost"
                              className="h-8 w-8 text-red-500 hover:text-red-600 hover:bg-red-50"
                              onClick={() => handleReject(user)}
                              title="Reject"
                              data-testid={`button-reject-${user.id}`}
                            >
                              <XCircle className="h-4 w-4" />
                            </Button>
                          </>
                        )}
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <Button
                              size="icon"
                              variant="ghost"
                              className="h-8 w-8 text-muted-foreground hover:text-foreground"
                              data-testid={`button-more-${user.id}`}
                            >
                              <MoreHorizontal className="h-4 w-4" />
                            </Button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align="end" className="w-40">
                            {user.status === "pending" && (
                              <>
                                <DropdownMenuItem
                                  className="text-green-600 focus:text-green-600 focus:bg-green-50 cursor-pointer"
                                  onClick={() => openApprove(user)}
                                >
                                  <CheckCircle2 className="h-4 w-4 mr-2" />
                                  Approve
                                </DropdownMenuItem>
                                <DropdownMenuItem
                                  className="text-red-600 focus:text-red-600 focus:bg-red-50 cursor-pointer"
                                  onClick={() => handleReject(user)}
                                >
                                  <XCircle className="h-4 w-4 mr-2" />
                                  Reject
                                </DropdownMenuItem>
                                <DropdownMenuSeparator />
                              </>
                            )}
                            <DropdownMenuItem
                              className="text-red-600 focus:text-red-600 focus:bg-red-50 cursor-pointer"
                              onClick={() => setConfirmDelete(user)}
                            >
                              <Trash2 className="h-4 w-4 mr-2" />
                              Delete
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
          <div className="px-4 py-3 border-t border-border bg-gray-50/50">
            <p className="text-xs text-muted-foreground">
              Showing {filtered.length} of {users?.length ?? 0} users
            </p>
          </div>
        )}
      </div>

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
                      <FormLabel className="text-sm font-medium cursor-pointer">
                        Permanent access
                      </FormLabel>
                      <p className="text-xs text-muted-foreground">
                        Credentials will not expire
                      </p>
                    </div>
                  </FormItem>
                )}
              />
              <DialogFooter className="gap-2">
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => setApproveUser(null)}
                  data-testid="button-cancel-approve"
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

      <Dialog open={!!confirmDelete} onOpenChange={(o) => !o && setConfirmDelete(null)}>
        <DialogContent className="sm:max-w-sm">
          <DialogHeader>
            <DialogTitle>Delete user?</DialogTitle>
            <DialogDescription>
              This will permanently remove{" "}
              <span className="font-medium text-foreground">
                @{confirmDelete?.telegramUsername || confirmDelete?.telegramId}
              </span>{" "}
              and all their data. This cannot be undone.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter className="gap-2 sm:gap-2 mt-2">
            <Button variant="outline" onClick={() => setConfirmDelete(null)}>
              Cancel
            </Button>
            <Button
              variant="destructive"
              disabled={deleteMutation.isPending}
              onClick={() => confirmDelete && handleDelete(confirmDelete)}
              data-testid="button-confirm-delete"
            >
              {deleteMutation.isPending ? (
                <><Loader2 className="h-4 w-4 mr-2 animate-spin" /> Deleting...</>
              ) : (
                "Delete user"
              )}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
