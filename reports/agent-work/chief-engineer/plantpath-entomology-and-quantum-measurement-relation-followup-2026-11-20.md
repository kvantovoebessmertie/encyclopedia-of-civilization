# Plant Pathology / Entomology and Quantum / Measurement — Targeted Relation Evidence Follow-up

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Exact inspected branch HEAD: `cdf8d0b132fd1b5de3b76e23fdd4bf05cf205f6c`  
Status: **REPORT-ONLY TARGETED REVIEW; NEW EVIDENCE ROUTES IDENTIFIED; CANONICAL SOURCES / EVIDENCE USES REQUIRE SEPARATE AUTHORIZATION; HOLD PRESERVED**

## 1. Scope and method

Re-fetched two current semantic-HOLD Relations, their target-specific Contexts, participant Claims, current Evidence Use records and Source records at one exact PR branch HEAD. Checked official source pages for more direct cross-domain evidence.

This is a bounded desk review, not independent subject-matter approval, rights clearance, Human View, or publication decision. No canonical record, Relation, Context, Evidence Use, Source, candidate register, allowlist or publication state was changed.

## 2. Plant Pathology / Entomology

### Exact current graph

- Relation: `REL-CROSS-PLANTPATH-ENTOMOLOGY@2`
- Context: `CTX-REL-CROSS-PLANTPATH-ENTOMOLOGY@1`
- Reciprocal reference: Relation @2 → Context @1 → Relation @2.
- Relation type: `plant_health_and_insect_ecology_link`; two linked-record roles; undirected.

Participants:
- `CLM-PLANT_PATHOLOGY_BASICS-A@1`: “Фитопатология изучает болезни и расстройства растений.”
- `CLM-ENTOMOLOGY_BASICS-A@1`: “Энтомология изучает насекомых и в широком профессиональном употреблении также связанных с ними членистоногих.”

Current Claim-level evidence:
- Plant Pathology A@1 → `EU-PLANT_PATHOLOGY_BASICS-A@1` → `SRC-PLANT_PATHOLOGY_BASICS@1`, American Phytopathological Society (APS), “What Is Phytopathology?” The EU has no pinpoint locator.
- Entomology A@1 → `EU-ENTOMOLOGY_BASICS-A@1` → `SRC-ENTOMOLOGY_BASICS@1`, Entomological Society of America (ESA), “What Is Entomology?” The EU has no pinpoint locator.

The selected Claims are accurate discipline-level definitions, but neither endpoint states a plant–insect interaction or pathogen-vector mechanism. The current Relation therefore remains broader than the explicit proposition pair alone demonstrates.

### New direct source-fit findings

APS, “Plant Disease Profiles”:
https://www.apsnet.org/edcenter/learningPP/PDProfiles/Pages/default.aspx

The page says its profiles explain relationships between hosts, microbes and the environment that result in plant disease. Its bacterial-pathogen section notes relationships with insect vectors; its viral-pathogen section states that plant viruses are often vectored by insects or physical contact.

ESA, “What Is Entomology?”:
https://entsoc.org/about/what-is-entomology

The page explains that insects can destroy plants and damage crops, while other insects pollinate crops, prey on insect pests and recycle nutrients. Its agricultural-entomology section describes insect-pest management and crop protection.

Together these sources establish that plant pathology and entomology have concrete, documented points of contact: insect vectors of plant pathogens, insect damage to crops, pollination and biological control. They are more direct than the current generic discipline-definition Evidence Use descriptions.

### Assessment and safe next action

- The Relation type is plausible as contextual navigation between plant health and insect ecology.
- The current A/A endpoints remain generic definitions; they do not themselves state the vector mechanism.
- APS Plant Disease Profiles is a candidate relation-level bridge or a possible basis for a future claim-specific evidence path, but it is not currently represented in the canonical graph.
- The current APS and ESA Source/Evidence Use records do not have pinpoint locators.
- The new pages carry source-specific rights terms that have not been cleared for the Encyclopedia's final distribution model; the APS page footer states © APS, all rights reserved.

**Disposition: HOLD.** The new source discovery makes this a stronger remediation candidate, but no new Source, Evidence Use, endpoint substitution, Relation version or Context version is authorized here. A bounded owner authorization must define whether to add a relation-level Source, add claim-level evidence, or use a different existing endpoint. Independent plant-pathology / entomology review remains required.

## 3. Quantum / Measurement

