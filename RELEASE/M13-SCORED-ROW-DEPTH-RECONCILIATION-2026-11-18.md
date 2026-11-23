# M13 scored-row depth reconciliation

Date: 2026-11-18  
Audited branch: `m13-system-wide-depth-audit-2026-10-09`  
Source revision: `a4f3f61c8338a28b76b6594f2215439eebe805cc`  
Source artifact: Reference implementation tests run `44324850558`, artifact `14437300274` (`m13-scored-claim-reconciliation-ledger`)  
Artifact SHA-256: `59549239a3b3b566ad944d312d5497f8fad4e87d9c6914e1660caf1ebe4ad10b`

## 1. Purpose

Correct and refine the interpretation of the 1,501 historical D/E/B rows. This is a read-only reconciliation of report provenance and score-row populations. It does not adjudicate historical scores, replace source review, or certify Claims.

## 2. Reproduced ledger totals

The exact-HEAD ledger reports:

- Claim records in inventory: 1,494.
- Scored report rows: 1,501.
- Unique normalized report Claim IDs: 1,494.
- Duplicate groups: 7, containing 14 rows.
- Unmatched scored rows: 0.
- One separator-normalized match still requires manual confirmation.
- All 1,494 inventory Claims have at least one matching scored row.

The ledger itself explicitly warns that it is an identifier/accounting ledger, not semantic duplicate adjudication, evidence validation, or acceptance of prior scores.

## 3. Row provenance strata

| Report population | Rows | Interpretation |
|---|---:|---|
| Batches 12 and 17–43 | 459 | Earlier scored-report rows; methodology and evidentiary depth are heterogeneous and must be classified per report |
| Batches 44–52 | 900 | Rows extracted from reports explicitly titled source-passage reviews |
| Batch 53 | 100 | Rows extracted from five source-passage review/scoring reports |
| Batch 54 | 42 | Rows extracted from two source-passage review/scoring reports |
| **Total** | **1,501** | |

For Batches 53 and 54 the exact report-file breakdown is:

| Batch 53 report | Rows |
|---|---:|
| `M13-CLAIM-REVIEW-BATCH-53-FINAL-39-CLAIMS-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 39 |
| `M13-CLAIM-REVIEW-BATCH-53-PRIORITY-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 19 |
| `M13-CLAIM-REVIEW-BATCH-53-SAFETY-RISK-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 13 |
| `M13-CLAIM-REVIEW-BATCH-53-LANE04-05-REMAINING-CONCEPTUAL-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 21 |
| `M13-CLAIM-REVIEW-BATCH-53-LANE04-05-ADDITIONAL-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 8 |
| **Batch 53 total** | **100** |

| Batch 54 report | Rows |
|---|---:|
| `M13-CLAIM-REVIEW-BATCH-54-PARTIAL-PRIORITY-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 18 |
| `M13-CLAIM-REVIEW-BATCH-54-FINAL-24-CLAIMS-SOURCE-PASSAGE-REVIEW-2026-11-12.md` | 24 |
| **Batch 54 total** | **42** |

The separate file `M13-BATCH-53-LANE-01-CONTENT-RISK-SCREEN-2026-11-12.md` is a routing-only screen of 20 Claims and explicitly assigns zero D/E/B scores. It is not the five scored Batch 53 source-passage reports listed above. Conflating these distinct documents produces an incorrect description of the 100 Batch 53 ledger rows.

## 4. Evidence-fit score distribution

| Population | Rows | E=0 | E=1 | E=2 | E=3 |
|---|---:|---:|---:|---:|---:|
| Batches 12–43 | 459 | 10 | 152 | 201 | 96 |
| Batches 44–52 | 900 | 1 | 883 | 16 | 0 |
| Batch 53 | 100 | 0 | 100 | 0 | 0 |
| Batch 54 | 42 | 0 | 42 | 0 | 0 |
| **Total** | **1,501** | **11** | **1,177** | **217** | **96** |

The Batch 53 final 39-Claim report states that all 39 linked Evidence Use records lack reproducible claim-specific page/section/figure/table locators and therefore receive E=1 even where the external source directly supports the Claim. The Batch 53 priority 19-Claim report states the same. The Batch 54 partial 18-Claim report and final 24-Claim report likewise state that all 42 Evidence Use records lack reproducible claim-specific locators and receive E=1.

Thus, a source-passage review row and a high E score are not synonymous. In these reports, source passages were checked, but the stored Evidence Use locator trail remained insufficient for E above 1.

## 5. Correction to prior independent review

The independent review report in PR #35 (§5.5, finding F-5) correctly cautions that a scored row is not automatically a substantive review and that row depth is heterogeneous. However, its specific statement that “Batch 53 = risk-routing only” is not supported by the row-level ledger provenance.

The review cited `M13-BATCH-53-LANE-01-CONTENT-RISK-SCREEN-2026-11-12.md`, which is a separate 20-Claim routing screen. The 100 Batch 53 scored rows in the ledger originate from the five distinct `M13-CLAIM-REVIEW-BATCH-53-…-SOURCE-PASSAGE-REVIEW…` files listed in §3. Those files contain D/E/B score tables and source-passage findings. The correct conclusion is:

- Batch 53 includes 100 scored rows from source-passage review reports.
- A separate Batch 53 risk-routing screen exists and assigns zero D/E/B; it is not the source of those 100 rows.
- The 100 scored rows remain desk/source-passage assessments, not specialist approval, Human View, independent review, or release clearance.
- E=1 throughout Batch 53 because claim-specific locators are absent from the stored Evidence Use records.

The earlier review's broader caution about heterogeneous depth remains valid and should be retained. Its specific Batch 53 example must be corrected.

## 6. Disposition and limitations

1. Preserve the 1,501-row ledger as an accounting artifact, not an accepted score register.
2. Keep all seven repeated groups open for adjudication; do not select a winning score by chronology or arithmetic.
3. Classify the 459 pre-Batch-44 rows report-by-report before treating them as comparable source-passage reviews.
4. For the 1,042 rows from Batches 44–54, retain the distinction between source-passage checking and missing stored Evidence Use pinpoints; E=1 is not evidence that no external passage was consulted.
5. Do not infer that any Claim is release-cleared from this reconciliation.

No canonical Claim, Evidence Use, Source, Context, Relation or Decision record was changed. No score, batch assignment, or queue selection was changed. This report does not authorize Phase 1 or close the wider M13 audit.
