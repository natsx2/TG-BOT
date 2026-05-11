# BruteTG

A Telegram bot management system — run the bot, approve/reject user access requests, and manage credentials from a dark-themed admin panel.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 8080, served at /api)
- `cd bot && python bot.py` — run the Telegram bot
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM (tables: `bot_users`, `admin_settings`)
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)
- Bot: Python 3.11, python-telegram-bot==21.11.1
- Admin panel: React + Vite, shadcn/ui, TanStack Query, wouter

## Where things live

- `artifacts/api-server/src/routes/` — Express routes: auth.ts, users.ts, bot.ts
- `artifacts/api-server/src/lib/auth.ts` — JWT signing, password hashing, admin credential management
- `artifacts/admin-panel/src/` — React admin panel (pages: login, dashboard, users, pending, settings)
- `artifacts/admin-panel/src/lib/api.ts` — fetch wrapper injecting Bearer token
- `artifacts/admin-panel/src/hooks/use-auth.tsx` — auth context (login/logout/token)
- `bot/bot.py` — Telegram bot with keep-alive thread and all commands
- `lib/db/src/schema/users.ts` — source-of-truth DB schema

## Architecture decisions

- JWT-based admin auth stored in localStorage under `brutetg_token`
- Admin credentials stored in `admin_settings` table (hashed passwords with bcrypt)
- Bot keep-alive thread pings `/api/healthz` every 14 minutes to prevent cold starts
- API uses Zod schemas derived from Drizzle schema via `drizzle-zod`
- Admin panel uses direct fetch (not generated hooks) since the OpenAPI spec only covers healthz

## Product

- Telegram bot accepting user registrations and providing menu-driven tools
- Admin panel for reviewing pending users, granting/revoking access, and managing admin credentials
- Bot commands: /start, /menu, /status, /au2, /fbclone, /nika, /logout, /help

## User preferences

- Default admin credentials: username `admin`, password `admin321`
- Bot token stored as `BOT_TOKEN` env var

## Gotchas

- Always run `pnpm --filter @workspace/db run push` after DB schema changes
- Bot uses `API_BASE_URL` env var (defaults to `http://localhost:80/api`) for keep-alive pings
- When deploying on Render: set `BOT_TOKEN`, `DATABASE_URL`, `SESSION_SECRET`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
