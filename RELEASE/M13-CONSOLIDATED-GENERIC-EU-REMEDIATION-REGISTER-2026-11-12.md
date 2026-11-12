# M13 consolidated generic-Evidence-Use remediation register and structural findings

Date: 2026-11-12
Repository branch: m13-system-wide-depth-audit-2026-10-09
Scope: full 4,834-record inventory; 1,494 Claims; 1,670 Evidence Use records; 619 Sources. Evidence-linkage artifact from Reference workflow run 43262022587, validated against the current content tree; later branch commits in this interval changed release reports only, not canonical content records.

## 1. Executive reconciliation

The static evidence-linkage audit found 1,143 structural finding rows:

| Finding | Rows | Current interpretation |
|---|---:|---|
| Generic Evidence Use descriptions | 519 | Candidate locator/remediation worklist; not proof that sources are invalid. |
| Separator-only filename/ID aliases | 493 | Hyphen/underscore naming variation; comparison-only normalization. |
| Duplicate Source URI candidates | 77 | 33 shared-URI groups; source independence cannot be inferred from repeated IDs. |
| Source identity sentence candidates | 48 | Source metadata needs bibliographic identity review. |
| Filename/internal-ID mismatches | 6 | Three Claim and three Evidence Use records in web-systems-basics. |

All 4,834 files were valid JSON. The 519 generic EU IDs were all mapped to exactly one Claim in the generated worksheet: 519/519 mapped, 0 orphaned generic EU IDs.

The 140-Claim machine high-consequence generic-EU subset now has source-passage report coverage 140/140. The residual 49 were content-screened and source-reviewed: 23 moderate and 26 low direct-consequence Claims. The 23 moderate had an earlier dedicated report and were cross-checked in the new thematic reports; the 26 low Claims received their first source-passage review in this pass.

Across the 49 residual Claims:
- 39 direct source support at the stated scope;
- 7 partial support / source or jurisdiction augmentation required;
- 3 not directly supported by the current source chain.

“Direct” means the external passage supports the proposition at the stated scope. It does not mean the canonical EU has been repaired. Exact locators are proposed in the linked reports but canonical locators added remain 0.

The current-rubric recalibration report identifies 38 of the 140 high-consequence Claims with historical E=2 or E=3. Under the current M13 locator rule, all 140 remain provisional current E=1 / HOLD until the canonical EU stores a reproducible Claim-specific locator and the passage is verified. Historical scores remain preserved as historical assessments.

## 2. Residual-49 Claim remediation register

Status key:
- DIRECT — passage supports the Claim at the stated scope; add the exact locator to the canonical EU only after bounded authorization.
- PARTIAL — add a source, narrow the Claim, or add jurisdiction/date/standard boundaries.
- NOT DIRECT — current source chain does not support the full proposition; replace/add an appropriate source or revise the Claim after editorial review.

