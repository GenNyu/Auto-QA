const { chromium } = require("@playwright/test");
const fs = require("fs");
const path = require("path");

const args = parseArgs(process.argv.slice(2));

const DEFAULT_COLLECTION_URL =
  "https://kb.urbox.vn/collection/public-engr-o6fF0NycI7/recent";

const COLLECTION_URL = args.url || DEFAULT_COLLECTION_URL;
const INPUT_DIR = args.input || "pcidss/Appendixes";
const SESSION_DIR = args.session || "./data/sessions/kb_session_vn";
const REPORT_FILE = args.report || "./kb_add_iso_report.json";

const DRY_RUN = parseBool(args["dry-run"], false);
const FORCE = parseBool(args.force, false);
const INCLUDE_README = parseBool(args["include-readme"], false);
const HEADLESS = parseBool(args.headless, false);
const PUBLISH = parseBool(args.publish, true);

const DELAY_MS = args.delay ? Number(args.delay) : 1000;
const LIMIT = args.limit ? Number(args.limit) : undefined;

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

function parseBool(value, defaultValue = false) {
  if (value === undefined) return defaultValue;
  return value === true || value === "true";
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function getMarkdownFiles(inputDir) {
  if (!fs.existsSync(inputDir)) {
    throw new Error(`Input directory not found: ${inputDir}`);
  }

  return fs
    .readdirSync(inputDir)
    .filter((name) => name.toLowerCase().endsWith(".md"))
    .filter((name) => INCLUDE_README || name.toLowerCase() !== "readme.md")
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }))
    .map((name) => path.join(inputDir, name));
}

function titleFromFile(filePath) {
  return path.basename(filePath, path.extname(filePath));
}

function getCollectionUrlId(collectionUrl) {
  const url = new URL(collectionUrl);

  const collectionSegment = url.pathname
    .split("/")
    .filter(Boolean)
    .find((segment, index, parts) => parts[index - 1] === "collection");

  if (!collectionSegment) return undefined;

  const parts = collectionSegment.split("-");
  return parts[parts.length - 1] || undefined;
}

async function getCsrfToken(page) {
  const token = await page.evaluate(() => {
    const metaToken =
      document.querySelector('meta[name="csrf-token"]')?.content ||
      document.querySelector('meta[name="csrfToken"]')?.content;

    if (metaToken) return metaToken;

    const csrfFromCookie = document.cookie
      .split("; ")
      .find((row) => {
        const name = row.split("=")[0].toLowerCase();
        return name.includes("csrf") || name.includes("xsrf");
      });

    if (csrfFromCookie) {
      return decodeURIComponent(csrfFromCookie.split("=")[1]);
    }

    return undefined;
  });

  if (token) return token;

  const cookies = await page.context().cookies();
  const csrfCookie = cookies.find((cookie) => {
    const name = cookie.name.toLowerCase();
    return name.includes("csrf") || name.includes("xsrf");
  });

  return csrfCookie?.value;
}

