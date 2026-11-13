"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const Ajv = require("ajv");
const addFormats = require("ajv-formats");
const { chromium } = require("playwright");

const root = path.resolve(process.argv[2] || process.cwd());
const output = path.resolve(process.argv[3] || "/tmp/mvp-form-browser");
fs.mkdirSync(output, { recursive: true });

const pageFile = path.join(root, "CONTRIBUTIONS", "intake-form-prototype.html");
const scriptFile = path.join(root, "CONTRIBUTIONS", "intake-form.js");
const schemaFile = path.join(root, "CONTRIBUTIONS", "contribution-submission-v1.schema.json");
for (const file of [pageFile, scriptFile, schemaFile]) {
  assert.ok(fs.existsSync(file), "Missing required form file: " + file);
}

const schema = JSON.parse(fs.readFileSync(schemaFile, "utf8"));
const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);
const validate = ajv.compile(schema);

const allowed = new Map([
  ["/", { file: pageFile, type: "text/html; charset=utf-8" }],
  ["/intake-form.js", { file: scriptFile, type: "text/javascript; charset=utf-8" }]
]);
const server = http.createServer((req, res) => {
  const pathname = new URL(req.url, "http://127.0.0.1").pathname;
  const item = allowed.get(pathname);
  if (!item) {
    res.writeHead(404);
    res.end("Not found");
    return;
  }
  res.writeHead(200, {
    "content-type": item.type,
    "x-content-type-options": "nosniff",
    "cache-control": "no-store"
  });
  fs.createReadStream(item.file).pipe(res);
});

function fillBase(page, type) {
  return (async () => {
    await page.locator("#submission_type").selectOption(type);
    await page.locator("#subject_area").fill("Тестовая предметная область");
    await page.locator("#topic").fill("Автоматическая проверка");
    await page.locator("#title").fill("Тестовое предложение для проверки формы");
    await page.locator("#proposal_text").fill("Это синтетический текст предложения для проверки браузерного сценария.");
    await page.locator("#rationale").fill("Тест проверяет корректность формирования локального JSON и работу условных требований.");
    await page.locator("#evidence_notes").fill("Синтетический источник и тестовый локатор используются только в автоматической проверке.");
    await page.locator("#applicability").fill("Только тестовая среда.");
    await page.locator("#limitations").fill("Не является реальным содержательным утверждением.");
    await page.locator("#uncertainty").fill("Тестовые данные.");
    await page.locator("#contributor_role").selectOption("researcher");
    await page.locator("#rights_ack").check();
  })();
}

function setSource(page, index, title, supports) {
  return (async () => {
    const entry = page.locator(".source-entry").nth(index);
    await entry.locator('[data-field="title"]').fill(title);
    await entry.locator('[data-field="publisher"]').fill("Synthetic test publisher");
    await entry.locator('[data-field="publication_date"]').fill("2026");
    await entry.locator('[data-field="url"]').fill("https://example.org/synthetic-source");
    await entry.locator('[data-field="locator"]').fill("Section 1, test paragraph");
    await entry.locator('[data-field="supports"]').fill(supports);
    await entry.locator('[data-field="limitations"]').fill("Synthetic fixture; no factual support is claimed.");
  })();
}

async function downloadAndValidate(page, name) {
  const downloadPromise = page.waitForEvent("download");
  await page.locator('button[type="submit"]').click();
  const download = await downloadPromise;
  const target = path.join(output, name);
  await download.saveAs(target);
  const payload = JSON.parse(fs.readFileSync(target, "utf8"));
  const valid = validate(payload);
  assert.ok(valid, name + " failed JSON Schema validation: " + JSON.stringify(validate.errors));
  return payload;
}

async function expectBrowserValidationFailure(page) {
  await page.locator('button[type="submit"]').click();
  const valid = await page.locator("#contribution-form").evaluate(form => form.checkValidity());
  assert.equal(valid, false, "Expected native browser validation to block incomplete form");
}

