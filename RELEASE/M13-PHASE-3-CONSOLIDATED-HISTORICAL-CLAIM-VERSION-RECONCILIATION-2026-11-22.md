# M13 Phase 3 — consolidated historical Claim-version reconciliation

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Current comparison HEAD: `a1a0947ebd5de693a2db9ef509724d7f5ecdefa6`

## Final consolidated result

**All 239/239 historical Claim-version gaps are resolved. No historical Claim version remains unknown.** Of the 239 rows, 238 have exact historical/current Claim path and Blob SHA equality; the remaining row has a properly versioned current successor (Claim@2) with matching Evidence Use and Relation version updates. No same-version content-drift exception remains open.

| Control | Result |
|---|---:|
| Phase 2 historical score-row occurrences | 1,501 |
| Unique normalized Claim IDs | 1,494 |
| Original historical Claim-version gaps | 239 |
| Batch 41 exact snapshot recoveries | 94 |
| Batch 17 exact snapshot recoveries | 1 |
| Batch 21 exact snapshot recoveries | 11 |
| Batches 18–40 historical Claim-version recoveries | 133 |
| **Total historical Claim-version recoveries** | **239/239** |
| **Rows with historical Claim version known** | **1,501/1,501** |
| **Unique Claims with historical Claim version known** | **1,494/1,494** |
| Exact historical/current path + Blob SHA matches | **238** |
| Explicitly versioned current successor | **1** |
| **Unknown historical Claim versions remaining** | **0** |
| Current accepted D/E/B assessments | **0/1,494** |
| Historical score reuse authorized | **0** |

The companion CSV now contains the complete 239-row master reconciliation, joined to the Phase 2 report rows and exact historical snapshot evidence. All rows remain HISTORICAL_ONLY_NOT_ACCEPTED and NOT_AUTHORIZED for score reuse.

## Cohort accounting

- **Batch 41: 94/94.** Exact historical paths and Blob SHAs; six original identifier strings differ only by the initial CLM separator and were joined read-only using separator normalization.
- **Batch 17: 1/1.** Exact snapshot `01d9d58900fd2003c297a27ba08e60475ccdd0c5`.
- **Batch 21: 11/11.** Exact snapshot `ff5c39d1743a96e945e476910466b9a567b7daca`.
- **Batches 18–40: 133/133.** Exact report-parent snapshots and historical Claim JSON versions identified; 132 exact Blob matches at the original comparison snapshot and one subsequently corrected through an explicit versioned successor.

The complete row-level master preserves original report code/line/row, Claim ID, historical D/E/B, report path, historical/current Claim versions, historical/current paths, snapshot commit, historical/current Blob SHAs, reconciliation status, and score-reuse prohibition.

## Generator CO emergency Claim — versioned successor verified

The original exception was CLM-GENERATOR-CO-ALARM-EMERGENCY@1:

- Historical snapshot: `18d9c1ba150c5b9d4e6d8f4a5b2923cf47ac13d5`
- Historical Blob SHA: `29c7f166b28510e323f0b391f2bcc37506839ce2`
- Historical report: Batch 19, line 13, row 1; historical D/E/B 2/3/3.

The later authorized correction did not rewrite Claim@1. It created an explicit current successor:

- Current Claim@2 Blob SHA: `973ab535fd2fc681e3f9731ec88bb3b87fd184d2`
- Current Claim@2 restores the no-re-entry boundary: do not return until emergency services permit it.
- CDC Evidence Use @2 is limited to immediate fresh-air response and emergency medical assistance.
- A separate CPSC Evidence Use @1 links Claim@2 to the existing CPSC Source@1 and supports only the no-re-entry instruction.
- Cross-slice Relation @2 updates the generator Claim participant to @2 while preserving the other participant, order, roles, relation type, direction, frame and Source provenance.
- The exact authorization is recorded in M13-CORRECTION-AUTHORIZATION-GENERATOR-CO-VERSION-LINEAGE-2026-11-22.md and the separate Relation authorization.
- Regression test_generator_co_emergency_claim_has_versioned_cdc_and_cpsc_support checks Claim/EU versions, exact CDC/CPSC source references, scope separation and preservation of the emergency warning.

**Disposition:** the historical same-version content-drift defect is resolved by a properly versioned successor. Historical Claim@1 and its Blob SHA remain preserved. The current Claim is @2. This closes the version-lineage integrity exception only; it does not accept the old 2/3/3 score, assign a new score, or clear the Claim for public release.

## Non-transfer and remaining independent gates

This reconciliation proves historical Claim-version provenance only.

- Historical D/E/B values remain historical-only; no score was transferred.
- Current accepted D/E/B remains 0/1,494.
- Historical Evidence Use/Source version provenance remains a separate task, including the Batch 53–54 gaps recorded in Phase 2.
- Current source passage fit, exact locator reproducibility, source independence, specialist review, Human View/adversarial review, rights, publication and release decisions remain separate gates.
- The CO emergency Claim remains subject to high-consequence Human View and independent content/safety review despite the corrected version lineage.

No canonical record was changed by this reconciliation-document update. The authorized CO Claim/EU/Relation corrections are separately represented in their own canonical version history and exact regression tests. main remains untouched; PR #21 remains Draft/unmerged; M13 remains OPEN / NOT RELEASE-READY.
