import { test, Page } from "@playwright/test";
import * as process from "process";
import * as fs from "fs";
import * as path from "path";

/* ============================
   CONFIG
============================ */

const URL = "https://chat.urbox.dev/";

// Login selectors
const EMAIL_INPUT = "#email";
const PASSWORD_INPUT = "#password";
const LOGIN_BUTTON = 'button:has-text("Sign in")';

// Chat input selector
const EDITOR_BOX = "div.ProseMirror";
const BOT_BLOCK_SELECTOR = [
  "div.chat-assistant",
  "div.chat-message.assistant",
  "div[data-message-role='assistant']",
  "div[data-role='assistant']",
  "div[data-message-author-role='assistant']",
  "div[data-testid='assistant-message']",
  "article[data-message-author-role='assistant']",
].join(", ");
const USER_BLOCK_SELECTOR = [
  "div.chat-user",
  "div.chat-message.user",
  "div[data-message-role='user']",
  "div[data-role='user']",
  "div[data-message-author-role='user']",
  "div[data-testid='user-message']",
  "article[data-message-author-role='user']",
].join(", ");

// Account test
const EMAIL = "3khoa@yopmail.com";
const PASSWORD = "khoa3";

// Input + Output JSON
const INPUT_FILE = process.env.QA_INPUT || "outputs/PCI_DSS_qa.json";
const OUTPUT_FILE = process.env.QA_OUTPUT || "outputs/PCI_DSS_qa_output.json";

// Restart browser after N questions
const MAX_PER_SESSION = 6;

/* ============================
   HELPER FUNCTIONS
============================ */

/**
 * Login vào chatbot
 */
async function login(page: Page) {
  console.log("🔑 Opening login page...");

  await page.goto(URL);

  await page.waitForSelector(EMAIL_INPUT, { timeout: 60000 });

  await page.fill(EMAIL_INPUT, EMAIL);
  await page.fill(PASSWORD_INPUT, PASSWORD);

  await page.click(LOGIN_BUTTON);

  console.log("✅ Logged in, waiting for chat editor...");

  await page.waitForSelector(EDITOR_BOX, { timeout: 60000 });

  console.log("✅ Chat editor ready!");
}
async function selectENGTestModel(page: Page) {
  await page.waitForTimeout(4000);

  // Kiểm tra model hiện tại
  const currentModel = page.locator('button[aria-label^="Selected model:"]');
  const count = await currentModel.count();

  if (count > 0) {
    const label = await currentModel.getAttribute("aria-label");
    console.log(`✅ Current model: "${label}"`);

    // Nếu đã đúng model rồi thì skip
    if (label?.includes("ENG Test")) {
      console.log("✅ Correct model already selected, skipping...");
      return;
    }
  }

  // Nếu sai model → click để mở dropdown và chọn lại
  console.log("🖱 Opening model dropdown to switch...");
  await currentModel.click({ force: true });
  await page.waitForTimeout(2000);

  const engTestModelOption = page
    .locator('button[aria-roledescription="model-item"]')
    .filter({ hasText: /ENG Test/i });

  const optionCount = await engTestModelOption.count();
  if (optionCount > 0) {
    await engTestModelOption.click({ force: true });
    console.log("✅ ENG Test selected!");
  } else {
    console.log("✅ Model already correct, no switch needed.");
  }
}

/**
 * Scroll xuống cuối trang chat
 */
async function scrollToBottom(page: Page) {
  await page.evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight);
  });
}

async function getLatestBotBlock(page: Page): Promise<ReturnType<Page["locator"]> | null> {
  const botBlocks = page.locator(BOT_BLOCK_SELECTOR);
  const count = await botBlocks.count();

  if (count === 0) return null;

  for (let i = count - 1; i >= 0; i--) {
    const block = botBlocks.nth(i);
    let text = "";
    try {
      text = (await block.innerText()).trim();
    } catch {
      text = "";
    }

    if (!text) continue;

    const cleaned = text
      .replace(/Thought for .*?seconds?\s*/gi, "")
      .replace(/Thought for less than a second\s*/gi, "")
      .replace(/\(Nguồn:.*?\)\s*/gs, "")
      .replace(/\d+\s*Sources?\s*/gi, "")
      .replace(/Nguồn\s*:?/gi, "")
      .replace(/Sources?\s*:?/gi, "")
      .trim();

    if (cleaned.length > 0) return block;
  }

  return null;
}

