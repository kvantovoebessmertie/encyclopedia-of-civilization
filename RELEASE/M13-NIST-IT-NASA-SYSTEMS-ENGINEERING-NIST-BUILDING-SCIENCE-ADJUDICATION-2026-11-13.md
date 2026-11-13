# M13 duplicate-source adjudication: NIST IT, NASA Systems Engineering, and NIST Building Science

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `bb013a26b7ed44e37982ddd6ebec484e039b1bd1`  
Scope: three shared-URI groups from the 33-group duplicate-source inventory. Source, Evidence Use and Claim records were inspected directly; public source pages were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| NIST Information Technology Laboratory | 6 | 18 | One broad institutional landing page reused as if it were six topic-specific sources; it does not substantiate the linked technical propositions at the recorded locator. |
| NASA Systems Engineering Handbook | 4 | 12 | One identifiable handbook reused across four slices. It is a relevant source for several Claims, but each Evidence Use needs a section-level locator and some Claims need narrower scope or another source. |
| NIST Building Science | 3 | 9 | All three IDs point to the same NIST URL, which currently returns 404. The former shared page cannot be treated as a currently retrievable source. Specific NIST publications provide partial replacement candidates. |

**Totals: 13 Source records, 39 linked Claims, three URI groups.** Repeated Source IDs do not create independent corroboration. Preserve all Source IDs and Evidence Use records until a separately authorized, versioned remediation is approved.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This is a source-fit adjudication report only.

## 2. NIST Information Technology Laboratory — six IDs, one broad page

### Source identity

The following six Source records all resolve to the exact same URI, `https://www.nist.gov/itl`:

- `SRC-COMPUTER_ARCHITECTURE_BASICS`
- `SRC-DATABASES_BASICS`
- `SRC-DISTRIBUTED_SYSTEMS_BASICS`
- `SRC-PROGRAMMING_LANGUAGES_BASICS`
- `SRC-SOFTWARE_ENGINEERING_BASICS`
- `SRC_DATA_GOVERNANCE_BASICS`

The first five Source identity fields are subject-description sentences, not bibliographic titles. The sixth says “NIST — Information technology”. All six records represent one NIST ITL landing page, not six publications and not six independent sources.

The live NIST page identifies itself as the **Information Technology Laboratory** and describes the laboratory's mission, research domains and institutional role. Its current page navigation points to topic areas such as cloud computing, complex systems, data and informatics, networking and software research. The page does not itself provide the definitions or technical explanations asserted by the linked Claims. The separate NIST “Information technology” topic page is also an overview/index, not a substitute for claim-specific technical references.

### Claim/Evidence Use review

All 18 Evidence Use records use generic descriptions and contain no section, page, standard clause, report number or other reproducible pinpoint.

| Slice / Claim IDs | Claim subject | Source-fit decision |
|---|---|---|
| `computer-architecture-basics`: `CLM-COMPUTER_ARCHITECTURE_BASICS-A/B/C` | Processor, memory vs storage, architecture and component interaction | NIST ITL landing page does not directly establish any of the three propositions. Replace or augment with a computer-architecture textbook or recognized technical standard; select pinpoint sections for processor instruction execution, memory hierarchy and architecture. |
| `databases-basics`: `CLM-DATABASES_BASICS-A/B/C` | Database definition, schema and queries | NIST ITL landing page does not explain database organization, schemas or query semantics. Use a database textbook or standards-based technical reference and identify the relevant chapters/sections. |
| `distributed-systems-basics`: `CLM-DISTRIBUTED_SYSTEMS_BASICS-A/B/C` | Networked components, latency/partial failure, consistency/availability | NIST ITL landing page is not direct support. A general distributed-systems reference is needed for the failure model and consistency/availability propositions; do not substitute a generic NIST cloud or IT overview without checking its scope. |
| `programming-languages-basics`: `CLM-PROGRAMMING_LANGUAGES_BASICS-A/B/C` | Syntax/semantics, interpretation/translation, computational models and abstraction | NIST ITL landing page does not establish these language concepts. Use a programming-languages or compiler textbook/standard with exact section locators. |
| `software-engineering-basics`: `CLM-SOFTWARE_ENGINEERING_BASICS-A/B/C` | Lifecycle activities, testing evidence, retesting after change | NIST ITL landing page does not describe the software-engineering lifecycle or testing claims. A recognized software-engineering body of knowledge, standard or textbook is required. |
| `data-governance-basics`: `CLM_DATA_GOVERNANCE_BASICS_A/B/C` | Roles/responsibilities, quality/access/security/privacy/lifecycle, policy-to-practice | NIST ITL landing page does not define organizational data governance or substantiate the listed governance domains. Consider a dedicated data-governance framework/standard; NIST privacy and cybersecurity frameworks may support only their respective privacy/security portions, not the entire governance proposition. |

