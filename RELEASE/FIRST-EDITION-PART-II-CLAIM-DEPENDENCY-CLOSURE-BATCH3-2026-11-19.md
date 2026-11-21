# First Edition — Part II Claim Dependency Closure Batch 3

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `be9008d376264d16232ad9232eaaf83f07ec3479`  
Status: **11/11 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; ALL HOLD; EVIDENCE LOCATOR AND SUBSTANTIVE REVIEW OPEN**

## 1. Scope and result

This batch closes the final 11 Claims previously marked identity-only in the base-register pool: SI units (2), soil microbiology (3), soil science (3), statistics (1), thermodynamics (1) and water-resource management (1).

| Check | Result |
|---|---:|
| Claims fetched and parsed | 11/11 |
| Evidence Use records fetched and parsed | 11/11 |
| Source records fetched and parsed | 6/6 |
| Claim ID/version/type matches | 11/11 |
| Evidence Use `claim_ref` matches exact Claim | 11/11 |
| Evidence Use `source_ref` matches exact Source | 11/11 |
| Claim provenance source identity matches EU source target | 11/11 |
| Evidence Use records with claim-specific `material.locator` | 0/11 |
| Source records with exact locator/pinpoint | 0/6 |
| New dependency records absent from prior master | 7 |

Two SI Evidence Use records are version 2, not version 1. Both exact v2 records correctly reference the v1 Claims and the v1 NIST Source; no version downgrade or invented v1 EU was made.

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Graph result |
|---|---|---|---|---|
| si-units-basics | `CLM-SI-DERIVED@1` | `EU-SI-DERIVED@2` | `SRC-NIST-SI-UNITS@1` | MATCH |
| si-units-basics | `CLM-SI-SEVEN-BASE@1` | `EU-SI-SEVEN-BASE@2` | `SRC-NIST-SI-UNITS@1` | MATCH |
| soil-microbiology-basics | `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | `EU-SOIL_MICROBIOLOGY_BASICS-A@1` | `SRC-SOIL_MICROBIOLOGY_BASICS@1` | MATCH |
| soil-microbiology-basics | `CLM-SOIL_MICROBIOLOGY_BASICS-B@1` | `EU-SOIL_MICROBIOLOGY_BASICS-B@1` | `SRC-SOIL_MICROBIOLOGY_BASICS@1` | MATCH |
| soil-microbiology-basics | `CLM-SOIL_MICROBIOLOGY_BASICS-C@1` | `EU-SOIL_MICROBIOLOGY_BASICS-C@1` | `SRC-SOIL_MICROBIOLOGY_BASICS@1` | MATCH |
| soil-science-basics | `CLM_SOIL_SCIENCE_BASICS_A@1` | `EU_SOIL_SCIENCE_BASICS_A@1` | `SRC_SOIL_SCIENCE_BASICS@1` | MATCH |
| soil-science-basics | `CLM_SOIL_SCIENCE_BASICS_B@1` | `EU_SOIL_SCIENCE_BASICS_B@1` | `SRC_SOIL_SCIENCE_BASICS@1` | MATCH |
| soil-science-basics | `CLM_SOIL_SCIENCE_BASICS_C@1` | `EU_SOIL_SCIENCE_BASICS_C@1` | `SRC_SOIL_SCIENCE_BASICS@1` | MATCH |
| statistics-basics | `CLM-STATISTICS_BASICS-A@1` | `EU-STATISTICS_BASICS-A@1` | `SRC-STATISTICS_BASICS@1` | MATCH |
| thermodynamics-basics | `CLM-THERMODYNAMICS_BASICS-A@1` | `EU-THERMODYNAMICS_BASICS-A@1` | `SRC-THERMODYNAMICS_BASICS@1` | MATCH |
| water-resource-management-basics | `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_A@1` | `EU_WATER_RESOURCE_MANAGEMENT_BASICS_A@1` | `SRC_WATER_RESOURCE_MANAGEMENT_BASICS@1` | MATCH |

## 3. Seven missing dependencies added to the master

- `SRC-NIST-SI-UNITS@1`
- `EU-SOIL_MICROBIOLOGY_BASICS-A@1`
- `EU-SOIL_MICROBIOLOGY_BASICS-B@1`
- `EU-SOIL_MICROBIOLOGY_BASICS-C@1`
- `EU_SOIL_SCIENCE_BASICS_A@1`
- `EU_SOIL_SCIENCE_BASICS_B@1`
- `EU_SOIL_SCIENCE_BASICS_C@1`

All seven were fetched from canonical JSON at the inspection HEAD and matched exact ID, version and type. The other required EU and Source records were already present in the master and were re-fetched in this batch.

## 4. Evidence and editorial blockers

All 11 Evidence Use records have correct Claim and Source edges but no claim-specific locator. All six Sources also lack a pinpoint locator.

- SI: NIST SI Units is authoritative, but the Evidence Use records do not point to the exact defining-constant or derived-unit passages.
- Soil microbiology: USDA NRCS Soil Health Starter Kit is relevant, but the precise pages/figures for microbial communities, decomposition, nutrient cycling and soil biodiversity are not identified.
- Soil science: FAO Soils Portal is authoritative, but the exact pages for inherent/dynamic soil quality and soil functions are not identified.
- Statistics: NIST/SEMATECH Engineering Statistics Handbook is suitable, but the exact section for descriptive methods, variation and inference is missing.
- Thermodynamics: OpenStax College Physics 2e is suitable for introductory thermodynamics, but the exact section locator is missing.
- Water-resource management: UNESCO's Water portal is a broad portal, not a pinpoint for the surface-water/groundwater proposition.

All 11 Claims remain HOLD. Rights, attribution and reuse terms were not cleared by this dependency pass.

## 5. Cumulative closure

Batches 1–3 now close all **40/40 Claims** that were previously marked `canonical_json_verified_identity_only` in the base-register pool:

- Batch 1: 19 Claims / 19 EUs / 15 Sources; 10 previously omitted EUs discovered.
- Batch 2: 10 Claims / 10 EUs / 5 shared Sources; 10 previously omitted EUs discovered.
- Batch 3: 11 Claims / 11 EUs / 6 Sources; 7 previously omitted dependencies discovered.

Cumulative result: 40/40 Claim → Evidence Use → Source identity/version/type chains match. A total of 27 previously omitted dependency records were discovered across the three batches (10 + 10 + 7) and added to the master exactly once. This closes the graph identity/version/type pass for this 40-Claim subset only; it does not establish evidence sufficiency or close the wider dependency audit for every Part II candidate.

No canonical JSON changed. No record was promoted to INCLUDE or EXCLUDE. All decisions remain HOLD pending locators, source-fit assessment, rights review, editorial ownership and Human View.
