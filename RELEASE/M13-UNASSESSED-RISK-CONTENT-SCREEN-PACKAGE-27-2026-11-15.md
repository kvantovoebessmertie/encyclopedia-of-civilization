# M13 — Unassessed Risk Content Screen — Package 27

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `5952942d47bad14c946fb5d6b595ab2ce61be7fd`  
Queue workflow run: `43680814585`  
Queue artifact: `14148043133` (`m13-review-queue-5952942d47bad14c946fb5d6b595ab2ce61be7fd`)  
Artifact SHA-256: `ed915af7cf2b47cc665950f0e365ae88ac74eb4a208f377aff982663df1b9d4b`

## 1. Fresh queue and selection integrity

Package 27 is Lane 1 of the fresh queue generated after the Package 26 source-fit correction.

- 4,834 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows reconciled; 0 Claims without a scored-report match.
- 92 unassessed-risk candidates remained after exclusions.
- 617 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with reviewed holdouts; 619 unique exclusions across these sets.
- 92 Claims selected in five lanes: 20, 20, 20, 20 and 12. There are 8 unfilled slots because only 92 eligible candidates remained.
- Lane 1 contains 20 unique Claims and 22 Evidence Use links. Economic History Claims B and C each have a second independent-source Evidence Use.
- All selected Claim IDs are unique. Queue flags remain triage signals only; absence of a flag is not a low-risk finding.

## 2. Record-chain verification

The 20 selected Claim records, all 22 linked Evidence Use records and 12 referenced Source records were fetched from the exact queue-source revision. All 22 Evidence Use records are version 1, use `evidence_role=supports`, and their `claim_ref` and `source_ref` resolve to the expected version-1 records. Economic History B and C each have two separate Evidence Use links: one to Our World in Data and one to World Bank World Development Indicators.

The chain verification establishes reference integrity only. Many Evidence Use descriptions remain generic and omit exact passage/page/table locators. A valid record chain is not by itself a complete evidence argument.

### Provenance lineage exceptions

Four Evidence Use records in the Energy Markets and Energy Policy slices have a self-referential `provenance.created_from` entry pointing to their Claim rather than to the Source:
- `EU-ENERGY_MARKETS_BASICS-B`
- `EU-ENERGY_MARKETS_BASICS-C`
- `EU-ENERGY_POLICY_BASICS-B`
- `EU-ENERGY_POLICY_BASICS-C`

Their content `claim_ref` and `source_ref` fields resolve correctly, so the substantive links are identifiable. The provenance lineage is inconsistent and must be reconciled through the authorized versioned correction process; do not silently rewrite it.

## 3. Results

**8 Claims have direct conceptual support in the registered source material, subject to exact locator capture. 12 remain partial because the registered URI is a broad hub, the Claim exceeds the material actually registered, or a more specific source is needed.** These are source-fit findings only, not D/E/B scores or publication decisions.

