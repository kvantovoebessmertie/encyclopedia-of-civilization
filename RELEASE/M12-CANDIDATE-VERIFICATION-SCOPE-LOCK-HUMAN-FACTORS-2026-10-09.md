# M12 Candidate Verification and Scope Lock — Human Factors — 2026-10-09

## Locked baseline

- Base branch: `m11-gap-map-after-m10-human-view-2026-10-09`
- Base SHA: `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`
- Working branch: `m12-human-factors-source-and-human-view-2026-10-09`
- Candidate: existing `human-factors-basics` slice (9 existing Records)
- Verified source candidate: NASA Johnson Space Center, Human Factors & Performance — https://www.nasa.gov/reference/jsc-human-factors-performance/

## Exact authorized content surface

1. `CONTENT/vertical-slices/human-factors-basics/README.md`
2. `CONTENT/vertical-slices/human-factors-basics/records/SRC-HUMAN_FACTORS_BASICS.json`
3. `CONTENT/vertical-slices/human-factors-basics/records/CLM-HUMAN_FACTORS_BASICS-A.json`
4. `CONTENT/vertical-slices/human-factors-basics/records/CLM-HUMAN_FACTORS_BASICS-B.json`
5. `CONTENT/vertical-slices/human-factors-basics/records/CLM-HUMAN_FACTORS_BASICS-C.json`
6. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-A.json`
7. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-B.json`
8. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-C.json`
9. `REFERENCE/tests/test_content_human_factors_basics_vertical_slice.py`
10. `RELEASE/EDITORIAL-CORRECTION.json` — append the M12 authorization/audit entry only.
11. `RELEASE/M12-INITIAL-GAP-AUDIT-HUMAN-FACTORS-2026-10-09.md`
12. This scope-lock document.
13. `RELEASE/M12-CORRECTION-AUTHORIZATION-HUMAN-FACTORS-2026-10-09.md`
14. `RELEASE/M12-POST-CORRECTION-AUDIT-HUMAN-FACTORS-2026-10-09.md`
15. `RELEASE/M12-UNIFIED-DEBT-MAP-2026-10-09.md`

No other paths are authorized. If review identifies a necessary additional path, stop and amend this lock before editing it.

## Correction requirements

- Preserve the Source record ID and source identity as NASA Johnson Space Center Human Factors & Performance; change only its locator to the independently retrieved official NASA URL above, and document the old locator as unverified rather than asserting it is broken.
- Narrow Claims A–C to content directly supported by the selected NASA page. Do not claim that one source establishes universal human-factors principles across all domains.
- Rewrite each Evidence Use description to name the specific source contribution for its linked Claim and explain relevant boundaries.
- Rewrite README in Russian for an ordinary reader: definition, a clearly illustrative example, links to Claims/Evidence Use/Source, practical relevance, and explicit limits (educational overview; not a design certification, comprehensive risk assessment, or substitute for domain expertise).
- Extend the dedicated regression to assert slice structure/linkage, Source locator, reader-facing README, unique claim-specific Evidence Use descriptions, claim wording, and limitations.
- Maintain the existing nine-record slice and all 19 registered Record types. No new or deleted Records.
- Do not change Context, Scope, Relations, other slices, architecture, record IDs, record types, Claim/Evidence Use linkage IDs, evidence roles, or provenance method except the Source URL and wording specifically authorized above.
- Do not claim multi-source independence: this bounded correction uses one official NASA page. If any Claim cannot be supported by that page, narrow or remove that Claim only within its existing record; do not fabricate support.

## Acceptance

M12 is not CLEAN until all authorized findings are resolved, the exact diff and tree invariants are independently checked, the targeted regression passes, Reference implementation tests, Release Conformance Gate and Offline Edition all pass on the same exact final HEAD, and PR/base/main state is verified. Keep PR open/draft/unmerged; do not modify `main`.