async function getUserBlockCount(page: Page): Promise<number> {
  const userBlocks = page.locator(USER_BLOCK_SELECTOR);
  return await userBlocks.count();
}

async function getBotBlockAfterUserIndex(
  page: Page,
  userIndex: number,
  prevBotText?: string
): Promise<ReturnType<Page["locator"]> | null> {
  const idx = await page.evaluate(
    ({ userSel, botSel, uIndex, prevText }) => {
      const bots = Array.from(document.querySelectorAll(botSel));
      const users = Array.from(document.querySelectorAll(userSel));
      if (!bots.length || users.length <= uIndex) return null;

      const userEl = users[uIndex];
      const followingIdxs: number[] = [];
      for (let i = 0; i < bots.length; i++) {
        const bot = bots[i];
        if (
          userEl.compareDocumentPosition(bot) &
          Node.DOCUMENT_POSITION_FOLLOWING
        ) {
          followingIdxs.push(i);
        }
      }

      if (!followingIdxs.length) return null;

      // Prefer the newest bot after user that is not equal to previous text
      if (prevText) {
        for (let k = followingIdxs.length - 1; k >= 0; k--) {
          const i = followingIdxs[k];
          const txt = (bots[i] as HTMLElement).innerText.trim();
          if (txt && txt !== prevText) return i;
        }
      }

      // Fallback: last bot following the user
      return followingIdxs[followingIdxs.length - 1];
    },
    {
      userSel: USER_BLOCK_SELECTOR,
      botSel: BOT_BLOCK_SELECTOR,
      uIndex: userIndex,
      prevText: prevBotText?.trim() || "",
    }
  );

  if (idx === null) return null;
  const botBlocks = page.locator(BOT_BLOCK_SELECTOR);
  return botBlocks.nth(idx);
}

async function dumpDebug(page: Page, reason: string) {
  try {
    const ts = Date.now();
    const dir = path.join("test-results", "qa-debug");
    fs.mkdirSync(dir, { recursive: true });

    const htmlPath = path.join(dir, `debug_${ts}.html`);
    const shotPath = path.join(dir, `debug_${ts}.png`);
    const metaPath = path.join(dir, `debug_${ts}.txt`);

    const html = await page.content();
    fs.writeFileSync(htmlPath, html, "utf-8");

    await page.screenshot({ path: shotPath, fullPage: true });

    const meta = [
      `reason=${reason}`,
      `url=${page.url()}`,
      `timestamp=${new Date(ts).toISOString()}`,
    ].join("\n");
    fs.writeFileSync(metaPath, meta, "utf-8");
    console.log(`🧪 Debug saved: ${dir}/debug_${ts}.*`);
  } catch (err) {
    console.log("⚠️ Failed to dump debug:", err);
  }
}

/**
 * Wait bot trả lời xong
 */
async function waitBotDone(page: Page) {
  console.log("⏳ Waiting bot response...");

  const stopBtn = page.locator('button:has-text("Stop")');

  if (await stopBtn.isVisible().catch(() => false)) {
    await stopBtn.waitFor({ state: "hidden", timeout: 450000 });
  }

  await page.waitForTimeout(4500);

  console.log("✅ Bot finished!");
}

async function getBotBlockCount(page: Page): Promise<number> {
  const botBlocks = page.locator(BOT_BLOCK_SELECTOR);
  return await botBlocks.count();
}

async function getLatestBotText(page: Page): Promise<string> {
  const lastBot = await getLatestBotBlock(page);
  if (!lastBot) return "";
  try {
    return (await lastBot.innerText()).trim();
  } catch {
    return "";
  }
}

