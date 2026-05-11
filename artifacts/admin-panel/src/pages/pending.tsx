import { usePendingUsers, useApproveUser, useRejectUser, User } from "@/hooks/use-users";
import { Button } from "@/components/ui/button";
import { CheckCircle2, XCircle } from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { useState } from "react";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Card } from "@/components/ui/card";

const approveSchema = z.object({
  accessUsername: z.string().min(1, "Access username required"),
  accessPassword: z.string().min(1, "Access password required"),
  permanent: z.boolean().default(true),
});

export default function Pending() {
  const { data: pendingUsers, isLoading } = usePendingUsers();
  const approveMutation = useApproveUser();
  const rejectMutation = useRejectUser();
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

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">Action Queue</h2>
        <p className="text-muted-foreground font-mono text-sm mt-1">Awaiting admin disposition.</p>
      </div>

      <div className="grid gap-4">
        {isLoading ? (
          <div className="text-center py-12 font-mono text-muted-foreground border border-border border-dashed rounded-md">Initializing data stream...</div>
        ) : pendingUsers?.length === 0 ? (
          <div className="text-center py-12 font-mono text-muted-foreground border border-border border-dashed rounded-md">Queue empty. All clear.</div>
        ) : (
          pendingUsers?.map(user => (
            <Card key={user.id} className="p-4 flex flex-col md:flex-row md:items-center justify-between gap-4 bg-black/20 hover:bg-black/40 transition-colors border-l-4 border-l-primary">
              <div>
                <div className="font-medium text-lg">{user.firstName} {user.lastName}</div>
                <div className="text-sm text-muted-foreground font-mono">@{user.telegramUsername} | ID: {user.telegramId}</div>
                <div className="text-xs text-muted-foreground font-mono mt-2">Requested: {new Date(user.registeredAt).toLocaleString()}</div>
              </div>
              <div className="flex gap-2">
                <Button variant="outline" className="border-red-500/20 text-red-500 hover:bg-red-500/10 hover:text-red-400 font-mono tracking-wide" onClick={() => handleReject(user.id)}>
                  <XCircle className="w-4 h-4 mr-2" /> REJECT
                </Button>
                <Button className="font-mono tracking-wide" onClick={() => handleApproveClick(user)}>
                  <CheckCircle2 className="w-4 h-4 mr-2" /> APPROVE
                </Button>
              </div>
            </Card>
          ))
        )}
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
