import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";

export type User = {
  id: number;
  telegramId: string;
  telegramUsername: string | null;
  firstName: string;
  lastName: string | null;
  status: "pending" | "approved" | "rejected";
  accessUsername?: string | null;
  expiresAt?: string | null;
  registeredAt: string;
  createdAt: string;
  notes?: string | null;
};

export function usePendingUsers() {
  return useQuery<User[]>({
    queryKey: ["users", "pending"],
    queryFn: () => apiFetch("/admin/users?status=pending"),
    refetchInterval: 8000,
  });
}

export function useApproveUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: number; data?: Record<string, unknown> }) =>
      apiFetch(`/admin/users/${id}/approve`, {
        method: "POST",
        body: JSON.stringify(data ?? {}),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });
}

export function useRejectUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: number; data?: Record<string, unknown> }) =>
      apiFetch(`/admin/users/${id}/reject`, {
        method: "POST",
        body: JSON.stringify(data ?? {}),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });
}
