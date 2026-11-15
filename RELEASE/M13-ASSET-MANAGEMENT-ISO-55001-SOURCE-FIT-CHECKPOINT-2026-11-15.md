# M13 asset-management Source identity correction checkpoint

Date: 2026-11-15  
Authorization: `M13-ASSET-MANAGEMENT-ISO-55001-001`  
Basis: Packages 05 and 06, 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Confirmed defect

The Source record was labelled ISO 55000:2024 but stored the official ISO URI `https://www.iso.org/standard/83054.html`, which identifies ISO 55001:2024, *Asset management — Asset management system — Requirements*. ISO 55000:2024 is a distinct standard at `https://www.iso.org/standard/83053.html`. The defect is a Source identity/URI mismatch, not a basis to conflate the standards.

## Bounded correction

- `SRC-ASSET_MANAGEMENT_BASICS@2` now identifies ISO 55001:2024 and preserves the existing URI.
- `EU-ASSET_MANAGEMENT_BASICS-A/B/C@2` now reference Source @2 and describe the official ISO overview passages with explicit scope boundaries.
- Claim A: overview-level lifecycle/value/risk/objectives support.
- Claim B: only performance/risk/expenditure balancing is supported by the cited overview; the Claim's “opportunities” element remains unsupported.
- Claim C: overview-level support for policy, objectives, system implementation and continual improvement.
- No clause-level locator is claimed because the public landing-page preview is not the full paid standard.
- README and dedicated regression updated to preserve the identity distinction and support boundaries.

## Integrity

Claim statements and Claim types remain unchanged. After exact-head preflight identified the six stale Source @1 provenance references, the separately registered addendum `M13-SOURCE-V2-CLAIM-PROVENANCE-001` versioned only the three Claims in this slice to record version 2 and point `provenance.created_from` to Source @2. No new/deleted record, Relation, coverage count, D/E/B, risk metadata or publication approval. Slice remains nine records. `main` unchanged; PR #21 remains Draft/unmerged.

## Verification required

Run dedicated regression, Content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. This checkpoint records the correction, not successful CI or M13 closure.


## Exact-head inbound-reference migration

The first provenance-only Claim version update exposed additional stale inbound references during Content preflight. Under the separately registered addendum `M13-SOURCE-V2-INBOUND-REFERENCES-001`, the slice's Context and Scope records were versioned only to update `target_ref` to Claim @2, and its three Evidence Use records were versioned only to update `claim_ref` to Claim @2. Source @2 references, provenance, evidence descriptions, Claim statements, Context/Scope prose and all other fields were preserved. Dedicated regressions now assert the full Claim→Evidence Use/Context/Scope version lineage. This is a storage-reference migration only; it does not clear any Claim or approve publication.
