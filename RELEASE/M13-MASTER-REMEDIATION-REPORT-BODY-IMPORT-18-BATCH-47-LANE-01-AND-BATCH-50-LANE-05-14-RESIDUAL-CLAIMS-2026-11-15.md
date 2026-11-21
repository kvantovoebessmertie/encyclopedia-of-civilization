# M13 master remediation — exact report-body import 18

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source reports:
- `RELEASE/M13-BATCH-47-LANE-01-SOURCE-PASSAGE-REVIEW-2026-11-12.md` (blob `8ed9ecb17532eb0b193449ae97d44ddb6813dbd9`)
- `RELEASE/M13-BATCH-50-LANE-05-SOURCE-PASSAGE-REVIEW-2026-11-12.md` (blob `c434735c839a88cde9b9a69ee552925453c7672d`)

## Scope and exact join

Both reports were read in full. Each reviews 20 Claims. Exact Claim-ID matching against the 359-row residual Generic Evidence Use cohort yields 7 rows from Batch 47 Lane 1 and 7 rows from Batch 50 Lane 5 (14 total). All other report entries are outside the residual cohort and excluded. No fuzzy or normalized-ID matching was used.

All 14 canonical Evidence Use JSON records were fetched from exact paths in the master ledger at this branch. Each is record version 1, and its `content.claim_ref` and `content.source_ref` exactly match the expected Claim v1 and Source v1 IDs. Exact EU blob SHAs are recorded in the CSV ledger. This verifies the current EU edges only; it does not certify the full Claim/Source contents or source passage validity.

## Imported findings

| Source lane | Claim ID | Desk D/E/B | Import disposition | Finding / next action |
|---|---|---:|---|---|
| Batch 47 L1 | CLM-MEASUREMENT_SCIENCE_BASICS-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | BIPM VIM 2.9 defines a measurement result as quantity values attributed to a measurand together with relevant information, including uncertainty. Add VIM 2.9 and relevant-note locator; distinguish measurement value from full result. |
| Batch 47 L1 | CLM-MINERALOGY_BASICS-A | 1/1/2 | NOT_ESTABLISHED_BY_CURRENT_SOURCE | USGS defines a mineral as a naturally occurring inorganic element or compound with orderly internal structure and characteristic composition/physical properties. The Claim says mineralogy studies elements and compounds, which is broader and potentially inaccurate; propose correction to minerals and add exact definition locator. |
| Batch 47 L1 | CLM-MINERALOGY_BASICS-B | 2/1/2 | PARTIAL | USGS Minerals 101 supports composition, internal structure, crystal form and physical properties, but the registered URI is a general thesaurus rather than the cited definition page. Resolve source identity/URI and add pinpoint. |
| Batch 47 L1 | CLM-SCIENTIFIC_METHOD_BASICS-B | 2/1/2 | NOT_ESTABLISHED_BY_CURRENT_SOURCE | The registered National Academies chapter is broad science-education material; the generic source identity sentence does not establish a testable-hypothesis definition. Add exact definition locator and clarify whether hypothesis means explanatory proposition or assumption. |
| Batch 47 L1 | CLM-SEISMOLOGY_BASICS-A | 3/1/2 | PARTIAL | USGS Earthquake Hazards is relevant to earthquakes and seismic waves, but the broad program page is not a precise definition of seismology. Add a USGS glossary or introductory seismology locator. |
| Batch 47 L1 | CLM-SENSOR_SYSTEMS_BASICS-B | 1/1/1 | NOT_ESTABLISHED_BY_CURRENT_SOURCE | NIST IoT Cybersecurity does not support the general measurement range/accuracy/conditions proposition; this is a source-scope mismatch. Replace with metrology sources such as VIM/GUM and add exact locators. |
| Batch 47 L1 | CLM-SOIL_BASICS-C | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | USDA NRCS soils material is relevant to spatial and depth variability, but the registered landing page lacks a soil-profile/landscape locator. Add a specific NRCS soil-survey passage. |
| Batch 50 L5 | CLM_WATER_RESOURCES_BASICS_A | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | USGS Water Resources and EPA Water support surface/groundwater and wetlands as components important to ecosystems and human uses. Add exact definition passages. |
| Batch 50 L5 | CLM_WATER_RESOURCES_BASICS_C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | USGS water-resources material supports quantity, quality and availability monitoring, but the spatial/temporal interpretation boundary needs a precise monitoring passage. |
| Batch 50 L5 | CLM-WEATHER_BASICS-A | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | NOAA Weather & Atmosphere is directly relevant to weather as atmospheric conditions at a specific place/time, but the collection landing page lacks the exact definition locator. |
| Batch 50 L5 | CLM-WEATHER_BASICS-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NOAA Weather Observations explicitly lists temperature, humidity, precipitation, pressure and wind as observable atmospheric variables. Add exact page locator. |
| Batch 50 L5 | CLM-WEATHER_BASICS-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NOAA/Met Office material distinguishes observations of current conditions from model-based forecasts of future conditions. Add an exact forecasting passage. |
| Batch 50 L5 | CLM-ZOOLOGY_BASICS-B | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | OpenStax Biology 2e Chapter 28 introduces animal diversity and evolutionary lineages, but the Claim's plan-of-organization proposition needs a specific section locator. |
| Batch 50 L5 | CLM-ZOOLOGY_BASICS-C | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | OpenStax Chapter 28 supports classification by observable and evolutionary traits, but no exact phylogenetic/classification passage is recorded. |

## Control results

- Exact residual-cohort imports: **14/14** (Batch 47 Lane 1: 7; Batch 50 Lane 5: 7).
- Canonical Evidence Use records modified: **0**.
- Claim, Source, Context, Scope and Relation records modified: **0**.
- Official D/E/B values overwritten: **0**; desk scores remain separate provisional fields.
- All 14 Claims remain **HOLD**.
- Rights/permissions, specialist, independent, Human View, editorial and publication gates remain uncleared.
- No canonical-write authorization is created or implied.

Disposition labels are conservative ledger classifications derived from the report narrative, not new specialist adjudications. Append-only remediation documentation; not release or publication approval.
