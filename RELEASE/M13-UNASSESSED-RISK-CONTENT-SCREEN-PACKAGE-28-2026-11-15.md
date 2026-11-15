# M13 — Unassessed Risk Content Screen — Package 28

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `8d97bda4126374f23f83f271f4497096ae91b04f`  
Queue workflow run: `43680949325`  
Queue artifact: `14148680807` (`m13-review-queue-8d97bda4126374f23f83f271f4497096ae91b04f`)  
Artifact SHA-256: `eaf3fd77e5a12687f5ed5c8d4454523c8be41b2bc6cc7bd32674deb99e0cab1d`

## 1. Fresh queue and selection integrity

Package 28 is Lane 1 of the fresh queue generated after Package 27.

- 4,834 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows reconciled; 0 Claims without a scored-report match.
- 72 unassessed-risk candidates remained after exclusions.
- 637 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with reviewed holdouts; 639 unique exclusions across these sets.
- 72 Claims selected in four non-empty lanes: 20, 20, 20 and 12; lane 5 is empty. There are 28 unfilled slots because only 72 eligible candidates remained.
- Lane 1 contains 20 unique Claims and 20 Evidence Use links. All selected Claim IDs are unique.
- Risk flags are routing signals only. Absence of a flag is not evidence of low risk.

## 2. Record-chain verification

The 20 selected Claim records, 20 linked Evidence Use records and 10 referenced Source records were fetched from the exact queue-source revision. All 20 Evidence Use records are version 1, use `evidence_role=supports`, and their `claim_ref` and `source_ref` resolve to the expected version-1 records.

Most Evidence Use descriptions are generic and do not record exact passage locators. The CDC/NIOSH ergonomics records are more specific and accurately limit the source to risk factors and a systematic ergonomics-program definition. Structural reference integrity is confirmed; it does not automatically establish substantive completeness.

## 3. Results

**17 Claims have direct conceptual support in their registered source material, subject to exact locator capture and scope limits. 3 remain partial or require claim-level remediation.**