async function waitForNewBotMessageOrTextChange(
  page: Page,
  prevCount: number,
  prevText: string
) {
  console.log("⏳ Waiting for new bot message or text change...");

  try {
    await page.waitForFunction(
      (selector, count, lastText) => {
        const bots = document.querySelectorAll(selector);
        if (bots.length > count) return true;

        if (!bots.length) return false;

        let lastBot: HTMLElement | null = null;
        for (let i = bots.length - 1; i >= 0; i--) {
          const el = bots[i] as HTMLElement;
          const txt = el.innerText.trim();
          if (txt.length > 0) {
            lastBot = el;
            break;
          }
        }
        if (!lastBot) return false;

        const text = lastBot.innerText.trim();
        if (!text) return false;

        return text !== lastText;
      },
      BOT_BLOCK_SELECTOR,
      prevCount,
      prevText,
      { timeout: 360000 }
    );
  } catch {
    console.log("⚠️ Wait for new bot message timed out, continue...");
  }

  console.log("✅ New bot message or text change detected!");
}

async function waitLatestBotStable(page: Page) {
  console.log("⏳ Waiting latest bot text to stabilize...");

  await page.waitForFunction(
    (selector) => {
      const bots = document.querySelectorAll(selector);
      if (!bots.length) return false;

      let lastBot: HTMLElement | null = null;
      for (let i = bots.length - 1; i >= 0; i--) {
        const el = bots[i] as HTMLElement;
        const txt = el.innerText.trim();
        if (txt.length > 0) {
          lastBot = el;
          break;
        }
      }
      if (!lastBot) return false;

      const text = lastBot.innerText.trim();
      if (text.length === 0) return false;

      const w = window as any;
      if (!w.__lastBotText) {
        w.__lastBotText = text;
        w.__lastBotTime = Date.now();
        return false;
      }

      if (w.__lastBotText !== text) {
        w.__lastBotText = text;
        w.__lastBotTime = Date.now();
        return false;
      }

      return Date.now() - w.__lastBotTime > 2000;
    },
    BOT_BLOCK_SELECTOR,
    { timeout: 360000 }
  );

  console.log("✅ Latest bot text stable!");
}

async function waitForBotStart(page: Page, prevCount: number) {
  console.log("⏳ Waiting bot to start responding...");
  try {
    await page.waitForFunction(
      (selector, count) => {
        const bots = document.querySelectorAll(selector);
        if (bots.length > count) return true;

        for (let i = bots.length - 1; i >= 0; i--) {
          const el = bots[i] as HTMLElement;
          const txt = el.innerText.trim();
          if (txt.length > 0) return true;
        }
        return false;
      },
      BOT_BLOCK_SELECTOR,
      prevCount,
      { timeout: 360000 }
    );
  } catch {
    console.log("⚠️ Wait bot start timed out, continue...");
  }
}

/**
 * Send câu hỏi bằng Enter
 */
async function sendQuestion(page: Page, question: string, prevUserCount?: number) {
  console.log("✍️ Sending:", question);

  await page.waitForSelector(EDITOR_BOX, { timeout: 60000 });

  await page.click(EDITOR_BOX);

  // Clear input
  await page.keyboard.press("Control+A");
  await page.keyboard.press("Backspace");

  // Type chậm (giữ xuống dòng bằng Shift+Enter, chỉ Enter ở cuối)
  const lines = question.split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line) {
      await page.keyboard.type(line, { delay: 30 });
    }
    if (i < lines.length - 1) {
      await page.keyboard.press("Shift+Enter");
    }
  }

  // Ưu tiên click nút Send (tránh Enter tạo bullet trống)
  let sent = false;
  const tryClickSend = async () => {
    const sendBtn = page
      .locator(
        'button[aria-label*="Send" i], button[aria-label*="Send message" i], button:has-text("Send"), button:has-text("Gửi"), button[aria-label*="Gửi" i], button[type="submit"]'
      )
      .first();
    if (await sendBtn.count()) {
      const disabled =
        (await sendBtn.getAttribute("disabled")) !== null ||
        (await sendBtn.getAttribute("aria-disabled")) === "true";
      if (!disabled) {
        await sendBtn.click({ force: true });
        return true;
      }
    }
    return false;
  };

  if (typeof prevUserCount === "number") {
    sent = await tryClickSend();
    if (sent) {
      await page.waitForTimeout(800);
      const afterClick = await getUserBlockCount(page);
      if (afterClick <= prevUserCount) {
        sent = false;
      }
    }
  }

  // Fallback: Enter gửi
  if (!sent) {
    await page.keyboard.press("Enter");
  }

  // Nếu chưa gửi được thì thử Ctrl+Enter hoặc click nút Send
  if (typeof prevUserCount === "number") {
    await page.waitForTimeout(800);
    const afterEnter = await getUserBlockCount(page);
    if (afterEnter <= prevUserCount) {
      console.log("⚠️ Enter chưa gửi, thử Ctrl+Enter...");
      await page.keyboard.press("Control+Enter");
      await page.waitForTimeout(800);
      const afterCtrlEnter = await getUserBlockCount(page);
      if (afterCtrlEnter <= prevUserCount) {
        console.log("⚠️ Ctrl+Enter chưa gửi, thử click nút Send...");
        const clicked = await tryClickSend();
        if (!clicked) console.log("⚠️ Không tìm thấy nút Send hoặc nút bị disabled.");
      }
    }
  }

  console.log("📨 Sent!");
}

