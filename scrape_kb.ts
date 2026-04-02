import { chromium } from "@playwright/test";
import fs from "fs";
import path from "path";

/* ============================
   CONFIG
============================ */

const KB_COLLECTION_URL = "https://kb.urbox.dev/collection/test123-NWfGO8uFOf/recent";

const SESSION_DIR = "./data/sessions/kb_session";
const OUTPUT_DIR = "./kb_files";
const METADATA_FILE = "./kb_files/.metadata.json";

// Delay giữa mỗi document khi trigger re-embed (ms)
// Đặt đủ dài để Outline save/process kịp
const TRIGGER_DELAY_MS = 3000;

/* ============================
   METADATA
============================ */

interface FileMeta {
  fileName: string;
  localSize: number;
  downloadedAt: string;
}

interface Metadata {
  files: Record<string, FileMeta>;
}

function loadMetadata(): Metadata {
  if (!fs.existsSync(METADATA_FILE)) return { files: {} };
  try {
    return JSON.parse(fs.readFileSync(METADATA_FILE, "utf-8"));
  } catch {
    return { files: {} };
  }
}

function saveMetadata(meta: Metadata) {
  fs.writeFileSync(METADATA_FILE, JSON.stringify(meta, null, 2), "utf-8");
}

function shouldSkip(fileName: string, meta: Metadata): boolean {
  const localPath = path.join(OUTPUT_DIR, fileName);
  if (!fs.existsSync(localPath)) return false;
  const prev = meta.files[fileName];
  if (!prev) return false;
  const localSize = fs.statSync(localPath).size;
  console.log(`   ⏭️  Skip (unchanged, local=${localSize}B, downloaded at ${prev.downloadedAt})`);
  return true;
}

function ensureOutputDir() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    console.log(`📁 Created output folder: ${OUTPUT_DIR}`);
  }
}

function cleanOutputDir() {
  if (!fs.existsSync(OUTPUT_DIR)) return;
  const entries = fs.readdirSync(OUTPUT_DIR);
  if (entries.length === 0) return;

  for (const name of entries) {
    const fullPath = path.join(OUTPUT_DIR, name);
    if (fs.statSync(fullPath).isFile()) {
      fs.unlinkSync(fullPath);
    }
  }

  console.log(`🧹 Cleaned output folder: ${OUTPUT_DIR}`);
}

/* ============================
   STEP 1: SCRAPE documents về local
============================ */