| Claim ID | Existing Source | Result | Finding / required follow-up |
|---|---|---|---|
| `CLM-ENVIRONMENTAL_ECONOMICS_BASICS-C` | World Bank, *Environment* | PARTIAL — EVALUATION-METHOD SOURCE NEEDED | The registered World Bank page is a broad topic hub and does not establish the Claim's method-dependence proposition (goals, time horizon, data and evaluation method). Add a specific environmental-policy monitoring/evaluation source that explains how objectives determine indicators, data collection, time horizon and evaluation design. Candidate: World Bank, *Toward a Holistic Approach to Sustainable Development: A Guide to Integrated Land Use Initiatives*, monitoring/evaluation strategy section. |
| `CLM-EPIDEMIOLOGY_BASICS-A` | CDC, *Principles of Epidemiology* | PARTIAL — NON-SUBSTANTIVE CLAIM / REWRITE HOLD | The Claim says only that the slice “describes basic concepts and their relationships.” This is a meta-description of the topic, not a discrete, falsifiable epidemiological proposition. The CDC source cannot substantively validate that circular description. Replace with a specific Claim (for example, a properly scoped definition of epidemiology or a core measure) and then review the corresponding CDC passage. Do not score this as supported in its current form. |
| `CLM-EPISTEMOLOGY_BASICS-A` | Stanford Encyclopedia of Philosophy, *Epistemology* | DIRECT CONCEPTUAL SUPPORT | SEP defines epistemology narrowly as the study of knowledge and justified belief, and identifies questions about sources, structure and limits of knowledge. Record the opening definition locator. |
| `CLM-EPISTEMOLOGY_BASICS-C` | Stanford Encyclopedia of Philosophy, *Epistemology* | DIRECT CONCEPTUAL SUPPORT | SEP discusses the relation between evidence, belief and justification, including cases where a belief is justified by available evidence yet false, and the limits of such justification. Record the opening discussion and the relevant justification sections. |
| `CLM-ERGONOMICS_BASICS-B` | CDC/NIOSH, *About Ergonomics and Work-Related Musculoskeletal Disorders* | DIRECT CONCEPTUAL SUPPORT | NIOSH identifies force, repetition, awkward postures and vibration among physical risk factors for work-related musculoskeletal disorders. Record the “Workplace risks” section and retain the boundary that these are risk factors, not a diagnosis of an individual worker or a site-specific risk assessment. |
| `CLM-ERGONOMICS_BASICS-C` | CDC/NIOSH, *About Ergonomics and Work-Related Musculoskeletal Disorders* | DIRECT CONCEPTUAL SUPPORT | NIOSH explicitly defines an ergonomics program as a systematic process for identifying, analyzing and controlling workplace risk factors. Record the “Ergonomics program” locator; the page does not by itself provide a complete task-specific assessment protocol. |
| `CLM-ETHNOBOTANY_BASICS-A` | Royal Botanic Gardens, Kew, *Tradition to Transition: Ethnobotanical Insights into Changing Enset Farming Systems in Ethiopia* | DIRECT CONCEPTUAL SUPPORT | Kew explicitly defines ethnobotany as exploring human relationships with plants by combining botany and social sciences, including how cultures use, manage and perceive plants. Record the “What do we mean when we talk about ethnobotany?” section. |
| `CLM-ETHNOBOTANY_BASICS-B` | Same Kew source | DIRECT CONCEPTUAL SUPPORT | Kew documents local enset farming systems in which crop varieties, cultivation, processing, use and consumption are embedded in cultural practices and community life. Record the enset and Basketo sections; retain the Ethiopia-specific case-study scope. |
| `CLM-ETHNOBOTANY_BASICS-C` | Same Kew source | DIRECT CONCEPTUAL SUPPORT | Kew describes changes in land allocated to enset, consumption patterns and crop-variety abundance, showing how changes in land use and production practices can affect local plant diversity. Record the “Shifting Agricultural Priorities” section and present it as a documented case, not a universal causal law. |
| `CLM-FOOD_DISTRIBUTION_BASICS-C` | FAO, *Food Systems* | PARTIAL — SPECIFIC FOOD-SECURITY SOURCE NEEDED | The registered FAO page describes the food chain from production through processing, transport, distribution and consumption, but is a broad hub. The Claim's point that local availability is not determined solely by production requires a precise source on imports, reserves, markets, transport and physical/economic access. Add FAO's food-security dimensions or HLPE Report 12 with exact locators. |
| `CLM-FORMAL_METHODS_BASICS-A` | NASA Langley, *What Is Formal Methods?* | DIRECT CONCEPTUAL SUPPORT | NASA defines formal methods as mathematically rigorous techniques and tools for specification, design and verification of software and hardware systems. Record the opening definition and retain the distinction between rigorous specification and formal verification. |
| `CLM-FORMAL_METHODS_BASICS-B` | Same NASA source | DIRECT CONCEPTUAL SUPPORT | NASA describes formal verification as checking whether properties hold across the state space and identifies model checking and theorem proving as techniques. Record the state-space and formal-verification passages. |
| `CLM-FORMAL_METHODS_BASICS-C` | Same NASA source | DIRECT CONCEPTUAL SUPPORT | NASA explicitly explains that full state-space examination is rarely practical for real systems because of complexity and lists abstraction, focusing on critical components, reducing model ranges, hierarchical analysis and automation as practical approaches. Record these limitation/mitigation passages. |
| `CLM-GAME_THEORY_BASICS-A` | Stanford Encyclopedia of Philosophy, *Game Theory* (Fall 2014 archive) | DIRECT CONCEPTUAL SUPPORT | SEP defines a game through interacting choices where each agent's best action depends on expectations about other agents' actions. Record the opening definition and section 2.2. |
| `CLM-GAME_THEORY_BASICS-B` | Same SEP source | DIRECT CONCEPTUAL SUPPORT | SEP defines Nash equilibrium as a set of strategies in which no player can improve their payoff by changing strategy unilaterally, given the other players' strategies. Record section 2.5. |
| `CLM-GAME_THEORY_BASICS-C` | Same SEP source | DIRECT CONCEPTUAL SUPPORT | SEP distinguishes equilibrium from social desirability and shows Prisoner's Dilemma equilibria that are Pareto-inferior to feasible cooperative outcomes. Record sections 2.5–2.7; preserve the distinction between stability, individual incentives and social efficiency. |
| `CLM-GEODESY_BASICS-A` | NOAA National Geodetic Survey, *What Is Geodesy?* | DIRECT CONCEPTUAL SUPPORT | NGS defines geodesy as accurately measuring and understanding Earth's geometric shape, orientation in space and gravity field. Record the opening definition. |
| `CLM-GEODESY_BASICS-B` | Same NOAA NGS source | DIRECT CONCEPTUAL SUPPORT | NGS explains that geodesists assign consistent coordinates to points on Earth's surface and that accurately measured points form the basis of the National Spatial Reference System, allowing maps to align consistently. Record the coordinate and NSRS paragraphs. |
| `CLM-GEODESY_BASICS-C` | Same NOAA NGS source | DIRECT CONCEPTUAL SUPPORT | NGS explicitly identifies mapping shorelines, determining land boundaries and improving transportation/navigation safety as applications. It also explains that consistent coordinates are essential. Record these application passages and avoid implying every legal boundary is determined by geodesy alone. |
| `CLM-GEOPHYSICS_BASICS-A` | USGS, *Earthquake Hazards Program Glossary* | DIRECT CONCEPTUAL SUPPORT | The registered USGS glossary contains a direct “Geophysics” entry defining it as the branch of Earth science using physical measurements and mathematical models to explore and analyze the structure and dynamics of the solid Earth and related fluid envelopes. Record that exact glossary entry. |

