# M13 + MVP — continuation checkpoint

Date: 2026-11-14  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Active M13 branch: `m13-system-wide-depth-audit-2026-10-09`  
Latest verified M13 branch HEAD before this checkpoint update: `37d887629506fcb6360231586c6d3e78637b2048`

## 1. Exact latest work

### M13 — unassessed risk content screen

- Package 07: `RELEASE/M13-UNASSESSED-RISK-CONTENT-SCREEN-PACKAGE-07-2026-11-14.md`
  - Commit: `2468282141f20a53bc17852782fa99a840df4f59`
  - 20 additional Claim statements routed by content.
  - No canonical Claim/EU/Source JSON, risk metadata or D/E/B values changed.
  - Package's historical coverage statement (216 prior exact IDs) must continue to be treated as provisional until the complete exact-ID ledger, including the 14 unnamed preliminary observations, is reconstructed.

### M13 — strict passage/locator gap queue

- Baseline: 47 exact Claim/EU/Source triples in `M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`.
- Package 07 touched 6 of those 47 candidates (behavioral economics B/C, biodiversity A/B, calibration B/C). Biodiversity C was screened in Package 07 but is not one of the 47 rows.
- Package 01: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-01-2026-11-14.md`
  - Commit: `13bead3e1810b102233af67b9cf59d8eb890ea17`
  - Reviews 7 additional exact triples: emergency management B/C, shelter A/B/C, water security B, hydropower A.
  - Risk routes: 2 high-consequence, 1 elevated, 3 moderate, 1 low-direct-consequence.
  - Exact Claim/EU/Source references resolve for all 7; all 7 EUs remain generic/non-pinpoint.
  - Canonical passage locators added: 0. Canonical JSON changed: 0. D/E/B or risk metadata changed: 0.
  - Main finding: Shelter B has a material ventilation ambiguity; hazard-specific shelter advice must not be generalized. Keep B/C HOLD and require qualified emergency-management review.
  - Other key findings: emergency-management source fit is partial; Ready.gov root page is not a passage locator; UN-Water definition and DOE hydropower statement are directly supportive at desk level but still need canonical pinpoints.

- Package 02: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-02-2026-11-14.md`\n  - Commit: `37d887629506fcb6360231586c6d3e78637b2048`\n  - Reviews 6 additional exact triples: digital communications A/B/C, electronics B/C, calibration A.\n  - Findings: ITU-T B is directly supported by the series catalogue; A/C are partial. NIST's Semiconductors page directly supports Electronics B, while Electronics C remains partial. Calibration A is directly defined by JCGM VIM 2.39, but the canonical NIST Source/EU does not carry that locator and the Claim is a simplified version of the full definition.\n  - Risk routes: 1 elevated, 3 moderate, 2 low-direct-consequence.\n  - Canonical records changed: 0; locators added: 0; scores/risk metadata changed: 0.\n\nAcross Packages 07, 01 and 02, 19 of the 47 strict-queue rows have been touched (6 + 7 + 6); 28 remain, subject to exact-ID reconciliation. Do not count the 20-Claim risk screen Package 07 as 20 strict-queue rows.

## 2. Reconciliation blocker — do not paper over

- The source unassessed-risk screening CSV contains 711 rows at source revision `f26820e59b08b4036ad78302dad8118c51dac540`.
- The preliminary 17-Claim screen names only 3 IDs; 14 other inspected Claims are not enumerated.
- The 14 unnamed observations remain unresolved. Do not add reported counts as if they were unique Claim IDs.
- The 14 November coverage reconciliation records 45 unique explicit IDs in the first four reports and 35 more in Packages 05/06, while historical unnamed observations remain unresolved.
- Package 07's stated 216 prior exact IDs is provisional pending reconstruction of the complete underlying list. Do not calculate a cumulative unique percentage from it without an exact deduplicated ledger.
- The current queue CSV still shows UNASSESSED risk metadata for all 711 rows; a desk screen does not itself update canonical risk metadata.

## 3. Latest CI and protected-state status