| Claim ID | Priority route | Passage status | Required remediation | Review report |
|---|---|---|---|---|
| CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A | LOW | DIRECT | OpenStax Biology 2e §§1.2, 43.6–43.7; keep animal-development scope. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B | LOW | DIRECT | OpenStax Biology 2e §§43.7 and 27.1; exact differentiation/tissue locator. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-VIROLOGY_BASICS-A | LOW | DIRECT | OpenStax Biology 2e §§21.1–21.2; distinguish viral host types. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-HISTORY_METHODS_BASICS-A | LOW | DIRECT | AHA History Discipline Core: methods and historical record. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-HISTORY_METHODS_BASICS-C | LOW | DIRECT | AHA Historical Thinking Skills: chronology versus causation. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-HUMAN_RIGHTS_BASICS-B | MODERATE | DIRECT | UDHR Preamble and Articles 1–2; preserve declaratory/normative scope. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-ECOPHYSIOLOGY_BASICS-A | LOW | DIRECT | OpenStax Biology 2e §§33.3 and 44.2; restrict animal/temperature generalization. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-ECOPHYSIOLOGY_BASICS-B | LOW | DIRECT | OpenStax Biology 2e §§33.3 and 44.2; restrict animal/temperature generalization. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-MICROECONOMICS_BASICS-A | LOW | DIRECT | OpenStax Principles of Economics 3e §§3.1–3.2; preserve ceteris paribus. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-ACCOUNTING_BASICS-B | MODERATE | DIRECT | IFRS Conceptual Framework Chapters 1 and 7; exact presentation/disclosure locators. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-ACCOUNTING_BASICS-C | MODERATE | DIRECT | IFRS Conceptual Framework Chapters 4–7; add applicable standard for applied use. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-ADMINISTRATIVE_LAW_BASICS-A | MODERATE | DIRECT | Cornell Wex, Administrative law; explicitly mark U.S. jurisdiction. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-BEHAVIORAL_ECONOMICS_BASICS-A | MODERATE | DIRECT | Nobel Prize 2002 press release, Kahneman/prospect theory paragraphs. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-CELL_BASICS-A | LOW | DIRECT | OpenStax Biology 2e §4.1, Cell Theory. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-CELL_BASICS-B | LOW | DIRECT | OpenStax Biology 2e §§4.2–4.3, prokaryotic/eukaryotic cells. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-CELL_BASICS-C | LOW | DIRECT | OpenStax Biology 2e §§4.2–4.3, cell components and organelles. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-COMPUTING_BASICS-A | LOW | DIRECT | OpenStax Introduction to Computer Science §5.1, computer systems. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-COMPUTING_BASICS-B | LOW | DIRECT | OpenStax Introduction to Computer Science §§2.1, 3.1–3.2, algorithms/input/output. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-COMPUTING_BASICS-C | LOW | DIRECT | OpenStax Introduction to Computer Science §5.1; scope to conventional binary systems. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-CONSTITUTIONAL_SYSTEMS_BASICS-A | MODERATE | DIRECT | OpenStax Introduction to Political Science §§9.2 and 10.1; retain country variation. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B | MODERATE | DIRECT | OpenStax Introduction to Political Science §10 Key Terms and §10.1. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C | MODERATE | DIRECT | OpenStax Introduction to Political Science §§10.1 and 10.5; powers vary by constitution. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-DEVELOPMENT_ECONOMICS_BASICS-A | LOW | DIRECT | World Bank Economic Review, McKenzie 2017, abstract and four-topic findings. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-DIPLOMACY_BASICS-A | MODERATE | DIRECT | UN Treaty Collection, Vienna Convention treaty status and Article 51. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-DIPLOMACY_BASICS-B | MODERATE | DIRECT | Vienna Convention on Diplomatic Relations, Preamble and Articles 2–3. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-HUMAN_RIGHTS_BASICS-A | MODERATE | DIRECT | UN UDHR official page, proclamation date and GA resolution 217 A. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-INTERNATIONAL_RELATIONS_BASICS-A | MODERATE | DIRECT | UN Charter official page, signature/entry-into-force dates. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-LABOR_RELATIONS_BASICS-A | MODERATE | DIRECT | ILO Convention No. 154, Article 2; preserve national-law variation. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-MATTER_BASICS-A | LOW | DIRECT | OpenStax Chemistry 2e §1.2, classification of matter. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-MOTION_BASICS-A | LOW | DIRECT | OpenStax University Physics Volume 1 §3.1, position/reference frame. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-MOTION_BASICS-B | LOW | DIRECT | OpenStax University Physics Volume 1 §3.1; wording must mean average velocity, not scalar average speed. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-MOTION_BASICS-C | LOW | DIRECT | OpenStax University Physics Volume 1 §3.3, average/instantaneous acceleration. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-POLITICAL_SCIENCE_BASICS-A | LOW | DIRECT | OpenStax Introduction to Political Science §1.3, systematic study of politics. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-POLITICAL_SCIENCE_BASICS-B | LOW | DIRECT | OpenStax Introduction to Political Science §§1.3 and 1.5, empirical method. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-POLITICAL_SCIENCE_BASICS-C | LOW | DIRECT | OpenStax Introduction to Political Science §1.5 and Chapter 1 key terms. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-PUBLIC_FINANCE_BASICS-A | MODERATE | DIRECT | IMF Fiscal Policy, overview and how fiscal policy works. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-PUBLIC_FINANCE_BASICS-C | MODERATE | DIRECT | IMF Fiscal Policy, taxes/spending/revenue/expenditure relationship. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-PUBLIC_POLICY_BASICS-A | MODERATE | DIRECT | OECD Government at a Glance 2025 §5.2, public policy evaluation. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-TAXATION_BASICS-A | MODERATE | DIRECT | OECD Tax Policy, revenue objective; add domestic statute for applied use. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-INTERNATIONAL_LAW_BASICS-A | MODERATE | PARTIAL | Add ICJ Reparation for Injuries and international legal-personality doctrine; narrow subjects/fields. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-ACCOUNTING_BASICS-A | MODERATE | PARTIAL | Add an accounting-cycle/bookkeeping source; IFRS Conceptual Framework alone does not explain transaction recording. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-CIVIL_SOCIETY_BASICS-A | LOW | PARTIAL | Add OECD DAC Recommendation definition and retrieve exact page from the canonical World Bank PDF. | [R2](M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md) |
| CLM-COMPARATIVE_LAW_BASICS-A | MODERATE | PARTIAL | Add University of Michigan comparative-law definition and exact method locator. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-C | MODERATE | PARTIAL | Add specific WBDG planning/commissioning pages and local construction/contract law. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-FINANCE_BASICS-A | MODERATE | PARTIAL | Add OpenStax Principles of Finance 2e §§7.1 and 9.1; Investor.gov landing page is insufficient. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-PUBLIC_ADMINISTRATION_BASICS-C | MODERATE | PARTIAL | Add OECD Public Integrity Handbook plus jurisdiction-specific primary law. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |
| CLM-ECOPHYSIOLOGY_BASICS-C | LOW | NOT DIRECT | Replace/augment with comparative-physiology methods source on controlled measurement conditions. | [R1](M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md) |
| CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A | LOW | NOT DIRECT | Replace the regional UNESCO history page with a scholarly source on comparative method/context. | [R3](M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md) |
| CLM-LABOR_ECONOMICS_BASICS-A | LOW | NOT DIRECT | Add a labor-economics textbook or ILO labor-market source covering employment, wages, supply/demand and institutions. | [R4](M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md) |

