import { test, Page } from "@playwright/test";
import * as process from "process";
import * as fs from "fs";
import * as path from "path";
import { escapeRegExp, optionalEnv, requireEnv } from "./env";

/* ============================
   CONFIG
   Mọi giá trị dưới đây do qa.py truyền vào qua biến môi trường.
============================ */

const URL = optionalEnv("CHAT_URL", "https://chat.urbox.dev/");
const CHAT_MODEL = optionalEnv("CHAT_MODEL", "ENGR Test1");

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
const EMAIL = requireEnv("CHAT_EMAIL");
const PASSWORD = requireEnv("CHAT_PASSWORD");

// Input + Output JSON
const INPUT_FILE = process.env.QA_INPUT || "qa_input.json";
const OUTPUT_FILE = process.env.QA_OUTPUT || "qa_output.json";

// Restart browser after N questions
const MAX_PER_SESSION = Number(optionalEnv("QA_MAX_PER_SESSION", "10"));

// Độ dài tối thiểu (sau khi clean) để coi là một câu trả lời thật, không phải
// mẩu text còn sót lại của trạng thái đang tải.
const MIN_ANSWER_LENGTH = 20;

/* ============================
   HELPER FUNCTIONS
============================ */

function cleanBotText(text: string): string {
  return text
    .replace(/Thought for .*?seconds?\s*/gi, "")
    .replace(/Thought for less than a second\s*/gi, "")
    // Bỏ TRỌN dòng chú thích nguồn ở cuối câu trả lời. Trước đây chỉ xoá mỗi chữ
    // "Nguồn", để lại "tham khảo: Link" làm dòng cuối — dòng này ngắn và không
    // kết thúc bằng dấu câu nên looksIncompleteBotText luôn báo "chưa xong".
    .replace(/^[ \t]*Nguồn tham khảo\s*:.*$/gim, "")
    // Token trích dẫn tên file, vd: 20260128_BD_OPS...nh_toan.md
    .replace(/\b\d{8}_\S*\.md\b/g, "")
    // "Link", "Link 1", "Link 2"... mỗi cái một dòng trong danh sách nguồn
    // Dạng "Link 1 / Link 2 / ..." cũng có thể xuất hiện trên một dòng
    .replace(/^[ \t]*(Link[ \t]*\d*[ \t]*(\/[ \t]*Link[ \t]*\d*[ \t]*)*)$/gim, "")
    .replace(/\(Nguồn:.*?\)\s*/gs, "")
    .replace(/\d+\s*Sources?\s*/gi, "")
    .replace(/Nguồn\s*:?/gi, "")
    .replace(/Sources?\s*:?/gi, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function isTrivialBotText(text: string): boolean {
  const cleaned = cleanBotText(text).trim().toLowerCase();
  if (!cleaned) return true;
  if (cleaned === "querying" || cleaned.startsWith("querying")) return true;
  if (cleaned === "searching" || cleaned.startsWith("searching")) return true;
  return false;
}

function looksIncompleteBotText(text: string): boolean {
  const cleaned = cleanBotText(text);
  if (!cleaned) return true;

  const boldCount = (cleaned.match(/\*\*/g) || []).length;
  if (boldCount % 2 === 1) return true;

  const fenceCount = (cleaned.match(/```/g) || []).length;
  if (fenceCount % 2 === 1) return true;

  const lastLine = cleaned.split("\n").pop() || "";
  const trimmedLast = lastLine.trim();
  if (trimmedLast.length > 0) {
    const endsWithPunct = /[.!?…)"'\]]$/.test(trimmedLast);
    if (!endsWithPunct && trimmedLast.length < 20) return true;
  }

  return false;
}

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
/**
 * Đọc tên model đang được chọn, từ aria-label "Selected model: <tên>".
 */
async function getSelectedModel(page: Page): Promise<string | null> {
  const button = page.locator('button[aria-label^="Selected model:"]');
  if ((await button.count()) === 0) return null;

  const label = await button.getAttribute("aria-label");
  return label ? label.replace(/^Selected model:\s*/i, "").trim() : null;
}

/**
 * Chọn đúng model CHAT_MODEL trên giao diện chat.
 *
 * Toàn bộ kết quả đánh giá phụ thuộc vào việc hỏi ĐÚNG model, nên hàm này ném lỗi
 * khi không đổi được. Bản trước in "✅ Model already correct" ngay trong nhánh
 * không tìm thấy model, nên khi dropdown không mở hoặc tên model sai chính tả thì
 * cả lượt chạy vẫn tiếp tục — với model cũ, mà log lại báo thành công.
 */
async function selectENGTestModel(page: Page) {
  await page.waitForTimeout(4000);

  const current = await getSelectedModel(page);
  console.log(`ℹ️  Model đang chọn: "${current ?? "(không đọc được)"}"`);

  if (current === CHAT_MODEL) {
    console.log(`✅ Đã đúng model "${CHAT_MODEL}", bỏ qua bước đổi.`);
    return;
  }

  const button = page.locator('button[aria-label^="Selected model:"]');
  if ((await button.count()) === 0) {
    throw new Error(
      "Không tìm thấy nút chọn model trên giao diện. " +
        "Giao diện chat có thể đã đổi, cần cập nhật selector trong tests/KB.spec.ts."
    );
  }

  console.log(`🖱  Mở dropdown để đổi sang "${CHAT_MODEL}"...`);
  await button.click({ force: true });
  await page.waitForTimeout(1500);

  // Danh sách model cuộn được và chỉ render phần đang nhìn thấy, nên phải gõ vào
  // ô tìm kiếm thay vì mong model nằm sẵn trong DOM.
  const search = page.locator('input[placeholder*="Search a model" i]');
  if ((await search.count()) > 0) {
    await search.first().fill(CHAT_MODEL);
  }

  // Open WebUI dựng danh sách model bằng role listbox/option:
  //     <div role="listbox" aria-label="Available models">
  //       <div role="option" aria-label="Select BD Solution model"> …
  // Selector cũ `button[aria-roledescription="model-item"]` không khớp gì cả — đó là
  // lý do bước đổi model chưa bao giờ chạy, chỉ là trước đây nó im lặng bỏ qua.
  const items = page.locator(
    '[role="option"], button[aria-roledescription="model-item"]'
  );
  await items.first().waitFor({ state: "visible", timeout: 10000 }).catch(() => {});
  const total = await items.count();

  const escaped = escapeRegExp(CHAT_MODEL);
  // Thử từ chặt tới lỏng, để "ENG Test" không chọn nhầm "ENGR Test1".
  const strategies = [
    () => page.getByRole("option", {
      name: new RegExp(`^Select\\s+${escaped}\\s+model$`, "i"),
    }),
    () => items.filter({ hasText: new RegExp(`^\\s*${escaped}\\s*$`, "i") }),
    () => items.filter({ hasText: new RegExp(escaped, "i") }),
  ];

  let target = items.filter({ hasText: new RegExp(escaped, "i") });
  for (const strategy of strategies) {
    const candidate = strategy();
    if ((await candidate.count()) > 0) {
      target = candidate;
      break;
    }
  }

  if ((await target.count()) === 0) {
    const available: string[] = [];
    for (let i = 0; i < Math.min(total, 20); i++) {
      const item = items.nth(i);
      const label = (await item.getAttribute("aria-label")) || "";
      const name = label.replace(/^Select\s+/i, "").replace(/\s+model$/i, "").trim();
      available.push(name || (await item.innerText()).trim().split("\n")[0]);
    }
    await dumpDebug(page, "model_not_found");
    throw new Error(
      `Không tìm thấy model "${CHAT_MODEL}" trong danh sách.\n` +
        `   Model đang có: ${available.join(", ") || "(danh sách rỗng)"}\n` +
        `   Sửa CHAT_MODEL trong .env cho khớp đúng chữ hiển thị trên giao diện.`
    );
  }

  await target.first().click({ force: true });
  await page.waitForTimeout(2000);

  // Xác nhận đã đổi thật, không tin vào cú click.
  const after = await getSelectedModel(page);
  if (after !== CHAT_MODEL) {
    await dumpDebug(page, "model_switch_failed");
    throw new Error(
      `Đổi model thất bại: vẫn đang là "${after ?? "(không đọc được)"}", ` +
        `cần "${CHAT_MODEL}".`
    );
  }

  console.log(`✅ Đã đổi sang model "${CHAT_MODEL}".`);
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

    if (!isTrivialBotText(text)) return block;
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

      const clean = (txt: string) =>
        txt
          .replace(/Thought for .*?seconds?\s*/gi, "")
          .replace(/Thought for less than a second\s*/gi, "")
          .replace(/\(Nguồn:.*?\)\s*/gs, "")
          .replace(/\d+\s*Sources?\s*/gi, "")
          .replace(/Nguồn\s*:?/gi, "")
          .replace(/Sources?\s*:?/gi, "")
          .trim()
          .toLowerCase();

      // Prefer the newest bot after user that is not trivial or same as previous text
      for (let k = followingIdxs.length - 1; k >= 0; k--) {
        const i = followingIdxs[k];
        const raw = (bots[i] as HTMLElement).innerText.trim();
        const cleaned = clean(raw);
        if (!cleaned) continue;
        if (cleaned === "querying" || cleaned.startsWith("querying")) continue;
        if (cleaned === "searching" || cleaned.startsWith("searching")) continue;
        if (prevText && cleaned === prevText.toLowerCase()) continue;
        return i;
      }

      // Fallback: last bot following the user
      return followingIdxs[followingIdxs.length - 1];
    },
    {
      userSel: USER_BLOCK_SELECTOR,
      botSel: BOT_BLOCK_SELECTOR,
      uIndex: userIndex,
      prevText: cleanBotText(prevBotText?.trim() || ""),
    }
  );

  if (idx === null) return null;
  const botBlocks = page.locator(BOT_BLOCK_SELECTOR);
  return botBlocks.nth(idx);
}

async function dumpDebug(page: Page, reason: string) {
  try {
    const ts = Date.now();
    const dir = path.join("test-results", "kb-debug");
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

  await page.waitForTimeout(20000);

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

  const start = Date.now();
  const timeoutMs = 450000;
  const stableMs = 15000;
  // Chốt chặn: văn bản đứng yên lâu tới mức này thì nhận, kể cả khi
  // looksIncompleteBotText vẫn báo "chưa xong". Không có mốc này, một dòng cuối
  // bất thường sẽ giữ vòng lặp chạy hết 450s cho MỖI câu hỏi.
  const forceAcceptMs = 45000;
  let lastCleaned = "";
  let lastChange = Date.now();

  while (Date.now() - start < timeoutMs) {
    const block = await getLatestBotBlock(page);
    if (!block) {
      await page.waitForTimeout(1000);
      continue;
    }

    let text = "";
    try {
      text = (await block.innerText()).trim();
    } catch {
      text = "";
    }

    if (isTrivialBotText(text)) {
      await page.waitForTimeout(1000);
      continue;
    }

    const cleaned = cleanBotText(text);

    if (cleaned !== lastCleaned) {
      lastCleaned = cleaned;
      lastChange = Date.now();
      await page.waitForTimeout(1000);
      continue;
    }

    // lastChange CHỈ được cập nhật ở nhánh text đổi phía trên. Không đụng vào nó
    // ở đây, nếu không idleMs sẽ bị ghim và mốc forceAcceptMs không bao giờ tới.
    const idleMs = Date.now() - lastChange;

    if (idleMs >= stableMs && !looksIncompleteBotText(text)) break;

    if (idleMs >= forceAcceptMs) {
      console.log(
        `⚠️ Text đứng yên ${Math.round(idleMs / 1000)}s mà vẫn bị coi là chưa xong — nhận luôn.`
      );
      break;
    }

    await page.waitForTimeout(1000);
  }

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
      { timeout: 450000 }
    );
  } catch {
    console.log("⚠️ Wait bot start timed out, continue...");
  }
}

/**
 * Send câu hỏi bằng Enter
 */
async function sendQuestion(page: Page, question: string) {
  console.log("✍️ Sending:", question);

  await page.waitForSelector(EDITOR_BOX, { timeout: 60000 });

  await page.click(EDITOR_BOX);

  // Clear input
  await page.keyboard.press("Control+A");
  await page.keyboard.press("Backspace");

  // Type chậm
  await page.keyboard.type(question, { delay: 30 });

  // Enter gửi
  await page.keyboard.press("Enter");

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
  // Panel nguồn là toggle: click lại khi đang mở sẽ ĐÓNG nó. Vòng retry cũ click
  // mỗi lượt nên panel cứ mở/đóng xen kẽ. Chỉ click khi chưa thấy item nguồn nào.
  const SOURCE_ITEM_SELECTOR = "button[id^='source-'], a[id^='source-']";
  const alreadyExpanded =
    (await lastBot.locator(SOURCE_ITEM_SELECTOR).count()) > 0;

  if (alreadyExpanded) {
    console.log("↩️  Panel nguồn đã mở sẵn, bỏ qua bước click.");
  } else {
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
  }

  // STEP 2: Wait sources appear
  let sourceButtons = lastBot.locator(SOURCE_ITEM_SELECTOR);

  try {
    await sourceButtons.first().waitFor({ timeout: 8000 });
  } catch {
    sourceButtons = page.locator(SOURCE_ITEM_SELECTOR);
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

/**
 * Cổng validate câu trả lời trước khi ghi vào output.
 *
 * CHỦ Ý không dùng looksIncompleteBotText ở đây. Hàm đó là tín hiệu tiến độ cho
 * waitLatestBotStable ("stream còn chạy không?"), không phải tiêu chí hợp lệ.
 * Khi vòng chờ force-accept vì heuristic đó báo "chưa xong", cổng validate dùng
 * lại đúng tiêu chí sẽ luôn loại câu trả lời — và retry đọc lại đúng chuỗi đã
 * đứng yên nên không bao giờ cứu được. Đáp án dạng bảng hoặc danh sách có dòng
 * cuối là một ô ngắn không dấu câu (vd "Ngày tạo", "10") luôn dính bẫy này.
 * Ở đây chỉ giữ những tiêu chí khách quan.
 */
function isBadAnswer(answer: string): boolean {
  if (!answer || answer.startsWith("❌")) return true;
  const cleaned = cleanBotText(answer).toLowerCase();
  if (!cleaned) return true;
  if (cleaned.startsWith("querying")) return true;
  if (cleaned.startsWith("searching")) return true;
  if (cleaned.length < MIN_ANSWER_LENGTH) return true;
  return false;
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

test("KB JSON Auto Answer + Source Extract (Restart every 10)", async ({
  browser,
}) => {
  test.setTimeout(3600000);

  /* ============================
     STEP 1: Load KB.json
  ============================ */

  console.log("📂 Loading KB.json...");
  const kbData = JSON.parse(fs.readFileSync(INPUT_FILE, "utf-8"));

  console.log("✅ Total questions:", kbData.length);

  /* ============================
     STEP 2: Load existing output.json
  ============================ */

  let output = loadExistingOutput();
  let startIndex = output.length;
  const flaggedIndexes: number[] = [];

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
      await sendQuestion(page, question);

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

        // Chỉ lấy lại phần đang hỏng. Trước đây cả hai đều bị đọc lại mỗi lượt,
        // vừa tốn thời gian vừa làm phần đã lấy được bị ghi đè bằng kết quả xấu.
        if (isBadAnswer(answer)) {
          answer = await getLatestBotAnswer(page, userIndex, prevBotText);
        }
        if (isBadSources(sources)) {
          sources = await getLatestBotSources(page, userIndex, prevBotText);
        }

        if (!isBadAnswer(answer) && !isBadSources(sources)) break;

        if (attempt < maxAttempts) {
          const missing = [
            isBadAnswer(answer) ? "answer" : null,
            isBadSources(sources) ? "sources" : null,
          ]
            .filter(Boolean)
            .join(" + ");
          console.log(`⚠️  Thiếu ${missing}, chờ rồi thử lại...`);
          await page.waitForTimeout(4500);
        }
      }

      const answerBad = isBadAnswer(answer);
      const sourcesBad = isBadSources(sources);
      const missingParts = [
        answerBad ? "answer" : null,
        sourcesBad ? "sources" : null,
      ]
        .filter(Boolean)
        .join("+");

      if (missingParts) {
        // Không throw nữa: output resume theo độ dài file, nên một câu hỏng sẽ
        // chặn vĩnh viễn toàn bộ phần còn lại của bộ câu hỏi. Ghi cờ rồi chạy
        // tiếp, review lại các câu có needs_review sau.
        await dumpDebug(page, `missing_${missingParts}_after_retries`);
        console.log(
          `⚠️  Câu ${startIndex + 1} thiếu ${missingParts} sau ${maxAttempts} lần thử — ghi cờ và chạy tiếp.`
        );
        console.log(`   answer(200): ${JSON.stringify(answer.slice(0, 200))}`);
        console.log(`   sources: ${JSON.stringify(sources)}`);
        flaggedIndexes.push(startIndex + 1);
      } else {
        console.log("✅ Answer:", answer);
        console.log("✅ Sources:", sources);
      }

      // ✅ Giữ nguyên structure KB.json nhưng không mutate file gốc
const originalObj = kbData[startIndex];

// clone object và chỉ thêm đúng field answer + file
const newObj: Record<string, any> = {
  ...originalObj,
  answer: answer,
  sources: sources,
};

if (missingParts) {
  newObj.needs_review = true;
  newObj.flag = `missing_${missingParts}`;
}

// push object đầy đủ vào output
output.push(newObj);



      // Save output after each question
      saveOutput(output);

      console.log("💾 Saved:", startIndex + 1);

      startIndex++;

      await page.waitForTimeout(3000);
    }

    console.log("♻️ Closing browser session after 10 questions...");
    await context.close();
  }

  console.log("\n✅ DONE! All questions completed.");
  console.log("📌 Output saved in:", OUTPUT_FILE);

  if (flaggedIndexes.length) {
    console.log(
      `⚠️  ${flaggedIndexes.length} câu bị gắn cờ needs_review: ${flaggedIndexes.join(", ")}`
    );
    console.log("   Xem test-results/kb-debug/ để đối chiếu HTML + ảnh chụp.");
  }
});
