# M13 master remediation — exact report-body import 12

Date: 2026-11-15  
Source report: `RELEASE/M13-BATCH-50-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md`  
Source report blob: `545d3ab01a866f49e7cd671a1f9912f02269df1a`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Scope and exact join

The source report reviews 20 Claims. Exact Claim-ID matching against the 359-row residual Generic Evidence Use cohort yields **13** rows. Seven source-report entries are outside the residual cohort and are excluded. No fuzzy or normalized-ID join was used.

All 13 canonical Evidence Use JSON files were fetched from the exact paths in the master ledger. Each is record version 1 and contains the exact Claim v1 and Source v1 references corresponding to its record ID. This confirms linkage only, not substantive support or rights.

## Imported findings

| Claim ID | Desk D/E/B | Disposition | Finding / next action |
|---|---:|---|---|
| CLM-ROBOTICS_ENGINEERING_BASICS-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NIST Robotics is relevant to task/environment-specific validation and performance; add standards and test-method locators for suitability criteria. |
| CLM-SAMPLING_BASICS-A | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NIST/SEMATECH defines sampling as selecting part of a population to obtain information about the whole; add exact handbook section. |
| CLM-SAMPLING_BASICS-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NIST/SEMATECH supports sampling design effects on representativeness and inference; add probability/nonprobability sampling locator. |
| CLM-SAMPLING_BASICS-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NIST handbook covers variability, sample size, selection methods and bias; add exact chapters. |
| CLM-SCIENTIFIC_METHOD_BASICS-A | 2/1/2 | PARTIAL | National Academies chapter 1 is a broad science-education framework, not a precise definition of research testing explanations through observations/data; add a precise source and scope boundary. |
| CLM-SCIENTIFIC_METHOD_BASICS-C | 2/1/3 | DIRECT_WITH_PINPOINT_GAP | The inference-limit boundary is sound, but the registered chapter does not pinpoint it; add an inference/limitations section or methodology source. |
| CLM-SEISMOLOGY_BASICS-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | USGS supports seismographs recording ground motion; add exact instrument/recording locator. |
| CLM-SEISMOLOGY_BASICS-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | USGS supports effects depending on magnitude, depth, distance and local site conditions; pinpoint all factors. |
| CLM-SENSOR_SYSTEMS_BASICS-A | 2/1/2 | PARTIAL | NIST IoT Cybersecurity is relevant to connected sensor devices but is not a general source for sensor-system observation and data-processing architecture; add general sensor/instrumentation source. |
| CLM-SENSOR_SYSTEMS_BASICS-C | 1/1/2 | NOT_ESTABLISHED_BY_CURRENT_SOURCE | NIST IoT cybersecurity does not establish calibration, sensor placement and environmental conditions as determinants of data meaning; replace with metrology/sensor-characterization references. |
| CLM-SETTLEMENT_GEOGRAPHY-A | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | UN-Habitat Degree of Urbanisation manual supports continuous urban-to-rural classification for international comparison; add methodology locator. |
| CLM-SETTLEMENT_GEOGRAPHY-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | UN-Habitat provides harmonized criteria distinguishing cities, towns and rural areas; add exact classification locator. |
| CLM-SETTLEMENT_GEOGRAPHY-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | UN-Habitat presents the classification as statistical, not a replacement for national definitions; add methodological-note locator. |

## Control results

- Exact residual-cohort imports: **13/13**.
- Out-of-cohort entries excluded: **7**.
- Canonical Evidence Use records modified: **0**.
- Claim, Source, Context, Scope and Relation records modified: **0**.
- Official D/E/B values overwritten: **0**; scores are provisional desk values in separate ledger columns.
- All 13 Claims remain **HOLD**.
- Rights/permissions, specialist, independent, Human View, editorial and publication gates remain uncleared by this import.
- No canonical-write authorization is created or implied.

Append-only remediation documentation; not a release or publication approval.
