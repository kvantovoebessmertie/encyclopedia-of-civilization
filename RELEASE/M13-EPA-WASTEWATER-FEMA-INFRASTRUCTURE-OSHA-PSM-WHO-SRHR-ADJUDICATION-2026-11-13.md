# M13 duplicate-source adjudication: municipal wastewater, FEMA infrastructure dependency, OSHA process safety, and WHO SRHR

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `e4f9dbc92ca8b5945faf2501ea0ec0340cc728d4`  
Scope: four safety-critical shared-URI groups from the consolidated duplicate-source inventory. Source, Evidence Use and Claim records were inspected directly; official source pages and relevant linked standards/publications were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| EPA Municipal Wastewater | 2 | 6 | One EPA landing page. It directly supports collection/treatment/discharge and permit context; a linked EPA Primer supplies the treatment-process detail but is a separate publication and needs its own Source record. |
| FEMA Infrastructure Dependency | 2 | 6 | One FEMA resource-library page. The duplicate FEMA IDs are not independent. Three resilience Claims also have a separate NIST Community Resilience Program source that directly supports them; the FEMA page itself returned 403 on direct retrieval. |
| OSHA Process Safety Management | 2 | 6 | One OSHA overview page. It directly supports the PSM-specific Claims, but not general industrial safety without scope limits. The actual 29 CFR 1910.119 standard is a distinct and more precise source candidate. |
| WHO Sexual and Reproductive Health and Rights | 2 | 3 | One WHO topic page. It directly supports the two definitional/scope Claims; it does not directly support the individual-medical-assessment disclaimer Claim. |

**Totals: 8 Source records, 21 linked Claims, four URI groups.** Identical URLs count as one publication/page identity for independence analysis. They do not create additional corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This report is an adjudication record only.

## 2. EPA Municipal Wastewater — two IDs, one landing page

### Source identity

Both records point to `https://www.epa.gov/npdes/municipal-wastewater`:

- `SRC_WASTEWATER_ENGINEERING_BASICS`
- `SRC_WASTEWATER_TREATMENT_BASICS`

Both identify “U.S. Environmental Protection Agency — Municipal Wastewater”. The current EPA page is retrievable. It describes municipal collection systems, delivery to treatment facilities, discharge or reuse, and NPDES permits and discharge conditions. It also describes collection-system infiltration/inflow and wet-weather peak-flow operational problems.

The page links a separate publication: **EPA 832-R-04-001, _Primer for Municipal Wastewater Treatment Systems_** (September 2004). That PDF has distinct publication identity and substantive treatment-process content. It is not the same object as the municipal-wastewater landing page.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM_WASTEWATER_ENGINEERING_BASICS_A` — wastewater engineering applies engineering methods to collection, treatment and management | Partial. The landing page directly describes collection and treatment, but does not define the engineering discipline or its methods. Narrow the Claim to municipal collection/treatment functions or add a wastewater-engineering reference. |
| `CLM_WASTEWATER_ENGINEERING_BASICS_B` — treatment uses physical, biological and chemical processes | Direct in the linked EPA Primer, not fully in the landing page itself. The Primer has a “Basic Wastewater Treatment Processes” section with separate Physical, Biological and Chemical subsections (PDF pp. 10–11). Add the Primer as a separate Source record and cite those sections. |
| `CLM_WASTEWATER_ENGINEERING_BASICS_C` — design depends on influent, objectives, hydraulics, climate, regulations, resources and receiving environment | Partial. The landing page supports regulatory limits, wet-weather flows, infiltration/inflow and receiving-water/discharge context. It does not establish the full list of design variables. Add design guidance/engineering standards for influent characterization, hydraulics, climate and resource constraints. |
| `CLM_WASTEWATER_TREATMENT_BASICS_A` — municipal treatment uses physical, biological and chemical processes before discharge/management | Direct in the linked EPA Primer, which describes the three process families and their mechanisms. The current landing page links the Primer but does not itself give the same detail. Add the Primer as a separate Source record with pinpoint sections. |
| `CLM_WASTEWATER_TREATMENT_BASICS_B` — systems are designed around incoming wastewater characteristics and pollutants/conditions to control | Partial-to-direct in the EPA Primer. Its pollutant discussion and treatment-process sections describe oxygen-demanding substances, pathogens, nutrients, chemicals and thermal pollutants and how processes address them. Add exact passages; avoid implying a complete engineering design procedure. |
| `CLM_WASTEWATER_TREATMENT_BASICS_C` — effluent requirements depend on regulation, receiving environment and permitted discharge conditions | Direct for the US municipal NPDES context. The landing page states that NPDES permits establish discharge limits and conditions and describes discharge to water bodies, land or reuse. Keep the jurisdiction and permit scope explicit. |

### Disposition

- Two Source IDs, one EPA landing-page identity; no independent corroboration is created by the duplicate IDs.
- Add EPA 832-R-04-001 as a separate bibliographically complete Source record if authorized. It is a distinct publication linked from the existing page.
- The current Evidence Use records are generic and have no pinpoint locators. All six Claims remain locator-remediation candidates; the design-generalization Claim needs additional engineering evidence.

## 3. FEMA Infrastructure Dependency — two IDs, one resource-library page

### Source identity

Both records point to `https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency`:

- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025`
- `SRC-M4-INFRASTRUCTURE-DEPENDENCY-FEMA`

