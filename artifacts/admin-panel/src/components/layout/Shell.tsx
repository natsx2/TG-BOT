import React, { useState, useEffect } from "react";
import { Link, useLocation } from "wouter";
import { useAuth } from "@/hooks/use-auth";
import { Button } from "@/components/ui/button";
import {
  Shield, LayoutDashboard, Users, UserPlus, LogOut,
  Activity, Settings2, Menu, X, Zap,
} from "lucide-react";

const NAV_ITEMS = [
  { href: "/", icon: LayoutDashboard, label: "Overview" },
  { href: "/users/pending", icon: UserPlus, label: "Pending Review" },
  { href: "/users", icon: Users, label: "All Users" },
  { href: "/tasks", icon: Activity, label: "Task Monitor" },
  { href: "/settings", icon: Settings2, label: "Tool Settings" },
];

function NavLinks({ location, onClick }: { location: string; onClick?: () => void }) {
  return (
    <>
      {NAV_ITEMS.map(({ href, icon: Icon, label }) => {
        const active = location === href;
        return (
          <Link
            key={href}
            href={href}
            onClick={onClick}
            className={`flex items-center gap-3 px-3 py-2.5 rounded-md text-sm font-medium transition-all duration-150 ${
              active
                ? "bg-primary/15 text-primary border border-primary/20 shadow-sm"
                : "text-muted-foreground hover:bg-secondary hover:text-foreground"
            }`}
          >
            <Icon size={17} className={`flex-shrink-0 ${active ? "text-primary" : ""}`} />
            {label}
          </Link>
        );
      })}
    </>
  );
}

export function Shell({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();
  const { logout } = useAuth();
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => { setMenuOpen(false); }, [location]);

  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [menuOpen]);

  return (
    <div className="flex h-screen overflow-hidden bg-background dark">

      {/* ── Desktop sidebar ─────────────────────────────────── */}
      <aside className="w-64 border-r border-border bg-card flex-col hidden md:flex">
        <div className="h-16 flex items-center px-5 border-b border-border gap-3">
          <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-primary/10 border border-primary/20">
            <Shield className="h-4 w-4 text-primary" />
          </div>
          <span className="font-bold text-base tracking-tight text-foreground">BruteTG</span>
          <Zap className="h-3.5 w-3.5 text-primary ml-auto" />
        </div>

        <nav className="flex-1 px-3 py-5 space-y-0.5 overflow-y-auto">
          <NavLinks location={location} />
        </nav>

        <div className="p-3 border-t border-border">
          <Button
            variant="ghost"
            className="w-full justify-start text-muted-foreground hover:text-destructive hover:bg-destructive/10 gap-3 text-sm"
            onClick={logout}
          >
            <LogOut size={16} />Sign Out
          </Button>
        </div>
      </aside>

      {/* ── Mobile: overlay ────────────────────────────────── */}
      {menuOpen && (
        <div
          className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm md:hidden"
          onClick={() => setMenuOpen(false)}
        />
      )}

      {/* ── Mobile: slide-out sidebar ──────────────────────── */}
      <aside
        className={`
          fixed top-0 left-0 h-full w-72 z-50 bg-card border-r border-border flex flex-col
          transition-transform duration-300 ease-in-out md:hidden
          ${menuOpen ? "translate-x-0" : "-translate-x-full"}
        `}
      >
        <div className="h-14 flex items-center px-4 border-b border-border gap-3">
          <div className="flex items-center justify-center w-7 h-7 rounded-md bg-primary/10 border border-primary/20">
            <Shield className="h-3.5 w-3.5 text-primary" />
          </div>
          <span className="font-bold text-sm text-foreground">BruteTG</span>
          <Button
            variant="ghost"
            size="icon"
            className="ml-auto h-8 w-8 text-muted-foreground hover:text-foreground"
            onClick={() => setMenuOpen(false)}
          >
            <X size={18} />
          </Button>
        </div>

        <nav className="flex-1 px-3 py-4 space-y-0.5 overflow-y-auto">
          <NavLinks location={location} onClick={() => setMenuOpen(false)} />
        </nav>

        <div className="p-3 border-t border-border">
          <Button
            variant="ghost"
            className="w-full justify-start text-muted-foreground hover:text-destructive hover:bg-destructive/10 gap-3 text-sm"
            onClick={() => { setMenuOpen(false); logout(); }}
          >
            <LogOut size={16} />Sign Out
          </Button>
        </div>
      </aside>

      {/* ── Main content ───────────────────────────────────── */}
      <main className="flex-1 flex flex-col overflow-hidden min-w-0">
        {/* Mobile top bar */}
        <div className="h-14 border-b border-border bg-card flex items-center justify-between px-4 md:hidden flex-shrink-0">
          <Button
            variant="ghost"
            size="icon"
            className="h-9 w-9 text-muted-foreground hover:text-foreground"
            onClick={() => setMenuOpen(true)}
            aria-label="Open menu"
          >
            <Menu size={20} />
          </Button>

          <div className="flex items-center gap-2">
            <div className="flex items-center justify-center w-7 h-7 rounded-md bg-primary/10 border border-primary/20">
              <Shield className="h-3.5 w-3.5 text-primary" />
            </div>
            <span className="font-bold text-sm text-foreground">BruteTG</span>
          </div>

          <Button
            variant="ghost"
            size="icon"
            className="h-9 w-9 text-muted-foreground hover:text-destructive hover:bg-destructive/10"
            onClick={logout}
            aria-label="Sign out"
          >
            <LogOut size={18} />
          </Button>
        </div>

        <div className="flex-1 overflow-auto bg-background p-4 md:p-8">
          {children}
        </div>
      </main>
    </div>
  );
}
