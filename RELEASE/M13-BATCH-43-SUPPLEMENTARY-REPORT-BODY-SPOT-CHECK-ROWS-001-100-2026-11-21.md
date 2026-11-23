# M13 Batch 43 — complete report-body inspection (rows 001–100)

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: all 100 Batch 43 scored-row reports.  
Method: fetched and read the complete body of every report, including Claim text, historical Claim/Evidence Use/Source version header, passage-review discussion, D/E/B rationale and disposition.  
Status: **100/100 report bodies inspected. Historical scores remain historical. No canonical record changed.**

## 1. Inspection result

Batch 43 worklist describes a frozen set of 100 unique Claim versions. All 100 corresponding report files exist and were individually fetched and read. All 100 contain a Claim/Evidence Use/Source version header and a D/E/B assessment with a disposition.

Historical score distribution from the report bodies:

| Dimension | Score 1 | Score 2 | Score 3 | Total |
|---|---:|---:|---:|---:|
| D (Depth) | 5 | 29 | 66 | 100 |
| E (Evidence) | 26 | 67 | 7 | 100 |
| B (Boundaries) | 6 | 61 | 33 | 100 |

These are counts of historical report scores only. They are not current accepted assessments and must not be copied into the current worksheet.

## 2. Row-level inspection ledger

