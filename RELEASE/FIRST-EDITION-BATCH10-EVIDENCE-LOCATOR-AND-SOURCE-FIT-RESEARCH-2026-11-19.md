# First Edition — Batch 10 Evidence Locator and Source-Fit Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `[current branch HEAD at report creation]`  
Status: **20 CANDIDATE CLAIMS / 24 EUS RESEARCHED ACROSS SIX SLICES; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Batch 10 selects only candidate Claims present in the exact-version master and not covered by Batches 1–9 or active bounded authorizations. The six candidate slices are:

- agrifood-systems-basics — Claims A–C, 3 EUs plus one independent World Bank EU;
- ecophysiology-basics — Claims A–C, 3 EUs;
- food-distribution-basics — Claims A–D, 4 EUs;
- infrastructure-resilience-basics — Claims A–D, 7 EUs;
- magnetism-basics — Claims A–C, 3 EUs.
- agricultural-engineering-basics — Claims A–C, 3 EUs.

**Batch 10 total: 20 candidate Claims, 24 Evidence Use records, 9 Source records.** All 20 Claims, 24 EUs and nine Sources were confirmed present in the exact-version master. The existing master count and candidate denominator do not change.

The Agricultural Engineering slice is part of the current candidate master. Its exact records are present and are included in this Batch 10 review; the issue is source fit, not candidate eligibility. The previous out-of-pool classification was an extraction error and is corrected here.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All six candidate slices remain HOLD.

## 2. Batch 10 summary

| Slice | Claims | EUs | Main result |
|---|---:|---:|---|
| agrifood-systems-basics | 3 | 4 | FAO direct locators for A/B; FAO + World Bank direct system-level support for C; correct World Bank URI to About Us page |
| ecophysiology-basics | 3 | 3 | Current OpenStax URI is mismatched; replace with Biology 2e §33.3 and §1.1 locators |
| food-distribution-basics | 4 | 4 | FAO Chapter 1 and WFP Supply Chain provide direct locators; current WFP Source URI is wrong |
| infrastructure-resilience-basics | 4 | 7 | NIST SP 1190 Volumes I/II directly support A–D; FEMA page was inaccessible during this review and is not counted as verified |
| magnetism-basics | 3 | 3 | OpenStax Physics §20.1 directly supports A–C; Claim C should be narrowed to a defined force relationship |
| agricultural-engineering-basics | 3 | 3 | Current FAO land/water source is too narrow; ASABE + FAO mechanization and land/water sources provide direct routes |
| **Total** | **20** | **24** | **All direct locator candidates found; source/wording corrections and rights gates remain** |

All Evidence Use records currently have generic descriptions rather than claim-specific `material.locator` values. The direct locators below are research candidates only.

## 3. Agrifood Systems Basics — Claims A–C

Current records:
- `CLM-AGRIFOOD_SYSTEMS_BASICS-A/B/C@1`
- `EU-AGRIFOOD_SYSTEMS_BASICS-A/B/C@1`
- `EU-AGRIFOOD-WORLDBANK-CORROBORATION@1`
- `SRC-AGRIFOOD_SYSTEMS_BASICS@1`
- `SRC-WORLDBANK-FOODSYSTEMS-2030@1`

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A / FAO EU A | Agrifood systems include people, activities, investments and decisions connected with producing and delivering food and agricultural products | FAO Agrifood Systems page, opening definition and “What are agrifood systems?” |
| B / FAO EU B | The chain can include growing, harvesting, processing, packaging, transport, distribution, trade, preparation, consumption and disposal | FAO Agrifood Systems page, “What are agrifood systems?” and the description of activities from production to consumption/disposal |
| C / FAO EU C | Analysis requires considering production, economic, social and environmental links together | FAO Agrifood Systems page, outcomes/definition; World Bank FoodSystems 2030 “About Us” → “Our Approach: Systems Transformation” and “Theory of Change” |
| C / World Bank independent EU | Independent institutional corroboration of the systems approach | World Bank page explicitly describes interconnected human health, planetary health and economic prosperity, and three interlinked outcomes: healthy people, healthy planet, healthy economies |

