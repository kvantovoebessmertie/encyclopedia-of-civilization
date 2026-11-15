# M13 — risk-screen false-positive correction: OpenStax / tax substring

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`

> **Current routing supersession:** the 507/367 figures in §3 below are historical. The latest exact coverage and queue reconciliation is `M13-GENERIC-EU-496-356-CURRENT-QUEUE-CHECKPOINT-2026-11-15.md`: 496 current generic-EU candidates, 120 high-consequence, 20 priority second-pass, 356 residual. The current 41-Claim unassessed-risk queue has zero overlap with the current generic-EU set. The false-positive classifier findings and same-revision before/after analysis below remain valid.

Current code/test commits:
- `5600144efadc77c6f2a68c7d7c9c0f8fad50d2bf` — bounded English legal/financial word families
- `5f7a8cb9c04f4233601b0915bce20b5a13899cd2` — regression coverage

## 1. Confirmed defect

The English legal/financial regex contained unbounded substrings such as `tax`. This matched the middle of the source name `OpenStax` and falsely classified unrelated educational Claims as `legal_financial`.

A same-revision comparison of the pre-fix worksheet (`87a78a69f89700f4cf06dac7bfb2f21f1045d8d0`) with the corrected worksheet (`16b4c8ee71f7f2c85b0f0a07298a16d26c53521a`) found:
- legal_financial classifications: 219 → 131 (**88 fewer false-positive matches**);
- high_consequence_screen flags across all 1,494 Claims: 595 → 519 (**76 fewer**; some affected Claims had another independent risk domain);
- no new legal_financial classifications were introduced.

Of the 88 removed classifications, 87 were triggered by `tax` inside OpenStax source identities and one by `tax` inside the ordinary word `taxonomy` in an electrical-safety evidence description. The earlier worksheet at revision `74f9bbdb461a734ddd1041b1ed2520266de22fcf` had 215 legal_financial matches and 591 high-consequence flags; it is a different, earlier snapshot and must not be mixed with the `87a78a` baseline.

The regression confirms that OpenStax Biology 2e, taxonomy and similar substrings do not match the legal/financial domain, while genuine terms such as tax, taxation, taxable, legal jurisdictions, loans and contractual obligations still match.

## 2. Corrected classifier

The English terms now use word boundaries and explicit word families:
- legal / illegal; jurisdiction(s);
- tax, taxes, taxation, taxpayer(s), taxable;
- loan(s), contract(s), contractual;
- financial, investment(s), accounting, financial reporting.

Russian morphological stems are unchanged. This avoids substring collisions without dropping common inflected forms.

## 3. Exact generic-EU queue reconciliation

The latest exact generic-EU coverage artifact contains **507 unique mapped Claim/Evidence Use pairs** (workflow run `43741898249`, artifact `14172389123`, generated on branch commit `770dabc0384cf4d113ffa849e6b671b2462a8912`). The corrected claim worksheet generated at the same branch HEAD confirms 120 high-consequence candidates in that 507-row set. The existing 20-Claim priority second-pass group is present in the 507 and disjoint from those 120.

Therefore the current routing arithmetic is:

`507 - 120 - 20 = 367` residual generic-EU candidates.

The earlier 359-row and 370-row residual ledgers are superseded for current routing. The 17 Claims listed below were falsely classified as high consequence and were imported into the residual; 14 of those 17 remain in the current 507-row coverage set and 367-row residual. The three Energy Basics Claims are no longer generic-EU candidates after the bounded source-fit correction described below.

Nine Evidence Use records no longer match the generic-description markers:
- `EU-ASSET_MANAGEMENT_BASICS-A`, `EU-ASSET_MANAGEMENT_BASICS-B`, `EU-ASSET_MANAGEMENT_BASICS-C`;
- `EU-BEHAVIORAL_BIOLOGY_BASICS-A`, `EU-BEHAVIORAL_BIOLOGY_BASICS-B`, `EU-BEHAVIORAL_BIOLOGY_BASICS-C`;
- `EU-ENERGY_BASICS-A`, `EU-ENERGY_BASICS-B`, `EU-ENERGY_BASICS-C`.

The six Asset Management and Behavioural Biology records explain the 516 → 510 reduction. The three Energy Basics records listed below explain the subsequent 510 → 507 reduction. All nine are now EU v3 with claim-specific source descriptions/pinpoints and no longer match the generic-description markers. Their removal is not substantive approval or publication clearance. Asset Management B still has an unsupported opportunities element; Behavioural Biology C remains partially supported and the OpenStax rights boundary unresolved; Energy Basics remains subject to independent semantic and rights review.

## 4. Whole-corpus impact and no lost scored Claims

The corrected worksheet was compared with the pre-fix worksheet at the same PR merge-tree baseline across all 1,494 Claims:
- 88 Claims lost the false legal_financial match: 87 were triggered by `tax` inside OpenStax source identities, and one by `tax` inside `taxonomy` in an electrical-safety evidence description.
- 76 of those 88 also lost `high_consequence_screen`; the other 12 retain an independent risk domain and therefore remain high-consequence routed.
- All 76 Claims that lost the high-consequence flag have an exact matching historical scored-report row with D/E/B fields in Reference workflow run 43710480136, artifact 14160590942. The current ledger still reports 1,494/1,494 Claims with at least one scored-row match and zero unmatched report rows. No score value was changed by this classifier correction.
- 20 of the 76 intersected the historical 516 generic-EU candidate set: 17 are the additional residual Claims listed below; the 3 Behavioural Biology Claims have since been removed from the generic-EU candidate set by their authorized EU v3 source-fit corrections. The three Energy Basics Claims later left the generic-EU set after the separately authorized OpenStax source/pinpoint correction.
- The remaining 56 are outside the historical 516 generic-EU candidate set and the 711-Claim unassessed-risk queue. They already have scored-report rows; no new generic-EU or unassessed-risk queue is created for them by this correction.
- Exactly 3 false-positive Claims overlap the historical 711-Claim queue: Behavioural Biology A/B/C. Their Package 06 source-fit screen remains the controlling review; all three stay HOLD.

These are routing and accounting corrections only. Historical score rows are not re-certified by their presence in the ledger.

### 17 historically reclassified Claims (14 remain in the current residual)

| Claim @1 | Evidence Use @1 | Source @1 | Existing source-review report | Existing finding |
|---|---|---|---|---|
| CLM-CELL_BASICS-A | EU-CELL_BASICS-A | SRC-CELL_BASICS | M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md | Direct conceptual support; §4.1 locator missing; OpenStax rights HOLD |
| CLM-CELL_BASICS-B | EU-CELL_BASICS-B | SRC-CELL_BASICS | M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md | Direct concept support; §§4.2–4.3 locators missing; OpenStax rights HOLD |
| CLM-CELL_BASICS-C | EU-CELL_BASICS-C | SRC-CELL_BASICS | M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md | Direct but broad; §§4.3–4.4 locators missing; OpenStax rights HOLD |
| CLM-COMPUTING_BASICS-A | EU-COMPUTING_BASICS-A | SRC-COMPUTING_BASICS | M13-BATCH-44-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-11.md | §5.1 relevant; exact locator and wording-scope check missing |
| CLM-COMPUTING_BASICS-B | EU-COMPUTING_BASICS-B | SRC-COMPUTING_BASICS | M13-BATCH-44-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §§2.1 and 3.1 directly relevant; locator missing |
| CLM-COMPUTING_BASICS-C | EU-COMPUTING_BASICS-C | SRC-COMPUTING_BASICS | M13-BATCH-44-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §5.1 relevant; locator and digital-representation scope needed |
| CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B | EU-CONSTITUTIONAL_SYSTEMS_BASICS-B | SRC-CONSTITUTIONAL_SYSTEMS_BASICS | M13-BATCH-44-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §10.1 direct; locator and country-variation boundary needed |
| CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C | EU-CONSTITUTIONAL_SYSTEMS_BASICS-C | SRC-CONSTITUTIONAL_SYSTEMS_BASICS | M13-BATCH-44-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md | Partial / scope qualification; §§10.1 and 10.5; HOLD |
| CLM-ENERGY_BASICS-A | EU-ENERGY_BASICS-A@1 (superseded by @3) | SRC-ENERGY_BASICS@1 (superseded by @2) | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | Historical §9.1 review; current OpenStax Chapter 7 §7.2 pinpoint recorded separately; no longer a generic-EU candidate |
| CLM-ENERGY_BASICS-B | EU-ENERGY_BASICS-B@1 (superseded by @3) | SRC-ENERGY_BASICS@1 (superseded by @2) | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | Historical §9.1 review; current OpenStax Chapter 7 §§7.3–7.4 pinpoint recorded separately; no longer a generic-EU candidate |
| CLM-ENERGY_BASICS-C | EU-ENERGY_BASICS-C@1 (superseded by @3) | SRC-ENERGY_BASICS@1 (superseded by @2) | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | Historical §9.1 review; current OpenStax Chapter 7 §7.1 pinpoint recorded separately; no longer a generic-EU candidate |
| CLM-MATTER_BASICS-A | EU-MATTER_BASICS-A | SRC-MATTER_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §1.2 supports element/compound/mixture distinction; locator and Claim-depth review needed |
| CLM-MOTION_BASICS-A | EU-MOTION_BASICS-A | SRC-MOTION_BASICS | M13-BATCH-44-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-11.md | §2.1 supports reference-frame statement; locator missing |
| CLM-MOTION_BASICS-B | EU-MOTION_BASICS-B | SRC-MOTION_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §3.1 is average velocity (displacement/time); Russian Claim may conflate speed and velocity; HOLD |
| CLM-MOTION_BASICS-C | EU-MOTION_BASICS-C | SRC-MOTION_BASICS | M13-BATCH-44-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-11.md | Acceleration passage relevant; exact locator missing |
| CLM-POLITICAL_SCIENCE_BASICS-B | EU-POLITICAL_SCIENCE_BASICS-B | SRC-POLITICAL_SCIENCE_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §1.5 supports empirical evidence/hypotheses; locator missing |
| CLM-POLITICAL_SCIENCE_BASICS-C | EU-POLITICAL_SCIENCE_BASICS-C | SRC-POLITICAL_SCIENCE_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §§1.4–1.5 support normative/empirical distinction; locator missing |

## 4. Exact current record-link check

At the time of the original 17-Claim import, all 17 Evidence Use records were freshly fetched and their Claim/Source/provenance references matched v1. The three Energy Basics records have since been versioned to EU @3, with Claim @2 and Source @2 references, under the separate bounded authorization. The remaining 14 imported Claims remain in the current generic-EU residual; the latest coverage artifact maps each to one current Evidence Use ID.

The prior source-review report bodies were inspected for the exact Claim IDs and findings. These rows are already source-reviewed; do not repeat the same source searches. Import the existing dispositions and locator/rights actions into the consolidated ledger.

## 5. Disposition and guardrails

- All 17 historically reclassified Claims remain HOLD; no Claim is cleared by reclassification. The three Energy Basics Claims left the generic-EU routing set only because their Evidence Use descriptions were corrected, not because their review/HOLD status was cleared.
- The three Cell Basics Claims retain the explicit OpenStax rights hold. Rights for all other OpenStax sources remain separately reviewable; a public URL is not blanket permission for AI ingestion or reuse.
- Motion B retains its speed/velocity terminology issue.
- Constitutional Systems C retains a scope/variation issue.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation, risk metadata or D/E/B value was changed.
- No automated risk flag is a substantive risk determination.
- The original 17-row import was an append-only remediation-ledger correction, not a new source-passage review population. The current residual contains 14 of those rows after the three Energy Basics EU corrections.

## 6. Verification

The refreshed worksheet confirms 1,494 Claims and 4,851 scanned records, with 131 legal_financial risk-domain matches and 519 high_consequence_screen flags. Joined to the latest 507-row generic-EU coverage artifact, it confirms 120 high-consequence candidates, 20 priority second-pass Claims and **367 residual candidates**. Fourteen of the 17 historically reclassified Claims remain in the current residual; the three Energy Basics Claims are now outside the generic-EU set after their authorized EU v3 correction.

The earlier 359-row and 370-row ledgers and intermediate 376-row arithmetic are superseded. The current conversation now has a regenerated 367-row residual ledger and README, built from the 507-row coverage artifact and the 1,494-Claim worksheet. The exact-head automation queue selects 42 unassessed-risk Claims; 11 overlap the 367 residual and 31 are outside it. A fresh exact-head 3/3 verification remains required after the final documentation/test commits.

After the final workflow results, re-run the claim worksheet and generic-EU coverage on the same final HEAD and confirm the 507 / 120 / 20 / 367 partition. Keep PR #21 Draft/unmerged and `main` unchanged.

M13 remains OPEN / NOT RELEASE-READY. This routing correction does not assign D/E/B scores, grant rights, approve specialist review or Human View, or authorize publication.
