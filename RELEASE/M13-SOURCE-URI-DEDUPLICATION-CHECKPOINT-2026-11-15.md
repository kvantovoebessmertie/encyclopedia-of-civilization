# M13 source URI deduplication checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-SOURCE-URI-DEDUPLICATION-001`
Addendum: `RELEASE/M13-SOURCE-URI-DEDUPLICATION-ADDENDUM-2026-11-15.md`
HEAD before this checkpoint: `8ec07a3588c23bfc02724e229e74f7458456bc01`

## Change

Removed the duplicate Source record `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP` from `materials-basics`. The same NIST page remains represented once by `SRC-NIST-MECHANICAL-PERFORMANCE@1` in `materials-science-basics`.

Versioned `EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE` from v1 to v2, changing only:
- `record_version` 1 → 2;
- `provenance.created_from[0].record_id` to `SRC-NIST-MECHANICAL-PERFORMANCE`;
- `content.source_ref.record_id` to `SRC-NIST-MECHANICAL-PERFORMANCE`.

The claim reference remains `CLM-MATERIALS_BASICS-C@1`; the source version remains 1; evidence role, description, status, provenance method and all other fields are preserved.

The materials-basics regression now verifies that the Evidence Use resolves to the one canonical Source in the materials-science slice. The coverage file is reconciled from 4,850 to 4,849 total records and 626 to 625 Sources. Evidence Use remains 1,679, Claims 1,494, slices 483.

## Decision and verification

This removes one duplicate Source representation without changing the supported proposition or adding a new source. No Claim, Context, Scope, Relation, risk metadata or D/E/B ledger changed. No publication or release approval is implied.

The new checkpoint HEAD requires a fresh exact-head run of Content preflight, the dedicated materials-basics regression, Reference Tests, Release Conformance Gate and Offline Edition, followed by an independent tree/diff check.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged. `main` remains unchanged.