/* ============================
   EXTRACT ANSWER
============================ */

async function getLatestBotAnswer(
  page: Page,
  userIndex?: number,
  prevBotText?: string
): Promise<string> {
  console.log("📝 Extracting answer...");

  const lastBot =
    userIndex !== undefined
      ? await getBotBlockAfterUserIndex(page, userIndex, prevBotText)
      : await getLatestBotBlock(page);
  if (!lastBot) {
    await dumpDebug(page, "no_bot_messages_found");
    return "❌ No bot messages found";
  }

  // wait answer render (robust across markup changes)
  const contentLocator = lastBot.locator(
    "p[dir='auto'], div.markdown, div.markdown *, pre, li, div.prose, div.message-content, article, span"
  );

  try {
    await contentLocator.first().waitFor({ timeout: 20000 });
  } catch {
    try {
      const handle = await lastBot.elementHandle();
      if (!handle) {
        await dumpDebug(page, "no_bot_content_found");
        return "❌ No bot content found";
      }
      await page.waitForFunction(
        (el) => {
          const node = el as HTMLElement | null;
          return !!node && node.innerText.trim().length > 0;
        },
        handle,
        { timeout: 20000 }
      );
    } catch {
      await dumpDebug(page, "no_bot_content_found");
      return "❌ No bot content found";
    }
  }

  // ✅ lấy full text như code cũ (không bao giờ Empty)
  let answerText = (await lastBot.innerText()).trim();

  // ============================
  // ✅ CLEAN đúng 3 phần thừa
  // ============================

  // 1. Remove Thought line (all variations)
  answerText = answerText.replace(/Thought for .*?seconds?\s*/gi, "");
  answerText = answerText.replace(/Thought for less than a second\s*/gi, "");
  // 2. Remove nguồn ở cuối
  answerText = answerText.replace(/\(Nguồn:.*?\)\s*/gs, "");

  // 3. Remove "2 Sources" / "3 Sources"
  answerText = answerText.replace(/\d+\s*Sources?\s*/g, "");

  // ✅ trim lại
  answerText = answerText.trim();

  if (answerText.length === 0) {
    await dumpDebug(page, "empty_answer_after_clean");
    return "❌ Empty answer";
  }

  return answerText;
}
  
/* ============================
   EXTRACT SOURCES
============================ */

