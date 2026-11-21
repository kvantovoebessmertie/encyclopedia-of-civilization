# First Edition — Batch 14 Earth Systems, Climate Adaptation and Remote Sensing Locator Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `b788772bf0a073896e7c57c1927341327d9f6ad0`  
Status: **6 CANDIDATE CLAIMS / 6 EUS PLUS 9 OUT-OF-MASTER CLAIMS / 9 EUS RESEARCHED ACROSS FIVE SLICES; DIRECT LOCATORS FOUND; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Batch 14 performs locator/source research on five slices. Exact-master verification confirms only Remote Sensing and Solar System are candidate slices; Climate Adaptation, Hydrology and Meteorology are current corpus slices absent from the first-edition candidate master and are treated as out-of-master supplemental research, not candidate work:

**Candidate scope (6 Claims / 6 EUs / 2 Sources):**
- remote-sensing-basics — Claims A–C;
- solar-system-basics — Claims A–C.

**Out-of-master supplemental research (9 Claims / 9 EUs / 3 Sources):**
- climate-adaptation-basics — Claims A–C;
- hydrology-basics — Claims A–C;
- meteorology-basics — Claims A–C.

The broad domain audits for climate/space/remote sensing and hydrology/meteorology/oceanography were consulted. This follow-up does not repeat their broad audit conclusions. It pins existing Claim/EU chains to exact passages and identifies where current Source identity/URI is too broad.

Solar System review is limited to the three current Claims (system inventory, Sun as a star, and galactic location); it does not reopen the previously screened orbital-material topic. Water Security is excluded because it has its own P8 re-audit. Oceanography was handled separately in Batch 13.

All 15 Claims and 15 EUs were re-fetched from the PR branch. Exact-master inspection confirms Remote Sensing and Solar System records are present, while Climate Adaptation, Hydrology and Meteorology A–C and their EUs/Sources are absent from the candidate master. The EUs currently contain generic descriptions rather than claim-specific `material.locator` values.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All five slices remain HOLD.

## 2. Aggregate findings

| Slice | Claims / EUs | Result |
|---|---:|---|
| climate-adaptation-basics | 0 candidate; 3 current out-of-master / 3 EUs | IPCC AR6 WGII SPM and Chapters 1/16 directly support risk components, context-specific adaptation and adaptation limits/residual risk |
| hydrology-basics | 0 candidate; 3 current out-of-master / 3 EUs | USGS “What is Hydrology?” directly covers the definition and water pathways; add section locators |
| meteorology-basics | 0 candidate; 3 current out-of-master / 3 EUs | NOAA weather page and observation page support A/B; NOAA NCEI numerical weather prediction directly supports C |
| remote-sensing-basics | 3 candidate / 3 EUs | NASA ARSET and USGS sources support the definition, spectral response and resolution/observation limits; current Landsat-only Source is too narrow |
| solar-system-basics | 3 candidate / 3 EUs | NASA Solar System Facts directly supports all three Claims; Sun Facts gives a stronger specific locator for B |

**Total researched:** 15 Claims / 15 EUs / five Sources. **Candidate master scope:** 6 Claims / 6 EUs / two Sources. **Out-of-master supplemental scope:** 9 Claims / 9 EUs / three Sources. New source records may be needed for Meteorology C and Remote Sensing A–C; canonical IDs are not assigned here.

## 3. Climate Adaptation Basics — Claims A–C

Current records:
- `CLM-CLIMATE_ADAPTATION-A/B/C@1`
- `EU-CLIMATE_ADAPTATION-A/B/C@1`
- `SRC-CLIMATE_ADAPTATION@1`

Current Source: IPCC, *AR6 Working Group II: Impacts, Adaptation and Vulnerability*. It is appropriate; the EUs need precise report locators.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Climate risks arise from interaction among hazards, exposure and vulnerability | Summary for Policymakers (SPM), A.3.1; Technical Summary section on climate-risk framing; Chapter 1 §1.2.1 and Annex II Glossary |
| B | Adaptation is considered in the context of particular climate impacts, systems and conditions | SPM B.4, especially B.4.2 “Adaptation is context-specific”; Chapter 1 §1.4.1 on adaptation context |
| C | Adaptation measures have contextual limits; their effects and residual risks require separate evaluation | Chapter 16 §16.4 “Limits to adaptation and residual risks”; SPM C.3 and Technical Summary TS.D.2 |

Sources:
- IPCC AR6 WGII report: https://www.ipcc.ch/report/ar6/wg2/
- Technical Summary: https://www.ipcc.ch/report/ar6/wg2/chapter/technical-summary/
- Chapter 16, “Key Risks across Sectors and Regions”: https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-16/
- Chapter 17, “Decision-Making Options for Managing Risk”: https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-17/

The report directly frames risk through hazards, exposure and vulnerability; it defines adaptation in human and natural systems; and it assesses adaptation limits and residual risk. Preserve the IPCC's confidence language and distinctions between natural, managed and human systems. Do not imply that every adaptation measure has the same limits or that residual risk is zero when adaptation is implemented.

