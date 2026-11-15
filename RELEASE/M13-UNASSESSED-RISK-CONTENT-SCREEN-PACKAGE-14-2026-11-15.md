# M13 — unassessed-risk content screen, Package 14

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `f7964ca35e4b3f2832287750a731ee3fc94f0e72`  
Queue artifact: `14144742409` (workflow run `43672756486`, successful)  
Scope: Lane 1, first 20 exact Claim IDs from the refreshed 100-Claim queue.  
State: **desk-level source-fit and risk-routing review. No D/E/B scores, canonical record edits, risk metadata changes, publication changes or specialist approvals.** This package is not an M13 closure decision.

## 1. Queue integrity and exact scope

The exact artifact was downloaded and inspected. It reports:

- 1,494 inventoried Claims;
- 357 previously screened Claims excluded;
- 17 unreconciled HOLD Claims excluded;
- 15 overlaps between those two exclusion sets;
- 359 unique exclusions;
- 352 eligible unassessed candidates;
- 100 selected Claims in five lanes of 20;
- 100 unique selected IDs and zero unfilled slots.

The queue explicitly warns that absence of risk domains or machine triage flags does not establish low risk. In the inventory, 783 Claims have at least one recorded risk signal, 591 have a high-consequence screen, and 711 have no recorded risk signal; those 711 remain UNASSESSED, not low-risk.

Package 13's 20 Claims are in the previously-screened exclusion set and do not reappear in the selected queue. Lane 1 below is the next 20-Claim batch. All 20 were checked against their Claim statement and associated Evidence Use / Source packet.

