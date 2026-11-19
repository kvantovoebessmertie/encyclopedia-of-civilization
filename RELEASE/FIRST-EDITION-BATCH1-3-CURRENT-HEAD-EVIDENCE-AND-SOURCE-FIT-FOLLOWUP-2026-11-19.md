# First Edition — Batch 1 / Batch 3 Current-Head Evidence and Source-Fit Follow-up

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Frozen current-head inspection: `cbb620b1b2fc714414b57dc53ac7b8faba8980e1`  
Status: **RESEARCH COMPLETE FOR 30 CURRENT CLAIMS IN THE NON-OVERLAPPING BATCH 1 SLICES AND 9 BATCH 3 BASE CLAIMS; 6 P9 EUS AND 1 BIPM EU RE-REVIEWED; ALL CANDIDATE DISPOSITIONS HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope, history and controls

This follow-up continues the earlier Claim-dependency closure without repeating Batch 2 or Batch 7–9 source research.

Historical Batch 1 inspected 19 Claims across 15 slices. Five one-Claim slices overlap with the already completed Batch 2 research (ecotoxicology, entomology, marine biology, pathology and plant pathology); those five are not re-researched here. The remaining 14 historical Batch 1 Claims are researched below.

The current PR branch contains additional published/complete Claim records that were not part of the historical Batch 1 denominator. Sixteen such records were found in eight of the non-overlapping slices: Claims B/C in astronomy, cell basics, cell biology, evolution, genetics, immunology, measurement uncertainty and motion. They are documented separately as current-slice scope expansion; they are **not silently added to the 1,058 candidate-key denominator**.

Historical Batch 3 inspected 11 Claims: two SI units Claims and nine Claims across soil microbiology, soil science, statistics, thermodynamics and water-resource management. The two SI Evidence Use records have since been versioned to v2 under the existing bounded SI authorization and now contain direct NIST section references. This follow-up researches the other nine Batch 3 base Claims.

The current branch also contains five further Claims outside the historical Batch 3 denominator: Statistics B, Thermodynamics B/C and Water-resource-management B/C. They are identified as scope-expansion candidates, not treated as already included in the first-edition master. Four have direct locator candidates in the relevant sources below; Statistics B remains for a separate exact Claim/source-fit pass.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited by this report. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. No new canonical IDs are assigned here. All affected first-edition candidate slices remain HOLD.

## 2. Aggregate findings

| Workstream | Historical scope | Current-head follow-up |
|---|---:|---|
| Batch 1, non-overlapping part | 14 Claims / 10 slices | 14 base Claims researched; 16 additional current Claims identified and reviewed for source/locator routes |
| Batch 3, excluding SI | 9 Claims / 5 slices | 9 base Claims researched |
| SI units | 2 Claims / 2 EUs | Historical 0/11 locator metric remains historical; current EU-SI-DERIVED@2 and EU-SI-SEVEN-BASE@2 now carry exact NIST section references |
| P9 Marine Biology and Pathology | 6 additional EUs + 2 Sources | All six exact edges re-fetched; NOAA source only partial for Marine A/C and not direct for B; NCBI source identity is a cell-biology chapter, not a general pathology reference |
| Measurement uncertainty independent source | 1 additional EU + 1 Source | BIPM/JCGM VIM 2.26 directly supports Claim B's formal definition; the EU currently has no pinpoint |

**Research outcome:** direct locator candidates are available for the 14 historical non-overlapping Batch 1 Claims and nine non-SI Batch 3 Claims. The three major substantive blockers are (1) 9 placeholder Claims across Cell Biology, Genetics and Immunology (3 each); (2) the too-broad Biodiversity C and Soil Science C formulations; and (3) the Water Resources source-fit mismatch. Rights screening is not legal clearance.

## 3. Batch 1 — 10 non-overlapping slices

### 3.1 Astronomy Basics — three current Claims

Current records: `CLM-ASTRONOMY_BASICS-A/B/C@1`, `SRC-ASTRONOMY_BASICS@1`. The current Source identity and URL already identify NASA Science, *Chapter 1: The Solar System*; no Source identity replacement is needed.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A | The Solar System includes the Sun and many objects moving under its gravitational influence | Chapter 1, “Knowledge of the Solar System”, especially the opening definition of the Sun, heliosphere and objects orbiting the Sun |
| B | Planets, dwarf planets, asteroids and comets differ in physical and orbital characteristics | “Knowledge of the Solar System”; “Motions Within the Solar System”; classification passages on planets, asteroids, Pluto/dwarf planets and the Kuiper Belt |
| C | Astronomical distances use AU and light-year at different cosmic scales | “Distances Within the Solar System” and “Light Time”; AU is based on mean Earth–Sun distance; a light-year is the distance light travels in one year |

Official source: https://science.nasa.gov/learn/basics-of-space-flight/chapter1-1/

