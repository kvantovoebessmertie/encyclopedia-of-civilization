# Part I — Survival and Preservation of Life
## First-edition reader-facing implementation and completion register

Date: 2026-11-18  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **SECTION ARCHITECTURE AND EDITORIAL IMPLEMENTATION COMPLETE; RECORD-LEVEL PUBLICATION NOT APPROVED**  
Scope: Part I only. This document does not authorize publication, deployment, or changes to canonical Claims.

## 1. Purpose and reader promise

Part I is the Encyclopedia's standalone opening section. It helps a reader orient themselves when life, health, shelter, water, food, energy, or community continuity is threatened. It is not a substitute for emergency services, local authorities, trained professionals, or current jurisdiction-specific instructions.

The section is deliberately practical without pretending that a general-purpose encyclopedia can safely prescribe every action in every place. It teaches the reader to:
- recognize the kind of problem and the information needed to assess it;
- distinguish immediate danger from longer-term resilience;
- identify when official instructions or qualified help take precedence;
- understand the systems behind essential needs;
- recognize uncertainty, unsafe improvisation, and the limits of their own competence;
- preserve resources and coordinate with other people without creating additional hazards.

The section is not a claim that survival is reducible to a checklist. It is the first doorway into the full Encyclopedia.

## 2. Fixed reading order and chapter briefs

### Chapter 1. Orientation, warnings, and emergency coordination

**Reader outcome.** The reader understands how to orient themselves before acting: identify the hazard, establish whether there is an immediate threat, locate authoritative local information, communicate the situation, and recognize when professional emergency response is required.

**Coverage.** Warning systems and alerts; emergency information; incident coordination; disaster risk and response; humanitarian logistics.

**Existing candidate slices.** `emergency-alert-warning`, `disaster-response-basics`, `emergency-management-basics`, `disaster-risk-reduction-basics`, `humanitarian-logistics-basics`.

**Editorial boundaries.** Alert examples are jurisdiction-specific. A warning is not a universal instruction. Local emergency-service and authority directions take precedence. Do not imply that a reader should enter a hazardous area to verify information.

### Chapter 2. Water: access, quality, storage, and sanitation systems

**Reader outcome.** The reader understands that water availability and water safety are different questions; that contamination type matters; and that storage, treatment, infrastructure, and wastewater are connected but not interchangeable topics.

**Coverage.** Water resources; household and emergency storage; source assessment; filtration and treatment assessment; chemical and microbial hazards; hydrology; water infrastructure; wastewater.

**Existing candidate slices.** `water`, `water-resources-basics`, `water-filter-assessment`, `water-treatment-basics`, `chemical-water-advisory`, `emergency-water-storage-state`, `water-infrastructure-basics`, `hydrology-basics`, `wastewater-basics`, `wastewater-engineering-basics`.

**Editorial boundaries.** No universal treatment recipe. Boiling is not a remedy for chemical contamination. Product claims about filters must not be generalized beyond the tested contaminant and operating conditions. Local advisories and qualified water authorities govern emergency use. Any operational treatment advice remains HOLD until exact source passages, conditions, and specialist review are confirmed.

### Chapter 3. Food, nutrition, and food security

**Reader outcome.** The reader can distinguish food safety, preservation, nutrition, and food availability as related but different problems; understand that time, temperature, contamination, and storage conditions affect safety; and recognize when food should not be consumed.

**Coverage.** Food safety; preservation; outage and flood conditions; food security; nutrition; food science.

**Existing candidate slices.** `power-outage-food`, `flood-food-safety`, `food-security-basics`, `food-safety-basics`, `food-preservation-basics`, `food-science-basics`, `nutrition-basics`, `nutrition-science-basics`.

**Editorial boundaries.** Do not turn a general temperature/time reference into a guarantee for every food, appliance, or exposure history. Do not publish preservation procedures without validated conditions and exact evidence. Nutrition information is general education, not individualized medical advice. Reuse P2 reviews for the previously audited food slices; do not repeat their closed substantive or Human View work.

### Chapter 4. Shelter, housing, and safe construction principles

**Reader outcome.** The reader understands the functions of shelter, the role of weather and building systems, and the distinction between basic observation and structural assessment.

**Coverage.** Shelter needs; housing systems; building science; materials and construction principles; settlement and civil infrastructure.

**Existing candidate slices.** `shelter-basics`, `construction-basics`, `housing-systems-basics`, `architecture-basics`, `civil-engineering-basics`, `human-settlement-systems-basics`.

