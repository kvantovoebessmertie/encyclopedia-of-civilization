# M13 source-identity adjudication — duplicate CDC emergency-water Source records

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: desk-review source-identity and linkage finding; no canonical records changed; no independent reviewer or specialist certification claimed.

## 1. Findings

Two additional duplicate-URI groups in the safety-critical water domain were inspected at the canonical Source and Evidence Use record level.

### Group A — CDC emergency water page

Both Source records point to the exact same URL:

`https://www.cdc.gov/water-emergency/about/index.html`

| Source ID | Source identity | Linked Evidence Use |
|---|---|---|
| `SRC-CDC-WATER-EMERGENCY-2024` | CDC — How to Make Water Safe in an Emergency | `EU-WATER-BOILING-EFFECTIVE`, `EU-WATER-BOILING-TIME`, `EU-WATER-CHEMICAL-LIMIT` |
| `SRC-CDC-WATER-FILTER-2025` | CDC — How to Make Water Safe in an Emergency | `EU-WATER-FILTER-LIMITS` |

The two Source records describe the same CDC page, with the same identity and URI. They are one publication identity, not two independent CDC sources. The Evidence Use records should remain separate because they support different Claims; the Source catalog duplication must not create an independence count.

Scope caution: the EUs refer to sections on boiling, boiling duration and filter limitations, but the registered URI is the broad CDC emergency-water landing page. Exact page/section locators must be checked against the current page structure. If the filter guidance is actually a child page, the canonical Source should identify that child publication rather than relying on a hub URL.

### Group B — CDC emergency water storage page

Both Source records point to the exact same URL:

`https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html`

| Source ID | Source identity | Linked Evidence Use |
|---|---|---|
| `SRC-CDC-WATER-STORAGE-2025` | CDC — How to Create an Emergency Water Supply | `EU-WATER-STORAGE-CONTAINER` |
| `SRC-CDC-WATER-STORAGE-ATTRIBUTION-2025` | CDC — About Creating and Storing an Emergency Water Supply | `EU-CLAIM-SOURCE` |

The two Source records resolve to the same CDC page. Their title wording differs slightly, but the exact URI is identical. They are duplicate catalog entries for one publication identity, not independent sources.

The two Evidence Use records support different Claims (water-storage container safety and attribution/food-grade container guidance). Keep both EUs; consolidate only the Source identity if and when a versioned canonical source-ID change is authorized.

## 2. Relationship to the EPA duplicate group already reviewed

The earlier EPA adjudication found three Source IDs resolving to one EPA emergency-disinfection page. Taken together, the EPA and CDC inspections now establish four safety-critical duplicate-URI groups in the current 33-group register:
- EPA emergency disinfection: 3 Source IDs, one publication identity.
- CDC emergency-water landing page: 2 Source IDs, one publication identity.
- CDC emergency-water storage page: 2 Source IDs, one publication identity.

These are three duplicate-URI groups, not four. The total Source records in these three groups is seven.

## 3. Adjudication and required treatment

1. Count each exact URL/publication identity once when assessing source independence and corroboration.
2. Preserve distinct Evidence Use records and their Claim links; different Claims can legitimately use different passages of the same publication.
3. Do not count the duplicate Source IDs as independent sources, independent institutions, or independent corroboration.
4. For the CDC emergency-water landing page, verify whether each referenced boiling/filter passage is actually present on that page or belongs to a linked child page. Correct the Source identity/URI only under bounded authorization.
5. For the CDC storage page, add exact section locators to the two EUs only after verifying the page's current structure and the precise supporting text.
6. Preserve all original Source IDs and record history until an approved, versioned consolidation is implemented with linkage and offline regressions.

## 4. Verification boundary

- Exact URI equality: verified directly in all four canonical Source records.
- Source identity text: verified directly in all four records.
- EU-to-Claim and EU-to-Source references: verified directly in all five listed Evidence Use records.
- Exact passage/locator verification: not completed in this source-identity pass.
- D/E/B scores changed: 0.
- Canonical records changed: 0.
- Independent adjudication: not completed.

M13 remains **IN PROGRESS**. This report is a source-identity reconciliation proposal, not release clearance.