### Disposition

- One shared NIST ITL institutional page; six Source IDs are not six sources.
- All 18 Claim/Evidence Use chains remain **source-fit HOLD** pending claim-specific source selection and exact locators.
- Do not describe these as six independent NIST confirmations.
- Do not simply replace `/itl` with the newer NIST `/information-technology` topic overview: it is still a directory/overview and does not solve the Claim-level evidence gap.

## 3. NASA Systems Engineering Handbook — four IDs, one handbook

### Source identity

The following four Source records use the exact same URI, `https://www.nasa.gov/reference/systems-engineering-handbook/`, and identify the same publication, **NASA Systems Engineering Handbook**:

- `SRC-DECISION_ANALYSIS_BASICS`
- `SRC-OPERATIONS_MANAGEMENT_BASICS`
- `SRC-SYSTEMS_ENGINEERING_BASICS`
- `SRC-SYSTEMS_MODELING_BASICS`

This is one handbook, not four independent publications. Unlike the NIST ITL group, it is a specific handbook with a navigable chapter structure. The current NASA page exposes sections 1.0–6.0 and an appendix. The source can support several claims when the relevant section is identified; the root URL alone is not an adequate locator.

### Claim-specific source fit and locator proposals

| Claim | Assessment and proposed pinpoint |
|---|---|
| `CLM-DECISION_ANALYSIS_BASICS-A` — compare alternatives by criteria and consequences | Directly aligned with NASA SEH §6.8.1–§6.8.1.2.1: decision context, criteria, alternatives, uncertainty and evaluation. Scope must remain systems-engineering/project decision analysis. |
| `CLM-DECISION_ANALYSIS_BASICS-B` — goals, constraints, uncertainty and consequences | Directly aligned with §6.8.1.1–§6.8.1.2.1, including technical/cost/schedule inputs, objectives/constraints, uncertainty, risk and criteria. Add the precise section locator. |
| `CLM-DECISION_ANALYSIS_BASICS-C` — trade studies compare options and tradeoffs against requirements | Directly aligned with §4.4 Design Solution Definition and §6.8.1.2.3; the handbook describes trade studies and alternative selection. Add both pinpoint sections. |
| `CLM-OPERATIONS_MANAGEMENT_BASICS-A` — goals, processes, resources and constraints across a lifecycle | Partial support only. §3.0 and especially §3.8 cover NASA project/system operations and sustainment; they do not establish a general operations-management discipline. Narrow the Claim to systems operations/sustainment in a NASA project context or add a dedicated operations-management source. |
| `CLM-OPERATIONS_MANAGEMENT_BASICS-B` — stakeholders, technical limits, risks and evidence in operational decisions | Partial support. §6.8.1.1–§6.8.1.2.1 covers decision context, stakeholders, technical/cost/schedule factors, risk, evidence and criteria. The current Claim's broad “operations” framing should be bounded to technical/project decisions. |
| `CLM-OPERATIONS_MANAGEMENT_BASICS-C` — efficiency cannot be assessed with one metric alone | Partial support. §2.5 discusses cost-effectiveness and tradeoffs among performance, cost, schedule and risk. The source supports a multi-attribute systems-engineering evaluation, not a universal operations-management rule. Narrow scope accordingly or add a broader operations source. |
| `CLM-SYSTEMS_ENGINEERING_BASICS-A` — interdisciplinary approach across design, realization, management, operations and retirement | Direct support. NASA SEH §2.0 defines systems engineering as a methodical multidisciplinary approach spanning design, realization, technical management, operations and retirement. |
| `CLM-SYSTEMS_ENGINEERING_BASICS-B` — systems engineering spans the lifecycle, not design alone | Direct support. Use §2.0 and the lifecycle treatment in §3.0, including §3.8 Operations and Sustainment and §3.9 Closeout. |
| `CLM-SYSTEMS_ENGINEERING_BASICS-C` — verification and validation are distinct technical processes | Direct support. NASA SEH §2.4 explicitly distinguishes verification against requirements from validation against intended purpose/use environment. |
| `CLM-SYSTEMS_MODELING_BASICS-A` — modeling represents elements, relationships and behavior at a selected abstraction | Partial support. §2.3 describes iterative modeling, mock-ups and simulation; §4.3 discusses logical decomposition models. The current Claim's definition of a model as a selective representation needs a modeling-specific source or a more exact passage. |
| `CLM-SYSTEMS_MODELING_BASICS-B` — a model represents selected aspects, not the entire system | Not directly established by the reviewed SEH passages. Add a dedicated modeling reference and pinpoint the definition/limitations of a model; do not infer this from a general handbook mention of modeling. |
| `CLM-SYSTEMS_MODELING_BASICS-C` — modeling supports requirements, interactions, alternatives and consequences under assumptions | Partial support. NASA SEH §§2.3 and 4.3 cover models and system relationships; §§4.4 and 6.8 cover trade studies and decision analysis. A more direct companion source is **NASA Systems Modeling Handbook for Systems Engineering**, NASA-HDBK-1009, which specifically covers integrating SysML modeling with NASA SE processes and work products. Verify the exact relevant section before adding a canonical locator. |