| # | Claim | Evidence Use | Source |
|---:|---|---|---|
| 1 | `CLM-HISTORY_OF_SCIENCE-C@1` | `EU-HISTORY_OF_SCIENCE-C@1` | `SRC-HISTORY_OF_SCIENCE@1` |
| 2 | `CLM-HISTORY_OF_TECHNOLOGY-A@1` | `EU-HISTORY_OF_TECHNOLOGY-A@1` | `SRC-HISTORY_OF_TECHNOLOGY@1` |
| 3 | `CLM-HISTORY_OF_TECHNOLOGY-B@1` | `EU-HISTORY_OF_TECHNOLOGY-B@1` | `SRC-HISTORY_OF_TECHNOLOGY@1` |
| 4 | `CLM-HISTORY_OF_TECHNOLOGY-C@1` | `EU-HISTORY_OF_TECHNOLOGY-C@1` | `SRC-HISTORY_OF_TECHNOLOGY@1` |
| 5 | `CLM-HOUSING_SYSTEMS_BASICS-B@1` | `EU-HOUSING_SYSTEMS_BASICS-B@1` | `SRC-HOUSING_SYSTEMS_BASICS@1` |
| 6 | `CLM-HUMAN_AI_INTERACTION_BASICS-A@1` | `EU-HUMAN_AI_INTERACTION_BASICS-A@1` | `SRC-HUMAN_AI_INTERACTION_BASICS@1` |
| 7 | `CLM-HUMAN_AI_INTERACTION_BASICS-B@1` | `EU-HUMAN_AI_INTERACTION_BASICS-B@1` | `SRC-HUMAN_AI_INTERACTION_BASICS@1` |
| 8 | `CLM-HUMAN_AI_INTERACTION_BASICS-C@1` | `EU-HUMAN_AI_INTERACTION_BASICS-C@1` | `SRC-HUMAN_AI_INTERACTION_BASICS@1` |
| 9 | `CLM-HUMAN_RIGHTS_BASICS-C@1` | `EU-HUMAN_RIGHTS_BASICS-C@1` | `SRC-HUMAN_RIGHTS_BASICS@1` |
| 10 | `CLM-HUMANITARIAN_LOGISTICS_BASICS-A@1` | `EU-HUMANITARIAN_LOGISTICS_BASICS-A@1` | `SRC-HUMANITARIAN_LOGISTICS_BASICS@1` |
| 11 | `CLM-HUMANITARIAN_LOGISTICS_BASICS-B@1` | `EU-HUMANITARIAN_LOGISTICS_BASICS-B@1` | `SRC-HUMANITARIAN_LOGISTICS_BASICS@1` |
| 12 | `CLM-HYDRAULIC_ENGINEERING-A@1` | `EU-HYDRAULIC_ENGINEERING-A@1` | `SRC-HYDRAULIC_ENGINEERING@1` |
| 13 | `CLM-HYDRAULIC_ENGINEERING-B@1` | `EU-HYDRAULIC_ENGINEERING-B@1` | `SRC-HYDRAULIC_ENGINEERING@1` |
| 14 | `CLM-HYDRAULIC_ENGINEERING-C@1` | `EU-HYDRAULIC_ENGINEERING-C@1` | `SRC-HYDRAULIC_ENGINEERING@1` |
| 15 | `CLM-INDOOR_AIR_QUALITY_BASICS-A@1` | `EU-INDOOR_AIR_QUALITY_BASICS-A@1` | `SRC-INDOOR_AIR_QUALITY_BASICS@1` |
| 16 | `CLM-INDOOR_AIR_QUALITY_BASICS-B@1` | `EU-INDOOR_AIR_QUALITY_BASICS-B@1` | `SRC-INDOOR_AIR_QUALITY_BASICS@1` |
| 17 | `CLM-INDOOR_AIR_QUALITY_BASICS-C@1` | `EU-INDOOR_AIR_QUALITY_BASICS-C@1` | `SRC-INDOOR_AIR_QUALITY_BASICS@1` |
| 18 | `CLM-INFORMATION_LITERACY_BASICS-A@1` | `EU-INFORMATION_LITERACY_BASICS-A@1`; `EU-INFORMATION_LITERACY_BASICS-A-2@1` | `SRC-INFORMATION_LITERACY_BASICS@1`; `SRC-ACRL-INFORMATION-LITERACY-2026@1` |
| 19 | `CLM-INFORMATION_LITERACY_BASICS-B@1` | `EU-INFORMATION_LITERACY_BASICS-B@1`; `EU-INFORMATION_LITERACY_BASICS-B-2@1` | `SRC-INFORMATION_LITERACY_BASICS@1`; `SRC-ACRL-INFORMATION-LITERACY-2026@1` |
| 20 | `CLM-INFORMATION_LITERACY_BASICS-C@1` | `EU-INFORMATION_LITERACY_BASICS-C@1`; `EU-INFORMATION_LITERACY_BASICS-C-2@1` | `SRC-INFORMATION_LITERACY_BASICS@1`; `SRC-ACRL-INFORMATION-LITERACY-2026@1` |

## 2. Claim-by-Claim source-fit findings

### 2.1 History of Science C — period- and question-specific evidence for causal/priority claims

**Claim:** “Историческое утверждение о причинах или приоритетах научного изменения требует источников, соответствующих конкретному периоду и вопросу.”

**Registered source:** Smithsonian Libraries and Archives, History of Science and Technology Research Guide — https://library.si.edu/research/history-science-technology

**Finding: PARTIAL / METHODOLOGICAL CLAIM.** The guide is a curated research gateway listing catalogues, primary-source collections, archives and subject resources. It demonstrates that historical research uses sources suited to specific topics and periods, but it does not directly establish a formal rule for evaluating causal or priority claims. Its shared URL with the Technology slice is a duplicate-source-URI candidate, not independent corroboration.

**Follow-up:** Add a recognized historiography or historical-method source on causal explanation and priority disputes, with an exact passage. Keep the present guide as a discovery resource, not the sole evidentiary basis.

### 2.2 History of Technology A — development of technical objects, practices and knowledge

