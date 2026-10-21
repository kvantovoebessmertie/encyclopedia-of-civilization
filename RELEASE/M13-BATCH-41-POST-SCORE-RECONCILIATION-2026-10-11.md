# M13 Batch 41 — Post-Score Reconciliation Checkpoint
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **provisional reconciliation; Batch 41 and M13 remain open**

## Purpose and evidence base

This checkpoint reconciles the six existing Batch 41 scored-block reports (#1–100) against the Batch 41 linkage reconciliation report. It is a cross-report accounting pass, not a fresh independent scientific re-score, not semantic duplicate adjudication, and not authorization to edit Claim/Evidence Use/Source/Relation JSON.

Reports checked:
- `M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-01` through `-06` (all dated 2026-10-11).
- `M13-BATCH-41-LINKAGE-RECONCILIATION-2026-10-11.md`.
- Existing Batch 41 agricultural-engineering/bioinformatics linkage addendum.
- `M13-CLAIM-AUDIT-RECONCILIATION-CHECKPOINT-2026-10-11.md`.

## 1. Scored-block accounting

The six score tables contain **100 rows covering candidate numbers 1–100 exactly once**. This resolves the local report-row coverage question only; it does not prove the 100 candidates are all semantically unique or eligible after the complete corpus-ledger exclusion pass.

Score distribution carried from the authored reports:

| Dimension | Score 0 | Score 1 | Score 2 | Score 3 | Total |
|---|---:|---:|---:|---:|---:|
| D — explanatory depth | 0 | 11 | 73 | 16 | 100 |
| E — claim-specific evidence fit | 10 | 9 | 47 | 34 | 100 |
| B — boundary discipline | 0 | 0 | 9 | 91 | 100 |

The E=0 rows are:
- #32 `CLM-ANTHROPOLOGY_BASICS-A`
- #33 `CLM-ANTHROPOLOGY_BASICS-B`
- #34 `CLM-ANTHROPOLOGY_BASICS-C`
- #42 `CLM-ARCHITECTURE_BASICS-B`
- #43 `CLM-ARCHITECTURE_BASICS-C`
- #45 `CLM-ARCHIVAL_DESCRIPTION_BASICS-B`
- #76 `CLM-BEHAVIORAL_BIOLOGY_BASICS-C`
- #80 `CLM-BIOCHEMISTRY_BASICS-A`
- #81 `CLM-BIOCHEMISTRY_BASICS-B`
- #82 `CLM-BIOCHEMISTRY_BASICS-C`

The E=1 rows are:
- #5 `CLM-ACOUSTICS_BASICS-B`
- #10 `CLM-AGRICULTURAL_ENGINEERING_BASICS-A` (separator variant recorded in the report)
- #12 `CLM-AGRICULTURAL_ENGINEERING_BASICS-C` (separator variant recorded in the report)
- #23 `CLM-ANALYTICAL_CHEMISTRY_BASICS-A`
- #28 `CLM-ANATOMY_BASICS-C`
- #46 `CLM-ARCHIVAL_DESCRIPTION_BASICS-C`
- #62 `CLM-ASTRONOMY_OBSERVATION_BASICS-A`
- #85 `CLM-BIODIVERSITY_BASICS-C`
- #97 `CLM-CARTOGRAPHY-C`

These 19 rows form the first priority for substantive evidence-fit resolution. E=0 does not mean the Claim is necessarily false; the authored reports characterize these mostly as methodology/editorial propositions unsupported by the current subject-matter source. Decide claim type, scope, source fit, and whether to retain, narrow, or move to editorial guidance only during an authorized correction phase.

## 2. Linkage results and remaining source-traceability work

The separate linkage report records:
- **100/100 primary Claim → Evidence Use → Source pointer chains structurally pass**.
- All **15 additional Evidence Use records** across the 33 candidate slices resolve to candidate Claims and Source records.
- **44 unique Source records** were checked for identity/URI metadata.
- One confirmed Source identity/URI mismatch: `SRC-ASSET_MANAGEMENT_BASICS` labels ISO 55000:2024 while its URI points to ISO 55001:2024.
- The linkage table has 49 generic Evidence Use descriptions and 52 rows where pinpoint locator specificity remains unverified. These counts can overlap and are not counts of unique defective Claims.
- 11 distinct additional Source IDs are potential corroboration sources, not proof of independent corroboration.

Structural pointer correctness is not substantive support. Claim-specific passage coverage, locator precision, source independence, and date/jurisdiction suitability remain open.

## 3. Eligibility gate and status correction

The earlier `M13-CLAIM-AUDIT-RECONCILIATION-CHECKPOINT-2026-10-11.md` said Batch 41 could continue diagnostic work but was not yet authorized for final scoring until the prior-score exclusion and claim-specific source-fit gate were documented. Six scored-block reports were subsequently authored. To avoid treating this sequence as if the gate had been satisfied retroactively, **all 100 D/E/B rows are treated as provisional scored rows pending explicit gate reconciliation**.

The existing prior-report overlap scan is an exact/separator-normalized report-text check, not semantic duplicate proof. The 100 rows must still be reconciled against the consolidated inventory-wide ledger before Batch 41 is marked final.

## 4. Ordered next actions

1. Resolve and document the 19 E=0/E=1 cases against actual source passages and the intended Claim type/scope; retain every unresolved case explicitly.
2. Correct the `SRC-ASSET_MANAGEMENT_BASICS` identity/URI discrepancy only after the authorized correction phase and direct verification of the intended ISO source.
3. Close generic Evidence Use descriptions and pinpoint locators claim by claim; do not infer that a generic description is adequate because pointers resolve.
4. Complete the all-corpus row-level ledger and prior-score/semantic-overlap exclusion; confirm the 100 Batch 41 candidates remain eligible and unique.
5. Reconcile any resulting D/E/B changes with all duplicate groups, then run independent review, authorized corrections, regression tests, and exact-HEAD CI/tree/PR/base/main verification.

## Protected-state boundary

No content JSON was changed in this checkpoint. Do not change `main`, merge or close PR #21, or declare M13 CLEAN. PR #21 remains draft/open/unmerged per the latest metadata check; M13 remains in progress.
