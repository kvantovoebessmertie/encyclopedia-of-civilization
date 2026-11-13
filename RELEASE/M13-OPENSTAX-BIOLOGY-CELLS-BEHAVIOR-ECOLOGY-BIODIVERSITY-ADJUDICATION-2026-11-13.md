# M13 duplicate-source adjudication: OpenStax Biology 2e — cells, behavior/ecology, biodiversity/conservation

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `2ac1f60fe49b057116b9ff5ef71515160f6a4b75`  
Scope: three shared-URI groups, six Source records and 18 linked Claims. Source, Evidence Use and Claim records were inspected directly; OpenStax chapter/section pages and licensing terms were checked separately.

## 1. Executive findings

| Shared-URI group | Source IDs | Claims | Adjudication |
|---|---:|---:|---|
| Cell structure | 2 | 6 | Both IDs point to the same Chapter 4 introduction. Three cell-basics Claims have relevant sections in the chapter, but their Evidence Use locators are too broad. The three cell-biology Claims are generic editorial statements, not biology facts. |
| Behavioral biology / Ecology | 2 | 6 | The shared URL is Chapter 46 Introduction, which is about ecosystems, not behavioral biology. The behavioral Source identity is mismatched to its URL; the correct OpenStax section is 45.7. The three ecology Claims are generic editorial statements. |
| Biodiversity / Conservation biology | 2 | 6 | The shared URL is §47.4 Preserving Biodiversity. It is relevant to conservation, but the Biodiversity Source identity points to a definition/levels Claim better supported by §47.1. The two Source IDs are not independent publications. |

**Totals: 6 Source records, 18 linked Claims, three same-URL groups.** All six Source records identify the same textbook, **OpenStax Biology 2e**. Different chapters/sections in one textbook are not independent corroborating publications. In two of the three groups, the same URL appears to be a copy-paste error that masks the intended distinct section.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed.

## 2. Cell structure — two IDs, same Chapter 4 introduction

### Source identity

- `SRC-CELL_BASICS`
- `SRC-CELL_BIOLOGY_BASICS`

Both point to `https://openstax.org/books/biology-2e/pages/4-introduction`. The first identifies “OpenStax Biology 2e — cell structure and function”; the second says “OpenStax Biology 2e — Cell Structure”. These are two records for one Chapter 4 introduction, not independent sources.

The introduction itself says cells are the building blocks of organisms and lists the Chapter 4 sections:
- §4.1 Studying Cells
- §4.2 Prokaryotic Cells
- §4.3 Eukaryotic Cells
- §4.4 The Endomembrane System and Proteins
- §4.5 The Cytoskeleton
- §4.6 Connections between Cells and Cellular Activities

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-CELL_BASICS-A` — a cell is the basic structural and functional unit of living organisms | Direct in OpenStax §4.1, which states that a cell is the smallest unit of a living thing and the basic building block of all organisms. The current Source URL is only the chapter introduction; add §4.1 as the pinpoint/source locator. |
| `CLM-CELL_BASICS-B` — prokaryotic cells lack a membrane-bound nucleus while eukaryotic cells have one | Direct in §§4.2–4.3. Section 4.2 says prokaryotes lack a nucleus and membrane-bound organelles; §4.3 says eukaryotic cells have a membrane-bound nucleus. |
| `CLM-CELL_BASICS-C` — cellular structures perform different functions within the cell | Direct in §4.3, which explains specialized organelle functions, and §§4.4–4.6 for further structures and activities. |
| `CLM-CELL_BIOLOGY_BASICS-A` — the slice introduces basic concepts and relationships needed to orient in the subject | This describes the Encyclopedia slice itself, not an external biological fact. OpenStax cannot establish that the project slice introduces those concepts. Reclassify as editorial/structural metadata or replace with an actual cell-biology Claim through authorized review. |
| `CLM-CELL_BIOLOGY_BASICS-B` — interpretation depends on source, context and applicability limits | This is a general evidence-method principle, not a cell-biology fact. It belongs in a methodology/epistemic standard, not as a Claim supported by a cell-structure textbook page. |
| `CLM-CELL_BIOLOGY_BASICS-C` — basic knowledge does not replace specialized verification when conditions, measurements or professional judgment matter | This is a scope/safety boundary, not a cell-biology fact. It needs a suitable policy or decision record, not the OpenStax cell chapter. |

### Disposition

One textbook source, two IDs. The cell-basics Claims have direct support in specific sections, but the current EU records cite only the Chapter 4 introduction and do not identify the relevant passages. The cell-biology-basics Claims are generic editorial statements and should not remain as ordinary documented-fact Claims without an authorized content-model decision.

## 3. Behavioral biology / Ecology — same URL, one misidentified source

### Source identity

- `SRC-BEHAVIORAL_BIOLOGY_BASICS` points to `https://openstax.org/books/biology-2e/pages/46-introduction`, but its Source identity says behavioral biology.
- `SRC-ECOLOGY_BASICS` points to the same URL and identifies OpenStax Biology 2e — Ecology.

