# M13 duplicate-source adjudication: NOAA Weather and Atmosphere, USGS Water Resources, and USGS GIS

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `6a5037ffa32d58f6c90709f9cb3aac98b244bfda`  
Scope: three academic/science reference shared-URI groups. Source, Evidence Use and Claim records were inspected directly; NOAA, USGS and EPA pages were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| NOAA Weather and Atmosphere | 3 | 9 | One NOAA education-collection page. It directly supports the weather definition and several weather-variable/forecast Claims, but not all atmospheric-structure and meteorology propositions. |
| USGS Water Resources Mission Area | 2 | 6 | One current USGS mission-area page. It supports core water monitoring and resource topics. A separate EPA page independently supports Water Resources Claim A; an EPA Source is also in the Claim provenance for B/C but no corresponding Evidence Use link was found. |
| USGS Geographic Information Systems | 2 | 6 | Both IDs point to a USGS URL that now returns 404. Current USGS FAQ and older specific USGS publications are replacement candidates; the data-quality Claim needs more precise standards evidence. |

**Totals: 7 Source records, 21 linked Claims, three URI groups.** Repeated Source IDs at one URL do not create independent corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This report is source-fit adjudication only.

## 2. NOAA Weather and Atmosphere — three IDs, one collection page

### Source identity

All three records point to `https://www.noaa.gov/education/resource-collections/weather-atmosphere`:

- `SRC-ATMOSPHERIC_SCIENCE_BASICS`
- `SRC-METEOROLOGY_BASICS`
- `SRC-WEATHER_BASICS`

The first two Source identity fields are broad definition sentences; the third says “NOAA — Weather & Atmosphere”. All three identify one NOAA education-resource collection page, not three independent publications.

The current NOAA page directly defines weather as the state of the atmosphere at a given time and geographic location. It says forecasts estimate near-future conditions using statistical models of similar past weather events, and lists temperature, airborne moisture, cloudiness and wind as weather components. It also describes observations used by meteorologists, weather systems and interactions among solar radiation, oceans, landscapes and atmospheric motion.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-A` — the atmosphere is Earth’s gaseous envelope where meteorological processes occur | Partial. NOAA’s page is about weather and atmospheric processes, but the inspected page does not define the atmosphere as a gaseous envelope. Add a specific NOAA/NASA atmospheric-science reference. |
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-B` — temperature, pressure and composition vary with altitude and time | Not directly supported. The page mentions temperature and air pressure in weather-system context, but not vertical atmospheric profiles or composition changes with altitude. Add a source on atmospheric structure/composition. |
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-C` — atmospheric processes involve transfer of energy and matter | Partial. NOAA describes interactions among solar radiation, oceans, landscapes and atmospheric motion, but the full energy/matter-transfer statement is not explicit. Add an atmospheric thermodynamics/transport source. |
| `CLM-METEOROLOGY_BASICS-A` — meteorology studies the atmosphere and weather phenomena | Partial. The page is a NOAA weather/atmosphere education collection and shows meteorological observations, but it does not explicitly define meteorology as a discipline. |
| `CLM-METEOROLOGY_BASICS-B` — temperature, pressure, humidity and wind are core meteorological quantities | Direct in substance. NOAA lists temperature, airborne moisture and wind as weather components and identifies air pressure in its description of ocean-atmosphere interactions. Add the page-level locator and avoid implying this is an exhaustive list. |
| `CLM-METEOROLOGY_BASICS-C` — observations and models are used together to analyze and forecast weather | Direct. The page states that meteorologists make observations to develop forecasts and that forecasts use statistical models of similar conditions from previous events. |
| `CLM-WEATHER_BASICS-A` — weather is the state of the atmosphere at a particular place and time | Direct. NOAA’s opening definition states this explicitly. |
| `CLM-WEATHER_BASICS-B` — temperature, pressure, humidity, wind and precipitation are observable atmospheric characteristics | Direct in substance, with a small locator gap: NOAA explicitly lists temperature, airborne moisture and wind, mentions air pressure, and describes rainfall/snow in its resource collections. Add the relevant page passages. |
| `CLM-WEATHER_BASICS-C` — a forecast estimates future atmospheric conditions and is not an observation of a past state | Direct. NOAA describes forecasts as estimates of conditions expected in the near future and distinguishes them from observations used to develop those forecasts. |

### Disposition

- Three Source IDs = one NOAA collection page; no independent corroboration between them.
- Retain the page for the weather definition, weather variables, observation and forecast Claims.
- Add distinct NOAA/NASA technical sources for atmospheric composition, vertical structure and energy/matter transport.
- All nine Evidence Use descriptions are generic and lack section/page locators.

## 3. USGS Water Resources Mission Area — two IDs, one current page

### Source identity

Both records point to `https://www.usgs.gov/mission-areas/water-resources`:

