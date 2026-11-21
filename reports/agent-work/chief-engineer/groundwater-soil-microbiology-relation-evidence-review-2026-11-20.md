# Groundwater / Soil Microbiology Relation — current-head evidence desk review

Date: 2026-11-20  
Inspection ref: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `302f1082f0b9de08b71553a80f59dbc9682c9a55`  
Disposition: report-only; preserve canonical records and HOLD states.

## Exact records re-fetched

- `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2`
- `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1` → exact target Relation @2.
- Groundwater endpoint: `CLM-GROUNDWATER_BASICS-A@1`, `EU-GROUNDWATER_BASICS-A@1`, `SRC-GROUNDWATER_BASICS@1`.
- Soil microbiology endpoint: `CLM-SOIL_MICROBIOLOGY_BASICS-A@1`, `EU-SOIL_MICROBIOLOGY_BASICS-A@1`, `SRC-SOIL_MICROBIOLOGY_BASICS@1`.

Endpoint Claims: groundwater occupies saturated pores and fractures in soil/rock; soil contains complex communities of microorganisms and other organisms. Both EUs link exact Claim/Source versions, but contain only generic source descriptions and no pinpoint locators. Relation roles are generic `linked_record`; the Context cycle is coherent.

## Direct official evidence for the cross-domain mechanism

The existing two endpoint sources establish the separate concepts but not the mechanism connecting them. Additional official research located during this review provides a direct bridge:

1. USGS, *Hydrologic Cycle and Interactions — Chemical Interactions of Ground Water and Surface Water*: https://pubs.usgs.gov/circ/circ1139/htdocs/natural_processes_of_ground.htm  
   The section on evolution of water chemistry states that when water infiltrates the land surface, soil microorganisms significantly affect water chemistry; microbial degradation of soil organic matter produces dissolved CO₂, which changes pH and initiates mineral-weathering reactions.
2. USGS, *The significance of microbial processes in hydrogeology and geochemistry* (2000): https://www.usgs.gov/publications/significance-microbial-processes-hydrogeology-and-geochemistry  
   The abstract states that microbial processes affect groundwater chemical composition and aquifer hydraulic properties in both contaminated and pristine systems.
3. USGS, *Bacteria and Their Effects on Ground-Water Quality*: https://mi.water.usgs.gov/h2oqual/GWBactHOWeb.html  
   Describes bacteria in soils and aquifers, microbial effects on groundwater pH/redox/dissolved oxygen/mineral constituents, and microbial transformations in groundwater.

These sources support a genuine soil–groundwater microbial/geochemical interface. The first two are especially useful for a carefully bounded relation statement; the third provides broader background but should be reviewed for age and context before being treated as a current primary source.

## Semantic assessment

<badge color="success">Strong contextual-navigation candidate</badge>

The relation is scientifically defensible as contextual navigation between soil microbiology and groundwater hydrogeochemistry. The mechanism is not merely that soil and groundwater are adjacent: microbial activity in the soil zone during infiltration changes water chemistry, and microbial activity within aquifers can further alter groundwater chemistry and aquifer properties.

Boundary cautions:
- Do not imply that all soil microbes enter groundwater, or that groundwater always contains the same microbial community as soil.
- Do not claim that microbial activity necessarily makes groundwater safe or potable; pathogens and contaminants can remain.
- Keep the distinction between soil-zone processes during infiltration and microbial processes inside the aquifer.
- Existing endpoint Claims are broad definitions; the new USGS evidence supports the cross-domain bridge, not a replacement for their separate definitions.

## Rights / evidence / authorization

This review stores source identities and concise factual paraphrases only. It does not establish reuse rights or project-wide distribution compatibility. The USGS pages and publication must be checked at item level before expressive reuse or distribution. The newly found sources are not yet canonical Source/Evidence Use records.

## Disposition and next action

- Keep Relation @2, Context @1, both Claims @1, both EUs @1, Sources @1 and affected slices HOLD.
- No Source, EU, Claim, Relation or Context version was changed.
- Recommended next step: prepare a bounded authorization proposal for adding one USGS cross-domain Source and Relation-level provenance/Evidence Use path (rather than altering generic endpoint Claims), with exact source locator(s), attribution/rights note and independent hydrogeology/microbial ecology review.
- Human View and publication/rights approval remain separate gates.
- No canonical or implementation file was changed. No CI result is claimed for this documentation-only report.
