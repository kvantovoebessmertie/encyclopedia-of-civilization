# M13 — Batch 41 historical Claim-version reconciliation

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input snapshot: `56ae3a379239eb7704d4d63c940a4e29d4aa1ca7`  
Result artifact: `M13-PHASE-3-BATCH-41-HISTORICAL-CLAIM-VERSION-RECONCILIATION-2026-11-22.csv`

## Result

**94/94 previously unresolved Batch 41 Claim-version rows now have an exact historical snapshot match.** Every reconciled row is Claim@1 at the scored-block report commit. For every row, the Claim path and Git blob SHA at the exact report commit match the corresponding current Claim snapshot. The identical blob establishes identical file content, including `record_version: "1"`.

| Scored block | Report commit | Reconciled rows |
|---|---|---:|
| 01 | `8041231bfccc5c8fba521c883256f6ddc6e89863` | 6 |
| 02 | `d5d80749fb5208259ed66ebb23785a29c4bd9609` | 14 |
| 03 | `c42885ffcfd46d831254922c04c0ec956b21307b` | 20 |
| 04 | `cd1a9e2cf2640b1a1da39af0d2710da547ef302d` | 17 |
| 05 | `14078b3994edec546f88e6d0f1181c7586611bc9` | 17 |
| 06 | `4be018cce7acb634dddc28ee73ee099522a305ac` | 20 |
| **Total** | | **94** |

## Method and controls

1. Started from the 94 rows in the Batch 41 current Claim-version crosswalk.
2. Identified the scored-block report for each Claim and used the exact commit that added that report.
3. Inspected the complete Git tree at each report commit (all six trees were complete, not truncated).
4. Located the Claim file at its actual repository path and compared the historical blob SHA to the current blob SHA.
5. Required a unique report-block assignment, a unique current record path for each blob, an exact historical path/blob match, and current version `1` before marking the row resolved.
6. Preserved filename/internal-ID separator differences; no IDs were renamed or normalized in canonical records.

## Path corrections captured in the reconciliation CSV

Six path strings in the earlier current-state crosswalk used underscores before the terminal A/B/C instead of the actual hyphenated filenames. The reconciliation CSV records the verified repository paths for:
- three Bioinformatics Claim files;
- three Biomedical Engineering Claim files.

The underlying blob SHAs were unique and matched the exact historical report-commit trees. This is a path-metadata correction only; no Claim JSON was changed.

## Scope boundary

This closes **historical Claim-version provenance only** for these 94 Batch 41 rows.

- Historical Claim version: **RESOLVED as @1** for 94/94.
- Historical D/E/B score acceptance or transfer: **NOT AUTHORIZED**.
- Current Evidence Use and Source version provenance: not resolved by this Claim-only crosswalk.
- Current E/source-fit revalidation, pinpoint locators, source independence, duplicate/overlap eligibility, specialist review, Human View, adversarial review, and final D/E/B acceptance remain separate gates.
- The six Batch 41 rows already reconstructed as historical Claim@1 / EU@1 / Source@1 for current Claim@2 are documented separately in `M13-BATCH-41-SIX-V2-CLAIM-HISTORICAL-SNAPSHOT-RECONSTRUCTION-2026-11-18.md`; they are not part of this 94-row set.

No canonical Claim, Evidence Use, Source, Assessment, Relation, or main-branch file was modified. PR #21 remains open, Draft, and unmerged. M13 is not complete.