The current OpenStax page title is **Ch. 46 Introduction**. Its outline is:
- §46.1 Ecology of Ecosystems
- §46.2 Energy Flow through Ecosystems
- §46.3 Biogeochemical Cycles

The page’s introduction is an ecosystem-dynamics case study. It is not a behavioral-biology section. The behavioral Source identity and URL do not match.

### Correct behavioral source candidate

OpenStax Biology 2e has a distinct section **§45.7 Behavioral Biology: Proximate and Ultimate Causes of Behavior** at:

`https://openstax.org/books/biology-2e/pages/45-7-behavioral-biology-proximate-and-ultimate-causes-of-behavior`

This section defines behavior as a change in an organism’s activity in response to a stimulus and behavioral biology as the study of the biological and evolutionary bases for such changes. It distinguishes innate behavior with a strong genetic component from learned behavior shaped by environmental conditioning.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-A` — behavior includes observable actions of an organism under particular conditions | Direct in OpenStax §45.7, which defines behavior as a change in activity in response to a stimulus. The current §46 URL is wrong. |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-B` — inherited traits and environmental factors can both influence behavior | Direct in §45.7, which distinguishes innate behavior with a strong genetic component from learned behavior shaped by environmental conditioning and experience. The current §46 URL is wrong. |
| `CLM-BEHAVIORAL_BIOLOGY_BASICS-C` — interpretation should describe observable conditions rather than assign unverified motives | Partial. §45.7 distinguishes proximate and ultimate causes and explains behavior through stimuli, inherited mechanisms and environmental learning. It does not state the exact “do not attribute unverified motives” rule. Add a methods source or narrow the Claim to the proximate/ultimate distinction. |
| `CLM-ECOLOGY_BASICS-A` — the slice introduces basic concepts and relationships needed to orient in ecology | This is a description of the Encyclopedia slice, not an external ecology fact. The Chapter 46 introduction cannot validate the project’s own structure. Reclassify as editorial/structural metadata or replace with a substantive ecology Claim. |
| `CLM-ECOLOGY_BASICS-B` — interpretation depends on source, context and applicability limits | General evidence-method principle, not an ecology fact. It belongs in a methodology standard, not an ecology Claim. |
| `CLM-ECOLOGY_BASICS-C` — basic knowledge does not replace specialized verification when conditions, measurements or professional judgment matter | General scope/safety boundary, not an ecology fact. It belongs in a policy/decision record rather than an ecology Claim. |

### Disposition

The two Source IDs must not be treated as proof that the same section supports both subjects. The behavioral record has a source-URL mismatch; §45.7 is the appropriate OpenStax section candidate. The ecology record points to a relevant ecosystem chapter, but its three linked Claims are generic editorial statements rather than domain facts.

## 4. Biodiversity / Conservation biology — same URL, one misidentified source

### Source identity

- `SRC-BIODIVERSITY_BASICS`
- `SRC-CONSERVATION_BIOLOGY_BASICS`

Both point to `https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity`. The conservation Source identity matches §47.4. The biodiversity Source identity describes diversity at multiple levels of organization, which is more directly covered by **§47.1 The Biodiversity Crisis**:

`https://openstax.org/books/biology-2e/pages/47-1-the-biodiversity-crisis`

