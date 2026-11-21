# Cross-Slice Semantic HOLD Follow-up — Current Endpoint and Evidence Recheck

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `45b67ef32e5b08c2e1ca21c2d96bc089c5b16243`  
Status: **REPORT-ONLY RECHECK — NO CANONICAL CHANGE; ALL REVIEWED RELATIONS REMAIN HOLD**

## 1. Scope and method

This follow-up re-fetches current Relation @2 records and their target-specific Context @1 records after the 2026-11-20 Context-isolation implementation. It checks the exact endpoint statements and existing Evidence Use / Source chains for six Relations from the 15-item semantic HOLD remediation register.

The audit is limited to the records named below. It does not certify full endpoint eligibility, rights, editorial approval, or release readiness. No canonical Content, test, Standard, register, allowlist, or publication state was changed. No endpoint was replaced and no HOLD was removed.

## 2. Exact Relation / Context target check

The six Relation @2 records were re-fetched from the current branch. Each corresponding Context @1 was also re-fetched and its `target_ref` confirmed to point to that exact Relation @2:

- `REL-CROSS-CO-EMERGENCY-ESCALATION@2` ↔ `CTX-REL-CROSS-CO-EMERGENCY-ESCALATION@1`
- `REL-CROSS-AIR-POWER-SYSTEMS@2` ↔ `CTX-REL-CROSS-AIR-POWER-SYSTEMS@1`
- `REL-CROSS-AMR-PLANT-HEALTH@2` ↔ `CTX-REL-CROSS-AMR-PLANT-HEALTH@1`
- `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2` ↔ `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1`
- `REL-CROSS-FOOD-PUBLIC-HEALTH@2` ↔ `CTX-REL-CROSS-FOOD-PUBLIC-HEALTH@1`
- `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2` ↔ `CTX-REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1`

The bounded Context condition remains: the link is limited to the stated Relation type and does not replace the Claims, Scope, or Evidence Use. This confirms the Context-target architecture for these six pairs only; it does not establish semantic correctness of the Relations.

## 3. Relation-by-relation findings

### 3.1 `REL-CROSS-CO-EMERGENCY-ESCALATION@2` — retain semantic HOLD

**Exact endpoints**
- `CLM-CO-HEATING-EMERGENCY@1`: on a CO alarm or possible poisoning symptoms, immediately go to fresh air, seek emergency medical help, and do not return before safety is checked.
- `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`: the same immediate response, with the additional condition that exposure occurs while a generator is operating.

**Evidence checked**
- CPSC, *Carbon-Monoxide-Questions-and-Answers*: alarm response section directs people outside, to emergency services, and prohibits re-entry until responders authorize it.
- CDC, *What to Do to Protect Yourself During a Power Outage*, “Carbon monoxide poisoning” and “Know what to do”: identifies generator-related CO hazards and emergency response.

**Assessment**
The source contexts are materially distinct (general residential CO alarm response versus generator use during power outages), but the two Claim propositions substantially repeat the same immediate escalation sequence. The generator-specific Claim does not currently state the additional generator-placement/prevention guidance that is present in the CDC source. The Relation can serve as a navigation pointer between a general and a generator-specific scenario, but its present endpoint pair adds little distinct knowledge.

**Disposition:** HOLD. Reconsider only if editorial review establishes a distinct contribution for both endpoints or the Relation is deliberately narrowed to scenario navigation. Do not treat the shared action as two independent pieces of evidence for the same proposition. Both Evidence Use descriptions are broad and lack pinpoint locators.

### 3.2 `REL-CROSS-AIR-POWER-SYSTEMS@2` — retain semantic HOLD

**Exact endpoints**
- `CLM-AIR_QUALITY_BASICS-A@1`: air-quality monitoring measures pollutant concentrations at observation stations.
- `CLM-POWER_SYSTEMS_BASICS-A@1`: an electric power system combines generation, transmission, distribution, and load.

