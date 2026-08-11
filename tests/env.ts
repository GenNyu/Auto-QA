import * as fs from "fs";
import * as path from "path";

/**
 * Đọc file .env ở thư mục gốc dự án vào process.env.
 * Không ghi đè biến môi trường đã có sẵn.
 */
export function loadEnvFile(envPath = path.resolve(__dirname, "..", ".env")): void {
  if (!fs.existsSync(envPath)) return;

  for (const rawLine of fs.readFileSync(envPath, "utf-8").split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;

    const idx = line.indexOf("=");
    const key = line.slice(0, idx).trim();
    const value = line.slice(idx + 1).trim().replace(/^["']|["']$/g, "");
    if (key && !(key in process.env)) process.env[key] = value;
  }
}

/** Escape chuỗi để nhúng an toàn vào RegExp. */
export function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Lấy biến môi trường tuỳ chọn, có giá trị mặc định. */
export function optionalEnv(key: string, fallback: string): string {
  loadEnvFile();
  return process.env[key] || fallback;
}

/**
 * Lấy biến môi trường bắt buộc, báo lỗi rõ ràng nếu thiếu.
 */
export function requireEnv(key: string): string {
  loadEnvFile();
  const value = process.env[key];
  if (!value) {
    throw new Error(
      `\n❌ Thiếu cấu hình: ${key}\n\n` +
        `   Hãy tạo file .env ở thư mục gốc và điền giá trị:\n` +
        `       cp .env.example .env\n\n` +
        `   Sau đó mở .env và điền ${key}=...\n`
    );
  }
  return value;
}