**Claim:** “История технологий рассматривает развитие технических объектов, практик и связанных с ними знаний во времени.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** The Smithsonian guide identifies resources covering technical manuals, trade literature, engineering archives, historical collections and the relationship between technology, engineering and society, politics, economics and culture. Its National Museum of American History Archives Center description identifies collections documenting technology, invention and innovation. This is a good research-resource basis, though not a formal definition of the discipline.

**Follow-up:** Add pinpoint descriptions for the Trade Literature Collection and Archives Center, and ideally a scholarly history-of-technology introduction for the disciplinary definition.

### 2.3 History of Technology B — documentary and archival source types

**Claim:** “Источники по истории технологий включают материалы о технологиях и инженерии, а также архивные и библиотечные коллекции.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** The Smithsonian guide explicitly lists technical manuals, catalogues, brochures, engineering archives, library catalogues, rare books, manuscripts and museum object records. The claim is appropriately broad and does not imply that these collections are exhaustive.

**Follow-up:** Replace the generic EU sentence with the specific collection types and stable links. Do not count multiple collections within the same Smithsonian guide as independent sources.

### 2.4 History of Technology C — artifact existence does not establish a single cause

**Claim:** “Наличие технического артефакта само по себе не доказывает единственную причину его появления или распространения.”

**Finding: PARTIAL / INFERENCE SAFEGUARD.** Smithsonian's primary-source teaching material explains that objects are evidence of human thought, workmanship and use, but “objects alone will not tell us the whole story”; they must be studied carefully and critically alongside other evidence. This supports caution against over-interpreting artifacts. It does not directly prove a general causal-inference rule about the origin or diffusion of every technology.

**Follow-up:** Add a historical-methodology source on multi-causal explanation and triangulation of material, documentary and contextual evidence. Preserve this as an inference/methodological principle, not a fact attributed solely to the Smithsonian collections guide.

### 2.5 Housing Systems B — housing location and access to services

**Claim:** “Жильё связано с доступом к занятости, образованию, здравоохранению и другим городским и социальным услугам.”

**Registered source:** UN-Habitat, Housing — https://unhabitat.org/topic/housing

**Finding: DIRECT SUPPORT.** UN-Habitat explicitly states that access to housing is a precondition for access to employment, education, health and social services. Its housing adequacy material further treats location as inadequate where housing is isolated from jobs, healthcare, schools, childcare and other social facilities.

**Follow-up:** Add exact locators to the UN-Habitat Housing overview and its location/adequate-housing guidance. Keep the statement general; do not infer that housing alone guarantees access to services.

### 2.6 Human-AI Interaction A — distinguish human and AI decision roles

**Claim:** “Роли человека и ИИ в принятии решений должны быть различимы.”

**Registered source:** NIST AI RMF 1.0, Appendix C — https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/

**Finding: DIRECT SUPPORT.** Appendix C explicitly says human roles and responsibilities in decision-making and AI oversight need to be clearly defined and differentiated. It describes configurations ranging from fully autonomous to fully manual, including AI decisions, human expert decisions and AI as an additional opinion.

**Follow-up:** Add Appendix C, first issue, PDF page 40, as the exact locator. The current EU must quote/paraphrase this passage rather than remain generic.

### 2.7 Human-AI Interaction B — task, context and human participation affect outcomes

**Claim:** “Результат человек–ИИ зависит от задачи, контекста и организации участия человека.”

**Finding: DIRECT SUPPORT.** NIST Appendix C states that human-AI interaction results vary. It gives perceptual-judgment tasks as an example where AI may amplify human bias, while judiciously organized human-AI teams can achieve complementarity and improve overall performance. It also describes different human/AI configurations and oversight needs.

**Follow-up:** Add Appendix C, first and third issues, PDF page 40. Clarify that outcomes are conditional; do not claim that human-AI collaboration always improves performance.

### 2.8 Human-AI Interaction C — model representations can lose human context

**Claim:** “Модели могут терять часть контекста человеческих явлений, поэтому ограничения важны при интерпретации.”

