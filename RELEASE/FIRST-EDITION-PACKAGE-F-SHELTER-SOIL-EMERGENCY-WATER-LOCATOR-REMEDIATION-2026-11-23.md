# First Edition — Package F: Shelter, Soil and Emergency Water locator remediation

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Base inspection HEAD: `9711fa0ea8e0275c71f358e986f0713ee35658df`  
PR #22: OPEN / DRAFT / NOT MERGED  
Status: source-locator research and bounded remediation specification; NOT canonical implementation, safety approval, rights clearance or release selection.

## 1. Purpose and boundaries

This package continues the 32-record audit in `RELEASE/SHELTER-SOIL-EMERGENCY-WATER-32-RECORD-AUDIT-2026-11-23.md`. It converts the identified evidence gaps into exact source locator proposals and explicit editorial boundaries.

The package does not:
- edit canonical Claims, Evidence Use, Sources, Contexts, Scopes or Relations;
- version or create canonical records;
- assign INCLUDE, EXCLUDE or remove HOLD;
- create or modify a production selection manifest or allowlist;
- authorize public distribution, specialist sign-off, legal rights or owner decisions.

The 32-record audit remains the record-level baseline. At current PR HEAD 9711fa0, the 10 records in `water` and 9 records in `soil-basics` were re-fetched. Their exact IDs, versions and blob SHAs are recorded below. Shelter's 13-record set and findings are retained from the prior bounded audit at inspection HEAD `7c68ccb0d4d399d266aa92d80bbf910c8255c048`; no claim is made that all 13 shelter blobs were re-fetched again at 9711fa0.

## 2. Emergency Water — locator closure is now sufficiently specific to draft versioned EU updates

### 2.1 Current canonical records re-fetched at HEAD 9711fa0

| Record | Version | Blob SHA |
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

### 2.2 Exact source locators verified

**CDC — How to Make Water Safe in an Emergency**  
https://www.cdc.gov/water-emergency/about/

- Page heading: “Water with fuel or toxic chemicals in it” — explicitly says water containing fuel, toxic chemicals or radioactive materials cannot be made safe by boiling or disinfecting.
- Page heading: “Steps for boiling water” — clear water to a rolling boil for 1 minute; above 6,500 feet, 3 minutes; cool and store in clean, sanitized containers with tight covers.
- The same section says cloudy water should first be filtered through a clean cloth/paper/coffee filter or allowed to settle, then clear water drawn off before boiling.
- Page date shown: September 19, 2024.

**EPA — Emergency Disinfection of Drinking Water**  
https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

- Opening warning immediately below the introductory paragraph: boiling/disinfection does not destroy heavy metals, salts and most other chemicals.
- Opening boiling instruction: boiling kills pathogenic bacteria, viruses and protozoa; cloudy water should settle and be filtered.
- EPA page gives a different high-altitude threshold: above 5,000 feet (1,000 meters), boil for 3 minutes. This must NOT be merged into the CDC-specific 6,500-foot recommendation.

### 2.3 Record-level locator mapping proposed for the next authorized version

| Existing EU | Proposed locator in the existing source graph | Boundary to preserve |
|---|---|---|
| EU-WATER-BOILING-EFFECTIVE@1 | CDC, “Boil” and “Steps for boiling water”; EPA, opening boiling instruction | Boiling is a microbial inactivation/disinfection measure; do not imply it removes all hazards |
| EU-WATER-BOILING-TIME@1 | CDC, “Steps for boiling water”, step 1 | Keep CDC's 1 minute / above 6,500 feet 3 minutes. Do not substitute EPA's 5,000-foot threshold |
| EU-WATER-CHEMICAL-LIMIT@1 | CDC, “Water with fuel or toxic chemicals in it”; EPA opening warning | Keep chemical and radioactive contamination warning adjacent to any boiling guidance |
| EU-WATER-INDEPENDENT-CORROBORATION@1 | EPA opening paragraph and boiling instruction | Corroborates microbial treatment and chemical-contaminant limitation only; do not import EPA's altitude value into CDC-specific Claim |

This mapping is a drafting specification only. The existing EU records remain v1 until separately authorized versioned changes are made.

### 2.4 Safety/editorial constraints

