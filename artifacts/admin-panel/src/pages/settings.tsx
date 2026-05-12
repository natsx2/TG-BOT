import React, { useEffect, useState } from "react";
import { useGetToolSettings, useUpdateToolSettings } from "@workspace/api-client-react";
import { Shell } from "@/components/layout/Shell";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import { useToast } from "@/hooks/use-toast";
import { useAuth } from "@/hooks/use-auth";
import { apiFetch } from "@/lib/api";
import {
  Settings2, Save, ShieldCheck, KeyRound, User2, Lock, Eye, EyeOff,
  Zap, Bell, Timer, RefreshCw, Bot, Activity,
} from "lucide-react";

export default function SettingsPage() {
  const { toast } = useToast();
  const { login } = useAuth();
  const { data: settings, isLoading } = useGetToolSettings();
  const updateMutation = useUpdateToolSettings();

  const [form, setForm] = useState({
    showOk: true,
    showFail: true,
    showNoCp: true,
    showNoLimit: true,
    notifyEvery: 10,
    shareDelay: 1000,
    crckDelay: 500,
    createDelay: 2000,
  });

  const [credForm, setCredForm] = useState({
    currentPassword: "",
    newUsername: "",
    newPassword: "",
    confirmPassword: "",
  });
  const [showCurrentPw, setShowCurrentPw] = useState(false);
  const [showNewPw, setShowNewPw] = useState(false);
  const [credLoading, setCredLoading] = useState(false);

  useEffect(() => {
    if (settings) {
      setForm({
        showOk: settings.showOk,
        showFail: settings.showFail,
        showNoCp: settings.showNoCp,
        showNoLimit: settings.showNoLimit,
        notifyEvery: settings.notifyEvery,
        shareDelay: settings.shareDelay,
        crckDelay: settings.crckDelay,
        createDelay: settings.createDelay,
      });
    }
  }, [settings]);

  const handleSave = () => {
    updateMutation.mutate({ data: form }, {
      onSuccess: () => toast({ title: "Settings saved", description: "Tool settings updated successfully." }),
      onError: () => toast({ variant: "destructive", title: "Failed to save settings" }),
    });
  };

  const handleCredChange = async (e: React.FormEvent) => {
    e.preventDefault();
    if (credForm.newPassword && credForm.newPassword !== credForm.confirmPassword) {
      toast({ variant: "destructive", title: "Passwords don't match", description: "New password and confirm password must be the same." });
      return;
    }
    if (!credForm.newUsername && !credForm.newPassword) {
      toast({ variant: "destructive", title: "Nothing to update", description: "Enter a new username or password." });
      return;
    }
    try {
      setCredLoading(true);
      const res = await apiFetch("/auth/credentials", {
        method: "PATCH",
        body: JSON.stringify({
          currentPassword: credForm.currentPassword,
          ...(credForm.newUsername ? { newUsername: credForm.newUsername } : {}),
          ...(credForm.newPassword ? { newPassword: credForm.newPassword } : {}),
        }),
      });
      login(res.token, { username: res.username });
      setCredForm({ currentPassword: "", newUsername: "", newPassword: "", confirmPassword: "" });
      toast({ title: "Credentials updated", description: "Your admin credentials have been changed." });
    } catch (err: any) {
      toast({ variant: "destructive", title: "Update failed", description: err.message || "Incorrect current password." });
    } finally {
      setCredLoading(false);
    }
  };

  if (isLoading) return <Shell><div className="text-muted-foreground p-8">Loading settings...</div></Shell>;

  return (
    <Shell>
      <div className="max-w-3xl mx-auto space-y-6">

        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-foreground flex items-center gap-3">
              <Settings2 className="h-8 w-8 text-primary" /> Settings
            </h1>
            <p className="text-muted-foreground mt-1">Configure admin credentials, tool behavior, and output display.</p>
          </div>
        </div>

        {/* Admin Credentials */}
        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <ShieldCheck className="h-5 w-5 text-primary" />
              Admin Credentials
            </CardTitle>
            <CardDescription>Change your admin login username and/or password. Current password is always required.</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleCredChange} className="space-y-4">
              <div className="flex items-center gap-3 p-3 rounded-lg border border-border bg-background">
                <Lock className="h-4 w-4 text-muted-foreground flex-shrink-0" />
                <div className="flex-1 space-y-1">
                  <Label htmlFor="currentPassword" className="text-sm font-medium text-foreground">
                    Current Password <span className="text-red-400">*</span>
                  </Label>
                  <div className="relative">
                    <Input
                      id="currentPassword"
                      type={showCurrentPw ? "text" : "password"}
                      value={credForm.currentPassword}
                      onChange={e => setCredForm(f => ({ ...f, currentPassword: e.target.value }))}
                      className="bg-transparent border-0 border-b border-border rounded-none px-0 focus-visible:ring-0 h-8 pr-8"
                      placeholder="Enter current password"
                      required
                    />
                    <button
                      type="button"
                      onClick={() => setShowCurrentPw(v => !v)}
                      className="absolute right-0 top-1 text-muted-foreground hover:text-foreground"
                    >
                      {showCurrentPw ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                    </button>
                  </div>
                </div>
              </div>

              <div className="grid sm:grid-cols-2 gap-4">
                <div className="flex items-center gap-3 p-3 rounded-lg border border-border bg-background">
                  <User2 className="h-4 w-4 text-muted-foreground flex-shrink-0" />
                  <div className="flex-1 space-y-1">
                    <Label htmlFor="newUsername" className="text-sm font-medium text-foreground">New Username</Label>
                    <Input
                      id="newUsername"
                      type="text"
                      value={credForm.newUsername}
                      onChange={e => setCredForm(f => ({ ...f, newUsername: e.target.value }))}
                      className="bg-transparent border-0 border-b border-border rounded-none px-0 focus-visible:ring-0 h-8"
                      placeholder="Leave blank to keep current"
                    />
                  </div>
                </div>

                <div className="flex items-center gap-3 p-3 rounded-lg border border-border bg-background">
                  <KeyRound className="h-4 w-4 text-muted-foreground flex-shrink-0" />
                  <div className="flex-1 space-y-1">
                    <Label htmlFor="newPassword" className="text-sm font-medium text-foreground">New Password</Label>
                    <div className="relative">
                      <Input
                        id="newPassword"
                        type={showNewPw ? "text" : "password"}
                        value={credForm.newPassword}
                        onChange={e => setCredForm(f => ({ ...f, newPassword: e.target.value }))}
                        className="bg-transparent border-0 border-b border-border rounded-none px-0 focus-visible:ring-0 h-8 pr-8"
                        placeholder="Leave blank to keep current"
                      />
                      <button
                        type="button"
                        onClick={() => setShowNewPw(v => !v)}
                        className="absolute right-0 top-1 text-muted-foreground hover:text-foreground"
                      >
                        {showNewPw ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              {credForm.newPassword && (
                <div className="flex items-center gap-3 p-3 rounded-lg border border-border bg-background">
                  <KeyRound className="h-4 w-4 text-muted-foreground flex-shrink-0" />
                  <div className="flex-1 space-y-1">
                    <Label htmlFor="confirmPassword" className="text-sm font-medium text-foreground">Confirm New Password</Label>
                    <Input
                      id="confirmPassword"
                      type="password"
                      value={credForm.confirmPassword}
                      onChange={e => setCredForm(f => ({ ...f, confirmPassword: e.target.value }))}
                      className="bg-transparent border-0 border-b border-border rounded-none px-0 focus-visible:ring-0 h-8"
                      placeholder="Re-enter new password"
                    />
                  </div>
                </div>
              )}

              <Button type="submit" disabled={credLoading || !credForm.currentPassword} className="gap-2">
                {credLoading ? <RefreshCw className="h-4 w-4 animate-spin" /> : <ShieldCheck className="h-4 w-4" />}
                {credLoading ? "Updating..." : "Update Credentials"}
              </Button>
            </form>
          </CardContent>
        </Card>

        <Separator className="bg-border" />

        {/* Tool Output Display */}
        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Activity className="h-5 w-5 text-primary" />
              Output Display
            </CardTitle>
            <CardDescription>Control which result types are shown to users in Telegram.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            {([
              { key: "showOk", label: "Show OK Results", description: "Successful hits are sent to users", color: "text-green-400", icon: "✅" },
              { key: "showFail", label: "Show FAIL Results", description: "Failed attempts are sent to users", color: "text-red-400", icon: "❌" },
              { key: "showNoCp", label: "Show NO-CP Results", description: "Checkpoint/locked accounts are shown", color: "text-yellow-400", icon: "⚠️" },
              { key: "showNoLimit", label: "Show NO-LIMIT Results", description: "2FA/special accounts are shown", color: "text-blue-400", icon: "♾️" },
            ] as const).map(({ key, label, description, color, icon }) => (
              <div key={key} className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
                <div>
                  <Label htmlFor={key} className={`font-medium flex items-center gap-2 ${color}`}>
                    <span>{icon}</span> {label}
                  </Label>
                  <p className="text-xs text-muted-foreground mt-0.5">{description}</p>
                </div>
                <Switch
                  id={key}
                  checked={form[key as keyof typeof form] as boolean}
                  onCheckedChange={(v) => setForm(f => ({ ...f, [key]: v }))}
                />
              </div>
            ))}
          </CardContent>
        </Card>

        {/* Notification Settings */}
        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Bell className="h-5 w-5 text-primary" /> Notification Settings
            </CardTitle>
            <CardDescription>Configure how often progress updates are sent to users.</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
              <div>
                <Label htmlFor="notifyEvery" className="font-medium flex items-center gap-2">
                  <Bell className="h-4 w-4 text-muted-foreground" /> Notify every N results
                </Label>
                <p className="text-xs text-muted-foreground mt-0.5">Send a progress update every N processed items</p>
              </div>
              <Input
                id="notifyEvery"
                type="number"
                min={1} max={1000}
                value={form.notifyEvery}
                onChange={e => setForm(f => ({ ...f, notifyEvery: parseInt(e.target.value) || 10 }))}
                className="w-24 text-right bg-background border-border"
              />
            </div>
          </CardContent>
        </Card>

        {/* Tool Speed */}
        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Timer className="h-5 w-5 text-primary" /> Tool Speed / Delay
            </CardTitle>
            <CardDescription>Milliseconds between each operation. Lower = faster but more rate-limiting risk.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            {([
              { key: "shareDelay", label: "SHARE Delay", color: "text-blue-400", icon: <Zap className="h-4 w-4 text-blue-400" /> },
              { key: "crckDelay", label: "CRCK Delay", color: "text-red-400", icon: <Zap className="h-4 w-4 text-red-400" /> },
              { key: "createDelay", label: "CREATE Delay", color: "text-green-400", icon: <Zap className="h-4 w-4 text-green-400" /> },
            ] as const).map(({ key, label, color, icon }) => (
              <div key={key} className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
                <Label htmlFor={key} className={`font-medium flex items-center gap-2 ${color}`}>
                  {icon} {label} <span className="text-muted-foreground font-normal text-xs">(ms)</span>
                </Label>
                <Input
                  id={key}
                  type="number"
                  min={0} max={60000}
                  value={form[key as keyof typeof form] as number}
                  onChange={e => setForm(f => ({ ...f, [key]: parseInt(e.target.value) || 0 }))}
                  className="w-28 text-right bg-background border-border"
                />
              </div>
            ))}
          </CardContent>
        </Card>

        <div className="flex items-center justify-between">
          <p className="text-xs text-muted-foreground">
            Last updated: {settings?.updatedAt ? new Date(settings.updatedAt).toLocaleString() : "Never"}
            {settings?.updatedBy ? ` by ${settings.updatedBy}` : ""}
          </p>
          <Button onClick={handleSave} disabled={updateMutation.isPending} className="gap-2">
            {updateMutation.isPending ? <RefreshCw className="h-4 w-4 animate-spin" /> : <Save className="h-4 w-4" />}
            {updateMutation.isPending ? "Saving..." : "Save Tool Settings"}
          </Button>
        </div>
      </div>
    </Shell>
  );
}