## 4. Cross-record, source and scope findings

1. The CDC/NIOSH ergonomics Source directly supports Claims B and C. The two Evidence Use descriptions correctly distinguish risk-factor examples from the systematic programme definition.
2. The Epidemiology Claim A is not a substantive proposition; it is a generic slice-description sentence. It must be rewritten before evidence-fit or D/E/B assessment.
3. The Kew ethnobotany source is a detailed Ethiopia/enset case study. It directly supports the stated relationship concepts, but any global generalization must be supported by additional cases.
4. The FAO Food Systems page is a high-level entry point. Add a more specific FAO food-security or food-distribution source for local availability, transport, markets, reserves and access.
5. The NASA formal-methods source directly addresses state-space complexity and practical abstraction strategies; the Claim should not imply that full formal verification of every possible system is routinely feasible.
6. The Stanford SEP Game Theory entry is the Winter 2014 archived edition. It explicitly distinguishes Nash equilibrium from social efficiency and Pareto superiority. Keep the archived edition pinned rather than silently switching to the current entry.
7. The NOAA geodesy page is an official National Geodetic Survey explainer and directly supports coordinates, spatial reference, mapping, boundaries and navigation. Its examples are U.S.-focused; avoid implying legal rules are globally uniform.
8. The USGS Source is a glossary page. Its exact “Geophysics” entry is a suitable pinpoint; the broader glossary should not be treated as evidence for unrelated geophysical propositions.
9. Legacy `publication_status=published` and `completion_status=complete` values are distinct from M13 risk status. All 20 Claims remain `UNASSESSED`; no publication authorization is inferred.

## 5. Decision

- 20 Claim records and 20 Evidence Use records inspected; all 20 Claim → Evidence Use → Source references resolve at version 1.
- 17 Claims have direct conceptual support, subject to exact locator capture and scope limitations.
- 3 remain partial or require claim-level remediation: Environmental Economics C, Epidemiology A and Food Distribution C.
- Epidemiology A is a meta-description, not a substantive Claim, and must be rewritten.
- No D/E/B scores assigned or inferred.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation or risk metadata modified.
- No publication, release or public-pilot approval granted.
- Package 28 closes only this 20-Claim screening pass. Package 29 must come from a newly generated queue after this commit, not from this artifact.

## 6. Source references reviewed

- World Bank integrated land-use M&E guidance: https://documents1.worldbank.org/curated/en/831591628501365387/pdf/Toward-a-Holistic-Approach-to-Sustainable-Development-A-Guide-to-Integrated-Land-Use-Initiatives.pdf
- CDC Principles of Epidemiology: https://www.cdc.gov/training-publichealth101/php/lessons/principles-of-epidemiology.html
- Stanford Encyclopedia of Philosophy, Epistemology: https://plato.stanford.edu/entries/epistemology/
- CDC/NIOSH Ergonomics overview: https://www.cdc.gov/niosh/ergonomics/about/index.html
- CDC/NIOSH Step 1 risk factors: https://www.cdc.gov/niosh/ergonomics/ergo-programs/risk-factors.html
- Royal Botanic Gardens, Kew, ethnobotany and enset: https://www.kew.org/read-and-watch/ethnobotanical-insights-enset-ethiopia
- FAO HLPE Report 12, Nutrition and Food Systems: https://www.fao.org/fileadmin/user_upload/hlpe/hlpe_documents/HLPE_Reports/HLPE-Report-12_EN.pdf
- FAO Food Systems: https://www.fao.org/food-systems/en/
- NASA Langley, What Is Formal Methods?: https://shemesh.larc.nasa.gov/fm/fm-what.html
- Stanford Encyclopedia of Philosophy, Game Theory (Fall 2014): https://plato.stanford.edu/archives/fall2014/entries/game-theory/
- NOAA National Geodetic Survey, What Is Geodesy?: https://www.ngs.noaa.gov/INFO/facts/geodesy.shtml
- USGS Earthquake Hazards Program Glossary, “Geophysics”: https://www.usgs.gov/glossary/earthquake-hazards-program
