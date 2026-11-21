# M13 — unassessed-risk content screen package 06

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue basis: 711-row `m13-unassessed-risk-screening.csv`, source revision `f26820e59b08b4036ad78302dad8118c51dac540`  
Scope: 15 additional Claim→Evidence Use→Source chains following Package 05.  
State: **content-level desk screen; no risk metadata, D/E/B score, canonical record, or publication status changed.**

## 1. Method and limits

Inspected the exact Claim and linked Evidence Use records, the registered Source record and URI, and the live external source page. The review records direct/partial/missing support and routing only. It does not assign risk likelihood/severity, D/E/B ratings, specialist approval, or publication clearance. Generic EUs without reproducible pinpoints remain insufficient for final evidence certification even where a source's subject matter is relevant.

## 2. Asset management — 1 Claim

Registered Source: `SRC-ASSET_MANAGEMENT_BASICS@1`, labelled ISO 55000:2024 but with URI `https://www.iso.org/standard/83054.html`. The URI resolves to ISO 55001:2024; ISO 55000:2024 is a different standard/page (83053).

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ASSET_MANAGEMENT_BASICS-C@1` | The claim that an asset management system provides a coordinated approach to planning, decision-making and improvement is conceptually supported by the current ISO 55001:2024 page. However, the registered Source identity remains mislabeled as ISO 55000:2024. | HOLD for the same confirmed Source identity/URI correction affecting Claims A/B/C in this slice. Preserve the distinction between ISO 55000 vocabulary/principles and ISO 55001 management-system requirements. |

## 3. Astronomy — 4 Claims

Registered sources:
- NASA Science, *The Solar System*, https://science.nasa.gov/learn/basics-of-space-flight/chapter1-1/
- NASA Science, *Universe overview*, https://science.nasa.gov/universe/overview/

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ASTRONOMY_BASICS-A@1` | NASA's Solar System chapter describes the Sun, planets and other solar-system objects, and the Sun's gravitational influence. This supports the Claim's basic system-level statement. | Direct conceptual support. Add a stable pinpoint and keep the scope to the solar system. |
| `CLM-ASTRONOMY_BASICS-B@1` | The registered NASA chapter provides object categories and some physical/orbital context, but the Claim asserts that planets, dwarf planets, asteroids and comets differ in both physical properties and orbital characteristics. The landing/chapter reference does not, by itself, establish all distinctions. | Partial support. Add NASA/IAU classification sources and a JPL/NASA orbital-properties source with exact pinpoints; do not conflate classification criteria with orbital differences. |
| `CLM-ASTRONOMY_BASICS-C@1` | NASA's Solar System chapter gives the astronomical unit (Sun–Earth distance) and light-year as distinct distance scales. | Direct support. Add the exact units/distance table pinpoint. |
| `CLM-ASTRONOMY_OBSERVATION_BASICS-C@1` | The registered NASA Universe overview is primarily a cosmological-history page. It does not directly establish the Claim that telescopes/observatories collect and analyse signals from distant objects. NASA's separate “Telescopes 101” page explains that telescopes gather and focus light; the observatories page gives examples of instruments observing cosmic signals. | HOLD for source-fit correction. Add the exact telescope/observatory pages as separately identified Sources/EUs; do not treat navigation links from the overview as evidence passages. |

## 4. Astrophysics — 3 Claims

