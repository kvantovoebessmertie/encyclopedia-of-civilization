# M13 Claim Audit Reconciliation Checkpoint — Batch 40 — 2026-10-10

## Purpose and scope

This checkpoint records a direct extraction check of the latest scored report, Batch 40, against the existing reconciliation protocol. It is an audit artifact only. It does not authorize Batch 41 scoring, close the full ledger, or change any content Record.

## Batch 40 extraction

Source report:
`RELEASE/M13-CLAIM-REVIEW-BATCH-40-CAUSAL-BIOLOGY-CHEMISTRY-AND-CHRONOLOGY-2026-10-10.md`

- Source report blob SHA: `48e3b72d38546992080539236a3b224b10f41377`
- Explicit Claim-level scored rows extracted from its results table: **30**
- Each extracted row has explicit D/E/B values in the 0–3 range and a rationale in the source report.
- Extracted IDs were unique within this Batch 40 table.
- Batch 40 is consistent with the already recorded aggregate of 156 scored table rows across reports 17–40 (the preceding reports account for 126 rows; Batch 40 adds 30).

The 30 extracted IDs and scores are:

| Claim ID | D | E | B |
|---|---:|---:|---:|
| `CLM-CAUSAL_INFERENCE_BASICS-A` | 2 | 2 | 3 |
| `CLM-CAUSAL_INFERENCE_BASICS-B` | 3 | 3 | 3 |
| `CLM-CAUSAL_INFERENCE_BASICS-C` | 2 | 2 | 3 |
| `CLM-CELL_BASICS-A` | 2 | 2 | 3 |
| `CLM-CELL_BASICS-B` | 2 | 3 | 3 |
| `CLM-CELL_BASICS-C` | 1 | 2 | 2 |
| `CLM-CELL_BIOLOGY_BASICS-A` | 1 | 1 | 2 |
| `CLM-CELL_BIOLOGY_BASICS-B` | 1 | 1 | 3 |
| `CLM-CELL_BIOLOGY_BASICS-C` | 1 | 1 | 3 |
| `CLM-CENTRAL_BANKING_BASICS-A` | 2 | 2 | 3 |
| `CLM-CENTRAL_BANKING_BASICS-B` | 2 | 3 | 3 |
| `CLM-CENTRAL_BANKING_BASICS-C` | 2 | 2 | 3 |
| `CLM-CERAMICS_BASICS-A` | 3 | 3 | 3 |
| `CLM-CERAMICS_BASICS-B` | 2 | 3 | 3 |
| `CLM-CERAMICS_BASICS-C` | 2 | 2 | 3 |
| `CLM-CERAMICS_BASICS-D` | 3 | 3 | 3 |
| `CLM-CHEMICAL_ENGINEERING_BASICS-A` | 2 | 2 | 2 |
| `CLM-CHEMICAL_ENGINEERING_BASICS-B` | 2 | 2 | 2 |
| `CLM-CHEMICAL_ENGINEERING_BASICS-C` | 2 | 2 | 3 |
| `CLM-CHEMICAL_REACTIONS_BASICS-A` | 1 | 2 | 2 |
| `CLM-CHEMICAL_REACTIONS_BASICS-B` | 3 | 3 | 3 |
| `CLM-CHEMICAL_REACTIONS_BASICS-C` | 2 | 3 | 3 |
| `CLM-CHEM-WATER-NO-BOIL` | 3 | 3 | 3 |
| `CLM-CHEM-WATER-NO-DRINK` | 3 | 3 | 2 |
| `CLM-CHRONOLOGY_METHODS-A` | 2 | 1 | 2 |
| `CLM-CHRONOLOGY_METHODS-B` | 3 | 2 | 3 |
| `CLM-CHRONOLOGY_METHODS-C` | 2 | 1 | 3 |
| `CLM-CIVIL_ENGINEERING_BASICS-A` | 1 | 1 | 2 |
| `CLM-CIVIL_ENGINEERING_BASICS-B` | 1 | 1 | 3 |
| `CLM-CIVIL_ENGINEERING_BASICS-C` | 1 | 1 | 3 |

## What this checkpoint does not establish

- It does not prove the 156 rows across Batches 17–40 are 156 unique Claims.
- Known overlaps remain: the nuclear Claims repeated between Batches 12 and 17, and four water-treatment/emergency-water Claims repeated between Batches 21 and 27.
- The maximum previously established unique count for the 156 rows remains 152 before any additional duplicate/alias checks.
- This checkpoint does not reconcile every scored ID against the full frozen inventory, JSON internal IDs, linked Evidence Use/Source records, or the set of unscored Claims.
- Batch 41 remains unscored and unauthorized until the global scored-row ledger and overlap gate are completed.

## Required next actions

1. Extract explicit Claim result rows from all in-scope reports into one ledger, preserving report ID, exact table ID, D/E/B values, and source report path.
2. Deduplicate only after comparison-only normalization and inspection; preserve original strings and do not silently rewrite stored IDs.
3. Reconcile all scored IDs to the frozen 1,494 Claim-file inventory and JSON internal `record_id`.
4. Independently check the ledger arithmetic and duplicate groups.
5. Only then finalize a fixed, non-overlapping 100-Claim Batch 41 candidate set and begin scoring.
6. Keep M13 open/draft/unmerged; do not change `main` or content Records in audit-only work.

## Repository boundary

This checkpoint changes only the audit documentation on the M13 branch. It does not authorize content edits, new Record types, new Relations, PR merge, or changes to protected historical baselines.
