# First Edition — Residual candidate follow-up: Agricultural Systems, Ecophysiology, Food Distribution, Infrastructure Resilience and Water Security

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `mvp-public-contribution-design-2026-10-11` (branch tree inspected during this pass; exact pre-report HEAD is recorded in the priority-board checkpoint)  
Status: **20 CLAIMS / 25 EVIDENCE-USE RECORDS ACROSS SIX SLICES REVIEWED; DIRECT LOCATOR CANDIDATES FOUND FOR MOST CLAIMS; TWO MATERIAL SOURCE-MISMATCH AREAS; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection

This is the next residual dependency/source-fit pass after Batches 1–9 and the Batch 4–6 residual dossier. Selection was restricted to six candidate slices whose exact-version master entries were still marked `canonical_json_dependency_verified_hold` and for which no prior substantive source-fit dossier or bounded authorization was found during the selection pass:

1. agricultural-engineering-basics — 3 Claims / 3 EUs;
2. agrifood-systems-basics — 3 Claims / 4 EUs (including independent World Bank corroboration);
3. ecophysiology-basics — 3 Claims / 3 EUs;
4. food-distribution-basics — 4 Claims / 4 EUs;
5. infrastructure-resilience-basics — 4 Claims / 7 EUs;
6. water-security-basics — 3 Claims / 4 EUs.

**Total: 20 Claims and 25 Evidence Use records.** All exact IDs, versions and record types were checked against canonical JSON in the current branch and cross-checked against the existing exact-version master. No new dependency node was discovered in these six slices; the master already contains the relevant Source, EU, Context and Scope rows. Candidate denominator remains 1,058; master total remains 1,129 exact-version rows (1,058 candidate keys + 71 dependency records); Part II coverage remains 124/385.

No canonical JSON, relation, context, scope, allowlist, publication state or candidate disposition was changed. All six slices remain HOLD.

## 2. Agricultural Engineering Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM_AGRICULTURAL_ENGINEERING_BASICS_A/B/C@1`
- EUs: `EU_AGRICULTURAL_ENGINEERING_BASICS_A/B/C@1`
- Source: `SRC_AGRICULTURAL_ENGINEERING_BASICS@1`

The current Source identity says “FAO — Land and water management” but its URI is the FAO soil-water-management landing page. This is not a close match for the subject “agricultural engineering” or the full set of claims. The EUs contain only generic “source supports the claim” descriptions and no section-level locators.

| Claim | Current proposition | Direct source and locator candidate | Fit |
|---|---|---|---|
| A | Agricultural engineering applies engineering principles to agricultural production and resource management | FAO Sustainable Agricultural Mechanization, “What is sustainable mechanization”: opening definition; scope includes farming and processing technologies, from hand tools to motorized equipment; covers productivity, resource use, market access and climate-related hazards | Strong for the mechanization component; narrower than all agricultural engineering |
| B | Agricultural engineering includes machinery, irrigation, drainage, storage, processing and other farm operations | FAO “What is sustainable mechanization”: land preparation, seeding/planting, weed control, pest management, fertilizer application, harvesting and preparation for storage; FAO “On-farm postharvest and value addition”: shelling, milling, packaging, transport, storage and marketing | Direct for machinery and post-harvest/processing; irrigation/drainage need their own FAO irrigation and water-management locators |
| C | Engineering choices depend on crops, soils, water, climate, energy, labour and operating conditions | FAO mechanization overview states sustainable mechanization considers technological, economic, social, environmental and cultural aspects and must be adapted to local context; FAO irrigation pages discuss water stress, crop production and local management | Partial. The exact seven-factor list is not supported as a single universal decision rule by the current Source |

Sources:
- FAO, “What is sustainable mechanization”: https://www.fao.org/sustainable-agricultural-mechanization/overview/what-is-sustainable-mechanization/en/
- FAO, “On farm postharvest and value addition”: https://www.fao.org/sustainable-agricultural-mechanization/guidelines-operations/on-farm-postharvest-and-value-addition/en/
- FAO, “Irrigation management”: https://www.fao.org/land-water/water/agricultural-water-management/irrigation/en/
- FAO, “Water harvesting and storage”: https://www.fao.org/land-water/water/agricultural-water-management/water-harvesting-and-storage