- Latest M13 commit `13bead3e1810b102233af67b9cf59d8eb890ea17` is the exact branch HEAD.
- Its Reference implementation tests were pending, Offline Edition was in progress, and Release Conformance Gate was queued at the last check. Re-fetch these exact-head workflow runs before reporting success.
- M13 PR #21 remains open, Draft, unmerged; base is the M12 human-factors branch. Do not merge or change `main` without the established gates and explicit release decision.
- Neither package commit modifies canonical content records.

## 4. MVP — current verified state

All implementation PRs remain open, Draft and unmerged:
- PR #22 — public MVP / publication gates and professional contribution workflow.
- PR #24 — offline HTML escaping.
- PR #25 — allowlisted read-only reader and private SI-units preview.
- PR #26 — professional contribution intake schema/contract.
- PR #27 — local professional contribution form with JSON export.

Latest exact-head GitHub Actions results checked:
- PR #22: Offline Edition, Reference implementation tests, Release Conformance Gate — all SUCCESS.
- PR #24: same three checks — all SUCCESS.
- PR #25: Offline Edition, private SI preview, Release Conformance Gate, Reference implementation tests — all SUCCESS.
- PR #26: Reference implementation tests, Offline Edition, Release Conformance Gate — all SUCCESS.
- PR #27: Reference implementation tests, Offline Edition, browser form tests, Release Conformance Gate — all SUCCESS.

PR #27 browser inspection validates six downloaded JSON payloads against the v1 JSON Schema and exercises conditional requirements, source/relation editors, duplicate IDs, reset, keyboard focus, mobile overflow, no external requests and no browser errors.

**MVP remains NO-GO for a real-record public pilot.** The reader is technically demonstrated with synthetic fixtures and a private SI preview; no public release allowlist is approved. The independent three-reader comprehension test for the SI candidate Claims has not been run. Rights/editorial approval, public operations, privacy, correction/takedown and deployment ownership remain open. The contribution form is local JSON export only, not a public intake endpoint.

## 5. Next execution order

1. Recheck the exact-head CI runs for M13 commit `13bead3e1810b102233af67b9cf59d8eb890ea17`.
2. Continue the strict 47-item passage/locator queue in content-driven packages, prioritizing electronics, emergency communications, shelter, water security, hydropower and calibration; verify exact IDs and prior report coverage before each package.
3. Recover the 14 unnamed IDs from the preliminary screen via workflow artifacts, logs or commit history. Until recovered, keep cumulative risk-screen coverage explicitly unreconciled.
4. Build the exact deduplicated ledger for the 711 risk queue; only then report cumulative unique coverage and remaining count.
5. Prepare bounded, versioned correction proposals for the clear passage/locator defects. Do not edit canonical JSON without the required authorization, exact source passage, rights review and regression scope.
6. Continue MVP reader and intake quality review; do not merge PRs or publish. The independent three-reader test requires actual readers and must not be marked complete by automated browser tests.

## 6. Non-negotiable quality rules

- No score or risk label by filename alone.
- No treating institution relevance as direct passage support.
- No counting filename mentions as completed semantic review.
- No treating a green CI run as content, rights, specialist or publication approval.
- No canonical edits without a bounded authorization and exact-version regression checks.
- Keep PRs Draft/unmerged and `main` unchanged until all required gates pass.


## 7. Continuation update — strict passage/locator Package 03 (2026-11-14)