The 49 rows above are grouped in four append-only source-passage reports:
- R1: M13-HIGH-CONSEQUENCE-DEVELOPMENT-VIROLOGY-HISTORY-HUMAN-RIGHTS-ECOPHYSIOLOGY-REVIEW-2026-11-12.md
- R2: M13-HIGH-CONSEQUENCE-ECONOMICS-ACCOUNTING-ADMIN-LAW-CELL-BIOLOGY-CIVIL-SOCIETY-REVIEW-2026-11-12.md
- R3: M13-HIGH-CONSEQUENCE-COMPARATIVE-CIVILIZATIONS-LAW-COMPUTING-CONSTITUTIONAL-SYSTEMS-DEVELOPMENT-ECONOMICS-REVIEW-2026-11-12.md
- R4: M13-HIGH-CONSEQUENCE-DIPLOMACY-FINANCE-LABOUR-PHYSICS-POLITICAL-SCIENCE-PUBLIC-FINANCE-REVIEW-2026-11-12.md

### Reconciliation with the prior 23-Claim moderate report

The earlier RELEASE/M13-REMAINING-49-MODERATE-23-CLAIM-SOURCE-PASSAGE-REVIEW-2026-11-12.md remains part of the audit trail. The new R1–R4 reports rechecked the 23 moderate Claims while adding first-pass source review for the 26 low direct-consequence Claims. Do not count the overlap twice. The residual-49 unique coverage is 49/49, not 72/49.

## 3. Full generic-EU queue

The 519 generic EU records are the full candidate remediation set. 140 belong to the machine high-consequence route; 379 remain outside that subset and should be processed in thematic batches after the high-consequence canonical locator work is complete.

Non-exclusive risk-domain counts among the 519 generic-EU-linked Claims:
- legal/financial: 56
- health/medical: 25
- construction/tools/materials: 18
- communications/information continuity: 15
- water/food/sanitation: 12
- electricity/energy: 11
- transport/access: 9
- emergency/fire/CO: 8
- chemicals/hazards: 5
- shelter/evacuation/access: 4

These counts overlap; a Claim can have multiple domain flags. Machine flags route work but do not substitute for a content-based risk decision.

## 4. Duplicate Source URI candidates — 77 records, 33 URI groups

A repeated URI does not prove two Source records are identical, nor does it establish independent corroboration. The 77 rows form 33 groups: 26 pairs, 5 triples, one group of four and one group of six.