**Recommended bounded remediation:**
1. Correct the Source identity/URI to an exact FAO Sustainable Agricultural Mechanization publication/page, or split the current broad Claim set across mechanization and irrigation/water-management sources.
2. Pin EU A to the mechanization definition and stated technology range.
3. Pin EU B to the operation list and the post-harvest operations page; add distinct irrigation/drainage evidence only if those examples remain in the Claim.
4. Narrow Claim C to the supported proposition: “Выбор и применение сельскохозяйственной механизации должны учитывать местный технологический, экономический, социальный, экологический и культурный контекст.” If the owner retains the current exact factor list, provide a multi-source support chain for each material factor rather than relying on the broad mechanization page.

Rights: FAO pages are public references; do not infer permission to reproduce embedded third-party images, diagrams or full text. Attribute the exact publication/page and verify any intended reuse.

## 3. Agrifood Systems Basics — 3 Claims / 4 EUs

Canonical records:
- Claims: `CLM-AGRIFOOD_SYSTEMS_BASICS-A/B/C@1`
- Primary EUs: `EU-AGRIFOOD_SYSTEMS_BASICS-A/B/C@1`
- Independent EU: `EU-AGRIFOOD-WORLDBANK-CORROBORATION@1`
- Sources: `SRC-AGRIFOOD_SYSTEMS_BASICS@1`, `SRC-WORLDBANK-FOODSYSTEMS-2030@1`

The FAO source identity and URI are consistent at the broad agrifood-systems level. The three primary EUs nevertheless need claim-specific locators; the independent World Bank EU currently has only a generic description and no direct locator.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A / FAO | Agrifood systems include people, activities, investments and choices related to production and delivery of food and agricultural goods | FAO “Agrifood Systems” FAQ, “What are agrifood systems?”: definition includes all interconnected components, people, activities, investments and choices; FAO landing page opening paragraph | Direct |
| B / FAO | The chain may include growing, harvesting, processing, packaging, transport, distribution, trade, preparation, consumption and disposal | FAO FAQ, “What are agrifood systems?”; FAO 2021 *The State of Food and Agriculture*, Chapter 1, Box 1 defining agrifood systems | Direct |
| C / FAO | Systems analysis considers production, economic, social and environmental connections | FAO FAQ, “Why should we think of food and agriculture as a system?”: interconnected components, dynamic interactions, synergies/trade-offs and links to environmental, economic, health and social systems | Direct |
| C / World Bank independent EU | World Bank independently corroborates the systems approach | World Bank Food Systems 2030 programme overview: use only passages explicitly describing the programme’s systems approach, interlinked food-system dimensions, and economic/social/environmental/institutional factors; exact page locator must be recorded in the EU | Partial until pinpoint is inserted |

Sources:
- FAO, “Frequently asked questions on agrifood systems transformation”: https://www.fao.org/food-systems/faq/en
- FAO, “Agrifood Systems”: https://www.fao.org/food-systems/en
- FAO, *The State of Food and Agriculture 2021*, Chapter 1: https://www.fao.org/4/cb4476en/cb4476en.pdf
- World Bank, Food Systems 2030: https://www.worldbank.org/en/programs/food-systems-2030

The current FAO definition is broader than food alone: it includes non-food agricultural, forestry, fisheries and other products. Preserve that distinction where the Claim says “продовольствие и сельскохозяйственные товары.” FAO also explicitly says agrifood systems operate at multiple scales and that no single uniform system exists.

**Recommended remediation:** pin the three FAO EUs to the exact FAQ question/answer headings and the relevant FAO 2021 Box 1. Add a specific World Bank locator to the existing independent EU. Do not create a new World Bank EU or Source; both already exist. Until the independent locator is pinned, treat the World Bank chain as a source candidate, not completed independent corroboration.

Rights: FAO and World Bank publication terms vary by item. Public programme pages are not a blanket licence for reuse of images or third-party materials.

