# M13 — residual 356 queue: source-identity crosswalk for five partial report matches

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input: corrected scan of 60 report files referenced by the residual 356 queue, plus 16 additional files referenced only by excluded candidates, as documented in `M13-RESIDUAL-356-SOURCE-REPORT-BODY-EXACT-TRIPLE-RECONCILIATION-2026-11-23.md`.

## 1. Purpose

The corrected strict report-body scan across the 60 residual-associated report files found five residual rows where the report contains the exact Claim@1 and EU@1 and names the source, but does not print the canonical Source ID token in the Claim section. This tranche resolves whether the named source is the same source identity as the exact Source@1 linked by the canonical EU@1 record.

This is a source-title/URI-to-canonical-Source crosswalk, not an explicit Source-ID token match. The distinction is retained in the ledger.

## 2. Exact crosswalk checks

### Measurement Uncertainty B

- Report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-MEASUREMENT-UNCERTAINTY-BASICS-2026-11-12.md`.
- Report body identifies Claim `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1`, EU `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1`, and lists current sources NIST TN 1297 and BIPM/JCGM VIM. It also identifies a separate `EU-MEASUREMENT_UNCERTAINTY_BIPM@1`.
- Canonical EU-B@1 was fetched: its `claim_ref` is Claim B@1 and its `source_ref` is `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`.
- Canonical Source@1 was fetched: its URI is exactly `https://www.nist.gov/pml/nist-technical-note-1297`, the NIST TN 1297 document identified in the report.
- Result: **Source identity crosswalk resolved** for the queue's generic EU-B to NIST TN 1297. The separate BIPM EU remains a distinct chain and is not substituted for the queue EU.

### Measurement Uncertainty C

- Report: same Measurement Uncertainty thematic report.
- Report body identifies Claim C@1 and EU-C@1 and names NIST TN 1297 as the current Source.
- Canonical EU-C@1 was fetched: its `claim_ref` is Claim C@1 and its `source_ref` is `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`.
- Canonical Source@1 URI exactly matches the NIST TN 1297 URL above.
- Result: **Source identity crosswalk resolved**. The report separately notes that VIM 2.48 is the strongest conceptual definition for “measurement model” and is not currently linked to Claim C; this remains a separate proposed Source/EU addition, not an inferred correction.

### Statistics Inference A, B and C

- Report: `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-STATISTICS-INFERENCE-BASICS-2026-11-12.md`.
- The report contains the exact Claim@1 and EU@1 for A, B and C. It identifies the reviewed source as the NIST/SEMATECH *e-Handbook of Statistical Methods*, cites its exact chapter/section pages, and states in its cross-record findings that all three Evidence Uses point to the intended Claim and Source IDs.
- Canonical EU-A@1, EU-B@1 and EU-C@1 were fetched. Each references its corresponding Claim@1 and `SRC-STATISTICS_INFERENCE_BASICS@1`.
- Canonical Source@1 was fetched: its identity is NIST/SEMATECH — *e-Handbook of Statistical Methods*, with URI `https://www.itl.nist.gov/div898/handbook/`. The report's cited section URLs are pages within that same canonical handbook domain and edition.
- Result: **Source identity crosswalk resolved** for all three Claims. The report still finds that the EUs lack claim-specific locators; the exact section URLs in the report are review findings, not locators already stored in canonical EUs.

## 3. Updated report-body routing ledger

| Measure | Result |
|---|---:|
| Residual queue | 356 |
| Explicit Claim@1 / EU@1 / Source@1 triples | 19 |
| Additional exact Claim@1 / EU@1 with Source identity crosswalk | 5 |
| Residual rows with report-body source identity resolved | **24/356** |
| Residual rows without an EU@1 token in the 60 residual-associated report bodies | 332 |
| Residual rows still lacking an explicit triple or source crosswalk | 332 |
| Canonical EU locator updates made | 0 |
| Canonical Source changes made | 0 |
| D/E/B scores assigned | 0 |

The five crosswalk rows remain distinct from the 19 explicit triples. They are not silently added to the exact-triple count. Together they establish report-body identity linkage for 24 residual rows. The other 332 residual rows still require manual source-report reconciliation.

## 4. Substantive findings and remaining boundaries

- Measurement Uncertainty A/B/C have direct passages located in NIST TN 1297 and BIPM/JCGM VIM, but current EU descriptions remain generic. Claim B and C need VIM-specific Source/EU linkage if those passages are used; Claim C's measurement-model definition must not be attributed solely to NIST.
- Statistics Inference A/B/C have direct NIST e-Handbook passages for sampling inference, method-specific assumptions, confidence intervals and hypothesis tests. The report warns that assumptions are method-specific and that a non-rejected hypothesis must not be treated as proven true. The current EUs still point only to the handbook landing page.
- No review finding is imported into a canonical record. No locator is added, no source is silently substituted, and no claim wording is changed.

## 5. Protected state

All five Claims remain HOLD. No canonical Claim, Evidence Use, Source, Assessment, Relation, risk, allowlist or publication record was changed. No D/E/B score was assigned or transferred. No rights, specialist, Human View or release approval is inferred. PR #21 remains Draft/open/unmerged; `main` was not modified.
