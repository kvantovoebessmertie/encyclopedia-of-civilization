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


## Internal record-ID verification — nine separator variants

After the filename comparison above, the nine variant files were opened and their JSON fields inspected directly. All nine have `record_type: "claim"`; each internal `record_id` exactly matches the underscore-form identifier in its scored table row, while the filename uses the alternate separator style.

| Report family | Internal record IDs | Provenance field |
|---|---|---|
| Batch 38 — Biostatistics | `CLM_BIOSTATISTICS_BASICS_A/B/C` | `SRC_BIOSTATISTICS_BASICS` |
| Batch 39 — Bridge Engineering | `CLM_BRIDGE_ENGINEERING_BASICS_A/B/C` | `SRC_BRIDGE_ENGINEERING_BASICS` |
| Batch 39 — Building Science | `CLM_BUILDING_SCIENCE_BASICS_A/B/C` | `SRC_BUILDING_SCIENCE_BASICS` |

This resolves the nine cases as filename-versus-internal-ID formatting differences, not missing Claim records. No record was edited, no IDs were merged, and no alias was inferred. The provenance values are recorded links only; source existence, source content, Evidence Use linkage, and evidential sufficiency still require separate verification.


## Source and Evidence Use spot-check — nine verified records

The nine Claims' three source records and nine corresponding Evidence Use records were fetched from the current branch. All three Source records exist and contain external canonical locators:
- Biostatistics: NCBI MeSH, `https://www.ncbi.nlm.nih.gov/mesh/?term=Biostatistics`
- Bridge engineering: FHWA Bridges & Structures, `https://www.fhwa.dot.gov/BRIDGE/`
- Building science: NIST Building Science, `https://www.nist.gov/building-science`

All nine Evidence Use records exist, use `evidence_role: supports`, and point to the matching internal Claim ID and Source ID. However, each Evidence Use record's material description is generic (for example, “source is used within the stated material”) and does not identify a specific passage, page, section, or mapped supporting statement. The Source records store identity and URL, not a local excerpt or pinpoint citation.

**Audit disposition:** structural linkage is present for these nine examples; substantive support has not yet been established by this check. This is a follow-up evidence-quality finding, not a conclusion that the Claims are false. The source URLs and target passages still need to be reviewed against each exact Claim. No content records were modified.


## Inventory reconciliation — Batches 17–24

The explicit scored rows in Batches 17–24 total 59. Each of the 59 scored-table IDs is unique within this eight-report subset. Filename matching found 48 exact filename-ID matches and 11 additional rows whose filenames match after separator-only normalization.

The 11 separator-format cases were then checked against their actual JSON records. All 11 have `record_type: "claim"`, and each internal `record_id` exactly matches the scored-table ID:
- Batch 17: three nuclear-physics Claims.
- Batch 20: `CLM_FOOD_SAFETY_CDC_A` and three electrical-grid Claims.
- Batch 21: `CLM_ELECTRICAL_SAFETY_NIOSH_A`.
- Batch 24: three sanitation Claims.

These are filename-format differences, not missing records or evidence that the stored IDs should be rewritten. Batch 17's three nuclear Claims still overlap Batch 12; this is a cross-report duplicate even though no ID repeats inside Batches 17–24 themselves. The 59-row count is therefore a report-row count, not 59 new unique Claims across the entire audit.

This subset's table rows include mixed separator conventions. Future ledger rows must preserve the original table ID, exact file path, and internal `record_id` as separate fields; comparison normalization must never overwrite those originals.


## Batch 41 candidate worklist — 2026-10-10

A controlled worklist of exactly 100 candidate Claim JSON paths has been committed at `RELEASE/M13-CLAIM-AUDIT-BATCH-41-WORKLIST-2026-10-10.md` (selection commit `fff08426090c1b70fa3937a835bfe2fcea0fb3fd`). The 100 candidates span 33 slice families not explicitly represented in the available scored reports for Batches 12 and 16–40. This is a candidate-selection artifact only: it is **not** a scored Batch 41 report and does not increment the accepted scored-Claim count.

Initial record-level spot-check of the first eight candidate files found `record_type: claim` and exact agreement between filename IDs and internal `record_id` for all eight. This is only an 8/100 identity check. All 100 still require internal-ID validation, explicit prior-score/alias exclusion, Evidence Use and Source linkage checks, and claim-specific D/E/B scoring before Batch 41 can be considered complete. No content records were edited.

CI was triggered by the worklist commit; at the time of this update, Reference implementation tests, Release Conformance Gate, and Offline Edition were still in progress on the new HEAD. M13 remains open and the PR remains draft/unmerged.


## Current checkpoint — 2026-10-10 13:00 UTC

### Exact-head CI verification

The prior note that CI was still running is superseded by the following completed pull-request runs for HEAD `676832f9dceb18adc966330b90cbc34b691b7798`:

- Reference implementation tests — run #3075, **success**.
- Release Conformance Gate — run #2735, **success**.
- Offline Edition — run #2567, **success**.

This is a 3/3 pass on the current audited HEAD at the time of this checkpoint; it verifies the configured workflows, not the completeness or substantive correctness of the depth audit.

### Scored-report extraction checkpoint

The explicit claim-level result tables in review reports 17–40 are being treated as source rows for a consolidated ledger, not as a unique-Claim total. Existing reconciliation establishes:

- Batches 17–40 contain 156 scored rows.
- Four rows in Batch 27 repeat rows already scored in Batch 21, so the known cross-report unique ceiling is 152 before further alias/duplicate checks.
- Batch 12 overlaps Batch 17 on three nuclear-physics Claims; Batch 16 is a separately labeled high-consequence review and must remain a separate review family unless the final ledger explicitly models that distinction.
- The report set contains mixed filename and internal-ID separator conventions. Comparison normalization is for matching only and must not overwrite the original report ID, exact file path, or internal `record_id`.

The next blocking deliverable remains the consolidated row-level ledger across every report family in scope, including exact source report/row, stored ID, matched JSON path, internal ID, duplicate/alias group, and score/rationale presence. The extraction pass is not yet independently reconciled end-to-end, so the provisional 152 figure is not accepted as the final unique count and no new Batch 41 scoring is authorized by this checkpoint.

### Protected-state verification

At this checkpoint PR #21 is still open, draft, and unmerged; its base is `e87e5bba60c9ed1101ecd4d53493c968c4760dac`, and `main` remains `203a7028e08da394fd44630fe38727be07bc8849`. No content Records were changed by this reconciliation update.