## 4. Ecophysiology Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM-ECOPHYSIOLOGY_BASICS-A/B/C@1`
- EUs: `EU-ECOPHYSIOLOGY_BASICS-A/B/C@1`
- Source: `SRC-ECOPHYSIOLOGY_BASICS@1`

**Material source mismatch:** the current Source identity is a generic definition of ecophysiology, while its URI points to OpenStax Biology 2e Chapter 44 “Animal Sensory Systems and Movement”. That chapter URL/title is not an adequate source identity for the three claims. The claims are plausible but broad; generic EU descriptions do not identify evidence.

| Claim | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A | Organism physiological processes depend on external conditions | OpenStax Biology 2e §44.1 “The Scope of Ecology” (organisms interact with their environment); §33.3 “Homeostasis” (external temperature and other changes trigger physiological adjustments); §30.6 for plant responses to light, gravity, temperature and touch | Direct after narrowing the domain to physiological responses to environmental stimuli/conditions |
| B | Organisms have ranges of conditions within which physiological functions are maintained | OpenStax §33.3: homeostasis maintains body functions within specific ranges and describes thermoregulation; §44.2 “Biogeography”: enzymes operate within temperature ranges and organisms must maintain or inhabit conditions that support metabolism | Partial/direct for temperature and homeostasis; the current broad claim across all environmental factors requires more than these examples |
| C | Comparison of physiological responses requires comparable measurement conditions | No direct source in the current OpenStax set establishes this as a general methodological rule. NIST measurement-science guidance can support the narrower methodological proposition that measurements must define the measurand, method and conditions to be compared meaningfully; a specific protocol/statistical source is needed for the full claim | Not yet directly supported by the current Source |

Sources:
- OpenStax §44.1: https://openstax.org/books/biology-2e/pages/44-1-the-scope-of-ecology
- OpenStax §33.3: https://openstax.org/books/biology-2e/pages/33-3-homeostasis
- OpenStax §44.2: https://openstax.org/books/biology-2e/pages/44-2-biogeography
- OpenStax §30.6: https://openstax.org/books/biology-2e/pages/30-6-plant-sensory-systems-and-responses

**Recommended remediation:**
1. Replace the generic Source identity with a real bibliographic source identity and the appropriate OpenStax section URL(s), or create separately allocated Sources for the relevant chapters.
2. Claim A can be narrowed to: “Физиологические процессы организмов реагируют на изменения внешних условий, включая температуру, свет и доступность ресурсов.”
3. Claim B should name the condition class and avoid implying a single fixed universal range: “Для отдельных физиологических функций существуют диапазоны условий, в которых функция сохраняется; границы зависят от вида, функции и длительности воздействия.”
4. Claim C requires a distinct measurement-method source and careful formulation. A suitable narrower form is: “Для корректного сравнения физиологических показателей необходимо документировать и сопоставлять условия измерения и методику.” This remains a proposal, not an approved Claim revision.

Rights: OpenStax *Biology 2e* is CC BY-NC-SA 4.0; its current page/preface also states restrictions concerning LLM ingestion/generative-AI offerings without prior written permission. This is a project-level rights blocker requiring owner/legal review, not a cleared source.

## 5. Food Distribution Basics — 4 Claims / 4 EUs

Canonical records:
- Claims: `CLM-FOOD_DISTRIBUTION_BASICS-A/B/C/D@1`
- EUs: `EU-FOOD_DISTRIBUTION_BASICS-A/B/C/D@1`
- Sources: `SRC-FOOD_DISTRIBUTION_BASICS@1`, `SRC-FOOD_DISTRIBUTION_WFP@1`

