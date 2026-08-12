import { defineConfig } from "@playwright/test";

export default defineConfig({
  timeout: 30 * 60 * 1000,
  use: {
    headless: false,
    channel: "chrome", // Dùng Chrome của máy thay vì cài Chromium
  },
  testDir: ".",
  reporter: [["list"]],
});