**Finding: DIRECT SUPPORT.** NIST Appendix C says data-driven approaches can represent individual and social observational/decision practices as measurable quantities, but mathematical modelling of complex human phenomena can remove necessary context. It notes that this loss can obscure individual and societal impacts relevant to risk management.

**Follow-up:** Add Appendix C, opening paragraphs, PDF page 40. Preserve the modal “могут”; the source does not claim that every model necessarily loses context.

### 2.9 Human Rights C — UDHR status and influence on later international law

**Claim:** “Декларация является декларативным международным документом и стала основой для последующего развития международной системы защиты прав человека.”

**Registered source:** United Nations, Universal Declaration of Human Rights — https://www.un.org/en/about-us/universal-declaration-of-human-rights/

**Finding: DIRECT SUPPORT WITH LEGAL PRECISION REQUIRED.** UN Geneva explains that the UDHR itself is not legally binding as a document but represents a joint commitment of States; the UN describes it as inspiring more than 80 international human-rights treaties and declarations. The UN Foundation of International Human Rights Law page characterizes it as the foundation of international human-rights law. “Декларативный” must not be misunderstood as meaning legally irrelevant or without normative influence.

**Follow-up:** Add the UN Foundation of International Human Rights Law page and UN Geneva explanation as separate locators. Clarify that the UDHR is a declaration, not a treaty, and that later binding obligations arise through subsequent legal instruments and other sources of international law.

### 2.10 Humanitarian Logistics A — overcoming logistics constraints to deliver assistance

**Claim:** “Гуманитарная логистика помогает преодолевать логистические ограничения при доставке помощи пострадавшему населению.”

**Registered source:** WFP Logistics Cluster — https://www.wfp.org/logistics-cluster

**Finding: DIRECT SUPPORT.** WFP states that the Logistics Cluster supports actors in overcoming logistics constraints to delivery of global humanitarian assistance and provides leadership and logistics support during crises. This closely matches the Claim.

**Follow-up:** Remove the trailing slice name from the Claim text if it is not part of the intended canonical statement; add a locator to the WFP mandate/purpose paragraph. Treat WFP and the Logistics Cluster website as related organizational sources, not automatically independent.

### 2.11 Humanitarian Logistics B — coordination, information management and common services

**Claim:** “Координация, информационный обмен и доступ к общим логистическим услугам являются частью поддержки гуманитарных операций.”

**Finding: DIRECT SUPPORT.** The Logistics Cluster mandate explicitly lists coordination, information management and facilitating access to common logistics services. Its core services and country-level activities give operational examples of those functions.

**Follow-up:** Add the Logistics Cluster “Who we are / The Logistics Cluster” mandate and core-services passages. Avoid implying that every response operation receives identical services; support depends on needs and local capacity.

### 2.12 Hydraulic Engineering A — distinction between hydrology and hydraulics

**Claim:** “Гидравлика и гидрология связаны с водными ресурсами, но описывают разные аспекты поведения и управления водой.”

**Registered source:** U.S. Army Corps of Engineers — Hydrology and Hydraulics.

**Finding: PARTIAL.** USACE district descriptions distinguish hydrologic and hydraulic matters and list different applications, but the registered source page is a broad organizational overview and does not clearly define the conceptual distinction. Hydrology generally addresses occurrence, movement and distribution of water; hydraulics addresses fluid behaviour and flow in systems and structures. The exact definitions need a technical reference.

**Follow-up:** Add a USACE H&H technical manual or authoritative hydrology/hydraulics textbook defining both disciplines, then make the EU explain the distinction without treating the fields as wholly separate.

### 2.13 Hydraulic Engineering B — analysis of flows and water structures

**Claim:** “Инженерная гидравлика применяется к анализу водных потоков и водных сооружений в рамках задач управления водными ресурсами.”

**Finding: DIRECT CONCEPTUAL SUPPORT.** USACE Hydraulics & Hydrology branches describe hydraulic engineering design and analysis for water resources, including open channels, conduits, hydraulic structures, erosion protection and flood-risk reduction. This directly supports the practical application described.