Both identify “FEMA — Infrastructure Dependency Primer”. These are two Source IDs for one URL, not two independent FEMA publications. Direct retrieval of the FEMA page returned HTTP 403 during this review, so its current page text and exact linked document could not be independently inspected. The Source records do not preserve a separate publication number, author, date or local copy that would resolve this ambiguity.

### Linked Claims and independent-source check

The duplicate FEMA page is used in the following Evidence Use records:

- `EU-INFRASTRUCTURE_RESILIENCE-A-2` → `CLM-INFRASTRUCTURE_RESILIENCE-A`
- `EU-INFRASTRUCTURE_RESILIENCE-B-2` → `CLM-INFRASTRUCTURE_RESILIENCE-B`
- `EU-INFRASTRUCTURE_RESILIENCE-C-2` → `CLM-INFRASTRUCTURE_RESILIENCE-C`
- `EU-INFRASTRUCTURE_RESILIENCE-D` → `CLM-INFRASTRUCTURE_RESILIENCE-D`
- `EU-M4-INFRASTRUCTURE-DEPENDENCY-FEMA` → `CLM-INFRASTRUCTURE_BASICS-C`
- `EU-M4-INFRASTRUCTURE-DEPENDENCY-FEMA` is a separate link to `CLM-M4-INFRASTRUCTURE-DEPENDENCY-A` only through its own record `EU-CLM-M4-INFRASTRUCTURE-DEPENDENCY-A`; preserve the exact record-to-Claim reference during any correction.

The NIST Community Resilience Program page, Source `SRC-INFRASTRUCTURE_RESILIENCE`, is a distinct source and was independently inspected. It directly states that community resilience includes preparation, adaptation, withstanding disruption and recovery within a specified time frame; it describes cascading effects, interdependencies between infrastructure and social/economic systems, and functional recovery requirements. It therefore provides independent institutional support for Claims A, B and C, whose Evidence Use records already link it.

The NIST Infrastructure overview, Source `SRC-INFRASTRUCTURE_BASICS`, is another distinct URL, but it mainly defines the breadth and societal role of infrastructure. It does not directly establish the specific dependency/reliability proposition in `CLM-INFRASTRUCTURE_BASICS-C`. Do not count this generic overview as independent corroboration for that Claim without a direct passage.

