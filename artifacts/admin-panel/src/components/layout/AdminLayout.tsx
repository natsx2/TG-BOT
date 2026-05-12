import { ReactNode, useState } from "react";
import { Link, useLocation } from "wouter";
import {
  LayoutDashboard,
  Users,
  Clock,
  Settings,
  LogOut,
  Bot,
  Menu,
  ChevronDown,
  Shield,
  Activity,
  Sun,
  Moon,
} from "lucide-react";
import { useAuth } from "@/hooks/use-auth";
import { useTheme } from "@/hooks/use-theme";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Separator } from "@/components/ui/separator";

const navItems = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/users",     label: "Users",     icon: Users },
  { href: "/pending",   label: "Pending",   icon: Clock },
  { href: "/activity",  label: "Activity",  icon: Activity },
  { href: "/settings",  label: "Settings",  icon: Settings },
];

function NavLink({
  item,
  onClick,
  mobile = false,
}: {
  item: (typeof navItems)[0];
  onClick?: () => void;
  mobile?: boolean;
}) {
  const [location] = useLocation();
  const active = location === item.href;

  if (mobile) {
    return (
      <Link
        href={item.href}
        onClick={onClick}
        data-testid={`nav-mobile-${item.label.toLowerCase()}`}
        className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
          active
            ? "bg-primary text-primary-foreground"
            : "text-foreground hover:bg-muted"
        }`}
      >
        <item.icon className="h-4 w-4 flex-shrink-0" />
        {item.label}
      </Link>
    );
  }

  return (
    <Link
      href={item.href}
      data-testid={`nav-${item.label.toLowerCase()}`}
      className={`flex items-center gap-2 px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${
        active
          ? "bg-primary/10 text-primary"
          : "text-muted-foreground hover:text-foreground hover:bg-muted"
      }`}
    >
      <item.icon className="h-4 w-4" />
      {item.label}
    </Link>
  );
}

export function AdminLayout({ children }: { children: ReactNode }) {
  const { user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <div className="min-h-screen bg-background">
      {/* Top navbar */}
      <nav className="fixed top-0 left-0 right-0 z-50 h-14 bg-card border-b border-border flex items-center px-4 gap-3">
        {/* Mobile menu trigger */}
        <Sheet open={mobileOpen} onOpenChange={setMobileOpen}>
          <SheetTrigger asChild>
            <Button
              variant="ghost"
              size="icon"
              className="md:hidden h-8 w-8 text-foreground"
              data-testid="button-mobile-menu"
            >
              <Menu className="h-5 w-5" />
            </Button>
          </SheetTrigger>
          <SheetContent side="left" className="w-72 p-0 bg-card">
            <div className="flex flex-col h-full">
              <div className="p-5 border-b border-border flex items-center gap-3">
                <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center flex-shrink-0">
                  <Bot className="h-4 w-4 text-primary-foreground" />
                </div>
                <div>
                  <p className="font-semibold text-sm text-foreground">BruteTG</p>
                  <p className="text-xs text-muted-foreground">Admin Panel</p>
                </div>
              </div>

              <nav className="flex-1 p-3 space-y-0.5 overflow-y-auto">
                {navItems.map((item) => (
                  <NavLink
                    key={item.href}
                    item={item}
                    mobile
                    onClick={() => setMobileOpen(false)}
                  />
                ))}
              </nav>

              <div className="p-3 border-t border-border space-y-1">
                {/* Dark/Light mode toggle — only here in slide menu */}
                <button
                  onClick={toggleTheme}
                  data-testid="button-toggle-theme"
                  className="flex w-full items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-foreground hover:bg-muted transition-colors"
                >
                  {theme === "dark" ? (
                    <Sun className="h-4 w-4" />
                  ) : (
                    <Moon className="h-4 w-4" />
                  )}
                  {theme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode"}
                </button>

                <div className="flex items-center gap-3 px-3 py-2 rounded-lg bg-muted/50">
                  <Avatar className="h-7 w-7 flex-shrink-0">
                    <AvatarFallback className="text-xs bg-primary text-primary-foreground font-semibold">
                      {user?.username?.[0]?.toUpperCase() || "A"}
                    </AvatarFallback>
                  </Avatar>
                  <div className="min-w-0">
                    <p className="text-sm font-medium truncate text-foreground">{user?.username || "Admin"}</p>
                    <div className="flex items-center gap-1">
                      <Shield className="h-3 w-3 text-muted-foreground" />
                      <p className="text-xs text-muted-foreground">Administrator</p>
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => { logout(); setMobileOpen(false); }}
                  data-testid="button-mobile-logout"
                  className="flex w-full items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-red-500 hover:bg-red-500/10 transition-colors"
                >
                  <LogOut className="h-4 w-4" />
                  Sign out
                </button>
              </div>
            </div>
          </SheetContent>
        </Sheet>

        {/* Logo */}
        <Link href="/dashboard" className="flex items-center gap-2 flex-shrink-0">
          <div className="w-7 h-7 bg-primary rounded-md flex items-center justify-center">
            <Bot className="h-4 w-4 text-primary-foreground" />
          </div>
          <span className="font-semibold text-sm text-foreground hidden sm:block">BruteTG</span>
        </Link>

        <Separator orientation="vertical" className="h-5 hidden md:block mx-1 bg-border" />

        {/* Desktop nav links */}
        <div className="hidden md:flex items-center gap-0.5">
          {navItems.map((item) => (
            <NavLink key={item.href} item={item} />
          ))}
        </div>

        <div className="flex-1" />

        {/* User dropdown */}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button
              variant="ghost"
              className="flex items-center gap-2 h-8 px-2 rounded-lg text-foreground"
              data-testid="button-user-menu"
            >
              <Avatar className="h-6 w-6">
                <AvatarFallback className="text-[10px] bg-primary text-primary-foreground font-semibold">
                  {user?.username?.[0]?.toUpperCase() || "A"}
                </AvatarFallback>
              </Avatar>
              <span className="text-sm font-medium hidden sm:block text-foreground">
                {user?.username || "Admin"}
              </span>
              <ChevronDown className="h-3.5 w-3.5 text-muted-foreground hidden sm:block" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-52 bg-card border-border">
            <DropdownMenuLabel className="font-normal">
              <div className="flex flex-col space-y-0.5">
                <p className="text-sm font-medium text-foreground">{user?.username || "Admin"}</p>
                <div className="flex items-center gap-1">
                  <Shield className="h-3 w-3 text-muted-foreground" />
                  <p className="text-xs text-muted-foreground">Administrator</p>
                </div>
              </div>
            </DropdownMenuLabel>
            <DropdownMenuSeparator className="bg-border" />
            <DropdownMenuItem asChild>
              <Link href="/settings" className="cursor-pointer text-foreground">
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </Link>
            </DropdownMenuItem>
            <DropdownMenuSeparator className="bg-border" />
            <DropdownMenuItem
              onClick={logout}
              className="text-red-500 focus:text-red-500 focus:bg-red-500/10 cursor-pointer"
              data-testid="button-logout"
            >
              <LogOut className="h-4 w-4 mr-2" />
              Sign out
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </nav>

      <main className="pt-14 min-h-screen bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {children}
        </div>
      </main>
    </div>
  );
}
