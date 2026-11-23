# M13 — residual 356 queue: corrected source-report body exact-triple reconciliation

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **CORRECTED CURRENT RESULT — supersedes the first publication of this report.**

## 0. Correction and supersession

The first publication counted 36 exact triples found in 60 report bodies as if all 36 belonged to the residual 356-row queue. That was an overcount: 17 of those 36 triples were outside the residual queue (12 high-consequence candidates and five records outside the 496-candidate denominator). The corrected queue intersection is **19/356**, not 36/356.

A further 16 distinct report files from the current coverage artifact were fetched and checked. They contained 14 additional exact triples, all outside the residual queue (13 high-consequence candidates and one priority-20 candidate). This corrected report replaces the earlier 36/356 interpretation. No canonical data or evaluation was changed.

## 1. Current queue and method

The current Generic Evidence Use Coverage workflow artifact was regenerated on M13 HEAD `1d51ab46f6d5786fed03da6a69f0a3d21a6b4c81` (run 45158327193; artifact 14810310697). It reports:
- 496 generic-EU candidates;
- 496/496 mapped to exact Claim IDs and EU IDs;
- 0 unmapped and 0 ambiguous mappings;
- 496/496 candidates with at least one source-review filename mention.

Reconciliation against the exact Claim worksheet and the separate priority-20 report retains the same residual queue:
- 120 high-consequence machine-triage candidates;
- 20 disjoint priority-20 Claims;
- overlap: 0;
- residual: 496 − 120 − 20 = **356** unique Claim/EU pairs and canonical paths.

The current coverage artifact names 76 distinct source-review report files across the full 496-candidate population. **60 of those files are referenced by the residual 356 rows**; the other 16 are referenced only by candidates excluded from the residual queue. All 76 files were fetched and inspected so that exact matches from excluded rows would not be miscounted as residual matches. A filename mention remains only a routing hint.

An exact match requires the expected versioned Claim@1, EU@1 and Source@1 identifiers to appear together in the report's same row or Claim section. Bare IDs, source titles/institution names, report filenames, unversioned IDs, or another EU/Source chain do not count.

## 2. Corrected results

| Measure | Result |
|---|---:|
| Residual queue | 356 |
| Rows with source-review filename mention | 356/356 |
| Distinct report files referenced by residual queue | 60 |
| Additional report files referenced only by excluded candidates | 16 |
| Distinct report files fetched and inspected overall | 76 |
| Distinct EU@1 tokens found across those report bodies | 59 |
| Exact versioned triples found across all 76 reports | 50 |
| Of those exact triples, belonging to the residual 356 queue | **19** |
| Exact triples outside the residual queue | 31 |
| Residual rows with an EU@1 mention but no exact Claim/EU/Source triple | 5 |
| Residual rows with no EU@1 token in the inspected report bodies | 332 |
| Residual rows without an exact triple confirmed | **337** |

The 31 exact triples outside the residual queue are excluded from its numerator:
- 25 belong to the 120 high-consequence machine-triage candidates;
- 1 belongs to the separate priority-20 set;
- 5 are outside the 496-candidate denominator (three Behavioral Biology and two Cell records).

Seven additional EU@1 tokens are not exact triples: five are partial residual references (listed in §4) and two are distinct non-queue Evidence Use records. They are not silently mapped into the residual queue.

## 3. Exact triples confirmed within the residual 356

The following 19 exact Claim@1 / EU@1 / Source@1 triples are present in the cited report bodies and are members of the residual queue:

| Evidence Use @1 | Exact report body |
|---|---|
| `EU-ALGEBRA_BASICS-A@1` | `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-03-2026-11-14.md` |
| `EU-ALGEBRA_BASICS-B@1` | Package 03 |
| `EU-ALGEBRA_BASICS-C@1` | Package 03 |
| `EU-ANATOMY_BASICS-B@1` | Package 03 |
| `EU-ARCHIVAL_SCIENCE-A@1` | Package 03 |
| `EU-ARCHIVAL_SCIENCE-B@1` | Package 03 |
| `EU-ARCHIVAL_SCIENCE-C@1` | Package 03 |
| `EU-ANATOMY_BASICS-C@1` | `M13-ANATOMY-BASICS-C-SOURCE-PASSAGE-REASSESSMENT-2026-11-15.md` |
| `EU-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-06-2026-11-14.md` |
| `EU-BEHAVIORAL_ECONOMICS_BASICS-C@1` | Package 06 |
| `EU-BIODIVERSITY_BASICS-A@1` | Package 06 |
| `EU-BIODIVERSITY_BASICS-B@1` | Package 06 |
| `EU-CALIBRATION_BASICS-B@1` | Package 06 |
| `EU-CALIBRATION_BASICS-C@1` | Package 06 |
| `EU-CELL_BASICS-C@1` | `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md` |
| `EU-ENERGY_SECURITY_BASICS-A@1` | `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-ENERGY-SECURITY-BASICS-2026-11-12.md` |
| `EU-ENERGY_SECURITY_BASICS-B@1` | Energy Security thematic report |
| `EU-ENERGY_SECURITY_BASICS-C@1` | Energy Security thematic report |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-MEASUREMENT-UNCERTAINTY-BASICS-2026-11-12.md` |

Counts by report:
- Strict Package 03: 7 residual rows (two other triples in that report are outside the residual queue).
- Strict Package 05: 1 residual row (the other exact triples are outside the candidate denominator or high-consequence exclusions).
- Strict Package 06: 6 residual rows.
- Anatomy C reassessment: 1.
- Energy Security thematic report: 3.
- Measurement Uncertainty thematic report: 1.
- Total: **19**.

These matches establish report-body identity/version linkage only. They do not certify that the passage is sufficient, the locator is reproducible, the source is current/independent, rights are clear, or the Claim is suitable for scoring/publication.

## 4. Partial residual EU mentions requiring source-ID reconciliation

Five additional residual rows have a versioned EU@1 mention and corresponding Claim context, but the report does not state the exact expected canonical Source ID/version in the same Claim section:
- `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1`;
- `EU-MEASUREMENT_UNCERTAINTY_BASICS-C@1`;
- `EU-STATISTICS_INFERENCE_BASICS-A@1`;
- `EU-STATISTICS_INFERENCE_BASICS-B@1`;
- `EU-STATISTICS_INFERENCE_BASICS-C@1`.

The Measurement Uncertainty report names NIST/BIPM works in prose; the Statistics Inference report identifies NIST passages. Those descriptions are useful research evidence, but are not substitutes for the exact canonical Source ID/version. The separate `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` is an additional distinct Evidence Use, not the queue's generic EU mapping.

Two other EU@1 tokens in the 76 report bodies are not members of the residual candidate mapping:
- `EU-ENERGY-SECURITY@1` (separate EU-specific corroboration record);
- `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` (additional BIPM Evidence Use).

## 5. Additional 16 report files from excluded candidates checked

The full 496-candidate artifact introduced 16 additional report filenames beyond the 60 files associated with the residual queue. These 16 are referenced only by high-consequence or priority-20 candidates, not by the residual 356:
- `M13-BATCH-44-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-BATCH-44-LANE-03-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-BATCH-44-LANE-04-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-BATCH-44-LANE-05-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-BATCH-45-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-CLAIM-AUDIT-BATCH-41-INITIAL-SOURCE-FIT-SPOTCHECK-2026-10-10.md`
- `M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-569-571-2026-10-11.md`
- `M13-EVIDENCE-LOCATOR-REVIEW-ENVIRONMENTAL-HEALTH-OCCUPATIONAL-SAFETY-DISASTER-2026-11-12.md`
- `M13-EVIDENCE-LOCATOR-REVIEW-WATER-FOOD-SANITATION-2026-11-12.md`
- `M13-REMAINING-379-PRIORITY-20-CLAIM-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-REMAINING-49-MODERATE-23-CLAIM-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
- `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-01-2026-11-14.md`
- `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-02-2026-11-14.md`
- `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-FOUNDATION-ENGINEERING-BASICS-2026-11-12.md`
- `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-SOCIAL-POLICY-BASICS-2026-11-13.md`
- `M13-UNSCORED-CLAIM-SOURCE-FIT-TRIAGE-BATCH-11-2026-10-11.md`

These additional reports contain 14 further exact triples, all outside the residual 356: 13 high-consequence candidates and one priority-20 Claim (Foundation Engineering A). Foundation Engineering B/C are priority-20 partial EU mentions, not exact triples. None of these 14 is added to the residual numerator.

## 6. Required next actions

1. Complete manual row-level matching for the 337 residual rows without an exact triple confirmed here. Start with the five partial EU references in §4, then reconcile the remaining report bodies by exact Claim/EU/Source/version.
2. Preserve the 120 high-consequence and 20 priority-20 exclusions; do not reintroduce their exact triples into the residual denominator.
3. For each matched report, classify the actual passage result (DIRECT / PARTIAL / NOT ESTABLISHED), locator quality, scope limitations, source currency, rights, source independence and required specialist review.
4. Do not infer D/E/B or release eligibility from report presence. Every row remains subject to its existing HOLD and human-confirmation requirements.

## 7. Protected state

No Claim, Evidence Use, Source, Assessment, Relation, risk, allowlist or publication record was changed. No historical evaluation was transferred into current D/E/B. No D/E/B score was assigned. No canonical write permission was created. PR #21 remains Draft/open/unmerged; `main` was not modified.