Sources:
- FAO, “Agrifood Systems”: https://www.fao.org/food-systems/en
- World Bank, FoodSystems 2030 “About Us”: https://www.worldbank.org/en/programs/food-systems-2030/about-us

**Important Source correction:** the existing World Bank Source URI points to the FoodSystems 2030 programme home page, which is not the strongest direct locator for the independent corroboration description. Version the Source URI to the “About Us” page and pin the exact “Our Approach: Systems Transformation” / “Theory of Change” passages. The independent EU is a real separate dependency and should remain distinct from the FAO EU.

Support boundary: the World Bank page describes the programme's conceptual approach and its three outcomes; it does not prove that every national agrifood system has the same structure or outcomes. Keep the Claim descriptive and avoid policy-causality inference.

## 4. Ecophysiology Basics — Claims A–C

Current records:
- `CLM-ECOPHYSIOLOGY_BASICS-A/B/C@1`
- `EU-ECOPHYSIOLOGY_BASICS-A/B/C@1`
- `SRC-ECOPHYSIOLOGY_BASICS@1`

The current Source identity is a generic definition of ecological physiology, but its URI points to OpenStax *Biology 2e* §44, “Animal Sensory Systems and Movement”. That is a material Source mismatch for the three Claims.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Physiological processes of an organism depend on external conditions | OpenStax *Biology 2e* §33.3 “Homeostasis”: external temperature and other changes act as stimuli; physiological systems adjust |
| B | Organisms have ranges of conditions in which their physiological functions are maintained | §33.3 “Homeostasis”: body functions are maintained within specific ranges around a set point; external changes trigger regulatory responses |
| C | Comparing physiological responses requires comparable measurement conditions | OpenStax *Biology 2e* §1.1 “The Science of Biology”: controlled experiments, variables and controls; proposed Claim narrowing below |

Sources:
- §33.3: https://openstax.org/books/biology-2e/pages/33-3-homeostasis
- §1.1: https://openstax.org/books/biology-2e/pages/1-1-the-science-of-biology
- Book: https://openstax.org/books/biology-2e

Recommended Claim C narrowing, if approved:

> При контролируемом экспериментальном сравнении изменяют исследуемый фактор, сохраняя остальные существенные условия сопоставимыми.

This describes the experimental-control principle directly; it is more precise than a broad assertion about all physiological comparisons. Correct the Source identity to OpenStax *Biology 2e* and the URI to the book-level or §33.3 page; use section-specific EU locators. Claims A/B can remain unchanged if the source/version references are aligned. Claim C requires an explicit wording decision.

**Rights:** OpenStax *Biology 2e* identifies CC BY-NC-SA 4.0 and includes a restriction on LLM ingestion/generative-AI offerings without prior written permission. Attribution and ShareAlike apply to permitted non-commercial reuse; commercial use is not granted. This remains a project-level rights blocker.

## 5. Food Distribution Basics — Claims A–D

Current records:
- `CLM-FOOD_DISTRIBUTION_BASICS-A/B/C/D@1`
- `EU-FOOD_DISTRIBUTION_BASICS-A/B/C/D@1`
- `SRC-FOOD_DISTRIBUTION_BASICS@1`
- `SRC-FOOD_DISTRIBUTION_WFP@1`

The existing FAO Source is the broad “Food Systems” page. A more direct source for the distribution Claims is FAO, *Food Supply and Distribution Systems to Cities*, Chapter 1. The existing WFP Source identity is accurate, but its URI points to a 2024 procurement infographic rather than the direct WFP Supply Chain page.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A / FAO EU A | Food distribution connects production and other food-system stages with consumers | FAO *Food Supply and Distribution Systems to Cities*, Chapter 1, §1.1 “What are food supply and distribution systems to cities?” |
| B / FAO EU B | Transport, storage, infrastructure, markets, rules and food losses affect distribution | FAO Chapter 1, §1.1 (economic agents, infrastructure, services and laws); §1.2.1.1 and §1.2.1.2 (supply/distribution subsystems); §1.2.2 (external/internal factors); §§1.2.2.1–1.2.2.2 |
| C / FAO EU C | Local food availability is not determined only by production volume | FAO Chapter 1, §1.1 and §1.2; World Bank “What is Food Security?” — physical availability versus economic/physical access, incomes, expenditure, markets and prices |
| D / WFP EU D | A humanitarian food chain can include procurement, storage, transport and final delivery | WFP “Supply chain” → “How does WFP’s supply chain deliver food?”, “Procurement”, “Transport and storage” and “Delivery” |

