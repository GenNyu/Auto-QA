import { defineConfig } from "@playwright/test";

export default defineConfig({
  timeout: 30 * 60 * 1000,
  use: {
    headless: false,
  },
  testDir: ".",
  reporter: [["list"]],
});
