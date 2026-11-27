# Domain audit — hydrology, meteorology, oceanography
Date: 2026-11-19
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`
PR: #22 — `mvp-public-contribution-design-2026-10-11`
Reviewed baseline: `6ec981a667c9bf76ab81c9dc6bc8cb32652370a7`
Status: content/evidence screen; no publication approval.

## Scope and method

Inspected the exact Source, Claim A/B/C, Evidence Use A/B/C, Context and Scope JSON records in all three slices at the reviewed commit. Checked the live official source pages and their relevant passages. Checked the existing hydrology cross-slice relation. This is a record-level source/content audit, not a rewrite or release decision.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was changed. No record was promoted to INCLUDE. No allowlist or publication state was changed. No change was made to `main`.

## 1. Hydrology basics — HOLD pending Evidence Use precision

Dependency closure:
- `SRC-HYDROLOGY_BASICS@1`
- `CLM-HYDROLOGY_BASICS-A/B/C@1`
- `EU-HYDROLOGY_BASICS-A/B/C@1`
- `CTX-HYDROLOGY_BASICS@1`
- `SCP-HYDROLOGY_BASICS@1`

Source: USGS Water Science School, “What is Hydrology?”
https://www.usgs.gov/water-science-school/science/what-hydrology

Findings:
- Claim A (“Гидрология охватывает возникновение, распределение, движение и свойства вод Земли.”) is directly supported by the USGS definition of hydrology as the science of occurrence, distribution, movement and properties of Earth's waters.
- Claim B (movement between surface, groundwater and atmosphere) is supported by the USGS hydrologic-cycle description: water moves from the surface to the atmosphere and back; it can flow to rivers, infiltrate/percolate into groundwater, and return through springs, seepage and transpiration.
- Claim C (runoff, infiltration, evaporation and transpiration pathways) is directly supported by the USGS pathways discussion and its list of transport processes.
- All three EUs point to the correct Claim and Source IDs, but each Evidence Use contains only the same generic sentence. None identifies the definition, hydrologic-cycle passage or pathway/transport-process passage. The source fit is good; the Evidence Use is not yet auditable at claim-level granularity.
- Context and Scope both target Claim A only. Their introductory/non-exhaustive boundary is suitable for the slice, but this audit does not treat those records as separately targeted Context/Scope for Claims B/C.

Decision: **HOLD — strong direct source fit; add claim-specific source locators and passage descriptions through an authorized, versioned EU correction.** Do not rewrite the Claims merely to compensate for generic EUs.

## 2. Meteorology basics — HOLD pending Evidence Use precision

Dependency closure:
- `SRC-METEOROLOGY_BASICS@1`
- `CLM-METEOROLOGY_BASICS-A/B/C@1`
- `EU-METEOROLOGY_BASICS-A/B/C@1`
- `CTX-METEOROLOGY_BASICS@1`
- `SCP-METEOROLOGY_BASICS@1`

Sources inspected:
- NOAA, “Weather and atmosphere”: https://www.noaa.gov/education/resource-collections/weather-atmosphere
- NOAA, “Weather observations”: https://www.noaa.gov/education/resource-collections/weather-atmosphere/weather-observations

Findings:
- Claim A (weather as atmospheric state at a place and time) is directly supported by the “Weather and atmosphere” definition.
- Claim B (temperature, pressure, humidity and wind as basic meteorological quantities) is directly supported by NOAA “Weather observations”, which names temperature, humidity, precipitation, air pressure, wind speed and wind direction as key atmospheric observations.
- Claim C (observations and models used jointly for weather analysis/forecasting) is directly supported by NOAA “Weather observations”: observations are uploaded into computer models, and meteorologists combine large-scale forecasts with local observations and knowledge of local weather patterns.
- All three EUs correctly reference their respective Claims and the slice Source ID, but retain generic descriptions with no pinpoint. The current Source URL is the parent NOAA collection page; B/C need the specific “Weather observations” child-page locator recorded explicitly in Evidence Use.
- Context and Scope target Claim A only; their basic educational boundary is appropriate for that target.

Decision: **HOLD — all three propositions have direct authoritative support; record precise NOAA page/section locators in each EU through authorized, versioned correction.** No substantive Claim rewrite is indicated by this screen.

## 3. Oceanography basics — HOLD; Claim content/type defect

Dependency closure:
- `SRC-OCEANOGRAPHY_BASICS@1`
- `CLM-OCEANOGRAPHY_BASICS-A/B/C@1`
- `EU-OCEANOGRAPHY_BASICS-A/B/C@1`
- `CTX-OCEANOGRAPHY_BASICS@1`
- `SCP-OCEANOGRAPHY_BASICS@1`

Current Source: NOAA Ocean Exploration homepage
https://oceanexplorer.noaa.gov/

Findings:
- Claim A (“Срез oceanography-basics вводит базовые понятия…”) describes the intended purpose of a slice; it is editorial metadata, not a testable oceanography proposition.
- Claim B (“Интерпретация сведений… зависит от источника, контекста и границ применимости…”) is a general epistemic/editorial rule, not a domain-specific oceanography fact.
- Claim C (“Базовое знание… не заменяет специализированную проверку…”) is a scope/competence disclaimer, not a scientific proposition.
- All three are currently typed as `documented_fact` and linked to the NOAA Ocean Exploration homepage. That homepage describes the NOAA exploration programme and public engagement; it does not substantiate these three statements as oceanographic facts. The generic EU descriptions do not repair the content-type/source mismatch.
- Context and Scope target Claim A and provide a useful introductory/specialized-use boundary, but they cannot convert editorial descriptions into scientific Claims.
- Better authoritative NOAA material exists for future substantive Claims: NOAA’s definition of oceanography in its nautical-charts glossary covers the ocean’s physical, chemical, biological and geological properties and interactions; NOAA Ocean Exploration’s “What causes ocean currents?” and CTD materials provide concrete, bounded propositions about currents, temperature, salinity and depth. These are candidate sources only, not retroactive support for the current Claims.

Decision: **HOLD — all three Claims require owner/editor-authorized replacement with substantive, falsifiable oceanography propositions and corresponding claim-specific Evidence Use.** Do not make a cosmetic EU locator change while leaving the current Claim type/content defect intact.

## 4. Cross-slice relations and non-duplication

The existing `REL-M3-WATER-RESOURCES-HYDROLOGY@1` relation is present and links `CLM_WATER_RESOURCES_BASICS_B@1` with `CLM-HYDROLOGY_BASICS-A@1`. It is preserved; no duplicate hydrology/water-resources relation is proposed.

No new meteorology–oceanography or hydrology–meteorology relation is added from these records alone. Such links may be scientifically plausible, but a relation should be grounded in specific substantive Claim pairs and a defined relation meaning, not inferred from adjacent slice names or broad subject overlap.

## Consolidated result

| Slice | Claims screened | Evidence/source result | Context/Scope | Decision |
|---|---:|---|---|---|
| Hydrology | A/B/C | Direct USGS support; EU locators too generic | Both target A | HOLD |
| Meteorology | A/B/C | Direct NOAA support; EU locators too generic; B/C need child-page pinpoint | Both target A | HOLD |
| Oceanography | A/B/C | Current Claims are editorial/scope metadata; homepage does not support them as scientific facts | Useful boundary, target A only | HOLD |

No INCLUDE decision is made. Technical CI success, slice completeness and `publication_status: published` do not replace this record-level editorial decision. Existing closed audits and relations remain undisturbed.