**Editorial boundaries.** No DIY structural certification, load-bearing modification instructions, or claims that visible inspection proves a building safe. Damaged structures, gas/electrical hazards, and unstable ground require appropriate authorities or qualified professionals. M3 shelter review may be reused only within its exact recorded scope and checkpoint status.

### Chapter 5. Health, hygiene, sanitation, and first aid

**Reader outcome.** The reader understands prevention, hygiene, sanitation, exposure risks, basic first-aid boundaries, and the importance of timely escalation to medical services.

**Coverage.** Hand hygiene; waste and wastewater; sanitation; public and environmental health; infection and epidemiology foundations; basic injury information and burn first aid; anatomy and physiology as supporting knowledge.

**Existing candidate slices.** `emergency-hand-hygiene`, `emergency-waste-sanitation`, `septic-system-emergency`, `sanitation-basics`, `waste-management-basics`, `public-health-basics`, `environmental-health-basics`, `burn-first-aid`, `anatomy-basics`, `physiology-basics`, `microbiology-basics`, `epidemiology-basics`, `nutrition-basics`, `sleep-basics`.

**Editorial boundaries.** No diagnosis, individualized treatment, medication dosing, invasive procedures, or substitution for emergency medical care. First-aid material must state what it does not cover and when to seek urgent help. Wastewater/septic instructions require exact local and technical boundaries. Medical and sanitation procedures remain HOLD without appropriate qualified review.

### Chapter 6. Heat, fire, electricity, energy, and lighting

**Reader outcome.** The reader understands common household and environmental hazards, the importance of prevention and early warning, and why improvised heating, generators, electrical work, and fire response can be dangerous.

**Coverage.** Fire and smoke safety; wildfire smoke; heat and cold exposure; carbon monoxide; emergency lighting; electricity; energy systems and storage.

**Existing candidate slices.** `fire`, `home-fire-smoke-safety`, `wildfire-smoke-safety`, `fire-safety-basics`, `extreme-heat-safety`, `cold-weather-hypothermia`, `carbon-monoxide-heating-safety`, `generator-carbon-monoxide-safety`, `emergency-lighting-safety`, `electricity-basics`, `electrical-safety-basics`, `energy-basics`, `energy-systems-basics`, `energy-storage-basics`, `renewable-energy-basics`.

**Editorial boundaries.** No instructions for hazardous firefighting, live electrical work, generator operation in enclosed or partially enclosed spaces, or improvised combustion heating. CO is an invisible life-threatening hazard; warnings and evacuation/escalation guidance must be prominent. Weather exposure guidance is context-sensitive. Reuse P1 and M3 audits only within their exact scope; all high-consequence operational claims require enhanced review.

### Chapter 7. Tools, materials, repair, and making

**Reader outcome.** The reader understands basic tool selection and inspection, common material properties, and the limits of repair without training or appropriate protective equipment.

**Coverage.** Hand-tool safety; materials; material science; manufacturing and repair principles.

**Existing candidate slices.** `hand-tool-safety`, `materials-basics`, `materials-science-basics`, `manufacturing-basics`, `manufacturing-systems-basics`, `robotics-basics`.

**Editorial boundaries.** Do not infer PPE or defective-tool requirements from a Context/Scope pair attached to a different Claim. No dangerous machine modification or hazardous fabrication procedures. Reuse P1 review for the hand-tool slice and preserve the exact per-Claim boundaries in the existing manifest.

### Chapter 8. Land, agriculture, soil, seeds, plants, and animals

**Reader outcome.** The reader understands the biological and ecological foundations of food production and resource stewardship, including the limits imposed by climate, soil, water, pests, animal health, and local ecosystems.

**Coverage.** Agriculture; soil; seed storage; plant biology and physiology; forestry; fisheries; livestock; zoology; ecology; ecosystems; fermentation as a food-system topic.

**Existing candidate slices.** `agriculture-basics`, `early-agriculture`, `soil-basics`, `seed-storage-basics`, `plant-biology-basics`, `plant-physiology-basics`, `forestry-basics`, `fisheries-basics`, `livestock-systems-basics`, `zoology-basics`, `ecology-basics`, `ecosystems-basics`, `food-fermentation-basics`.

**Editorial boundaries.** General biological explanation must be separated from locally actionable growing, harvesting, animal-health, or food-safety advice. Do not imply that wild plants, fungi, water, or animals are safe to consume without reliable identification and local expertise. Plant-biology candidate already screened in an earlier pilot remains HOLD; do not silently replace that decision.

### Chapter 9. Natural and environmental hazards

**Reader outcome.** The reader understands hazard mechanisms and the difference between general science, preparedness information, and time- and place-specific protective instructions.