| Row | Historical Claim ID | D/E/B | Body-inspection finding |
|---:|---|---:|---|
| 001 | `CLM-SEPTIC-REDUCE-WATER@1` | 2/2/2 | CDC septic emergency page directly supports reducing nonessential water use; canonical EU lacks the exact “During/After an emergency” locator; retain emergency-context qualifiers. |
| 002 | `CLM-SEPTIC-SEWAGE-CONTACT@1` | 2/2/2 | CDC directly warns against contact with floodwater that may contain sewage; preserve broad contamination boundary, not only visible overflow. |
| 003 | `CLM-DISASTER_RESPONSE_FEMA_A@1` | 1/2/2 | FEMA glossary “Response” entry closely matches; exact entry locator missing from EU; keep separate from recovery and operational powers. |
| 004 | `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1` | 1/2/2 | FEMA course objectives support partner roles, but government/private/community categories are not all expressly listed in the cited passage. |
| 005 | `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1` | 2/1/1 | FEMA course overview does not directly support the full jurisdiction/event/system dependency; insufficient passage-level evidence. |
| 006 | `CLM-FIRE-C@1` | 2/1/2 | Canonical Ready.gov page returned 403; a related official PDF supports residual heat hazards but is not the linked canonical source and cannot be silently substituted. |
| 007 | `CLM-HUMANITARIAN_LOGISTICS_BASICS-C@1` | 1/1/1 | WFP Logistics Cluster page is topically relevant but does not evidence after-action learning, practice sharing and future preparedness as a combined proposition; trailing slice label is editorial. |
| 008 | `CLM-SEPTIC-PROFESSIONAL-INSPECTION@1` | 2/1/1 | Canonical EPA page could not be fetched; CDC is a different source and cannot replace it; “requires” may overstate source wording. |
| 009 | `CLM-WATER-FILTER-LIMITS@1` | 2/2/2 | CDC directly supports portable-filter limits and absolute pore-size thresholds; keep the warning that filtration does not remove all pathogens. |
| 010 | `CLM-SYSTEMS_THINKING_BASICS-D@1` | 2/2/1 | WHO supports interaction/interdependency and unintended effects in health systems; Claim generalizes cross-domain and adds feedback without direct support. |
| 011 | `CLM-WOODWORKING_BASICS-D@1` | 2/1/1 | OSHA supports irritant/respiratory effects of wood dust, but not the full cutting/sanding and process-specific control proposition. |
| 012 | `CLM_WATER_QUALITY_WHO_A@1` | 2/1/2 | WHO current guideline page supports health-based targets/preventive risk management, but stored canonical URI did not resolve and current alternative URI is not linked; URI reconciliation needed. |
| 013 | `CLM-PLANT_PATHOLOGY_BASICS-A@1` | 1/2/2 | APS directly supports plant-pathology definition; EU lacks heading locator; copyright/attribution is separate. |
| 014 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B@1` | 2/2/2 | SAMHSA directly supports preparedness/response/recovery/mitigation scope; exact locator and rights review remain. |
| 015 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-C@1` | 2/1/2 | Canonical SAMHSA page supports broad phases/community context but not full intervention-tailoring statement; a more direct separate page is not in the canonical chain. |
| 016 | `CLM-ENTOMOLOGY_BASICS-B@1` | 2/2/2 | Entomological Society of America directly supports beneficial and harmful insect roles; EU lacks pinpoint; copyrighted page is not reuse permission. |
| 017 | `CLM-ENTOMOLOGY_BASICS-C@1` | 1/2/2 | ESA page explicitly lists application areas; EU lacks section locator and rights/attribution remain. |
| 018 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-B@1` | 2/1/1 | WHO environmental-health overview is relevant but does not define the claimed exposure-assessment method; direct risk-assessment source needed. |
| 019 | `CLM-ERGONOMICS_BASICS-A@1` | 2/2/2 | NIOSH directly defines ergonomics around designing tasks to fit worker capabilities; exact EU locator missing; not proof a specific workstation is safe. |
| 020 | `CLM-FOOD_SECURITY_BASICS-D@1` | 2/2/2 | USDA ERS definition directly supports household food security; “What Is Food Security?” locator and rights/attribution still needed. |
| 021 | `CLM-HEALTH_ECONOMICS_BASICS-A@1` | 2/2/2 | WHO health-economics page supports allocation, cost, budget impact and efficiency; EU lacks exact sections; not a complete policy-priority rule. |
| 022 | `CLM-HEALTH_ECONOMICS_BASICS-B@1` | 2/2/2 | WHO supports prioritization and resource allocation under constraints; EU section locator missing; economic analysis does not decide alone. |
| 023 | `CLM-HEALTH_ECONOMICS_BASICS-C@1` | 2/1/2 | Linked WHO page supports efficiency but not full financial-protection/UHC clause; separate WHO source cannot be silently substituted. |
| 024 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A@1` | 2/2/2 | WHO HTA overview directly defines systematic multidisciplinary evaluation; exact EU locator missing. |
| 025 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B@1` | 2/1/2 | Linked WHO page does not enumerate the full clinical/social/economic/organizational/ethical list; a better WHO Q&A page is not in the canonical chain. |
| 026 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C@1` | 2/2/2 | WHO supports policy-level decision role; “not individualized medical advice” is editorial boundary language, not a direct source quote. |
| 027 | `CLM-HISTORY_OF_MEDICINE-A@1` | 3/2/2 | NLM MeSH directly supports study of past events and development in medicine; Claim’s knowledge/practice extension exceeds exact wording. |
| 028 | `CLM-HISTORY_OF_MEDICINE-B@1` | 2/1/2 | Linked NLM MeSH definition does not support changing boundaries/context requirement; separate NLM guidance is not in canonical chain. |
| 029 | `CLM-INSPECTION_BASICS-A@1` | 2/1/2 | OSHA workplace inspection source does not define inspection universally or support “predefined criteria”; scope mismatch. |
| 030 | `CLM-INSPECTION_BASICS-B@1` | 2/1/2 | OSHA page does not support the full general determinant list, especially recorded-data quality; scope mismatch. |
| 031 | `CLM-INSPECTION_BASICS-C@1` | 2/2/2 | OSHA supports identifying hazards/violations, but universal specialist-opinion boundary is not directly sourced and must be distinguished as editorial principle or separately evidenced. |
| 032 | `CLM-M4-HEALTH-RESILIENCE-A@1` | 3/2/2 | WHO toolkit directly supports maintaining essential services/adapting to disruption; current EU@2 itself notes missing exact page/module pinpoint. |
| 033 | `CLM-M5-ENVIRONMENTAL-WASTEWATER-D@1` | 2/2/3 | UNEP report is well matched to wastewater pollution/health risk and context-sensitive management, but no page/section/figure locator is stored for each clause. |
| 034 | `CLM-MANUFACTURING_BASICS-B@1` | 3/3/2 | NIST glossary definition directly lists maintenance, supply/distribution, safety and IT; exact entry URI is stable, but EU has no persisted locator/quotation and attribution review remains. |
| 035 | `CLM-MEDICAL_DEVICES_BASICS-A@1` | 3/2/2 | WHO directly supports intended-medical-purpose definition and broad device range; exact locator and jurisdictional-definition boundary missing. |
| 036 | `CLM-MEDICAL_DEVICES_BASICS-B@1` | 3/2/3 | WHO supports context/setting and safety/effectiveness, but not all claimed causal factors (device characteristics/user training) in one pinpoint; high-consequence. |
| 037 | `CLM-MEDICAL_DEVICES_BASICS-C@1` | 3/2/3 | Separate WHO regulatory framework supports jurisdictional variation, but canonical linked topic page/EU does not represent it; source alignment needed. |
| 038 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-A@1` | 3/2/2 | WHO definition directly matches mental well-being, coping, abilities, learning/work and community contribution; EU locator missing. |
| 039 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-B@1` | 3/2/2 | WHO directly supports interacting individual/family/community/structural factors; EU lacks pinpoint and individual-prediction boundary must remain. |
| 040 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-C@1` | 3/1/3 | Broad WHO mental-health topic page does not establish that general information cannot diagnose/treat; separate ICD-11 clinical source is not linked. |
| 041 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-D@1` | 3/2/3 | NIMH article supports professional-help escalation, but canonical Source is broad landing page; crisis contacts are U.S.-specific. |
| 042 | `CLM-NUTRITION_BASICS-A@1` | 3/2/2 | NIEHS directly defines nutrition as consuming/absorbing/using nutrients; “Introduction” locator missing from EU. |
| 043 | `CLM-NUTRITION_BASICS-B@1` | 3/2/2 | NIEHS “What Are Nutrients?” directly supports macro/micronutrient categories; exact EU locator missing. |
| 044 | `CLM-NUTRITION_BASICS-D@1` | 3/2/2 | WHO directly supports adequacy, balance, moderation, diversity and context variation; exact locator and rights review needed. |
| 045 | `CLM-OCCUPATIONAL_SAFETY_BASICS-A@1` | 2/2/3 | ILO supports occupational safety purpose; trailing slice-name parenthetical is an editorial artifact; exact locator and cleanup require authorized change. |
| 046 | `CLM-OCCUPATIONAL_SAFETY_BASICS-B@1` | 2/2/3 | ILO management guidance supports risk control, organization and worker participation; trailing slice-name artifact; high-consequence and locator gap. |
| 047 | `CLM-OCCUPATIONAL_SAFETY_BASICS-C@1` | 2/2/3 | ILO supports jurisdiction/workplace context; trailing slice-name artifact; exact locator and local legal boundary needed. |
| 048 | `CLM-PHYSIOLOGY_BASICS-A@1` | 3/2/2 | OpenStax A&P 2e §1.1 directly supports physiology definition; EU pinpoint and CC BY-NC-SA rights review remain. |
| 049 | `CLM-PLANT_PATHOLOGY_BASICS-B@1` | 3/2/2 | APS directly distinguishes biotic pathogens and abiotic factors; EU lacks pinpoint; rights review required. |
| 050 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-A@1` | 3/2/2 | WHO Global Health Ethics supports broad scope; exact overview locator missing; not a complete ethical framework or law. |
| 051 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-B@1` | 3/1/2 | WHO supports ethics domain generally but not all listed analytic elements (competing interests, proportionality, fairness) via a pinpoint. |
| 052 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-C@1` | 3/1/2 | WHO topic page does not directly support all four contextual factors; claim-specific source locator needed. |
| 053 | `CLM-PUBLIC_HEALTH_SURVEILLANCE_BASICS-D@1` | 3/2/3 | CDC directly supports ongoing collection/analysis/interpretation and action; exact locator for the two-clause claim missing; not individual diagnosis/live directive. |
| 054 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-B@1` | 3/2/3 | UNDRR supports context, access and channels; explicit trust component needs pinpoint; high-consequence communication. |
| 055 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-C@1` | 3/2/3 | UNDRR supports effects of ineffective/misleading risk communication; exact locator missing. |
| 056 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-D@1` | 3/2/3 | CDC supports audience/context and updates; uncertainty/numbers are more explicit in a related page not fully represented in canonical EU. |
| 057 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-A@1` | 3/1/2 | ICMJE authorship/contributor page does not directly support broad scientific-publication-as-research-communication proposition; source-fit mismatch. |
| 058 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-B@1` | 3/3/2 | ICMJE “Why Authorship Matters” directly states credit plus responsibility/accountability; exact section should be persisted in EU. |
| 059 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-C@1` | 3/2/2 | ICMJE distinguishes authors and contributors; biomedical publishing scope and exact section locator need to remain explicit. |
| 060 | `CLM-SOCIAL_POLICY_BASICS-A@1` | 3/2/2 | OECD Social Policy directly supports protection of individuals/families and well-being; exact section locator missing. |
| 061 | `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | 3/2/2 | USDA NRCS supports soil organism communities; exact page/section locator missing. |
| 062 | `CLM-SOIL_MICROBIOLOGY_BASICS-B@1` | 3/2/2 | USDA supports nutrient cycling and organism roles, but decomposition clause needs a direct pinpoint rather than inference. |
| 063 | `CLM-SOIL_MICROBIOLOGY_BASICS-C@1` | 3/2/2 | USDA supports biodiversity and soil functions; exact page/section locator missing. |
| 064 | `CLM-SYSTEMS_THINKING_BASICS-A@1` | 3/2/2 | CDC POLARIS supports interactions/dependencies and systems framing; EU lacks exact section locator. |
| 065 | `CLM-SYSTEMS_THINKING_BASICS-B@1` | 3/3/2 | CDC “Identifying Systems Problems” directly lists dynamic, interconnected, multi-organization/multiple-interest characteristics; locator should be persisted. |
| 066 | `CLM-SYSTEMS_THINKING_BASICS-C@1` | 3/3/2 | CDC “Looking for Feedback” directly supports feedback and unintended consequences; exact locator should be persisted. |
| 067 | `CLM-VACCINATION_INFORMATION_BASICS-A@1` | 3/2/3 | WHO directly supports pre-introduction phased trials and evaluation; retain ongoing post-introduction monitoring boundary; exact locator missing. |
| 068 | `CLM-WASTEWATER_BASICS-A@1` | 3/2/2 | EPA supports treatment and hydrologic-cycle context, but canonical EU does not pinpoint all stages of collection/treatment/return. |
| 069 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_A@1` | 3/2/3 | FDA drug-development overview is broad; specific mechanism-of-action/interaction passage is not in canonical Source locator. |
| 070 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_B@1` | 3/2/3 | FDA detailed material directly supports ADME, benefits, side effects and interactions, but canonical Source is the broad process page; detailed locator missing. |
| 071 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_C@1` | 3/2/3 | FDA supports staged preclinical/clinical development; population/indication boundary not pinpointed in current source chain. |
| 072 | `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_A@1` | 3/2/3 | WHO surveillance definition closely matches continuous/systematic collection, analysis and interpretation; exact section locator missing. |
| 073 | `CLM_REHABILITATION_BASICS_A@1` | 3/2/2 | WHO directly supports optimizing functioning/reducing disability; “maintain functioning” wording needs exact text check and locator. |
| 074 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A@1` | 3/2/3 | WHO topic supports contraception, fertility, pregnancy/maternal health and STIs; locator missing; list should remain illustrative. |
| 075 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_B@1` | 3/2/3 | WHO broad framing supports multidimensional reproductive health; exact life-course passage locator missing. |
| 076 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_C@1` | 3/1/3 | WHO topic page does not establish general-info/individual-care, jurisdiction and guideline-currency boundaries in one canonical passage. |
| 077 | `CLM_TELEMEDICINE_BASICS_A@1` | 3/1/3 | WHO digital-health programme page does not directly define telemedicine; dedicated definition source required. |
| 078 | `CLM_TELEMEDICINE_BASICS_B@1` | 3/1/3 | Broad WHO digital-health page does not enumerate consultation, diagnosis, treatment and follow-up as telemedicine services. |
| 079 | `CLM_TELEMEDICINE_BASICS_C@1` | 3/1/3 | Broad WHO page does not support the complete clinical/technology/connectivity/privacy/safety/context factor list; dedicated standard needed. |
| 080 | `CLM_WATER_QUALITY_BASICS_A@1` | 3/2/2 | EPA directly supports water-quality criteria as scientific benchmarks for designated uses; exact locator missing; not a site-specific safety determination. |
| 081 | `CLM-FOOD-TARGET-TEMP@1` | 3/1/3 | Linked USDA outage page does not state 40°F/0°F targets; separate source required for precise thresholds. |
| 082 | `CLM-SEED-DRY-STORAGE@1` | 3/1/2 | USDA/NRCS source identity and URI pairing need verification; current chain does not directly support humidity/viability claim. |
| 083 | `CLM-WASTEWATER_BASICS-C@1` | 3/1/2 | EPA Wastewater 101 does not directly support all variables, especially local regulatory requirements; separate source chain needed. |
| 084 | `CLM-WATER_INFRASTRUCTURE_BASICS-A@1` | 3/2/3 | EPA directly lists distribution-system pipes, storage, valves and pumps; exact EU locator missing. |
| 085 | `CLM-WATER_INFRASTRUCTURE_BASICS-B@1` | 3/2/3 | EPA directly describes distribution system as physical barrier and operation/maintenance to reduce contamination; exact locator missing. |
| 086 | `CLM-WATER_INFRASTRUCTURE_BASICS-C@1` | 3/2/3 | EPA sections cover water age, storage, pressure, corrosion, cross-connections/backflow; jurisdiction clause needs separate support and EU pinpoints. |
| 087 | `CLM_MARINE_BIOLOGY_BASICS_B@1` | 3/2/2 | NOAA Aquatic Food Webs supports feeding links and energy transfer, but canonical Source points to broad Marine Life collection. |
| 088 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A@1` | 3/2/2 | OpenStax describes staged embryonic development, but exact passage for cells/tissues/organism wording and rights review needed. |
| 089 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B@1` | 3/2/2 | OpenStax supports tissue specialization/development, but direct cell-differentiation definition and pinpoint missing. |
| 090 | `CLM-ELECTRICAL_MACHINES_BASICS-A@1` | 3/3/2 | DOE directly defines electric motor as converting electrical power into rotational mechanical power; exact definition/CFR locator needed in EU. |
| 091 | `CLM-ELECTRICAL_MACHINES_BASICS-B@1` | 3/2/2 | DOE supports category-specific U.S. motor requirements/test procedures; not a global jurisdiction comparison; pinpoint missing. |
| 092 | `CLM-ELECTRICAL_MACHINES_BASICS-C@1` | 3/2/3 | DOE directly supports energy standards and test procedures for covered motor categories; CFR sections/applicability boundary need pinpoint. |
| 093 | `CLM-ELECTRICITY_BASICS-A@1` | 3/2/3 | DOE directly supports electricity powering homes, businesses and critical infrastructure; exact locator missing. |
| 094 | `CLM-ELECTRICITY_BASICS-B@1` | 3/2/3 | DOE supports generation/transmission/substations/distribution; canonical page broad and EU lacks locator. |
| 095 | `CLM-ELECTRICITY_BASICS-C@1` | 3/2/3 | DOE directly supports continuous supply-demand balancing for reliability; exact locator missing. |
| 096 | `CLM-ELECTRONICS_BASICS-A@1` | 3/1/2 | NIST electronics topic page does not define the full processing/transmission/measurement scope; adjacent topical relevance only. |
| 097 | `CLM-ELECTRONICS_BASICS-B@1` | 3/1/2 | NIST lists semiconductors as a topic but does not directly support their claimed foundational role in components/integrated circuits. |
| 098 | `CLM-HYDROLOGY_BASICS-C@2` | 3/3/2 | USGS “What is Hydrology?” section/paragraph explicitly supports listed pathways; exact Claim/EU/Source @2 chain; rights and independent review remain. |
| 099 | `CLM-HYDROPOWER_BASICS-A@1` | 3/3/3 | DOE Hydropower Basics directly states moving water generates electricity; exact locator should be persisted; high-consequence energy topic and rights review remain. |
| 100 | `CLM-M5-ENERGY-GRID-RESILIENCE-D@1` | 3/2/3 | DOE grid modernization supports reliability, resilience, flexibility, source integration and storage; final context/risk clause lacks exact pinpoint. |