- `SRC-WATER_RESOURCES_BASICS`
- `SRC-WATER_RESOURCES_MANAGEMENT_BASICS`

Both identify the USGS Water Resources Mission Area, with minor wording/provenance differences. They are one USGS mission-area page, not two independent sources.

The current USGS page says the Mission Area monitors, assesses and researches streamflow, groundwater, water quality, water use and availability. The separate USGS page **Understanding Water Availability** defines water availability in terms of spatial and temporal distributions of water quantity and quality, human/ecosystem needs, natural and human influences, and supply/demand.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM_WATER_RESOURCES_BASICS_A` — water resources include surface/groundwater, wetlands and other aquatic components supporting ecosystems and human use | Direct through two linked institutions. The USGS page supports streamflow, groundwater and water use/availability. A separate EPA source, `SRC_EPA_WATER_RESOURCES`, is linked by `EU_WATER_RESOURCES_BASICS_EPA` and explicitly enumerates lakes, streams, groundwater, coastal waters, wetlands, associated ecosystems and human uses. This is genuine cross-institution corroboration for Claim A. |
| `CLM_WATER_RESOURCES_BASICS_B` — assessment considers quantity/distribution and physical, chemical and biological condition | The EPA page directly states this exact distinction, but the inspected Evidence Use chain links only the USGS Source. The Claim’s provenance lists the EPA Source as well, but there is no separate EPA Evidence Use for B. The USGS page provides partial support for water quantity/quality assessment. Do not count the unlinked EPA provenance entry as an active corroborating EU. |
| `CLM_WATER_RESOURCES_BASICS_C` — monitoring uses quantity, quality and availability data; interpretation depends on spatial and temporal conditions | Partial from the linked USGS Mission Area page. The separate USGS _Understanding Water Availability_ page explicitly defines availability through spatial and temporal distribution, quantity, quality and human/ecosystem needs, but it is not currently linked by an Evidence Use record. The EPA Source is listed in Claim provenance but no EPA EU is present for C. |
| `CLM_WATER_RESOURCES_MANAGEMENT_BASICS_A` — management requires quantity, quality, distribution and variability | Partial-to-direct. The USGS Mission Area page directly covers quantity, quality and availability; the dedicated _Understanding Water Availability_ page explicitly covers spatial/temporal distribution and changes. Add the latter as a separate Source/Evidence Use if authorized. |
| `CLM_WATER_RESOURCES_MANAGEMENT_BASICS_B` — assessment relies on observations/data about surface and groundwater | Direct. The USGS page explicitly covers streamflow and groundwater monitoring/assessment and access to water data. |
| `CLM_WATER_RESOURCES_MANAGEMENT_BASICS_C` — decisions depend on natural conditions, user needs, infrastructure and applicable rules | Partial. USGS describes water management, supply/demand and human/ecosystem needs, but the current Mission Area page does not substantiate the complete list of infrastructure and regulatory factors. Add policy/management guidance and narrow the geographic/jurisdictional scope. |

### Disposition

- Two Source IDs = one USGS Mission Area page; no independent corroboration between them.
- Claim A has a distinct EPA source and Evidence Use link, so its cross-institution corroboration is real.
- For Claims B/C, the presence of `SRC_EPA_WATER_RESOURCES` in Claim provenance is not equivalent to an Evidence Use link. The actual EU inventory contains only the EPA link for Claim A.
- The USGS _Understanding Water Availability_ page is a strong, separate source candidate for spatial/temporal availability and supply/demand Claims; it is not currently linked.
- The generic Evidence Use descriptions need exact section locators.

## 4. USGS Geographic Information Systems — two IDs, one unavailable URL

### Source identity

Both records point to `https://www.usgs.gov/programs/national-geospatial-program/geographic-information-systems-gis`:

