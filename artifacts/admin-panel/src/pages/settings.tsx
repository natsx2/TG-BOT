import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useMutation } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";
import { AlertCircle } from "lucide-react";
import { useAuth } from "@/hooks/use-auth";

const settingsSchema = z.object({
  currentPassword: z.string().min(1, "Current password required"),
  newUsername: z.string().optional(),
  newPassword: z.string().optional(),
}).refine(data => data.newUsername || data.newPassword, {
  message: "Provide either a new username or new password",
  path: ["newUsername"]
});

export default function Settings() {
  const { toast } = useToast();
  const { logout } = useAuth();

  const form = useForm<z.infer<typeof settingsSchema>>({
    resolver: zodResolver(settingsSchema),
    defaultValues: {
      currentPassword: "",
      newUsername: "",
      newPassword: "",
    },
  });

  const mutation = useMutation({
    mutationFn: (data: z.infer<typeof settingsSchema>) =>
      apiFetch("/auth/credentials", {
        method: "PATCH",
        body: JSON.stringify(data)
      }),
    onSuccess: () => {
      toast({ title: "Credentials updated. Disconnecting session." });
      form.reset();
      setTimeout(() => logout(), 1500);
    },
    onError: (err: any) => {
      toast({ title: "Update failed.", description: err.message, variant: "destructive" });
    }
  });

  const onSubmit = (values: z.infer<typeof settingsSchema>) => {
    mutation.mutate(values);
  };

  return (
    <div className="space-y-6 max-w-2xl">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">System Configuration</h2>
        <p className="text-muted-foreground font-mono text-sm mt-1">Manage operator identity.</p>
      </div>

      <Card className="border-border">
        <CardHeader>
          <CardTitle>Operator Credentials</CardTitle>
          <CardDescription>Update your login credentials. This will terminate your current session.</CardDescription>
        </CardHeader>
        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
              <FormField
                control={form.control}
                name="currentPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Current Passphrase</FormLabel>
                    <FormControl>
                      <Input type="password" {...field} className="font-mono bg-black/50 max-w-sm" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <div className="pt-4 pb-2">
                <div className="text-xs uppercase tracking-wider text-muted-foreground font-bold mb-4">New Parameters</div>
                <div className="space-y-4">
                  <FormField
                    control={form.control}
                    name="newUsername"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>New Operator ID</FormLabel>
                        <FormControl>
                          <Input {...field} placeholder="Leave blank to keep current" className="font-mono bg-black/50 max-w-sm" />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name="newPassword"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>New Passphrase</FormLabel>
                        <FormControl>
                          <Input type="password" {...field} placeholder="Leave blank to keep current" className="font-mono bg-black/50 max-w-sm" />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                </div>
              </div>

              <div className="bg-destructive/10 border border-destructive/20 p-4 rounded-md flex items-start gap-3 mt-6">
                <AlertCircle className="w-5 h-5 text-destructive mt-0.5" />
                <p className="text-sm text-destructive-foreground font-mono">Modifying credentials will immediately invalidate all active tokens and require re-authentication.</p>
              </div>

              <Button type="submit" variant="destructive" disabled={mutation.isPending} className="font-mono uppercase tracking-wider mt-4">
                {mutation.isPending ? "Executing..." : "Commit Changes"}
              </Button>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
}
