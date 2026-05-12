import React from "react";
import { Link, useLocation } from "wouter";
import { useAdminLogout } from "@workspace/api-client-react";
import { Button } from "@/components/ui/button";
import { Shield, LayoutDashboard, Users, UserPlus, LogOut, Activity, Settings2 } from "lucide-react";

export function Shell({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();
  const logoutMutation = useAdminLogout();

  const handleLogout = () => {
    logoutMutation.mutate(undefined, {
      onSuccess: () => {
        window.location.href = "/login";
      }
    });
  };

  return (
    <div className="flex h-screen overflow-hidden bg-background dark">
      {/* Sidebar */}
      <aside className="w-64 border-r border-border bg-card flex flex-col hidden md:flex">
        <div className="h-16 flex items-center px-6 border-b border-border">
          <Shield className="h-6 w-6 text-primary mr-3" />
          <span className="font-semibold text-lg tracking-tight text-foreground">Command Center</span>
        </div>
        
        <nav className="flex-1 px-4 py-6 space-y-1 overflow-y-auto">
          {[
            { href: "/", icon: <LayoutDashboard className="h-5 w-5 mr-3" />, label: "Overview" },
            { href: "/users/pending", icon: <UserPlus className="h-5 w-5 mr-3" />, label: "Pending Review" },
            { href: "/users", icon: <Users className="h-5 w-5 mr-3" />, label: "All Users" },
            { href: "/tasks", icon: <Activity className="h-5 w-5 mr-3" />, label: "Task Monitor" },
            { href: "/settings", icon: <Settings2 className="h-5 w-5 mr-3" />, label: "Tool Settings" },
          ].map(({ href, icon, label }) => (
            <Link key={href} href={href} className={`flex items-center px-3 py-2 rounded-md transition-colors ${location === href ? "bg-primary/10 text-primary" : "text-muted-foreground hover:bg-secondary hover:text-foreground"}`}>
              {icon}{label}
            </Link>
          ))}
        </nav>

        <div className="p-4 border-t border-border">
          <Button 
            variant="ghost" 
            className="w-full justify-start text-muted-foreground hover:text-foreground"
            onClick={handleLogout}
            disabled={logoutMutation.isPending}
          >
            <LogOut className="h-5 w-5 mr-3" />
            Sign Out
          </Button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden">
        <div className="h-16 border-b border-border bg-card flex items-center justify-between px-6 md:hidden">
          <div className="flex items-center">
            <Shield className="h-6 w-6 text-primary mr-3" />
            <span className="font-semibold text-foreground">Command Center</span>
          </div>
          <Button variant="ghost" size="icon" onClick={handleLogout}>
            <LogOut className="h-5 w-5" />
          </Button>
        </div>
        
        <div className="flex-1 overflow-auto bg-background p-6 md:p-8">
          {children}
        </div>
      </main>
    </div>
  );
}
