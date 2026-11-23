# M13 Phase 2 → Phase 3 — final historical Claim-version count reconciliation

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Final result

**The original 239/239 historical Claim-version gaps are now resolved. No historical Claim version remains unknown across the 1,501 scored-report rows / 1,494 unique Claims.**

| Measure | Phase 2 baseline | Final Phase 3 result |
|---|---:|---:|
| Historical score-row occurrences | 1,501 | 1,501 |
| Unique normalized Claim IDs | 1,494 | 1,494 |
| Rows with historical Claim version recovered | 1,262 | **1,501** |
| Unique Claims with historical Claim version recovered | 1,255 | **1,494** |
| Rows with historical Claim version unresolved | 239 | **0** |
| Unique Claims with historical Claim version unresolved | 239 | **0** |
| Current accepted D/E/B assessments | 0 | **0** |

## Phase 3 recovery tranches

| Tranche | Rows resolved | Evidence basis |
|---|---:|---|
| Batch 41 | 94 | Exact historical snapshots, paths and Blob SHA comparison |
| Batch 17 | 1 | Exact snapshot `01d9d58900fd2003c297a27ba08e60475ccdd0c5` |
| Batch 21 | 11 | Exact snapshot `ff5c39d1743a96e945e476910466b9a567b7daca` |
| Batches 18–40 | 133 | Exact report-introduction commits, first-parent snapshots and Claim JSON inspection |
| **Total** | **239** | **Complete** |

The final 239-row master crosswalk joins every recovered Claim version to the immutable Phase 2 report row. All 239 historical version labels are identified as Claim@1. Current Claim lineage is exact for 238 rows; the remaining Generator CO row has a documented current Claim@2 successor.

## Final Blob and lineage disposition

- 238/239 rows have exact historical/current path and Blob SHA equality.
- 1/239 row is a versioned successor, not a same-version mutation: Generator CO Emergency historical Claim@1 is preserved; current Claim@2 was created under the explicit M13-GENERATOR-CO-VERSION-LINEAGE-002 authorization, with CDC EU@2 and a separate CPSC EU@1; cross-slice Relation@2 was separately authorized and updated to reference Claim@2.
- The former same-version content-drift integrity HOLD is therefore closed as a version-lineage issue. The high-consequence safety/Human View review remains open.
- 0 unresolved historical Claim-version labels remain.
- 0 historical scores are authorized for reuse or transfer.
- Current accepted D/E/B remains 0/1,494.

## Reproducibility and artifact relationship

Inputs and row-level evidence:
1. Immutable Phase 2 Claim-to-report provenance ledger and CSV (1,501 score-row occurrences).
2. Batch 41 94-row historical snapshot reconciliation.
3. Batch 17/21 12-row historical snapshot reconciliation.
4. Batches 18–40 four-cohort historical snapshot crosswalks (133 rows).
5. Final 239-row consolidated master crosswalk: M13-PHASE-3-CONSOLIDATED-HISTORICAL-CLAIM-VERSION-RECONCILIATION-2026-11-22.csv.

The Phase 2 source ledger and its original digests remain unchanged. This Phase 2→3 document is the final count/disposition addendum; it does not rewrite historical reports or canonical records.

## Non-transfer and protected boundaries

- Historical D/E/B values remain historical-only; no scores were transferred.
- Current D/E/B assessment fields remain blank for all 1,494 Claims.
- Historical Evidence Use and Source version recovery remains a separate reconciliation task.
- Passage support, locator reproducibility, source independence, specialist/Human View/adversarial review, rights and publication/release gates remain separate.
- No canonical content was changed by this count reconciliation. The separately authorized CO version-lineage and Relation corrections remain preserved in canonical Git history.
- main remains untouched; PR #21 remains Draft/unmerged; M13 remains OPEN / NOT RELEASE-READY.
