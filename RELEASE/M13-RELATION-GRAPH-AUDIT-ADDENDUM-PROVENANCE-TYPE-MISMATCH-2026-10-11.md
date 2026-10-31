# M13 Relation Graph Audit Addendum — Provenance Semantics Recheck
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Related report: `RELEASE/M13-RELATION-GRAPH-AUDIT-2026-10-11.md`
Status: **Corrective reclassification; the earlier “confirmed type mismatch” conclusion is withdrawn. No content JSON changed.**

## Correction to the previous finding

The earlier version of this addendum called three Relation records “confirmed provenance-type mismatches” because `provenance.created_from` contains Claim IDs instead of Source IDs. That conclusion was too strong and is withdrawn.

The governing Relation standard, `STANDARD/013-RELATION.md`, §135 (“Relation provenance”), explicitly says Relation provenance may include an **assertion, direct Observation, Measurement, Claim, Source, Inference, computation, Model, reconstruction, imported relation, or Assessment**. The canonical record schema `IMPLEMENTATION/005-RECORD-SCHEMA.json` defines `provenance.created_from` as an array of generic `record_ref` values and does not constrain its targets to Source records.

Therefore, a Claim reference in Relation provenance is **not inherently invalid**. The fact that these Claim IDs also appear as participants makes the metadata worth reviewing for intent and possible redundancy, but does not establish a schema or standard violation. No correction to these Relation JSON records is justified from the prefix/type check alone.

## Records for semantic review, not confirmed defects

| Relation | `provenance.created_from` values | Same values in participants? | Current disposition |
|---|---|---|---|
| `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY` | `CLM-LABOR_ECONOMICS_BASICS-C`; `CLM-SOCIAL_POLICY_BASICS-C` | Yes | Check whether these Claim records genuinely describe the relation's provenance or merely repeat its endpoints. Not a confirmed type violation. |
| `REL-CROSS-MIGRATION-LABOR-ECONOMICS` | `CLM-MIGRATION_AND_MOBILITY_BASICS-C`; `CLM-LABOR_ECONOMICS_BASICS-C` | Yes | Check provenance intent and redundancy. Not a confirmed type violation. |
| `REL-CROSS-POLITICAL-ECONOMY-TAXATION` | `CLM-POLITICAL_ECONOMY_BASICS-B`; `CLM-TAXATION_BASICS-B` | Yes | Check provenance intent and redundancy. Not a confirmed type violation. |

Record paths:
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY.json`
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MIGRATION-LABOR-ECONOMICS.json`
- `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-POLITICAL-ECONOMY-TAXATION.json`

## Corrected disposition

1. Remove these three items from the **confirmed-defect** count.
2. Keep them in a **provenance-intent / possible redundancy** review queue until the local authoring convention for `created_from` is clarified and the actual lineage is checked.
3. Do not replace Claim IDs with guessed Source IDs. If the relations were derived from endpoint Claims, those Claims may be legitimate provenance under the Relation standard. If the field is intended to represent a different lineage dimension, record that distinction explicitly.
4. Amend the Relation audit's description of `created_from`: check that references resolve and preserve their target types, but do not require all provenance targets to be Sources unless a narrower, explicit profile requires it.
5. No Claim, Evidence Use, Source, or Relation JSON was changed.

This correction is based on the normative Relation standard and the canonical schema. It narrows the earlier report's conclusion and prevents an unsupported false-positive from being treated as a confirmed corpus error.
