# M13 — residual 356 queue: source-review report-body exact-triple reconciliation

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue: exact 356-row residual generic Evidence Use queue reconstructed from workflow run 43748097686 artifacts 14174823129 and 14174388824, plus the disjoint 20-Claim priority review.

## 1. Purpose and method

The coverage artifact records at least one source-review report filename mention for all 356 residual rows. A filename mention is a routing hint only. This pass therefore fetched all **60 distinct report files** named by the 356 queue rows from the current M13 branch and scanned their report bodies.

A row was counted as an exact body-level triple match only where the report body contains the exact versioned identifiers:
- expected Claim ID at `@1`;
- expected Evidence Use ID at `@1`;
- expected Source ID at `@1`.

The three identifiers were checked in the same report body and their local section/row context was inspected. A report title, slice name, source institution/title, bare ID, unversioned ID, or filename mention alone does not count. The matcher does not infer an ID from a similar title and does not transfer any review finding into canonical records.

## 2. Result

| Measure | Result |
|---|---:|
| Residual queue rows | 356 |
| Rows with at least one source-review filename mention | 356/356 |
| Distinct report files fetched and inspected | 60 |
| Distinct versioned EU@1 tokens found in those report bodies | 43 |
| Exact Claim@1 + EU@1 + Source@1 triples confirmed | **36** |
| Residual rows without an exact triple confirmed by this pass | **320** |
| Canonical review findings imported | 0 |
| D/E/B scores assigned | 0 |
| Canonical writes authorized | 0 |

The 320 rows are **not** asserted to have never been reviewed. They remain unverified by this strict identifier/version test because the cited report body either lacks an exact versioned EU/Claim/Source triple, uses only a bare or differently scoped identifier, names sources in prose without the canonical Source ID, or the report body does not identify the complete chain. Manual reconciliation remains required before any finding can be attributed to the exact queue row.

## 3. Exact triple matches

The following 36 queue rows have a versioned Claim/EU/Source triple in the cited report body:

| Evidence Use @1 | Exact report body |
|---|---|
| `EU-ACOUSTICS_BASICS-C@1` | `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-03-2026-11-14.md` |
| `EU-ALGEBRA_BASICS-A@1` | Package 03 |
| `EU-ALGEBRA_BASICS-B@1` | Package 03 |
| `EU-ALGEBRA_BASICS-C@1` | Package 03 |
| `EU-ANATOMY_BASICS-A@1` | Package 03 |
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
| `EU-BEHAVIORAL_BIOLOGY_BASICS-A@1` | `M13-STRICT-PASSAGE-LOCATOR-REVIEW-PACKAGE-05-2026-11-14.md` |
| `EU-BEHAVIORAL_BIOLOGY_BASICS-B@1` | Package 05 |
| `EU-BEHAVIORAL_BIOLOGY_BASICS-C@1` | Package 05 |
| `EU-CELL_BASICS-A@1` | Package 05 |
| `EU-CELL_BASICS-B@1` | Package 05 |
| `EU-CELL_BASICS-C@1` | Package 05 |
| `EU-CIVIL_SOCIETY_BASICS-A@1` | Package 05 |
| `EU-HISTORY_OF_MEDICINE-A@1` | Package 05 |
| `EU-HISTORY_OF_MEDICINE-B@1` | Package 05 |
| `EU-HISTORY_OF_MEDICINE-C@1` | Package 05 |
| `EU-HUMANITARIAN_LOGISTICS_BASICS-C@1` | Package 05 |
| `EU-MIGRATION_AND_MOBILITY_BASICS-A@1` | Package 05 |
| `EU-SCIENTIFIC_PUBLISHING_BASICS-A@1` | Package 05 |
| `EU-SCIENTIFIC_PUBLISHING_BASICS-B@1` | Package 05 |
| `EU-SCIENTIFIC_PUBLISHING_BASICS-C@1` | Package 05 |
| `EU-URBAN_PLANNING_BASICS-A@1` | Package 05 |
| `EU-ENERGY_SECURITY_BASICS-A@1` | `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-ENERGY-SECURITY-BASICS-2026-11-12.md` |
| `EU-ENERGY_SECURITY_BASICS-B@1` | Energy Security thematic report |
| `EU-ENERGY_SECURITY_BASICS-C@1` | Energy Security thematic report |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-MEASUREMENT-UNCERTAINTY-BASICS-2026-11-12.md` |

Counts by report:
- Strict Package 03: 9.
- Strict Package 05: 16.
- Strict Package 06: 6.
- Anatomy C reassessment: 1.
- Energy Security thematic report: 3.
- Measurement Uncertainty thematic report: 1.
- Total: **36**.

## 4. Identifier mentions not accepted as exact triples

Seven additional EU@1 tokens were found in the inspected report bodies but were not accepted as exact queue Claim/EU/Source triples:
- `EU-ENERGY-SECURITY@1`: separate EU-specific corroboration record, not the queue's generic Energy Security A/B/C Evidence Use chain.
- `EU-MEASUREMENT_UNCERTAINTY_BIPM@1`: additional BIPM Evidence Use for Measurement Uncertainty B; it is a distinct EU record and does not replace the queue's generic EU mapping.
- `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1` and `EU-MEASUREMENT_UNCERTAINTY_BASICS-C@1`: the thematic report names NIST/BIPM source works in prose but does not state the exact expected canonical Source ID beside the complete triple for those Claim sections.
- `EU-STATISTICS_INFERENCE_BASICS-A@1`, `EU-STATISTICS_INFERENCE_BASICS-B@1`, `EU-STATISTICS_INFERENCE_BASICS-C@1`: the report identifies Claim/EU pairs and specific NIST passages, but does not identify the exact canonical Source ID in those Claim sections.

These are valuable source-review leads. They must be reconciled to the canonical queue's Source ID/version and the precise EU record before any result is imported. The report's narrative description of an institution or publication is not interchangeable with the canonical Source identity.

## 5. Required next actions

1. Complete manual row-level matching for the 320 queue rows without an exact triple confirmed here. Use the report body, exact Claim/EU/Source identity and version, and the exact passage/locator—not only a text match.
2. Resolve the seven non-matching EU identifier cases above, preserving distinct corroboration records and Source identities.
3. For each matched report, classify the actual passage result (DIRECT / PARTIAL / NOT ESTABLISHED), locator quality, scope limitations, rights, source currency and required specialist review. Do not infer those results from the presence of a triple.
4. Keep all 356 rows subject to their existing HOLD/human-confirmation requirements. Do not write scores, status, relations, rights or publication decisions from this report-only reconciliation.

## 6. Protected state

No Claim, Evidence Use, Source, Assessment, Relation, risk, allowlist or publication record was changed. No historical evaluation was transferred into current D/E/B. No D/E/B score was assigned. No canonical write permission was created. PR #21 remains Draft/open/unmerged; `main` was not modified.
