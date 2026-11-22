# M13 Phase 3 — consolidated historical Claim-version reconciliation

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Consolidated result

**106/106 historical Claim-version gaps reconciled. 133 unique Claims remain historically unresolved.**

| Control | Result |
|---|---:|
| Phase 2 historical score rows | 1,501 |
| Unique normalized Claim IDs | 1,494 |
| Phase 2 historical Claim-version gaps | 239 |
| Batch 41 exact snapshot recoveries | 94 |
| Batch 17 exact snapshot recoveries | 1 |
| Batch 21 exact snapshot recoveries | 11 |
| **Total recovered by Phase 3 packages** | **106** |
| Rows with historical Claim version recovered | **1,368** |
| Unique Claims with historical Claim version recovered | **1,361** |
| **Remaining unresolved Claim versions** | **133** |
| Current accepted D/E/B assessments | **0 / 1,494** |

The consolidated CSV contains 106 row-level records. Each row is joined to its original Phase 2 score-row occurrence and exact historical snapshot evidence. All 106 rows are marked `RESOLVED` and `NOT_AUTHORIZED` for historical score reuse.

## Cohort accounting

- Batch 41: 94/94. Exact historical paths and Blob SHAs; six original identifier strings differ only by the initial CLM separator and were joined read-only using separator normalization.
- Batch 17: 1/1. Exact snapshot `01d9d58900fd2003c297a27ba08e60475ccdd0c5`.
- Batch 21: 11/11. Exact snapshot `ff5c39d1743a96e945e476910466b9a567b7daca`.

All 106 historical Claim files were inspected at their exact snapshot references, parsed for canonical Claim identity and version, and compared with the current M13 branch file at the same repository path. The Batch 17 and Batch 21 rows all have exact path and Blob SHA matches. Batch 41 preserves its previously documented exact-path/blob and normalized-identifier reconciliation.

## Remaining 133

The remaining 133 unresolved unique Claims are outside the 106 recovered rows. They remain unresolved until a specific report commit or historical Git tree can establish the exact Claim version. No inference from current version, report date, current path, or nearby commits is permitted.

## Non-transfer boundary

This reconciliation proves historical Claim version only. It does not recover all historical Evidence Use/Source versions, validate source passages or locators, resolve repeated-score adjudications, establish current accepted D/E/B, or confer publication eligibility. All historical D/E/B values remain historical-only. No score reuse is authorized.

No canonical content record was changed. This consolidated artifact is noncanonical accounting evidence. `main` remains untouched; PR #21 remains Draft and unmerged; M13 remains OPEN / NOT CLEAN.
