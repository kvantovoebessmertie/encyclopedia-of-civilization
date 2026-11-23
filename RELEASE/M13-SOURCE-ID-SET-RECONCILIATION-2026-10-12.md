# M13 Source ID Set Reconciliation — 2026-10-12

Status: **count and separator-normalized set match established; literal canonical-ID reconciliation remains open**

## Snapshot and method

- Source corpus tree inspected: `c871b4e28dbc7f6bcd0c4996f2872151e6954267` (M13 branch before this documentation checkpoint).
- Static corpus audit reports **4,832 valid record files**, including **1,494 Claims**, **1,669 Evidence Use records**, and **618 Source records**.
- The M13 claim-audit worksheet contains **618 distinct Source IDs referenced by Claims' Evidence Use paths**.
- The 618 Source-record filenames and the 618 referenced Source IDs have an **exact set match after separator normalization**: uppercase each ID and remove non-alphanumeric separators. Reproducible summary for the sorted normalized set: 618 entries, serialized length 15,496 characters, rolling checksum (base 31, 32-bit) **3,453,968,189**.
- This resolves the prior **count-level** discrepancy (an older worksheet snapshot showed 617; the current artifact and source inventory both show 618) and establishes that no Source ID is missing/orphaned at the separator-normalized level.

## Remaining issue — literal IDs and filenames

The linkage audit reports **61 Source records** with separator-only filename/internal-ID alias findings. Thus, normalized set equality must **not** be reported as literal byte-for-byte ID equality. Those aliases need an explicit, reviewed canonicalization decision or versioned remediation; do not silently rewrite references or source records.

The linkage audit also reports six filename/internal-ID mismatch findings across the corpus overall; its Source-record subset contains the 61 separator-only aliases and no additional non-separator mismatch finding. The six other mismatches still require their own record-level review.

## Controls and disposition

- This is a reconciliation note, not a content correction.
- No Source, Evidence Use, Claim, or other canonical JSON was changed by this check.
- No D/E/B scores were assigned and no release/allowlist decision was made.
- The normalized match is a structural result only. It does not prove source passages support Claims, demonstrate source independence, settle licensing/attribution, or replace Human View.
- Next action: inspect the 61 alias rows and determine whether to preserve the existing IDs with explicit aliases or perform a bounded versioned migration. Validate all affected `source_ref` links and regressions before any canonical change.
