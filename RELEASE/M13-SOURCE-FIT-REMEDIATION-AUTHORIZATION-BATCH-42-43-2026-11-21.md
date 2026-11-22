# M13 — Proposed bounded source-fit remediation authorization, Batch 42–43

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Proposal status: **APPROVED — ACTIVE UNDER EDITORIAL-CORRECTION REGISTRY**
Approval: explicit project-owner approval received 2026-11-22.  
Authorization base PR #21 head: `d3f80ddcc249aaef949b51255dfb1e0ce3b20a7a`.

## 1. Purpose and boundary

This proposal converts the directly verified source-fit findings into a finite authorization boundary. The project owner approved it on 2026-11-22 and it is active as registry finding `M13-SOURCE-FIT-REMEDIATION-001` in `RELEASE/EDITORIAL-CORRECTION.json`.

The intended work is evidence-graph remediation only: add claim-specific direct Source/Evidence Use edges where the existing edge is materially mismatched or incomplete; improve two existing WHO Evidence Use locators where the Source itself is already correct. No Claim statement is to be rewritten.

## 2. Exact target set

### A. New direct Source + Evidence Use edges

For each row below, preserve all existing records and links and add one distinct Evidence Use edge to the existing Claim@1. Add a new Source record when the source is new to this package; rows 018 and 030 share the single January 23, 2026 CPSC Source record because they cite the same document. Do not repoint, overwrite, delete, or collapse any historical Source/EU edge.

| Batch / row | Existing Claim | New direct source | Required locator and support boundary |
|---|---|---|---|
| 42 / 018 | `CLM-GENERATOR-REFUEL-COOL@1` | CPSC, *Keep Warm and Safe This Winter: Tips for Using Generators, Furnaces and Space Heaters* (2026-01-23); https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters | “Generators” section; supports stopping the generator and allowing it to cool before refuelling. Do not generalize to unrelated generator maintenance. |
| 42 / 021 | `CLM-HOME-FIRE-ESCAPE-PLAN@1` | USFA, *Home Fire Escape Plans*; https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/ | “Making and practicing your fire escape plan”; map the home, two ways out, unobstructed exits, outside meeting place and practice, limited to the page's stated guidance. |
| 42 / 022 | `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` | NFPA, *Escape Planning*; https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning | Exact paragraph(s) for two ways out and household escape planning. During implementation, inspect the live page and record a reproducible heading/paragraph locator; do not rely on search-result summaries alone. |
| 42 / 025 | `CLM_WASTEWATER_TREATMENT_BASICS_A@1` | EPA, *Primer for Municipal Wastewater Treatment Systems*; https://www.epa.gov/sites/production/files/2015-09/documents/primer.pdf | “Basic Wastewater Treatment Processes,” printed page 10, “Physical,” “Biological,” and “Chemical”; support only the described treatment-process categories and examples. |
| 42 / 030 | `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1` | CPSC, *Keep Warm and Safe This Winter…* (2026-01-23), same URL as row 018 | “Use Flashlights Instead of Candles”; battery-powered flashlights/lanterns during a power outage. Preserve the existing NFPA edge as a separate evidence role. |
| 42 / 068 | `CLM-EPIDEMIOLOGY_BASICS-D@1` | WHO, *Basic Epidemiology*, 2nd edition, Chapter 1, Box 1.2; https://iris.who.int/bitstream/handle/10665/43541/9241547073_eng.pdf | “Definition of epidemiology,” Box 1.2. Verify the PDF page/box in the implementation environment; if inaccessible, use the WHO-hosted glossary PDF already identified in the adjudication report and record its exact glossary entry. Do not use the participatory-surveillance news page as the definition source. |
| 43 / 081 | `CLM-FOOD-TARGET-TEMP@1` | FDA, *Food and Water Safety During Power Outages and Floods*; https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods | “Prepare Yourself Before Power Emergencies”; freezer at or below 0°F and refrigerator at or below 40°F. Do not attribute the 0°F threshold to the existing FDA “Key Tips” page. Keep outage-duration advice distinct from steady-state target temperatures. |

