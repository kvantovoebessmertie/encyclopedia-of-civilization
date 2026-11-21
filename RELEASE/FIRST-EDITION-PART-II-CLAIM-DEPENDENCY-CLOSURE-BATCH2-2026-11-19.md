# First Edition — Part II Claim Dependency Closure Batch 2

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `e669cf913716a0e402fb9b700602390b7889ad84`  
Status: **10/10 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; ALL HOLD; EVIDENCE LOCATOR AND SUBSTANTIVE REVIEW OPEN**

## 1. Scope and result

This batch closes the remaining two Claims in each of five slices: ecotoxicology, entomology, marine biology, pathology and plant pathology. It follows each Claim to its exact Evidence Use and Source references.

| Check | Result |
|---|---:|
| Claims fetched and parsed | 10/10 |
| Evidence Use records fetched and parsed | 10/10 |
| Shared Source records already verified in Batch 1 | 5/5 |
| Claim ID/version/type matches | 10/10 |
| Evidence Use `claim_ref` matches exact Claim | 10/10 |
| Evidence Use `source_ref` matches exact Source | 10/10 |
| Claim provenance source identity matches EU source target | 10/10 |
| Evidence Use records with claim-specific `material.locator` | 0/10 |
| New Evidence Use dependency records absent from master | 10 |

The canonical JSON was read at the inspection HEAD. The ten Claims and ten Evidence Use records all have version 1 and exact expected types. The five Source records were fetched in Batch 1 and are unchanged at this HEAD (the commit comparison from Batch 1's source inspection HEAD contains documentation-only changes).

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Graph result |
|---|---|---|---|---|
| ecotoxicology-basics | `CLM-ECOTOXICOLOGY_BASICS-B@1` | `EU-ECOTOXICOLOGY_BASICS-B@1` | `SRC-ECOTOXICOLOGY_BASICS@1` | MATCH |
| ecotoxicology-basics | `CLM-ECOTOXICOLOGY_BASICS-C@1` | `EU-ECOTOXICOLOGY_BASICS-C@1` | `SRC-ECOTOXICOLOGY_BASICS@1` | MATCH |
| entomology-basics | `CLM-ENTOMOLOGY_BASICS-B@1` | `EU-ENTOMOLOGY_BASICS-B@1` | `SRC-ENTOMOLOGY_BASICS@1` | MATCH |
| entomology-basics | `CLM-ENTOMOLOGY_BASICS-C@1` | `EU-ENTOMOLOGY_BASICS-C@1` | `SRC-ENTOMOLOGY_BASICS@1` | MATCH |
| marine-biology-basics | `CLM_MARINE_BIOLOGY_BASICS_B@1` | `EU_MARINE_BIOLOGY_BASICS_B@1` | `SRC_MARINE_BIOLOGY_BASICS@1` | MATCH |
| marine-biology-basics | `CLM_MARINE_BIOLOGY_BASICS_C@1` | `EU_MARINE_BIOLOGY_BASICS_C@1` | `SRC_MARINE_BIOLOGY_BASICS@1` | MATCH |
| pathology-basics | `CLM_PATHOLOGY_BASICS_B@1` | `EU_PATHOLOGY_BASICS_B@1` | `SRC_PATHOLOGY_BASICS@1` | MATCH |
| pathology-basics | `CLM_PATHOLOGY_BASICS_C@1` | `EU_PATHOLOGY_BASICS_C@1` | `SRC_PATHOLOGY_BASICS@1` | MATCH |
| plant-pathology-basics | `CLM-PLANT_PATHOLOGY_BASICS-B@1` | `EU-PLANT_PATHOLOGY_BASICS-B@1` | `SRC-PLANT_PATHOLOGY_BASICS@1` | MATCH |
| plant-pathology-basics | `CLM-PLANT_PATHOLOGY_BASICS-C@1` | `EU-PLANT_PATHOLOGY_BASICS-C@1` | `SRC-PLANT_PATHOLOGY_BASICS@1` | MATCH |

## 3. Evidence and editorial blockers

All ten Evidence Use records have a correct `claim_ref` and `source_ref`, but no claim-specific locator. The source pages remain broad and require precise section/term pinpoints before an evidence sufficiency decision.

- Ecotoxicology: EPA “Ecological effects” is relevant but broad; the three Claims need precise sections for stressor/exposure determinants and study limitations.
- Entomology: the Entomological Society of America “What Is Entomology?” page is appropriate for the discipline definition but does not, without pinpoints or additional sources, substantiate the full ecological-role and application claims.
- Marine biology: NOAA’s general “Marine life” resource collection is too broad for the food-web and environmental-condition claims; add claim-specific NOAA or scientific sources.
- Pathology: NCBI MeSH is a suitable controlled-vocabulary source for the discipline definition, but not necessarily the distinctions among cellular, tissue, laboratory and clinical approaches or interpretation context.
- Plant pathology: the APS definition page supports the discipline's general remit, but the causes-of-disease and interdisciplinary-scope claims require direct pinpoints or additional authoritative sources.

No rights or attribution clearance was performed in this batch. All ten Claims remain HOLD.

## 4. Decision

- 10/10 Claim → Evidence Use → Source chains: **MATCH**.
- Ten Evidence Use dependencies are missing from the previous master and must be added once, by exact `record_id@version`.
- All ten Claims remain **HOLD** because locators are absent and source-fit review is incomplete.
- No canonical JSON changed. No INCLUDE/EXCLUDE decision or release allowlist was created.

## 5. Cumulative dependency-closure progress

Batch 1 + Batch 2 now cover 29/40 Claims previously marked identity-only in the base-register pool. The remaining 11 identity-only Claims require the same exact chain check. After that, a separate substantive pass must resolve all locator and source-fit blockers across the 29 closed chains.
