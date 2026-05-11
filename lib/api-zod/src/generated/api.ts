/**
 * BruteTG Admin Panel API — Zod schemas
 */
import * as zod from "zod";

export const HealthCheckResponse = zod.object({
  status: zod.string(),
});

export const AdminLoginBody = zod.object({
  username: zod.string(),
  password: zod.string(),
});

export const AdminLoginResponse = zod.object({
  token: zod.string(),
  username: zod.string(),
});

export const GetAdminMeResponse = zod.object({
  token: zod.string(),
  username: zod.string(),
});

export const UpdateAdminCredentialsBody = zod.object({
  currentPassword: zod.string(),
  newUsername: zod.string().optional(),
  newPassword: zod.string().optional(),
});

export const UpdateAdminCredentialsResponse = zod.object({
  token: zod.string(),
  username: zod.string(),
});

export const ListUsersQueryParams = zod.object({
  status: zod.enum(["pending", "approved", "rejected"]).optional(),
});

export const ListUsersResponseItem = zod.object({
  id: zod.number(),
  telegramId: zod.string(),
  telegramUsername: zod.string().nullish(),
  firstName: zod.string().nullish(),
  lastName: zod.string().nullish(),
  status: zod.enum(["pending", "approved", "rejected"]),
  accessUsername: zod.string().nullish(),
  expiresAt: zod.coerce.date().nullish(),
  registeredAt: zod.coerce.date(),
  approvedAt: zod.coerce.date().nullish(),
  approvedBy: zod.string().nullish(),
  notes: zod.string().nullish(),
});
export const ListUsersResponse = zod.array(ListUsersResponseItem);

export const ListPendingUsersResponseItem = ListUsersResponseItem;
export const ListPendingUsersResponse = zod.array(ListPendingUsersResponseItem);

export const GetUserStatsResponse = zod.object({
  total: zod.number(),
  pending: zod.number(),
  approved: zod.number(),
  rejected: zod.number(),
});

export const RegisterUserBody = zod.object({
  telegramId: zod.string(),
  telegramUsername: zod.string().optional(),
  firstName: zod.string().optional(),
  lastName: zod.string().optional(),
});

export const GetUserParams = zod.object({
  id: zod.coerce.number(),
});

export const GetUserResponse = ListUsersResponseItem;

export const DeleteUserParams = zod.object({
  id: zod.coerce.number(),
});

export const ApproveUserParams = zod.object({
  id: zod.coerce.number(),
});

export const ApproveUserBody = zod.object({
  accessUsername: zod.string(),
  accessPassword: zod.string(),
  permanent: zod.boolean().optional(),
  durationDays: zod.number().nullish(),
  durationHours: zod.number().nullish(),
  durationMinutes: zod.number().nullish(),
  durationSeconds: zod.number().nullish(),
  approvedBy: zod.string().optional(),
  notes: zod.string().optional(),
});

export const ApproveUserResponse = ListUsersResponseItem;

export const RejectUserParams = zod.object({
  id: zod.coerce.number(),
});

export const RejectUserBody = zod.object({
  notes: zod.string().optional(),
  approvedBy: zod.string().optional(),
});

export const RejectUserResponse = ListUsersResponseItem;

export const UpdateUserAccessParams = zod.object({
  id: zod.coerce.number(),
});

export const UpdateUserAccessBody = zod.object({
  accessUsername: zod.string().optional(),
  accessPassword: zod.string().optional(),
  permanent: zod.boolean().optional(),
  durationDays: zod.number().nullish(),
  durationHours: zod.number().nullish(),
  durationMinutes: zod.number().nullish(),
  durationSeconds: zod.number().nullish(),
});

export const UpdateUserAccessResponse = ListUsersResponseItem;

export const CheckUserStatusParams = zod.object({
  telegramId: zod.coerce.string(),
});

export const CheckUserStatusResponse = zod.object({
  telegramId: zod.string(),
  status: zod.string(),
  registered: zod.boolean(),
});

export const VerifyBotUserBody = zod.object({
  telegramId: zod.string(),
  accessUsername: zod.string(),
  accessPassword: zod.string(),
});

export const VerifyBotUserResponse = zod.object({
  valid: zod.boolean(),
  telegramId: zod.string(),
  expiresAt: zod.coerce.date().nullish(),
  message: zod.string().optional(),
});