| Source records in group | Shared URI | Source IDs |
|---:|---|---|
| 3 | https://apps.usgs.gov/thesaurus/thesaurus-full.php | SRC-GEOMORPHOLOGY_BASICS; SRC-MINERALOGY_BASICS; SRC-PETROLOGY_BASICS |
| 2 | https://cdc.gov/niosh/electrical-safety/about/ | SRC-ELECTRICAL_SAFETY_BASICS; SRC_ELECTRICAL_SAFETY_NIOSH |
| 2 | https://csrc.nist.gov/glossary/term/network | SRC-COMPUTER_NETWORKS_BASICS; SRC-NETWORKS_BASICS |
| 2 | https://library.si.edu/research/history-science-technology | SRC-HISTORY_OF_SCIENCE; SRC-HISTORY_OF_TECHNOLOGY |
| 2 | https://nap.nationalacademies.org/read/23674/chapter/4 | SRC-COMMUNICATION_BASICS; SRC-SCIENTIFIC_COMMUNICATION_BASICS |
| 2 | https://openstax.org/books/biology-2e/pages/4-introduction | SRC-CELL_BASICS; SRC-CELL_BIOLOGY_BASICS |
| 2 | https://openstax.org/books/biology-2e/pages/46-introduction | SRC-BEHAVIORAL_BIOLOGY_BASICS; SRC-ECOLOGY_BASICS |
| 2 | https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity | SRC-BIODIVERSITY_BASICS; SRC-CONSERVATION_BIOLOGY_BASICS |
| 2 | https://www.ala.org/acrl/standards/ilframework | SRC-ACRL-CRITICAL-INQUIRY-2026; SRC-ACRL-INFORMATION-LITERACY-2026 |
| 2 | https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html | SRC-CDC-WATER-STORAGE-2025; SRC-CDC-WATER-STORAGE-ATTRIBUTION-2025 |
| 2 | https://www.cdc.gov/water-emergency/about/index.html | SRC-CDC-WATER-EMERGENCY-2024; SRC-CDC-WATER-FILTER-2025 |
| 3 | https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water | SRC-EPA-EMERGENCY-DISINFECTION-WATER; SRC-EPA-EMERGENCY-WATER-2026; SRC-EPA-WATER-TREATMENT-2026 |
| 2 | https://www.epa.gov/npdes/municipal-wastewater | SRC_WASTEWATER_ENGINEERING_BASICS; SRC_WASTEWATER_TREATMENT_BASICS |
| 2 | https://www.fao.org/food-systems/en | SRC-AGRIFOOD_SYSTEMS_BASICS; SRC-FOOD_SYSTEMS |
| 2 | https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency | SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025; SRC-M4-INFRASTRUCTURE-DEPENDENCY-FEMA |
| 2 | https://www.genome.gov/genetics-glossary | SRC-GENETICS_BASICS; SRC-GENOMICS_BASICS |
| 2 | https://www.ilo.org/topics/social-protection | SRC-SOCIAL_INSURANCE_BASICS; SRC-SOCIAL_PROTECTION_BASICS |
| 3 | https://www.itl.nist.gov/div898/handbook/ | SRC-PROBABILITY_BASICS; SRC-SAMPLING_BASICS; SRC-STATISTICS_INFERENCE_BASICS |
| 2 | https://www.nasa.gov/reference/system-engineering-handbook-appendix/ | SRC-RELIABILITY_ENGINEERING_BASICS; SRC-REQUIREMENTS_ENGINEERING_BASICS |
| 4 | https://www.nasa.gov/reference/systems-engineering-handbook/ | SRC-DECISION_ANALYSIS_BASICS; SRC-OPERATIONS_MANAGEMENT_BASICS; SRC-SYSTEMS_ENGINEERING_BASICS; SRC-SYSTEMS_MODELING_BASICS |
| 2 | https://www.ncbi.nlm.nih.gov/books/ | SRC_BIOINFORMATICS_BASICS; SRC_SYSTEMS_BIOLOGY_BASICS |
| 3 | https://www.nist.gov/building-science | SRC-BUILDING_ENVELOPE_BASICS; SRC-CONSTRUCTION_BASICS; SRC_BUILDING_SCIENCE_BASICS |
| 6 | https://www.nist.gov/itl | SRC-COMPUTER_ARCHITECTURE_BASICS; SRC-DATABASES_BASICS; SRC-DISTRIBUTED_SYSTEMS_BASICS; SRC-PROGRAMMING_LANGUAGES_BASICS; SRC-SOFTWARE_ENGINEERING_BASICS; SRC_DATA_GOVERNANCE_BASICS |
| 2 | https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program | SRC-EMBEDDED_SYSTEMS_BASICS; SRC-SENSOR_SYSTEMS_BASICS |
| 2 | https://www.nist.gov/metrology | SRC-MEASUREMENT_INSTRUMENTATION_BASICS; SRC-METROLOGY_BASICS |
| 2 | https://www.nist.gov/pml/owm/metric-si/si-units | SRC-NIST-SI-UNITS; SRC-UNITS_AND_MEASUREMENT |
| 3 | https://www.noaa.gov/education/resource-collections/weather-atmosphere | SRC-ATMOSPHERIC_SCIENCE_BASICS; SRC-METEOROLOGY_BASICS; SRC-WEATHER_BASICS |
| 2 | https://www.osha.gov/process-safety-management | SRC-INDUSTRIAL_SAFETY_BASICS; SRC_INDUSTRIAL_PROCESS_SAFETY_BASICS |
| 2 | https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/earthquake.html | SRC-RED-CROSS-AFTERSHOCK-2026; SRC-RED-CROSS-EARTHQUAKE |
| 2 | https://www.unesco.org/en/artificial-intelligence/recommendation-ethics | SRC-AI_ETHICS_BASICS; SRC-DATA_ETHICS_BASICS |
| 2 | https://www.usgs.gov/mission-areas/water-resources | SRC-WATER_RESOURCES_BASICS; SRC-WATER_RESOURCES_MANAGEMENT_BASICS |
| 2 | https://www.usgs.gov/programs/national-geospatial-program/geographic-information-systems-gis | SRC-GEOSPATIAL_ANALYSIS_BASICS; SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS |
| 2 | https://www.who.int/health-topics/sexual-and-reproductive-health-and-rights | SRC_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES; SRC_WHO_SRH_FACTS_2026 |