async function getLatestBotSources(
  page: Page,
  userIndex?: number,
  prevBotText?: string
): Promise<string[]> {
  console.log("📌 Extracting sources...");

  const lastBot =
    userIndex !== undefined
      ? await getBotBlockAfterUserIndex(page, userIndex, prevBotText)
      : await getLatestBotBlock(page);
  if (!lastBot) return ["❌ No bot blocks found"];

  // Try to reveal message actions if UI uses hover
  try {
    await lastBot.hover({ force: true });
    await page.waitForTimeout(500);
  } catch {}

  // STEP 1: Click button "1 Source"
  let openSourceBtn = lastBot
    .locator("button")
    .filter({ hasText: /Source|Sources|Nguồn/i })
    .first();

  if ((await openSourceBtn.count()) === 0) {
    openSourceBtn = lastBot
      .locator("button[aria-label*='Source' i], button[aria-label*='Sources' i], button[aria-label*='Nguồn' i]")
      .first();
  }

  if ((await openSourceBtn.count()) === 0) {
    openSourceBtn = page
      .locator("button")
      .filter({ hasText: /Source|Sources|Nguồn/i })
      .first();
  }

  if ((await openSourceBtn.count()) === 0) {
    await dumpDebug(page, "no_source_button_found");
    return ["❌ No Source button found"];
  }

  console.log("🖱 Clicking Source expand...");
  await openSourceBtn.click();

  // STEP 2: Wait sources appear
  let sourceButtons = lastBot.locator("button[id^='source-'], a[id^='source-']");

  try {
    await sourceButtons.first().waitFor({ timeout: 8000 });
  } catch {
    sourceButtons = page.locator("button[id^='source-'], a[id^='source-']");
    try {
      await sourceButtons.first().waitFor({ timeout: 8000 });
    } catch {
      return ["❌ Source list did not expand"];
    }
  }

  // STEP 3: Extract filenames FULL
  const total = await sourceButtons.count();

  let sources: string[] = [];

  for (let i = 0; i < total; i++) {
    const rawText = (await sourceButtons.nth(i).innerText()).trim();

    const lines = rawText.split("\n").map((l) => l.trim());

    if (lines.length >= 2) {
      sources.push(lines[1]); // filename full
    } else if (lines.length === 1 && lines[0]) {
      sources.push(lines[0]);
    }
  }

  sources = [...new Set(sources)];

  return sources.length > 0
    ? sources
    : ["❌ No source filename extracted"];
}

function isBadAnswer(answer: string): boolean {
  return (
    !answer ||
    answer.startsWith("❌") ||
    answer.trim().length === 0 ||
    answer.trim().toLowerCase() === "querying"
  );
}

function isBadSources(sources: string[]): boolean {
  if (!sources || sources.length === 0) return true;
  return sources.some((s) => s.startsWith("❌"));
}

/* ============================
   OUTPUT RESUME SUPPORT
============================ */

/**
 * Load output cũ nếu đã tồn tại → resume tiếp
 */
function loadExistingOutput(): any[] {
  if (!fs.existsSync(OUTPUT_FILE)) return [];

  try {
    const raw = fs.readFileSync(OUTPUT_FILE, "utf-8").trim();
    if (!raw) return [];

    return JSON.parse(raw);
  } catch {
    console.log("⚠️ Output file corrupted, reset...");
    return [];
  }
}

/**
 * Save output cộng dồn
 */
function saveOutput(data: any[]) {
  const outputDir = path.dirname(OUTPUT_FILE);
  if (outputDir && outputDir !== ".") {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(data, null, 2), "utf-8");
}

/* ============================
   MAIN TEST
============================ */