Proposed record IDs below are provisional until preflight proves uniqueness and conformity with the repository's naming conventions:

- Row 018: `SRC-CPSC-WINTER-SAFETY-2026` + `EU-GENERATOR-REFUEL-COOL-CPSC-2026`
- Row 021: `SRC-USFA-HOME-FIRE-ESCAPE-PLANS-2026` + `EU-HOME-FIRE-ESCAPE-PLAN-USFA-DIRECT-2026`
- Row 022: `SRC-NFPA-ESCAPE-PLANNING-2026` + `EU-HOME-FIRE-TWO-WAYS-NFPA-ESCAPE-2026`
- Row 025: `SRC-EPA-WASTEWATER-PRIMER-2015` + `EU-WASTEWATER-TREATMENT-BASICS-A-EPA-PRIMER`
- Row 030: (reuse `SRC-CPSC-WINTER-SAFETY-2026@1` from the generator slice) + `EU-LIGHTING-FLASHLIGHT-OUTAGE-CPSC-2026`
- Row 068: `SRC-WHO-BASIC-EPIDEMIOLOGY-2E` + `EU-EPIDEMIOLOGY_BASICS-D-WHO-BASIC-EPIDEMIOLOGY`
- Row 081: `SRC-FDA-POWER-OUTAGE-FLOODS-2026` + `EU-FOOD-TARGET-TEMP-FDA-FREEZER-0F`

### B. Existing Evidence Use pinpoint improvements only

1. Batch 43 row 012: version `EU_WATER_QUALITY_WHO_A` from @1 to @2, retaining the current correct `SRC_WATER_QUALITY_WHO@1` and `CLM_WATER_QUALITY_WHO_A@1`. Add the exact WHO “Drinking-water quality guidelines” locator and bounded description. Do not change the Source URI or version: the reported bad URL was a stale/transcribed report URL, not a demonstrated canonical Source mutation.
2. Batch 42 row 059: version `EU_CLINICAL_TRIALS_BASICS_A` from @1 to @2, retaining `SRC_CLINICAL_TRIALS_BASICS@1` and `CLM_CLINICAL_TRIALS_BASICS_A@1`. Add the exact WHO “Overview” locator and keep the description limited to the core clinical-trial definition.

No Claim, Source, Context, Scope, Relation, Assessment, risk record or other canonical record is authorized for modification in these two items.

## 3. Permitted supporting files

Following explicit approval, as registered in `RELEASE/EDITORIAL-CORRECTION.json`:

1. Add the 6 unique new Source JSON records and 7 new Evidence Use JSON records listed in §2A, in their existing target vertical-slice `records/` directories.
2. Version only the 2 Evidence Use records listed in §2B.
3. Update only the README files of the eight target slices: `generator-carbon-monoxide-safety`, `home-fire-smoke-safety`, `wastewater-treatment-basics`, `emergency-lighting-safety`, `epidemiology-basics`, `power-outage-food`, `water-quality-basics`, and `clinical-trials-basics`.
4. Update only the dedicated existing regression test(s) for those eight slices. No test framework, shared schema, validator, or unrelated test file changes.
5. Update `RELEASE/CONTENT-COVERAGE.json` only for the actual net increase of 13 new records (6 Sources + 7 Evidence Use records); verify all totals from the repository's counting tool rather than hand-editing an assumed total.
6. Register this authorization in `RELEASE/EDITORIAL-CORRECTION.json` with this exact file path and scope.
7. Update only the relevant M13 checkpoint and the Batch 42–43 source-fit adjudication report to record completed work, test evidence, exact commit SHA and remaining gates.

The exact README and regression paths must be resolved from the current branch during preflight before any write. If the repository contains no dedicated test for one target slice, stop and request a scope amendment rather than creating a broad/shared test outside this authorization.

## 4. Explicit exclusions

This proposal does **not** authorize:

