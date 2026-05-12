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
import { Settings2, Save } from "lucide-react";

export default function SettingsPage() {
  const { toast } = useToast();
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

  if (isLoading) return <Shell><div className="text-muted-foreground p-8">Loading settings...</div></Shell>;

  return (
    <Shell>
      <div className="max-w-3xl mx-auto space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-foreground">Tool Settings</h1>
            <p className="text-muted-foreground mt-1">Customize output display and tool behavior.</p>
          </div>
          <Button onClick={handleSave} disabled={updateMutation.isPending} className="gap-2">
            <Save className="h-4 w-4" />
            {updateMutation.isPending ? "Saving..." : "Save Changes"}
          </Button>
        </div>

        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="flex items-center gap-2"><Settings2 className="h-5 w-5 text-primary" /> Output Display</CardTitle>
            <CardDescription>Control which result types are shown to users in Telegram.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {([
              { key: "showOk", label: "Show OK Results", description: "✅ Successful hits are sent to users", color: "text-green-400" },
              { key: "showFail", label: "Show FAIL Results", description: "❌ Failed attempts are sent to users", color: "text-red-400" },
              { key: "showNoCp", label: "Show NO-CP Results", description: "⚠️ Checkpoint/locked accounts are shown", color: "text-yellow-400" },
              { key: "showNoLimit", label: "Show NO-LIMIT Results", description: "♾️ 2FA/special accounts are shown", color: "text-blue-400" },
            ] as const).map(({ key, label, description, color }) => (
              <div key={key} className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
                <div>
                  <Label htmlFor={key} className={`font-medium ${color}`}>{label}</Label>
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

        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle>Notification Settings</CardTitle>
            <CardDescription>Configure how often progress updates are sent.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
              <div>
                <Label htmlFor="notifyEvery" className="font-medium">Notify every N results</Label>
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

        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle>Tool Speed / Delay</CardTitle>
            <CardDescription>Milliseconds between each operation. Lower = faster but more likely to be rate-limited.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {([
              { key: "shareDelay", label: "🔵 SHARE Delay (ms)", min: 0, max: 60000, default: 1000 },
              { key: "crckDelay", label: "🔴 CRCK Delay (ms)", min: 0, max: 60000, default: 500 },
              { key: "createDelay", label: "🟢 CREATE Delay (ms)", min: 0, max: 60000, default: 2000 },
            ] as const).map(({ key, label, min, max }) => (
              <div key={key} className="flex items-center justify-between p-3 rounded-lg border border-border bg-background">
                <Label htmlFor={key} className="font-medium">{label}</Label>
                <Input
                  id={key}
                  type="number"
                  min={min} max={max}
                  value={form[key as keyof typeof form] as number}
                  onChange={e => setForm(f => ({ ...f, [key]: parseInt(e.target.value) || 0 }))}
                  className="w-28 text-right bg-background border-border"
                />
              </div>
            ))}
          </CardContent>
        </Card>

        <div className="text-xs text-muted-foreground">
          Last updated: {settings?.updatedAt ? new Date(settings.updatedAt).toLocaleString() : "Never"}{settings?.updatedBy ? ` by ${settings.updatedBy}` : ""}
        </div>
      </div>
    </Shell>
  );
}