The FAO Source currently points to the broad FAO Food Systems portal. It is contextually relevant but not the strongest direct source for the claims about urban distribution, transport, storage, market access and losses. The WFP Source title says “Supply Chain” but its URI points to a 2024 procurement infographic page; that is a source identity/URI mismatch for a claim about the complete chain of procurement, storage, transport and last-mile delivery.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A / FAO | Distribution links production and other food-system stages with consumers | FAO, *Food Supply and Distribution Systems to Cities*, Chapter 1 §1.1 “What are food supply and distribution systems to cities?”; §1.2.1 separates supply-to-city and urban-distribution subsystems | Direct for urban food distribution systems; preserve the urban scope |
| B / FAO | Distribution is affected by transport, storage, infrastructure, markets, rules and food losses | Same FAO chapter: §1.1 (activities and actors); §1.2.1.1 (storage, handling, packaging, transport); discussion of wholesale markets, cold storage, transport, regulation and post-harvest losses | Direct for the listed system factors, with locator split by topic |
| C / FAO | Local food availability is not determined only by production volume | Same FAO chapter: §1.2 and the passage distinguishing food availability from accessibility; consumer purchasing power, food access costs and social relations affect access | Direct, but the Claim should retain the access/availability distinction |
| D / WFP | A humanitarian food chain may include procurement, storage, transport and delivery to final locations | WFP “Supply chain”: opening description and “How does WFP’s supply chain deliver food?”; transport/storage and delivery sections | Direct. Existing WFP Source URI should point to this page, not procurement infographics |

Sources:
- FAO, *Food Supply and Distribution Systems to Cities*, Chapter 1: https://www.fao.org/4/X6996E/x6996e08.htm
- FAO, *Urban Food Supply and Distribution — Policies, Strategies and Programmes*: https://www.fao.org/4/x8296e/x8296e07.htm
- FAO Evidence Platform, storage/processing/packaging and logistics: https://www.fao.org/evidence-platform-agri-food-systems-nutrition/recommendations/detail/3.2.4.a/en
- WFP, “Supply chain”: https://www.wfp.org/supply-chain

**Recommended remediation:**
1. Keep FAO Food Systems as contextual background if useful, but pin A–C to the specific FAO urban food supply/distribution chapter.
2. Make the urban/geographical scope explicit in EU descriptions; the FAO manual does not establish every claim for every rural, national or global system.
3. Correct `SRC-FOOD_DISTRIBUTION_WFP@1` identity/URI to the exact WFP Supply Chain page, then pin EU D to procurement, transport/storage and final delivery.
4. Do not overstate the FAO manual's historical statistics as current global rates; only use its conceptual descriptions unless the figures are independently refreshed.

Rights: FAO and WFP pages are public institutional sources, but this does not grant permission to reproduce photographs, maps, tables or contributed material. WFP operational descriptions may change over time; retain an access date.

## 6. Infrastructure Resilience Basics — 4 Claims / 7 EUs

Canonical records:
- Claims: `CLM-INFRASTRUCTURE_RESILIENCE-A/B/C/D@1`
- Primary EUs: `EU-INFRASTRUCTURE_RESILIENCE-A/B/C@1`
- Additional EUs: `EU-INFRASTRUCTURE_RESILIENCE-A-2/B-2/C-2@1`, `EU-INFRASTRUCTURE_RESILIENCE-D@1`
- Sources: `SRC-INFRASTRUCTURE_RESILIENCE@1` (NIST Community Resilience Program), `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1` (FEMA Infrastructure Dependency Primer)

The current primary NIST Source is appropriate at the programme level but each EU needs a specific NIST guide/section locator. The FEMA Source is appropriate for dependency concepts but must be pinned to the actual primer content and scope. The seven EU records are not redundant by count alone: A–C have primary NIST and additional FEMA evidence; D has FEMA evidence.

