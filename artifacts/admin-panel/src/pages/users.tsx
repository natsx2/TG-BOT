import { useState } from "react";
import { useUsers, useApproveUser, useRejectUser, useDeleteUser, User } from "@/hooks/use-users";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Checkbox } from "@/components/ui/checkbox";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { CheckCircle2, XCircle, Trash2, Search } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
});

export default function UsersPage() {
  const { data: users, isLoading } = useUsers();
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState<"all" | "pending" | "approved" | "rejected">("all");
  
  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();
  const deleteMutation = useDeleteUser();
  const { toast } = useToast();

  const [approveDialogUser, setApproveDialogUser] = useState<User | null>(null);

  const form = useForm<z.infer<typeof approveSchema>>({
    resolver: zodResolver(approveSchema),
    defaultValues: {
      accessUsername: "",
      accessPassword: "",
      permanent: true,
    },
  });

  const handleApproveClick = (user: User) => {
    form.reset({
      accessUsername: user.telegramUsername || user.telegramId.toString(),
      accessPassword: Math.random().toString(36).slice(-8),
      permanent: true
    });
    setApproveDialogUser(user);
  };

  const submitApprove = (values: z.infer<typeof approveSchema>) => {
    if (!approveDialogUser) return;
    approveMutation.mutate({ id: approveDialogUser.id, data: values }, {
      onSuccess: () => {
        toast({ title: "User approved." });
        setApproveDialogUser(null);
      },
      onError: (err: any) => {
        toast({ title: "Approval failed.", description: err.message, variant: "destructive" });
      }
    });
  };

  const handleReject = (id: number) => {
    if (confirm("Reject this request?")) {
      rejectMutation.mutate({ id, data: { notes: "Rejected by admin" } }, {
        onSuccess: () => toast({ title: "User rejected." }),
        onError: (err: any) => toast({ title: "Action failed.", description: err.message, variant: "destructive" })
      });
    }
  };

  const handleDelete = (id: number) => {
    if (confirm("WARNING: Irrevocably delete this user?")) {
      deleteMutation.mutate(id, {
        onSuccess: () => toast({ title: "User deleted." }),
        onError: (err: any) => toast({ title: "Action failed.", description: err.message, variant: "destructive" })
      });
    }
  };

  const filteredUsers = users?.filter(u => {
    if (filter !== "all" && u.status !== filter) return false;
    if (search) {
      const s = search.toLowerCase();
      return u.telegramUsername?.toLowerCase().includes(s) || 
             u.firstName?.toLowerCase().includes(s) || 
             u.telegramId.toString().includes(s);
    }
    return true;
  });

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">User Database</h2>
        <p className="text-muted-foreground font-mono text-sm mt-1">Manage all identities and access states.</p>
      </div>

      <div className="flex flex-col sm:flex-row items-center gap-4 justify-between">
        <div className="flex items-center gap-2 bg-black/50 border border-border rounded-md px-3 py-1 w-full max-w-sm">
          <Search className="h-4 w-4 text-muted-foreground" />
          <input 
            className="bg-transparent border-none outline-none focus:ring-0 text-sm font-mono flex-1 py-1"
            placeholder="Search by ID, Username..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
        <div className="flex gap-2">
          {(["all", "pending", "approved", "rejected"] as const).map((f) => (
            <Button
              key={f}
              variant={filter === f ? "default" : "outline"}
              size="sm"
              onClick={() => setFilter(f)}
              className="capitalize font-mono text-xs"
            >
              {f}
            </Button>
          ))}
        </div>
      </div>

      <div className="border border-border rounded-md overflow-hidden bg-card">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="font-mono">TG_ID</TableHead>
              <TableHead>Identity</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Access</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading ? (
              <TableRow><TableCell colSpan={5} className="text-center py-8 font-mono text-muted-foreground">Loading...</TableCell></TableRow>
            ) : filteredUsers?.length === 0 ? (
              <TableRow><TableCell colSpan={5} className="text-center py-8 font-mono text-muted-foreground">No records found.</TableCell></TableRow>
            ) : (
              filteredUsers?.map((user) => (
                <TableRow key={user.id}>
                  <TableCell className="font-mono text-xs text-muted-foreground">{user.telegramId}</TableCell>
                  <TableCell>
                    <div className="font-medium">{user.firstName} {user.lastName}</div>
                    <div className="text-xs text-muted-foreground font-mono">@{user.telegramUsername}</div>
                  </TableCell>
                  <TableCell>
                    {user.status === 'pending' && <Badge variant="outline" className="text-yellow-500 border-yellow-500/20 bg-yellow-500/10">PENDING</Badge>}
                    {user.status === 'approved' && <Badge variant="outline" className="text-green-500 border-green-500/20 bg-green-500/10">APPROVED</Badge>}
                    {user.status === 'rejected' && <Badge variant="outline" className="text-red-500 border-red-500/20 bg-red-500/10">REJECTED</Badge>}
                  </TableCell>
                  <TableCell className="font-mono text-xs">
                    {user.accessUsername ? (
                      <span className="text-muted-foreground">User: <span className="text-foreground">{user.accessUsername}</span></span>
                    ) : "-"}
                  </TableCell>
                  <TableCell className="text-right space-x-2">
                    {user.status === 'pending' && (
                      <>
                        <Button size="icon" variant="ghost" className="h-8 w-8 text-green-500 hover:text-green-400 hover:bg-green-500/10" onClick={() => handleApproveClick(user)} title="Approve">
                          <CheckCircle2 className="h-4 w-4" />
                        </Button>
                        <Button size="icon" variant="ghost" className="h-8 w-8 text-red-500 hover:text-red-400 hover:bg-red-500/10" onClick={() => handleReject(user.id)} title="Reject">
                          <XCircle className="h-4 w-4" />
                        </Button>
                      </>
                    )}
                    <Button size="icon" variant="ghost" className="h-8 w-8 text-muted-foreground hover:text-destructive hover:bg-destructive/10" onClick={() => handleDelete(user.id)} title="Delete">
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </div>

      <Dialog open={!!approveDialogUser} onOpenChange={(o) => !o && setApproveDialogUser(null)}>
        <DialogContent className="sm:max-w-md border-border">
          <DialogHeader>
            <DialogTitle>Authorize Access</DialogTitle>
            <p className="text-sm text-muted-foreground font-mono mt-1">Configuring credentials for {approveDialogUser?.telegramUsername || approveDialogUser?.telegramId}</p>
          </DialogHeader>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(submitApprove)} className="space-y-4 pt-4">
              <FormField
                control={form.control}
                name="accessUsername"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Access Username</FormLabel>
                    <FormControl>
                      <Input {...field} className="font-mono" />
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
                      <Input {...field} className="font-mono" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="permanent"
                render={({ field }) => (
                  <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border border-border p-4">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <div className="space-y-1 leading-none">
                      <FormLabel>Permanent Access</FormLabel>
                      <p className="text-xs text-muted-foreground">If unchecked, credentials will expire based on system defaults.</p>
                    </div>
                  </FormItem>
                )}
              />
              <DialogFooter>
                <Button type="button" variant="outline" onClick={() => setApproveDialogUser(null)}>Cancel</Button>
                <Button type="submit" disabled={approveMutation.isPending}>{approveMutation.isPending ? "Committing..." : "Authorize"}</Button>
              </DialogFooter>
            </form>
          </Form>
        </DialogContent>
      </Dialog>
    </div>
  );
}