- Package: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-03-2026-11-14.md`
- Commit: `6f16a0b7a2d6d8340ba1193719453b1ecb10071e`
- Scope: 9 additional exact Claim/Evidence Use/Source triples from the 47-item queue:
  - Acoustics C;
  - Algebra A/B/C;
  - Anatomy A/B;
  - Archival Science A/B/C.
- All 9 Claim → EU → Source ID/version chains were checked and resolve.
- All 9 Evidence Use records remain generic/non-pinpoint.
- Desk review found direct or partial passage support for all 9, with important qualification:
  - WHO noise guidance supports source-specific environmental exposure metrics, but not every applicable legal framework and not occupational noise.
  - OpenStax College Algebra passages directly support Algebra A/B/C, but the source explicitly prohibits LLM/generative-AI ingestion without prior written permission; CC BY-NC-SA conditions also apply. Keep all three on rights HOLD.
  - The registered NIGMS page for Anatomy A/B could not be retrieved during this review. NCBI Bookshelf offers direct supplementary definitions, but is not the registered Source; do not silently substitute it.
  - SAA Archives 101 directly supports the core processing and provenance principles; the description/context Claim is only partially supported at its full wording.
- No canonical Claim/EU/Source JSON, D/E/B score, risk metadata or publication state changed.
- Dedicated strict-queue rows reviewed: **28/47** (prior 19 + this package 9); **19 remain** for dedicated review, subject to exact-ID reconciliation.
- New commit's combined status and workflow-run query returned no status entries at the time of this checkpoint update. Do not report CI success until checks are visible and pass.
- M13 PR #21 remains protected: do not merge or retarget main; verify its head SHA and draft state after the branch update.

## 8. Next execution order after Package 03

1. Continue the remaining 19 strict-queue triples; choose the next tranche by content/risk and source rights, not alphabetical convenience alone.
2. Recover the 14 unnamed preliminary risk-screen Claim IDs and reconstruct the exact deduplicated ledger for the 711-row queue.
3. Re-run the full-corpus strict generic-EU scan after the review corpus changes; filename signals are discovery aids, not semantic completion.
4. Keep OpenStax Algebra A/B/C on rights HOLD pending written permission or a rights-compatible replacement source.
5. Keep the NIGMS Anatomy source identity unresolved until the registered page is verified or a bounded Source/EU replacement proposal is authorized.
6. Continue MVP review in parallel; retain NO-GO for real-record public pilot until rights/editorial, independent reader testing, privacy/operations, correction/takedown and deployment ownership are closed.


## 9. Continuation update — strict passage/locator Package 04 (2026-11-14)

- Package: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-04-2026-11-14.md`
- Commit: `c165c99cb30d25be92bfc3260124ae282f482a31`
- Scope: Asset Management A/B/C — 3 exact Claim/EU/Source triples.
- All 3 Claim → EU → Source ID/version chains resolve; all 3 EUs are generic/non-pinpoint.
- Material source-identity defect found: the Source record names ISO 55000:2024 but stores URI `https://www.iso.org/standard/83054.html`, which is ISO 55001:2024. ISO 55000:2024 is `https://www.iso.org/standard/83053.html`. Do not silently replace; create a bounded, versioned Source correction proposal after authorization.
- The ISO website states that ISO material is copyright protected and, except for specifically licensed ISO Open Data, may not be used for AI/ML, including prompting or enabling AI tools to generate responses. Keep all three Claims on rights HOLD; no AI ingestion or AI-enabled generation from the standard is cleared.
- Direct/partial conceptual support was located for all three Claims, but this does not cure the source identity mismatch or rights restriction.
- No canonical records, source URIs, passage locators, D/E/B scores, risk metadata or publication states changed.
- Strict-queue dedicated review total: **31/47** (Package 03 baseline 28 + Package 04 3); **16 remain**, subject to exact-ID reconciliation.
- Exact commit status/workflow query returned no check entries at the time of review. Do not report CI success until GitHub checks become visible and pass.

## 10. Next execution order after Package 04

1. Continue the remaining 16 strict-queue triples; prioritize high-consequence and source-identity/rights defects.
2. Keep Asset Management A/B/C on HOLD until ISO identity and AI-use rights are resolved; do not substitute ISO 55000 and ISO 55001.
3. Recover the 14 unnamed preliminary risk-screen Claim IDs and reconstruct the exact deduplicated ledger for the 711-row queue.
4. Re-run the strict generic-EU full-corpus scan after the review corpus changes.
5. Keep MVP NO-GO for real-record public pilot until rights/editorial, independent reader testing, privacy/operations, correction/takedown and deployment ownership are closed.


## 11. Continuation update — strict passage/locator Package 05 and exact-ID ledger (2026-11-14)

