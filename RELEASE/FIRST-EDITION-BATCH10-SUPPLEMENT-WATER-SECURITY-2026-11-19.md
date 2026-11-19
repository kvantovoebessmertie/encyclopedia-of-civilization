# First Edition — Batch 10 Supplement: Water Security Source and Dependency Review

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Status: **3 CLAIMS / 4 EUS RE-REVIEWED AS AN ADDITIONAL CANDIDATE SLICE; DIRECT UN-WATER LOCATORS FOUND; EPA SUPPORT BOUNDARY CONFIRMED; HOLD; NO CANONICAL JSON CHANGED**

## 1. Relationship to Batch 10

The existing Batch 10 dossier is `FIRST-EDITION-BATCH10-EVIDENCE-LOCATOR-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`. It already covers Agricultural Engineering, Agrifood Systems, Ecophysiology, Food Distribution, Infrastructure Resilience and Magnetism (20 Claims / 24 EUs). This supplement does **not** renumber or replace that batch and does not add those five overlapping slices to its denominator.

This supplement adds a separate review of `water-security-basics`, which is present in the exact-version master as a candidate slice but was not listed in the existing Batch 10 dossier.

## 2. Exact canonical scope

- Claims: `CLM-WATER_SECURITY-A@1`, `CLM-WATER_SECURITY-B@1`, `CLM-WATER_SECURITY-C@1`
- EUs: `EU-WATER_SECURITY-A@1`, `EU-WATER_SECURITY-B@1`, `EU-WATER_SECURITY-C@1`, `EU-EPA-WATER-SECURITY-B@1`
- Sources: `SRC-WATER_SECURITY@1` (UN-Water) and `SRC-EPA-WATER-SECURITY@1` (EPA)
- Context/Scope: `CTX-WATER_SECURITY@1`, `SCP-WATER_SECURITY@1`

All exact IDs, versions and types are present in the current exact-version master; no missing dependency node was discovered. All records remain HOLD.

## 3. Claim-level source fit

| Claim / EU | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| A / UN-Water | UN-Water working definition includes sustainable access to adequate quantities of acceptable-quality water | UN-Water Analytical Brief, §1 “A Working Definition of Water Security” | Direct |
| B / UN-Water | Water security includes protection from pollution and water-related disasters and preservation of ecosystems | UN-Water Analytical Brief, §1 definition | Direct |
| B / EPA independent EU | Water security includes protection against contamination and disruption caused by natural or human-made disasters | EPA “Water Security”, opening paragraphs on contamination threats and natural/human-made disasters affecting water and wastewater utilities | Direct for drinking-water contamination/infrastructure disruption; does not independently support ecosystem preservation |
| C / UN-Water | Assessment depends on water-cycle conditions, population, infrastructure, environment and social context | UN-Water Analytical Brief, §1 and §3D “Climate Change and Water Security”; §3D describes geographic location, water availability/use, demographic change, management/allocation systems, legal frameworks, governance, ecosystem resilience and hydrological variability | Direct for the listed dimensions; the current list is not exhaustive |

Sources:
- UN-Water, *Water Security and the Global Water Agenda*: https://www.unwater.org/publications/water-security-and-global-water-agenda
- UN-Water Analytical Brief PDF: https://www.unwater.org/sites/default/files/app/uploads/2017/05/analytical_brief_oct2013_web.pdf
- EPA, “Water Security”: https://www.epa.gov/emergency-response-research/water-security
- EPA, “Basic Information about Source Water Protection”: https://www.epa.gov/sourcewaterprotection/basic-information-about-source-water-protection

## 4. Support boundaries

- The UN-Water definition is explicitly a **working definition** developed as a starting point for dialogue in the UN system. Do not represent it as a universally binding legal definition.
- UN-Water §1 supports adequate quantities, acceptable quality, livelihoods, well-being, socio-economic development, protection from water-borne pollution and water-related disasters, and ecosystem preservation.
- EPA's “Water Security” page is focused on drinking-water and wastewater utilities, contamination threats and service disruptions. It is not a second independent source for the full UN-Water ecosystem and socio-economic definition.
- UN-Water §3D shows that climate-related effects on water security vary geographically and depend on water availability/use, population, infrastructure, governance and ecosystem resilience. Do not treat the factors listed in Claim C as exhaustive or assign a universal weighting to them.
- EPA's “Basic Information about Source Water Protection” is an additional direct source for surface/groundwater source protection, contamination prevention, water quality and availability; it is not currently represented by a canonical EU and no new ID is proposed here.

## 5. Recommended bounded remediation

1. Version `EU-WATER_SECURITY-A` with locator §1, “A Working Definition of Water Security”, including the opening definition.
2. Version `EU-WATER_SECURITY-B` with locator §1, preserving the full UN-Water definition and its ecosystem clause.
3. Version `EU-EPA-WATER-SECURITY-B` with the EPA “Water Security” opening paragraphs; state explicitly that the EU supports contamination/disaster/infrastructure disruption, not the ecosystem-preservation clause.
4. Version `EU-WATER_SECURITY-C` with §1 and §3D; identify the relevant list of geographic, demographic, hydrological, infrastructure, governance and ecosystem dimensions.
5. Do not change Claims A–C unless an editor decides to narrow Claim C or adjust the wording to make the working-definition boundary explicit.
6. Keep the two Sources separate; do not collapse EPA drinking-water security into the broader UN-Water water-security framework.

This is a remediation proposal only. No bounded authorization for these canonical changes was found in the inspected authorization register; no canonical update is performed here.

## 6. Rights and release gates

- Attribute the UN-Water Analytical Brief by exact title, date (2013) and section.
- EPA public pages are useful references but public access does not grant permission to reproduce third-party images, graphics or contributed content.
- Water security is a high-consequence domain. These claims are conceptual; they are not water-quality limits, treatment instructions, emergency response procedures or infrastructure design criteria.
- All records remain HOLD pending owner approval, rights review, independent editorial review and Human View.

## 7. Explicit non-actions

No canonical JSON, version, publication state, completion state, allowlist, relation, candidate disposition or release decision changed. No new Source/EU ID was created. PR #22 remains Draft and unmerged; `main` was not modified.
