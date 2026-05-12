import { useState } from "react";
import { Switch, Route, Router as WouterRouter } from "wouter";
import { AuthProvider, useAuth } from "@/lib/auth";
import Login from "@/pages/Login";
import Dashboard from "@/pages/Dashboard";
import BotControl from "@/pages/BotControl";
import Tools from "@/pages/Tools";
import Logs from "@/pages/Logs";
import Settings from "@/pages/Settings";
import Users from "@/pages/Users";
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";

const PAGE_TITLES: Record<string, string> = {
  "/": "Dashboard",
  "/bot": "Bot Control",
  "/users": "Users",
  "/tools": "Tools",
  "/logs": "Activity Logs",
  "/settings": "Settings",
};

function AppShell() {
  const { user, loading } = useAuth();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <div className="w-6 h-6 border-2 border-primary border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!user) return <Login />;

  return (
    <div className="min-h-screen bg-background">
      <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />
      <div className="lg:pl-64 flex flex-col min-h-screen">
        <Switch>
          {Object.entries(PAGE_TITLES).map(([path, title]) => (
            <Route key={path} path={path}>
              <Navbar title={title} onMenuToggle={() => setSidebarOpen(v => !v)} />
              <main className="flex-1 p-4 lg:p-6">
                {path === "/" && <Dashboard />}
                {path === "/bot" && <BotControl />}
                {path === "/users" && <Users />}
                {path === "/tools" && <Tools />}
                {path === "/logs" && <Logs />}
                {path === "/settings" && <Settings />}
              </main>
            </Route>
          ))}
        </Switch>
      </div>
    </div>
  );
}

function App() {
  return (
    <AuthProvider>
      <WouterRouter base={import.meta.env.BASE_URL.replace(/\/$/, "")}>
        <AppShell />
      </WouterRouter>
    </AuthProvider>
  );
}

export default App;
