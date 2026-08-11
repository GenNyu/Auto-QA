const { chromium } = require("@playwright/test");

const args = parseArgs(process.argv.slice(2));

const KB_URL = args.url || "https://kb.urbox.vn";
const SESSION_DIR = args.session || "./data/sessions/kb_session_vn";
const HEADLESS = args.headless === "true";

function parseArgs(argv) {
  const parsed = {};
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (!arg.startsWith("--")) continue;

    const key = arg.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      parsed[key] = "true";
    } else {
      parsed[key] = next;
      i++;
    }
  }
  return parsed;
}

async function main() {
  console.log(`Opening persistent browser for ${KB_URL}`);
  console.log(`Session directory: ${SESSION_DIR}`);

  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: HEADLESS,
  });

  const page = context.pages()[0] || (await context.newPage());
  await page.goto(KB_URL);

  console.log("");
  console.log("Login in the opened browser.");
  console.log("When the KB page is visible, press ENTER here to save the session.");
  console.log("");

  await new Promise((resolve) => {
    process.stdin.resume();
    process.stdin.setEncoding("utf8");
    process.stdin.once("data", resolve);
  });

  await context.close();

  console.log(`Session saved to ${SESSION_DIR}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
