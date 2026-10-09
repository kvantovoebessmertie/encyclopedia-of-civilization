# M11 Controlled Correction Authorization — 2026-10-09

## Authorization basis

This authorization is based on the revalidated read-only findings in `M11-INITIAL-GAP-AUDIT-2026-10-09.md`. It authorizes only the exact paths below on branch `m11-gap-map-after-m10-human-view-2026-10-09`. The three slices are pre-existing content; this is a bounded maturation pass, not slice creation.

## Confirmed findings

- Accessibility: `M11-ACC-001` README/Human View; `M11-ACC-002` generic Evidence Use; `M11-ACC-003` international framework versus local technical criteria; `M11-ACC-004` regression gap.
- Ergonomics: `M11-ERG-001` README/Human View; `M11-ERG-002` generic Evidence Use; `M11-ERG-003` Claim C exceeds the directly described NIOSH overview; `M11-ERG-004` regression gap.
- Human factors: `M11-HF-001` README/Human View; `M11-HF-002` generic Evidence Use; `M11-HF-003` regression gap.
- Limitation `M11-HF-LIMIT-004`: the exact canonical NASA locator could not be independently retrieved. This is not a confirmed broken URL. Preserve the source identity/URL; if source fit cannot be established during post-correction review, stop and request a separate scope amendment.

## Exact authorized file list

1. `CONTENT/vertical-slices/accessibility-basics/README.md`
2. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-A.json`
3. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-B.json`
4. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-C.json`
5. `REFERENCE/tests/test_content_accessibility_basics_vertical_slice.py`
6. `CONTENT/vertical-slices/ergonomics-basics/README.md`
7. `CONTENT/vertical-slices/ergonomics-basics/records/CLM-ERGONOMICS_BASICS-C.json`
8. `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-A.json`
9. `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-B.json`
10. `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-C.json`
11. `REFERENCE/tests/test_content_ergonomics_basics_vertical_slice.py`
12. `CONTENT/vertical-slices/human-factors-basics/README.md`
13. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-A.json`
14. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-B.json`
15. `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-C.json`
16. `REFERENCE/tests/test_content_human_factors_basics_vertical_slice.py`
17. `RELEASE/EDITORIAL-CORRECTION.json` — add only the M11 authorization entry.
18. M11 authorization, debt-map and post-correction audit records required to record the change and verification.

## Required correction behaviors

- Give each README a concise Russian-facing explanation of the subject, a bounded illustrative example where appropriate, and clear applicability limits. Do not present educational material as certification, local legal advice, individualized medical advice, or a complete workplace/site risk assessment.
- Rewrite each of the nine existing Evidence Use descriptions so it identifies the specific contribution to its linked Claim and the limits of that support. Preserve IDs, provenance, refs and `supports` roles.
- Narrow only `CLM-ERGONOMICS_BASICS-C` to the NIOSH overview's directly described process: identifying, analyzing and controlling workplace risk factors. Do not add an evaluation protocol to that claim based only on the recorded overview.
- Preserve the current wording of all three accessibility Claims and all three human-factors Claims in this pass. If source fit remains uncertain, do not invent support or expand the Claim.
- Add regression assertions for the confirmed content and boundary requirements while retaining every existing shape, count, provenance and linkage assertion.

## Explicit exclusions and invariants

- No new or deleted Records, Sources, Evidence Use records, Context, Scope, Relations, record types or slices.
- No edits to any Source record, canonical source identity/URL, provenance method, record ID, Claim/Evidence Use reference, evidence role, Context/Scope target ref or Relation participant.
- No Relation changes; preserve `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` exactly. Permitted Relation delta is zero.
- No changes to other slices, global architecture, release-gate logic, `main`, protected M10 branch, or accepted historical checkpoints.
- No source-count quota. Do not add a source merely to make the source count larger.
- Do not weaken existing tests or release gates.

## Stop condition

The NASA locator issue remains a limitation, not a confirmed source failure. If the exact recorded source or an authoritative redirect cannot substantiate a revised human-factors Evidence Use description, stop the affected correction and request a documented scope amendment. Do not silently replace the source or claim external verification that did not occur.

## Acceptance gates

After correction: re-read all changed records; verify unchanged slice shapes, coverage, source identity/URLs, provenance/linkage, Context/Scope and Relation tree; run all three targeted regressions; run Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD; independently verify exact diff, PR base/head/state and unchanged `main`. Any commit after final CI requires a fresh exact-head 3/3 run.

**Status: AUTHORIZED FOR THE EXACT FILE LIST ABOVE; NOT CLEAN.** This authorization does not authorize merging or promotion.
