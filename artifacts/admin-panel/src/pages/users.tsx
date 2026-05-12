import React, { useState } from "react";
import { useQueryClient } from "@tanstack/react-query";
import {
  useListBotUsers,
  getListBotUsersQueryKey,
  useApproveUser,
  useRejectUser,
  useDeleteBotUser,
  useSetUserExpiry,
  getGetAdminStatsQueryKey
} from "@workspace/api-client-react";
import { Shell } from "@/components/layout/Shell";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { useToast } from "@/hooks/use-toast";
import { Search, MoreHorizontal, CheckCircle, XCircle, Trash2, ShieldAlert, Clock } from "lucide-react";
import { format } from "date-fns";

type BotUser = {
  id: number;
  telegramId: string;
  firstName: string;
  lastName?: string | null;
  username?: string | null;
  status: "pending" | "approved" | "rejected";
  rejectionReason?: string | null;
  expiresAt?: string | null;
  createdAt: string;
};

export default function Users({ defaultFilter = "all" }: { defaultFilter?: "all" | "pending" | "approved" | "rejected" }) {
  const [filter, setFilter] = useState<"all" | "pending" | "approved" | "rejected">(defaultFilter);
  const [search, setSearch] = useState("");
  const [debouncedSearch, setDebouncedSearch] = useState("");
  const [rejectDialogUser, setRejectDialogUser] = useState<number | null>(null);
  const [rejectReason, setRejectReason] = useState("");
  const [expiryDialogUser, setExpiryDialogUser] = useState<BotUser | null>(null);
  const [expiryDate, setExpiryDate] = useState("");

  const queryClient = useQueryClient();
  const { toast } = useToast();

  React.useEffect(() => {
    const timer = setTimeout(() => setDebouncedSearch(search), 300);
    return () => clearTimeout(timer);
  }, [search]);

  const { data: users, isLoading } = useListBotUsers(
    { status: filter, search: debouncedSearch || undefined },
    { query: { queryKey: getListBotUsersQueryKey({ status: filter, search: debouncedSearch || undefined }) } }
  );

  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();
  const deleteMutation = useDeleteBotUser();
  const expiryMutation = useSetUserExpiry();

  const invalidate = () => {
    queryClient.invalidateQueries({ queryKey: getListBotUsersQueryKey() });
    queryClient.invalidateQueries({ queryKey: getGetAdminStatsQueryKey() });
  };

  const handleApprove = (id: number) => {
    approveMutation.mutate({ id }, { onSuccess: () => { toast({ title: "User Approved" }); invalidate(); } });
  };

  const handleReject = () => {
    if (!rejectDialogUser) return;
    rejectMutation.mutate({ id: rejectDialogUser, data: { reason: rejectReason || undefined } }, {
      onSuccess: () => {
        toast({ title: "User Rejected" });
        setRejectDialogUser(null);
        setRejectReason("");
        invalidate();
      }
    });
  };

  const handleDelete = (id: number) => {
    if (!window.confirm("Permanently delete this user?")) return;
    deleteMutation.mutate({ id }, { onSuccess: () => { toast({ title: "User Deleted" }); invalidate(); } });
  };

  const handleSetExpiry = () => {
    if (!expiryDialogUser) return;
    expiryMutation.mutate(
      { id: expiryDialogUser.id, data: { expiresAt: expiryDate || null } },
      {
        onSuccess: () => {
          toast({ title: expiryDate ? "Expiry set" : "Expiry removed" });
          setExpiryDialogUser(null);
          setExpiryDate("");
          invalidate();
        }
      }
    );
  };

  const openExpiryDialog = (user: BotUser) => {
    setExpiryDialogUser(user);
    setExpiryDate(user.expiresAt ? user.expiresAt.substring(0, 10) : "");
  };

  const getStatusBadge = (status: string, expiresAt?: string | null) => {
    const expired = expiresAt && new Date() > new Date(expiresAt);
    if (status === "approved" && expired) {
      return <Badge variant="outline" className="text-orange-400 border-orange-400/20 bg-orange-400/10">Expired</Badge>;
    }
    switch (status) {
      case "pending": return <Badge variant="outline" className="text-yellow-500 border-yellow-500/20 bg-yellow-500/10">Pending</Badge>;
      case "approved": return <Badge variant="outline" className="text-green-500 border-green-500/20 bg-green-500/10">Approved</Badge>;
      case "rejected": return <Badge variant="outline" className="text-red-500 border-red-500/20 bg-red-500/10">Rejected</Badge>;
      default: return <Badge>{status}</Badge>;
    }
  };

  return (
    <Shell>
      <div className="max-w-7xl mx-auto space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-foreground">User Management</h1>
          <p className="text-muted-foreground mt-1">Review and manage bot access requests.</p>
        </div>

        <div className="flex flex-col sm:flex-row items-center gap-4 bg-card p-4 rounded-lg border border-border">
          <div className="relative flex-1 w-full">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
            <Input placeholder="Search by name, username, or ID..."
              value={search} onChange={(e) => setSearch(e.target.value)}
              className="pl-9 bg-background border-border" />
          </div>
          <div className="flex gap-2 w-full sm:w-auto overflow-x-auto pb-2 sm:pb-0">
            {(["all", "pending", "approved", "rejected"] as const).map((f) => (
              <Button key={f} variant={filter === f ? "default" : "outline"}
                onClick={() => setFilter(f)} className="capitalize whitespace-nowrap">
                {f}
              </Button>
            ))}
          </div>
        </div>

        <div className="bg-card rounded-lg border border-border overflow-hidden">
          <Table>
            <TableHeader className="bg-secondary/50">
              <TableRow className="border-border hover:bg-transparent">
                <TableHead>User</TableHead>
                <TableHead>Telegram ID</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Expiry</TableHead>
                <TableHead>Joined</TableHead>
                <TableHead className="text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {isLoading ? (
                <TableRow><TableCell colSpan={6} className="text-center py-8 text-muted-foreground">Loading users...</TableCell></TableRow>
              ) : !users?.length ? (
                <TableRow>
                  <TableCell colSpan={6} className="text-center py-16">
                    <ShieldAlert className="h-12 w-12 mx-auto text-muted-foreground/50 mb-4" />
                    <p className="text-lg font-medium text-foreground">No users found</p>
                    <p className="text-muted-foreground">Try adjusting your search or filters.</p>
                  </TableCell>
                </TableRow>
              ) : (
                (users as BotUser[]).map((user) => (
                  <TableRow key={user.id} className="border-border hover:bg-secondary/30">
                    <TableCell>
                      <div className="flex items-center gap-3">
                        <Avatar className="h-9 w-9 border border-border">
                          <AvatarFallback className="bg-primary/20 text-primary">{user.firstName[0]}</AvatarFallback>
                        </Avatar>
                        <div>
                          <p className="font-medium text-foreground">{user.firstName} {user.lastName}</p>
                          <p className="text-sm text-muted-foreground">@{user.username || "—"}</p>
                        </div>
                      </div>
                    </TableCell>
                    <TableCell className="font-mono text-sm text-muted-foreground">{user.telegramId}</TableCell>
                    <TableCell>{getStatusBadge(user.status, user.expiresAt)}</TableCell>
                    <TableCell className="text-sm text-muted-foreground">
                      {user.expiresAt ? (
                        <span className={new Date() > new Date(user.expiresAt) ? "text-red-400" : "text-green-400"}>
                          {format(new Date(user.expiresAt), "MMM d, yyyy")}
                        </span>
                      ) : (
                        <span className="text-muted-foreground/50">Never</span>
                      )}
                    </TableCell>
                    <TableCell className="text-muted-foreground text-sm">
                      {format(new Date(user.createdAt), "MMM d, yyyy")}
                    </TableCell>
                    <TableCell className="text-right">
                      <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                          <Button variant="ghost" size="icon" className="hover:bg-secondary">
                            <MoreHorizontal className="h-4 w-4" />
                          </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="end" className="w-52 bg-card border-border">
                          {user.status !== "approved" && (
                            <DropdownMenuItem onClick={() => handleApprove(user.id)} className="cursor-pointer text-green-500 focus:text-green-600 focus:bg-green-500/10">
                              <CheckCircle className="h-4 w-4 mr-2" /> Approve
                            </DropdownMenuItem>
                          )}
                          {user.status !== "rejected" && (
                            <DropdownMenuItem onClick={() => setRejectDialogUser(user.id)} className="cursor-pointer text-yellow-500 focus:text-yellow-600 focus:bg-yellow-500/10">
                              <XCircle className="h-4 w-4 mr-2" /> Reject
                            </DropdownMenuItem>
                          )}
                          {user.status === "approved" && (
                            <DropdownMenuItem onClick={() => openExpiryDialog(user)} className="cursor-pointer text-blue-400 focus:text-blue-500 focus:bg-blue-500/10">
                              <Clock className="h-4 w-4 mr-2" /> Set Expiry
                            </DropdownMenuItem>
                          )}
                          <DropdownMenuItem onClick={() => handleDelete(user.id)} className="cursor-pointer text-red-500 focus:text-red-600 focus:bg-red-500/10">
                            <Trash2 className="h-4 w-4 mr-2" /> Delete
                          </DropdownMenuItem>
                        </DropdownMenuContent>
                      </DropdownMenu>
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </div>
      </div>

      {/* Reject Dialog */}
      <Dialog open={!!rejectDialogUser} onOpenChange={(open) => !open && setRejectDialogUser(null)}>
        <DialogContent className="sm:max-w-[425px] bg-card border-border">
          <DialogHeader><DialogTitle className="text-foreground">Reject User</DialogTitle></DialogHeader>
          <div className="grid gap-4 py-4">
            <div className="space-y-2">
              <Label htmlFor="reason" className="text-foreground">Reason (Optional)</Label>
              <Textarea id="reason" placeholder="Brief reason for rejection..."
                value={rejectReason} onChange={(e) => setRejectReason(e.target.value)}
                className="bg-background border-border" />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setRejectDialogUser(null)}>Cancel</Button>
            <Button variant="destructive" onClick={handleReject} disabled={rejectMutation.isPending}>
              {rejectMutation.isPending ? "Rejecting..." : "Confirm Rejection"}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Expiry Dialog */}
      <Dialog open={!!expiryDialogUser} onOpenChange={(open) => !open && setExpiryDialogUser(null)}>
        <DialogContent className="sm:max-w-[400px] bg-card border-border">
          <DialogHeader>
            <DialogTitle className="text-foreground">⏰ Set Access Expiry</DialogTitle>
          </DialogHeader>
          <div className="py-4 space-y-3">
            <p className="text-sm text-muted-foreground">
              Set an expiry date for <strong className="text-foreground">{expiryDialogUser?.firstName}</strong>. Leave blank to remove expiry (unlimited access).
            </p>
            <div className="space-y-2">
              <Label htmlFor="expiry" className="text-foreground">Expiry Date</Label>
              <Input id="expiry" type="date" value={expiryDate}
                onChange={(e) => setExpiryDate(e.target.value)}
                className="bg-background border-border" />
            </div>
          </div>
          <DialogFooter className="gap-2">
            <Button variant="outline" onClick={() => { setExpiryDialogUser(null); setExpiryDate(""); }}>Cancel</Button>
            {expiryDate && (
              <Button variant="outline" className="text-red-400" onClick={() => setExpiryDate("")}>Clear</Button>
            )}
            <Button onClick={handleSetExpiry} disabled={expiryMutation.isPending}>
              {expiryMutation.isPending ? "Saving..." : expiryDate ? "Set Expiry" : "Remove Expiry"}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </Shell>
  );
}
