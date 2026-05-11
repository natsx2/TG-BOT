import { Router, type IRouter } from "express";
import {
  hashPassword,
  generateToken,
  getAdminCredentials,
  setAdminCredentials,
  verifyToken,
} from "../lib/auth";
import { requireAuth } from "../middlewares/requireAuth";
import {
  AdminLoginBody,
  UpdateAdminCredentialsBody,
} from "@workspace/api-zod";

const router: IRouter = Router();

router.post("/auth/login", async (req, res): Promise<void> => {
  const parsed = AdminLoginBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const { username, password } = parsed.data;
  const creds = await getAdminCredentials();

  if (username !== creds.username || hashPassword(password) !== creds.passwordHash) {
    res.status(401).json({ error: "Invalid username or password" });
    return;
  }

  const token = generateToken(username);
  res.json({ token, username });
});

router.post("/auth/logout", (_req, res): void => {
  res.sendStatus(204);
});

router.get("/auth/me", requireAuth, async (req, res): Promise<void> => {
  const authHeader = req.headers.authorization!;
  const token = authHeader.slice(7);
  const payload = verifyToken(token);
  if (!payload) {
    res.status(401).json({ error: "Unauthorized" });
    return;
  }
  res.json({ token, username: payload.username });
});

router.patch("/auth/credentials", requireAuth, async (req, res): Promise<void> => {
  const parsed = UpdateAdminCredentialsBody.safeParse(req.body);
  if (!parsed.success) {
    res.status(400).json({ error: parsed.error.message });
    return;
  }

  const { currentPassword, newUsername, newPassword } = parsed.data;
  const creds = await getAdminCredentials();

  if (hashPassword(currentPassword) !== creds.passwordHash) {
    res.status(401).json({ error: "Current password is incorrect" });
    return;
  }

  const updatedUsername = newUsername ?? creds.username;
  const updatedPasswordHash = newPassword ? hashPassword(newPassword) : creds.passwordHash;

  await setAdminCredentials(updatedUsername, updatedPasswordHash);
  const token = generateToken(updatedUsername);
  res.json({ token, username: updatedUsername });
});

export default router;
