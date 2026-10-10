# M13 Claim Audit Reconciliation — 2026-10-10

## Status
**Reconciliation in progress; Batch 41 is not authorized to start yet.** This report records confirmed report-level overlaps. It does not claim the full inventory-to-ledger reconciliation is complete.

Branch: `m13-system-wide-depth-audit-2026-10-09`
Reviewed report set: general Claim Review reports numbered 12 and 17–40, plus the separately labelled high-consequence/foundational Batch 16.
Frozen inventory denominator recorded by the baseline: 1,494 Claim-prefixed files. The baseline itself says semantic/type/registry reconciliation remains open.

## Confirmed overlaps

### 1. Batch 12 and Batch 17
Batch 12 lists:
- `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A`
- `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B`
- `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C`

Batch 17 lists those same three Claims plus `CLM-WATER-CHEMICAL-LIMIT`. Batch 17's four-row table scores the nuclear Claims again; therefore its description as four Claims reviewed cannot be interpreted as four new unique Claims relative to Batch 12. This is a cross-series overlap, not proof that the individual review notes are invalid.

Sources:
- `RELEASE/M13-CLAIM-REVIEW-BATCH-12-NUCLEAR-PHYSICS-2026-10-09.md`
- `RELEASE/M13-CLAIM-REVIEW-BATCH-17-NUCLEAR-AND-WATER-2026-10-10.md`

### 2. Batch 21 and Batch 27
The following four Claim IDs appear as scored rows in both reports:
- `CLM-WATER_TREATMENT_BASICS-A`
- `CLM-WATER_TREATMENT_BASICS-B`
- `CLM-WATER_TREATMENT_BASICS-C`
- `CLM-M5-WATER-EMERGENCY-DISINFECTION-D`

Batch 21 describes these as reviewed; Batch 27 repeats the same four rows while calling them “additional.” They must count once in the unique-Claim tally unless a documented second-review purpose is explicitly tracked separately.

Sources:
- `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md`
- `RELEASE/M13-CLAIM-REVIEW-BATCH-27-WATER-TREATMENT-2026-10-10.md`

## Arithmetic consequence (report-level only)
The 24 general reports numbered 17–40 contain exactly 156 scored table rows when counted by the explicit Claim-level result rows. Four rows in Batch 27 repeat Claim IDs already scored in Batch 21. Thus, **the maximum unique count across these 156 rows is 152 before checking any additional duplicate IDs or aliases**. This is a provisional arithmetic ceiling, not yet the accepted unique-Claim count, because every ID still must be reconciled against the frozen inventory and normalized carefully. The Batch 12/17 overlap is additionally relevant when combining all report families, but Batch 12 was not part of the 156 figure as currently recorded. Batch 16 is explicitly labelled high-consequence/foundational and must not be silently mixed into the general-series denominator.

Do not yet declare 152 as the final accepted count: the complete ledger must test every row for additional duplicate IDs, aliases/format variants, missing inventory members, and unscored Claims.

## Required next steps
1. Extract the scored Claim rows (not every textual mention) from every review report in scope.
2. Normalize IDs only for comparison while preserving exact stored IDs; inspect potential aliases instead of automatically merging them.
3. Deduplicate the scored-row ledger and report: row count, unique IDs, duplicate groups, claims absent from the frozen 1,494 inventory, and inventory Claims with no qualifying score/rationale.
4. Reconcile each candidate ID to its actual Claim JSON record and linked Evidence Use/Source records.
5. Update the batch-size decision only after the reconciliation is independently checked. Select Batch 41 as 100 previously unscored, inventory-backed Claims, with explicit exclusions for every previously scored ID.
6. Continue content review without changing content records during audit-only batches. Corrections require their own scoped change set and regression checks.
7. Keep M13 open and do not merge the PR or change `main`. CI green on an earlier SHA is not evidence of content-audit completion.

## Acceptance boundary
This report records confirmed accounting defects and the reconciliation protocol. It is not the final ledger, does not certify all previous scoring, and does not close M13.


## Additional inventory comparison — Batches 25–40

At HEAD `15c54158fb37e93369b7f3b67551a98fccfd496e`, the explicit scored-table rows in Batches 25–32 total 34, and Batches 33–40 total 63. All 97 extracted rows were compared against the 1,494 Claim JSON filenames in the recursive repository tree.

- Batches 25–32: 34/34 exact filename-ID matches.
- Batches 33–40: 54/63 exact filename-ID matches; 9 rows differ in separator style but match a filename ID after a comparison-only normalization that replaces underscores with hyphens and collapses repeated hyphens.
- The nine separator variants are the three Biostatistics IDs in Batch 38, the three Bridge Engineering IDs in Batch 39, and the three Building Science IDs in Batch 39.
- No row in these 97 extracted rows remains unmatched after that comparison-only normalization.
- This is filename reconciliation only. It does **not** authorize rewriting stored identifiers or treating the variants as aliases without inspecting the actual JSON `id` fields and references.

The extraction therefore confirms that the ledger must preserve both the exact scored-table string and the exact inventory filename, and must separately record whether the JSON record's internal identifier matches either form. The all-series unique count remains unresolved; Batch 41 remains unauthorized until the full ledger, duplicate groups, and internal-ID checks are completed.