Sources:
- FAO, *Food Supply and Distribution Systems to Cities*, Chapter 1: https://www.fao.org/4/X6996E/x6996e08.htm
- World Bank, “What is Food Security?”: https://www.worldbank.org/en/brief/2023/06/11/what-is-food-security
- WFP, “Supply chain”: https://www.wfp.org/supply-chain

The FAO chapter directly describes the system as a combination of production, handling, storage, transport, processing, packaging, wholesale and retail activities; it also identifies economic agents, infrastructure, facilities, services, laws and regulations. It explicitly separates food supply to cities from urban food distribution. The World Bank source directly distinguishes food availability from household access and affordability, so Claim C is not inferred solely from the FAO definition.

**Source corrections**
1. Correct `SRC-FOOD_DISTRIBUTION_BASICS` identity/URI to the exact FAO publication/chapter, or add a distinct Source for this chapter under canonical ID allocation. Do not leave the generic FAO home page as if it were the exact chapter.
2. Version `SRC-FOOD_DISTRIBUTION_WFP` and correct its URI from the 2024 procurement infographic to https://www.wfp.org/supply-chain. The WFP page directly lists planning, procurement, transport/storage and delivery, including last-mile delivery.
3. If Claim C uses the World Bank access/availability distinction, add a separate Source/Evidence Use chain. Do not overload the FAO Source with a second publisher's locator.

Rights: the FAO chapter and World Bank page require source-specific attribution/reuse review; the FAO publication is not a blanket commercial reuse licence. WFP's public page is not a blanket permission to reproduce its images or materials.

## 6. Infrastructure Resilience Basics — Claims A–D