(async () => {
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const address = server.address();
  const browser = await chromium.launch({ headless: true });
  const browserErrors = [];
  const externalRequests = [];
  let payloadIndex = 0;

  try {
    const context = await browser.newContext({
      acceptDownloads: true,
      viewport: { width: 1280, height: 900 }
    });
    const page = await context.newPage();
    page.on("pageerror", error => browserErrors.push("pageerror: " + error.message));
    page.on("console", message => {
      if (message.type() === "error") browserErrors.push("console: " + message.text());
    });
    page.on("request", request => {
      const url = new URL(request.url());
      if (url.hostname !== "127.0.0.1") externalRequests.push(request.url());
    });

    const response = await page.goto("http://127.0.0.1:" + address.port + "/", {
      waitUntil: "networkidle",
      timeout: 15000
    });
    assert.equal(response.status(), 200);
    assert.equal(await page.locator(".source-entry").count(), 1, "Form should start with one optional source editor");
    assert.equal(await page.locator(".relation-entry").count(), 0);
    assert.equal(await page.locator("#submission_type").inputValue(), "new_claim");

    // New Claim: source title and support must be required; valid payload must satisfy the schema.
    await fillBase(page, "new_claim");
    assert.equal(await page.locator('.source-entry [data-field="title"]').isRequired(), true);
    await expectBrowserValidationFailure(page);
    await setSource(page, 0, "Synthetic source for new Claim", "Supports only the synthetic test proposition.");
    const newClaim = await downloadAndValidate(page, "01-new-claim.json");
    assert.equal(newClaim.submission_type, "new_claim");
    assert.equal(newClaim.sources.length, 1);
    assert.equal(newClaim.sources[0].locator, "Section 1, test paragraph");

    // Gap: an untouched source editor is optional and is omitted from the JSON array.
    await fillBase(page, "gap");
    const gap = await downloadAndValidate(page, "02-gap-no-source.json");
    assert.equal(gap.submission_type, "gap");
    assert.deepEqual(gap.sources, []);

    // Correction: at least one related record ID is required; no source is required.
    await fillBase(page, "correction");
    await expectBrowserValidationFailure(page);
    await page.locator("#related_record_ids").fill("CLM-SYNTHETIC-001");
    const correction = await downloadAndValidate(page, "03-correction.json");
    assert.deepEqual(correction.related_record_ids, ["CLM-SYNTHETIC-001"]);
    assert.deepEqual(correction.sources, []);

    // Contradiction: two distinct related IDs are required.
    await fillBase(page, "contradiction");
    await page.locator("#related_record_ids").fill("CLM-SYNTHETIC-001");
    await expectBrowserValidationFailure(page);
    await page.locator("#related_record_ids").fill("CLM-SYNTHETIC-001\nCLM-SYNTHETIC-002");
    const contradiction = await downloadAndValidate(page, "04-contradiction.json");
    assert.equal(contradiction.related_record_ids.length, 2);

    // Source proposal: both a related record and a completed source are required.
    await fillBase(page, "source");
    await page.locator("#related_record_ids").fill("CLM-SYNTHETIC-003");
    await expectBrowserValidationFailure(page);
    await setSource(page, 0, "Synthetic source proposal", "Provides a test source description.");
    const sourceProposal = await downloadAndValidate(page, "05-source-proposal.json");
    assert.equal(sourceProposal.submission_type, "source");
    assert.equal(sourceProposal.sources.length, 1);

    // Relation proposal: dynamic entry, required fields, direction and payload structure.
    await fillBase(page, "relation");
    await page.locator("#add-relation").click();
    assert.equal(await page.locator(".relation-entry").count(), 1);
    const relation = page.locator(".relation-entry").first();
    await relation.locator('[data-field="source_record_id"]').fill("CLM-SYNTHETIC-004");
    await relation.locator('[data-field="target_record_id"]').fill("CLM-SYNTHETIC-005");
    await relation.locator('[data-field="relation_type"]').fill("depends_on");
    await relation.locator('[data-field="rationale"]').fill("Synthetic relation rationale for automated testing.");
    const relationPayload = await downloadAndValidate(page, "06-relation.json");
    assert.equal(relationPayload.proposed_relations.length, 1);
    assert.equal(relationPayload.proposed_relations[0].direction, "directed");

    // Duplicate IDs are rejected by the browser-side business rule, not silently deduplicated.
    await fillBase(page, "correction");
    await page.locator("#related_record_ids").fill("CLM-SYNTHETIC-006\nCLM-SYNTHETIC-006");
    await page.locator('button[type="submit"]').click();
    assert.match(await page.locator("#status").innerText(), /дубликаты/i);

    // Add/remove controls and reset return the form to a clean, usable initial state.
    await page.locator("#add-source").click();
    assert.equal(await page.locator(".source-entry").count(), 2);
    await page.locator(".source-entry").nth(1).locator("[data-remove]").click();
    assert.equal(await page.locator(".source-entry").count(), 1);
    await page.locator("#add-relation").click();
    assert.equal(await page.locator(".relation-entry").count(), 1);
    await page.locator(".relation-entry").first().locator("[data-remove]").click();
    assert.equal(await page.locator(".relation-entry").count(), 0);
    await page.locator('button[type="reset"]').click();
    await page.waitForFunction(() =>
      document.querySelectorAll(".source-entry").length === 1 &&
      document.querySelectorAll(".relation-entry").length === 0 &&
      document.querySelector("#submission_type").value === "new_claim"
    );
    assert.equal(await page.locator("#title").inputValue(), "");
    assert.equal(await page.locator("#status").innerText(), "");

    // Keyboard-only entry and visible focus.
    await page.locator("body").click({ position: { x: 1, y: 1 } });
    await page.keyboard.press("Tab");
    assert.equal(await page.evaluate(() => document.activeElement?.id), "submission_type");
    const focusVisible = await page.locator("#submission_type").evaluate(el => {
      const style = getComputedStyle(el);
      return style.outlineStyle !== "none" || style.boxShadow !== "none";
    });
    assert.ok(focusVisible, "Keyboard focus must be visibly indicated");

    // Narrow viewport: no horizontal overflow or clipped primary controls.
    await page.setViewportSize({ width: 390, height: 844 });
    const mobile = await page.evaluate(() => ({
      viewportWidth: window.innerWidth,
      documentWidth: document.documentElement.scrollWidth,
      headingVisible: (() => {
        const rect = document.querySelector("h1").getBoundingClientRect();
        return rect.width > 0 && rect.left >= 0 && rect.right <= window.innerWidth;
      })(),
      submitVisible: (() => {
        const rect = document.querySelector('button[type="submit"]').getBoundingClientRect();
        return rect.width > 0 && rect.left >= 0 && rect.right <= window.innerWidth;
      })()
    }));
    assert.ok(mobile.documentWidth <= mobile.viewportWidth, "Mobile horizontal overflow detected");
    assert.ok(mobile.headingVisible, "Main heading should fit on mobile");
    assert.ok(mobile.submitVisible, "Submit control should fit on mobile");
    await page.screenshot({ path: path.join(output, "form-mobile-390x844.png"), fullPage: true });

    assert.deepEqual(externalRequests, [], "Local-only form must not issue external requests");
    assert.deepEqual(browserErrors, [], "Browser console/runtime errors must be absent");
    fs.writeFileSync(path.join(output, "browser-form-results.json"), JSON.stringify({
      result: "PASS",
      schema: schema.$id,
      payloadsValidated: [
        "01-new-claim.json",
        "02-gap-no-source.json",
        "03-correction.json",
        "04-contradiction.json",
        "05-source-proposal.json",
        "06-relation.json"
      ],
      checks: [
        "JSON Schema validation of downloaded payloads",
        "conditional source requirements",
        "conditional related-record requirements",
        "duplicate-ID rejection",
        "relation add/remove and payload",
        "source add/remove",
        "form reset",
        "keyboard-only first focus",
        "visible keyboard focus",
        "mobile no-horizontal-overflow",
        "no external requests",
        "no browser console/runtime errors"
      ],
      externalRequests,
      browserErrors
    }, null, 2) + "\n");

    console.log("Contribution form browser inspection passed; results: " + output);
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error => {
  console.error(error);
  server.close();
  process.exitCode = 1;
});
