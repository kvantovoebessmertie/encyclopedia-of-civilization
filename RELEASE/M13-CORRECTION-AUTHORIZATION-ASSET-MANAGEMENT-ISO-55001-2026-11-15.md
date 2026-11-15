# M13 bounded Source identity correction — asset management

Date: 2026-11-15  
Authorization ID: `M13-ASSET-MANAGEMENT-ISO-55001-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding

Package 05 identified a confirmed mismatch: `SRC-ASSET_MANAGEMENT_BASICS@1` is labelled ISO 55000:2024 but its URI `https://www.iso.org/standard/83054.html` resolves to ISO 55001:2024, “Asset management — Asset management system — Requirements”. ISO 55000:2024 is a distinct standard at `https://www.iso.org/standard/83053.html`.

The existing URI and all three Claims are substantively aligned to the ISO 55001:2024 overview. This correction preserves the existing URI and corrects the Source identity to the standard it actually identifies. It does not merge ISO 55000 and ISO 55001.

## Authorized exact scope

On branch `m13-system-wide-depth-audit-2026-10-09` only:
1. Version `SRC-ASSET_MANAGEMENT_BASICS` from v1 to v2, correcting only source identity to ISO 55001:2024 while preserving its URI.
2. Version the three existing Evidence Use records A/B/C from v1 to v2, updating only Source-version lineage/reference and claim-specific descriptions with source page locators and limitations.
3. Update only the asset-management slice README.
4. Strengthen only `REFERENCE/tests/test_content_asset_management_basics_vertical_slice.py` to assert exact ISO identity/URI, versioned links and evidence-scope boundaries.
5. Register this authorization ID and slice slug; add this authorization and M13 checkpoint documentation.

## Explicit exclusions

No Claim wording/version/provenance, Source addition/deletion, other slice, Context, Scope, Relation, risk metadata, D/E/B score, publication allowlist, schema, coverage count, release gate, `main`, or PR merge change is authorized. The ISO landing-page preview is not the full paid standard; no clause-level pinpoint may be invented. Claim B's “opportunities” wording is not directly established by the cited overview's stated balance of performance, risk and expenditure and remains a scope limitation requiring separate evidence or later narrowing under a separate authorization.

## Acceptance

Run the dedicated regression, Content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact changed paths, unchanged Claim wording and unchanged `main`. This correction does not clear any Claim for publication and does not close M13.
