# M13 bounded provenance-reference addendum — Source v2 storage migration

Date: 2026-11-15  
Authorization ID: `M13-SOURCE-V2-CLAIM-PROVENANCE-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Confirmed preflight defect

The exact-head Content preflight on `c142df34e756869d36fb5e5d2b3951f3792213a3` reports six verified `VAL-L3-REFERENCE-VERSION` errors. The six existing Claim records in the two bounded corrections still declare `provenance.created_from` Source version 1, while the storage resolver retains only the corrected Source version 2:

- `CLM-ASSET_MANAGEMENT_BASICS-A/B/C` → `SRC-ASSET_MANAGEMENT_BASICS@2`
- `CLM-BEHAVIORAL_BIOLOGY_BASICS-A/B/C` → `SRC-BEHAVIORAL_BIOLOGY_BASICS@2`

This is a provenance-version reference defect caused by the versioned Source corrections, not a defect in the Claim statements.

## Exact authorized scope

On the M13 branch only:

1. Version each of the six named Claim records from record version 1 to record version 2.
2. Change only the single `provenance.created_from[0].version` value from `1` to `2`, retaining the exact Source record ID and provenance method.
3. Add regression assertions to the existing asset-management and behavioural-biology slice tests that all three Claims in each slice point to the corresponding Source @2.
4. Add this addendum and a verification checkpoint.

## Explicit exclusions

No Claim statement, Claim type, Source identity/content, Evidence Use, Context, Scope, Relation, risk metadata, D/E/B, publication status, coverage count, other slice, schema, `main`, PR state or merge is authorized. This is a provenance-reference-only version bump. It does not establish evidence sufficiency or publication readiness.

## Acceptance

Content preflight, both dedicated slice regressions, full Reference Tests, Release Conformance Gate and Offline Edition must all pass on one identical exact HEAD. Preserve PR #21 as Draft/unmerged and `main` unchanged.