No Claim wording change is proposed. Add exact section/table/paragraph locators to each EU. Rights: IPCC reports have publisher/copyright terms; attribution and report-specific reuse terms must be checked. Do not reproduce IPCC figures without permission.

## 4. Hydrology Basics — Claims A–C

Current records:
- `CLM-HYDROLOGY_BASICS-A/B/C@1`
- `EU-HYDROLOGY_BASICS-A/B/C@1`
- `SRC-HYDROLOGY_BASICS@1`

Current Source: USGS Water Science School, “What is Hydrology?” This page directly supports all three Claims; no Source identity change is necessary.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Hydrology covers occurrence, distribution, movement and properties of Earth's waters | “What is Hydrology?”, opening definition |
| B | The hydrologic cycle moves water among surface waters, groundwater and the atmosphere | Same page, paragraph defining the continuous water cycle and pathways; USGS “Water cycle”, “Pools and Fluxes” and “Fluxes move water between pools” |
| C | Water pathways include runoff, infiltration, evaporation and transpiration | “What is Hydrology?”, pathways paragraph; USGS “Water cycle”, “Fluxes move water between pools”; USGS “Surface Runoff and the Water Cycle”, “Evapotranspiration and the Water Cycle” |

Sources:
- USGS, “What is Hydrology?”: https://www.usgs.gov/water-science-school/science/what-hydrology
- USGS, “Water cycle”: https://www.usgs.gov/special-topics/water-science-school/water-cycle
- USGS, “Surface Runoff and the Water Cycle”: https://www.usgs.gov/water-science-school/science/surface-runoff-and-water-cycle
- USGS, “Evapotranspiration and the Water Cycle”: https://www.usgs.gov/water-science-school/science/evapotranspiration-and-water-cycle

The current “What is Hydrology?” page itself names occurrence, distribution, movement and properties, and describes water returning through rainfall/snowfall, rivers, soil infiltration, evaporation and transpiration. The broader Water Cycle page is useful for pinning pools and fluxes among atmosphere, surface, soil and groundwater. Keep the distinction between the global water cycle and specific local catchment pathways.

No Claim wording change is necessary. Pin the current USGS Source to its exact passages; if the EUs use the Water Cycle page, add a distinct Source/EU chain rather than silently changing the Source URI to a different publication.

## 5. Meteorology Basics — Claims A–C

Current records:
- `CLM-METEOROLOGY_BASICS-A/B/C@1`
- `EU-METEOROLOGY_BASICS-A/B/C@1`
- `SRC-METEOROLOGY_BASICS@1`

Current Source: NOAA Education, “Weather and atmosphere”. It directly supports A and much of B. Claim C needs the NOAA NCEI numerical-weather-prediction page.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Weather describes the state of the atmosphere at a particular place and time | NOAA “Weather and atmosphere”, opening definition |
| B | Temperature, pressure, humidity and wind are basic meteorological variables | NOAA “Weather observations”, “Observation methods” paragraph listing temperature, humidity, precipitation, air pressure, wind speed and direction |
| C | Observations and models are used together to analyze and forecast weather | NOAA NCEI “Numerical Weather Prediction”, opening paragraph: computer models process current weather observations to forecast future weather |

Sources:
- NOAA, “Weather and atmosphere”: https://www.noaa.gov/education/resource-collections/weather-atmosphere
- NOAA, “Weather observations”: https://www.noaa.gov/education/resource-collections/weather-atmosphere/weather-observations
- NOAA NCEI, “Numerical Weather Prediction”: https://www.ncei.noaa.gov/products/weather-climate-models/numerical-weather-prediction

The existing Source page directly defines weather and identifies its components. The observation page gives the exact meteorological measurements. The NCEI page is the direct source for the observation/model connection. Do not imply that a forecast model simply extrapolates one observation; NOAA describes data assimilation and model processing.

Recommended source graph:
- Keep the existing NOAA Education Source for A and B, with separate exact locators.
- Add a distinct NCEI Source/EU for C. Do not point the existing NOAA Education Source to an unrelated NCEI product page.

## 6. Remote Sensing Basics — Claims A–C

Current records:
- `CLM-REMOTE_SENSING_BASICS-A/B/C@1`
- `EU-REMOTE_SENSING_BASICS-A/B/C@1`
- `SRC-REMOTE_SENSING_BASICS@1`

Current Source: USGS Landsat Missions. It is relevant to satellite remote sensing, but the current Source identity is broader than the specific Landsat page and is not the strongest direct source for the general definition and physical measurement principle.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Remote sensing uses measurements collected at a distance, for example from aircraft or space platforms | NASA Applied Remote Sensing Training Program, *Fundamentals of Remote Sensing*, “What is Remote Sensing?”, slide 5; NASA Earth Observatory, “Remote Sensing”, opening section |
| B | Measured reflected/emitted radiation is related to physical properties of the observed object | NASA ARSET slide 5: satellites carry sensors measuring electromagnetic radiation reflected/emitted by terrestrial and atmospheric sources; USGS Spectral Characteristics Viewer, “Target Spectra” and “Sensor RSR Sampling of Target Spectra” |
| C | Interpretation requires attention to spatial/spectral resolution and observation conditions | USGS Circular 1525, sections “Spatial Resolution”, “Spectral Resolution”, “Temporal Resolution” and “Radiometric Resolution”; USGS Landsat “What are the best Landsat spectral bands for use in my research?” |

