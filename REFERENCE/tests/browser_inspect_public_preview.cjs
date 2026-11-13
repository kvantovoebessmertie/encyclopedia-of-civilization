"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { chromium } = require("playwright");

const root = path.resolve(process.argv[2] || "/tmp/mvp-synthetic-preview");
const output = path.resolve(process.argv[3] || "/tmp/mvp-browser-inspection");
fs.mkdirSync(output, { recursive: true });
for (const file of ["index.html", "search.js", "preview-manifest.json"]) {
  assert.ok(fs.existsSync(path.join(root, file)), `Missing preview artifact file: ${file}`);
}

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
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    page.on("pageerror", error => errors.push("pageerror: " + error.message));
    page.on("console", message => { if (message.type() === "error") errors.push("console: " + message.text()); });
    page.on("requestfailed", request => errors.push("requestfailed: " + request.url() + " " + (request.failure()?.errorText || "")));
    const response = await page.goto(`http://127.0.0.1:${address.port}/`, { waitUntil: "networkidle", timeout: 15000 });
    assert.equal(response.status(), 200, "Reader page should load successfully");
    await page.locator("#count").waitFor();
    assert.match(await page.locator("#count").innerText(), /2 of 2 records shown/);
    assert.equal(await page.locator("article").count(), 2, "Only the two synthetic allowlisted records should render");
    await page.screenshot({ path: path.join(output, "desktop-1280x900.png"), fullPage: true });

    // Exercise actual browser search behavior, including no-match and reset.
    await page.locator("#q").fill("DEMO-CLAIM-001");
    assert.match(await page.locator("#count").innerText(), /1 of 2 records shown/);
    assert.equal(await page.locator("article:visible").count(), 1);
    await page.locator("#q").fill("no-such-record");
    assert.match(await page.locator("#count").innerText(), /0 of 2 records shown/);
    await page.locator("#q").fill("");
    assert.match(await page.locator("#count").innerText(), /2 of 2 records shown/);

    // Verify first keyboard stop reaches the search field and focus is visible.
    await page.locator("#q").evaluate(el => el.blur());
    await page.locator("body").click({ position: { x: 1, y: 1 } });
    await page.keyboard.press("Tab");
    assert.equal(await page.evaluate(() => document.activeElement?.id), "q", "First Tab stop should be the search field");
    const focusVisible = await page.locator("#q").evaluate(el => {
      const style = getComputedStyle(el);
      return style.outlineStyle !== "none" || style.boxShadow !== "none";
    });
    assert.ok(focusVisible, "Keyboard focus should be visibly indicated by browser or authored style");
    // Walk the complete page-level tab sequence through every interactive preview control.
    const expectedTabOrder = ["q", "first-record-summary", "second-record-summary"];
    for (const expected of expectedTabOrder.slice(1)) {
      await page.keyboard.press("Tab");
      const active = await page.evaluate(() => {
        const el = document.activeElement;
        if (el?.id === "q") return "q";
        const summaries = Array.from(document.querySelectorAll("article details summary"));
        const index = summaries.indexOf(el);
        return index === 0 ? "first-record-summary" : index === 1 ? "second-record-summary" : (el?.tagName || "unknown").toLowerCase();
      });
      assert.equal(active, expected, "Keyboard focus order should follow search, then each record's technical-view disclosure");
    }

    // Real mobile viewport checks: no horizontal overflow and key content remains visible.
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
    assert.ok(mobile.headingVisible, "Main heading should fit within the mobile viewport width");
    assert.ok(mobile.searchVisible, "Search input should fit within the mobile viewport width");
    assert.match(mobile.bodyText, /не является редакционным одобрением|not editorial approval/i);
    await page.screenshot({ path: path.join(output, "mobile-390x844.png"), fullPage: true });

    assert.deepEqual(errors, [], "Browser console/runtime/network errors must be absent");
    fs.writeFileSync(path.join(output, "browser-inspection-results.json"), JSON.stringify({
      result: "PASS",
      viewport: "390x844",
      desktopScreenshot: "desktop-1280x900.png",
      mobileScreenshot: "mobile-390x844.png",
      checks: ["page load", "two-record allowlist", "search match/no-match/reset", "keyboard first focus", "visible focus", "keyboard focus order", "mobile no-horizontal-overflow", "mobile heading/search visibility", "console/runtime/network errors"],
      browserErrors: errors
    }, null, 2) + "\n");
    console.log("Browser inspection passed; screenshots and JSON report written to " + output);
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
  server.close();
});