### Priority adjudication order

1. Safety-critical groups: CDC emergency water, EPA emergency disinfection, NIOSH electrical safety, municipal wastewater, FEMA infrastructure dependency, OSHA process safety, WHO sexual/reproductive health.
2. Technical assurance groups: NIST IT (six records), NASA Systems Engineering Handbook (four records), NIST building science, NIST metrology, NIST IoT.
3. General academic groups: OpenStax biology, NIST statistics handbook, USGS/NOAA, ACRL, Smithsonian/NA, FAO, UNESCO and other groups.

For each group:
- inspect the exact Source record title/issuer/version/date and actual page content;
- distinguish same document from same broad landing page;
- add exact section/page locators to each relevant EU;
- do not count identical pages as independent sources;
- preserve Source IDs and history until a versioned consolidation is authorized.

## 5. Source identity sentence candidates — 48 records

The static audit found 48 Source records whose source_identity value is sentence-like. This is a metadata review candidate, not automatic proof of invalidity. The Source identity should be checked against the actual bibliographic source title, issuer, version/date and URI; a proposition about the subject should not silently substitute for the identity of the source.

SRC-ACCOUNTING_BASICS; SRC-ALGEBRA_BASICS; SRC-ARTIFICIAL_INTELLIGENCE_BASICS; SRC-ATMOSPHERIC_SCIENCE_BASICS; SRC-BEHAVIORAL_BIOLOGY_BASICS; SRC-BIODIVERSITY_BASICS; SRC-CALCULUS_BASICS; SRC-CLOUD_COMPUTING_BASICS; SRC-COMBINATORICS_BASICS; SRC-COMPUTER_ARCHITECTURE_BASICS; SRC-CONSERVATION_BIOLOGY_BASICS; SRC-CRYPTOGRAPHY_BASICS; SRC-CYBERSECURITY_BASICS; SRC-DATABASES_BASICS; SRC-DEMOGRAPHIC_METHODS_BASICS; SRC-DEVELOPMENTAL_BIOLOGY_BASICS; SRC-DISTRIBUTED_SYSTEMS_BASICS; SRC-ECOPHYSIOLOGY_BASICS; SRC-EDUCATION_SCIENCE_BASICS; SRC-FINANCE_BASICS; SRC-GEOMETRY_BASICS; SRC-GEOMORPHOLOGY_BASICS; SRC-HISTORY_METHODS_BASICS; SRC-LINEAR_ALGEBRA_BASICS; SRC-MACROECONOMICS_BASICS; SRC-MEASUREMENT_UNCERTAINTY_BASICS; SRC-METEOROLOGY_BASICS; SRC-MICROBIOME_BASICS; SRC-MICROECONOMICS_BASICS; SRC-MINERALOGY_BASICS; SRC-NUMBER_THEORY_BASICS; SRC-NUMERICAL_METHODS_BASICS; SRC-ORGANIZATIONAL_BEHAVIOR_BASICS; SRC-PALEONTOLOGY_BASICS; SRC-PARASITOLOGY_BASICS; SRC-PETROLOGY_BASICS; SRC-PLANT_PHYSIOLOGY_BASICS; SRC-PROGRAMMING_LANGUAGES_BASICS; SRC-PUBLIC_ADMINISTRATION_BASICS; SRC-REMOTE_SENSING_BASICS; SRC-SCIENTIFIC_METHOD_BASICS; SRC-SEISMOLOGY_BASICS; SRC-SOFTWARE_ENGINEERING_BASICS; SRC-TRIGONOMETRY_BASICS; SRC-URBAN_PLANNING_BASICS; SRC-VIROLOGY_BASICS; SRC-VOLCANOLOGY_BASICS; SRC-ZOOLOGY_BASICS