Sources:
- NASA ARSET, *Fundamentals of Remote Sensing*, “What is Remote Sensing?”: https://appliedsciences.nasa.gov/sites/default/files/2022-11/Fundamentals_of_RS_Edited_SC.pdf
- NASA Earth Observatory, “Remote Sensing”: https://science.nasa.gov/earth/earth-observatory/remote-sensing/
- USGS, “Spectral Characteristics Viewer”: https://landsat.usgs.gov/spectral-characteristics-viewer
- USGS Circular 1525, *Remote Sensing for Monitoring Mine Lands and Recovery Efforts*: https://pubs.usgs.gov/circ/1525/cir1525.pdf
- USGS, “What are the best Landsat spectral bands for use in my research?”: https://www.usgs.gov/faqs/what-are-best-landsat-spectral-bands-use-my-research

The NASA ARSET material directly explains sensors measuring reflected/emitted electromagnetic radiation and derives physical quantities such as height, temperature and moisture with calibrated instruments. The USGS Spectral Characteristics Viewer compares sensor response curves with target spectra. USGS Circular 1525 defines spatial, spectral, temporal and radiometric resolution and discusses trade-offs.

Recommended source graph:
1. Add a distinct NASA ARSET/Earth Observatory Source/EU for Claims A/B.
2. Keep the existing USGS Landsat Source for Claim C, but correct its identity to the exact USGS Landsat source and use direct locator references.
3. If Claim C retains the general phrase “conditions of observation”, use the USGS Circular's temporal/radiometric resolution and atmospheric context; do not imply resolution is the only interpretive limitation.
4. Do not invent new Source IDs. Use canonical ID allocation and the approved Source reuse policy.

Support boundary: the Landsat band table is specific to particular Landsat sensor generations and bands. Do not generalize the exact wavelength/resolution values to all remote-sensing sensors.

## 7. Solar System Basics — Claims A–C

Current records:
- `CLM-SOLAR_SYSTEM_BASICS-A/B/C@1`
- `EU-SOLAR_SYSTEM_BASICS-A/B/C@1`
- `SRC-SOLAR_SYSTEM_BASICS@1`

Current Source: NASA Science, “Solar System Facts”. It directly supports all three Claims. No Source graph expansion is required.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | The Solar System includes the Sun, eight planets, dwarf planets, moons, asteroids and comets | NASA “Solar System Facts”, “Introduction” |
| B | The Sun is the star of the Solar System | NASA “Solar System Facts”, opening sentence; NASA “Our Sun: Facts”, opening paragraph |
| C | The Solar System is located in the Milky Way | NASA “Solar System Facts”, “Introduction”, paragraph beginning “Our solar system is located in the Milky Way” |

Sources:
- NASA, “Solar System Facts”: https://science.nasa.gov/solar-system/solar-system-facts/
- NASA, “Our Sun: Facts”: https://science.nasa.gov/sun/facts/

NASA states that the Solar System includes the Sun, eight planets, five officially named dwarf planets, hundreds of moons and thousands of asteroids and comets; it is located in the Milky Way. NASA's Sun facts page identifies the Sun as a star and the Solar System's only star.

Preserve the current scope: the Claim A inventory is a general description, not an exhaustive list of all small bodies or trans-Neptunian objects. Claim C is galactic location, not a claim about orbital period or galactic motion; the earlier orbit audit boundary is respected.

## 8. Rights, scope and editorial gates

- IPCC AR6 WGII: publisher/copyright terms apply; use exact citations and do not reproduce report figures without permission.
- USGS pages and publications are generally U.S. Government works, but some photographs/media on Water Science School pages are third-party or separately restricted. Check item-level “Sources/Usage” notices.
- NOAA and NASA factual pages are U.S. Government sources; embedded images, videos and third-party media may have separate rights.
- NASA ARSET and USGS Landsat data products have source-specific documentation; do not assume every third-party training image or dataset is public domain.
- All five slices remain HOLD pending exact locator implementation, source rights, independent editorial review and Human View.

## 9. Recommended execution order after owner authorization

1. Candidate locator-only: Solar System A–C.
2. Candidate source/locator work: Remote Sensing A/B with NASA source/EU; retain USGS Landsat source for C with exact resolution/observation locators.
3. Out-of-master supplemental work: Climate Adaptation A–C, Hydrology A–C and Meteorology A–C remain outside the candidate denominator. Do not apply canonical changes until the owner explicitly approves their admission to first-edition scope.
4. Re-fetch all authorized candidate records at one frozen HEAD; apply only approved source/EU version changes; validate exact Claim→EU→Source references, run affected-slice tests and then full release gates on the final immutable HEAD.

## 10. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change any Claim statement or version;
- create new canonical Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve the six candidate locator/source updates; separately decide whether the nine Climate Adaptation, Hydrology and Meteorology Claims should enter the first-edition candidate pool; approve the new NCEI and NASA remote-sensing Source/EU chains and their canonical IDs.