### Disposition

- One NASA handbook identity across four Source IDs; no independent corroboration is created by the duplicate IDs.
- The handbook is a relevant source for decision analysis and systems engineering, but not a universal authority for generic operations management or all systems-modeling definitions.
- The 12 Evidence Use records remain unpinned. The section references above are proposals for a bounded, versioned locator correction, not canonical edits.
- For systems modeling, inspect NASA-HDBK-1009 as a distinct source candidate; do not conflate it with the Systems Engineering Handbook.

## 4. NIST Building Science — three IDs, one currently unavailable URL

### Source identity and availability

The following Source records all point to `https://www.nist.gov/building-science`:

- `SRC-BUILDING_ENVELOPE_BASICS`
- `SRC-CONSTRUCTION_BASICS`
- `SRC_BUILDING_SCIENCE_BASICS`

They are three identifiers for one NIST Building Science landing-page URL. At the time of this review, the URL returned **HTTP 404**. The shared page is therefore not currently retrievable as recorded. A Source identity label alone does not establish which NIST publication or passage was intended.

### Specific NIST publications inspected

Two distinct, retrievable NIST publications provide useful but bounded candidates:

1. **NIST Technical Note 1869, _Research and Development Opportunities for the NIST Net Zero Energy Residential Test Facility_** (March 2015), especially §2.1 (climate, site, form and orientation), §3.1.1 (building enclosure design), §3.1.2 (enclosure airtightness), and the HVAC/ventilation sections in §3.2. Section 3.1.1 discusses water, airflow, vapor and thermal control layers, continuity, materials, connections, durability and heat transfer.
2. **Persily and Emmerich, _Effect of Air Infiltration and Ventilation_** (NIST publication, 2009). Its abstract addresses infiltration/ventilation, moisture transport, driving forces, envelope airtightness and measurement, mechanical ventilation and interzone airflow.

These are separate publications, not merely corrected URLs for the old landing page. They must be added as new, bibliographically identified Source records if authorized; they must not be silently substituted under the existing IDs.

### Claim-specific source fit