- any Claim wording, ID, version, type, status or provenance change;
- overwriting or repointing existing Source records, including `SRC-CPSC-GENERATOR-2026@1`, `SRC-USFA-HOME-FIRE-2026@1`, `SRC-NFPA-HOME-FIRE-2026@1`, `SRC_WASTEWATER_TREATMENT_BASICS@1`, `SRC-NFPA-CANDLE-SAFETY-2026@1`, `SRC-WHO-EPIDEMIOLOGY-2024@1`, or `SRC-FDA-POWER-OUTAGE-2026@1`;
- deletion, deduplication, renaming, or replacement of any record;
- changes to any other Evidence Use, Source, Context, Scope, Relation, Assessment, risk metadata, rights metadata or publication status;
- any D/E/B assignment, acceptance or import of historical scores;
- clearing HOLD, Human View, specialist review, rights review, source-independence review, or public-release approval;
- changes to `main`, merging PR #21, changing branch protection, or expanding the target set.

## 5. Mandatory preflight before the first canonical write

The following preflight and acceptance controls govern the implementation. Record-level links, paths and ID collisions were inspected; the automated full content preflight and exact-head CI remain pending:

1. Exact-head and branch check: PR #21 remains Draft/unmerged; `main` remains unchanged; branch head is a documented successor containing only permitted work.
2. Record-ID collision check for all proposed IDs and exact path/slice resolution for all targets.
3. Schema/versioning preflight for all 15 new/versioned records (6 Sources + 7 new EUs + 2 existing EUs @2).
4. Provenance/link integrity: every new EU points to the intended Claim@1 and new Source@1; each EU's `provenance.created_from` agrees with its Source; row 012 and row 059 @2 preserve exact Claim/Source refs.
5. Source identity, exact locator, access and rights metadata review; especially live NFPA page extraction and WHO PDF page/box verification.
6. Slice README/test path inventory and coverage-count baseline.
7. **Process deviation:** the automated dry-run content preflight was not executed before the first canonical JSON writes. This deviation is recorded and must be addressed by full post-write preflight and exact-head CI before any acceptance. If any check fails, stop and repair only within this authorization.

## 6. Required regression and exact-head CI

For every target slice, dedicated tests must assert:
- record identity, record type, version and schema validity;
- exact Claim@1 / Source@1 / Evidence Use@1 or @2 cross-links;
- the exact source URL and required section/page/box locator;
- claim-specific scope limitations;
- preservation of the prior historical Source/EU records and all multi-source edges;
- no Claim statement/provenance changes and no unrelated record-count drift.

Then run, on one exact final PR head:

- content preflight and full schema/semantic validation;
- all eight dedicated slice regressions;
- full Reference implementation tests;
- Release Conformance Gate;
- Offline Edition build and tests;
- repository coverage/integrity checks, including the updated 13-record net delta.

All required checks must complete successfully on the exact final SHA. Recheck PR #21 metadata, base/main SHA and changed-file list after CI. A green check on an earlier SHA is not sufficient.

## 7. Acceptance boundary

Even if all technical checks pass, the result is only a source/evidence remediation increment. Current accepted D/E/B assessments from this work remain **0**. No Claim is cleared for publication by this authorization. M13 remains OPEN until the independent Human View, specialist, rights, evidence diversity, cross-slice, risk and release gates are separately completed.

## 8. Execution record

- Owner approval: 2026-11-22.
- Registry activation commit: `b04c2ff0c270a4620456d3fe5a39e006f08909f3`.
- README and dedicated regression commit: `1852b1d834f1509deef629624f026d031fe3e8e8`.
- Canonical evidence and coverage commit: `b7717f2a277b1a52c937b9d89047a748721d79e4`.
- Implemented: 6 unique Source records, 7 new Evidence Use records, and 2 existing Evidence Use records versioned to @2; net corpus delta +13.
- One CPSC Source is shared by generator row 018 and emergency-lighting row 030 to avoid duplicate URI records.
- The NFPA page returned no readable text in the direct page fetch; its exact page/section locator is recorded, but passage-level extraction remains a limitation and is not a release clearance.
- WHO *Basic Epidemiology* PDF is an official WHO IRIS resource with the Box 1.2 text indexed, but direct page retrieval timed out; rights/redistribution review remains separate.
- Automated content preflight, full CI, independent final diff/tree review and exact final SHA acceptance remain pending.

This active authorization is limited to the exact changes and exclusions above.