Section 47.1 defines biodiversity in terms of species number/abundance and separately discusses genetic diversity and ecosystem diversity. It also describes the balance between speciation and extinction. Section 47.4 covers conservation methods, protected areas, preserve design and habitat restoration.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-BIODIVERSITY_BASICS-A` — biodiversity includes species diversity, genetic variation and ecosystem diversity | The current linked §47.4 is partial. OpenStax §47.1 directly covers species diversity, genetic diversity and ecosystem diversity (especially §§“Types of Biodiversity”). The current Source URL is too narrow/wrong for the full Claim. |
| `CLM-BIODIVERSITY_BASICS-B` — species numbers change through the balance of speciation and extinction | Direct in OpenStax §47.1, “Biodiversity Change through Geological Time”. The current §47.4 also discusses speciation and extinction in preserve-design context, but §47.1 is the precise locator. |
| `CLM-BIODIVERSITY_BASICS-C` — biodiversity assessment depends on area, time and observation method | Partial. §47.1 discusses measures, levels of organization, species distribution and species-area relationships; §47.4 discusses preserve size and design. The complete method/scale/time statement needs a more explicit biodiversity-monitoring or sampling reference. |
| `CLM-CONSERVATION_BIOLOGY_BASICS-A` — biodiversity is linked to species diversity and changing abundance over time | Direct-to-partial in §47.4, which discusses species numbers, migration, speciation and extinction; §47.1 is a more exact section for species abundance and biodiversity change. |
| `CLM-CONSERVATION_BIOLOGY_BASICS-B` — conservation considers populations, habitats and ecosystems | Direct in §47.4, particularly preserve design and habitat/ecosystem sections. |
| `CLM-CONSERVATION_BIOLOGY_BASICS-C` — habitat restoration is a tool for conserving biodiversity | Direct in §47.4, “Habitat Restoration”, which describes restoration as a mechanism for restoring and maintaining biodiversity and provides the Yellowstone example. |

### Disposition

One textbook, two Source IDs. The conservation Source points to the appropriate §47.4 page. The biodiversity Source should point to §47.1 or include it as an additional specific Source; the two URLs are different sections of the same book and do not provide independent corroboration.

## 5. OpenStax licensing boundary — relevant to the MVP

The OpenStax pages inspected state that Biology 2e uses a **Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)** license. The page also says:
- reuse/redistribution is limited to noncommercial purposes with attribution and ShareAlike terms;
- OpenStax images, activities and assessments are subject to the same restrictions, and commercial use requires permission;
- the textbook may not be used to train large language models or be ingested into generative-AI offerings without prior written permission.

This does not prevent citing OpenStax or independently paraphrasing factual material, but it does mean the MVP must not copy its text, figures or assessments without license-compatible handling. Any reuse in a commercial context or any LLM-training use requires separate rights review/permission. Keep source attribution and the noncommercial/share-alike boundary explicit in the project’s rights register.

## 6. Consolidated audit decision and next actions

1. Count OpenStax Biology 2e as one textbook for independence analysis. Different sections are useful distinct locators, not independent publications.
2. Keep all 18 Claims in the M13 denominator. Do not delete, merge or rewrite canonical records based only on duplicate URLs.
3. Prepare bounded source/locator corrections:
   - Cell basics: use §4.1 for the cell-unit Claim, §§4.2–4.3 for prokaryote/eukaryote differences, and §4.3–§4.6 for cell structures/functions.
   - Behavioral biology: correct the intended locator to §45.7; do not cite Chapter 46 ecosystems for behavioral biology.
   - Ecology: replace generic slice-description Claims with actual ecology facts or reclassify them as editorial metadata.
   - Biodiversity: use §47.1 for levels of biodiversity and speciation/extinction; retain §47.4 for conservation and habitat restoration.
   - Conservation: use §47.4 with exact subsection locators.
   - Cell-biology basics: resolve the three generic methodology/scope Claims through an authorized content-model decision.
4. Resolve OpenStax rights handling for the MVP: attribution, noncommercial use, ShareAlike obligations for any derivative material, no unlicensed figures/assessments, and no LLM-training use without permission.
5. Add section-specific locators to Evidence Use records only through authorized versioned corrections. Run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA after canonical changes.

## 7. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records source identity, link correctness, claim fit and licensing constraints. It is not a release approval or authorization to edit canonical records.
