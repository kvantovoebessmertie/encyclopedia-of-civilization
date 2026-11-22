# M13 Phase 2 → Phase 3 — historical Claim-version count reconciliation

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: reconcile the immutable Phase 2 claim-to-report provenance ledger with the completed Batch 41 Phase 3 historical Claim snapshot reconstruction.

## Result

**94/94 Batch 41 historical Claim-version gaps are now reconciled against the Phase 2 ledger. The remaining historical Claim-version gap is 145 unique Claims, all in the earlier Batch 12 / Batches 17–40 report population.**

| Measure | Phase 2 ledger snapshot | After Batch 41 Phase 3 reconciliation |
|---|---:|---:|
| Historical score-row occurrences | 1,501 | 1,501 |
| Unique normalized Claim IDs | 1,494 | 1,494 |
| Rows with historical Claim version recovered | 1,262 | 1,356 |
| Unique Claims with historical Claim version recovered | 1,255 | 1,349 |
| Rows with historical Claim version unresolved | 239 | **145** |
| Unique Claims with historical Claim version unresolved | 239 | **145** |
| Batch 41 unresolved Claim-version rows | 94 | **0** |
| Current accepted D/E/B assessments | 0 | **0** |

The 94-row Phase 3 reconciliation closes only the Batch 41 Claim-version portion of the Phase 2 gap. It does not recover historical Evidence Use or Source versions for those rows, validate current source fit, or authorize historical score reuse.

## Reproducible join

Inputs:

1. `M13-PHASE-2-CLAIM-TO-REPORT-PROVENANCE-LEDGER-2026-11-22.csv` — 1,501 score-row occurrences; 239 rows have no recovered historical Claim version.
2. `M13-PHASE-3-BATCH-41-HISTORICAL-CLAIM-VERSION-RECONCILIATION-2026-11-22.csv` — 94 Batch 41 rows marked RESOLVED as Claim@1 through exact historical/current path and blob comparison.

Join controls:

- Restricted the Phase 2 unresolved population to report codes B41.1–B41.6: 94 rows.
- Confirmed 94 unique Claim identifiers in that population and 94 unique identifiers in the Phase 3 reconciliation.
- Compared IDs using a read-only separator normalization that treats hyphen and underscore as equivalent; no stored identifier or path was modified.
- Result: **94/94 unique normalized IDs matched; zero unmatched rows; zero normalization collisions.**
- 88 identifiers matched byte-for-byte as strings. Six differ only in the initial `CLM-` versus `CLM_` separator:
  - Bioinformatics A, B and C;
  - Biomedical Engineering A, B and C.
- The Phase 3 CSV preserves the verified repository paths and blob SHAs. The original Phase 2 IDs and source report rows remain unchanged.

## Remaining 145 historical Claim-version gaps

All 94 Batch 41 gaps are removed from the unresolved count. The remaining 145 are the earlier report population:

- Batches 12 and 17–40: 159 score rows.
- 14 rows already had historical Claim-version provenance through the seven repeated groups.
- 145 rows remain without a per-Claim historical version.
- No version is inferred for those 145 rows.

This addendum does not claim that all 145 are recoverable. Each must be resolved only through an exact report header, explicit version marker, or complete historical Git snapshot/blob comparison. If the exact snapshot cannot be established, retain UNRESOLVED.

## Non-transfer and audit boundaries

- Historical D/E/B values remain historical-only.
- Historical score acceptance or transfer remains NOT AUTHORIZED.
- Current accepted D/E/B remains 0/1,494.
- The seven duplicate groups remain preserved; this count reconciliation does not adjudicate their competing rationales or select winning scores.
- Historical Evidence Use and Source version provenance remains a separate reconciliation task.
- Current passage-level source fit, exact locators, source independence, high-consequence review, specialist review, Human View, adversarial review, rights and publication gates remain separate.
- No canonical Claim, Evidence Use, Source, Assessment, Relation, risk record, or main-branch file was changed by this addendum.

## Artifact relationship

The Phase 2 ledger and CSV remain immutable records of their generated source snapshot and original 239-gap accounting. This addendum supplies the later Phase 3 reconciliation delta; it does not rewrite the historical ledger or its digest.

PR #21 remains Draft and unmerged. `main` remains untouched. M13 remains OPEN and is not CLEAN.