Priority candidates for immediate metadata review include cybersecurity, cryptography, accounting, finance, public administration, software engineering, computer architecture, databases, distributed systems, virology and ecophysiology. Examples already inspected:
- SRC-CYBERSECURITY_BASICS: identity is a Russian definition sentence; URI is the NIST Cybersecurity Framework landing page.
- SRC-CRYPTOGRAPHY_BASICS: identity is a definition sentence; URI is the NIST Cryptography landing page.
- SRC-PUBLIC_ADMINISTRATION_BASICS: identity is a definition sentence; URI is the OECD public-governance landing page.
- SRC-FINANCE_BASICS: identity is a definition sentence; URI is Investor.gov Investing Basics.
- SRC-ECOPHYSIOLOGY_BASICS: identity is a definition sentence; the current OpenStax URI path was not retrievable as a valid page in the source-passage review.
- SRC-SOFTWARE_ENGINEERING_BASICS, SRC-COMPUTER_ARCHITECTURE_BASICS, SRC-DATABASES_BASICS and SRC-DISTRIBUTED_SYSTEMS_BASICS use the broad NIST IT landing page rather than a topic-specific source page.

## 6. Filename and identifier reconciliation

- 493 separator-only filename/ID aliases occur across record types. These are format-only hyphen/underscore differences; retain stored identifiers and use normalization only for comparison.
- Six genuine filename/internal-ID mismatch rows exist in web-systems-basics:
  - Claim files CLM-A.json, CLM-B.json, CLM-C.json contain full internal IDs CLM-WEB_SYSTEMS_BASICS-A/B/C.
  - Evidence Use files EU-A.json, EU-B.json, EU-C.json contain full internal IDs EU-WEB_SYSTEMS_BASICS-A/B/C.
- The scored-report ledger separately reports 160 separator-only differences in Claim filename/internal-ID pairs and 3 genuine Claim mismatches. These are not contradictory: the 493 alias rows include multiple record types, while the ledger's 160/3 split is Claim-only.
- One Batch 44 report alias, CLM-POWER_ELECTRONICS_BASICS_B@1, matches a canonical Claim only after separator normalization and version suffix handling; manual confirmation remains required.

No path, stored ID, relation or canonical record is changed by this report.

## 7. Current-rubric E-score boundary

The separate RELEASE/M13-HIGH-CONSEQUENCE-E-SCORE-RECALIBRATION-38-CLAIMS-2026-11-12.md records:
- 140 high-consequence generic-EU Claims;
- historical E=1: 102;
- historical E=2: 33;
- historical E=3: 5;
- 38 historical E=2/3 rows require current-rubric recalibration.

The current rubric requires a reproducible Claim-specific locator in the canonical EU. Until that is present and checked, current E is provisionally 1 for all 140. Historical reports and scores remain unchanged.

## 8. Controlled next sequence

1. Build the versioned canonical EU correction proposal for the 140 high-consequence records, starting with water/food/sanitation, health, electrical safety, emergency/shelter, occupational safety, construction and transport.
2. Reconcile the 38 historical E=2/3 rows against the current locator rule; do not overwrite historical scores.
3. Adjudicate the 33 duplicate-URI groups, beginning with safety-critical sources; confirm whether each is the same document, a broad landing page or distinct source material.
4. Correct the 48 Source identity sentence candidates using actual bibliographic titles and issuers.
5. Resolve the six web-systems-basics path/ID mismatches with reference/Relation regression tests.
6. Process the remaining 379 generic-EU records in thematic batches.
7. Preserve the 493 separator aliases unless a separate naming migration is explicitly authorized.

## 9. Acceptance boundary

- Canonical Claim/Evidence Use/Source JSON changed: 0.
- Canonical Evidence Use locators added: 0.
- D/E/B scores changed by these supplementary reviews: 0.
- Specialist peer review and Human View completed: 0.
- Claims accepted or release-cleared: 0.
- All affected Claims remain HOLD until canonical source-chain repair and all independent release gates pass.

This register is a precise work plan, not a release approval.
