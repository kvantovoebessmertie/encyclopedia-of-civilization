# M13 — bounded remediation routing for Content Screen Packages 29–31

Date: 2026-11-15
Branch: m13-system-wide-depth-audit-2026-10-09
Baseline HEAD: 8fac92a2d951a29f721e0e02d394f1e199c4246d

## 1. Purpose and status

This is a noncanonical consolidation of actionable findings in Packages 29, 30 and 31. It is a routing and source-candidate proposal only.

No canonical Claim, Evidence Use, Source, Context, Scope, Relation, provenance or D/E/B field is changed or authorized. No Claim is promoted from UNASSESSED/HOLD. No rights clearance, specialist approval, Human View approval, publication or release decision is made.

## 2. Package integrity and arithmetic control

| Package | Claims screened | Direct stated | Partial/HOLD stated | Provenance exceptions |
|---|---:|---:|---:|---:|
| 29 | 20 | 14 | 6 | 0 |
| 30 | 20 | 15 | 5 | 2 |
| 31 | 12 | 3 in summary | 9 in summary | 2 |

**Package 31 arithmetic defect:** its table marks four Claims as direct conceptual support: Maps A, Maps B, Risk Management C (COSO only), and Statistics B. The summary and decision section say three direct and nine partial. Four direct plus eight partial equals 12. Correct the summary in a noncanonical erratum after checking the original evidence table. Do not silently reuse the inconsistent aggregate.

Packages 29–31 screen 52 Claims. These outcomes are not D/E/B scores and do not close M13.

## 3. Package 29 — remediation routing

### Partial support / additional source required

| Claim | Finding | Bounded next action |
|---|---|---|
| CLM-GEOPHYSICS_BASICS-C | USGS glossary supports separate methods, not the combined surface/remote/model workflow | Add a dedicated USGS geophysical mapping/survey method source and pinpoint the combined workflow. |
| CLM-HUMAN_COMPUTER_INTERACTION_BASICS-A | Existing NIST HCD page is outdated and only conceptually supports part of the interface definition | Existing HCI authorization leaves A on HOLD. Find a current, direct HCI interface source; separate authorization required before new Source/EU writes. |
| CLM-HUMAN_COMPUTER_INTERACTION_BASICS-B | Existing page supports user/context framing but not all Claim factors | Find a current usability/context-of-use source; verify rights and exact locator. Existing HCI authorization does not permit Claim wording changes. |
| CLM-HUMAN_COMPUTER_INTERACTION_BASICS-C | Existing page supports user-centred evaluation, not a universal observable-task protocol | Find a current usability-testing source; distinguish general principles from prescribed protocol. |
| CLM-INDUSTRIAL_ENGINEERING_BASICS-C | IISE source supports integrated systems but not local optimisation versus system-level interactions | Add a systems-engineering source explicitly discussing interactions, trade-offs and local versus system-level performance. |
| CLM-INFORMATION_ETHICS_BASICS-C | IFLA code does not establish reliability/evidential value merely from availability | Add ACRL Framework, “Authority Is Constructed and Contextual”, and its source-credibility knowledge practices. The current ACRL page notes a 2026 revision and CC BY-NC-SA 4.0 licence; preserve non-commercial/share-alike conditions. |

### Direct conceptual support — locator/source repair still required

- CLM-GEOPHYSICS_BASICS-B: pinpoint exact USGS glossary entries; retain individual-method scope.
- CLM-GOVERNANCE_BASICS-A: pinpoint OECD Policy Framework Part I and Part II.
- CLM-GRAPH_THEORY_BASICS-A/B: pinpoint MIT OCW Chapter 5; add Chapter 6 as a separate Source if full digraph treatment is needed.
- CLM-GROUNDWATER_BASICS-B/C: pinpoint USGS aquifer, replenishment, distribution and quality passages; retain local geological conditions.
- CLM-HEAT_TRANSFER_BASICS-A/B: pinpoint DOE Building Science Education definition and three modes; do not generalize to complete thermodynamics.
- CLM-HUMAN_FACTORS_BASICS-B/C: pinpoint NASA JSC sections; retain spaceflight/mission-system scope.
- CLM-INDUSTRIAL_ENGINEERING_BASICS-A/B: pinpoint IISE definition; preserve draft Body of Knowledge status.
- CLM-INFORMATION_ETHICS_BASICS-B: repair IFLA Source locator to official repository/PDF and pinpoint Code sections 1, 3 and 4; rights review remains separate.
- CLM-INFORMATION_THEORY_BASICS-A: pinpoint MIT OCW course description and exact entropy/encoding notes.

## 4. Package 30 — remediation routing

### Partial support / additional source required