test(
  `PCI DSS QA JSON Auto Answer + Source Extract (Restart every ${MAX_PER_SESSION})`,
  async ({ browser }) => {
  test.setTimeout(3600000);

  /* ============================
     STEP 1: Load PCI_DSS_qa.json
  ============================ */

  console.log("📂 Loading PCI_DSS_qa.json...");
  const kbData = JSON.parse(fs.readFileSync(INPUT_FILE, "utf-8"));

  console.log("✅ Total questions:", kbData.length);

  /* ============================
     STEP 2: Load existing output.json
  ============================ */

  let output = loadExistingOutput();
  let startIndex = output.length;

  console.log("📌 Resume from question:", startIndex + 1);

  /* ============================
     STEP 3: Loop until done
  ============================ */

  while (startIndex < kbData.length) {
    console.log("\n===============================");
    console.log("🚀 Starting NEW Chat Session...");
    console.log("===============================\n");

    // Open new browser context
    const context = await browser.newContext();
    const page = await context.newPage();

    // Login again
    await login(page);
    // ✅ Chọn model 
    await selectENGTestModel(page);

    // Ask up to MAX_PER_SESSION questions
    for (
      let i = 0;
      i < MAX_PER_SESSION && startIndex < kbData.length;
      i++
    ) {
      const question = kbData[startIndex].question;

      console.log(`\n==============================`);
      console.log(`❓ Question ${startIndex + 1}: ${question}`);
      console.log(`==============================\n`);

      await scrollToBottom(page);

      const prevBotCount = await getBotBlockCount(page);
      const prevBotText = await getLatestBotText(page);
      const prevUserCount = await getUserBlockCount(page);

      // Send question
      await sendQuestion(page, question, prevUserCount);

      // Wait bot start responding
      await waitForBotStart(page, prevBotCount);

      // Wait bot response done
      await waitBotDone(page);

      await waitForNewBotMessageOrTextChange(page, prevBotCount, prevBotText);

      await page.evaluate(() => {
        const w = window as any;
        delete w.__lastBotText;
        delete w.__lastBotTime;
      });

      await waitLatestBotStable(page);

// // ✅ CHỜ TEXT BOT RENDER ỔN ĐỊNH (FIX EMPTY ANSWER)
// await page.waitForFunction(() => {
//     const bots = document.querySelectorAll("div.chat-assistant");
//     if (!bots.length) return false;
  
//     const lastBot = bots[bots.length - 1] as HTMLElement;
//     return lastBot.innerText.trim().length > 20;
//   }, { timeout: 30000 });
// ✅ CHỜ TEXT BOT ỔN ĐỊNH (KHÔNG THAY ĐỔI TRONG 4 GIÂY)
await page.waitForFunction(() => {
  const bots = document.querySelectorAll(
    "div.chat-assistant, div.chat-message.assistant, div[data-message-role='assistant'], div[data-role='assistant'], div[data-message-author-role='assistant'], div[data-testid='assistant-message'], article[data-message-author-role='assistant']"
  );
  if (!bots.length) return false;

  let lastBot: HTMLElement | null = null;
  for (let i = bots.length - 1; i >= 0; i--) {
    const el = bots[i] as HTMLElement;
    const txt = el.innerText.trim();
    if (txt.length > 0) {
      lastBot = el;
      break;
    }
  }
  if (!lastBot) return false;

  const text = lastBot.innerText.trim();

  if (text.length < 20) return false;

  // lưu text vào window để so sánh
  if (!(window as any).__lastBotText) {
    (window as any).__lastBotText = text;
    (window as any).__lastBotTime = Date.now();
    return false;
  }

  if ((window as any).__lastBotText !== text) {
    (window as any).__lastBotText = text;
    (window as any).__lastBotTime = Date.now();
    return false;
  }

  // nếu text không đổi trong 4 giây → coi như xong
  return Date.now() - (window as any).__lastBotTime > 6000;

}, { timeout: 360000 });
  

      // Always scroll to bottom before extract to avoid picking old blocks
      await scrollToBottom(page);
      await page.waitForTimeout(1000);

      // Extract Answer + Sources with retry
      let answer = "";
      let sources: string[] = [];
      const maxAttempts = 5;

      const currentUserCount = await getUserBlockCount(page);
      const userIndex =
        currentUserCount > 0 ? currentUserCount - 1 : prevUserCount;

      for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        console.log(`🔁 Extract attempt ${attempt}/${maxAttempts}`);
        answer = await getLatestBotAnswer(page, userIndex, prevBotText);
        sources = await getLatestBotSources(page, userIndex, prevBotText);

        if (!isBadAnswer(answer) && !isBadSources(sources)) {
          break;
        }

        console.log("⚠️  Missing answer or sources, retrying after wait...");
        await page.waitForTimeout(4500);
      }

      if (isBadAnswer(answer) || isBadSources(sources)) {
        await dumpDebug(page, "missing_answer_or_sources_after_retries");
        throw new Error("Missing answer or sources after retries");
      }

      console.log("✅ Answer:", answer);
      console.log("✅ Sources:", sources);

      // ✅ Giữ nguyên structure PCI_DSS_qa.json nhưng không mutate file gốc
const originalObj = kbData[startIndex];

// clone object và chỉ thêm đúng field answer + source
const newObj = {
  ...originalObj,
  answer: answer,
  source: sources,
};

// push object đầy đủ vào output
output.push(newObj);



      // Save output after each question
      saveOutput(output);

      console.log("💾 Saved:", startIndex + 1);

      startIndex++;

      await page.waitForTimeout(3000);
    }

    console.log(
      `♻️ Closing browser session after ${MAX_PER_SESSION} questions...`
    );
    await context.close();
  }

  console.log("\n✅ DONE! All questions completed.");
  console.log("📌 Output saved in:", OUTPUT_FILE);
});
