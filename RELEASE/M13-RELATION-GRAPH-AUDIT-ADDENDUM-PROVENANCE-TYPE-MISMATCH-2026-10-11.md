# M13 Relation Graph Audit Addendum — Provenance Record-Type Mismatches
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Related report: `RELEASE/M13-RELATION-GRAPH-AUDIT-2026-10-11.md`
Status: audit finding; no content JSON changed.

## Finding

A second-pass review of the `provenance.created_from` column in the 64-row Relation ledger found three Relation records whose provenance pointers resolve to existing records but point to **Claim** records, not Source records. The original structural audit checked pointer existence and therefore reported these as resolving; it did not check the referenced record types. This addendum narrows that earlier “all provenance Sources resolve” conclusion: existence passes, provenance type correctness does not pass for these three records.

| Relation | Incorrect provenance record IDs | Participant record IDs | Type mismatch |
|---|---|---|---|
| `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY` | `CLM-LABOR_ECONOMICS_BASICS-C`; `CLM-SOCIAL_POLICY_BASICS-C` | Same two Claim IDs | `created_from` points to Claims |
| `REL-CROSS-MIGRATION-LABOR-ECONOMICS` | `CLM-MIGRATION_AND_MOBILITY_BASICS-C`; `CLM-LABOR_ECONOMICS_BASICS-C` | Same two Claim IDs | `created_from` points to Claims |
| `REL-CROSS-POLITICAL-ECONOMY-TAXATION` | `CLM-POLITICAL_ECONOMY_BASICS-B`; `CLM-TAXATION_BASICS-B` | Same two Claim IDs | `created_from` points to Claims |

The three exact Relation JSON paths are:
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY.json`
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MIGRATION-LABOR-ECONOMICS.json`
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-POLITICAL-ECONOMY-TAXATION.json`

In each record, the same Claim IDs appear both under `content.participants` (appropriate for the relationship endpoints) and under `provenance.created_from` (where the relation audit convention expects Source provenance). Thus this is not a missing-pointer issue; it is a provenance semantic/type issue.

## Disposition

1. Flag all three as **confirmed provenance-type mismatches**, pending authorized correction.
2. Do not infer or invent the intended Source IDs. During the authorized correction phase, inspect the two endpoint Claims' Source/Evidence Use graphs and determine which Sources actually informed the relation representation. If relation creation was based on editorial synthesis rather than source-based derivation, document that method according to the applicable provenance contract rather than substituting endpoint Claims for Sources.
3. Re-run the Relation audit with a type-aware check: every `provenance.created_from` pointer must resolve and satisfy the expected record type, not merely any existing record path.
4. A second pass then inspected `provenance.created_from` on all 64 Relation JSON files individually. Exactly these three Relations contain non-`SRC` IDs in provenance; the other 61 contain Source-prefixed provenance IDs. This closes the inventory-wide prefix/type triage for the current 64-record set, but Source record existence/type/version should still be enforced by an executable regression check.
5. No Relation or other content JSON was changed. PR #21 remains open Draft/unmerged; `main` remains protected and unchanged; M13 remains open.

## Audit accounting correction

The original Relation report's count of 64/64 records with no missing pointers and no role-cardinality errors remains a valid pointer-existence/cardinality result. It must **not** be described as 64/64 passing provenance integrity: the type-aware recheck has identified 3 provenance-type defects so far. Semantic validity of relation endpoints and whether each relation adds user value remain separate open checks.

## Second-pass verification result

All **64/64 Relation JSON files** listed by the Relation ledger were fetched and inspected for `provenance.created_from`. The three Relations above account for all six non-Source provenance references found. The other 61 records have only `SRC`-prefixed provenance IDs in the inspected field. This is a record-ID/type-prefix census, not a substitute for a schema-aware automated test that resolves each pointer and checks the target record's actual `record_type`.
