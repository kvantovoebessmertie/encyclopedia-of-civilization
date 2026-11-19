# First Edition — Batch 15: Hydrology and Meteorology Evidence-Use Locator Closure

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: current PR branch at report creation  
Status: **6 CLAIMS / 6 EUS REVIEWED; FIVE EUS LOCATORS DIRECTLY SUPPORTED; HYDROLOGY C NEEDS LINKED WATER-CYCLE PAGE PINPOINT; 12-RECORD BOUNDED AUTHORIZATION PROPOSAL PREPARED; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and duplicate control

The existing Hydrology/Meteorology/Oceanography domain audit identified:
- Hydrology A–C: substantive Claims with direct USGS support, but all three EUs are generic.
- Meteorology A–C: substantive Claims with direct NOAA support, but all three EUs are generic; B/C require the NOAA “Weather observations” child page.
- Oceanography A–C: editorial placeholders; already addressed by Batch 13 research and deliberately excluded from this pass.

Exact canonical records re-fetched:
- Hydrology: `SRC-HYDROLOGY_BASICS@1`, Claims A–C@1, EUs A–C@1, Context@1, Scope@1.
- Meteorology: `SRC-METEOROLOGY_BASICS@1`, Claims A–C@1, EUs A–C@1, Context@1, Scope@1.

All inspected records are v1. All six EUs contain only generic descriptions and no `material.locator`. No active bounded authorization for hydrology or meteorology was found in `RELEASE/EDITORIAL-CORRECTION.json`. No canonical changes were made.

## 2. Hydrology Basics — 3 Claims / 3 EUs

Current Claims:
- A: `Гидрология охватывает возникновение, распределение, движение и свойства вод Земли.`
- B: `Гидрологический цикл включает перемещение воды между поверхностью, подземными системами и атмосферой.`
- C: `Вода может проходить разные пути, включая сток, инфильтрацию, испарение и транспирацию.`

Current Source:
- `SRC-HYDROLOGY_BASICS@1`
- USGS Water Science School, “What is Hydrology?”
- https://www.usgs.gov/water-science-school/science/what-hydrology

### Direct locator map

| Claim / EU | Direct locator | Support boundary |
|---|---|---|
| A / `EU-HYDROLOGY_BASICS-A` | USGS, “What is Hydrology?”, section “What is Hydrology?”, opening definition paragraph | Directly defines hydrology as the science of occurrence, distribution, movement and properties of Earth's waters and their relation to the environment within each phase of the hydrologic cycle |
| B / `EU-HYDROLOGY_BASICS-B` | Same page, “What is Hydrology?”, paragraphs 2–4: continuous water cycle; movement from Earth's surface to atmosphere and back; water paths through atmosphere, over/under land, plants and groundwater | Direct |
| C / `EU-HYDROLOGY_BASICS-C` | USGS, “What is Hydrology?”, paragraphs on water pathways and transport processes; linked USGS “Water cycle” page, section “Fluxes move water between pools” | Direct for runoff, infiltration, evaporation/evapotranspiration and streamflow; the linked “What is Hydrology?” page separately identifies transpiration by growing plants |

Sources:
- USGS, “What is Hydrology?”: https://www.usgs.gov/water-science-school/science/what-hydrology
- USGS, “Water cycle”: https://www.usgs.gov/water-science-school/water-cycle

**Important precision for Claim C:** the “Water cycle” page explicitly lists evaporation, evapotranspiration, precipitation, runoff, streamflow, infiltration and groundwater recharge under “Fluxes move water between pools”. The “What is Hydrology?” page explicitly says water may be transpired by growing plants. Preserve the distinction: evapotranspiration is a combined process, while transpiration is the plant-mediated component. Do not use “evaporation” as a synonym for transpiration.

### Proposed bounded Source alignment

The existing Source identity is a one-sentence definition and its URI is the “What is Hydrology?” page. Because Claim C uses the linked USGS “Water cycle” page, the clean bounded approach is to version the Source to a USGS Water Science School source profile that explicitly identifies both related resources:
- Source identity v2: “U.S. Geological Survey, Water Science School — ‘What is Hydrology?’ and linked ‘Water cycle’ resource.”
- Keep the canonical URI on “What is Hydrology?”; record the linked “Water cycle” URL as an additional locator in the EU C material.
- Claims A–C advance v1→v2 only to align `provenance.created_from` with Source v2; no statement change.
- EUs A–C advance v1→v2 with the exact locator map above.
- Context and Scope advance v1→v2 only to target Claim A v2 and retain their current introductory boundary.

This Source v2 should not be interpreted as permission to combine unrelated USGS publications; the two pages are explicitly cross-linked within the Water Science School.

## 3. Meteorology Basics — 3 Claims / 3 EUs

Current Claims:
- A: `Погода описывает состояние атмосферы в определённом месте и времени.`
- B: `Температура, давление, влажность и ветер относятся к основным метеорологическим величинам.`
- C: `Наблюдения и модели используются совместно для анализа и прогнозирования погоды.`