Registered Source: NASA Science, *Stars*, https://science.nasa.gov/universe/stars/

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ASTROPHYSICS_BASICS-A@1` | NASA states that stars are giant balls of hot gas, mostly hydrogen with helium and small amounts of other elements. | Direct support. Add a pinpoint to the opening definition. |
| `CLM-ASTROPHYSICS_BASICS-B@1` | NASA's Stars page describes stellar life cycles and changes in properties as stars age. | Direct support. Add a pinpoint to the “Life cycle” passage. |
| `CLM-ASTROPHYSICS_BASICS-C@1` | The registered Stars page is relevant to stars, but the Claim extends to observations of other cosmic objects and characterizes these observations as astrophysical research into physical processes. The source page alone is too narrow for that scope. | Partial support. Add a NASA astrophysics overview and telescope/observatory sources with exact examples, or narrow the Claim to stellar research. |

## 5. Atmospheric chemistry and atmospheric science — 4 Claims

Registered sources:
- NOAA Geophysical Fluid Dynamics Laboratory, *Atmospheric Composition and Air Quality*, https://www.gfdl.noaa.gov/atmospheric-composition-and-air-quality/
- NOAA, *Weather and atmosphere*, https://www.noaa.gov/education/resource-collections/weather-atmosphere

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-ATMOSPHERIC_CHEMISTRY_BASICS-C@1` | NOAA GFDL explicitly states that chemistry and transport interact to determine the abundance/distribution of stratospheric water vapour and ozone, key trace constituents. This directly matches the Claim. | Direct support. Add a pinpoint to “Stratospheric Chemistry and Dynamics” (and, if needed, the linked research page). |
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-A@1` | The registered NOAA Weather and Atmosphere collection describes weather as the state of the atmosphere and related processes, but does not provide the claimed basic definition of the atmosphere as Earth's gaseous envelope. | HOLD for source-fit remediation. NOAA Jetstream's “The Atmosphere” page directly describes the gaseous envelope held by Earth's gravity and is a better candidate. |
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-B@1` | The registered Weather and Atmosphere collection does not establish the vertical variation of temperature, pressure and composition. NOAA Jetstream's “Layers of the Atmosphere” page directly describes layers identified by thermal characteristics, chemical composition, movement and density, with altitude-dependent changes. It does not by itself establish all temporal variation. | Partial support. Add the NOAA layers page and a separate time-variability source if the temporal phrase is retained. |
| `CLM-ATMOSPHERIC_SCIENCE_BASICS-C@1` | The registered NOAA collection describes interactions among solar radiation, oceans, landscapes and atmospheric circulation, but does not directly articulate the Claim's broad “transport of energy and matter” proposition. | Partial support. Add atmospheric dynamics/energy-budget and mass-transport sources with exact passages, or narrow the Claim to the interactions explicitly described. |

## 6. Behavioral biology — 3 Claims

Registered Source: OpenStax, *Biology 2e — Chapter 46 Introduction*, https://openstax.org/books/biology-2e/pages/46-introduction

A confirmed Source identity/URI mismatch was found: Chapter 46 is Ecology of Ecosystems, not Behavioral Biology. The relevant OpenStax material is §45.7, “Behavioral Biology: Proximate and Ultimate Causes of Behavior,” at https://openstax.org/books/biology-2e/pages/45-7-behavioral-biology-proximate-and-ultimate-causes-of-behavior.

| Claim | Passage-fit finding | Disposition |
|---|---|---|
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-A@1` | The registered Chapter 46 source is an ecosystem-ecology introduction and does not support the definition. OpenStax §45.7 defines behavior as a change in an organism's activity in response to a stimulus, which is a close match. | HOLD pending bounded Source identity/URI correction to §45.7 and a pinpoint. |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-B@1` | OpenStax §45.7 distinguishes innate behaviour with a strong genetic component from learned behaviour shaped by environmental conditioning. This directly supports the Claim's combined hereditary/environmental framing. | Direct conceptual support from the correct section, but HOLD until the Source record is version-corrected and the EU pinned. |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-C@1` | §45.7 discusses proximate and ultimate explanations and observable responses to stimuli, but the Claim's stronger methodological instruction not to attribute untestable motives is not directly established by the current source. | Partial support. Add a source on operational definitions/observational inference or narrow the Claim to distinguishing observed behaviour from explanatory hypotheses. |

## 7. Batch accounting and integrity

- Additional Claims inspected: **15/15**.
- Direct conceptual support from the registered source or a clearly identified exact section: astronomy A/C, astrophysics A/B, atmospheric chemistry C, behavioral biology B (correct section identified but Source record is wrong).
- Partial support: astronomy B, astrophysics C, atmospheric science B/C, behavioral biology C.
- HOLD for source-fit or Source identity remediation: asset management C; astronomy observation C; atmospheric science A; behavioral biology A/B pending bounded Source correction.
- Confirmed Source identity/URI defects observed in this pass: **2** — asset management (ISO 55000 label → ISO 55001 URI) and behavioral biology (OpenStax Chapter 46 ecology page registered for behavioural-biology Claims; relevant content is §45.7).
- Generic/non-pinpoint EUs: **15/15**.
- Risk metadata assigned: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Specialist adjudications and Human View approvals: **0**.

This package is a source-fit and routing screen only. No reviewed Claim is cleared for publication.

## 8. Required next actions

1. Route the ISO 55000/55001 and OpenStax Biology chapter mismatch for bounded, versioned Source corrections with regression tests.
2. Replace the NASA Universe overview as evidence for telescope/observatory operation with direct NASA telescope and observatory sources.
3. Add NASA/IAU classification and orbital-properties pinpoints for the astronomy taxonomy Claim.
4. Add NOAA Jetstream atmosphere/layers sources and dedicated transport/energy sources for atmospheric-science Claims.
5. Add exact NASA Stars and NOAA GFDL pinpoints to their EUs.
6. Keep all Claims on HOLD until evidence pinpoints, scope, source independence, specialist/Human View, rights/attribution and release gates are separately satisfied.
