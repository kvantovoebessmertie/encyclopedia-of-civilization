# M13 Claim Audit Reconciliation Checkpoint — 2026-10-11

## Purpose

This checkpoint resolves the current accounting mismatch between report-row counts, unique Claim counts, and Batch 41 gate status. It supersedes earlier provisional arithmetic where inconsistent, but does not certify the full corpus ledger or close M13.

Branch: `m13-system-wide-depth-audit-2026-10-09`
Frozen inventory denominator: 1,494 Claim-prefixed JSON files at the recorded baseline tree.
No content Claim, Evidence Use, Source, or Relation records were modified.

## Reconciled scored-report arithmetic

The explicit scored Claim rows in general review reports 17–40 total **156 rows**. The row totals by report were previously extracted and rechecked against the report-level checkpoints:
- Batches 17–24: 59 rows.
- Batches 25–32: 34 rows.
- Batches 33–40: 63 rows.
- Total Batches 17–40: 156 rows.

Confirmed report-level duplicates:
1. Batch 21 and Batch 27 repeat four scored IDs:
   - `CLM-WATER_TREATMENT_BASICS-A`
   - `CLM-WATER_TREATMENT_BASICS-B`
   - `CLM-WATER_TREATMENT_BASICS-C`
   - `CLM-M5-WATER-EMERGENCY-DISINFECTION-D`
2. Batch 12 and Batch 17 repeat three nuclear-physics IDs:
   - `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A`
   - `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B`
   - `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C`

Therefore:
- Batches 17–40: 156 rows minus 4 confirmed repeated rows = **152 provisionally unique Claim IDs**.
- Adding Batch 12 contributes 3 rows, all already represented in Batch 17; the combined reports 12 and 17–40 still represent **152 provisionally unique Claim IDs**, not 159.
- The earlier “156 scored Claims / 1,338 remaining” arithmetic in the batch-size decision counts report rows as unique Claims and is not valid as a unique-Claim denominator calculation.
- Provisional arithmetic against the frozen 1,494 denominator is **1,342 Claims not yet represented by a unique scored row**, before final inventory-to-ledger validation and any separately modelled review overlays.

These are report-ID accounting results, not a claim that all prior scores or evidence judgments are substantively correct.

## Filename and internal-ID reconciliation limits

Previously recorded checks establish:
- Batches 17–24: all 59 report IDs match a Claim filename exactly or after comparison-only separator normalization; 11 separator variants were inspected and each internal JSON `record_id` matches the original report-table ID.
- Batches 25–40: all 97 report IDs match a Claim filename exactly or after comparison-only separator normalization; nine separator variants were inspected and each internal JSON `record_id` matches the underscore-form report ID.
- Stored IDs and paths must remain unchanged. Normalization is comparison-only.
- The above does **not** mean every exact-filename-match record across all 156 rows has had its internal `record_id`, Evidence Use links, and Source links individually inspected. The full row-level ledger and all-record linkage audit remain open.
- Batch 16 remains a separately labelled high-consequence/foundational review overlay and must not silently be added to the general census denominator.

## Batch 41 gate — corrected interpretation

Batch 41 has a 100-candidate worklist across 33 slice families. Its identity checkpoint reports:
- 100/100 paths opened and checked as `record_type: claim`;
- 91 exact filename/internal-ID matches;
- 9 separator-only filename/internal-ID variants;
- no content identifiers were rewritten.

The first-pass prior-report text overlap scan found no exact or separator-insensitive IDs from the candidate worklist in the inspected reports for Batches 12 and 16–40. This is a report-text overlap pass, not a semantic-duplicate proof.

**Gate status:** Batch 41 may continue diagnostic identity, overlap, and evidence-linkage work. It remains **not authorized for final D/E/B scoring or completion** until candidate overlap/exclusion and claim-specific source-support checks are documented. The evidence-linkage triage has only sampled five slices and found recurring generic Evidence Use descriptions without pinpoint locators. No candidate should be scored merely because its references resolve or its `evidence_role` is `supports`.

## Required next actions

1. Build and independently verify the consolidated row-level ledger, preserving report ID, exact table ID, exact file path, internal `record_id`, D/E/B scores, rationale/disposition, and duplicate group.
2. Complete internal-ID and Claim → Evidence Use → Source checks for all prior scored rows; resolve any further duplicate, alias, or inventory mismatch.
3. Finish the Batch 41 prior-score exclusion and claim-specific source-fit gate, replacing any disqualified candidate while retaining 100 eligible unique candidates.
4. Only then score Batch 41, with per-Claim D/E/B values and rationales.
5. Keep M13 open; do not merge PR #21, change `main`, or edit content records during audit-only work.

## Protected-state boundary

At the time of the current verification, PR #21 remains open, draft, and unmerged; `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`. CI success is a code/workflow signal, not evidence that the corpus audit is complete.