The current NASA chapter directly defines the solar-system object set, distinguishes planets/asteroids/dwarf planets, and gives the AU/light-year scale. Preserve the distinction between the AU (Solar-System scale) and light-year (interstellar scale). The NASA chapter itself notes that the Oort Cloud is hypothesized and not directly observed; do not convert that caveat into a confirmed-object claim.

### 3.2 Biodiversity Basics — three historical Claims

Current records: `CLM-BIODIVERSITY_BASICS-A/B/C@1`, `SRC-BIODIVERSITY_BASICS@1`. The existing Source points to OpenStax *Biology 2e* §47.4. That page is useful for conservation but is not the best single locator for all three biodiversity propositions. Correct the Source identity to the book/chapter-level identity and use both §47.1 and §47.4 as claim-specific locators.

| Claim | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| A | Biodiversity includes species diversity, genetic variants and ecosystem diversity | §47.1 “The Biodiversity Crisis” → “Types of Biodiversity” | Direct: species diversity, genetic diversity and ecosystem diversity are separately described |
| B | Species abundance can change through the balance of speciation and extinction | §47.1 → “Biodiversity Change through Geological Time” | Direct: species counts increase when speciation exceeds extinction and decrease when extinction exceeds speciation |
| C | Biodiversity assessment depends on area, time and observation method | §47.1 → “Measuring Biodiversity” and “Types of Biodiversity”; §47.4 → “Measuring Biodiversity” | Partial: the source supports multiple levels/indices, species-area relationships and different cataloguing methods; it does not clearly establish the current three-part formulation as written |

Recommended Claim C narrowing, if approved:

> Оценка биоразнообразия использует разные показатели в зависимости от исследовательской задачи, включая видовое, генетическое и экосистемное разнообразие.

Sources:
- §47.1: https://openstax.org/books/biology-2e/pages/47-1-the-biodiversity-crisis
- §47.4: https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity

**Rights:** the live OpenStax *Biology 2e* page identifies CC BY-NC-SA 4.0 and includes a restriction on LLM ingestion/generative-AI offerings without prior written permission. Attribution and ShareAlike apply to permitted non-commercial reuse; commercial use requires permission. This is a material project-level rights blocker, not a cleared source.

### 3.3 Cell Basics — three current Claims

Current records: `CLM-CELL_BASICS-A/B/C@1`, `SRC-CELL_BASICS@1`. The Source identity is already OpenStax *Biology 2e — cell structure and function*; its chapter-level URL is suitable.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A | The cell is the basic structural and functional unit of living organisms | §4.1 “Studying Cells”, including cell theory and the basic unit of life |
| B | Prokaryotic cells lack a membrane-bound nucleus; eukaryotic cells have one | §4.2 “Prokaryotic Cells” and §4.3 “Eukaryotic Cells” |
| C | Cell structures perform different functions within a cell | §4.3 “Eukaryotic Cells”, organelle subsections and the cell-structure/function descriptions |

Official book chapter: https://openstax.org/books/biology-2e/pages/4-introduction

Claim C is broad but can be supported by a locator to the organelle/function descriptions. The EU should name the relevant structures, not merely point to the section introduction.

### 3.4 Cell Biology Basics — three placeholder Claims requiring replacement

Current records: `CLM-CELL_BIOLOGY_BASICS-A/B/C@1`, `SRC-CELL_BIOLOGY_BASICS@1`. The three existing Claims are generic editorial placeholders, not falsifiable subject-matter propositions. The Source already identifies OpenStax *Biology 2e — Cell Structure* and points to Chapter 4.

Proposed replacement Claims for owner/editor review:

| Claim | Proposed subject-matter statement | Direct locator |
|---|---|---|
| A | Эукариотические клетки содержат ядро и мембранные органеллы, которые разделяют клеточные процессы по специализированным компартментам | §4.3 “Eukaryotic Cells”, nucleus and organelles |
| B | Ядро эукариотической клетки содержит большую часть её ДНК, а рибосомы участвуют в синтезе белка | §4.3, nucleus and ribosomes |
| C | Митохондрии участвуют в клеточном дыхании и синтезе АТФ; хлоропласты осуществляют фотосинтез у растений и фотосинтезирующих эукариот | §4.3, mitochondria and chloroplasts |

Official source: https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells

Keep the domain boundary explicit: these are eukaryotic-cell propositions, not universal claims about all cells. Do not imply that all eukaryotes possess chloroplasts. The current three placeholder Claims should not be retained as published factual Claims. Replacements require subject-matter/editorial approval and versioned dependency updates.

### 3.5 Conservation Biology Basics — three historical Claims