| Claim / EUs | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A / NIST + FEMA | Community resilience includes preparing for hazards, adapting, withstanding disruption and recovering within specified times | NIST Community Resilience Planning Guide Vol. I, Introduction and six-step planning approach; NIST programme description “prepare for, resist, respond to, and recover from disruptive hazard events”; Playbook Action 3-2 for specified recovery times | Strong for preparedness, performance and recovery. “Adapt” and “withstand” should be pinned to the precise framework definition or claim narrowed to NIST's documented framing |
| B / NIST + FEMA | Infrastructure performance affects community social/economic functions; dependencies can cause cascading consequences | NIST SP 1190 Vol. II Chapter 11 “Dependencies and Cascading Effects”, especially “Dependencies Executive Summary” and §11.1; examples of electricity/telecom, transport/fuel and cascading failures | Direct |
| C / NIST + FEMA | Resilience planning uses functional performance and recovery goals, not only properties of individual assets | NIST SP 1190 Vol. I, Introduction and Step 3 / Action 3-2; Playbook Action 3-2 defines performance goals as recovery times for functions/services, grounded in community needs and infrastructure dependencies | Direct |
| D / FEMA | Infrastructure resilience assessment must account for cross-sector dependencies and how service failure/recovery changes other functions | FEMA Infrastructure Dependency Primer; NIST SP 1190 Vol. II Chapter 11 is a strong independently inspectable direct locator | Direct in principle; FEMA page/primer should be opened and exact section/locator pinned before relying on the existing EU |

Sources:
- NIST Community Resilience Planning Guide: https://www.nist.gov/community-resilience/planning-guide
- NIST SP 1190 Vol. I: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1190v1.pdf
- NIST SP 1190 Vol. II: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1190v2.pdf
- NIST Playbook: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1190GB-16.pdf
- FEMA Infrastructure Dependency Primer: https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency

**Important scope note:** NIST SP 1190 is a community planning methodology focused on buildings, infrastructure systems and the social/economic functions they support. It is not a universal quantitative law of resilience and does not prove that every system has the same recovery priorities. Recovery goals are community- and hazard-specific. Do not convert illustrative example recovery times in the Playbook into universal standards.

**Recommended remediation:** pin primary EUs A–C to exact NIST chapters/actions. Pin additional EUs A-2/B-2/C-2 and EU D to FEMA's actual dependency primer sections; if the FEMA primer is inaccessible or not sufficiently specific, retain NIST Vol. II as the directly inspectable support and do not claim independent FEMA corroboration until the source is verified. Do not collapse the two sources into a single generic “resilience” locator.

Rights: NIST publications are U.S. government works in many cases, but verify any incorporated third-party content and source-specific notices. FEMA page content and attached materials likewise require item-level attribution and third-party checks.

## 7. Water Security Basics — 3 Claims / 4 EUs

Canonical records:
- Claims: `CLM-WATER_SECURITY-A/B/C@1`
- EUs: `EU-WATER_SECURITY-A/B/C@1`, `EU-EPA-WATER-SECURITY-B@1`
- Sources: `SRC-WATER_SECURITY@1` (UN-Water), `SRC-EPA-WATER-SECURITY@1` (EPA)

The UN-Water source is correctly identified as *Water Security and the Global Water Agenda*. The primary EUs need exact sections in the Analytical Brief. The EPA source is relevant to Claim B but should be pinned to the page's description of contamination threats, natural/human-made disasters and water utility disruption.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A / UN-Water | UN-Water working definition includes sustainable access to adequate quantities of acceptable-quality water | UN-Water Analytical Brief, §1 “A Working Definition of Water Security” | Direct |
| B / UN-Water + EPA | Water security includes protection from pollution and water-related disasters and preservation of ecosystems | UN-Water §1 definition; EPA “Water Security” opening paragraphs on contamination threats and natural/human-made disasters affecting water/wastewater utilities | Direct for pollution/disasters; UN-Water is the source for ecosystems |
| C / UN-Water | Assessment depends on water-cycle conditions, population, infrastructure, environment and social context | UN-Water Analytical Brief §1 and §3D “Climate Change and Water Security”; the brief identifies geography, water availability/utilization, demographic change, management/allocation systems, legal frameworks, governance, ecosystem resilience and hydrological variability | Direct for the named dimensions, but the current Claim's list should not be treated as exhaustive |

Sources:
- UN-Water, *Water Security and the Global Water Agenda*: https://www.unwater.org/publications/water-security-and-global-water-agenda
- UN-Water Analytical Brief PDF, §1 and §3D: https://www.unwater.org/sites/default/files/app/uploads/2017/05/analytical_brief_oct2013_web.pdf
- EPA, “Water Security”: https://www.epa.gov/emergency-response-research/water-security
- EPA, “Basic Information about Source Water Protection”: https://www.epa.gov/sourcewaterprotection/basic-information-about-source-water-protection

