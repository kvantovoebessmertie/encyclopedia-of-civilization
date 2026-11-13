# MVP Pilot Candidate Screening — Initial GIS candidates

Date: 2026-10-11  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **screening checkpoint only — 0 candidates approved for publication**

This screening uses canonical records on `main` at revision `203a7028e08da394fd44630fe38727be07bc8849`. It is intentionally separate from M13's provisional review notes. It does not promote, change, or certify any canonical Record. The reader prototype must continue to use synthetic fixtures until an explicit allowlist is approved.

## Candidate register

| Candidate | Exact record set | Initial decision | Gate findings / required action |
|---|---|---|---|
| GIS-A | Claim `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A@1`; Evidence Use `EU_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A@1`; Source `SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS@1` | **HOLD** | The claim's core definition is supported by a current USGS GIS educational resource, but the Source record's stored URL could not be verified as the current destination. The Evidence Use has no section/paragraph pinpoint. Confirm exact canonical source URL and locator, check all content rights/attribution on the selected page, and inspect the rendered Claim/EU/Source navigation. |
| GIS-B | Claim `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_B@1`; Evidence Use `EU_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_B@1`; Source `SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS@1` | **HOLD** | The current USGS resource supports combining geographic data/layers and describes vector features and attributes. The selected claim still needs a specific pinpoint for “descriptive attributes”; the stored Source URL, content rights/attribution, and rendered navigation remain unresolved. |
| GIS-C | Claim `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_C@1`; Evidence Use `EU_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_C@1`; Source `SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS@1` | **HOLD** | A USGS GIS dataset-review checklist supports checking precision, projection/datum, attributes, missing values, and quality constraints. The claim's full list also includes scale and suitability, which need explicit support or narrower wording. Stored Source URL, exact Evidence Use pinpoints, rights/attribution, and rendered navigation remain unresolved. |

## Evidence checked

- Canonical Claim, Evidence Use, and Source files were read from the exact `main` revision stated above.
- Current USGS GIS educational resource: https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/usgs-geographic-information-systems-gis. It describes GIS functions, vector/raster data, and combining layers. Its page notes that some content may have restrictions; this screening does **not** assume every embedded asset is public domain.
- USGS GIS dataset review checklist: https://water.usgs.gov/usgs/gis/checklist1.html. It includes checks for precision, projection, datum, attributes, missing values, and data-quality constraints.

## Gate status

| Gate | Status | Reason |
|---|---|---|
| Stable identity and required links | **HOLD** | Claim/EU/Source references exist, but the publication renderer must verify exact IDs and navigation on the actual canonical record bundle. |
| Claim-specific evidence fit | **HOLD** | Core GIS definition is supported; B/C need exact, claim-specific pinpoints and full-proposition confirmation. |
| Source identity and locator | **HOLD** | The Source record's stored URL was not verified as the current destination. |
| Rights and attribution | **UNKNOWN** | The inspected USGS page warns that some content may have restrictions; exact text/assets and intended use must be checked. |
| Applicability and uncertainty | **HOLD** | Confirm whether the three introductory claims need additional scope/limitations in the reader. |
| Human View and rendered navigation | **NOT RUN** | No real-record allowlist or rendered candidate artifact has been approved/built. |
| Exact reproducible allowlist and artifact hashes | **NOT CREATED** | Candidates are not approved. |

## Decision

- Candidates screened: **3**
- Approved for pilot: **0**
- Held pending remediation: **3**
- Synthetic fixtures remain test-only and are not candidates for public knowledge content.
- Do not add these candidates to the reader allowlist, do not change canonical JSON, and do not merge or publish based on this checkpoint alone.

## Remediation order

1. Resolve the authoritative Source URL and record the exact section/paragraph used for each Claim.
2. Verify rights/attribution for the exact text and any media intended for display; do not infer rights from the USGS domain alone.
3. Resolve any identity/linkage or alias concerns in the rendered reader and its tests.
4. Build a private preview using an explicit exact-version allowlist and inspect every displayed Claim and source link.
5. Record a Human View decision and named editorial approval before any candidate is promoted to the pilot.
