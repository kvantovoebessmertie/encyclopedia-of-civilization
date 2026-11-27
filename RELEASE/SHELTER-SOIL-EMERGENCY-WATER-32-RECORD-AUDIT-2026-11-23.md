# Shelter, Soil and Emergency Water — 32-record evidence and semantic audit

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `7c68ccb0d4d399d266aa92d80bbf910c8255c048`  
PR #22: OPEN / DRAFT / NOT MERGED

## Scope and method

Read-only re-fetch of all 13 records in `shelter-basics`, all 9 records in `soil-basics`, and all 10 records in `water`. Exact versions, blob SHAs, claim wording, EU-to-Claim/Source edges, source identity, Context/Scope target applicability and available public source passages were checked. This is an evidence/semantic audit, not a Human View, rights clearance, safety approval, release selection or full corpus audit.

## 1. Shelter basics — 13/13 records

### Exact records re-fetched

| Record ID | Version | Blob SHA |
|---|---:|---|
| CLM-SHELTER_BASICS-A | 1 | `a9adb58fe7fccf356210f830aa2d68bf7d85f6ed` |
| CLM-SHELTER_BASICS-B | 1 | `964fc6fa47a3c2140bf0eeb920e466b3b4d767a5` |
| CLM-SHELTER_BASICS-C | 1 | `f2fd2c2b8deae0cd3307061e9fd1b064e216dee0` |
| EU-SHELTER_BASICS-A | 1 | `6247088823f369ba84fde2242711c21799091df7` |
| EU-SHELTER_BASICS-B | 1 | `5035464a64a203efb1e5550929d2d2b7dd166f2e` |
| EU-SHELTER_BASICS-C | 1 | `27d4ff3762f72eca1d24a2a93dea8c0a4f3741a1` |
| EU_SHELTER_BASICS_RED_CROSS | 1 | `97ec1d92f2ebe4c06277ec408030cfe15886dd81` |
| CTX-SHELTER_BASICS | 1 | `fddf476f38a51afea16acd42d39541211b28fab1` |
| CTX-REL_M3_SHELTER_SETTLEMENT | 1 | `8911d849bb6d0b583f5451d409a5ec9747b15d21` |
| SCP-SHELTER_BASICS | 1 | `6b3f2525f580bf3919779069ec493e30e7de2390` |
| REL_M3_SHELTER_SETTLEMENT | 2 | `08db4137577ffbcad65b2cf72e10aad3e0bee391` |
| SRC-SHELTER_BASICS | 1 | `8f01a2fbc4674a685008cd66376141f43044bad8` |
| SRC_RED_CROSS_SHELTER_BASICS | 1 | `77f0ed60a599e77f24ba2fe5b33d486f080e5239` |

### Findings

- Claim A (shelter as a basic need under environmental exposure and emergencies) is broadly consistent with FEMA/Ready.gov and Red Cross disaster-shelter materials. The canonical Ready.gov source is only the root portal; it is not a pinpoint.
- Claim B bundles weather, water availability, ventilation and site safety as universal selection/arrangement factors. The inspected Red Cross shelter-finder page describes services at managed community shelters, not a universal checklist for choosing or constructing a temporary shelter. FEMA material differentiates shelter-in-place, extended stay and community shelters; high-wind and chemical incidents require different, sometimes opposite, actions. The current broad Claim is not adequately supported by the existing EU/source pair.
- Claim C (no universally safe shelter for all hazards) is a sound safety boundary, but needs an exact source passage demonstrating hazard-specific shelter/evacuation choices. FEMA hurricane guidance and Red Cross hurricane guidance support hazard-specific decisions; they do not establish every possible hazard class.
- Red Cross EU v1 points to Claim A and Red Cross Source v1; it is a corroborating service/shelter reference, not evidence for Claims B/C.
- The Red Cross source identity/URI is a public shelter finder. It supports information about services and access at opened shelters; it does not itself validate the physical safety of an arbitrary shelter location.
- Cross-slice Relation v2 correctly links the shelter Claim A and human-settlement-systems Claim B as an undirected relation. Its Context is a relation frame, not evidence for the shelter Claims.
- Context and Scope target Claim A only. They must not be presented as governing Claims B/C without separate records.
- High-consequence risk: generic wording could be misread as instructions to remain inside or select a shelter when evacuation is required. Local emergency instructions and hazard-specific official guidance take precedence.

### Required remediation