### Exact current graph

- Relation: `REL-CROSS-QUANTUM-MEASUREMENT@2`
- Context: `CTX-REL-CROSS-QUANTUM-MEASUREMENT@1`
- Reciprocal reference: Relation @2 → Context @1 → Relation @2.
- Relation type: `quantum_and_measurement_link`; two linked-record roles; undirected.

Participants:
- `CLM-QUANTUM_MECHANICS_BASICS-A@1`: quantum physics describes physical systems at scales where quantum states and related probabilistic effects are significant.
- `CLM-MEASUREMENT_SCIENCE_BASICS-B@1`: a measurement result must be considered together with information needed for its interpretation and comparison.

Current Claim-level evidence:
- Quantum Claim A@1 → `EU-QUANTUM_MECHANICS_BASICS-A@1` → `SRC-QUANTUM_MECHANICS_BASICS@1`, NIST “Quantum Information Science”. The EU has no pinpoint locator.
- Measurement Claim B@1 → `EU-MEASUREMENT_SCIENCE_BASICS-B@1` → `SRC-MEASUREMENT_SCIENCE_BASICS@1`, BIPM International Vocabulary of Metrology (VIM). The EU has no pinpoint locator.

### Source URI defect and replacement candidate

The current NIST Source @1 uses:
https://www.nist.gov/topics/quantum-information-science

That exact URL currently returns HTTP 404. NIST's current “Quantum information science” page is available at:
https://www.nist.gov/quantum-information-science

The current NIST page directly states that:
- quantum information science combines quantum physics and information theory;
- quantum sensors support ultra-high-precision measurements;
- quantum effects set fundamental limits on the precision of physical measurements; and
- NIST studies and develops standards for quantum measurement.

A further NIST page, “Quantum Measurement Division”, describes NIST work using quantum behaviour to create measurement tools and capabilities and to improve precision measurement:
https://www.nist.gov/pml/quantum-measurement

These are direct source-fit routes for the Relation's quantum/measurement bridge. They do not establish that the generic BIPM VIM Claim B is a quantum-specific proposition.

### Assessment and safe next action

The endpoint pair is a defensible contextual-navigation candidate: one endpoint introduces quantum physical systems; the other explains how measurement results require interpretive information; NIST provides a concrete institutional and technical bridge between quantum effects and precision measurement.

However:
- the current NIST Source URI is stale (404);
- the current Quantum Evidence Use has no pinpoint locator;
- the current BIPM Evidence Use has no pinpoint locator;
- the NIST page supports the cross-domain Relation, but must not be represented as evidence for the generic BIPM measurement-interpretation Claim;
- rights and reuse conditions for NIST and BIPM material have not been cleared for the final distribution model.

**Disposition: HOLD.** This is a strong candidate for bounded source-identity/locator remediation and independent metrology/quantum-science review. The stale NIST URI should not be silently edited: a Source version increment and any dependent Evidence Use/Relation provenance alignment require explicit authorization. No canonical change is made in this report.

## 4. Comparative result

| Relation | New evidence result | Remaining blocker | Disposition |
|---|---|---|---|
| Plant Pathology / Entomology @2 | APS directly describes insect vectors of plant viruses; ESA documents insect effects on crops and plant systems | Existing A/A Claims are generic; current EUs lack locators; new APS page not in canonical graph; rights review | HOLD |
| Quantum / Measurement @2 | Current NIST page directly links quantum physics, quantum sensors and precision measurement | Existing NIST Source URL returns 404; EUs lack locators; source version and dependent references need bounded correction; rights review | HOLD |

## 5. Change-control and next steps

1. Request a bounded owner decision for the Plant Pathology / Entomology route: whether to add a Relation-level APS Source, add a Claim-level Evidence Use, or retain the existing A/A navigation pair without canonical change.
2. Request a separate bounded owner decision for Quantum / Measurement: version the NIST Source URI to its current official page and define exact Evidence Use locator corrections and any dependent reference alignment.
3. Obtain independent plant-pathology / entomology and quantum-metrology subject-matter reviews.
4. Complete source-specific rights review and project-level distribution compatibility.
5. Preserve both Relations and all affected slices on HOLD. Do not create INCLUDE/EXCLUDE decisions or a public allowlist.

No canonical JSON, standard, validator, test, candidate denominator, allowlist or release decision was changed. PR #22 remains Draft and unmerged; `main` remains unchanged.