**Coverage.** Earthquakes and aftershocks; floods and cleanup; weather and climate; geology, seismology, volcanology; wildfire smoke; ocean hazards.

**Existing candidate slices.** `earthquake-protective-action`, `earthquake-aftershock-safety`, `flood`, `flood-cleanup-safety`, `flood-food-safety`, `weather-basics`, `climate-basics`, `geology-basics`, `seismology-basics`, `volcanology-basics`, `wildfire-smoke-safety`, `ocean-basics`.

**Editorial boundaries.** No universal evacuation thresholds, route safety guarantees, or hazard forecasts. Local official alerts take precedence. Cleanup may involve electrical, chemical, structural, sewage, and biological hazards; do not frame it as routine household work. The previously screened climate Claim remains HOLD pending its own exact gates.

### Chapter 10. Communication, navigation, transport, and logistics

**Reader outcome.** The reader understands how maps, coordinates, communication networks, transport, and supply chains support individual and community resilience.

**Coverage.** Maps and navigation; geographic coordinates; telecommunications and networks; public risk communication; transportation and public transport; infrastructure and humanitarian logistics.

**Existing candidate slices.** `maps-and-navigation-basics`, `geographic-coordinates-basics`, `telecommunications-basics`, `networks-basics`, `public-risk-communication-basics`, `transportation-basics`, `public-transport-basics`, `humanitarian-logistics-basics`, `infrastructure-basics`.

**Editorial boundaries.** Do not publish sensitive infrastructure details or imply that a route/network is available during a live incident. Maps and coordinate systems require clear datum, scale, currency, and uncertainty where relevant. Do not invent Relations between slices; only display canonical, source-supported Relations.

## 3. Cross-chapter reader pathways

These are conceptual navigation paths, not new Claims or evidence. They may be rendered as links only where canonical Relations and record-level provenance support the connection.

1. Water need → water resources → hydrology → chemistry/microbiology → treatment assessment → storage → public health.
2. Food need → food safety/preservation → nutrition → agriculture → soil and plant biology → ecology and climate.
3. Shelter need → materials → mechanics → construction → settlements → infrastructure and governance.
4. Illness or injury → anatomy/physiology → microbiology/epidemiology → first-aid boundaries → public health.
5. Energy need → physics/thermodynamics → electricity → generation/storage → infrastructure → safety.
6. Hazard response → earth/weather/climate science → warning systems → communication → logistics → governance.
7. Community recovery → agriculture/production → engineering → transport/networks → economics → institutions and education.

Do not create a Relation merely to make a pathway visually complete. Existing M3 food-preservation relation `REL_M3_FOOD_PRESERVATION_SAFETY@1` is preserved; do not duplicate it.

## 4. Candidate disposition and known evidence

### 4.1 Exact screened manifest already present

The existing `FIRST-EDITION-SURVIVAL-CANDIDATE-MANIFEST-2026-11-18.md` contains 112 exact records across nine slices, including 33 Claims. Every listed record is currently @1 and every row is HOLD. The nine slices are:
- emergency-alert-warning — 10 records / 3 Claims;
- hand-tool-safety — 10 / 3;
- home-fire-smoke-safety — 12 / 4;
- emergency-lighting-safety — 12 / 4;
- septic-system-emergency — 12 / 4;
- food-safety-basics — 12 / 4;
- food-preservation-basics — 12 / 3;
- flood-food-safety — 10 / 3;
- power-outage-food — 22 / 5.

The manifest pins exact Claim → Evidence Use → Source chains and per-Claim Context/Scope targets. Its HOLD decisions are retained. It is not silently expanded into an INCLUDE list.

### 4.2 Reused audit evidence — no repeat adjudication

- P1 emergency remainder: hand-tool safety, home fire/smoke safety, emergency lighting, emergency alerts, septic emergency. Existing substantive, evidence-diversity, scope/limits, cross-domain and Human View findings are reused. The P1 checkpoint remains validation-pending.
- P2 food resilience: food safety, food preservation, flood food safety, power-outage food. Existing substantive and Human View results are reused. The P2 checkpoint remains a candidate pending independent validation.
- M3: fire safety, shelter, water resources, food preservation, scientific method, emergency management. Existing substantive and Human View findings and the six recorded Relations are reused. M3 checkpoint remains a candidate, not a final release approval.
- Additional existing slices such as chemical-water-advisory, emergency-waste-sanitation, cold-weather-hypothermia, extreme-heat-safety, burn-first-aid, maps-and-navigation-basics, and emergency-management-basics are structural candidates only unless a separate exact review record establishes more.