| Claim ID | Existing Source | Result | Finding / required follow-up |
|---|---|---|---|
| `CLM-EARLY_AGRICULTURE-C` | FAO AGRIS / ICARDA, Harlan Symposium | DIRECT CONCEPTUAL SUPPORT | The AGRIS abstract identifies wheat, barley and lentils among the early crops domesticated in the Fertile Crescent. This supports the stated Southwest Asian example. Record the exact abstract locator and retain the regional and historical scope; do not generalize this list to all domestication centres. |
| `CLM-ECONOMETRICS_BASICS-A` | World Bank Staff Working Paper No. 302 (1978), *The Economic Theory of the Household and Impact Measurement of Nutrition and Related Health Programs* | DIRECT CONCEPTUAL SUPPORT — SOURCE IDENTITY CORRECTION NEEDED | Section IV, “An Econometric Approach,” explicitly describes econometrics as drawing on mathematics, statistics and economic theory to delineate economic relationships empirically. The registered Source identity is inaccurate: the PDF's actual title is the longer Working Paper title above; “An Econometric Approach” is the section title. Correct the bibliographic identity only through an authorized, versioned Source-record update and record section IV. |
| `CLM-ECONOMETRICS_BASICS-B` | Same World Bank Staff Working Paper No. 302 | DIRECT CONCEPTUAL SUPPORT — SOURCE IDENTITY CORRECTION NEEDED | Section IV explains that random, omitted, unidentified or inaccurately measured components are represented by a disturbance/error term. Record the exact section IV locator and correct the Source identity as described for Claim A. |
| `CLM-ECONOMETRICS_BASICS-C` | Same World Bank Staff Working Paper No. 302 | DIRECT CONCEPTUAL SUPPORT — SOURCE IDENTITY CORRECTION NEEDED | The introduction and section IV explain using econometrics to formulate/test hypotheses and estimate empirical relationships; section V compares econometric and experimental approaches to impact measurement. Record the introduction and section IV/V locators. Correct the Source identity as described for Claim A. |
| `CLM-ECONOMIC_GEOGRAPHY_BASICS-B` | World Bank, *World Development Report 2009* | PARTIAL — SOURCE PINPOINT HOLD | The Report's “density, distance and division” framework directly supports the conceptual dimensions in the Claim. The registered URI is only the WDR archive landing page, not the report or its relevant chapter. Add the exact 2009 report PDF/chapter as a specific Source and record the “three dimensions of development” locator. |
| `CLM-ECONOMIC_HISTORY-B` | Our World in Data, *Economic Growth*; World Bank, *World Development Indicators* | PARTIAL — DATA-SERIES PINPOINT HOLD | The Claim correctly identifies the importance of measurement method, price level and units when comparing historical indicators. The registered OWID page is a broad topic page and the WDI URI is a general table index. Add the exact historical GDP series and its metadata (constant prices, PPP/international-dollar basis, base year, geographic coverage) and identify the corresponding WDI series used for comparison. Do not count the two broad landing pages alone as proof of independent methodological corroboration. |
| `CLM-ECONOMIC_HISTORY-C` | Our World in Data, *Economic Growth*; World Bank, *World Development Indicators* | DIRECT CONCEPTUAL SUPPORT | OWID distinguishes economic growth from the full range of things people value and presents growth as an important but incomplete measure of living conditions. The registered OWID page supports the Claim's distinction. Record the definition and “growth does not reflect everything we value” locators; identify the exact WDI indicator if used as corroboration. |
| `CLM-EDUCATION_SYSTEMS-A` | UNESCO, *The Right to Education* | PARTIAL — WORDING/LEGAL SCOPE HOLD | UNESCO describes education as a human right and advocates lifelong-learning opportunities. However, UNESCO's separate discussion notes that lifelong learning is not an explicit standalone right under international human-rights law, although SDG 4 promotes lifelong-learning opportunities. The current Claim's phrase “lifelong learning as part of that right” overstates the legal position. Narrow the Claim to UNESCO's policy framework and distinguish the legally recognized right to education from the broader lifelong-learning agenda. |
| `CLM-ELECTORAL_SYSTEMS_BASICS-B` | International IDEA, *Electoral System Design: The New International IDEA Handbook* | DIRECT CONCEPTUAL SUPPORT | The handbook compares electoral-system families and their rules/consequences, including how votes are translated into seats. Record the relevant chapters on plurality/majority, proportional representation and mixed systems; do not imply that every system uses the same allocation formula. |
| `CLM-ELECTORAL_SYSTEMS_BASICS-C` | International IDEA, *Electoral System Design: The New International IDEA Handbook* | DIRECT CONCEPTUAL SUPPORT | The handbook explicitly says electoral-system design is contingent on the wider political and institutional framework and that design choices can have predicted and unforeseen effects. Record the overview and system-design advice chapters; preserve the country-specific context. |
| `CLM-ENERGY_EFFICIENCY_BASICS-A` | IEA, *Energy Efficiency* | PARTIAL — DEFINITION PINPOINT HOLD | The concept is consistent with the IEA definition: more services for the same energy input, or the same services for less energy input. The registered Source is a topic page; add the IEA glossary or a specific indicators/methodology publication as a versioned Source and record the exact definition. |
| `CLM-ENERGY_EFFICIENCY_BASICS-B` | IEA, *Energy Efficiency* | PARTIAL | The topic page is not a pinpoint source for the combined drivers listed in the Claim. IEA efficiency-indicator material distinguishes activity, structure and efficiency effects and gives sector-specific examples; add a specific decomposition/indicators source for technology, behaviour, buildings, equipment and demand structure. |
| `CLM-ENERGY_EFFICIENCY_BASICS-C` | IEA, *Energy Efficiency* | PARTIAL | The Claim's requirements for service, period and units are measurement-methodology propositions, not established by the registered topic hub. Add IEA energy-efficiency-indicator guidance that defines activity/service boundaries, numerator/denominator, units and reference period. |
| `CLM-ENERGY_MARKETS_BASICS-B` | U.S. EIA, *Energy Markets* | PARTIAL | The EIA topic hub does not itself establish the complete relationship among supply, demand, production, deliveries and infrastructure across energy carriers. Specific EIA natural-gas and electricity price explanations show that production/imports/storage, consumption infrastructure, weather and delivery constraints affect prices. Add the relevant carrier-specific Sources and avoid treating one market as universal. |
| `CLM-ENERGY_MARKETS_BASICS-C` | U.S. EIA, *Energy Markets* | PARTIAL | The broad hub does not establish that each energy carrier has distinct markets and physical constraints, or that one price indicator cannot represent the whole system. Add separate electricity, natural-gas, oil and (where in scope) coal market sources, including physical network/storage constraints and units; clarify that a price is a market-specific signal. |
| `CLM-ENERGY_POLICY_BASICS-B` | IEA, *Energy Policy* | PARTIAL — SPECIFIC SOURCE NEEDED | The Claim's security, affordability and environmental/sustainability dimensions are directly articulated in IEA World Energy Outlook 2024. The registered IEA topic page is broad; add the WEO chapter “Security, affordability and sustainability” as a specific Source and record its trade-off discussion. |
| `CLM-ENERGY_POLICY_BASICS-C` | IEA, *Energy Policy* | PARTIAL | The Claim's national-context and institutional caveat is plausible, but the registered topic hub does not establish it. Add a comparative energy-governance source showing how national resource endowments, energy-system structure, market design and institutional arrangements shape policy choices. |
| `CLM-ENTOMOLOGY_BASICS-A` | Entomological Society of America, *What Is Entomology?* | DIRECT CONCEPTUAL SUPPORT | The registered ESA page defines entomology as the study of insects and related animals and notes that professional usage often includes other arthropods such as spiders, ticks, centipedes and millipedes. Record the opening definition and preserve the distinction between insects and related arthropods. |
| `CLM-ENVIRONMENTAL_ECONOMICS_BASICS-A` | World Bank, *Environment* | PARTIAL | The registered World Bank topic hub is too broad to establish the field's conceptual scope. Add a specific environmental-economics source defining the interaction between economic activity, environmental impacts and policy evaluation. |
| `CLM-ENVIRONMENTAL_ECONOMICS_BASICS-B` | World Bank, *Environment* | PARTIAL — EXTERNALITY SOURCE NEEDED | The Claim is an externalities proposition: environmental costs/benefits may fall on parties other than the decision-maker, so private costs/benefits differ from social costs/benefits. The registered World Bank environment hub does not establish this. Candidate: IMF “Externalities: Prices Do Not Capture All Costs” or a specific World Bank externalities/public-policy source; add the exact source and locator. |