async function apiPost(page, origin, endpoint, body) {
  const csrfToken = await getCsrfToken(page);

  if (!csrfToken) {
    throw new Error(
      `CSRF token not found before calling ${endpoint}. Open the page manually and check Network headers.`
    );
  }

  const response = await page.evaluate(
    async ({ origin, endpoint, body, csrfToken }) => {
      const res = await fetch(`${origin}/api/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify(body),
      });

      const text = await res.text();

      return {
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        text,
      };
    },
    { origin, endpoint, body, csrfToken }
  );

  let data;

  try {
    data = JSON.parse(response.text);
  } catch {
    data = undefined;
  }

  if (!response.ok) {
    const detail = data ? JSON.stringify(data) : response.text;

    throw new Error(
      `${endpoint} failed (${response.status} ${response.statusText}): ${detail}`
    );
  }

  return data;
}

async function resolveCollectionId(page, origin, collectionUrl) {
  const targetUrl = new URL(collectionUrl);
  const targetPath = targetUrl.pathname.replace(/\/recent\/?$/, "");
  const targetUrlId = getCollectionUrlId(collectionUrl);

  const list = await apiPost(page, origin, "collections.list", {
    offset: 0,
    limit: 100,
  });

  const collections = Array.isArray(list.data) ? list.data : [];

  const found = collections.find((collection) => {
    const collectionUrlValue = collection.url || "";

    return (
      collection.urlId === targetUrlId ||
      collectionUrlValue === targetPath ||
      collectionUrlValue.endsWith(targetPath) ||
      (targetUrlId && collectionUrlValue.includes(targetUrlId))
    );
  });

  if (found && found.id) {
    return {
      id: found.id,
      name: found.name || found.title || targetPath,
    };
  }

  if (targetUrlId) {
    const info = await apiPost(page, origin, "collections.info", {
      id: targetUrlId,
    });

    if (info.data && info.data.id) {
      return {
        id: info.data.id,
        name: info.data.name || info.data.title || targetPath,
      };
    }
  }

  throw new Error(
    `Could not resolve collection id from URL: ${collectionUrl}. ` +
      "Open the target collection with a logged-in account that can edit it."
  );
}

async function listExistingTitles(page, origin, collectionId) {
  const titles = new Set();
  const limit = 100;
  let offset = 0;

  while (true) {
    const response = await apiPost(page, origin, "documents.list", {
      collectionId,
      offset,
      limit,
    });

    const documents = Array.isArray(response.data) ? response.data : [];

    for (const document of documents) {
      if (document.title) {
        titles.add(document.title.trim().toLowerCase());
      }
    }

    if (documents.length < limit) break;
    offset += documents.length;
  }

  return titles;
}

async function createDocument(page, origin, collectionId, title, text) {
  const response = await apiPost(page, origin, "documents.create", {
    title,
    text,
    collectionId,
    publish: PUBLISH,
  });

  if (!response.data || !response.data.id) {
    throw new Error(
      `documents.create returned an unexpected response for ${title}`
    );
  }

  return response.data;
}

function writeReport(report) {
  fs.writeFileSync(REPORT_FILE, JSON.stringify(report, null, 2), "utf8");
}

async function main() {
  if (Number.isNaN(DELAY_MS)) {
    throw new Error("Invalid --delay value");
  }

  if (LIMIT !== undefined && Number.isNaN(LIMIT)) {
    throw new Error("Invalid --limit value");
  }

  const files = getMarkdownFiles(INPUT_DIR);
  const uploadFiles = LIMIT ? files.slice(0, LIMIT) : files;
  const origin = new URL(COLLECTION_URL).origin;

  console.log(`Collection URL: ${COLLECTION_URL}`);
  console.log(`Input directory: ${INPUT_DIR}`);
  console.log(`Markdown files: ${uploadFiles.length}`);
  console.log(`Session directory: ${SESSION_DIR}`);
  console.log(`Mode: ${DRY_RUN ? "dry-run" : "create documents"}`);

  if (uploadFiles.length === 0) {
    console.log("No Markdown files found.");
    return;
  }

  if (!fs.existsSync(SESSION_DIR)) {
    throw new Error(
      `Session not found: ${SESSION_DIR}. Run: node setup_kb_session.js --url ${origin}`
    );
  }

  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: HEADLESS,
  });

  const page = context.pages()[0] || (await context.newPage());

  const report = {
    collectionUrl: COLLECTION_URL,
    inputDir: INPUT_DIR,
    startedAt: new Date().toISOString(),
    dryRun: DRY_RUN,
    force: FORCE,
    publish: PUBLISH,
    created: [],
    skipped: [],
    failed: [],
  };

  try {
    await page.goto(COLLECTION_URL, { waitUntil: "domcontentloaded" });
    await page.waitForTimeout(3000);

    const currentUrl = page.url();

    if (currentUrl.includes("/login") || currentUrl.includes("/signin")) {
      throw new Error(
        `Session is not logged in. Run: node setup_kb_session.js --url ${origin}`
      );
    }

    const csrfToken = await getCsrfToken(page);
    console.log(`CSRF token: ${csrfToken ? "found" : "not found"}`);

    const collection = await resolveCollectionId(page, origin, COLLECTION_URL);
    console.log(`Resolved collection: ${collection.name} (${collection.id})`);

    const existingTitles = FORCE
      ? new Set()
      : await listExistingTitles(page, origin, collection.id);

    for (let index = 0; index < uploadFiles.length; index++) {
      const filePath = uploadFiles[index];
      const title = titleFromFile(filePath);
      const normalizedTitle = title.trim().toLowerCase();
      const text = fs.readFileSync(filePath, "utf8");

      console.log(`[${index + 1}/${uploadFiles.length}] ${title}`);

      if (!FORCE && existingTitles.has(normalizedTitle)) {
        console.log("  skipped: title already exists");
        report.skipped.push({
          file: filePath,
          title,
          reason: "title_exists",
        });
        continue;
      }

      if (DRY_RUN) {
        console.log("  dry-run: would create");
        report.skipped.push({
          file: filePath,
          title,
          reason: "dry_run",
        });
        continue;
      }

      try {
        const document = await createDocument(
          page,
          origin,
          collection.id,
          title,
          text
        );

        console.log(`  created: ${document.id}`);

        report.created.push({
          file: filePath,
          title,
          id: document.id,
          url: document.url,
        });

        existingTitles.add(normalizedTitle);
      } catch (error) {
        console.log(`  failed: ${error.message}`);

        report.failed.push({
          file: filePath,
          title,
          error: error.message,
        });
      }

      if (DELAY_MS > 0) {
        await sleep(DELAY_MS);
      }
    }
  } finally {
    report.finishedAt = new Date().toISOString();
    writeReport(report);
    await context.close();
  }

  console.log("");
  console.log(`Created: ${report.created.length}`);
  console.log(`Skipped: ${report.skipped.length}`);
  console.log(`Failed: ${report.failed.length}`);
  console.log(`Report: ${REPORT_FILE}`);

  if (report.failed.length > 0) {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});