Current records:
- `CLM-INFRASTRUCTURE_RESILIENCE-A/B/C/D@1`
- Primary EUs `EU-INFRASTRUCTURE_RESILIENCE-A/B/C@1`
- Additional EUs `EU-INFRASTRUCTURE_RESILIENCE-A-2/B-2/C-2@1`
- `EU-INFRASTRUCTURE_RESILIENCE-D@1`
- Sources `SRC-INFRASTRUCTURE_RESILIENCE@1` (NIST Community Resilience Program) and `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A / NIST primary EU | Community resilience includes preparing for hazards, adapting, withstanding disruptions and recovering within defined timeframes | NIST SP 1190 Volume I, opening definition of community resilience (printed p. 1); §4.1 “Goals for Community Resilience”, p. 37, on performance goals and time to recovery |
| B / NIST primary EU | Infrastructure systems affect social/economic community functions; interdependencies can create cascading consequences | NIST SP 1190 Volume II, Chapter 11 “Dependencies and Cascading Effects”, opening discussion and dependency examples, pp. 38–39 |
| C / NIST primary EU | Resilience planning uses functional performance and recovery goals, not only asset-level properties | NIST SP 1190 Volume I, §4.1 “Goals for Community Resilience”, p. 37; §4.1.2, p. 38, on performance goals and recovery of community functions |
| D / FEMA EU | Infrastructure assessment must consider cross-sector dependencies and how failure/recovery of one service changes other community functions | NIST SP 1190 Volume II, Chapter 11 “Dependencies and Cascading Effects”; §11.2.4 “Source Dependency”, pp. 47–48 |

Sources:
- NIST SP 1190 Volume I: https://www.nist.gov/system/files/community-resilience-planning-guide-volume-1_0.pdf
- NIST SP 1190 Volume II: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1190v2.pdf
- Existing FEMA Source URI: https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency

**Critical source-access result:** the FEMA page could not be retrieved during this review (HTTP 403). Therefore the three additional FEMA EUs A-2/B-2/C-2 and the FEMA-only EU D cannot be treated as independently verified or assigned precise FEMA locators on this pass. Do not count the current generic descriptions as direct support.

NIST SP 1190 Volumes I/II provide direct alternative evidence:
- Volume I defines community resilience and gives planning steps/performance goals expressed as time to recovery of functions.
- Volume II addresses dependencies among infrastructure systems and cascading consequences, including source dependencies and restoration sequences.

Recommended source graph:
1. Correct the existing NIST Source identity/URI to the exact *Community Resilience Planning Guide for Buildings and Infrastructure Systems*, Volume I.
2. Add a separate Source for Volume II under the canonical ID allocation process, and use it for Claims B/D.
3. Keep the FEMA Source/EUs HOLD until the exact page can be reviewed and claim-specific locators verified, or replace them only under explicit source-graph authorization.
4. Do not infer that NIST Volume II and FEMA are the same source or silently rewrite the existing FEMA EU edges.

Rights: NIST SP 1190 is a U.S. Government work, but the guide warns that some figures/images may contain third-party material. No figure or image reuse is proposed. Complete item-level rights checks for any future reproduction.

## 7. Magnetism Basics — Claims A–C

Current records:
- `CLM-MAGNETISM_BASICS-A/B/C@1`
- `EU-MAGNETISM_BASICS-A/B/C@1`
- `SRC-MAGNETISM_BASICS@1`

The Source identity is currently the generic string “Authoritative reference source for magnetism-basics”; the URI already points to OpenStax Physics §20.1. Correct the Source identity to the exact OpenStax book and section.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | A magnetic field describes magnetic influence in space | §20.1 “Magnetic Fields, Field Lines, and Force”, magnetic-field definition and field-line discussion |
| B | Permanent magnets and current-carrying conductors can create magnetic fields | §20.1, “Magnets and Magnetization”; current-carrying wire and solenoid examples |
| C | Magnetic force depends on the magnetic field and properties of interacting objects | §20.1, “Magnetic Force”; equations (F=qvBsin	heta) for a moving charge and (F=Iell Bsin	heta) for a current-carrying wire |

Official source: https://openstax.org/books/physics/pages/20-1-magnetic-fields-field-lines-and-force

Claim C is too broad as currently worded. Recommended narrowing, if approved:

> Модуль магнитной силы, действующей на движущийся заряд, равен (F=qvBsin	heta), где (	heta) — угол между скоростью заряда и магнитным полем.

Alternatively, make it explicitly about a straight current-carrying wire and use (F=Iell Bsin	heta). Do not combine the two equations into one universal claim. The section directly supports the permanent-magnet/current-carrying-wire field examples and the force relationships.

Rights: verify the exact current OpenStax Physics edition's licence and preface. Public access does not itself establish commercial or AI-ingestion permission.

## 8. Agricultural Engineering Basics — Claims A–C

Current branch records:
- `CLM_AGRICULTURAL_ENGINEERING_BASICS_A/B/C@1`
- `EU_AGRICULTURAL_ENGINEERING_BASICS_A/B/C@1`
- `SRC_AGRICULTURAL_ENGINEERING_BASICS@1`

**All seven current records are present in the 1,129-row exact-version master.** The slice is part of Batch 10 and remains in the first-edition candidate denominator. The source/locator review below addresses source fit only; it does not change its candidate status.

Current Claims:
- A: Agricultural engineering applies engineering principles to agricultural production and resource management.
- B: It includes systems for machinery, irrigation, drainage, storage, processing and other farm operations.
- C: Choices depend on crops, soils, water, climate, energy, labor and operating conditions.

Current Source: FAO “Land and water management” — https://www.fao.org/land-water/land/soil-water-management/en/

**Source-fit assessment:** this FAO land/water page may support water/soil management aspects, but it is not an adequate general source for the discipline definition, agricultural machinery, storage and processing. Do not treat the current generic EUs as direct support.

Better source candidates:
- ASABE, “About the Profession”, exact professional definition of Agricultural and Biological Engineering; it explicitly covers engineering principles, biological systems/tools, production, processing and management of agricultural, food and natural-resource systems:
  https://asabe.org/about-us/about-the-profession
- FAO, “What is sustainable mechanization”, direct coverage of machinery/tools, land preparation, seeding, planting, weed control, harvesting, preparation for storage, on-farm processing, transport and marketing:
  https://www.fao.org/sustainable-agricultural-mechanization/overview/what-is-sustainable-mechanization/en/
- FAO, *Agricultural Mechanization in Sub-Saharan Africa: Guidelines for Preparing a Strategy*, Chapter 1, §1.1 “Background”, for the need to adapt technologies to local agronomic, socio-economic, environmental and industrial conditions:
  https://www.fao.org/fileadmin/user_upload/ags/publications/K7325e.pdf

Proposed bounded direction:
- Claim A → ASABE definition.
- Claim B → ASABE scope plus FAO sustainable mechanization; retain FAO Land and Water Management only for the irrigation/drainage subset, and add exact post-harvest/storage/processing support if those items remain in the statement.
- Claim C → FAO mechanization and the strategy guide; consider narrowing the list of conditions to the source's actual wording (technological, economic, social, environmental, cultural and local agronomic conditions).

ASABE is a professional association source and is not an open licence. Use paraphrase and attribution; no permission to reproduce text/figures is inferred. The existing FAO Source and all three EU records remain HOLD until their support boundaries are corrected or supplemented under a bounded source-graph authorization.

## 9. Current-master and scope reconciliation

- The 20 Batch 10 Claims, 24 EUs and nine Sources are present in the exact-version master. No new dependency rows were required.
- The master remains **1,129 exact-version rows = 1,058 candidate keys + 71 dependency records**.
- Part II slice coverage remains 124/385.
- Agricultural Engineering A–C, its three EUs and Source are present in the master and included in Batch 10.
- The previously identified 21 current Claims outside the master remain **21 known out-of-master Claims** across 11 slices. This is a known count from the reviewed slices, not an assertion that every out-of-master Claim across the entire repository has now been exhaustively enumerated.
- No candidate denominator, coverage count or HOLD decision changes.

## 10. Rights and release blockers

- FAO and World Bank sources require source-specific attribution/reuse review; no blanket commercial reproduction licence is asserted.
- OpenStax Biology 2e has CC BY-NC-SA 4.0 and an AI-ingestion restriction; OpenStax Physics edition-specific terms need review.
- ASABE material is copyright-controlled; paraphrase and attribution only absent permission.
- NIST SP 1190 contains government-work material but may include third-party figures/images; no such media reuse is proposed.
- FEMA content was not retrievable on this pass; no independent FEMA support is claimed.
- All six candidate slices remain HOLD pending exact locator implementation, source/rights review, independent editorial review and Human View.

## 11. Recommended execution order after authorization

1. Locator-only changes: Agrifood A/B; Food Distribution A/B/D; Magnetism A/B; Agricultural Engineering A/B/C after the source graph is bounded; Infrastructure A/C using NIST Volume I.
2. Correct Source identity/URI: Agrifood World Bank Source, Ecophysiology OpenStax Source, Food Distribution WFP Source, Infrastructure NIST Source, Magnetism OpenStax Source.
3. Source-graph expansion or replacement: Food Distribution C; Infrastructure B/D using NIST Volume II; Agrifood C independent World Bank; retain FEMA only after exact review.
4. Claim wording decisions: Ecophysiology C; Magnetism C. Keep statements unchanged unless owner/editor approves a versioned narrowing.
5. Re-fetch all authorized records at one frozen HEAD, apply only exact approved changes, update dependent references, run graph preflight and affected-slice tests, then full release gates on the final immutable HEAD.

## 12. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change any Claim statement or version;
- create new Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- change the existing candidate master denominator or record count;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve or amend the 20 candidate locator/source changes slice-by-slice; approve the Ecophysiology and Magnetism Claim narrowing separately; authorize any Agricultural Engineering Source/EU graph expansion separately from its current candidate status.