1. Replace the generic Ready.gov portal with precise, hazard-specific official locators (FEMA/Ready.gov and Red Cross) through separately versioned Source/Evidence Use records.
2. Split or narrow Claim B; do not imply that ventilation, water and generic site safety form one universal checklist. Chemical shelter-in-place guidance can require closing ventilation, while other contexts require different measures.
3. Keep Claim C bounded to the hazard-specific nature of protective actions and support it with more than one clearly scoped example.
4. Keep Red Cross EU limited to the Claim it actually supports.
5. Run specialist safety Human View and non-specialist reader review before any selection.

**Disposition: all three Claims HOLD.** No canonical records changed.

## 2. Soil basics — 9/9 records

### Exact records re-fetched

| Record ID | Version | Blob SHA |
|---|---:|---|
| CLM-SOIL_BASICS-A | 1 | `8361aa4e0fced72de5427b88c0c48e8c1afbd893` |
| CLM-SOIL_BASICS-B | 1 | `8a1a6fab404466146133c4dc15497a969fdbe959` |
| CLM-SOIL_BASICS-C | 1 | `022a62558702fbab79dc584c8ce55116c3d00341` |
| EU-SOIL_BASICS-A | 1 | `20e320b0f813e2c012ddf757b75d71c9ce6c0061` |
| EU-SOIL_BASICS-B | 1 | `96ed1489e30d39e13f1e7129536b23778d9b16aa` |
| EU-SOIL_BASICS-C | 1 | `a1e355906366b0e9cbb55438268947050c109187` |
| CTX-SOIL_BASICS | 1 | `c02bddff24a4502f6a38063ea295b11a39623fbb` |
| SCP-SOIL_BASICS | 1 | `33af90b59feb70aaf94403b29d18801ca608b4d9` |
| SRC-SOIL_BASICS | 1 | `e09d755f7590476c0ebe4ac4dec40d562e1c2e5b` |

### Findings

- Claim A's solids/liquid/gases framing aligns with the USDA NRCS soil definition: mineral and organic solids, liquid and gases. The live NRCS education page provides a direct definitional passage.
- Claim A additionally names living organisms as a separate component. NRCS's more complete definition includes mineral and organic matter, liquid and gases, while the soil-formation definition discusses macro- and microorganisms. The current statement is scientifically reasonable but the EU needs a pinpoint that directly supports the organism wording; avoid implying organisms are a fourth physical phase.
- Claim B bundles water movement, nutrient availability and plant-growth conditions. NRCS soil-function and soil-organic-matter materials support water flow/infiltration, nutrient cycling/availability and plant growth. One generic NRCS landing-page link is not enough to support the full bundle; each component needs a pinpoint and the role of organic matter/soil structure should not be overgeneralized to every soil.
- Claim C (soil properties vary by place and depth) is supported in principle by soil horizons and the NRCS description of soil formation, but the current source/EU does not identify the relevant passage. The wording should distinguish variation among soil profiles and horizons from a universal claim that every property always changes with depth.
- All three EUs are generic and point to the same NRCS source; none gives a formal section, paragraph, figure or page locator.
- Context and Scope target Claim A only. They do not automatically contextualize Claims B/C.
- The USDA NRCS page is an official public source, but public availability is not itself a complete licence assessment for reuse of any embedded graphics or third-party material. This package proposes text-only factual paraphrase and no asset reuse.

### Required remediation

1. Create versioned EUs with exact NRCS passages for soil composition/definition, soil functions and horizons/profile variation.
2. Consider a second independent soil-science source for Claim B's water/nutrient/plant-growth bundle.
3. Qualify Claim C to refer to profiles/horizons and site-specific properties, not an absolute rule for every soil/property.
4. Preserve the distinction between mineral/organic solids, soil water and soil air; living organisms are constituents of the soil system, not a separate phase.
5. Complete rights/attribution review and reader Human View.

**Disposition: all three Claims HOLD.** No canonical records changed.

## 3. Emergency water — 10/10 records

### Exact records re-fetched

| Record ID | Version | Blob SHA |
|---|---:|---|
| CLM-WATER-BOILING-EFFECTIVE | 1 | `d06635dda62f921ddb1c91fa37e16d44511d4b12` |
| CLM-WATER-BOILING-TIME | 1 | `2bde2b2bf39c3e3d9496bf8f5630b75b4c70b4e5` |
| CLM-WATER-CHEMICAL-LIMIT | 1 | `b7ac2ab38579c11113756234339a5f3ca74992f6` |
| CLM-WATER-INDEPENDENT-CORROBORATION | 1 | `cb633506abef534ff1d7c0c2ce07eeb9416b4745` |
| EU-WATER-BOILING-EFFECTIVE | 1 | `1033429c4706b092bd3e8d76089fd4c5c2a82894` |
| EU-WATER-BOILING-TIME | 1 | `4713c690c36fc07bc44ebacd23224bdbf018c5e6` |
| EU-WATER-CHEMICAL-LIMIT | 1 | `432b6cd5e593fbdb8e7cb9f3f657f5257da0443b` |
| EU-WATER-INDEPENDENT-CORROBORATION | 1 | `a3fe90d3e185ff06d6901e9568b2de8001f18848` |
| SRC-CDC-WATER-EMERGENCY-2024 | 1 | `6efae229c5292c2622b3cffa9e86928aefe810fd` |
| SRC-EPA-EMERGENCY-WATER-2026 | 1 | `c80df2ad26357e634eeabf2c5ef1f598abf5d8eb` |

