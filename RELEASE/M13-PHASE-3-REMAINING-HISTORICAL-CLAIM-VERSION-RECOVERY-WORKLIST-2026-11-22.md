# M13 — remaining historical Claim-version recovery worklist

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Worklist status

**133 unique Claims remain unresolved for historical Claim-version recovery.** This is the exact residual population after joining the Phase 2 ledger to the consolidated Phase 3 recovery CSV.

| Control | Result |
|---|---:|
| Phase 2 historical score rows | 1,501 |
| Phase 2 unique normalized Claim IDs | 1,494 |
| Original unresolved rows | 239 |
| Phase 3 exact historical recoveries | 106 |
| Remaining unresolved rows | **133** |
| Remaining unresolved unique Claims | **133** |
| Current accepted D/E/B assessments | **0 / 1,494** |

## Remaining rows by report batch

| Report | Unresolved Claims |
|---|---:|
| B18 | 3 |
| B19 | 7 |
| B20 | 15 |
| B22 | 7 |
| B23 | 4 |
| B24 | 4 |
| B25 | 7 |
| B26 | 4 |
| B28 | 3 |
| B29 | 6 |
| B30 | 4 |
| B31 | 3 |
| B32 | 3 |
| B33 | 3 |
| B34 | 3 |
| B35 | 3 |
| B36 | 3 |
| B37 | 3 |
| B38 | 3 |
| B39 | 15 |
| B40 | 30 |

The CSV companion is the row-level execution queue. It preserves original Phase 2 report codes, line numbers, Claim IDs, historical D/E/B values and duplicate-group membership. Historical scores remain marked `HISTORICAL_ONLY_NOT_ACCEPTED`.

## Recovery rule

For each row, recover a historical Claim version only when one of the following is available:

1. the exact report body explicitly identifies Claim@version;
2. the exact historical report commit/tree is established and the Claim JSON at that snapshot is inspected;
3. a separately documented exact Git snapshot reconstruction proves the historical path, record version and Blob SHA.

Then compare the historical Claim path and Blob SHA with the current M13 branch record. A current version match alone is not sufficient. If the exact historical snapshot cannot be established, leave the row UNRESOLVED.

The queue intentionally does not guess versions from current records, report dates, later snapshots, file paths, or neighboring batch commits.

## Non-transfer boundary

Historical D/E/B values are not accepted or transferred. The worklist does not resolve Evidence Use/Source historical versions, source passage fit, source independence, specialist review, Human View, rights or release status. The seven duplicate groups remain separately preserved and unadjudicated where indicated by the repeated-assessment report.

No canonical content was changed. `main` remains untouched; PR #21 remains Draft and unmerged. M13 remains OPEN / NOT CLEAN.