- Package 05: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md`
  - Commit: `768f1753faded357ccfa311c02203cfd0fb57ff7`
  - Covers all 16 remaining rows from the corrected 47-row strict queue: Behavioral Biology A/B/C; Cell A/B/C; Civil Society A; History of Medicine A/B/C; Humanitarian Logistics C; Migration A; Scientific Publishing A/B/C; Urban Planning A.
  - All 16 Claim/EU/Source v1 chains resolve and match; all 16 EUs are generic/non-pinpoint.
  - Desk dispositions: 8 direct conceptual matches (some require a separate source-identity correction or pinpoint); 6 partial; 2 not established by the registered Source. All remain HOLD.
  - Six OpenStax Biology Claims (Behavioral Biology A/B/C and Cell A/B/C) remain on explicit rights HOLD: OpenStax prohibits LLM/generative-AI ingestion without prior written permission and applies CC BY-NC-SA restrictions.
  - Other important issues: the exact registered World Bank PDF was not fully retrievable; NLM MeSH is too narrow for two broader historiography Claims; WFP Logistics Cluster landing page is not an after-action evaluation passage; ICMJE does not support the general scientific-publication Claim A; UN-Habitat Urban Lingo is not the currently registered topic-page Source.
  - No canonical JSON, passage locator, D/E/B score, risk metadata, rights permission or publication state changed.

- Exact reconciliation ledger: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-EXACT-ID-LEDGER-2026-11-14.md`
  - Commit: `9073922b98f52505b464136a2acbf956d2b6abe6`
  - Machine check parsed 47 source-queue rows, found 47 unique Claim IDs, zero duplicate IDs, zero unassigned rows.
  - Package allocation: Package 07 strict-queue overlap 6; Package 01 = 7; Package 02 = 6; Package 03 = 9; Package 04 = 3; Package 05 = 16. Total 47/47.
  - Package 07 is a 20-Claim risk-screen report; only six IDs are members of the 47-row strict queue. Its other 14 IDs are intentionally excluded.
  - This closes the **dedicated desk-review routing pass** for this 47-row queue only. It does not close M13, clear any HOLD, certify source support, resolve rights, or complete D/E/B scoring.

- Package 05 and ledger exact-head combined status/workflow queries returned empty arrays at the time checked. This is **not** evidence of green or failed CI. Recheck before reporting CI status.

## 12. Next execution order

1. Reconcile the strict 47-row findings into bounded Source/EU correction and rights worklists; keep all 47 HOLD until each defect is resolved.
2. Recover the 14 unnamed IDs from the preliminary 17-Claim risk screen and reconstruct the deduplicated ledger for the separate 711-row queue.
3. Re-run the full-corpus strict generic-EU scan after the new report files are present; filename signals remain discovery aids only.
4. Continue MVP quality/release-gate review; PRs #22/#24/#25/#26/#27 remain Draft/unmerged until exact-head CI and non-automated release gates are verified.
5. Preserve main, M13 Draft state, all publication HOLDs, and the rule against merging before every required gate passes.


## 13. Exact-head CI and unresolved preliminary-screen IDs — 2026-11-14

- Current M13 branch / PR #21 exact head: `379d8540190db6051f60048473615a8c30a36988`; PR #21 remains open, Draft and unmerged, based on `m12-human-factors-source-and-human-view-2026-10-09`.
- Exact-head GitHub Actions recheck:
  - Offline Edition: **SUCCESS** (run 43630742788).
  - Reference implementation tests: **IN PROGRESS** (run 43630742791).
  - Release Conformance Gate: **IN PROGRESS** (run 43630743376).
  - Therefore exact-head M13 CI is **not yet green**. Do not mark the package set technically complete until the latter two finish successfully.
- Downloaded and inspected the exact queue artifact from workflow run `43496934373`, artifact `14071268296`. It contains the 711-row CSV, generated automation queue, review evidence packets (0 packets) and runtime metrics. It does not contain the missing preliminary 14-ID selection list.
- Rechecked the preliminary report, coverage reconciliation, second-screen report, Packages 03–06 and prior conversation records. The preliminary report names only `CLM-AFTERSHOCK-DAMAGE`, `CLM-ELECTRICAL_SAFETY_OSHA_A`, and `CLM-FLOOD-FOOD-FDA-CONTACT`; no recoverable exact IDs were found for the other 14 observations.
- Keep those 14 historical observations **unidentified and unreconciled**. Do not infer their IDs from later packages or count them as unique. The current defensible coverage is 45 explicit unique IDs in the first four reports plus 35 additional explicit IDs in Packages 05/06, with 14 unnamed observations still unresolved (per the coverage reconciliation artifact).
- MVP PR state rechecked: PRs #22, #24, #25, #26 and #27 are all open, Draft and unmerged. Their latest exact-head workflow runs returned success for the required reported checks; PR #25 also has its private SI preview success and PR #27 its browser-form tests success. This is technical status only; the real-record public pilot remains NO-GO for the previously documented editorial, rights, independent-reader, privacy/operations and deployment gates.


