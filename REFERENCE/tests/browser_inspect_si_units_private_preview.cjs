"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { chromium } = require("playwright");

const root = path.resolve(process.argv[2] || "/tmp/mvp-si-private-review-preview");
const output = path.resolve(process.argv[3] || "/tmp/mvp-si-browser-inspection");
fs.mkdirSync(output, { recursive: true });
for (const file of ["index.html", "search.js", "preview-manifest.json"]) {
  assert.ok(fs.existsSync(path.join(root, file)), `Missing preview artifact file: ${file}`);
}

const expectedIds = [
  "CLM-SI-DERIVED",
  "CLM-SI-SEVEN-BASE",
  "CTX-SI",
  "EU-SI-DERIVED",
  "EU-SI-SEVEN-BASE",
  "SCP-SI",
  "SRC-NIST-SI-UNITS"
];
const manifest = JSON.parse(fs.readFileSync(path.join(root, "preview-manifest.json"), "utf8"));
assert.deepEqual(manifest.selected_records.map(x => x.record_id), expectedIds);
assert.equal(manifest.record_count, 7);
assert.equal(manifest.redistribution_allowed, false);
assert.equal(manifest.network_required, false);
assert.equal(manifest.selected_record_hashes.length, 7);

const mime = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8" };
const server = http.createServer((req, res) => {
  const pathname = decodeURIComponent(new URL(req.url, "http://127.0.0.1").pathname);
  const file = pathname === "/" ? "index.html" : pathname.slice(1);
  if (!["index.html", "search.js", "preview-manifest.json"].includes(file)) {
    res.writeHead(404); res.end("Not found"); return;
  }
  res.writeHead(200, { "content-type": mime[path.extname(file)] || "application/octet-stream", "x-content-type-options": "nosniff" });
  fs.createReadStream(path.join(root, file)).pipe(res);
});

(async () => {
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const address = server.address();
  const browser = await chromium.launch({ headless: true });
  const errors = [];
  const externalRequests = [];
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    page.on("pageerror", error => errors.push("pageerror: " + error.message));
    page.on("console", message => { if (message.type() === "error") errors.push("console: " + message.text()); });
    page.on("requestfailed", request => errors.push("requestfailed: " + request.url() + " " + (request.failure()?.errorText || "")));
    page.on("request", request => {
      if (!request.url().startsWith(`http://127.0.0.1:${address.port}/`)) externalRequests.push(request.url());
    });
    const response = await page.goto(`http://127.0.0.1:${address.port}/`, { waitUntil: "networkidle", timeout: 15000 });
    assert.equal(response.status(), 200, "Private reader page should load successfully");
    await page.locator("#count").waitFor();
    assert.match(await page.locator("#count").innerText(), /7 of 7 records shown/);
    assert.equal(await page.locator("article").count(), 7, "Only the seven authorized SI review records should render");
    const pageText = await page.locator("body").innerText();
    assert.match(pageText, /CLM-SI-SEVEN-BASE/);
    assert.match(pageText, /CLM-SI-DERIVED/);
    assert.match(pageText, /Defining Constants/);
    assert.match(pageText, /Base and Derived Units/);
    assert.match(pageText, /22/);
    assert.match(pageText, /не означает одобрения NIST/i);
    assert.match(pageText, /не распространять автоматически на Claim B/i);
    assert.doesNotMatch(pageText, /CLM-SI-ACCURACY-BOUNDARY/);
    assert.equal(await page.locator('a[href="https://www.nist.gov/pml/owm/metric-si/si-units"]').count(), 1);
    await page.screenshot({ path: path.join(output, "desktop-1280x900.png"), fullPage: true });

    await page.locator("#q").fill("определения которых выражены");
    assert.match(await page.locator("#count").innerText(), /1 of 7 records shown/);
    assert.equal(await page.locator("article:visible").count(), 1);
    await page.locator("#q").fill("NIST отмечает 22 производные единицы");
    assert.match(await page.locator("#count").innerText(), /1 of 7 records shown/);
    await page.locator("#q").fill("no-such-record");
    assert.match(await page.locator("#count").innerText(), /0 of 7 records shown/);
    await page.locator("#q").fill("");
    assert.match(await page.locator("#count").innerText(), /7 of 7 records shown/);

    await page.locator("#q").evaluate(el => el.blur());
    await page.locator("body").click({ position: { x: 1, y: 1 } });
    await page.keyboard.press("Tab");
    assert.equal(await page.evaluate(() => document.activeElement?.id), "q");
    const focusVisible = await page.locator("#q").evaluate(el => {
      const style = getComputedStyle(el);
      return style.outlineStyle !== "none" || style.boxShadow !== "none";
    });
    assert.ok(focusVisible, "Keyboard focus should be visibly indicated");
    const focusables = page.locator('a[href], article details summary');
    const focusableCount = await focusables.count();
    assert.ok(focusableCount >= 7, "All source/reference links and technical-view disclosures should be keyboard reachable");
    for (let index = 0; index < focusableCount; index++) {
      await page.keyboard.press("Tab");
      const focusedIndex = await page.evaluate(() =>
        Array.from(document.querySelectorAll('a[href], article details summary'))
          .indexOf(document.activeElement)
      );
      assert.equal(focusedIndex, index, "Keyboard focus should follow DOM order across record links and technical-view disclosures");
    }

    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(`http://127.0.0.1:${address.port}/`, { waitUntil: "networkidle", timeout: 15000 });
    const mobile = await page.evaluate(() => ({
      viewportWidth: window.innerWidth,
      documentWidth: document.documentElement.scrollWidth,
      headingVisible: (() => { const r = document.querySelector("h1").getBoundingClientRect(); return r.width > 0 && r.left >= 0 && r.right <= window.innerWidth; })(),
      searchVisible: (() => { const r = document.querySelector("#q").getBoundingClientRect(); return r.width > 0 && r.left >= 0 && r.right <= window.innerWidth; })(),
      bodyText: document.body.innerText
    }));
    assert.ok(mobile.documentWidth <= mobile.viewportWidth, `Mobile horizontal overflow: ${mobile.documentWidth}px > ${mobile.viewportWidth}px`);
    assert.ok(mobile.headingVisible);
    assert.ok(mobile.searchVisible);
    assert.match(mobile.bodyText, /не является редакционным одобрением|not editorial approval/i);
    await page.screenshot({ path: path.join(output, "mobile-390x844.png"), fullPage: true });

    assert.deepEqual(errors, [], "Browser console/runtime/network errors must be absent");
    assert.deepEqual(externalRequests, [], "Private preview must not make external network requests");
    fs.writeFileSync(path.join(output, "browser-inspection-results.json"), JSON.stringify({
      result: "PASS",
      viewport: "390x844",
      recordCount: 7,
      selectedRecordIds: expectedIds,
      desktopScreenshot: "desktop-1280x900.png",
      mobileScreenshot: "mobile-390x844.png",
      checks: [
        "exact seven-record private allowlist",
        "third SI Claim excluded",
        "NIST attribution link present",
        "Claim-specific section pinpoints visible",
        "22 special-named derived-unit boundary visible",
        "search match/no-match/reset",
        "keyboard first focus and visible focus",
        "keyboard focus order through seven technical disclosures",
        "mobile no-horizontal-overflow",
        "mobile heading/search visibility",
        "no external requests",
        "no console/runtime errors"
      ],
      browserErrors: errors,
      externalRequests
    }, null, 2) + "\n");
    console.log("SI private review browser inspection passed; screenshots and report written to " + output);
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
  server.close();
});
