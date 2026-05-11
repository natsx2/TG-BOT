import { Switch, Route, Router as WouterRouter, useLocation } from "wouter";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/not-found";
import { AuthProvider, useAuth } from "@/hooks/use-auth";
import { ThemeProvider } from "@/hooks/use-theme";
import { AdminLayout } from "@/components/layout/AdminLayout";
import Login from "@/pages/login";
import Dashboard from "@/pages/dashboard";
import Users from "@/pages/users";
import Pending from "@/pages/pending";
import Settings from "@/pages/settings";
import Activity from "@/pages/activity";

const queryClient = new QueryClient();

function ProtectedRoute({ component: Component, ...rest }: any) {
  const { token, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center font-mono text-muted-foreground">
        Verifying access...
      </div>
    );
  }

  if (!token) return <Login />;

  return (
    <AdminLayout>
      <Component {...rest} />
    </AdminLayout>
  );
}

function Router() {
  const { token, isLoading } = useAuth();
  const [location, setLocation] = useLocation();

  if (location === "/") {
    if (!isLoading) {
      if (token) setLocation("/dashboard");
      else setLocation("/login");
    }
    return null;
  }

  return (
    <Switch>
      <Route path="/login">
        {token ? () => { setLocation("/dashboard"); return null; } : <Login />}
      </Route>
      <Route path="/dashboard"><ProtectedRoute component={Dashboard} /></Route>
      <Route path="/users"><ProtectedRoute component={Users} /></Route>
      <Route path="/pending"><ProtectedRoute component={Pending} /></Route>
      <Route path="/activity"><ProtectedRoute component={Activity} /></Route>
      <Route path="/settings"><ProtectedRoute component={Settings} /></Route>
      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  return (
    <ThemeProvider>
      <QueryClientProvider client={queryClient}>
        <TooltipProvider>
          <WouterRouter base={import.meta.env.BASE_URL.replace(/\/$/, "")}>
            <AuthProvider>
              <Router />
            </AuthProvider>
          </WouterRouter>
          <Toaster />
        </TooltipProvider>
      </QueryClientProvider>
    </ThemeProvider>
  );
}

export default App;