## 14. Continuation update — queue generator repair and risk-screen Package 08 (2026-11-14)

### Queue generator defect and correction

- Root cause in `REFERENCE/m13_audit_pipeline.py`: queue candidate selection used the D/E/B scored-report ledger to exclude records. This conflated score-ledger presence with risk-triage completion and caused a valid 711-Claim risk-unassessed inventory to produce 0 selected Claims and 100 unfilled slots.
- Corrected candidate eligibility: select Claims with no recorded risk-domain or machine-triage signal, regardless of D/E/B ledger match.
- Added exact prior-screen deduplication by scanning auditable M13 risk-screen reports, including compact grouped IDs such as `CLM-X-A/B/C`.
- Added a holdout for the topic families containing the 14 unreconciled historical observations: disaster response, disaster-risk reduction, hydropower, industrial safety, public-health surveillance, safety engineering and infrastructure resilience.
- Added regression tests for D/E/B independence, exact prior-screen exclusion, grouped Claim-ID expansion, holdout handling and disjoint exclusion counts.
- Code commits: `ea6349dd30cb9a0880e60e7bc9b02e0b4cdb9c8a`, `fc4cce477f6bf61f31ce35b12ed6b9b62d306824`, `7f69471703523700dd27bfcfc1b872cec390f8f2`.
- Test commits: `671ddaec86e69b8c80b0c89738ca6de27cf1d887`, `24fd5a019c04c9173f0c30cc28ed503f620a3f0f`, `14972f3711b3632e1e11badcbf54cc10e6055469`.

### Successful queue generation

- Workflow run `43631545843` — M13 Audit Queue Automation: **SUCCESS** on revision `64517d688d4ea6bdc5bfc2e291014ab904989605`.
- Artifact `14128675169` contains the generated 711-row unassessed inventory, deduplicated 100-Claim queue and 100 reviewer evidence packets.
- Artifact counts: 711 risk-UNASSESSED Claims; 236 previously screened explicit IDs excluded; 17 unassessed Claims held out by unresolved-observation topic family; 15 IDs are in both exclusion sets; therefore 238 unique exclusions and 473 eligible candidates; 100 selected; 0 unfilled; 100 unique IDs; five lanes of 20; 100 evidence packets.
- The latest disjoint-exclusion metrics and their tests were added after that successful run; rerun the workflow at the final HEAD before declaring the latest revision green.
- This fixes queue generation. It does not assign risk labels or D/E/B scores.

### Risk-screen Package 08

- File: `RELEASE/M13-UNASSESSED-RISK-CONTENT-SCREEN-PACKAGE-08-2026-11-14.md`.
- Screens 20 exact Claims that are all present in the successful deduplicated 100-ID queue: Web Systems A/B/C; Climate Adaptation A/B/C; Climate Basics A/B/C; Cloud Computing A/C; Combinatorics C; Communication A/B/C; Comparative Civilizations B/C; Computer Architecture A/B/C.
- Exact Claim→EU→Source chains resolve 20/20; 3 EUs are v2 with MDN section locators, 17 remain generic/source-level.
- Desk fit: 11 direct conceptual, 5 partial, 4 not established by the registered Source. Routing only: 3 elevated, 11 moderate, 6 low direct-consequence.
- Zero canonical edits, zero risk metadata changes, zero D/E/B changes, zero specialist sign-offs and zero publication approvals.
- The 14 unnamed historical observations remain unreconciled. The report does not claim cumulative unique coverage.

### MVP / branch guardrails

- PR #21 M13 and PRs #22/#24/#25/#26/#27 MVP remain open, Draft and unmerged. Main remains untouched.
- The queue generator repair does not change MVP implementation. Continue the MVP exact-head security, browser, editorial, rights, privacy/operations and deployment gate review in parallel.
- Do not merge or mark public-pilot GO until exact-head CI is green and all non-automated gates are independently satisfied.
