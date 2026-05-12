import React, { useState, useEffect } from "react";
import { Link, useLocation } from "wouter";
import { useAuth } from "@/hooks/use-auth";
import { useQuery } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";
import { Button } from "@/components/ui/button";
import {
  Shield,
  LayoutDashboard,
  Users,
  Clock,
  LogOut,
  Activity,
  Settings2,
  Menu,
  X,
  Zap,
  CheckCircle2,
  Bot,
} from "lucide-react";

function usePendingCount() {
  return useQuery<number>({
    queryKey: ["pending-count"],
    queryFn: async () => {
      const data = await apiFetch("/admin/stats");
      return data.pending ?? 0;
    },
    refetchInterval: 8000,
  });
}

const NAV_ITEMS = [
  { href: "/",             icon: LayoutDashboard, label: "Overview",      badge: null },
  { href: "/users/pending",icon: Clock,           label: "Pending",       badge: "pending" },
  { href: "/users",        icon: Users,           label: "All Users",     badge: null },
  { href: "/tasks",        icon: Activity,        label: "Task Monitor",  badge: null },
  { href: "/settings",     icon: Settings2,       label: "Settings",      badge: null },
] as const;

function NavLinks({
  location,
  pendingCount,
  onClick,
}: {
  location: string;
  pendingCount: number;
  onClick?: () => void;
}) {
  return (
    <div className="space-y-0.5">
      {NAV_ITEMS.map(({ href, icon: Icon, label, badge }) => {
        const active = location === href || (href === "/" && location === "");
        const count  = badge === "pending" ? pendingCount : 0;
        return (
          <Link
            key={href}
            href={href}
            onClick={onClick}
            className={`
              group flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium
              transition-all duration-150 relative
              ${active
                ? "bg-primary/15 text-primary border border-primary/20 shadow-sm"
                : "text-muted-foreground hover:bg-secondary/60 hover:text-foreground border border-transparent"
              }
            `}
          >
            <Icon
              size={16}
              className={`flex-shrink-0 transition-colors ${active ? "text-primary" : "group-hover:text-foreground"}`}
            />
            <span className="flex-1 truncate">{label}</span>
            {count > 0 && (
              <span className="flex-shrink-0 min-w-[20px] h-5 px-1.5 rounded-full bg-amber-500 text-white text-[10px] font-bold flex items-center justify-center leading-none">
                {count > 99 ? "99+" : count}
              </span>
            )}
          </Link>
        );
      })}
    </div>
  );
}

