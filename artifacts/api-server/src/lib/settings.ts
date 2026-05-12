import { db } from "@workspace/db";
import { toolSettingsTable } from "@workspace/db";
import type { ToolSettings } from "@workspace/db";

let cached: ToolSettings | null = null;
let cacheTime = 0;
const CACHE_TTL = 30_000;

export async function getSettings(): Promise<ToolSettings> {
  const now = Date.now();
  if (cached && now - cacheTime < CACHE_TTL) return cached;

  const rows = await db.select().from(toolSettingsTable).limit(1);

  if (rows.length === 0) {
    const [inserted] = await db.insert(toolSettingsTable).values({}).returning();
    cached = inserted;
  } else {
    cached = rows[0];
  }

  cacheTime = now;
  return cached!;
}

export function invalidateSettingsCache(): void {
  cached = null;
  cacheTime = 0;
}
