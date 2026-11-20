# Air Quality / Power Systems Relation — current-head semantic desk review

Date: 2026-11-20  
Inspection ref: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `302f1082f0b9de08b71553a80f59dbc9682c9a55`  
Disposition: report-only; preserve canonical records and HOLD states.

## Exact records re-fetched

- `REL-CROSS-AIR-POWER-SYSTEMS@2`
- `CTX-REL-CROSS-AIR-POWER-SYSTEMS@1` → exact target Relation @2.
- Air endpoint: `CLM-AIR_QUALITY_BASICS-A@1`, `EU-AIR_QUALITY_BASICS-A@1`, `SRC-AIR_QUALITY_BASICS@1`.
- Power endpoint: `CLM-POWER_SYSTEMS_BASICS-A@1`, `EU-POWER_SYSTEMS_BASICS-A@1`, `SRC-POWER_SYSTEMS_BASICS@1`.

The Relation is undirected, with generic `linked_record` roles. The current endpoints are:
- Air: ambient-air monitoring measures pollutant concentrations at monitoring stations.
- Power: an electric power system combines generation, transmission, distribution and load.

Both endpoint EUs point to their respective exact Claim and Source versions. Their material fields are generic source descriptions, not pinpoint locators. The Relation Context cycle is coherent.

## Semantic assessment

The two Claims are independently plausible foundational facts, but the pair does not currently state or evidence a concrete cross-domain mechanism. A possible real-world connection is that air-quality monitoring infrastructure depends on electricity, and power-sector operations/emissions can affect air quality. Neither is represented by these endpoint Claims: the air Claim is about monitoring measurements, not power dependency; the power Claim is a generic system definition, not generation emissions or outage effects.

EPA's AirData documentation distinguishes monitored ambient concentrations from emissions data and lists power-sector emissions/operations as a separate data source. This confirms that air monitoring and power-sector environmental data can be related in a broader environmental-information architecture, but it does not establish the specific relation type between the current two Claims. It also cautions against conflating ambient monitoring measurements with emissions estimates.

Official EPA source checked:
- AirData Basic Information: https://www.epa.gov/outdoor-air-quality-data/airdata-basic-information
- EPA explains ambient concentrations are measured at monitoring stations and separately identifies power-sector emissions/operations/environmental data as another source category.

The NREL grid reference is represented by the canonical Source record as *The North American Electric Power System: The Grid* (https://docs.nrel.gov/docs/fy12osti/52409-4.pdf). Its stated subject supports the general grid-system Claim, not an air-quality monitoring dependency or emissions mechanism.

## Conclusion

Current evidence supports two separate domain facts, not the current cross-slice relation as a demonstrated mechanism. The relation may become defensible if re-scoped to an explicitly supported intersection, for example:
1. power-sector emissions and ambient air quality (requires an emissions-specific endpoint and suitable source); or
2. electricity dependency/continuity of monitoring stations (requires an explicit monitoring-infrastructure endpoint and source).

These are research directions only, not approved endpoint substitutions. Do not infer that power outages necessarily invalidate monitoring data or that grid generation emissions can be inferred from the current generic grid Claim.

## Disposition and next action

- Keep `REL-CROSS-AIR-POWER-SYSTEMS@2`, Context @1, both Claims @1, EUs @1, Sources @1 and affected slices HOLD.
- Do not change relation type, endpoints, provenance, Claim wording, Source/EU versions or publication states without bounded owner authorization.
- Request independent air-quality / power-systems boundary review before any endpoint proposal.
- Rights clearance and Human View remain separate gates.
- No canonical or implementation file was changed. No CI result is claimed for this documentation-only report.