**Assessment**
These are independently valid descriptions of two systems. Neither Claim states an interaction, dependency, emissions pathway, monitoring requirement for power infrastructure, or effect of power generation on ambient air. Their shared environmental/energy subject area does not establish the typed Relation `air_quality_and_energy_systems_link`.

Both Evidence Use records currently provide generic descriptions without pinpoint locators. The existing Source identities (US EPA AirData and NREL's *The North American Electric Power System: The Grid*) match the respective domains but do not, by themselves, bridge the two Claim propositions.

**Disposition:** HOLD. No direct endpoint alternative was established in this bounded recheck. Do not infer a power/air interaction from general domain knowledge or source co-presence.

### 3.3 `REL-CROSS-AMR-PLANT-HEALTH@2` — actionable candidate for semantic re-review; do not close HOLD yet

**Exact endpoints**
- `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`: resistance affects people, animals, plants, food systems, and the environment and requires an intersectoral approach.
- `CLM-PLANT_PATHOLOGY_BASICS-A@1`: phytopathology studies plant diseases and disorders.

**Newly checked source content**
The current WHO Antimicrobial Resistance fact sheet is dated 16 July 2026. Its overview states that antimicrobials are used to prevent and treat infectious diseases in people, animals, and plants; its societal-impact section says drug-resistant infections affect plant health and farm productivity. The existing canonical WHO Source URL is the same fact-sheet URL.

The current American Phytopathological Society page, *What Is Phytopathology?*, identifies plant pathology as the study and management of plant diseases. The existing APS Source URL is the same page.

**Assessment**
This is more directly aligned than the original HOLD rationale alone suggests: the current WHO source explicitly connects AMR to plant infections/plant health, while the APS source establishes the plant-disease domain. The Relation type `one_health_plant_health_link` may be defensible as contextual navigation between AMR and plant pathology.

However, the current AMR Evidence Use has only a generic description and no pinpoint locator. The Plant Pathology Evidence Use is also generic. The exact source passages must be pinned to the Claims, and the current canonical Claim wording must be checked against the version/date of the source material. This report does not assume that an updated web page silently upgrades historical Evidence Use verification.

**Disposition:** retain HOLD pending bounded evidence-locator/version review and independent semantic adjudication. This is the strongest actionable candidate in this six-Relation batch; it is not a promotion or approval.

Potential locator candidates for a future authorized review:
- WHO, *Antimicrobial resistance*, 16 July 2026, “Overview” and “Societal impacts” sections: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- American Phytopathological Society, *What Is Phytopathology?*, “The Study of Plant Disease” / “Understanding and Managing Plant Diseases”: https://www.apsnet.org/careers/Pages/WhatisPhytopathology.aspx

### 3.4 `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2` — retain semantic HOLD

**Exact endpoints**
- `CLM-GROUNDWATER_BASICS-A@1`: groundwater occurs in saturated pores and fractures of soils and rocks.
- `CLM-SOIL_MICROBIOLOGY_BASICS-A@1`: soil contains complex communities of microorganisms and other organisms.

**Assessment**
The Claims identify groundwater's physical setting and the biological complexity of soil. Neither Claim states a groundwater–microorganism interaction, transport mechanism, recharge effect, contaminant pathway, or ecological dependency. The Relation type `subsurface_water_and_soil_biology_link` implies more than the two endpoint propositions establish.

Both Evidence Use records are generic and contain no pinpoint locator. The Source identities (USGS Groundwater Basics and USDA NRCS Soil Health Starter Kit) are domain-relevant but do not create a relation absent an explicit proposition.

**Disposition:** HOLD. A future replacement must use an existing exact-version Claim that directly states a groundwater–microbe or groundwater–soil ecological mechanism and has its own locator. No such endpoint was established in this bounded scan.

### 3.5 `REL-CROSS-FOOD-PUBLIC-HEALTH@2` — retain semantic HOLD

**Exact endpoints**
- `CLM-FOOD_SECURITY_BASICS-D@1`: household food security means all members have access at all times to enough food for an active, healthy life.
- `CLM-PUBLIC_HEALTH_BASICS-A@1`: public health aims to improve population health and prevent disease.

**Evidence checked**
The current USDA ERS *Food Security in the U.S. — Measurement* page, updated 30 March 2026, defines household food security and distinguishes household-level food access from individual hunger. Its “What Is Food Security?” section is a suitable pinpoint for the existing Claim D.

**Assessment**
The wording shares a broad health orientation, but the selected public-health Claim is only a general definition and does not state a food-security determinant, nutrition pathway, food-insecurity health effect, or population-level mechanism. The current USDA page is principally a definition/measurement source; it does not turn these two narrow Claims into a demonstrated population-health relationship.

Both Evidence Use descriptions are generic. A more direct endpoint would need to state a documented food insecurity/nutrition/public-health relationship and have its own evidence chain.

**Disposition:** HOLD. The USDA “What Is Food Security?” section is a candidate locator for Claim D only; it does not resolve the Relation. Do not infer causation or health outcomes from the definition.

### 3.6 `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2` — retain semantic HOLD

**Exact endpoints**
- `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1`: integrated settlement planning links spatial, infrastructure, social, and environmental aspects rather than treating them in isolation.
- `CLM-PUBLIC_HEALTH_BASICS-A@1`: public health aims to improve population health and prevent disease.

**Assessment**
The settlement Claim supports an integrated, cross-sector planning model, but does not explicitly identify public health, health services, sanitation, housing-health effects, or disease prevention as one of the linked aspects. The public-health Claim is a generic disciplinary-purpose statement. Their combination may be a useful topical navigation route, but the current endpoints do not state the specific system relationship implied by `settlement_public_health_system_link`.

The settlement Evidence Use refers to OECD cross-sector urban-development integration; the public-health Evidence Use refers generically to WHO public-health material. Neither current Evidence Use supplies a pinpoint that demonstrates the specific settlement/public-health link.

**Disposition:** HOLD. A future repair needs an existing exact-version Claim about a settlement-health mechanism (e.g. water/sanitation, housing, environmental health, or service access) with direct evidence. Do not infer health effects or service availability from integrated planning alone.

## 4. Consolidated result

| Relation | Current result | Safe next action |
|---|---|---|
| CO emergency escalation @2 | HOLD — substantial proposition overlap | Editorial distinct-contribution test; no duplicate evidence credit |
| Air / power systems @2 | HOLD — no stated interaction | Find an existing interaction Claim or retain HOLD |
| AMR / plant health @2 | HOLD — plausible direct link now identified, but EU locators are weak | Bounded locator/version review; independent semantic re-adjudication |
| Groundwater / soil microbiology @2 | HOLD — no stated mechanism | Existing mechanism Claim with exact evidence, otherwise retain |
| Food / public health @2 | HOLD — broad conceptual overlap only | Direct food-health endpoint needed |
| Settlement / public health @2 | HOLD — broad integrated-planning overlap only | Direct settlement-health endpoint needed |

This review also confirms that the six Relation-specific Contexts target their exact current Relation versions. That structural result does not alter any semantic disposition.

## 5. Scope, authorization, and release boundary

- No Relation or Context was changed.
- No Claim, Evidence Use, Source, Scope, Event, State, or Object was changed.
- No candidate key or Part II slice was added.
- No relation endpoint was substituted.
- No INCLUDE, EXCLUDE, or public allowlist decision was made.
- All six Relations remain HOLD.
- Any canonical repair requires its own bounded authorization, exact version increments, source-specific evidence review, reciprocal-reference validation, and exact-head CI.
- Rights, editorial ownership, Human View, and release approval remain independent gates.

**Acceptance:** accept this document as a report-only recheck of six semantic HOLD Relations. It is not a closure report and does not approve publication.