| Claim | Source-fit decision |
|---|---|
| `CLM-INFRASTRUCTURE_RESILIENCE-A` — community resilience includes preparation, adaptation, withstanding disruptions and recovery within a time frame | Directly supported by NIST Community Resilience Program page. FEMA duplicate IDs count as one additional source, not two. |
| `CLM-INFRASTRUCTURE_RESILIENCE-B` — infrastructure supports social/economic functions and dependencies can create cascading consequences | Directly supported by NIST Community Resilience Program page, which describes cascading impacts and interconnected physical, social and economic systems. FEMA page remains an additional candidate but was not directly retrievable in this review. |
| `CLM-INFRASTRUCTURE_RESILIENCE-C` — resilience planning uses functional/recovery goals, not only asset properties | Directly supported by NIST Community Resilience Program page, including specified recovery periods and functional recovery criteria. |
| `CLM-INFRASTRUCTURE_RESILIENCE-D` — resilience assessment accounts for cross-sector dependencies and how failures/recovery affect other community functions | NIST Community Resilience Program content is relevant, but no NIST Evidence Use is currently linked to this Claim. Current linked evidence is the FEMA page only; mark as single-source pending a valid, pinpointed FEMA passage or an authorized new NIST Evidence Use. |
| `CLM-INFRASTRUCTURE_BASICS-C` — infrastructure reliability depends on interconnections, not only individual assets | FEMA page is the direct linked candidate. The linked NIST Infrastructure overview is too broad to establish the dependency mechanism. Current independent corroboration is not demonstrated by the linked NIST page. |
| `CLM-M4-INFRASTRUCTURE-DEPENDENCY-A` — failures can transmit consequences across interconnected systems | One linked FEMA Source ID only. The duplicated FEMA ID does not add a second source. NIST Community Resilience Program may be a suitable additional source, but it is not currently linked to this Claim. |

### Disposition

- Two FEMA Source IDs = one FEMA URL/page identity; no independent corroboration between them.
- The “additional independent corroboration” descriptions on the FEMA EUs are valid only in relation to the separately linked NIST Community Resilience Program source for Claims A/B/C. They must not be interpreted as two independent FEMA sources.
- FEMA direct content verification remains blocked by HTTP 403. Resolve the exact document identity and passage before treating it as fully adjudicated.
- Do not automatically add NIST EUs to Claims D or M4 dependency A; that requires an authorized, versioned change.

## 4. OSHA Process Safety Management — two IDs, one overview page

### Source identity

Both records point to `https://www.osha.gov/process-safety-management`:

- `SRC-INDUSTRIAL_SAFETY_BASICS`
- `SRC_INDUSTRIAL_PROCESS_SAFETY_BASICS`

Both identify the same OSHA Process Safety Management overview. The page is retrievable and states that OSHA’s PSM standard (29 CFR 1910.119) manages hazards associated with processes involving highly hazardous chemicals and integrates technologies, procedures and management practices.

The page links the actual **29 CFR 1910.119, Process safety management of highly hazardous chemicals**. That regulation is a separate, more precise authoritative source and contains the relevant elements, including process safety information, process hazard analysis, operating procedures, training, mechanical integrity and management of change.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-INDUSTRIAL_SAFETY_BASICS-A` — industrial safety includes systematic management of hazards from processes and equipment | Partial. OSHA PSM is specifically about hazards from processes involving highly hazardous chemicals; it does not define all industrial safety or all equipment hazards. Narrow to process safety for covered chemical processes or add broader occupational-safety evidence. |
| `CLM-INDUSTRIAL_SAFETY_BASICS-B` — process approach integrates technical information, procedures and management practices | Direct for OSHA PSM. The overview expressly says the program integrates technologies, procedures and management practices. |
| `CLM-INDUSTRIAL_SAFETY_BASICS-C` — safety requirements depend on jurisdiction, industry, process and applicable standards | Partial-to-direct within the US OSHA context. The page points to general-industry and construction standards; it cannot establish requirements in other jurisdictions. Explicitly bound the Claim to applicable jurisdictional/industry rules. |
| `CLM-INDUSTRIAL_PROCESS_SAFETY_BASICS-A` — process safety addresses hazards involving highly hazardous chemicals and industrial processes | Direct. The OSHA overview and 29 CFR 1910.119 Purpose and Application provisions establish this scope. |
| `CLM-INDUSTRIAL_PROCESS_SAFETY_BASICS-B` — PSM uses organized procedures and controls to prevent/limit catastrophic releases and related incidents | Direct. 29 CFR 1910.119 Purpose, §(d) process safety information, §(e) process hazard analysis and §(f) operating procedures provide the precise basis. |
| `CLM-INDUSTRIAL_PROCESS_SAFETY_BASICS-C` — process safety depends on hazard information, procedures, equipment integrity, training and management of change | Direct. Pinpoint 29 CFR 1910.119 §§(d), (e), (f), (g), (j) and (l), respectively. |

### Disposition

- Two Source IDs, one OSHA overview-page identity; they do not independently corroborate each other.
- Add 29 CFR 1910.119 as a separate Source record if authorized. Use the standard’s actual section/subsection locators for the process-safety Claims.
- Keep general industrial safety distinct from process safety management for covered highly hazardous chemical processes.

## 5. WHO Sexual and Reproductive Health and Rights — two IDs, one topic page

### Source identity

Both records point to `https://www.who.int/health-topics/sexual-and-reproductive-health-and-rights`:

- `SRC_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES`
- `SRC_WHO_SRH_FACTS_2026`

They identify the same WHO topic page. The current page is retrievable. It defines sexual and reproductive health as a broad range of services, including contraception, fertility/infertility care, maternal and perinatal health, STI prevention and treatment, and education on safe and healthy relationships. It describes complete physical, mental and social well-being in matters relating to the reproductive system and says services should be available throughout people's lives.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A` — SRH covers contraception, fertility, pregnancy, birth and STIs | Direct. The WHO overview explicitly lists contraception, fertility/infertility care, maternal/perinatal health and STI prevention/treatment. |
| `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_B` — reproductive health spans the life course and includes physical, mental and social aspects | Direct. The WHO definition explicitly covers complete physical, mental and social well-being and states that access should be available throughout life. |
| `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_C` — general information does not replace individual medical assessment and recommendations depend on personal situation, country and current guidance | Not directly supported by the topic page. The page gives a high-level overview and policy recommendations, not an individual clinical disclaimer or country-specific treatment rule. Add a source that explicitly supports the clinical boundary, or reclassify the sentence as an editorial safety limitation rather than a documented factual Claim through an authorized process. |

### Disposition

- Two Source IDs = one WHO topic page; no independent corroboration.
- The page is appropriate for Claims A and B with exact overview locators.
- Claim C is a prudent limitation but is not evidenced by the current page. It should not be marked as source-supported merely because WHO is the issuer.

## 6. Consolidated audit decision and next actions

1. Count one source identity per shared URL: EPA municipal wastewater = 1; FEMA infrastructure dependency = 1; OSHA PSM = 1; WHO SRHR = 1.
2. Keep all 21 linked Claims in the denominator. Do not merge Source IDs or Evidence Use records solely because their URLs match.
3. Distinguish a landing page from a linked publication or legal standard:
   - EPA Primer for Municipal Wastewater Treatment Systems is a distinct publication linked by the EPA page.
   - OSHA 29 CFR 1910.119 is a distinct legal standard linked by the OSHA overview.
4. Preserve actual independence:
   - NIST Community Resilience Program is a separate source from FEMA and already supports resilience Claims A/B/C.
   - Duplicate FEMA IDs are one FEMA source, not two.
   - Generic NIST Infrastructure page is not enough to support infrastructure interdependency claims without a relevant passage.
5. Prioritize source remediation for the unsupported or partial Claims, especially wastewater design generalizations, general industrial safety scope, the FEMA-only infrastructure Claims, and the WHO clinical-boundary statement.
6. Any canonical corrections require bounded authorization and a new versioned record; run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA after authorized changes.

## 7. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records inspected source identity, evidence scope and source fit. It is not a release approval or authorization to edit canonical records.