- `SRC-GEOSPATIAL_ANALYSIS_BASICS`
- `SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS`

Both identify “U.S. Geological Survey — Geographic Information Systems”. The recorded URL currently returns **404**. The two Source records are therefore duplicate identities for one unavailable page, not separate GIS publications.

### Current USGS replacement candidates inspected

1. **USGS FAQ, _What is a geographic information system (GIS)?_** The current search-indexed USGS text defines GIS as a computer system that analyzes and displays geographically referenced information attached to unique locations. Direct page retrieval triggered an anti-bot check, so the exact current text is available in the search result but not in the page extraction.
2. **USGS Open-File Report 94-86, _Use of a Geographic Information System for Spatial Data Analysis_** (1994), pp. 3–4. The report describes GIS as an organized collection of hardware, software and information for creating, managing, using and displaying spatial data; it identifies descriptive/numeric attributes and spatial relationships such as proximity, connectivity and containment.
3. **USGS glossary/FAQ entries** define GIS and spatial data, but each definition must be matched to the Claim and scope before use.

These are separate, retrievable source candidates; they are not replacements under the old landing-page identity.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-GEOSPATIAL_ANALYSIS_BASICS-A` — geospatial analysis uses location-linked data to study spatial relationships and patterns | Partial from the old unavailable landing-page source. The USGS Thesaurus has a direct definition of geospatial analysis as study of measurements/counts/computations by geographic location; it is a separate source candidate and not currently linked here. |
| `CLM-GEOSPATIAL_ANALYSIS_BASICS-B` — GIS stores, displays, analyzes and compares spatial data | Direct in the 1994 USGS report’s abstract, which describes hardware/software/information for creating, managing, using and displaying spatial data and analysis of spatial relationships and attributes. Add that report as a separate Source record if authorized. |
| `CLM-GEOSPATIAL_ANALYSIS_BASICS-C` — results depend on data quality, scale, accuracy and provenance | Not directly supported by the unavailable landing page or the reviewed GIS definition. Add geospatial metadata/data-quality standards and coordinate-reference guidance. |
| `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A` — GIS manages, analyzes and displays information associated with locations on Earth | Direct in the current USGS FAQ search result; the 1994 USGS report also supports the core definition. |
| `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_B` — GIS combines spatial data with descriptive attributes for mapping and analysis | Direct in the 1994 USGS report, which explicitly says the spatial database may contain descriptive or numeric attributes for each geographic feature. |
| `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_C` — GIS results depend on quality, scale, coordinate reference, completeness and data suitability | Not directly supported by the reviewed GIS definition sources. Requires geospatial metadata, accuracy, scale and coordinate-reference standards with exact clauses. |

### Disposition

- Two Source IDs = one currently unavailable USGS URL.
- Do not mark the old URL as available merely because the agency still publishes GIS information elsewhere.
- The current USGS FAQ is a useful candidate for the core GIS definition; USGS OFR 94-86 is a specific, older source for GIS components and spatial attributes; metadata/coordinate-system Claims need a standards source.
- All six Evidence Use descriptions are generic and lack exact locators.

## 5. Consolidated audit decision and next actions

1. Count one source identity per shared URI: NOAA Weather and Atmosphere = 1; USGS Water Resources = 1; USGS GIS = 1.
2. Keep all 21 linked Claims in the denominator. Do not merge Source IDs or Evidence Use records based only on URL equality.
3. Preserve actual independent corroboration:
   - EPA independently supports Water Resources Claim A through its own Source and EU.
   - EPA Source presence in Claim B/C provenance is not a substitute for corresponding Evidence Use records.
4. Replace unavailable or overbroad pages only through authorized, versioned source/Evidence Use changes:
   - NOAA: add atmospheric structure/composition/transport publications.
   - USGS Water: add _Understanding Water Availability_ for spatial/temporal quantity/quality and supply/demand.
   - USGS GIS: add the current FAQ and a specific publication for GIS attributes/analysis; add standards for accuracy, scale and coordinate reference.
5. Add exact page/section locators to every corrected Evidence Use. Run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA after authorized canonical changes.

## 6. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records inspected source identity, current retrievability, linkage and Claim-level fit. It is not a release approval or authorization to edit canonical records.
