import { chromium } from "@playwright/test";

/**
 * Chạy script này 1 lần đầu.
 * Mở browser, bạn login tay vào kb.urbox.dev bằng Google.
 * Login xong → press Enter ở terminal → session save về ./data/sessions/kb_session/
 */

const SESSION_DIR = "./data/sessions/kb_session";
const KB_URL = "https://kb.urbox.dev";

async function main() {
  console.log("🚀 Launching persistent browser...");

  // launchPersistentContext = launch + newContext gộp lại,
  // tự save cookies/session vào userDataDir
  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: false,
  });

  const page = context.pages()[0] || (await context.newPage());

  await page.goto(KB_URL);

  console.log("\n=========================================");
  console.log("👆 Browser đã mở.");
  console.log("   → Login vào kb.urbox.dev bằng Google của bạn");
  console.log("   → Sau khi login xong, thấy KB page rồi thì press ENTER ở đây");
  console.log("=========================================\n");

  // Wait user press Enter
  await new Promise<void>((resolve) => {
    process.stdin.resume();
    process.stdin.setEncoding("utf8");
    process.stdin.once("data", () => {
      resolve();
    });
  });

  console.log("💾 Saving session...");
  await context.close();

  console.log("✅ Session saved to ./data/sessions/kb_session/");
  console.log("   → Bây giờ chạy: npx playwright test scrape_kb.ts --headed");
}

main().catch(console.error);