### Findings

- CDC's current emergency-water page dated 2024-09-19 directly supports boiling as the most effective way to kill germs in water and gives the exact instruction: clear water at a rolling boil for 1 minute, or 3 minutes above 6,500 feet. It also instructs users to cool and store the water in clean, sanitized, covered containers.
- The boiling-time Claim is unusually specific and is accurately bounded to the cited CDC recommendation. Keep the U.S. altitude threshold and CDC recommendation context explicit; do not silently substitute a different authority's altitude threshold.
- CDC explicitly states that water containing fuel, toxic chemicals or radioactive materials cannot be made safe by boiling or disinfection. This directly supports the chemical-limit Claim.
- EPA independently supports boiling to kill most disease-causing microorganisms and says boiling/disinfection do not destroy contaminants such as heavy metals, salts and most other chemicals. EPA's altitude threshold differs from CDC's; do not combine the two instructions or imply a universal altitude number. The canonical independent-corroboration Claim currently avoids the altitude detail, which is appropriate.
- The four EUs are more specific than the generic EUs found in several other slices, but still lack formal locators (section headings/paragraphs). The current descriptions identify the relevant passages by subject, not stable pinpoint.
- The README correctly excludes universal treatment schemes, chemical-reagent dosages, region-specific water quality and individual medical decisions.
- Safety-critical boundary: boiling addresses biological hazards only. It does not remove fuel, toxic chemicals or radioactive contamination. The reader must not place the chemical-limit warning below or far away from the boiling instruction.
- The current CDC source is a maintained public-health page; EPA's page is official but older. Recheck live guidance at publication time and prioritize local public-health authority instructions where they differ.

### Required remediation

1. Version the four EUs with exact section/heading locators, retaining CDC as the authority for the 1-minute / 6,500-foot instruction.
2. Keep the chemical-contamination warning adjacent to any boiling guidance and in the same reader view.
3. Keep EPA corroboration separate from CDC's altitude-specific recommendation.
4. Add an explicit warning that cloudy water requires pre-treatment/settling and that the boiling procedure does not correct chemical contamination; avoid presenting this bounded slice as a complete water-treatment manual.
5. Complete safety specialist review, rights/attribution review and Human View.

**Disposition: all four Claims HOLD.** No canonical records changed.

## 4. Cross-slice conclusions and next work

1. **Emergency Water** has the strongest current evidence fit and the most urgent safety boundary. It is the best candidate for a tightly bounded, versioned EU-locator remediation package, followed by specialist safety review.
2. **Soil Basics** is a suitable low-to-moderate consequence explanatory candidate after exact NRCS locators and the composition/horizon wording are tightened.
3. **Shelter Basics** should not advance until Claims B/C are narrowed and hazard-specific evidence is linked. Shelter guidance is hazard-dependent and can be dangerous when generalized.
4. Do not copy these slices into a public manifest. All 10 Claims across the three slices remain HOLD.
5. No canonical JSON, Claim wording, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference, Decision, candidate register, denominator, coverage manifest or allowlist was changed.
6. No merge, deployment, public release or main-branch update was performed.

## 5. Public source checks

- CDC, “How to Make Water Safe in an Emergency” (2024-09-19): https://www.cdc.gov/water-emergency/about/index.html
- US EPA, “Emergency Disinfection of Drinking Water”: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water
- USDA NRCS, “What Is Soil?”: https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil
- USDA NRCS, “Soil Organic Matter”: https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil%20Organic%20Matter.pdf
- FEMA/Ready.gov, “Be Prepared for Any” hazard information sheets: https://www.ready.gov/sites/default/files/2025-02/fema_full-suite-hazard-info-sheets.pdf
- American Red Cross, “Hurricane Preparedness”: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/hurricane.html
- American Red Cross, “Disaster Shelters”: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html

## 6. Change-control

- All 32 canonical records were re-fetched at the exact inspection HEAD listed above.
- This report is the only intended change in this package.
- The report does not itself authorize canonical version increments or public inclusion.
- PR #22 remains OPEN / DRAFT / NOT MERGED; main remains unchanged.