**Follow-up:** Add the Omaha District Hydraulics section and Memphis District H&H Branch mission statement as exact locators. These are examples of USACE practice, not a universal definition of all hydraulic engineering.

### 2.14 Hydraulic Engineering C — USACE modelling and engineering analysis

**Claim:** “USACE использует гидравлическое моделирование и инженерный анализ для задач, связанных с каналами, сооружениями и управлением риском наводнений.”

**Finding: DIRECT SUPPORT.** USACE Omaha District identifies 1-D and 2-D hydraulic modelling, hydraulic design/review of open channels and conduits, hydraulic structures and flood-risk reduction measures. USACE Hydrologic Engineering Center describes watershed/channel information used for flood-damage reduction, operation of hydraulic-conveyance and water-control facilities, and flood preparation/response.

**Follow-up:** Add the Omaha District Hydraulics section and HEC study-classification page as exact locators. Keep the subject explicitly USACE; do not generalize its specific organizational practice to every agency.

### 2.15 Indoor Air Quality A — sources, ventilation and environmental conditions

**Claim:** “Качество воздуха внутри помещений зависит от источников загрязнения, вентиляции и условий среды.”

**Registered source:** U.S. EPA Indoor Air Quality — https://www.epa.gov/air-quality/indoor-air-quality

**Finding: DIRECT SUPPORT.** EPA identifies indoor pollutant sources, air-exchange rate, infiltration, natural and mechanical ventilation, outdoor climate, weather and occupant behaviour as factors affecting indoor air quality. The registered generic IAQ landing page should be supplemented with the EPA Report on the Environment page for the explicit factor list.

**Follow-up:** Add EPA Report on the Environment, “Other Factors Affecting Indoor Air Quality,” and its “Pollutants and Sources” section as locators.

### 2.16 Indoor Air Quality B — inadequate ventilation and pollutant concentration

**Claim:** “Недостаточная вентиляция может повышать концентрации некоторых загрязнителей внутри помещений.”

**Finding: DIRECT SUPPORT.** EPA explains that when infiltration, natural ventilation or mechanical ventilation is low, pollutant levels can increase. It also explains that ventilation dilutes indoor pollutants, while source control and filtration have distinct roles.

**Follow-up:** Add EPA *The Inside Story: A Guide to Indoor Air Quality*, ventilation/air-exchange discussion, and EPA *Care for Your Air*, ventilation guidance. Preserve “может”: source strength, outdoor concentrations and removal processes also affect indoor concentrations.

### 2.17 Indoor Air Quality C — room-specific assessment and interventions

**Claim:** “Оценка качества воздуха и меры по его улучшению зависят от конкретного помещения, источников и условий.”

**Finding: DIRECT SUPPORT.** EPA describes different pollutant sources in homes, apartments and offices; it notes that solutions depend on sources and building conditions and may require action by residents or building owners. EPA's guidance identifies source control, ventilation, filtration and humidity as context-dependent measures.

**Follow-up:** Add the EPA Inside Story sections on apartments and solutions, and EPA Improving Indoor Air Quality on source control and ventilation. Do not turn this broad Claim into a universal prescription for one intervention.

### 2.18 Information Literacy A — integrated critical work with information and sources

**Claim:** “Информационная грамотность включает навыки критической работы с информацией и источниками.”

**Registered sources:** UNESCO Media and Information Literacy; ACRL Framework for Information Literacy for Higher Education.

**Finding: DIRECT CONCEPTUAL SUPPORT.** ACRL defines information literacy as integrated abilities involving reflective discovery, understanding how information is produced and valued, and using information to create knowledge and participate ethically. Its “Authority Is Constructed and Contextual” frame requires critical source evaluation. UNESCO's MIL framework is complementary but broader and should not be treated as an independent duplicate of ACRL.

