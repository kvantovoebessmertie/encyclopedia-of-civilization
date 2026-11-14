# M13 Source Identity and URI-Reuse Triage
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision reviewed: `4453783e9dc2db55c4936a8acd85cbc666c46f86`
Status: **Metadata review queue recorded; no Source JSON changed.**

## Corpus-wide findings

The full Claim worksheet resolves **617 distinct Source IDs**, matching the corpus's Source count. A metadata triage found:

- **50 Source `source_identity` values end in a full stop and read as declarative subject-matter sentences**, rather than clearly identifying a publication, document, dataset, organization, or other source object.
- One of those values, `SRC-CRYPTOGRAPHY_BASICS`, exactly matches the statement of `CLM-CRYPTOGRAPHY_BASICS-A`: “Криптография использует математические методы для защиты информации.” Its URI is the NIST cryptography page. This is a high-confidence source-identity metadata defect; the remaining 49 sentence-like values need item-by-item confirmation.
- **33 exact URI-reuse groups** involve **77 Source records** (44 record IDs beyond one per group). Twenty groups have differing identity strings; thirteen groups repeat the same identity string. URL reuse is not automatically a duplicate-source error, but it does mean those records must not be counted as independent evidence merely because their Source IDs differ.
- The source-linkage audit now emits review candidates for sentence-like identities and reused URIs. These are triage flags, not automatic deletions or identity merges.

## Source IDs with sentence-like identity values (50)

- `SRC-ACCOUNTING_BASICS`
- `SRC-ALGEBRA_BASICS`
- `SRC-ARTIFICIAL_INTELLIGENCE_BASICS`
- `SRC-ATMOSPHERIC_SCIENCE_BASICS`
- `SRC-BEHAVIORAL_BIOLOGY_BASICS`
- `SRC-BIODIVERSITY_BASICS`
- `SRC-CALCULUS_BASICS`
- `SRC-CLOUD_COMPUTING_BASICS`
- `SRC-COMBINATORICS_BASICS`
- `SRC-COMPUTER_ARCHITECTURE_BASICS`
- `SRC-CONSERVATION_BIOLOGY_BASICS`
- `SRC-CRYPTOGRAPHY_BASICS`
- `SRC-CYBERSECURITY_BASICS`
- `SRC-DATABASES_BASICS`
- `SRC-DEMOGRAPHIC_METHODS_BASICS`
- `SRC-DEVELOPMENTAL_BIOLOGY_BASICS`
- `SRC-DISTRIBUTED_SYSTEMS_BASICS`
- `SRC-ECOPHYSIOLOGY_BASICS`
- `SRC-EDUCATION_SCIENCE_BASICS`
- `SRC-FINANCE_BASICS`
- `SRC-GEOMETRY_BASICS`
- `SRC-GEOMORPHOLOGY_BASICS`
- `SRC-HISTORY_METHODS_BASICS`
- `SRC-HUMAN_COMPUTER_INTERACTION_BASICS`
- `SRC-HYDROLOGY_BASICS`
- `SRC-LINEAR_ALGEBRA_BASICS`
- `SRC-MACROECONOMICS_BASICS`
- `SRC-MEASUREMENT_UNCERTAINTY_BASICS`
- `SRC-METEOROLOGY_BASICS`
- `SRC-MICROBIOME_BASICS`
- `SRC-MICROECONOMICS_BASICS`
- `SRC-MINERALOGY_BASICS`
- `SRC-NUMBER_THEORY_BASICS`
- `SRC-NUMERICAL_METHODS_BASICS`
- `SRC-ORGANIZATIONAL_BEHAVIOR_BASICS`
- `SRC-PALEONTOLOGY_BASICS`
- `SRC-PARASITOLOGY_BASICS`
- `SRC-PETROLOGY_BASICS`
- `SRC-PLANT_PHYSIOLOGY_BASICS`
- `SRC-PROGRAMMING_LANGUAGES_BASICS`
- `SRC-PUBLIC_ADMINISTRATION_BASICS`
- `SRC-REMOTE_SENSING_BASICS`
- `SRC-SCIENTIFIC_METHOD_BASICS`
- `SRC-SEISMOLOGY_BASICS`
- `SRC-SOFTWARE_ENGINEERING_BASICS`
- `SRC-TRIGONOMETRY_BASICS`
- `SRC-URBAN_PLANNING_BASICS`
- `SRC-VIROLOGY_BASICS`
- `SRC-VOLCANOLOGY_BASICS`
- `SRC-ZOOLOGY_BASICS`

## High-priority examples

1. `SRC-COMPUTER_ARCHITECTURE_BASICS`, `SRC-DATABASES_BASICS`, `SRC-DISTRIBUTED_SYSTEMS_BASICS`, `SRC-PROGRAMMING_LANGUAGES_BASICS`, and `SRC-SOFTWARE_ENGINEERING_BASICS` all point to the broad NIST ITL page (`https://www.nist.gov/itl`) while their `source_identity` values define the subject domains rather than identify the NIST source.
2. `SRC-GEOMORPHOLOGY_BASICS`, `SRC-MINERALOGY_BASICS`, and `SRC-PETROLOGY_BASICS` point to the USGS thesaurus page while their identity values are definitions of the respective fields.
3. `SRC-ATMOSPHERIC_SCIENCE_BASICS` and `SRC-METEOROLOGY_BASICS` point to NOAA's general weather/atmosphere resource page while their identity values are subject definitions; the same URL is also used by `SRC-WEATHER_BASICS`.
4. `SRC-CRYPTOGRAPHY_BASICS` reuses the exact text of its linked Claim as its source identity.

## Confirmed identity/locator mismatch requiring authorized correction

`SRC-ASSET_MANAGEMENT_BASICS` identifies **ISO 55000:2024** but points to ISO's page for **ISO 55001:2024** (`https://www.iso.org/standard/83054.html`). ISO's official ISO 55000:2024 page is `https://www.iso.org/standard/83053.html`; see [ISO 55000:2024](https://www.iso.org/standard/83053.html) and [ISO 55001:2024](https://www.iso.org/standard/83054.html). Do not update the Source JSON until the separately authorized correction phase; the intended source and its precise locator must be confirmed there.



## Confirmed false-independence example

The 33 URI-reuse groups include a confirmed case in `reproductive-health-information-boundaries`:

- `SRC_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES` and `SRC_WHO_SRH_FACTS_2026` both point to the exact same URI: `https://www.who.int/health-topics/sexual-and-reproductive-health-and-rights`.
- The three `EU_P9_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A/B/C` records describe the second Source as an “Independent ... source” that corroborates the Claim, even though its canonical URI is identical to the first Source.
- This affects Claims `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A/B/C` and six Evidence Use records. The two Source IDs do not represent independent external evidence from different URLs; the independent-corroboration wording is unsupported by the graph as stored.

During the authorized correction phase, either retain one canonical Source/Evidence Use chain or document distinct passages/scopes from the same WHO page without calling them independent sources. Do not merge IDs or edit content JSON before that phase.

## Disposition

1. Review all 50 sentence-like Source identities and replace descriptive propositions with accurate source identities only in the authorized correction phase.
2. Review the 33 URI-reuse groups for same-source reuse, different expressions/sections, incorrect identity labels, and false independence assumptions.
3. Preserve all current Source IDs and historical references; do not merge records based only on URI equality.
4. Treat the ISO 55000/55001 mismatch as a confirmed metadata defect, but defer content JSON edits until authorized.

No Claim, Evidence Use, Source, or Relation JSON was edited. M13 remains open.