1. The chemical/radioactive warning must be displayed in the same reader view as the boiling recommendation, not buried in a distant source note.
2. The CDC altitude threshold is the controlling value for the CDC-specific boiling-time Claim. EPA's distinct threshold is a separate authority-specific instruction.
3. This slice is not a complete water-treatment manual. It does not establish that any visibly clear water is chemically safe, nor does it authorize use of contaminated water.
4. Preserve the pre-treatment warning for cloudy water; do not imply boiling alone removes suspended material.
5. No bleach, iodine, chlorine-dioxide, dosing or filtration procedure should be added to these Claims by implication. Those procedures require their own exact records, product/concentration boundaries and specialist review.
6. Local public-health and emergency-authority instructions take precedence where they differ.

**Disposition: all four Claims remain HOLD.** Evidence locator drafting can proceed, but no safety approval or publication decision is made.

## 3. Soil Basics — USDA NRCS provides exact locators, with a wording distinction to preserve

### 3.1 Current canonical records re-fetched at HEAD 9711fa0

| Record | Version | Blob SHA |
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

### 3.2 Exact source locators verified

**USDA NRCS — What is Soil?**  
https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil

- Opening paragraph: soil functions include sustaining plant/animal life, regulating water flow, filtering/buffering pollutants, cycling nutrients and providing physical stability.
- The Soil Taxonomy definition: soil is a natural body comprised of mineral/organic solids, liquid and gases; it may be characterized by horizons/layers distinguishable from initial material.
- The following paragraph describes soil horizons near the surface and their alteration through interactions of climate, relief and living organisms over time.

**USDA NRCS — Soil Organic Matter, Guides for Educators**  
https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil%20Organic%20Matter.pdf

- Page 1, opening section: soil organic matter includes fresh plant residue, small living soil organisms, decomposing organic matter and stable organic matter; it is a source of nutrients.
- Page 1, same section: organic matter increases availability of most nutrients, available water capacity and moisture retention, and water infiltration.
- Page 3, “Relationship of Soil Organic Matter to Soil Functions”: nutrient supply, available water capacity, soil aggregation and infiltration are separately explained.

**USDA NRCS — Soil Survey Manual 2017, Chapter 1**  
https://www.nrcs.usda.gov/sites/default/files/2022-09/SSM-ch1.pdf

- Chapter 1, “Modern Concept of Soil”, printed page 8: Soil Taxonomy definition and soil horizons/layers. This is a supporting locator for the distinction between a soil body and its distinguishable horizons, not evidence that every soil property always changes with depth.

### 3.3 Proposed EU locator and editorial mapping

| Existing EU | Proposed exact locator | Required interpretation |
|---|---|---|
| EU-SOIL_BASICS-A@1 | NRCS “What is Soil?”, Soil Taxonomy definition; NRCS Soil Organic Matter, p. 1 for living-organism component | Soil physical phases are solids, liquid and gases. Organisms are biological constituents of the soil system/organic matter, not a fourth physical phase |
| EU-SOIL_BASICS-B@1 | NRCS “What is Soil?”, opening functional summary; Soil Organic Matter, pp. 1 and 3 | Water movement, nutrient availability and plant-growth functions are supported, but depend on soil type, organic matter, structure and site conditions |
| EU-SOIL_BASICS-C@1 | NRCS “What is Soil?”, Soil Taxonomy definition and horizon discussion; Soil Survey Manual, Ch. 1, “Modern Concept of Soil”, p. 8 | Describe distinguishable horizons/profiles and site variation. Do not assert that every property always changes with depth |

A second independent soil-science source is still desirable for Claim B. The existing single Source record and the NRCS source family should not be treated as independent corroboration merely because the same agency publishes multiple pages.

### 3.4 Wording and rights constraints

- Do not describe living organisms as a separate physical phase alongside solids, liquid and gases.
- Claim C must not be read as a universal monotonic depth rule. Soil horizons may be distinguishable; which properties vary and how depends on profile and site.
- NRCS page definitions explicitly attribute material to Soil Science Society of America and Soil Taxonomy. Record that attribution and inspect page-specific third-party notices before reuse.
- The Soil Organic Matter educator PDF includes a third-party figure credit (“Soil Food Web”); do not reproduce its figure or map in the edition. Use independently written factual paraphrase and a source link only, subject to the adopted source-reuse policy.
- This is a locator proposal, not blanket rights clearance for USDA/NRCS pages or embedded assets.

**Disposition: all three Claims remain HOLD.**

## 4. Shelter Basics — hazard-specific evidence confirms why broad claims must remain blocked

The earlier 13-record audit identified that Claim B combines weather, water availability, ventilation and site safety into a general checklist, while Claim C states a broad hazard boundary. The current Ready.gov portal and Red Cross shelter-finder source do not adequately support those universal propositions.

### 4.1 Exact source passages found

