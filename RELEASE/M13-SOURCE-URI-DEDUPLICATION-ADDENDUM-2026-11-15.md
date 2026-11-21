# M13 source URI deduplication addendum — Materials Performance Group

Date: 2026-11-15
Authorization ID: M13-SOURCE-URI-DEDUPLICATION-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `320ec91c6785fb9c78027e5569c75602fadd4297`
Status: AUTHORIZED FOR ONE SOURCE DEDUPLICATION AND ONE VERSIONED EVIDENCE LINK UPDATE

## Finding

The source-fit remediation registered the same NIST Mechanical Performance Group page twice:
- `CONTENT/vertical-slices/materials-basics/records/SRC-NIST-MECHANICAL-PERFORMANCE-GROUP.json`
- `CONTENT/vertical-slices/materials-science-basics/records/SRC-NIST-MECHANICAL-PERFORMANCE.json`

The records refer to the same official page and do not represent distinct source documents. The M13 linkage audit treats reused source URIs as review candidates. Keep the single canonical Source record in `materials-science-basics`, where it already supports Materials Science B and Materials Performance D, and reuse that Source from the materials-basics Evidence Use.

## Exact authorized changes

1. Delete only:
   `CONTENT/vertical-slices/materials-basics/records/SRC-NIST-MECHANICAL-PERFORMANCE-GROUP.json`
   Exact ID: `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP`.
2. Version only:
   `CONTENT/vertical-slices/materials-basics/records/EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE.json`
   from record_version 1 to 2. Change only `record_version`, `provenance.created_from[0].record_id`, and `content.source_ref.record_id`; set both source IDs to `SRC-NIST-MECHANICAL-PERFORMANCE`, preserving source version "1". Preserve claim_ref CLM-MATERIALS_BASICS-C@1, evidence_role, material description and every other field.
3. Update only `REFERENCE/tests/test_content_materials_basics_vertical_slice.py` to assert two local Source records, 12 local records, and the exact cross-slice source reference resolving to the single canonical Source in `materials-science-basics`.
4. Update only `RELEASE/CONTENT-COVERAGE.json` actual totals to reflect one fewer Source and one fewer total record. Keep Evidence Use count, Claim count and slice count unchanged.
5. Update only `RELEASE/EDITORIAL-CORRECTION.json` to register this exact authorization and append the finding ID.
6. Add `RELEASE/M13-SOURCE-URI-DEDUPLICATION-CHECKPOINT-2026-11-15.md` documenting the change and checks.

## Exclusions

No other Source, Evidence Use, Claim, README, Relation, Context, Scope, score, risk metadata, schema, release gate, or content count may change. No D/E/B assessment, rights clearance, publication approval, main update or PR merge is authorized. M13 remains OPEN / NOT RELEASE-READY.