Current Source:
- `SRC-METEOROLOGY_BASICS@1`
- NOAA, “Weather and atmosphere” resource collection
- https://www.noaa.gov/education/resource-collections/weather-atmosphere

### Direct locator map

| Claim / EU | Direct locator | Support boundary |
|---|---|---|
| A / `EU-METEOROLOGY_BASICS-A` | NOAA, “Weather and atmosphere”, opening paragraph defining weather as the state of the atmosphere at a given point in time and geographic location | Direct |
| B / `EU-METEOROLOGY_BASICS-B` | NOAA, “Weather observations”, section “Observation methods”, first paragraph | Direct: names temperature, humidity, precipitation, air pressure, wind speed and wind direction as key observations. The Claim's shorter list is a subset |
| C / `EU-METEOROLOGY_BASICS-C` | NOAA, “Weather observations”, section “Weather forecasting”, opening paragraph | Direct: observations are uploaded into computer models; meteorologists combine large-scale forecasts with local observations and knowledge of local weather patterns |

Sources:
- NOAA, “Weather and atmosphere”: https://www.noaa.gov/education/resource-collections/weather-atmosphere
- NOAA, “Weather observations”: https://www.noaa.gov/education/resource-collections/weather-atmosphere/weather-observations

**Support boundary:** the NOAA observation page describes U.S. National Weather Service practice, including U.S.-specific observation volumes and local office structure. The general statement that observations and models are used together is well supported, but do not generalize the reported U.S. daily observation counts or organizational arrangements to all meteorological services worldwide.

The current Source points to the parent NOAA collection, of which “Weather observations” is a linked child page. For a locator-only correction, keep `SRC-METEOROLOGY_BASICS@1` and specify the exact child-page title and subsection in EUs B/C. No Source identity change is required unless the owner prefers an exact child-page Source profile.

## 4. Proposed exact bounded authorization

No hydrology- or meteorology-specific authorization was found. The following exact scope is ready for owner approval:

| Record | Current | Proposed | Change |
|---|---:|---:|---|
| `SRC-HYDROLOGY_BASICS` | v1 | v2 | Source identity explicitly covers “What is Hydrology?” and its linked “Water cycle” page; keep canonical URI |
| `CLM-HYDROLOGY_BASICS-A/B/C` | v1 | v2 | Statements unchanged; provenance aligns to Source v2 |
| `EU-HYDROLOGY_BASICS-A/B/C` | v1 | v2 | Add direct locator text and exact Claim/Source v2 references |
| `CTX-HYDROLOGY_BASICS` | v1 | v2 | Update target_ref to Claim A v2; preserve current context wording unless needed for the new source profile |
| `SCP-HYDROLOGY_BASICS` | v1 | v2 | Update target_ref to Claim A v2; preserve current scope wording |
| `EU-METEOROLOGY_BASICS-A/B/C` | v1 | v2 | Add direct NOAA parent/child page locators; keep Claims and Source v1 unchanged |

**Total: 12 canonical records.** No Claim statement changes, no new IDs and no Source change in Meteorology.

## 5. Explicit prohibited changes

- No changes outside hydrology-basics and meteorology-basics.
- No changes to Claim statements or claim_type.
- No new Source, Claim, EU or Relation IDs.
- No publication_status or completion_status changes.
- No INCLUDE/EXCLUDE decision or allowlist changes; both slices remain HOLD.
- No Context/Scope content changes beyond exact target_ref alignment for Hydrology.
- No changes to the existing hydrology ↔ water-resources relation.
- No changes to Oceanography; it remains governed by Batch 13.
- No validator, storage, recovery, package or release-gate changes.
- No merge, deployment or release approval.

## 6. Rights and release boundaries

- USGS hydrology pages identify USGS source usage; individual images/media can have separate credits or restrictions. The “Water cycle” page contains some media marked as potentially restricted. The corpus should store bibliographic identity and locators only, not reproduce media.
- NOAA pages are official educational resources; third-party photos, videos and embedded media require item-level rights checks.
- These are basic educational claims, not hydrologic design parameters, weather warning thresholds or operational forecasting instructions.
- All records remain HOLD pending owner approval, source-rights review, independent editorial review and Human View.

## 7. Validation after approval

- Re-fetch all 12 records at a frozen PR HEAD.
- Verify exact ID, version, type and provenance.
- Verify hydrology Claim→EU→Source references point to v2; Context/Scope target Claim A v2.
- Verify meteorology EU Claim/Source refs remain v1 and every locator identifies the exact NOAA page/section.
- Verify all six EUs have non-empty claim-specific locators and preserve `evidence_role: supports`.
- Run affected-slice preflight/tests and exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests.
- Keep both slices HOLD. Technical PASS does not establish source rights, factual truth or release eligibility.

**Owner decision required:** approve or reject this exact 12-record bounded scope. No canonical change is performed by this research report.
