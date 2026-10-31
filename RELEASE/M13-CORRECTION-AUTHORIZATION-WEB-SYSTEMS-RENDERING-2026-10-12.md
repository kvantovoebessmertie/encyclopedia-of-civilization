# M13 Correction Authorization — Web Systems Browser Rendering Evidence — 2026-10-12

Authorization ID: `M13-WEB-SYSTEMS-RENDERING-002`

Status: **bounded editorial authorization; no publication approval**

## Finding

Passage-level review found that `SRC-WEB_SYSTEMS_BASICS@1` (MDN “How the Web Works”) explicitly says that actual browser rendering is covered separately in “How browsers load websites”. Existing Claim `CLM-WEB_SYSTEMS_BASICS-A@1` combines client/server resource delivery with browser processing/rendering. The existing Source supports the first clause but is not sufficient by itself for the rendering clause.

## Authorized scope

Only in `web-systems-basics`:

1. Add one Source record `SRC-MDN-HOW-BROWSERS-LOAD-WEBSITES` @1 with the official MDN URL `https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_browsers_load_websites`.
2. Add one Evidence Use record `EU-WEB_SYSTEMS_BASICS-A-RENDERING` @1 pointing to `CLM-WEB_SYSTEMS_BASICS-A@1` and the new Source @1. Its material must pinpoint “Web page rendering”, “Handling HTML”, and “Parsing CSS and rendering the page”, describe the high-level rendering process, and preserve MDN's caveat that this is a simplified explanation and browser behavior can differ.
3. Update the dedicated regression test, slice README, and `RELEASE/CONTENT-COVERAGE.json` counts only as required by those two new records.

No Claim wording, existing Source/Evidence Use IDs or versions, other records, Relations, other slices, or publication state may change. The new Source is additional evidence, not a claim that the current Source is independent of it; both are MDN educational materials and must not be counted as independent corroboration without further lineage review.

## Validation and boundaries

- Validate exact Claim/Source refs, versions, section markers, and the scope limitation in regression tests.
- Update corpus counts from actual records; do not adjust unrelated counts.
- Require exact-head content preflight, Reference tests, Release Conformance Gate, and Offline Edition.
- Keep M13 open and PR #21 Draft/unmerged. No public-reader allowlist entry, deployment, or publication approval is authorized.