Current records: `CLM-CONSERVATION_BIOLOGY_BASICS-A/B/C@1`, `SRC-CONSERVATION_BIOLOGY_BASICS@1`. The existing Source URI points to OpenStax *Biology 2e* §47.4; correct the Source identity to the book/chapter-level publication and use §47.1 for the first Claim.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A | Biodiversity relates to species diversity and changes in organism abundance over time | §47.1 “The Biodiversity Crisis” → “Types of Biodiversity” and “Biodiversity Change through Geological Time” |
| B | Conservation considers populations, habitats and ecosystems | §47.4 → “Changing Human Behavior”, “Conservation in Preserves” and “Preserve Design” |
| C | Habitat restoration is one tool for conserving biodiversity | §47.4 → “Habitat Restoration”, including restoration of degraded ecosystems and the Yellowstone example |

Official source: https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity

The source directly supports Claim C: habitat restoration can improve biodiversity in degraded ecosystems. Preserve the source's limitations: restoration cannot restore an extinct species, and the effectiveness of preserves depends on area, design, connectivity, enforcement and ecological context.

**Rights:** same OpenStax *Biology 2e* CC BY-NC-SA 4.0 and AI-ingestion restriction noted in §3.2. No text, figures or images are proposed for reproduction.

### 3.6 Evolution Basics — three current Claims; Source identity correction required

Current records: `CLM-EVOLUTION_BASICS-A/B/C@1`, `SRC-EVOLUTION_BASICS@1`. The Source URI points to the correct OpenStax Biology section, but its identity is the placeholder “Authoritative reference source for evolution-basics”. Correct the Source identity to OpenStax *Biology 2e*, §18.1 “Understanding Evolution”.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A | Evolution describes changes in organism populations across generations | §18.1 “Understanding Evolution”, definition of evolution at population level |
| B | Natural selection can change frequencies of heritable traits in populations | §18.1, “Natural Selection” and its conditions/mechanism |
| C | Natural selection requires heritable variation among individuals in a population | §18.1, “Natural Selection”; variation, heritability and differential reproductive success |

Official source: https://openstax.org/books/biology-2e/pages/18-1-understanding-evolution

Source identity correction should be versioned; dependent Claims must advance only as required to align `provenance.created_from` to Source @2, with statements unchanged. Pin each EU to its own paragraph/subheading. Do not conflate individual organisms changing during life with population-level evolution across generations.

### 3.7 Genetics Basics — three placeholder Claims requiring replacement

Current records: `CLM-GENETICS_BASICS-A/B/C@1`, `SRC-GENETICS_BASICS@1`. The NHGRI *Talking Glossary of Genetic Terms* is an appropriate source identity. All three current Claims are generic placeholder statements.

Proposed replacement Claims for owner/editor review:

| Claim | Proposed subject-matter statement | Direct glossary entry |
|---|---|---|
| A | Ген является базовой единицей наследования и содержит информацию, связанную с биологическими признаками | “Gene” |
| B | Наследуемые признаки или варианты, закодированные в ДНК, передаются от родителей потомству при размножении | “Inherited” |
| C | Мутация — изменение последовательности ДНК; герминальные мутации могут передаваться потомству, а соматические мутации не передаются потомству | “Mutation” |

Official source: https://www.genome.gov/genetics-glossary

These three entries directly support the proposed definitions. Keep Claim C's germline/somatic boundary explicit. The source is a glossary, not a comprehensive genetics textbook; more complex claims about penetrance, gene regulation, polygenic inheritance or clinical risk need additional sources. The three placeholder Claims should be replaced only after editorial approval.

### 3.8 Immunology Basics — three placeholder Claims and a Source mismatch

Current records: `CLM-IMMUNOLOGY_BASICS-A/B/C@1`, `SRC-IMMUNOLOGY_BASICS@1`. The Source title says “Innate and Adaptive Immunity”, but the stored URL is `18-1-how-pathogens-cause-disease`, which does not match the current OpenStax Microbiology section title. Correct the Source identity/URI to OpenStax *Microbiology*, Chapter 17 and Chapter 18, with direct locators.

Proposed replacement Claims for owner/editor review:

| Claim | Proposed subject-matter statement | Direct locator |
|---|---|---|
| A | Врождённый иммунитет обеспечивает быстрые неспецифические механизмы первой линии защиты от потенциальных патогенов | Chapter 17 Introduction; §17.1 “Physical Defenses” |
| B | Адаптивный иммунитет характеризуется специфичностью к антигену и иммунологической памятью | §18.1 “Overview of Specific Adaptive Immunity” |
| C | Адаптивный иммунитет включает гуморальный ответ с участием B-клеток и антител и клеточный ответ с участием T-клеток | §18.1; §§18.3 “T Lymphocytes and Cellular Immunity” and 18.4 “B Lymphocytes and Humoral Immunity” |