| Slice / Claim IDs | Assessment and proposed remediation |
|---|---|
| `building-envelope-basics`: `CLM-BUILDING_ENVELOPE_BASICS-A` | TN 1869 §3.1.1 directly supports the role of the enclosure and its water, airflow, vapor and thermal control layers. Use this specific report and section locator. |
| `building-envelope-basics`: `CLM-BUILDING_ENVELOPE_BASICS-B` | TN 1869 §§3.1.1–3.1.2 and the NIST 2009 infiltration/ventilation publication provide direct support for airflow, moisture transport, airtightness and durability. Two distinct NIST publications may be cited, but they are not independent merely because they share an institutional publisher. |
| `building-envelope-basics`: `CLM-BUILDING_ENVELOPE_BASICS-C` | TN 1869 §§2.1 and 3.1.1 provide partial support for climate/site and material/connection dependence in the studied residential facility. The Claim generalizes beyond that case; either narrow it or add broader evidence for climate/material/workmanship effects. |
| `construction-basics`: `CLM-CONSTRUCTION_BASICS-A` | TN 1869 abstract and §3 cover interactions among enclosure, conditioning, electrical systems and appliances in a particular residential test facility. Partial support only for the broad construction-science proposition; a broader building-science source is needed. |
| `construction-basics`: `CLM-CONSTRUCTION_BASICS-B` | TN 1869 §3.1.1 supports the importance of continuous control layers and component connections for enclosure performance/durability. It does not establish the full generalization about structural safety, loads and all material combinations. Add a suitable structural/materials source or narrow the Claim. |
| `construction-basics`: `CLM-CONSTRUCTION_BASICS-C` | The warning that general information cannot replace calculations, applicable codes and qualified review is prudent, but the recorded NIST landing page and TN 1869 do not directly establish this professional/safety boundary. Add applicable primary building-code/engineering guidance and jurisdiction context; do not treat this as supported by the current NIST source. |
| `building-science-basics`: `CLM_BUILDING_SCIENCE_BASICS_A` | TN 1869 provides examples of building systems, materials, energy, HVAC and environment, but does not fully define building science across people, materials, energy, moisture and outdoor environment. Partial support; use a dedicated building-science reference. |
| `building-science-basics`: `CLM_BUILDING_SCIENCE_BASICS_B` | TN 1869 §3.1.1 and the 2009 infiltration/ventilation publication support heat/air/moisture effects on performance and durability. Use exact sections and preserve the limited building-envelope scope. |
| `building-science-basics`: `CLM_BUILDING_SCIENCE_BASICS_C` | TN 1869 abstract and §§2.1, 3.1 and 3.2 provide partial evidence for interactions among enclosure, mechanical systems, materials and climate in one test-facility context. Occupancy and general building-performance claims need additional support. |

### Disposition

- The three Source IDs point to one URL, and that URL currently returns 404.
- TN 1869 and the 2009 NIST infiltration/ventilation publication are separate, retrievable candidates with narrower scopes.
- All nine linked Claims remain source-fit HOLD until a valid Source record and claim-specific locator are added through authorized versioned changes.
- Do not represent the replacement candidates as the same publication as the unavailable landing page.

## 5. Consolidated audit decision and next actions

1. Count each shared URI as one source identity for independence analysis: NIST ITL = 1; NASA SEH = 1; NIST Building Science landing page = 1 unavailable URL.
2. Keep all 39 Claim/Evidence Use chains in the audit denominator. Do not delete or merge Source IDs or Evidence Use records on the basis of URL equality.
3. Prepare separate bounded correction proposals:
   - NIST IT: replace broad landing-page support with topic-appropriate publications/standards for the 18 Claims.
   - NASA: add section-level locators for directly supported Claims, narrow the operations-management Claims, and inspect NASA-HDBK-1009 for systems modeling.
   - NIST Building Science: add bibliographically complete records for TN 1869 and the 2009 infiltration/ventilation publication; identify additional primary sources for the unsupported/generalized Claims.
4. Preserve the distinction between a relevant institution, a specific publication, a passage that supports a Claim, and an independent corroborating source.
5. Run exact-head Reference Tests, Release Conformance Gate and Offline Edition after any later authorized canonical correction. This report itself does not clear any Claim for publication.

## 6. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records inspected source identity, retrievability and Claim-level fit. It is not a release approval or an authorization to edit canonical records.