**Recommended remediation:** pin EU A to §1; pin EU B to §1 and the EPA opening paragraphs, keeping the distinct contributions explicit; pin EU C to §1 and §3D. The EPA EU supports the drinking-water infrastructure and contamination/disaster dimension; it does not independently establish the full UN-Water ecosystem-preservation definition. Keep the claim framed as the UN-Water working definition, not as a universal legal standard binding all states.

Rights: UN-Water and EPA documents require source-specific attribution and reuse checks. Do not reproduce third-party images or treat an EPA drinking-water security page as equivalent to the broader UN-Water definition of water security.

## 8. Cross-slice findings and priority ranking

### Priority 1 — clear locator-only work after bounded authorization

- Agrifood Systems A/B/C primary FAO EUs: direct exact headings/definitions exist.
- Food Distribution A/B/C: direct FAO Chapter 1 section and topic locators exist; preserve urban scope.
- Infrastructure Resilience A/B/C: direct NIST SP 1190 and Playbook locators exist.
- Water Security A/B/C: direct UN-Water sections exist; EPA provides a bounded additional source for B.
- Agricultural Engineering A/B: direct FAO mechanization/post-harvest passages exist, subject to splitting irrigation/drainage examples where needed.

### Priority 2 — source identity or scope correction before locator insertion

- Agricultural Engineering Source currently points to FAO land/soil/water management and should be corrected or split.
- Ecophysiology Source identity/URL is materially mismatched; Claim C lacks direct support in the existing source.
- Food Distribution WFP Source title/URI mismatch: the current URI is a procurement infographic, not the WFP Supply Chain overview.
- Agrifood independent World Bank EU has no direct locator; do not count as complete independent corroboration until pinned.
- FEMA independent EUs need exact primer locators; NIST Vol. II is the direct fallback.

### Priority 3 — editorial narrowing / additional support

- Agricultural Engineering C: narrow to local technological/economic/social/environmental/cultural context or support each factor separately.
- Ecophysiology A/B: keep the condition/function range boundary and avoid implying a single universal tolerance interval.
- Ecophysiology C: add a measurement-method source; no direct locator in the current Source.
- Food Distribution A/B/C: make the urban-system scope explicit where using FAO's city-focused manual.
- Infrastructure Resilience A: avoid combining “prepare/adapt/withstand/recover” into a single definition unless each term is sourced.

## 9. Rights, editorial and release gates

- All claims remain HOLD.
- No legal, licensing or commercial reuse clearance is implied by public access.
- OpenStax Biology 2e has CC BY-NC-SA 4.0 terms and a current AI-ingestion/generative-AI restriction that needs owner/legal review.
- FAO, World Bank, WFP, NIST, FEMA, UN-Water and EPA sources require exact attribution and item-specific rights checks, especially for images, figures, tables and third-party material.
- High-consequence topics include food availability/distribution, water security and infrastructure resilience. Claims are conceptual and must not be converted into operational safety thresholds, engineering design specifications, emergency plans or water-quality limits without domain-specific standards and review.
- Machine conformance and a pinned locator do not establish truth, sufficient evidence diversity, rights clearance or release eligibility.

## 10. Explicit non-actions

This report does not:
- authorize or perform canonical JSON changes;
- change any Claim statement/version or EU/source version;
- create or rename canonical IDs;
- change publication_status, completion_status, candidate allowlists or INCLUDE/HOLD/EXCLUDE decisions;
- change Context, Scope or Relations;
- alter validators, storage, recovery or release-gate semantics;
- merge PR #22, deploy or change `main`.

**Owner decision required:** approve bounded locator-only updates for the directly supported EUs; approve Source identity/URI corrections separately; decide whether to narrow Claims C in Agricultural Engineering and A/B/C in Ecophysiology; retain HOLD until rights and independent editorial/Human View review close.
