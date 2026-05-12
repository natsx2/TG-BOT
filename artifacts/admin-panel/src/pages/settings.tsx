import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useMutation } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";
import { AlertTriangle, KeyRound, Loader2, Settings as SettingsIcon, Shield, User } from "lucide-react";
import { useAuth } from "@/hooks/use-auth";

const settingsSchema = z
  .object({
    currentPassword: z.string().min(1, "Current password is required"),
    newUsername: z.string().optional(),
    newPassword: z.string().optional(),
  })
  .refine((data) => data.newUsername || data.newPassword, {
    message: "Provide at least a new username or new password",
    path: ["newUsername"],
  });

export default function Settings() {
  const { toast } = useToast();
  const { logout, user } = useAuth();

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
        body: JSON.stringify(data),
      }),
    onSuccess: () => {
      toast({
        title: "Credentials updated",
        description: "You will be signed out in a moment.",
      });
      form.reset();
      setTimeout(() => logout(), 1500);
    },
    onError: (err: any) => {
      toast({
        title: "Update failed",
        description: err.message,
        variant: "destructive",
      });
    },
  });

  return (
    <div className="space-y-6 max-w-2xl">
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-foreground">Settings</h1>
        <p className="text-sm text-muted-foreground mt-0.5">
          Manage your admin account credentials
        </p>
      </div>

      <div className="bg-card rounded-xl border border-border shadow-sm overflow-hidden">
        <div className="px-5 py-4 border-b border-border flex items-center gap-2">
          <div className="w-7 h-7 rounded-md bg-blue-500/10 flex items-center justify-center">
            <Shield className="h-4 w-4 text-blue-400" />
          </div>
          <div>
            <p className="text-sm font-semibold text-foreground">Account credentials</p>
            <p className="text-xs text-muted-foreground">Changing these will end your current session</p>
          </div>
        </div>

        <div className="p-5">
          <div className="flex items-center gap-3 p-3 bg-muted/30 rounded-lg border border-border mb-6">
            <div className="w-9 h-9 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0">
              <User className="h-4.5 w-4.5 text-primary" />
            </div>
            <div>
              <p className="text-sm font-medium text-foreground">{user?.username || "Admin"}</p>
              <div className="flex items-center gap-1 mt-0.5">
                <Shield className="h-3 w-3 text-muted-foreground" />
                <p className="text-xs text-muted-foreground">Administrator</p>
              </div>
            </div>
          </div>

          <Form {...form}>
            <form
              onSubmit={form.handleSubmit((v) => mutation.mutate(v))}
              className="space-y-5"
            >
              <div className="space-y-1">
                <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
                  Verification
                </p>
                <FormField
                  control={form.control}
                  name="currentPassword"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-sm">
                        <span className="flex items-center gap-1.5">
                          <KeyRound className="h-3.5 w-3.5 text-muted-foreground" />
                          Current password
                        </span>
                      </FormLabel>
                      <FormControl>
                        <Input
                          type="password"
                          placeholder="••••••••"
                          autoComplete="current-password"
                          className="max-w-sm h-9 text-sm bg-muted/30 border-border text-foreground"
                          data-testid="input-current-password"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>

              <div className="space-y-4 pt-1">
                <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
                  New credentials
                </p>
                <FormField
                  control={form.control}
                  name="newUsername"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-sm text-foreground">New username</FormLabel>
                      <FormControl>
                        <Input
                          placeholder="Leave blank to keep current"
                          autoComplete="username"
                          className="max-w-sm h-9 text-sm bg-muted/30 border-border text-foreground"
                          data-testid="input-new-username"
                          {...field}
                        />
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
                      <FormLabel className="text-sm text-foreground">New password</FormLabel>
                      <FormControl>
                        <Input
                          type="password"
                          placeholder="Leave blank to keep current"
                          autoComplete="new-password"
                          className="max-w-sm h-9 text-sm bg-muted/30 border-border text-foreground"
                          data-testid="input-new-password"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>

              <div className="flex items-start gap-3 rounded-lg bg-amber-500/10 border border-amber-500/30 p-4">
                <AlertTriangle className="h-4.5 w-4.5 text-amber-400 flex-shrink-0 mt-0.5" />
                <p className="text-sm text-amber-300">
                  Saving new credentials will immediately sign you out of all active sessions.
                  You will need to sign in again with the updated credentials.
                </p>
              </div>

              <div className="flex items-center gap-3">
                <Button
                  type="submit"
                  disabled={mutation.isPending}
                  className="h-9 text-sm"
                  data-testid="button-save-credentials"
                >
                  {mutation.isPending ? (
                    <><Loader2 className="h-4 w-4 mr-2 animate-spin" /> Saving changes...</>
                  ) : (
                    <>
                      <SettingsIcon className="h-4 w-4 mr-2" />
                      Save changes
                    </>
                  )}
                </Button>
                <Button
                  type="button"
                  variant="ghost"
                  className="h-9 text-sm text-muted-foreground"
                  onClick={() => form.reset()}
                >
                  Reset
                </Button>
              </div>
            </form>
          </Form>
        </div>
      </div>
    </div>
  );
}