## 4. Cross-record, source and scope findings

1. The 22 Evidence Use records resolve to the intended Claim and Source IDs at version 1. Economic History B and C each have two separate Evidence Use links to Our World in Data and World Bank WDI.
2. Four Evidence Use records in Energy Markets B/C and Energy Policy B/C have self-referential Claim entries in `provenance.created_from`, while their content Claim/Source refs resolve. This is a provenance-lineage defect.
3. `SRC-ECONOMETRICS_BASICS` has an inaccurate bibliographic identity. Its URI resolves to World Bank Staff Working Paper No. 302, Dov Chernichovsky (October 1978), *The Economic Theory of the Household and Impact Measurement of Nutrition and Related Health Programs*. “An Econometric Approach” is Section IV, not the document title. Preserve the useful evidence but repair the Source identity only through an authorized, versioned update.
4. `SRC-ECONOMIC_GEOGRAPHY_BASICS` points to the World Bank's WDR archive rather than the 2009 report itself. Add the specific report and exact chapter/section locator.
5. `SRC-ECONOMIC_HISTORY` and `SRC-ECONOMIC_HISTORY-INDEPENDENT` are two different institutions, but their registered URIs are broad pages. Their independence as organizations does not make their current generic landing pages sufficient evidence. Pin the exact series/indicator and metadata used.
6. The UNESCO Claim must distinguish the recognized right to education from lifelong-learning opportunities and policy commitments; do not turn a policy framing into a stronger claim about the content of international human-rights law.
7. IEA, EIA and World Bank source URIs for energy and environmental economics are topic hubs. The required child publications/definitions must be added as specific Source records before the relevant Claims are treated as fully supported.
8. The FAO AGRIS source is a bibliographic abstract. It directly supports the named crops in the Fertile Crescent/Southwest Asian context, not a universal account of all early domestication centres.
8. Legacy `publication_status=published` and `completion_status=complete` fields are distinct from M13 risk status. All 20 Claims remain `UNASSESSED`; no publication authorization is inferred.