No historical adjudication is repeated by this implementation.

### 4.3 Existing pilot decisions preserved

The prior pilot's four HOLD decisions remain unchanged:
- `CLM-PLANT_BIOLOGY_BASICS-A@1`
- `CLM-STATISTICS_BASICS-A@1`
- `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- `CLM-CLIMATE_BASICS-A@1`

They are not promoted by this section plan.

## 5. Publication-state register for Part I

| Candidate set | Current decision | Reason |
|---|---|---|
| 112 records in the nine-slice exact manifest | HOLD | Exact inventory exists; P1/P2 reuse is documented; checkpoint validation, locator/rights, consequence review and editorial approval remain open |
| Other slices named in the ten chapter briefs | HOLD — structural only | Slice membership is not record-level screening; exact IDs/versions/dependencies and review state have not been assembled here |
| High-consequence operational instructions (water treatment, medical/first aid, electrical, structural, chemical, fire, CO, sewage, hazard response) | HOLD | Qualified review and explicit safety boundaries required |
| Four previously screened pilot Claims | HOLD | Preserve existing decisions |
| Records not appropriate to the first survival section | EXCLUDE from Part I only, not deleted | Exclusion from this section is not a judgment that the record is invalid or should be removed from the Encyclopedia |

**INCLUDE: 0 records at this stage.** This is intentional. No record is promoted without complete exact-version gates.

## 6. Minimum publication gates

A candidate can move from HOLD to INCLUDE only when all applicable checks are recorded against the exact record version:

1. Exact ID, version, type, slice and canonical file hash.
2. Complete dependency chain: Claim, Evidence Use, Source, and applicable Context/Scope, plus exact target boundaries.
3. Source locator checked against the cited source passage; no invented or generic locator.
4. Applicability, jurisdiction, date, units, uncertainty and known limitations made explicit.
5. Rights and attribution status verified for the record and source material.
6. Substantive review state current and traceable; historical scores are not silently treated as current.
7. Human View: non-specialist comprehension, visible limitations, no misleading certainty.
8. Enhanced qualified review for high-consequence operational content.
9. Existing Relations verified; no artificial or duplicate relations.
10. Exact-head regression, Reference tests, Release Conformance Gate, security and Offline Edition pass.
11. Actual generated reader/offline artifact inspected; only allowlisted records appear.
12. Independent reviewer and accountable owner approve the bounded release.

A green CI run is necessary where required but never proves substantive safety or editorial approval.

## 7. Governance decisions that cannot be made by implementation

The repository's owner-decision record remains authoritative. The following require explicit owner decisions and must not be guessed by an implementer:
- publication license and reuse/commercial terms;
- named accountable editor and release approver;
- correction contact and urgent takedown responsibility;
- distribution channel and whether any hosted service exists;
- publication languages and translation responsibility;
- whether personal data is collected; if so, privacy notice, retention and deletion rules.

Until these are decided, use no public hosted contribution endpoint and do not claim a public release. A local/manual contribution route is the safer initial operating mode.

## 8. Reader and artifact implementation constraints

The current reader prototype and offline build may be reused, but this document does not claim that a real Part I edition has been built. The existing synthetic preview is not a real-content release artifact. The SI private preview is not Part I and remains private/non-redistributable.

When the Part I allowlist exists:
- pass only the exact allowlist to the existing builder;
- fail closed on unknown IDs, versions, record types or dependencies;
- exclude audit notes, internal decisions, private contact data and all HOLD/EXCLUDE records;
- render review status and limitations in plain language;
- keep the output offline-capable and deterministic;
- record source revision and content hashes in the manifest;
- inspect desktop and mobile output and test keyboard navigation, search, no-match behavior, escaping and network isolation.

## 9. Completion statement and remaining work

**Completed in this work block:** Part I's standalone role, ten-chapter reader sequence, chapter outcomes, subject coverage, slice mapping, safety/editorial boundaries, supported conceptual pathways, preservation of existing audit decisions, and publication gate criteria are consolidated into one implementation document.

**Not completed and not claimed:** full record-level inventory for every slice in Part I; exact-version dependency manifest for all those slices; promotion of any record to INCLUDE; qualified review of all high-consequence content; owner governance decisions; real-content reader/offline artifact; independent release approval; public release.

The next executable work is not another architecture discussion: complete the remaining exact record inventory chapter by chapter, reuse the audit records above, build the full version-pinned dependency register, and close only the blockers that can be closed with repository evidence. Keep all unresolved rows HOLD. Do not change `main`, merge this Draft PR, or start new M13 batches as part of this work.
