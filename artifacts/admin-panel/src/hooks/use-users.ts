import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { apiFetch } from "@/lib/api";

export type User = {
  id: number;
  telegramId: string;
  telegramUsername: string;
  firstName: string;
  lastName: string;
  status: "pending" | "approved" | "rejected";
  accessUsername?: string;
  expiresAt?: string;
  registeredAt: string;
  approvedAt?: string;
  approvedBy?: number;
  notes?: string;
};

export type Stats = {
  total: number;
  pending: number;
  approved: number;
  rejected: number;
};

export function useUsers() {
  return useQuery<User[]>({
    queryKey: ["users"],
    queryFn: () => apiFetch("/users"),
  });
}

export function usePendingUsers() {
  return useQuery<User[]>({
    queryKey: ["users", "pending"],
    queryFn: () => apiFetch("/users/pending"),
  });
}

export function useStats() {
  return useQuery<Stats>({
    queryKey: ["users", "stats"],
    queryFn: () => apiFetch("/users/stats"),
  });
}

export function useApproveUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: any }) =>
      apiFetch(`/users/${id}/approve`, {
        method: "PATCH",
        body: JSON.stringify(data),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });
}

export function useRejectUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: any }) =>
      apiFetch(`/users/${id}/reject`, {
        method: "PATCH",
        body: JSON.stringify(data),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });
}

export function useDeleteUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: number) =>
      apiFetch(`/users/${id}`, {
        method: "DELETE",
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });
}