## 3. Cross-row synthesis and priority findings

### Strongest direct source-fit cases (historical E=3)

Rows 034 (NIST Manufacturing Operations), 058 (ICMJE authorship/accountability), 065–066 (CDC POLARIS systems characteristics/feedback), 090 (DOE electric-motor definition), 098 (USGS hydrology @2), and 099 (DOE hydropower) received historical E=3. Row 098 is especially important because its report explicitly names Claim@2 / EU@2 / Source@2 and records a section/paragraph locator. Even these rows remain HOLD for separate canonical locator persistence, rights/attribution, independent review and any relevant specialist gates.

### Source-chain and scope defects

- **Canonical page unavailable or URI mismatch:** 006 (Ready.gov 403), 008 (EPA fetch failure), 012 (WHO current URI mismatch), 081 (USDA outage page does not support temperature thresholds), 082 (USDA/NRCS identity/URI mismatch).
- **Different source found but not linked canonically:** 015 (SAMHSA intervention tailoring), 023 (WHO financial protection/UHC), 025 (WHO HTA dimensions), 028 (NLM changing historical boundaries), 037 (WHO regulatory framework), 040 (ICD-11 diagnostic boundary), 056 (CDC numeric/uncertainty page), 076 (reproductive-health information boundary).
- **Broad page vs specific proposition:** 010, 018, 033, 036, 057, 069–071, 077–079, 083, 087–089, 096–097, 100.
- **Editorial defects requiring separate authorized correction:** rows 007 and 045–047 contain parenthetical slice-name text in the Claim wording.
- **Rights/attribution gate:** professional-society, WHO, ILO, OpenStax, NOAA and other source terms must be assessed for the intended distribution model; public accessibility is not blanket reuse permission.

