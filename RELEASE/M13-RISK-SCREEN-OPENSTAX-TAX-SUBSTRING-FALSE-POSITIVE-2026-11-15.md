# M13 — risk-screen false-positive correction: OpenStax / tax substring

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
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

The latest exact generic-EU coverage artifact contains **510 unique mapped Claim/Evidence Use pairs** (workflow run `43710332774`, artifact `14159847839`, generated on branch commit `bb73e1342192f7926af7e247fe0759a481b47a37`). The corrected claim worksheet (workflow run `43710480136`, artifact `14160401976`, PR merge-tree revision `4a1b48229669202ffa4eeb1b89e5d884d93f38fb`) identifies 120 high-consequence candidates in that 510-row set. The existing 20-Claim priority second-pass group is present in the 510 and disjoint from those 120.

Therefore the current routing arithmetic is:

`510 - 120 - 20 = 370` residual generic-EU candidates.

The earlier 359-row residual ledger was based on a stale risk partition. The 17 Claims listed below were falsely classified as high consequence and must be imported into the residual ledger; all 17 are present in the current 510-row coverage set and remain outside both the 120 high-consequence and 20 priority groups.

A further six Evidence Use records have since moved to version 3 with Claim-specific source descriptions and no longer match the generic-description markers:
- `EU-ASSET_MANAGEMENT_BASICS-A`, `EU-ASSET_MANAGEMENT_BASICS-B`, `EU-ASSET_MANAGEMENT_BASICS-C`;
- `EU-BEHAVIORAL_BIOLOGY_BASICS-A`, `EU-BEHAVIORAL_BIOLOGY_BASICS-B`, `EU-BEHAVIORAL_BIOLOGY_BASICS-C`.

These six explain the 516 → 510 coverage reduction. Their removal from the generic-EU candidate set is not a substantive approval or publication clearance; all existing partial-support, rights and HOLD dispositions remain in force. The three Behavioural Biology Claims must not be counted again in the current generic-EU residual population.

## 4. Whole-corpus impact and no lost scored Claims

The corrected worksheet was compared with the pre-fix worksheet across all 1,494 Claims:
- 84 Claims lost the false legal_financial match caused by OpenStax.
- 76 of those also lost high_consequence_screen; the other 8 retain an independent risk domain and therefore remain high-consequence routed.
- All 76 Claims that lost the high-consequence flag have an exact matching historical scored-report row with D/E/B fields in Reference workflow run 43710480136, artifact 14160590942. The current ledger still reports 1,494/1,494 Claims with at least one scored-row match and zero unmatched report rows. No score value was changed by this classifier correction.
- 20 of the 76 intersect the 516 generic-EU candidate set: 17 are the additional residual Claims listed below, and the 3 Behavioural Biology Claims already belong to the original 359 residual cohort.
- The remaining 56 are outside both the 516 generic-EU candidate set and the 711-Claim unassessed-risk queue. They already have scored-report rows; no new generic-EU or unassessed-risk queue is created for them by this correction.
- Exactly 3 false-positive Claims overlap the 711-Claim queue: Behavioural Biology A/B/C. Their Package 06 source-fit screen remains the controlling review; all three stay HOLD.

These are routing and accounting corrections only. Historical score rows are not re-certified by their presence in the ledger.

### 17 additional Claims to import into the residual ledger

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
| CLM-ENERGY_BASICS-A | EU-ENERGY_BASICS-A | SRC-ENERGY_BASICS | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §9.1 supports kinetic energy; locator and depth review needed |
| CLM-ENERGY_BASICS-B | EU-ENERGY_BASICS-B | SRC-ENERGY_BASICS | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §9.1 supports potential energy; locator and configuration scope needed |
| CLM-ENERGY_BASICS-C | EU-ENERGY_BASICS-C | SRC-ENERGY_BASICS | M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §9.1 supports work/energy transfer; locator and wording check needed |
| CLM-MATTER_BASICS-A | EU-MATTER_BASICS-A | SRC-MATTER_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §1.2 supports element/compound/mixture distinction; locator and Claim-depth review needed |
| CLM-MOTION_BASICS-A | EU-MOTION_BASICS-A | SRC-MOTION_BASICS | M13-BATCH-44-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-11.md | §2.1 supports reference-frame statement; locator missing |
| CLM-MOTION_BASICS-B | EU-MOTION_BASICS-B | SRC-MOTION_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §3.1 is average velocity (displacement/time); Russian Claim may conflate speed and velocity; HOLD |
| CLM-MOTION_BASICS-C | EU-MOTION_BASICS-C | SRC-MOTION_BASICS | M13-BATCH-44-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-11.md | Acceleration passage relevant; exact locator missing |
| CLM-POLITICAL_SCIENCE_BASICS-B | EU-POLITICAL_SCIENCE_BASICS-B | SRC-POLITICAL_SCIENCE_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §1.5 supports empirical evidence/hypotheses; locator missing |
| CLM-POLITICAL_SCIENCE_BASICS-C | EU-POLITICAL_SCIENCE_BASICS-C | SRC-POLITICAL_SCIENCE_BASICS | M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md | §§1.4–1.5 support normative/empirical distinction; locator missing |

## 4. Exact current record-link check

All 17 current Evidence Use records were freshly fetched from the M13 branch:
- EU record version: v1 for 17/17;
- Claim reference: exact matching Claim @1 for 17/17;
- Source reference: exact matching Source @1 for 17/17;
- provenance.created_from: exact matching Source @1 for 17/17.

The prior source-review report bodies were inspected for the exact Claim IDs and findings. These rows are already source-reviewed; do not repeat the same source searches. Import the existing dispositions and locator/rights actions into the consolidated ledger.

## 5. Disposition and guardrails

- The 17 additions remain HOLD; no Claim is cleared by reclassification.
- The three Cell Basics Claims retain the explicit OpenStax rights hold. Rights for all other OpenStax sources remain separately reviewable; a public URL is not blanket permission for AI ingestion or reuse.
- Motion B retains its speed/velocity terminology issue.
- Constitutional Systems C retains a scope/variation issue.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation, risk metadata or D/E/B value was changed.
- No automated risk flag is a substantive risk determination.
- The 17-row import is an append-only remediation-ledger correction, not a new source-passage review population.

## 6. Verification

The corrected worksheet artifact on PR merge-tree revision `4a1b48229669202ffa4eeb1b89e5d884d93f38fb` confirms 1,494 Claims and 4,851 scanned records, with 131 legal_financial risk-domain matches and 519 high_consequence_screen flags. Joined to the latest 510-row generic-EU coverage artifact, it confirms 120 high-consequence candidates, 20 priority second-pass Claims and **370 residual candidates**. All 17 supplemental Claims listed above are present in the current residual set. The six EU v3 records listed in Section 3 are absent from the current generic-EU candidate set.

The earlier 359-row ledger and the intermediate 376-row arithmetic are superseded. The current conversation now has a regenerated 370-row residual ledger and README, built from the 510-row coverage artifact and the 1,494-Claim worksheet. A fresh exact-head 3/3 verification remains required after the final documentation/test commits.

After the final workflow results, re-run both the claim worksheet and generic-EU coverage on the same final HEAD and confirm the 510 / 120 / 20 / 370 partition. Keep PR #21 Draft/unmerged and `main` unchanged.

M13 remains OPEN / NOT RELEASE-READY. This routing correction does not assign D/E/B scores, grant rights, approve specialist review or Human View, or authorize publication.
