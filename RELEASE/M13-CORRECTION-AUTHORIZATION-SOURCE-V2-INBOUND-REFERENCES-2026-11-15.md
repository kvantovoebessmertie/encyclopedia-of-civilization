# M13 bounded inbound-reference migration addendum — Source v2 Claim provenance

Date: 2026-11-15  
Authorization ID: `M13-SOURCE-V2-INBOUND-REFERENCES-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Confirmed preflight findings

After the six Claims were versioned to update only their `provenance.created_from` Source reference, exact-head Content preflight identified ten additional stale inbound references to Claim @1:

- Asset management: `CTX-ASSET_MANAGEMENT_BASICS.target_ref`, `SCP-ASSET_MANAGEMENT_BASICS.target_ref`, and `EU-ASSET_MANAGEMENT_BASICS-A/B/C.content.claim_ref`.
- Behavioural biology: `CTX-BEHAVIORAL_BIOLOGY_BASICS.target_ref`, `SCP-BEHAVIORAL_BIOLOGY_BASICS.target_ref`, and `EU-BEHAVIORAL_BIOLOGY_BASICS-A/B/C.content.claim_ref`.

The storage resolver retains only the latest record version. These references must therefore follow the six version-2 Claims.

## Exact authorized scope

On the M13 branch only, version these ten exact existing records and change only the listed reference fields:

- Asset management:
  - `CTX-ASSET_MANAGEMENT_BASICS` v1→v2: `content.target_ref` → `CLM-ASSET_MANAGEMENT_BASICS-A@2`.
  - `SCP-ASSET_MANAGEMENT_BASICS` v1→v2: `content.target_ref` → `CLM-ASSET_MANAGEMENT_BASICS-A@2`.
  - `EU-ASSET_MANAGEMENT_BASICS-A/B/C` v2→v3: each `content.claim_ref.version` → `2`; preserve claim IDs, Source @2 refs, provenance, evidence descriptions and all other content.
- Behavioural biology:
  - `CTX-BEHAVIORAL_BIOLOGY_BASICS` v1→v2: `content.target_ref` → `CLM-BEHAVIORAL_BIOLOGY_BASICS-A@2`.
  - `SCP-BEHAVIORAL_BIOLOGY_BASICS` v1→v2: `content.target_ref` → `CLM-BEHAVIORAL_BIOLOGY_BASICS-A@2`.
  - `EU-BEHAVIORAL_BIOLOGY_BASICS-A/B/C` v2→v3: each `content.claim_ref.version` → `2`; preserve claim IDs, Source @2 refs, provenance, evidence descriptions and all other content.

Add regression assertions to the two existing slice tests verifying every Context, Scope and Evidence Use inbound reference resolves to the exact Claim @2.

## Explicit exclusions

No Claim statement/type, Source, Evidence Use description, Evidence Use Source reference, Context/Scope prose, Relation, risk metadata, D/E/B, rights state, publication approval, coverage count, other slice, schema, `main`, PR state or merge is authorized. This is a reference-only storage-version migration.

## Acceptance

Content preflight, both dedicated regressions, full Reference Tests, Release Conformance Gate and Offline Edition must pass on one identical exact HEAD. Keep PR #21 Draft/unmerged and `main` unchanged.