Official sources:
- Chapter 17: https://openstax.org/books/microbiology/pages/17-introduction
- §18.1: https://openstax.org/books/microbiology/pages/18-1-overview-of-specific-adaptive-immunity
- §18.3: https://openstax.org/books/microbiology/pages/18-3-t-lymphocytes-and-cellular-immunity
- §18.4: https://openstax.org/books/microbiology/pages/18-4-b-lymphocytes-and-humoral-immunity

The current Source should be versioned to correct the title/URI. If the schema's single-URI Source model cannot accurately identify both chapters, use the book-level identity and precise section URLs in each Evidence Use locator, or create a separate Source only under the canonical ID allocation process. Do not invent IDs. The existing placeholder Claims do not become valid merely by adding locators.

### 3.9 Measurement Uncertainty Basics — three current Claims and an existing BIPM dependency

Current records: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A/B/C@1`, `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`. The NIST Source points to TN 1297 but has a generic Source identity. A second official source and independent EU already exist in the current content tree but were absent from the exact-version master:
- `SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY@1`
- `EU-MEASUREMENT_UNCERTAINTY_BIPM@1`, targeting Claim B.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| Claim A / `EU-MEASUREMENT_UNCERTAINTY_BASICS-A` | A measurement result should be interpreted together with its uncertainty estimate | NIST TN 1297 §7 “Reporting Uncertainty”, particularly the reporting statement and examples |
| Claim B / `EU-MEASUREMENT_UNCERTAINTY_BASICS-B` | Uncertainty characterizes the dispersion of values attributed to a measurand and is not automatically the same as error | BIPM/JCGM VIM 2.26 “measurement uncertainty”; NIST TN 1297 Appendix D1.1.3–D1.1.4 for the distinction between Type A/B evaluations and errors |
| Claim C / `EU-MEASUREMENT_UNCERTAINTY_BASICS-C` | Evaluating uncertainty requires defining the measurand and measurement model | NIST TN 1297 Appendix D4 “Measurand defined by the measurement method” and Appendix A “Law of Propagation of Uncertainty” |

Sources:
- NIST TN 1297 §7: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty
- NIST TN 1297 Appendix D1: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology
- NIST TN 1297 Appendix D4: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d4-measurand-defined-by-the-measurement-method-characterization-of-test-methods-simple-calibration
- NIST TN 1297 Appendix A: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-a-law-propagation-uncertainty
- BIPM/JCGM VIM 2.26: https://jcgm.bipm.org/vim/en/2.26.html

The existing Claim B wording is directly aligned with VIM 2.26. Pin the independent BIPM EU to the exact definition, not only to the generic source page. NIST TN 1297 Appendix D1 distinguishes uncertainty evaluation types from “Type A errors” / “Type B errors”; do not collapse uncertainty and error into synonyms. The NIST Source identity should be corrected to the full TN 1297 publication identity. The BIPM Source/EU are existing canonical records and must be added to the exact-version master, not recreated.

### 3.10 Motion Basics — three current Claims

Current records: `CLM-MOTION_BASICS-A/B/C@1`, `SRC-MOTION_BASICS@1`. The Source identity and URL already identify OpenStax Physics, one-dimensional kinematics.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A | An object's position is specified relative to a selected reference frame | §2.1 “Relative Motion, Distance, and Displacement”, “Defining Motion” |
| B | Average velocity is the ratio of displacement to the corresponding time interval | §2.2 “Speed and Velocity”, average velocity definition and equation |
| C | Acceleration describes change in velocity over time | §2.4 “Velocity vs. Time Graphs”, slope/acceleration discussion and acceleration equation |

Official sources:
- §2.1: https://openstax.org/books/physics/pages/2-1-relative-motion-distance-and-displacement
- §2.2: https://openstax.org/books/physics/pages/2-2-speed-and-velocity
- §2.4: https://openstax.org/books/physics/pages/2-4-velocity-vs-time-graphs

Claim B uses displacement (a vector) rather than total path length; do not substitute “distance” for “displacement” when describing average velocity. Claim C should be explicit about change in velocity per unit time.

## 4. Batch 3 — nine non-SI base Claims

### 4.1 Soil Microbiology Basics — three Claims

Current records: `CLM-SOIL_MICROBIOLOGY_BASICS-A/B/C@1`, `EU-SOIL_MICROBIOLOGY_BASICS-A/B/C@1`, `SRC-SOIL_MICROBIOLOGY_BASICS@1`.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Soil contains a complex community of microorganisms and other organisms | USDA NRCS *Soil Health Starter Kit*, “SOIL HEALTH DEFINED” and “HEALTHY SOILS ARE: full of life” |
| B | Soil microorganisms participate in organic-matter decomposition and nutrient cycling | “HEALTHY SOILS ARE: full of life” (organism roles/table); “Active and Stabilized Organic Matter” |
| C | Soil biodiversity is part of soil-ecosystem functioning | “BIODIVERSITY”; “HEALTHY SOILS ARE: full of life”; “HEALTHY, FUNCTIONING SOILS ARE ABLE TO” |

Official PDF: https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil-Health-Starter-Kit-reduced.pdf

The document directly states that soil is a living ecosystem containing bacteria, fungi and other organisms; it describes organisms feeding on dead organic matter, nutrient cycling, and the definition of biodiversity as variation of life forms in an ecosystem. Pinpoint by exact heading and printed page where visible. The PDF is a compilation of USDA/NRCS educational materials from different dates; do not assume that every image, diagram or component has identical rights status. No graphics or tables are proposed for reuse.

### 4.2 Soil Science Basics — three Claims

Current records: `CLM_SOIL_SCIENCE_BASICS_A/B/C@1`, `SRC_SOIL_SCIENCE_BASICS@1`.

| Claim | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| A | Soil properties include physical, chemical and biological characteristics that vary among soils and management conditions | FAO Soils Portal, “Soil properties”, opening paragraph | Direct |
| B | Soil quality has inherent and dynamic characteristics | Same page, opening paragraph | Direct |
| C | Soil functions connect soil properties with productivity, water regulation, nutrient cycling, biodiversity and ecosystem services | Same page, opening paragraph and definition of soil health | Partial: FAO supports productivity, diversity and environmental services, but does not enumerate every function in the current Claim |

Official source: https://www.fao.org/soils-portal/data-hub/soil-properties/en/

Recommended Claim C narrowing, if approved:

> Здоровье почвы характеризуется её способностью поддерживать продуктивность, разнообразие и экологические услуги наземных экосистем.

The current FAO page attributes the soil-health definition to ITPS (2020). If the broader current Claim is retained, add a distinct Source/Evidence Use chain for the additional water-regulation and nutrient-cycling functions; the USDA NRCS *Soil Health Starter Kit* provides direct passages on water storage, nutrient cycling, biodiversity and soil organisms. Do not invent a new Source ID.

### 4.3 Statistics Basics — Claim A and its independent OpenStax chain

Current records: `CLM-STATISTICS_BASICS-A@1`, `EU-STATISTICS_BASICS-A@1`, `SRC-STATISTICS_BASICS@1`; the current tree also contains `EU-STATISTICS_BASICS-OPENSTAX@1` and `SRC-OPENSTAX-STATISTICS-BASICS@1`. The OpenStax source and EU are already in the exact-version master; the EU still lacks a claim-specific locator.

Current Claim A: statistics provides methods for describing data, analyzing variation and quantitatively supporting conclusions.

| Evidence Use | Direct locator candidate |
|---|---|
| NIST primary EU A | NIST/SEMATECH Engineering Statistics Handbook, Chapter 1 “Exploratory Data Analysis” → §1.1.1 “What is EDA?”; its approach, focus and techniques passages |
| OpenStax independent EU | *Introductory Statistics 2e*, §1.1 “Definitions of Statistics, Probability, and Key Terms”; definition of statistics, descriptive statistics, inferential statistics, sampling and interpretation |

Sources:
- NIST §1.1.1: https://itl.nist.gov/div898/handbook/eda/section1/eda11.htm
- OpenStax §1.1: https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms

The OpenStax §1.1 page directly defines statistics as collection, analysis, interpretation and presentation of data, and distinguishes descriptive from inferential statistics. The NIST EDA section directly describes graphical and quantitative techniques used to maximize insight, uncover structure, detect outliers and test assumptions. The two EUs are complementary; do not treat the engineering-focused NIST handbook as the only source for the general definition.

Claim C was separately researched in Batch 9 and should not be repeated here. Current Claim B is an additional record outside the historical Batch 3 denominator and is not included in this locator pass.

### 4.4 Thermodynamics Basics — Claim A; additional B/C outside Batch 3 denominator

Current base record: `CLM-THERMODYNAMICS_BASICS-A@1`, `EU-THERMODYNAMICS_BASICS-A@1`, `SRC-THERMODYNAMICS_BASICS@1`. The same current slice also contains Claims B/C, which were not part of historical Batch 3 and are therefore recorded as scope expansion.

| Claim | Current proposition | Direct locator candidate |
|---|---|---|
| A (Batch 3 base) | Thermodynamics studies energy transformations, heat transfer and work in macroscopic systems | Chapter 15 “Introduction to Thermodynamics” and §15.1 |
| B (scope expansion) | The first law expresses conservation of energy with heat transfer and work | §15.1 “The First Law of Thermodynamics”; ΔU = Q − W |
| C (scope expansion) | The second law constrains process direction and is related to entropy | §15.3 “Introduction to the Second Law of Thermodynamics: Heat Engines and Their Efficiency”; §15.6 “Entropy and the Second Law of Thermodynamics” |

Official sources:
- Chapter 15: https://openstax.org/books/college-physics-2e/pages/15-introduction-to-thermodynamics
- §15.1: https://openstax.org/books/college-physics-2e/pages/15-1-the-first-law-of-thermodynamics
- §15.3: https://openstax.org/books/college-physics-2e/pages/15-3-introduction-to-the-second-law-of-thermodynamics-heat-engines-and-their-efficiency
- §15.6: https://openstax.org/books/college-physics-2e/pages/15-6-entropy-and-the-second-law-of-thermodynamics-disorder-and-the-unavailability-of-energy

The existing Source title and Chapter 15 URL are appropriate. Pin Claim A to the chapter introduction and §15.1; B/C locators are research candidates for the extra Claims only and do not place those Claims in the candidate master.

### 4.5 Water Resource Management Basics — Claim A; additional B/C outside Batch 3 denominator

Current base record: `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_A@1`, `EU_WATER_RESOURCE_MANAGEMENT_BASICS_A@1`, `SRC_WATER_RESOURCE_MANAGEMENT_BASICS@1`. The existing Source identity is “UNESCO — Water resources” and the URL redirects to a broad UNESCO water programme page. That landing page does not directly support the Claim's explicit surface-water/groundwater proposition.

| Claim | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| A (Batch 3 base) | Water resources include surface water and groundwater supporting ecosystems and human uses | UN-Water “Water and Ecosystems” → “The issue explained”; USGS “Water cycle” → “Pools store water” and groundwater/surface-water passages | Direct |
| B (scope expansion) | Water-resource management balances multiple uses and environmental requirements | UNEP “Integrated Water Resources Management” → opening definition and paragraphs explaining interdependent uses and environmental flows | Direct |
| C (scope expansion) | Water availability and quality are influenced by natural processes and human activities | USGS “Water cycle” → “What is the water cycle?”, “What drives the water cycle?” and “Humans alter the water cycle”; UNEP IWRM for the management context | Direct |

Sources:
- UN-Water, “Water and Ecosystems”: https://www.unwater.org/water-facts/water-and-ecosystems
- USGS, “Water cycle”: https://www.usgs.gov/special-topics/water-science-school/water-cycle
- UNEP, “Integrated Water Resources Management”: https://www.unep.org/en/what-we-do/fresh-water/water-resources-management/integrated-water-resources-management

**Recommended source graph:** the current UNESCO portal may remain as contextual background, but should not be represented as direct support for all three Claims. The cleanest route is a source/locator update for Claim A and C using USGS/UN-Water, plus a distinct UNEP IWRM Source/Evidence Use chain for Claim B. Alternatively, a bounded Source identity correction can repoint the existing Source only if its current Claim dependency scope and every dependent EU are explicitly handled. New Source/EU IDs must be assigned by the canonical ID process; none are invented here.

## 5. Additional P9 Evidence Use re-review — Marine Biology and Pathology

Six current v1 EUs and two v1 Sources were re-fetched from the PR branch. These records are absent from the exact-version master and are added to the dependency reconciliation in §6.

### 5.1 Marine Biology — NOAA source fit is partial

Current Claims:
- `CLM_MARINE_BIOLOGY_BASICS_A@1`: marine biology studies marine organisms, life cycles, habitats and interactions.
- `CLM_MARINE_BIOLOGY_BASICS_B@1`: marine food webs connect organisms through feeding relationships and energy transfer.
- `CLM_MARINE_BIOLOGY_BASICS_C@1`: marine-organism status depends on physical/biological conditions including temperature, oxygen, habitat and human impacts.

Current independent EUs `EU_P9_MARINE_BIOLOGY_BASICS_A/B/C@1` all point to `SRC_NOAA_ECOSYSTEM_SCIENCE_2026@1`, “What is ecosystem science?”

NOAA source: https://oceanservice.noaa.gov/facts/ecosci.html

- EU A: NOAA defines ecosystem science as studying relationships among living organisms, physical features, biochemical processes, natural phenomena and human activities in ecological communities, and explicitly lists ocean ecosystems. This is partial contextual support, not a definition of marine biology or life-cycle study.
- EU B: the page does not describe feeding relationships, trophic levels or energy transfer. It does **not** directly support the marine food-web Claim.
- EU C: the page supports physical/biological conditions and human impacts at ecosystem level, but does not directly identify the Claim's temperature and dissolved-oxygen examples. Keep the support boundary explicit.

Better direct source for EU B: NOAA “Aquatic food webs”, which directly defines food webs, feeding relationships, energy flow and trophic levels, including marine organisms:
https://www.noaa.gov/education/resource-collections/marine-life/aquatic-food-webs

Recommended action: retain the NOAA ecosystem-science source only for the limited support it actually provides; add a separate NOAA aquatic-food-web Source/Evidence Use chain for Claim B after canonical ID allocation. For Claim C, add direct section locators or a more specific marine environmental source for temperature and oxygen. Do not mark all three independent EUs as direct support based on the current generic description.

### 5.2 Pathology — current NCBI source identity is materially mismatched

Current Claims:
- `CLM_PATHOLOGY_BASICS_A@1`: pathology studies the nature and causes of disease through changes in cell and tissue structure/function.
- `CLM_PATHOLOGY_BASICS_B@1`: pathology disciplines differ by object and method, including cellular, tissue and clinical-laboratory approaches.
- `CLM_PATHOLOGY_BASICS_C@1`: interpretation of a pathological finding depends on specimen, method and clinical/research context.

Current independent EUs `EU_P9_PATHOLOGY_BASICS_A/B/C@1` all point to `SRC_NCBI_HISTOLOGY_PATHOLOGY@1`, “Histology: The Lives and Deaths of Cells in Tissues.”

The linked NCBI Bookshelf item is actually Chapter 22 of Alberts et al., *Molecular Biology of the Cell*, 4th edition. NCBI states that, by agreement with the publisher, it is accessible through search but cannot be browsed. It is a cell-biology chapter, not a general pathology reference:
https://www.ncbi.nlm.nih.gov/sites/books/NBK21066/

This is not a satisfactory independent source for the broad Claims B/C, and its access/rights boundary needs review. Do not count the generic “independent pathology source corroborates” text as evidence.

Better direct candidates:
- NCBI/StatPearls, “Histology, Staining” — defines medical histology, explains tissue sectioning/staining, microscopic examination and pathologist interpretation in diagnosis; it also directly notes that stain choice depends on the investigational question and interpretation is informed by patient history:
  https://www.ncbi.nlm.nih.gov/books/NBK557663/
- Peer-reviewed PMC review, “Pathology: the clinical description of human disease” — describes pathology across molecular, cellular, tissue, fluid-chemistry and organism levels, and the pathologist's integration of clinical, gross, morphologic and molecular evidence:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC7380242/
- NCBI/StatPearls, “Histology, Cell Death” — direct for cellular injury, adaptation, apoptosis and necrosis:
  https://www.ncbi.nlm.nih.gov/books/NBK526045/

Recommended action: source-fit review before any canonical version change. The current NCBI book chapter may be retained only for the narrow cellular/tissue context it supports; it should not be presented as an independent pathology source for all three Claims. Use the review/StatPearls sources with exact locators and item-level rights checks.

## 6. Exact-version master reconciliation — 10 additional dependency records

The following current canonical records were re-fetched at PR HEAD `cbb620b1b2fc714414b57dc53ac7b8faba8980e1`, exact ID/version/type checked, and confirmed absent from the existing 1,119-row exact-version master:

| Exact key | Type | Slice | Decision |
|---|---|---|---|
| `EU_P9_MARINE_BIOLOGY_BASICS_A@1` | evidence_use | marine-biology-basics | HOLD |
| `EU_P9_MARINE_BIOLOGY_BASICS_B@1` | evidence_use | marine-biology-basics | HOLD |
| `EU_P9_MARINE_BIOLOGY_BASICS_C@1` | evidence_use | marine-biology-basics | HOLD |
| `SRC_NOAA_ECOSYSTEM_SCIENCE_2026@1` | source | marine-biology-basics | HOLD |
| `EU_P9_PATHOLOGY_BASICS_A@1` | evidence_use | pathology-basics | HOLD |
| `EU_P9_PATHOLOGY_BASICS_B@1` | evidence_use | pathology-basics | HOLD |
| `EU_P9_PATHOLOGY_BASICS_C@1` | evidence_use | pathology-basics | HOLD |
| `SRC_NCBI_HISTOLOGY_PATHOLOGY@1` | source | pathology-basics | HOLD |
| `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` | evidence_use | measurement-uncertainty-basics | HOLD |
| `SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY@1` | source | measurement-uncertainty-basics | HOLD |

These are ten additional dependency nodes, not ten new candidate Claims. The original 19/19 Batch 1 and 11/11 Batch 3 historical chain metrics remain unchanged. After adding these ten rows to the master, the reconciled totals become **1,129 unique exact-version rows = 1,058 candidate keys + 71 dependency records**. No candidate denominator or slice coverage count changes.

## 7. Current-slice Claim scope expansion — 24 known additional Claims outside the historical Batch 1/3 denominator

The following exact v1 Claim records exist in the current PR branch but are absent from the 1,058 candidate-key master. They must not be silently treated as first-edition candidates. The 21 records listed below were identified in the Batch 1/3 pass. Inclusion in the first-edition candidate pool requires explicit scope triage and dependency closure.

| Slice | Additional current Claim records |
|---|---|
| astronomy-basics | `CLM-ASTRONOMY_BASICS-B@1`, `CLM-ASTRONOMY_BASICS-C@1` |
| cell-basics | `CLM-CELL_BASICS-B@1`, `CLM-CELL_BASICS-C@1` |
| cell-biology-basics | `CLM-CELL_BIOLOGY_BASICS-B@1`, `CLM-CELL_BIOLOGY_BASICS-C@1` |
| evolution-basics | `CLM-EVOLUTION_BASICS-B@1`, `CLM-EVOLUTION_BASICS-C@1` |
| genetics-basics | `CLM-GENETICS_BASICS-B@1`, `CLM-GENETICS_BASICS-C@1` |
| immunology-basics | `CLM-IMMUNOLOGY_BASICS-B@1`, `CLM-IMMUNOLOGY_BASICS-C@1` |
| measurement-uncertainty-basics | `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1`, `CLM-MEASUREMENT_UNCERTAINTY_BASICS-C@1` |
| motion-basics | `CLM-MOTION_BASICS-B@1`, `CLM-MOTION_BASICS-C@1` |
| statistics-basics | `CLM-STATISTICS_BASICS-B@1` |
| thermodynamics-basics | `CLM-THERMODYNAMICS_BASICS-B@1`, `CLM-THERMODYNAMICS_BASICS-C@1` |
| water-resource-management-basics | `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_B@1`, `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_C@1` |

All 21 Claims listed above were checked against the exact-version master and were absent. Agricultural Engineering A–C were separately confirmed present in the exact-version master and are included in Batch 10. This is a corpus-scope reconciliation issue, not an automatic invitation to expand the first edition. The candidate owner must decide whether the 21 out-of-master Claims belong in the first-edition scope. If approved, they need their own exact Claim→EU→Source closure and substantive review. The count is the set identified in these reviewed slices, not a claim that the entire repository has been exhaustively scanned for every out-of-master Claim.

## 8. Rights and editorial gates

- OpenStax *Biology 2e* is CC BY-NC-SA 4.0 and the live page includes a restriction on LLM ingestion/generative-AI offerings without prior written permission. The project distribution and AI-assisted production model need owner/legal review.
- OpenStax *Microbiology* and *College Physics 2e* require item/edition-specific licence verification; no permission or commercial-use clearance is inferred from public access.
- NHGRI glossary, NASA, NOAA, USGS, USDA NRCS, FAO, UNEP, UN-Water, NIST and BIPM pages/publications require source-specific attribution and reuse review. Government/public-agency hosting is not by itself a blanket permission to reproduce every embedded image, table or contributed component.
- NCBI Bookshelf Chapter 22 is access-limited by publisher agreement; it should not be relied on as a broadly reusable or fully inspectable independent pathology source.
- All replacement Claims require independent subject-matter/editorial review. Biology/medical content requires especially careful boundaries; none of these educational references is a patient-specific diagnostic authority.
- All affected slices remain HOLD pending rights, editorial ownership, Human View and high-consequence review.

## 9. Recommended execution order

1. Reconcile the ten missing dependency nodes in the exact-version master (without changing the candidate denominator).
2. Implement locator-only work only after bounded authorization: Astronomy A–C, Cell Basics A–C, Motion A–C, Soil Microbiology A–C, Soil Science A/B, Statistics A (both EUs), Thermodynamics A, and the already-existing BIPM EU.
3. Correct Source identity/fit and obtain explicit Claim wording approval: Biodiversity C, Soil Science C, Evolution Source identity, Immunology Source URI/title, Water Resources Source graph, Marine Biology B/C, Pathology A–C.
4. Obtain subject-matter/editorial approval for the nine placeholder Claim replacements in Cell Biology, Genetics and Immunology.
5. Decide whether the 21 additional current Claims outside the master should enter the first-edition candidate scope. Do not add them to the denominator by inference.
6. Re-fetch all authorized records at one frozen HEAD, apply only exact versioned changes, update EUs and dependent references, run graph preflight and affected-slice tests, then run all required release gates on the final immutable HEAD.
7. Preserve HOLD until source rights, editorial review and Human View close. Structural/CI PASS does not prove truth, rights clearance or release eligibility.

## 10. Explicit non-actions

This research does not:
- authorize or perform any canonical JSON change;
- change any Claim statement or version;
- create new canonical Source/Evidence Use IDs;
- change publication_status or completion_status;
- change INCLUDE/HOLD/EXCLUDE decisions or candidate allowlists;
- promote any slice to release;
- modify Relations, validators, storage, recovery, package or release-gate semantics;
- merge PR #22, deploy or change `main`.

**Project-owner decision still required:** approve, reject or amend the bounded canonical remediation scope slice-by-slice, and separately decide whether the 21 additional current Claims should be admitted to the first-edition candidate pool.