async function scrapeDocuments(page: any, docs: { title: string; href: string }[]) {
  const meta = loadMetadata();
  let skipped = 0;
  let downloaded = 0;

  for (let idx = 0; idx < docs.length; idx++) {
    const doc = docs[idx];
    const safeFileName = doc.title.replace(/[/\\:*?"<>|]/g, "_").replace(/\s+/g, "_") + ".md";

    console.log(`\n📄 [${idx + 1}/${docs.length}] ${doc.title}`);

    if (shouldSkip(safeFileName, meta)) {
      skipped++;
      continue;
    }

    const fullUrl = doc.href.startsWith("http") ? doc.href : `https://kb.urbox.dev${doc.href}`;
    await page.goto(fullUrl);
    await page.waitForTimeout(2000);

    // --- Attempt 1: Inline content ---
    const contentSelectors = [
      "div[class*='document-editor']",
      "div.ProseMirror",
      "article",
      "div[class*='Editor']",
      "div[class*='content']",
      "main",
    ];

    let extracted = "";

    for (const sel of contentSelectors) {
      const el = page.locator(sel);
      if ((await el.count()) > 0) {
        const text = (await el.first().innerText()).trim();
        if (text.length > 20) {
          extracted = text;
          console.log(`   📝 Extracted via: ${sel} (${text.length} chars)`);
          break;
        }
      }
    }

    // --- Attempt 2: Outline API ---
    if (!extracted) {
      console.log("   ⚠️ Inline failed, trying Outline API...");

      const slugMatch = fullUrl.match(/\/doc\/(.+)$/);
      if (slugMatch) {
        const slug = slugMatch[1];

        const apiResponse = await page.evaluate(async (slug: string) => {
          const res = await fetch("https://kb.urbox.dev/api/documents.search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: slug }),
          });
          return await res.text();
        }, slug);

        try {
          const apiData = JSON.parse(apiResponse);
          if (apiData.data && apiData.data.length > 0) {
            extracted = apiData.data[0].document.text;
            console.log(`   📝 Extracted via Outline API (${extracted.length} chars)`);
          }
        } catch {
          console.log("   ⚠️ API parse failed");
        }
      }
    }

    if (extracted) {
      const savePath = path.join(OUTPUT_DIR, safeFileName);
      fs.writeFileSync(savePath, extracted, "utf-8");

      const localSize = fs.statSync(savePath).size;
      meta.files[safeFileName] = {
        fileName: safeFileName,
        localSize,
        downloadedAt: new Date().toISOString(),
      };
      saveMetadata(meta);

      console.log(`   ✅ Saved: ${savePath} (${localSize.toLocaleString()} bytes)`);
      downloaded++;
    } else {
      console.log(`   ❌ Could not extract content`);
      await page.screenshot({ path: path.join(OUTPUT_DIR, `_debug_${safeFileName}.png`) });
    }
  }

  console.log(`\n📥 Scrape done — Downloaded: ${downloaded}, Skipped: ${skipped}`);
}

/* ============================
   STEP 2: TRIGGER re-embed
   Vào từng doc, append whitespace ở cuối, save.
   Outline auto-save nên chỉ cần focus vào editor + type + wait.
============================ */

async function triggerReEmbed(page: any, docs: { title: string; href: string }[]) {
  console.log("\n🔄 Starting re-embed trigger...");

  for (let idx = 0; idx < docs.length; idx++) {
    const doc = docs[idx];
    console.log(`\n⚡ Triggering [${idx + 1}/${docs.length}] ${doc.title}`);

    const fullUrl = doc.href.startsWith("http") ? doc.href : `https://kb.urbox.dev${doc.href}`;
    await page.goto(fullUrl);
    await page.waitForTimeout(2000);

    // Tìm editor (ProseMirror là editor của Outline)
    const editor = page.locator("div.ProseMirror");
    if ((await editor.count()) === 0) {
      console.log("   ⚠️ Editor not found, skipping");
      continue;
    }

    // Click vào cuối document
    await editor.first().click();
    await page.keyboard.press("Control+End"); // jump to end
    await page.waitForTimeout(500);

    // Append 1 whitespace
    await page.keyboard.press("End");         // đảm bảo ở cuối line
    await page.keyboard.type(" ");            // append space
    await page.waitForTimeout(500);

    // Outline auto-save — wait cho save kịp
    // Thường có loading indicator "Saving..." → wait disappear
    // Fallback: wait fixed delay
    await page.waitForTimeout(TRIGGER_DELAY_MS);

    console.log(`   ✅ Triggered: ${doc.title}`);
  }

  console.log("\n✅ Re-embed trigger done for all documents!");
}

/* ============================
   MAIN
============================ */

async function main() {
  ensureOutputDir();
  cleanOutputDir();

  if (!fs.existsSync(SESSION_DIR)) {
    console.log("❌ Session not found!");
    console.log("   → Chạy trước: npx ts-node setup_session.ts");
    return;
  }

  console.log("🚀 Launching browser with saved session...");
  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: false,
  });

  const page = context.pages()[0] || (await context.newPage());

  // Navigate đến collection
  console.log("📂 Navigating to KB collection...");
  await page.goto(KB_COLLECTION_URL);
  await page.waitForTimeout(3000);

  const actualUrl = page.url();
  console.log(`🛠 Actual URL: ${actualUrl}`);

  if (actualUrl.includes("/login") || actualUrl.includes("/signin")) {
    console.log("❌ Session expired! Chạy lại setup_session.ts để login lại.");
    await context.close();
    return;
  }

  // Lấy danh sách documents
  const docLinks = page.locator("a[href*='/doc/']");
  const docCount = await docLinks.count();
  console.log(`📌 Found ${docCount} document links`);

  const docs: { title: string; href: string }[] = [];

  for (let i = 0; i < docCount; i++) {
    const link = docLinks.nth(i);
    const href = await link.getAttribute("href");
    const title = (await link.innerText()).split("\n")[0].trim();
    if (href && title && !docs.find((d) => d.href === href)) {
      docs.push({ title, href });
    }
  }

  console.log(`📌 Unique documents: ${docs.length}`);
  docs.forEach((d, i) => console.log(`   ${i + 1}. ${d.title}`));

  if (docs.length === 0) {
    const pageText = await page.innerText("body");
    fs.writeFileSync(path.join(OUTPUT_DIR, "_debug_pagetext.txt"), pageText, "utf-8");
    const pageHtml = await page.content();
    fs.writeFileSync(path.join(OUTPUT_DIR, "_debug_pagehtml.html"), pageHtml, "utf-8");
    console.log("❌ No documents found. Debug files dumped.");
    await context.close();
    return;
  }

  // ── STEP 1: Scrape ──
  await scrapeDocuments(page, docs);

  // ── STEP 2: Trigger re-embed ──
  await triggerReEmbed(page, docs);

  // ── Summary ──
  const saved = fs.readdirSync(OUTPUT_DIR).filter((f) => f.endsWith(".md"));
  console.log("\n================================");
  console.log(`✅ All done!`);
  console.log(`   📁 Total files in ${OUTPUT_DIR}/: ${saved.length}`);
  console.log("--------------------------------");
  saved.forEach((f) => {
    const size = fs.statSync(path.join(OUTPUT_DIR, f)).size;
    console.log(`   📄 ${f} (${size.toLocaleString()} bytes)`);
  });
  console.log("================================\n");

  await context.close();
}

main().catch(console.error);