| Claim | Finding | Bounded next action |
|---|---|---|
| CLM-INSURANCE_BASICS-C | OECD page does not establish contract-specific coverage/exclusions | Add NAIC consumer explanation that insurance is a policy contract covering specified events; preserve U.S. consumer scope. Actual policy wording remains controlling. |
| CLM-LABOR_ECONOMICS_BASICS-B | Broad ILO/World Bank hubs do not establish worker income and employer labour cost | Add ILOSTAT distinction between employee earnings and employer labour costs. Do not equate wages with total labour cost. |
| CLM-LABOR_ECONOMICS_BASICS-C | Hubs do not establish the full indicator set | Add ILOSTAT definitions for earnings, hours and labour underutilisation; add productivity only with its own defined measure and scope. |
| CLM-LOGISTICS_BASICS-A | World Bank LPI is a performance index, not a full definition of logistics operations | Add CSCMP definition covering flow/storage, transport, warehousing, materials handling, fulfilment and inventory. Keep LPI for performance measurement only. |
| CLM-MANUFACTURING_SYSTEMS_BASICS-A | NIST Manufacturing hub is not itself an integrated-system definition | Add NIST Manufacturing Operations glossary and/or systems-design source; pinpoint the system boundary. |

### Direct conceptual support — locator/source repair still required

- CLM-INFORMATION_THEORY_BASICS-B/C: pinpoint MIT OCW entropy, source coding, channel coding and capacity materials; preserve assumptions.
- CLM-INFRASTRUCTURE_BASICS-A: pinpoint NIST “What is Infrastructure?”; retain physical and organizational scope.
- CLM-INTERNATIONAL_TRADE_BASICS-B: pinpoint WTO “What is the WTO?”; separately correct EU provenance through a bounded authorization.
- CLM-LABOR_LAW_BASICS-B: pinpoint ILO instruments, ratification and supervision; separately correct EU provenance. Do not infer national legal effect without jurisdictional review.
- CLM-LABOR_MARKETS_BASICS-A: pinpoint BLS CPS overview/design; preserve U.S. statistical-system scope.
- CLM-LEARNING_BASICS-A/B/C: pinpoint NIMH program overview; retain research-program context.
- CLM-MAINTENANCE_ENGINEERING_BASICS-A/B/C: pinpoint NASA RCM selection logic and feedback; retain NASA facilities/operations scope.
- CLM-M5-MANUFACTURING-FUNCTIONS-D: pinpoint UNIDO functions/integration discussion.
- CLM-MANUFACTURING_BASICS-A/C: pinpoint NIST glossary and UNIDO overview; distinguish operational definition from Industry 4.0 framing.

## 5. Package 31 — remediation routing

### Partial support / rights hold

| Claim | Finding | Bounded next action |
|---|---|---|
| CLM-MANUFACTURING_SYSTEMS_BASICS-B | NIST hub does not directly establish reproducibility, quality and efficiency improvement | Add NIST process measurement/control or Smart Manufacturing Systems Test Bed report; pinpoint data collection and system-performance passages. |
| CLM-MANUFACTURING_SYSTEMS_BASICS-C | NIST hub does not establish digital operations/monitoring/analysis integration | Add NIST Systems Analysis Integration for Smart Manufacturing Operations and/or AMS 200-2; pinpoint model integration. |
| CLM-MAPS_AND_NAVIGATION_BASICS-C | USGS fact sheet does not establish map quality, currency, accuracy and terrain verification | Add USGS US Topo accuracy FAQ and topographic mapping guidance. Preserve that US Topo is general reference and not authoritative for navigation or regulation. |
| CLM-MATERIALS_BASICS-A | Registered NIST Metallurgy page is opaque/unreadable | Replace reliance on the landing page with a specific authoritative materials-science source; exact passage and rights review required. |
| CLM-MATERIALS_BASICS-C | NSF overview does not establish composition/structure/processing/operating-condition formulation | Add a specific National Academies materials science source; distinguish composition, structure, processing, properties and application conditions. |
| CLM-M5-MATERIALS-PERFORMANCE-D | NSF overview does not establish the full application-specific assessment framework | Add materials selection/performance or failure-analysis source covering service conditions, failure mechanisms and application data. |
| CLM-MATERIALS_SCIENCE_BASICS-B | NSF page omits composites in accessible text; other NIST URL returns 404 | Add authoritative materials classification source; clarify categories overlap and are not exhaustive. |
| CLM-RISK_MANAGEMENT_BASICS-B | ISO 31000 is on RIGHTS HOLD for this AI-assisted workflow | Do not use ISO content. Add a rights-compatible government source such as UK Orange Book or NIST CSRC glossary; preserve jurisdiction/source scope. |
| CLM-RISK_MANAGEMENT_BASICS-C | Direct support is COSO only; ISO must not be corroboration | Keep COSO-only evidence and pinpoint “Integrating with Strategy and Performance”. Scope to enterprise risk management. |

### Direct conceptual support — locator repair

- CLM-MAPS_AND_NAVIGATION_BASICS-A/B: pinpoint USGS topographic map and scale definitions.
- CLM-STATISTICS_BASICS-B: pinpoint NIST/SEMATECH sampling, sample-size and measurement-error sections.

## 6. Provenance-lineage correction queue

Four Evidence Use records have provenance.created_from pointing to their Claim while content.claim_ref and content.source_ref resolve:

| Evidence Use | Current created_from | Candidate intended lineage |
|---|---|---|
| EU-INTERNATIONAL_TRADE_BASICS-B@1 | CLM-INTERNATIONAL_TRADE_BASICS-B@1 | SRC-INTERNATIONAL_TRADE_BASICS@1 |
| EU-LABOR_LAW_BASICS-B@1 | CLM-LABOR_LAW_BASICS-B@1 | SRC-LABOR_LAW_BASICS@1 |
| EU-RISK_MANAGEMENT_BASICS-B@1 | CLM-RISK_MANAGEMENT_BASICS-B@1 | SRC-RISK_MANAGEMENT_BASICS@1 — rights-held; do not use as evidence |
| EU-RISK_MANAGEMENT_BASICS-C@1 | CLM-RISK_MANAGEMENT_BASICS-C@1 | Must resolve from this EU’s own content.source_ref; do not assume ISO or COSO |

Package 31 identifies two ISO Evidence Use lineage exceptions. Risk Management C also has a separate COSO Evidence Use. Do not conflate the two evidence paths. Re-fetch each EU and its Source at the current HEAD before proposing any change.

A separate bounded authorization is required for these exact EU records, with only provenance.created_from permitted to change. Preserve IDs, versions, content references, statuses and history. Correcting lineage does not clear ISO rights restrictions.

## 7. Source candidates checked for proposal purposes

These are candidates, not automatic approvals. Verify edition, exact passage, rights and fit before adding Source/Evidence Use records.

- NIST CSRC risk glossary: https://csrc.nist.gov/glossary/term/risk — includes “effect of uncertainty on objectives”; select and preserve the appropriate source context.
- UK HM Treasury, Orange Book: https://www.gov.uk/government/publications/orange-book/the-orange-book-management-of-risk-principles-and-concepts — government risk definition and principles; preserve UK public-sector context.
- ILOSTAT wages and working-time concepts: https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/ — distinguishes employee earnings from employer labour costs.
- ILO Thesaurus, labour cost: https://metadata.ilo.org/PoolParty/wiki/thesaurus?URI=https%3A%2F%2Fmetadata.ilo.org%2Fthesaurus%2F517432494&lang=en — employer cost includes remuneration, benefits and social-security expenditure.
- CSCMP logistics definitions: https://cscmp.org/CSCMP/CSCMP/Develop/Starting_Your_Career/Frequently_Asked_Questions.aspx — flow/storage and operational activities.
- NAIC, How Does Insurance Work?: https://content.naic.org/consumer/how-does-insurance-work — policy is a contract; coverage applies to specified events; U.S. consumer context.
- ACRL Framework: https://www.ala.org/acrl/standards/ilframework — authority/credibility/context; page notes 2026 revision and CC BY-NC-SA 4.0.
- NIST AMS 200-2: https://www.nist.gov/publications/connecting-deploying-and-using-smart-manufacturing-systems-test-bed — integration of manufacturing technologies and data collection/curation/reuse.
- NIST Systems Analysis Integration: https://www.nist.gov/programs-projects/systems-analysis-integration-smart-manufacturing-operations — integration of engineering-analysis models and smart-manufacturing system models.
- USGS US Topo accuracy FAQ: https://www.usgs.gov/faqs/how-accurate-are-us-topo-maps-and-why-dont-they-have-an-accuracy-statement — source-specific accuracy metadata and navigation limitations.
- USGS Topographic Mapping: https://www.usgs.gov/educational-resources/topographic-mapping — scale, control points and mapping accuracy.
- National Academies materials science chapter: https://www.nationalacademies.org/read/9784/chapter/13 — properties, performance in application conditions, structure/composition, synthesis/processing; classification includes composites.

## 8. Execution order

1. Correct Package 31’s noncanonical arithmetic inconsistency after checking the original evidence table.
2. Prepare and independently review a four-record provenance authorization; resolve each intended Source from its own EU content.source_ref.
3. Keep ISO evidence excluded; propose a rights-compatible source for Risk Management B; preserve COSO-only support for Risk Management C.
4. Prepare locator-only proposals for direct conceptual support cases before considering Claim wording changes.
5. Prepare source-addition proposals for partial cases using the candidates above and exact locators.
6. Keep HCI A/B/C on HOLD; the earlier HCI authorization is not expanded here.
7. Re-fetch canonical records at the then-current branch HEAD before every correction; compare versions and SHAs.
8. Create exact per-batch authorizations naming files and permitted fields. This routing document grants no canonical-write permission.
9. Run dedicated regressions, Reference Tests, Release Conformance Gate and Offline Edition on the same exact final HEAD after each authorized batch.
10. Independently inspect diff, branch base, PR state and unchanged main.

## 9. Disposition

- Packages 29–31 consolidated: 52 Claims.
- Partial/HOLD routing as reported: 6 + 5 + 9, with Package 31 arithmetic erratum outstanding.
- Provenance exceptions: 4 Evidence Use records.
- ISO 31000 remains excluded from AI-assisted evidence use pending qualifying permission/Open Data basis.
- Canonical writes: 0. D/E/B changes: 0. Rights/specialist/Human View/publication approvals: 0.

M13 remains OPEN / NOT RELEASE-READY. This routing artifact does not authorize canonical correction or publication.