**Follow-up:** Add the ACRL definition and “Authority Is Constructed and Contextual” frame as precise EU locators; retain UNESCO as broader media/information literacy context with its own distinct role.

### 2.19 Information Literacy B — source, context, evidence and claim limitations

**Claim:** “Критическая оценка информации требует внимания к источнику, контексту, доказательствам и ограничениям утверждения.”

**Finding: DIRECT CONCEPTUAL SUPPORT, LOCATOR GAP.** ACRL explicitly states that authority is constructed and contextual, that resources should be evaluated against the information need and context of use, and that learners should critically evaluate sources for credibility and ask about origin, context and suitability. The “Research as Inquiry” frame calls for monitoring gathered information and assessing gaps or weaknesses. The current EU text needs to name these distinct passages rather than merely state that an additional source confirms the Claim.

**Follow-up:** Add exact ACRL “Authority Is Constructed and Contextual” and “Research as Inquiry” locators. Keep the claim as a general evaluative principle, not a fixed checklist that exhausts all forms of evidence appraisal.

### 2.20 Information Literacy C — repetition/publication does not establish truth

**Claim:** “Публикация или многократное повторение утверждения сами по себе не доказывают его истинность.”

**Finding: PARTIAL / STRONG CONCEPTUAL SUPPORT.** ACRL says sources and authority must be critically evaluated, research and information can be misrepresented or created to mislead, and misinformation/disinformation affect information conversations. This supports the need not to equate circulation or apparent authority with truth, but the exact proposition about repetition alone is not directly stated in the current registered passages.

**Follow-up:** Add a source specifically addressing repetition, familiarity/illusory-truth effects or the evidentiary distinction between repetition and verification. Alternatively narrow the Claim to the ACRL-supported statement that information can be misrepresented and requires critical evaluation.

## 3. Cross-cutting findings

1. **Generic EU descriptions remain the main documentary defect.** The source chain is often present, but the EU material does not yet identify the exact passage, its evidentiary role and its scope.
2. **Shared URLs do not create independent corroboration.** The History of Science and History of Technology Claims use the same Smithsonian guide URL. The three Human-AI Claims use one NIST appendix; the two humanitarian-logistics Claims use one Logistics Cluster mandate; these are coherent source clusters, not multiple independent sources.
3. **History of Science C and History of Technology C are methodological claims.** Their evidentiary requirements differ from ordinary descriptive Claims. They need historiography/methodology sources and must retain inference status.
4. **Hydraulic Engineering A needs a definitional source.** Official USACE activity pages establish what USACE does, but do not fully define the conceptual distinction between hydrology and hydraulics.
5. **Human Rights C needs legal precision.** The UDHR is not itself a treaty, but it has major normative and historical influence and inspired later binding instruments.
6. **Indoor-air claims require contextual qualifiers.** Source strength, outdoor air, air exchange, occupant behaviour and removal processes all matter; ventilation alone does not determine indoor concentrations.
7. **Information Literacy C requires either a source on repetition effects or narrower wording.** ACRL supports critical evaluation and misinformation awareness, not every possible psychological mechanism of repeated claims.
8. **No D/E/B scores are assigned.** Source-fit labels are descriptive desk-review findings, not M13 assessment grades.
9. **No canonical Claim, EU or Source record was edited.** No risk metadata, publication status, rights status or specialist approval was changed.

## 4. Disposition

- 20/20 Claims inspected at desk level against the exact Claim/EU/Source packet.
- 15 Claims have direct conceptual support, subject to exact locator and EU-description remediation.
- 5 Claims remain partial and require methodological, definitional or more specific source support.
- 20/20 remain unclosed for M13; no D/E/B score or specialist approval is inferred.
- Next work: add precise locators to the direct cases; source the historical-methodology and hydrology/hydraulics distinctions; repair the information-literacy repetition Claim; then conduct evidence-quality, source-independence and risk review.

**Package 14 is a source-fit checkpoint, not a closure certificate. HOLD remains in force.**
