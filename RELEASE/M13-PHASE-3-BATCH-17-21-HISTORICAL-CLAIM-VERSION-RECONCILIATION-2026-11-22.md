# M13 Phase 3 — Batch 17 and Batch 21 historical Claim-version recovery

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Result

**12/12 additional historical Claim versions recovered by exact historical Git snapshots and current Blob SHA comparison.**

- Batch 17: 1/1.
- Batch 21: 11/11.
- All 12 historical records are Claim@1.
- All 12 historical file paths match their current paths.
- All 12 historical Blob SHAs match the current Blob SHAs byte-for-byte.
- No separator normalization was required for this cohort.
- Historical score reuse remains NOT AUTHORIZED.

## Exact historical snapshots

| Cohort | Exact snapshot commit | Scored report |
|---|---|---|
| Batch 17 | `01d9d58900fd2003c297a27ba08e60475ccdd0c5` | `RELEASE/M13-CLAIM-REVIEW-BATCH-17-NUCLEAR-AND-WATER-2026-10-10.md` |
| Batch 21 | `ff5c39d1743a96e945e476910466b9a567b7daca` | `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` |

The report files were fetched at their exact snapshot commits and the scored Claim IDs were confirmed in the report bodies. Each corresponding Claim JSON was fetched at the same commit, parsed for `record_id`, `record_version` and `record_type`, and its Git Blob SHA compared with the current M13 branch file at the same path.

## Reconciliation accounting

The Phase 2 provenance ledger contains 1,501 historical score-row occurrences and 1,494 unique normalized Claim IDs. It marked 239 rows as lacking a recovered historical Claim version. The earlier Batch 41 reconciliation resolved 94 of those rows, leaving 145.

This package resolves 12 additional unique rows:

| Measure | Before this package | After this package |
|---|---:|---:|
| Historical score rows | 1,501 | 1,501 |
| Unique normalized Claim IDs | 1,494 | 1,494 |
| Rows with historical Claim version recovered | 1,356 | **1,368** |
| Unique Claims with historical Claim version recovered | 1,349 | **1,361** |
| Rows with historical Claim version unresolved | 145 | **133** |
| Unique Claims with historical Claim version unresolved | 145 | **133** |
| Current accepted D/E/B assessments | 0 | **0** |

The 133 remaining unresolved rows are outside the two snapshot cohorts recovered here. No version is inferred for them.

## Row-level evidence

The CSV companion `M13-PHASE-3-BATCH-17-21-HISTORICAL-CLAIM-VERSION-RECONCILIATION-2026-11-22.csv` contains one row per recovered Claim and records:

- exact report path and report line;
- original Claim ID as written in the report;
- historical Claim version;
- historical and current Claim paths;
- exact snapshot commit;
- historical and current Git Blob SHA;
- snapshot relation and score-reuse status.

Every row is `EXACT_PATH_AND_BLOB_MATCH`, `RESOLVED`, `NOT_AUTHORIZED`.

## Important separation

This recovery establishes the historical Claim version only. It does not establish historical Evidence Use or Source versions, passage-level source fit, currentness, source independence, rights, specialist review, Human View, or release eligibility. No historical D/E/B score is transferred into a current Assessment.

No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was modified. This package adds only a noncanonical reconciliation report and its CSV companion. `main` remains untouched; PR #21 remains Draft and unmerged. M13 remains OPEN / NOT CLEAN.
