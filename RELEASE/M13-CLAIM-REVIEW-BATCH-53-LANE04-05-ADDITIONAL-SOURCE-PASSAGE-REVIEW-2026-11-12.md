# M13 Batch 53 — remaining lane 04/05 high-priority source-passage review

Date: 2026-11-12
Branch: m13-system-wide-depth-audit-2026-10-09
Scope: 8 additional Claims from lanes 04 and 05. This is a continuation of the scored Batch 53 work, not a complete lane or batch close.

## 1. Method

Exact Claim, Evidence Use and Source records were checked, with the official source passages reviewed. D/E/B follow the locked M13 rubric. All eight Evidence Use records lack a reproducible Claim-specific locator, so E=1 in each case. No canonical records were modified.

## 2. Source-passage findings

### Quality control — 3 Claims

NIST/SEMATECH e-Handbook Chapter 6 states that it presents techniques for monitoring and controlling processes and signalling when corrective action is necessary. Section 6.3.1 explains that control charts monitor a quality characteristic over samples/time and use a centre line plus upper/lower control limits. Section 6.1.5 (“In Control but Unacceptable”) distinguishes statistical stability from acceptability: a process may be in control but still produce output with unacceptable mean or variability.

- Claim A is supported at the general process-monitoring/corrective-action level. The statement should not imply that every observed deviation warrants immediate adjustment; signals need interpretation.
- Claim B is directly supported by §6.3.1 and its distinction between control limits and product specifications is correct.
- Claim C is directly supported by §6.1.5 and makes an important practical distinction between process stability and product acceptance.
- Canonical EU descriptions contain no section locators; E remains 1.

### Seed applicability — 1 Claim

University of Minnesota Extension, “Saving vegetable seeds,” states that seed-saving and storage depend on plant type. It distinguishes self-pollinating and biennial crops, cross-pollinated crops, open-pollinated varieties and hybrids. Its storage section recommends cool/dry storage for the covered vegetable seeds and notes declining germination/vigor with age. It also states that hot-water treatment times/temperatures vary by plant and may injure some seeds.

- Claim is well bounded: it explicitly says general dry/cool storage guidance does not replace crop-specific requirements.
- The source is a vegetable-seed extension page, not a universal seed-storage standard. The claim's general wording should retain the species/crop-specific boundary.
- The EU describes this dependency but lacks a pinpoint. E remains 1.

### Plant pathology — 1 Claim

American Phytopathological Society, “What Is Phytopathology or Plant Pathology?”, directly states that plant pathology is an interdisciplinary science including botany, microbiology, crop science, soil science, ecology, genetics, biochemistry, molecular biology and physiology.

- The Claim's selected disciplines are directly present in the source. The claim omits crop science, soil science and molecular biology; omission is not contradiction because it says the field combines knowledge from listed areas, not that the list is exhaustive.
- This is a descriptive field-scope claim, not an operational plant-disease treatment instruction.
- The Evidence Use description identifies the source but does not preserve a specific locator; E remains 1.

### Public data — 3 Claims

UN Statistics Division's FAQ describes four connected areas: data collection, processing and dissemination; methodology, including standardization of methods, classifications and definitions; capacity development; and coordination. The UN Fundamental Principles of Official Statistics state that concepts, definitions, classifications, sources, methods and procedures should meet professional standards and be transparent. They call for documenting data collection/processing/dissemination and quality assessment. The principles also emphasize internationally aligned concepts, classifications and methods to support consistency and comparability.

- Claim A is supported by the institutional process description.
- Claim B is supported by the role of concepts, definitions, classifications and methods in consistency/comparability.
- Claim C is a valid epistemic boundary, but the UNSD homepage/principles do not directly state the exact proposition that public availability alone does not establish fitness for every analytic inference. The supporting logic is present in metadata, methods and quality-transparency requirements, but an additional data-quality/fitness-for-use source is needed.
- The canonical Source record points only to the UNSD homepage and the EU records lack locators. All three remain HOLD.

## 3. D/E/B score table

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| CLM-QUALITY_CONTROL_BASICS-A | 2 | 1 | 2 | Process observation and corrective action are meaningful; signal interpretation is required before adjustment. |
| CLM-QUALITY_CONTROL_BASICS-B | 3 | 1 | 3 | Explains control charts and explicitly distinguishes control limits from product requirements. |
| CLM-QUALITY_CONTROL_BASICS-C | 3 | 1 | 3 | Clearly distinguishes process stability from output acceptability; direct NIST §6.1.5 support. |
| CLM-SEED-APPLICABILITY | 2 | 1 | 3 | Explicitly limits general storage advice by species/seed condition and points to crop-specific requirements. |
| CLM-PLANT_PATHOLOGY_BASICS-C | 2 | 1 | 1 | Interdisciplinary scope is directly supported; introductory list has no substantive applicability boundary. |
| CLM-PUBLIC_DATA_BASICS-A | 2 | 1 | 1 | Identifies institutional collection, processing and dissemination processes; little mechanism or scope qualification. |
| CLM-PUBLIC_DATA_BASICS-B | 2 | 1 | 2 | Connects definitions, classifications and methods to comparability; source supports transparency and harmonization. |
| CLM-PUBLIC_DATA_BASICS-C | 2 | 1 | 2 | Provides an important inference boundary; exact fitness-for-use proposition needs a more direct source. |

## 4. Score summary and disposition

- Claims scored in this block: 8.
- D: score 1 = 0; score 2 = 6; score 3 = 2; mean = 2.25.
- E: score 0 = 0; score 1 = 8; score 2 = 0; score 3 = 0; mean = 1.00.
- B: score 1 = 2; score 2 = 3; score 3 = 3; score 0 = 0; mean = 2.13.
- Source-fit concern: public-data Claim C requires a direct data-quality/fitness-for-use source; the canonical UNSD homepage is too broad.
- No canonical Claim/Evidence Use/Source JSON changed.
- No Claim accepted or release-cleared.
- All eight remain HOLD pending exact locators and required domain review.

## 5. Sources checked

- NIST/SEMATECH e-Handbook, Chapter 6, especially §§6.1.5 and 6.3.1: https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm
- University of Minnesota Extension, Saving vegetable seeds: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/saving-vegetable-seeds
- American Phytopathological Society, What Is Phytopathology?: https://www.apsnet.org/careers/Pages/WhatisPhytopathology.aspx
- UN Statistics Division, FAQ: https://unstats.un.org/home/faq/
- UN Fundamental Principles / principles governing international statistical activities: https://unstats.un.org/unsd/methods/statorg/principles_stat_activities/principles_stat_activities.asp
