# Independent Security & Offline Review — PR #41 (SEC-1 HTML escaping)

- **Role:** Security & Offline (`.github/agents/security-offline.agent.md`, read first)
- **PR:** #41 `m13-sec1-html-escaping-remediation-2026-11-17` → `m13-system-wide-depth-audit-2026-10-09` (Draft, OPEN)
- **Exact SHA reviewed:** `fcb365c9f5b28eff11c36fe0ebb18ab756cd6370` (confirmed equal to `headRefOid` via `gh pr view 41`)
- **Base:** `92d76761bdc6e6d1bdbcfd74608652ae555b4fd3` (merge-base; PR commits `d64fb78`, `fcb365c`)
- **Prior report consulted (not relied on):** `reports/agent-work/security-offline/phase-0-offline-and-workflow-review.md` (PR #37 branch), SEC-1 at lines 41–47, 95.
- **Review type:** report only. PR #41, `main`, canonical records, workflows were not modified. No fixes implemented. No Phase 1 work.

## Verdict: **ACCEPT**

The fix correctly escapes every record-controlled value reaching `index.html`, canonical outputs are byte-identical to base, and only two files changed. Remaining items are non-blocking hardening recommendations; none is a required remediation.

## 1. Scope of change (VERIFIED)

`git diff --name-only 92d76761 fcb365c9…`:
- `REFERENCE/src/encyclopedia_reference/offline_edition.py` (+23/−2)
- `REFERENCE/tests/test_offline_edition.py` (+25)

No canonical records, workflows, governance files, schemas or other files touched.

## 2. Escaping by sink (VERIFIED by source read at SHA and by differential execution)

All HTML is generated in one place; `git grep` for `.html|<article|<pre|<h1` in `REFERENCE/src` finds only `offline_edition.py`.

| Value | Location (at SHA) | Context | Treatment | Correct? |
|---|---|---|---|---|
| `record_id` | `offline_edition.py:26,34` | element text (`<h2>`) | `html.escape(str(...), quote=True)` | Yes |
| `record_type` | `:27,35` | element text (`<p>`) | same | Yes |
| `record_version` | `:28,35` | element text (`<p>`) | same | Yes |
| serialized `content` | `:29-32,36` | element text in `<pre>` | `json.dumps(..., ensure_ascii=False, indent=2, sort_keys=True)` then `html.escape` | Yes (escape applied after serialization; keys and values both covered) |
| `edition_id` | `:38,45` | element text (`<p>`) | same | Yes |

Notes:
- All sinks are text-node context; no attribute, URL, script, or style context receives record data. `quote=True` is harmless over-escaping (defensible if an attribute sink is added later).
- `str()` coercion avoids a `TypeError` on non-string values and still escapes.
- Static template parts (title, `<style>`, `<h1>`) contain no record data.

**Independent differential run** (hostile record: `a<script>x</script>` id, `1"&<img src=x onerror=alert(1)>` version, `claim'><svg onload=1>` type, content containing `</pre><script>`, `<!-- -->`, U+2028, U+202E (bidi override), backticks, `javascript:`, key `k<b>`, `</style></title>`; edition_id `ed'"><script>1</script>`), tokenized with stdlib `html.parser`:
- **Base 92d76761:** start tags include `script`, `img`, `svg`; `on*` attributes present (`onload`, `onerror`) → vulnerable (reproduces SEC-1).
- **PR head:** tags only `article,b,h1,h2,meta,p,pre,style,title`; zero `on*` attributes → no injection, including cases absent from the PR's test (SVG, comment, `</style>`/`</title>` breakouts, key position, bidi/LS characters).

## 3. Regression-test assessment

`REFERENCE/tests/test_offline_edition.py:45-67` (`test_offline_html_escapes_record_controlled_content`). Verified it **fails on base** (test file copied onto base worktree → `1 failed`) and passes on head → a genuine regression test.

| Required case | Covered? | Where |
|---|---|---|
| script injection | Yes | id, type, content, edition_id payloads; `"<script>" not in html` |
| closing-tag breakout (`</pre>`) | Yes | content; `"</pre><script" not in html`, `&lt;/pre&gt;` |
| image/event-handler | Yes | version `<img src=x onerror=…>`; `"<img src=x" not in html`, `&lt;img` |
| quotes | Partly | `&quot;` asserted only via content; double quote in type/edition_id exercised but not asserted; apostrophe `&#x27;` not asserted |
| ampersand | Yes | `Жизнь &amp; знание`; `1&<img` in version |
| Unicode | Yes | Cyrillic/CJK/em dash preserved unescaped |

Weaknesses / missing cases (non-blocking, **Low**):
1. **Substring assertions, not structural.** `"<script>" not in html` would miss `<script src=…>` or `<SCRIPT>`; a parser-based assertion (no `script/img/svg` start tags, no `on*` attributes) is stronger and stdlib-only.
2. No assertion for `</style>`/`</title>` breakouts, `<!--`, SVG/`<iframe>`/`javascript:` links, bidi/line-separator characters (verified manually above; not in the suite).
3. No test that `records.json`/`records.jsonl`/SQLite remain unescaped (verified manually in §5).
4. Hostile `content` keys and non-string `record_version` not exercised.
5. Test targets only `index.html`; see F-2 (README.md).

## 4. CSP assessment

**Necessary?** Not for this PR. Escaping is the primary control and is correct in all (text-only) contexts. CSP is **defense-in-depth** against a future regression (e.g. a new attribute/URL sink) and is cheap here because the document is static and needs no scripts, images, fonts, or network.

**Minimal appropriate policy (if adopted)**, via `<meta http-equiv="Content-Security-Policy">` placed first, before the `<style>`:

```
default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'
```

- `default-src 'none'` blocks script, img, font, connect, frame, object, media — none used, so offline behaviour is unchanged and injected loads are refused.
- `style-src 'unsafe-inline'` is **required** because the existing `<style>` is inline (`offline_edition.py:41-43`). Trade-off: injected inline styles would be permitted (low impact: no secrets, no network). Stricter alternative: `style-src 'sha256-<hash>'` of the constant style text — viable but brittle (any CSS edit changes the hash); not recommended as a first step.
- `base-uri` and `form-action` do not fall back to `default-src`, hence listed explicitly; harmless with no `<base>`/forms.
- `file://`: browsers honour meta CSP for local files; no server or headers needed. Offline: policy only restricts loads; nothing is loaded. Print CSS is inline, unaffected.
- Limits: meta CSP cannot express `frame-ancestors`, `report-uri`, `sandbox`; applies only to content after the meta element; does not protect `records.json` etc. when opened directly. Adding it changes `index.html` bytes and thus the SHA-256 in `edition-manifest.json` (expected, deterministic).
- **Not verified:** page not loaded in a browser; CSP enforcement is analysis, not an observed result.

Recommendation: optional follow-up in a separate small PR with its own test (policy present, precedes `<style>`). Not required to accept #41.

## 5. Canonical outputs unchanged (VERIFIED)

Built the same hostile fixture with base and PR head:
- `records.json`: byte-identical (`cmp`), sha256 prefix `4f09187a10dc47a2` both.
- `records.jsonl`: byte-identical, `4bc886a7dd3f04c2` both.
- `records.sqlite3`: all rows equal (`SELECT * FROM records`); file hash `6d647a98a01acbff` both.
- `README.md`: identical hash.
- Only `index.html` differs (expected) and consequently `edition-manifest.json` (per-file hash of `index.html`). The diff does not touch `_canonical()` or the JSON/JSONL/SQLite writers.

## 6. Findings

| ID | Severity | Status | Finding |
|---|---|---|---|
| F-1 | — | Resolved | SEC-1 (stored HTML/script injection in `index.html`) remediated for all five required fields; reproduced on base, absent on head. |
| F-2 | Low | Confirmed by source read (not exploit-tested) | `offline_edition.py:22` writes raw `edition_id` into `README.md` (Markdown). Not HTML produced by the tool, but Markdown viewers that render inline HTML could act on it. `edition_id` is an operator-supplied build parameter, not record content; outside the PR's stated scope. |
| F-3 | Low | Gap | Test weaknesses in §3. |
| F-4 | Info | Recommendation | Optional meta CSP (§4). |

No Critical/High/Medium findings.

## 7. Commands executed and results

Run on detached worktrees of the exact SHAs (`/tmp/w41` = `fcb365c9…`, `/tmp/w92` = `92d76761…`), Python 3.12.3, pytest 9.2.0, in a venv.

```
git fetch origin m13-sec1-html-escaping-remediation-2026-11-17
git cat-file -t fcb365c9f5b28eff11c36fe0ebb18ab756cd6370        # commit
gh pr view 41 --json headRefOid,baseRefName,state,isDraft        # head == SHA, Draft, OPEN
git diff --stat 92d76761 fcb365c9…                               # 2 files
PYTHONPATH=src pytest tests/test_offline_edition.py -v           # head: 3 passed
PYTHONPATH=src pytest tests/test_offline_edition.py -q           # base: 2 passed (no new test)
pytest -q <new test copied to base> -k escapes                   # base: 1 failed (as intended)
pip install -e "REFERENCE[test]"
python -m pytest -q REFERENCE/tests                              # head: 1041 passed in 311.93s
differential build script (base vs head) + cmp + sqlite row comparison
gh pr checks 41; gh api repos/…/commits/fcb365c9…/check-runs
```

A first `pytest tests` run before installing `REFERENCE[test]` failed collection (`jsonschema` missing) — environment issue, resolved by the install, not a code defect.

CI on the exact head SHA (check-runs API): `release-gate` success, `test-reference` success, `build-and-test` ×2 success, `copilot-pull-request-reviewer` success. Reported from the API; job logs not inspected.

## 8. Remaining risks / not verified

- No browser rendering; XSS checked via HTML tokenization only. CSP not browser-tested.
- Real-corpus offline build not diffed base-vs-head (synthetic fixture only; full 1041-test suite and CI passed).
- Markdown/README sink (F-2) and any future non-text sink are not covered by this fix.
- Repo-level GitHub settings and workflow content out of scope.

## 9. Required remediation

None.

## 10. Optional follow-ups (separate PRs; owner approval needed)

1. Strengthen the regression test: parser-based assertions (no `script/img/svg/iframe` start tags, no `on*` attributes); add `</style>`, `<!--`, apostrophe, hostile key, non-str version, and a canonical-outputs-unescaped assertion.
2. Decide whether `README.md` `edition_id` should be sanitised or its charset validated.
3. Optionally add the meta CSP in §4 with a test.