## 5. Decision

- 20 Claim records and 22 Evidence Use records inspected; all 22 Claim → Evidence Use → Source references resolve at version 1.
- 8 Claims have direct conceptual support, subject to exact locator capture and scope limitations.
- 12 Claims remain partial and require specific Sources, exact pinpoints, wording correction or source-identity repair.
- Econometrics Source identity is inaccurate and needs a versioned bibliographic correction.
- Education Claim A needs legal-scope wording correction before it can be considered directly supported.
- No D/E/B scores assigned or inferred.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation or risk metadata modified.
- No publication, release or public-pilot approval granted.
- Package 27 closes only this 20-Claim screening pass. Package 28 must come from a newly generated queue after this commit, not from this artifact.

## 6. Source references reviewed

- FAO AGRIS / ICARDA Harlan Symposium: https://agris.fao.org/search/en/providers/122511/records/669faf4b4295623862505523
- World Bank Staff Working Paper No. 302, Section IV: https://documents1.worldbank.org/curated/en/647121468766826467/pdf/multi0page.pdf
- World Bank WDR 2009 report: https://digitallibrary.un.org/nanna/record/1305303/files/WDR2009Eng.pdf
- OWID historical GDP and international-dollar methodology: https://ourworldindata.org/grapher/global-gdp-over-the-long-run
- OWID GDP and welfare limitations: https://ourworldindata.org/the-missing-economic-measure-wealth
- UNESCO right to education: https://www.unesco.org/en/right-education
- UNESCO lifelong-learning legal status discussion: https://www.unesco.org/en/right-education/evolving
- International IDEA Electoral System Design handbook: https://www.idea.int/publications/catalogue/electoral-system-design-new-international-idea-handbook
- IEA Energy Efficiency glossary: https://www.iea.org/glossary
- IEA Energy Efficiency Indicators: https://iea.blob.core.windows.net/assets/135d18c1-7640-4918-ad53-c093130f2513/Energy_Efficiency_Indicators_Essentials_for_Policy_Making.pdf
- EIA natural-gas price factors: https://www.eia.gov/tools/faqs/faq.php?id=43&t=9
- EIA electricity price factors: https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
- IEA World Energy Outlook 2024, Security/Affordability/Sustainability: https://www.iea.org/reports/world-energy-outlook-2024/security-affordability-and-sustainability
- Entomological Society of America: https://entsoc.org/about/what-is-entomology
- IMF Externalities: https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/externalities