**FEMA — Key Planning Factors and Considerations for Response to and Recovery from a Chemical Incident (June 2022; update note June 2023)**  
https://www.fema.gov/sites/default/files/documents/fema_chemical-incident-kpf-2022.pdf

- KPF 4, §4.1 “Evacuation/Sheltering”, printed pp. 147–149.
- Printed pp. 147–148 explain that evacuation versus shelter-in-place depends on chemical identity/amount, movement, affected locations, time available, building sealing, traffic and weather.
- The document explicitly says no simple technical decision method exists because the factors and their importance vary by release scenario.
- Printed p. 148 notes that shelter-in-place may be unsafe when buildings are leaky or the release persists, and evacuation may be preferable for lingering flammable vapours or buildings that cannot be sealed.
- This is chemical-incident planning guidance; it does not support a universal shelter checklist for all hazards.

**UK Government — What to do in a chemical emergency**  
https://www.gov.uk/government/publications/chemical-emergencies-information-for-the-public/what-to-do-in-a-chemical-emergency

- “Stay in (sheltering-in-place)” section: close external doors/windows and, where instructed/appropriate, turn off equipment bringing outside air into the building; safety-critical chemical filtration/treatment systems may remain on.
- “Evacuation” section: evacuation is used when sheltering is not possible or remaining indoors could create greater exposure; emergency responders assess the relative risks.
- The page is under the Open Government Licence v3.0 except where third-party copyright is identified; third-party assets remain separately restricted.

### 4.2 Editorial disposition and proposed next action

1. Claim A may be retained as a general explanatory proposition only after its exact Ready.gov/FEMA locator is pinned and the text is checked against its stated scope.
2. Claim B must be split into distinct, hazard-bounded propositions or narrowed to a statement that shelter suitability depends on the hazard and official protective-action instructions. A single generic checklist is not supported.
3. Claim C may be narrowed to “protective actions differ by hazard and incident conditions” with clearly named examples. The FEMA chemical-incident source alone cannot prove a universal statement covering every hazard class.
4. Red Cross shelter-finder evidence remains limited to finding/understanding managed shelter services; it does not establish physical safety of an arbitrary site.
5. No instruction to shelter, evacuate, seal a building, change ventilation or select a site may be presented as universal. Local emergency services' incident-specific directions take precedence.
6. A qualified emergency-management/safety reviewer must inspect the final reader presentation before any shelter material is eligible for selection.

**Disposition: all three Claims remain HOLD.** No canonical rewrite or versioned source migration is authorized by this report.

## 5. Cross-slice priority decision

| Priority | Slice | Next permitted work | Release status |
|---:|---|---|---|
| 1 | Emergency Water | Prepare four versioned EU locator updates for owner/editor authorization; preserve adjacent chemical/radioactive warning | HOLD |
| 2 | Soil Basics | Prepare three versioned EU locator updates; obtain a second independent source for Claim B; preserve phase/organism distinction | HOLD |
| 3 | Shelter Basics | Prepare a bounded Claim B/C editorial decision packet and hazard-specific source graph; do not rush to EU-only patching | HOLD |

This is a work-priority order, not an INCLUDE ranking. No record is selected for the first edition by this package.

## 6. Verification and change-control statement

- The 10 water records and 9 soil records were fetched from branch `mvp-public-contribution-design-2026-10-11` at HEAD `9711fa0ea8e0275c71f358e986f0713ee35658df`; the blob SHAs above are the returned current values.
- The 13 shelter records and their prior exact-version/blob inventory are documented in the bounded audit at inspection HEAD `7c68ccb0d4d399d266aa92d80bbf910c8255c048`; this package does not claim a second full shelter re-fetch.
- Public source pages/PDF passages were inspected directly for the locators cited above.
- No canonical record, Claim wording, EU, Source, Context, Scope, Relation, Assessment, Inference, Decision, candidate register, denominator, coverage manifest, production allowlist or release state was changed.
- No legal permission, source licence, specialist safety approval, editor approval or release approval is inferred.
- PR #22 remains OPEN / DRAFT / NOT MERGED. No merge, deployment, public distribution or main-branch update was performed.

## 7. Next package

The next bounded package should be the **versioned EU implementation authorization packet** for Emergency Water and Soil Basics, plus a separate editorial decision packet for Shelter Basics. The packet must list exact before/after versions, schema-valid proposed JSON, source locators, attribution notes, and tests. Canonical writes must wait for the corresponding bounded owner authorization. After authorization, run exact-head reference, release-conformance and offline checks; do not report PASS until the exact new HEAD has completed them.
