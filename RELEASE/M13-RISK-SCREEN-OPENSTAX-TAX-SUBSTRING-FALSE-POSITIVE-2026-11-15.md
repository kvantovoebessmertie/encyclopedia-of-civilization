# M13 — risk-screen false-positive correction: OpenStax / tax substring

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Current code/test commits:
- `5600144efadc77c6f2a68c7d7c9c0f8fad50d2bf` — bounded English legal/financial word families
- `5f7a8cb9c04f4233601b0915bce20b5a13899cd2` — regression coverage

## 1. Confirmed defect

The English legal/financial regex contained unbounded substrings such as `tax`. This matched the middle of the source name `OpenStax` and falsely classified unrelated educational Claims as `legal_financial`.

A comparison of the pre-fix PR merge-tree worksheet (`87a78a69f89700f4cf06dac7bfb2f21f1045d8d0`) with the corrected worksheet (`e72cf8ec71d0659a9c042077db994fb7a214e872`) found:
- legal_financial classifications: 215 → 131 (84 fewer false-positive matches);
- high_consequence_screen flags across all 1,494 Claims: 595 → 519 (76 fewer; some affected Claims had another independent risk domain);
- no new legal_financial classifications were introduced.

The regression confirms that OpenStax Biology 2e does not match the legal/financial domain, while genuine terms such as tax, taxation, taxable, legal jurisdictions, loans and contractual obligations still match.

## 2. Corrected classifier

The English terms now use word boundaries and explicit word families:
- legal / illegal; jurisdiction(s);
- tax, taxes, taxation, taxpayer(s), taxable;
- loan(s), contract(s), contractual;
- financial, investment(s), accounting, financial reporting.

Russian morphological stems are unchanged. This avoids substring collisions without dropping common inflected forms.

## 3. Exact generic-EU queue reconciliation

The current generic-EU candidate set contains 516 mapped Claim/Evidence Use pairs. The corrected worksheet identifies 120 high-consequence candidates in that set. The existing 20-Claim priority second-pass group remains a separate subset of the residual population.

Therefore the corrected routing arithmetic is:

`516 - 120 - 20 = 376` residual generic-EU candidates.

The earlier 359-row residual ledger was based on a stale 137-high-consequence worksheet. It omitted 17 Claims that were falsely classified as high consequence solely because their OpenStax source identities contained the substring tax. These 17 must be added to the residual remediation ledger. The three Behavioural Biology Claims newly flagged in the pre-fix worksheet are already part of the original 359 residual set; after correction they remain in that set and are not counted again.

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

The corrected worksheet artifact was generated on PR merge-tree revision `e72cf8ec71d0659a9c042077db994fb7a214e872`. The exact branch HEAD after the word-family follow-up is `5f7a8cb9c04f4233601b0915bce20b5a13899cd2`; its final exact-head Reference Tests, Release Conformance Gate and Offline Edition results remain pending at this checkpoint.

After the final workflow results, re-run the worksheet on the same final HEAD and confirm the 120 / 20 / 376 partition. Keep PR #21 Draft/unmerged and `main` unchanged.

M13 remains OPEN / NOT RELEASE-READY. This routing correction does not assign D/E/B scores, grant rights, approve specialist review or Human View, or authorize publication.