### High-consequence/specialist routing

Keep heightened review on rows 001–002, 005–009, 011–012, 014–015, 018–020, 023, 026, 032–033, 035–041, 044–047, 053–056, 067, 069–071, 074–079, 081–086, 090–095, 098–100. These touch sanitation/sewage, water treatment, wildfire hazards, wood dust, drinking-water frameworks, vaccines, medical devices, mental health, risk communication, pharmacology, reproductive health, telemedicine, food temperatures, water infrastructure, electricity and hydropower. The historical desk review is not qualified Human View or operational clearance.

## 4. Crosswalk update

The 2026-11-18 crosswalk recorded 20 individually inspected Batch 42–43 report files and 180 not yet inspected. With Batch 42 rows 001–100 now individually inspected and this complete Batch 43 body inspection:

- Batch 42 report bodies: 100/100 inspected.
- Batch 43 report bodies: 100/100 inspected.
- Combined Batch 42–43 report bodies: **200/200 inspected**.
- Combined report bodies remaining uninspected: **0**.

This updates the report-body inspection count only. It does not itself reconcile every report Claim/EU/Source chain against current canonical records. Current graph verification for Batch 42 rows 069–100 is separately documented; the other 168 report rows still require controlled current-graph reconciliation and normalized-ID deduplication. The 100 Batch 43 worklist is described as 100 unique Claim versions, but do not assume the combined 200 report rows map to 200 unique normalized IDs until the master crosswalk join is rerun.

## 5. Current assessment and non-actions

- Historical Batch 43 D/E/B distribution is recorded above; **accepted current D/E/B remains 0** in the crosswalk snapshot.
- All reports retain HOLD. No row receives publication clearance from this report-body inspection.
- No historical D/E/B copied to current worksheet.
- No current worksheet status changed from `NOT_YET_REVIEWED`; D/E/B fields remain blank.
- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record changed.
- No machine-queue exclusion, risk-domain disposition or priority change was made.
- No rights/editorial approval, specialist review, independent review, formal risk assessment or Human View approval is inferred.

## 6. Next controlled steps

1. Rerun the master ledger/crosswalk join using all 200 report files, normalize IDs for comparison only, deduplicate and explicitly adjudicate repeated groups.
2. Reconcile current canonical Claim/EU/Source IDs and versions for Batch 42 rows 001–068 and all Batch 43 rows 001–100. Batch 42 rows 069–100 have a separate exact-chain report.
3. Preserve exact historical version headers and distinguish exact current graph match from passage-level evidence acceptance.
4. Remediate source identity/URI/scope defects and add precise canonical EU locators only through separately authorized, versioned corrections.
5. Route high-consequence claims to qualified Human View, independent review, rights review and formal risk assessment as required.