export function Shell({ children }: { children: React.ReactNode }) {
  const [location]   = useLocation();
  const { user, logout } = useAuth();
  const [menuOpen, setMenuOpen] = useState(false);
  const { data: pendingCount = 0 } = usePendingCount();

  useEffect(() => { setMenuOpen(false); }, [location]);
  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [menuOpen]);

  const SidebarContent = ({ onLinkClick }: { onLinkClick?: () => void }) => (
    <>
      <div className="h-16 flex items-center px-5 border-b border-border gap-3 flex-shrink-0">
        <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-primary/10 border border-primary/20">
          <Shield className="h-4 w-4 text-primary" />
        </div>
        <div className="flex-1 min-w-0">
          <p className="font-bold text-sm tracking-tight text-foreground leading-none">BruteTG</p>
          <p className="text-[10px] text-muted-foreground mt-0.5 leading-none">Admin Panel</p>
        </div>
        <Zap className="h-3.5 w-3.5 text-primary flex-shrink-0" />
      </div>

      <div className="px-3 pt-4 pb-1">
        <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60 px-1 mb-2">
          Navigation
        </p>
        <NavLinks location={location} pendingCount={pendingCount} onClick={onLinkClick} />
      </div>

      <div className="mt-auto px-3 pb-3 border-t border-border pt-3 flex-shrink-0">
        <div className="flex items-center gap-2.5 px-3 py-2 rounded-lg bg-muted/40 border border-border mb-2">
          <div className="flex items-center justify-center w-7 h-7 rounded-full bg-primary/15 border border-primary/20 flex-shrink-0">
            <Bot className="h-3.5 w-3.5 text-primary" />
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-xs font-semibold text-foreground truncate">{user?.username ?? "admin"}</p>
            <div className="flex items-center gap-1 mt-0.5">
              <CheckCircle2 className="h-2.5 w-2.5 text-green-400" />
              <p className="text-[10px] text-green-400 leading-none">Active session</p>
            </div>
          </div>
        </div>
        <Button
          variant="ghost"
          className="w-full justify-start text-muted-foreground hover:text-destructive hover:bg-destructive/10 gap-2.5 text-sm h-9"
          onClick={() => { onLinkClick?.(); logout(); }}
        >
          <LogOut size={15} />
          Sign Out
        </Button>
      </div>
    </>
  );

  return (
    <div className="flex h-screen overflow-hidden bg-background dark">

      {/* ── Desktop sidebar ─────────────────────────────────────── */}
      <aside className="w-60 border-r border-border bg-card flex-col hidden md:flex flex-shrink-0">
        <SidebarContent />
      </aside>

      {/* ── Mobile: backdrop ────────────────────────────────────── */}
      <div
        className={`fixed inset-0 z-40 bg-black/60 backdrop-blur-sm md:hidden transition-opacity duration-300 ${
          menuOpen ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none"
        }`}
        onClick={() => setMenuOpen(false)}
      />

      {/* ── Mobile: slide-out sidebar ───────────────────────────── */}
      <aside
        className={`
          fixed top-0 left-0 h-full w-72 z-50 bg-card border-r border-border flex flex-col
          transition-transform duration-300 ease-in-out md:hidden
          ${menuOpen ? "translate-x-0 shadow-2xl" : "-translate-x-full"}
        `}
      >
        <div className="h-14 flex items-center px-4 border-b border-border gap-3 flex-shrink-0">
          <div className="flex items-center justify-center w-7 h-7 rounded-md bg-primary/10 border border-primary/20">
            <Shield className="h-3.5 w-3.5 text-primary" />
          </div>
          <div className="flex-1 min-w-0">
            <p className="font-bold text-sm text-foreground leading-none">BruteTG</p>
            <p className="text-[10px] text-muted-foreground mt-0.5">Admin Panel</p>
          </div>
          <Button
            variant="ghost"
            size="icon"
            className="h-8 w-8 text-muted-foreground hover:text-foreground flex-shrink-0"
            onClick={() => setMenuOpen(false)}
          >
            <X size={18} />
          </Button>
        </div>

        <div className="flex-1 flex flex-col overflow-y-auto">
          <div className="px-3 pt-4 pb-1">
            <p className="text-[10px] font-semibold uppercase tracking-widest text-muted-foreground/60 px-1 mb-2">
              Navigation
            </p>
            <NavLinks
              location={location}
              pendingCount={pendingCount}
              onClick={() => setMenuOpen(false)}
            />
          </div>
        </div>

        <div className="px-3 pb-3 border-t border-border pt-3 flex-shrink-0">
          <div className="flex items-center gap-2.5 px-3 py-2 rounded-lg bg-muted/40 border border-border mb-2">
            <div className="flex items-center justify-center w-7 h-7 rounded-full bg-primary/15 border border-primary/20 flex-shrink-0">
              <Bot className="h-3.5 w-3.5 text-primary" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-xs font-semibold text-foreground truncate">{user?.username ?? "admin"}</p>
              <div className="flex items-center gap-1 mt-0.5">
                <CheckCircle2 className="h-2.5 w-2.5 text-green-400" />
                <p className="text-[10px] text-green-400">Active session</p>
              </div>
            </div>
          </div>
          <Button
            variant="ghost"
            className="w-full justify-start text-muted-foreground hover:text-destructive hover:bg-destructive/10 gap-2.5 text-sm h-9"
            onClick={() => { setMenuOpen(false); logout(); }}
          >
            <LogOut size={15} />
            Sign Out
          </Button>
        </div>
      </aside>

      {/* ── Main content ────────────────────────────────────────── */}
      <main className="flex-1 flex flex-col overflow-hidden min-w-0">

        {/* Mobile top bar */}
        <div className="h-14 border-b border-border bg-card flex items-center justify-between px-4 md:hidden flex-shrink-0">
          <Button
            variant="ghost"
            size="icon"
            className="h-9 w-9 text-muted-foreground hover:text-foreground relative"
            onClick={() => setMenuOpen(true)}
            aria-label="Open menu"
          >
            <Menu size={20} />
            {pendingCount > 0 && (
              <span className="absolute -top-0.5 -right-0.5 w-4 h-4 rounded-full bg-amber-500 text-white text-[9px] font-bold flex items-center justify-center">
                {pendingCount > 9 ? "9+" : pendingCount}
              </span>
            )}
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
