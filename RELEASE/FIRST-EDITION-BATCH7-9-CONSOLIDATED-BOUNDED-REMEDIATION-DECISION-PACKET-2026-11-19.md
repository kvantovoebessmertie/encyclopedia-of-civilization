# First Edition — Consolidated Batch 7–9 Bounded Remediation Decision Packet

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Target: PR #22 — `mvp-public-contribution-design-2026-10-11`  
Frozen proposal baseline: `5898c5be78475d1f190761343c7f95f865302405`  
Status: **DECISION PACKET ONLY — NO NEW CANONICAL AUTHORIZATION; NO CANONICAL JSON CHANGED BY THIS DOCUMENT**

## 1. Purpose and change-control boundary

This packet consolidates the unresolved, previously researched remediation proposals from Batch 7, Batch 8 and Batch 9. The relevant Claim, Evidence Use and Source records were re-fetched from the current PR branch at baseline `5898c5be78475d1f190761343c7f95f865302405`. The inspected records listed below are currently version 1 unless an exception is explicitly stated.

This is a decision-ready proposal, not an authorization to execute canonical edits. It does not modify canonical records, Relations, validators, coverage manifests, allowlists, publication/completion states or release decisions. It does not assign INCLUDE or EXCLUDE. All affected candidate slices remain HOLD.

Existing bounded authorizations and already-completed remediation work in `RELEASE/EDITORIAL-CORRECTION.json` are not reopened here. In particular, the six legal/trade/institutional slices, engineering/computing, chemistry, human sciences, remaining R7 source work and R9 workstreams retain their own scopes and reports. International Law's separate substantive review and reference-alignment authorization also remain separate; this packet does not supersede them.

## 2. Executive disposition

| Batch | Slice | Current records re-fetched | Proposed canonical work | Decision still needed |
|---|---|---:|---|---|
| 7 | cultural-anthropology-basics | 3 Claims, 3 EUs, 1 Source | Source identity/edition; 3 pinpoint EUs; narrow Claim B | Approve Claim B narrowing and non-commercial source compatibility |
| 7 | education-systems | 3 Claims, 3 EUs, 1 Source | Pin A/B; resolve Claim C scope and add the correct source dependency | Choose narrow UNESCO-methodology Claim C or authorize a multi-source comparative graph |
| 8 | electromagnetism-basics | 3 Claims, 3 EUs, 1 Source | Replace 3 metadata Claims; 3 pinpoint EUs; align dependencies | Subject-matter/editorial approval; OpenStax licence/AI-use boundary |
| 8 | fluid-mechanics-basics | 3 Claims, 3 EUs, 1 Source | Replace 3 metadata Claims; 3 pinpoint EUs; align dependencies | Subject-matter/editorial approval; assumptions and licence boundary |
| 8 | geometry-basics | 3 Claims, 3 EUs, 1 Source | Correct Source identity; 3 EUs; narrow Claim C | Approve Claim C wording and source replacement |
| 8 | governance-basics | 3 Claims, 3 EUs, 1 Source | Add 3 OECD locators; narrow Claim C | Approve Claim C scope; OECD rights review |
| 8 | historical-geography-basics | 3 Claims, 3 EUs, 1 Source | Replace generic Source with LOC guide; add 3 EUs | Approve source fit; item-level map rights boundary |
| 9 | settlement-geography-basics | 3 Claims, 3 EUs, 1 Source | Correct joint-source identity; 3 EUs | Approve bibliographic correction; CC BY-NC-SA compatibility |
| 9 | antimicrobial-resistance-basics | Claim C, EU C, Source | Update dynamic WHO source identity/date; pin EU C | Approve source metadata update and rights screen |
| 9 | statistics-basics | Claim C, EU C, Source | Pin NIST §4.3.1; narrow Claim C | Approve Claim C wording and joint-publication rights screen |

**Aggregate:** 10 slices; 26 Evidence Use records; 6 Claim statements proposed for substantive replacement (electromagnetism A–C and fluid mechanics A–C); 5 further Claim wording refinements/narrowings (cultural anthropology B, education systems C, geometry C, governance C, statistics C); 5 Source identity/edition changes proposed (cultural anthropology, geometry, historical geography, settlement geography, AMR). Education Systems requires an additional Source identity whose canonical ID has deliberately not been invented.

## 3. Batch 7 — proposed exact changes

### 3.1 Cultural Anthropology

Current canonical records at baseline: all listed records are v1.

| Record | Current | Proposed |
|---|---:|---|
| `SRC-CULTURAL_ANTHROPOLOGY` | @1 | @2 — identify Nina Brown, Thomas McIlwraith and Laura Tubelle de González, *Perspectives: An Open Introduction to Cultural Anthropology*, 2nd edition; use the official AAA textbook landing/edition identity and chapter PDFs |
| `CLM-CULTURAL_ANTHROPOLOGY-A` | @1 | @2 — statement unchanged; provenance only, aligned to Source @2 |
| `CLM-CULTURAL_ANTHROPOLOGY-B` | @1 | @2 — narrow statement to the four perspectives named by the source |
| `CLM-CULTURAL_ANTHROPOLOGY-C` | @1 | @2 — statement unchanged; provenance only, aligned to Source @2 |
| `EU-CULTURAL_ANTHROPOLOGY-A` | @1 | @2 — Introduction to Anthropology, “What is Anthropology?” and “What is Cultural Anthropology?”, printed pp. 5–6 |
| `EU-CULTURAL_ANTHROPOLOGY-B` | @1 | @2 — Introduction to Anthropology, “What is Anthropology?”, printed pp. 4–6 |
| `EU-CULTURAL_ANTHROPOLOGY-C` | @1 | @2 — Doing Fieldwork: Methods in Cultural Anthropology, “Emic and Etic Perspectives” pp. 48–49; “Observation and Participant Observation” pp. 60–61; “Field Notes” pp. 62–63; “Reflexivity” p. 66 |

**Proposed Claim B statement**

> Антропология изучает человеческий опыт через четыре традиционные области: культурную, лингвистическую, археологическую и биологическую антропологию.

Claim A and C statements remain unchanged. Context and Scope should be reviewed for target/version alignment if their target Claim A reference is advanced; no wider context rewrite is proposed.

**Source references**
- Introduction: https://perspectives.americananthro.org/second-edition/Chapters/Introduction_to_Anthropology.pdf
- Fieldwork: https://perspectives.americananthro.org/Chapters/Fieldwork.pdf

**Rights boundary:** the textbook identifies CC BY-NC 4.0. Attribution is required; commercial use is not granted. Embedded third-party components remain separately protected. If the Encyclopedia's distribution model requires commercial use, this source cannot be treated as cleared under that licence.

### 3.2 Education Systems

Current canonical records at baseline: all existing records are v1.

| Record | Current | Proposed |
|---|---:|---|
| `SRC-EDUCATION_SYSTEMS` | @1 | Keep @1 for Claim A's UNESCO right-to-education page; do not repoint it to a different page and thereby break Claim A's source identity |
| `CLM-EDUCATION_SYSTEMS-A` | @1 | Keep wording; no Claim edit proposed |
| `CLM-EDUCATION_SYSTEMS-B` | @1 | @2 only if required to align provenance to a separately approved Source for the 4A page; statement unchanged |
| `CLM-EDUCATION_SYSTEMS-C` | @1 | @2 only if the narrow Option 1 below is selected; replace broad comparative wording with a bounded statement about UNESCO's review methodology |
| `EU-EDUCATION_SYSTEMS-A` | @1 | @2 — UNESCO “The right to education”, page heading and opening statement |
| `EU-EDUCATION_SYSTEMS-B` | @1 | @2 — UNESCO “State obligations and responsibilities”, “Content of states’ obligations concerning the right to education”; requires a separate Source record for this distinct page |
| `EU-EDUCATION_SYSTEMS-C` | @1 | @2 only under Option 1; requires a separate Source record for “Education system reviews” |

**Claim A source and locator**
- UNESCO, https://www.unesco.org/en/right-education
- Locator: “The right to education” heading and opening statement on the right to quality education and lifelong learning opportunities.

**Claim B source and locator**
- UNESCO, https://www.unesco.org/en/right-education/state-obligations-responsibilities
- Locator: “Content of states’ obligations concerning the right to education”, including availability, accessibility, acceptability and adaptability.
- This is a distinct page from Claim A's current Source. A new Source record is needed; no new canonical ID is assigned in this packet.

**Claim C — recommended Option 1: narrow to a single-source methodology claim**

Proposed statement:

> Методология UNESCO по обзору образовательных систем адаптируется к приоритетам и контексту каждого государства-члена и может охватывать результаты системы, управление и финансирование, политику в отношении учителей, учебные программы и педагогику, а также согласованность системы.

- Source candidate: UNESCO, “Education system reviews”, https://www.unesco.org/en/education-policies/reviews
- Locator: page opening and “Areas commonly covered”.
- A separate Source record is required; ID remains **UNASSIGNED — do not create until the canonical ID policy and owner decision are applied**.

**Option 2 — retain the broad comparative Claim:** requires multiple independent evidence chains for law/policy (UNESCO PEER), governance/delivery (OECD PISA 2022 Volume II), curriculum/law (OECD curriculum report), and financing (OECD Education at a Glance 2026). This is a larger graph expansion and is not the default recommendation.

**Decision required:** choose Option 1 or Option 2. Do not leave the current broad Claim attached to the generic UNESCO landing page as if that single page supports all five dimensions.

## 4. Batch 8 — proposed exact changes

### 4.1 Electromagnetism Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-ELECTROMAGNETISM_BASICS` | @1→@2 | Identify OpenStax *University Physics Volume 2*, Chapter 13, “Electromagnetic Induction”; retain stable book/edition identity |
| `CLM-ELECTROMAGNETISM_BASICS-A` | @1→@2 | Replace metadata placeholder with substantive Claim A below |
| `CLM-ELECTROMAGNETISM_BASICS-B` | @1→@2 | Replace metadata placeholder with substantive Claim B below |
| `CLM-ELECTROMAGNETISM_BASICS-C` | @1→@2 | Replace metadata placeholder with substantive Claim C below |
| `EU-ELECTROMAGNETISM_BASICS-A/B/C` | each @1→@2 | Add corresponding section locator and precise conditions/support boundary |

**Proposed Claims**

A. Изменение магнитного потока через замкнутый контур вызывает индуцированную электродвижущую силу (ЭДС).

B. Направление индуцированной ЭДС соответствует такому направлению тока, при котором создаваемое им магнитное поле противодействует изменению магнитного потока, вызвавшему ЭДС.

C. Для прямого проводника длины (l), движущегося со скоростью (v) перпендикулярно однородному магнитному полю (B), модуль двигательной ЭДС равен (arepsilon = Blv).

**Evidence Use locators**
- EU A → §13.1 “Faraday’s Law”: https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
- EU B → §13.2 “Lenz’s Law”: https://openstax.org/books/university-physics-volume-2/pages/13-2-lenzs-law
- EU C → §13.3 “Motional Emf”: https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf

Claim C explicitly preserves perpendicular motion and a uniform field. Do not generalize (arepsilon=Blv) to arbitrary orientation without the angular factor.

### 4.2 Fluid Mechanics Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-FLUID_MECHANICS_BASICS` | @1→@2 | Identify OpenStax *University Physics Volume 1*, Chapter 14, “Fluid Mechanics” |
| `CLM-FLUID_MECHANICS_BASICS-A/B/C` | each @1→@2 | Replace three metadata placeholders with substantive Claims below |
| `EU-FLUID_MECHANICS_BASICS-A/B/C` | each @1→@2 | Add section-specific locators and model assumptions |

**Proposed Claims**

A. Для несжимаемой жидкости объёмный расход (Q) равен произведению площади поперечного сечения потока (A) на среднюю скорость (v): (Q=Av).

B. Для идеальной несжимаемой жидкости без вязкости вдоль линии тока сумма давления, кинетической энергии на единицу объёма и потенциальной энергии на единицу объёма остаётся постоянной.

C. Вязкость характеризует внутреннее трение в жидкости; ламинарное течение происходит слоями, а турбулентное сопровождается вихрями и перемешиванием слоёв.

**Evidence Use locators**
- EU A → §14.5 “Fluid Dynamics”: https://openstax.org/books/university-physics-volume-1/pages/14-5-fluid-dynamics
- EU B → §14.6 “Bernoulli’s Equation”: https://openstax.org/books/university-physics-volume-1/pages/14-6-bernoullis-equation
- EU C → §14.7 “Viscosity and Turbulence”: https://openstax.org/books/university-physics-volume-1/pages/14-7-viscosity-and-turbulence

Keep incompressibility and ideal-fluid assumptions explicit. Do not present Bernoulli's equation as universally applicable to viscous or compressible flows.

### 4.3 Geometry Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-GEOMETRY_BASICS` | @1→@2 | Replace mismatched Source identity with OpenStax *Contemporary Mathematics*, Chapter 10 “Geometry” |
| `CLM-GEOMETRY_BASICS-A/B` | @1→@2 | Statements unchanged; align provenance to Source @2 |
| `CLM-GEOMETRY_BASICS-C` | @1→@2 | Narrow to linear versus square units |
| `EU-GEOMETRY_BASICS-A/B/C` | each @1→@2 | Add direct section locators and exact current references |

**Proposed Claim C statement**

> Периметр выражается в линейных единицах, а площадь — в квадратных единицах.

**Evidence Use locators**
- EU A → §§10.1 “Points, Lines, and Planes”, 10.2 “Angles”, 10.3 “Triangles”.
- EU B → §10.4 “Polygons, Perimeter, and Circumference” and §10.6 “Area”.
- EU C → §§10.4 and 10.6, specifically linear perimeter units versus square area units.
- Source landing page: https://openstax.org/books/contemporary-mathematics/pages/10-introduction

**Rights:** OpenStax *Contemporary Mathematics* identifies CC BY-NC-SA 4.0. Attribution and ShareAlike apply to permitted non-commercial reuse; commercial use is not granted by this licence.

### 4.4 Governance Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-GOVERNANCE_BASICS` | @1 | Keep identity; existing OECD 2020 publication is the relevant source |
| `CLM-GOVERNANCE_BASICS-A/B` | @1 | Keep wording unless exact current record review finds an unsupported overstatement |
| `CLM-GOVERNANCE_BASICS-C` | @1→@2 | Narrow to the OECD's actual statements on country-specific strengths, national conditions and context-dependent values |
| `EU-GOVERNANCE_BASICS-A/B/C` | each @1→@2 | Add exact OECD page/figure/box locators and support boundaries |

**Proposed Claim C statement**

> Подходы к реформированию государственного управления должны учитывать национальные условия и особенности конкретного государства; применимость отдельных ценностей и инструментов зависит от контекста.

**Evidence Use locators**
- EU A → Introduction, “What is Sound Public Governance for the OECD?”, printed pp. 15–16; Box 1.1, p. 21.
- EU B → Introduction, “What is Sound Public Governance for the OECD?”, p. 15; Figure 0.2; Executive Summary, pp. 9–10.
- EU C → Foreword, p. 3; Introduction, p. 12; Chapter 1 “The Values of Sound Public Governance”, pp. 20–21.
- Official PDF: https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/12/policy-framework-on-sound-public-governance_931b05fc/c03e01b3-en.pdf

The current source supports a context-sensitive and country-specific formulation; it does not establish a universal causal rule about every governance arrangement.

**Rights:** the inspected OECD publication states © OECD 2020 and refers to OECD Terms and Conditions. No blanket CC licence was identified. Record source attribution and rights limits; do not treat this as clearance for reproduction/adaptation.

### 4.5 Historical Geography Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-HISTORICAL_GEOGRAPHY` | @1→@2 | Replace generic map-collections portal identity with LOC “Maps from the World Digital Library — Teacher’s Guide” |
| `CLM-HISTORICAL_GEOGRAPHY-A/B/C` | each @1→@2 | Statements unchanged; align provenance to Source @2 |
| `EU-HISTORICAL_GEOGRAPHY-A/B/C` | each @1→@2 | Add the direct map-analysis passages listed below |

**Evidence Use locators**
- EU A → “Maps as Primary Sources”; “A First Look at Maps”.
- EU B → “Some Types of Maps”.
- EU C → “A First Look at Maps”; “Point of View”; “Suggestions for Teachers”.
- Source: https://www.loc.gov/classroom-materials/maps-from-the-world-digital-library/

This is a methodological teaching guide. It is not a substitute for a specific historical map/catalogue item where a Claim asserts a particular event, border, settlement or historical condition. The LOC page is intended for classroom use; beyond-classroom reuse requires item-level copyright/fair-use review. Do not reproduce map images or scans under this proposal.

## 5. Batch 9 — proposed exact changes

### 5.1 Settlement Geography Basics

Current records: Source, Claims A–C and EUs A–C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-SETTLEMENT_GEOGRAPHY` | @1→@2 | Correct bibliographic identity to the joint 2021 manual by European Commission, FAO, UN-Habitat, ILO, OECD and World Bank; retain DOI and official landing/PDF URI |
| `CLM-SETTLEMENT_GEOGRAPHY-A/B/C` | each @1→@2 | Statements unchanged; align provenance to Source @2 |
| `EU-SETTLEMENT_GEOGRAPHY-A/B/C` | each @1→@2 | Add exact claim-specific locators below |

**Evidence Use locators**
- EU A → Abstract; Chapter 1 “Introduction”, p. 7; §6.2 “Short description”, pp. 33–34.
- EU B → §6.1 “Terminology” and Table 6.2, p. 33; §6.2, pp. 33–34; §6.3 “Grid cell classification”, beginning p. 34.
- EU C → Abstract; Chapter 1 “Introduction”, p. 7. Preserve the explicit statement that the method complements rather than replaces national statistical definitions.

**Source references**
- Official landing: https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas
- Official PDF: https://unhabitat.org/sites/default/files/2021/12/ks-02-20-499-en-n.pdf
- DOI: https://doi.org/10.2785/706535

**Rights:** CC BY-NC-SA 3.0 IGO; non-commercial only, attribution and ShareAlike conditions apply. Third-party cover photography and maps are excluded from the blanket grant. No map/image reuse is proposed.

### 5.2 Antimicrobial Resistance Basics

Current records: Source, Claim C and EU C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-ANTIMICROBIAL_RESISTANCE_BASICS` | @1→@2 | Record WHO fact-sheet identity and inspected update date 16 July 2026; preserve official URI |
| `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C` | @1→@2 | Statement unchanged; align provenance to Source @2 |
| `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C` | @1→@2 | Pin exact headings and explain the direct support boundary |

**Evidence Use locator**
- “Overview”
- “A global concern”
- “WHO response” — GAP-AMR 2026–2036, One Health, agrifood systems and environmental pollution paragraphs; six strategic objectives.
- Source: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- Inspection/update date: 16 July 2026.

The WHO page supports the human, animal, plant, agrifood and environmental dimensions and multisectoral response described in the current Claim. Do not imply exhaustive coverage of every organism, sector or transmission pathway. Public accessibility is not a republication licence; source-specific rights review remains open.

### 5.3 Statistics Basics

Current records: Source, Claim C and EU C are all v1.

| Record | Proposed version | Proposed change |
|---|---:|---|
| `SRC-STATISTICS_BASICS` | @1 | Keep source identity; no Source change proposed |
| `CLM-STATISTICS_BASICS-C` | @1→@2 | Narrow statement to the design-to-valid-conclusion proposition below |
| `EU-STATISTICS_BASICS-C` | @1→@2 | Pin NIST/SEMATECH §4.3.1 and state exactly what it supports |

**Proposed Claim C statement**

> Планирование эксперимента применяет статистические принципы на этапе сбора данных, чтобы повысить обоснованность и проверяемость инженерных выводов.

**Evidence Use locator**
- Chapter 4 “Process Modeling” → §4.3 “Data Collection for Process Modeling” → §4.3.1 “What is design of experiments (DOE)?”
- Official section: https://itl.nist.gov/div898/handbook/pmd/section3/pmd31.htm
- Handbook landing: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook

The source supports the connection between experimental design at data collection and valid, defensible, supportable engineering conclusions. It does not itself establish a direct comparison against calculations; do not preserve that comparative wording without additional evidence. The handbook is a joint NIST/SEMATECH publication; do not infer that every component is public domain solely because NIST is a U.S. federal agency. Complete item-level rights/attribution review.

## 6. Exact dependency and versioning rules for implementation

If and only if the relevant bounded authorization is approved, implementation must follow these rules:

1. Freeze one exact branch HEAD and re-fetch every affected canonical JSON at that HEAD immediately before editing.
2. Preserve canonical Record IDs and record types. Do not allocate new IDs ad hoc.
3. For each Source v1→v2 change, version every Claim whose `provenance.created_from` points to that Source if the reference must advance. Version dependent Evidence Use records to current Claim and Source references.
4. For any Claim statement change, increment that Claim version and update only the dependent Evidence Use references and target-specific Context/Scope references required by the schema.
5. Do not add a third Evidence Use base role. The Evidence Use Standard permits `supports` and `contradicts`; source context or methodological background must not be represented as direct support when it does not support the target proposition.
6. Context and Scope records target Claim A in these slice models. Do not imply that they apply to Claims B/C without an explicit schema/policy basis.
7. Preserve `publication_status` and `completion_status`. Do not create or alter the first-edition allowlist. Every slice in this packet remains HOLD.
8. Update only the explicitly authorized slice READMEs and the relevant remediation/register documentation. Do not modify Relations unless a separate exact-record authorization names them.
9. Add focused regression assertions only for changed identity/version references, locators or support boundaries. Do not modify validator, storage, recovery or release-gate semantics under this content authorization.
10. Re-run exact graph preflight, affected-slice tests and the full required release checks on one immutable final HEAD. A passing structural test does not establish truth, rights clearance or publication eligibility.

## 7. Rights, editorial and release blockers that remain open

- AAA *Perspectives* and OpenStax sources carry non-commercial licence limits; compatibility with the eventual project distribution model is unresolved.
- OpenStax University Physics prefaces include a restriction on LLM ingestion/AI offerings without prior written permission; obtain an owner/legal decision before treating the source as usable within the project's AI-assisted production context.
- OECD publication terms require source-specific review; no blanket open licence is asserted.
- LOC classroom materials and individual map items require item-level review for reuse beyond classroom use.
- The joint UN-Habitat/EC/FAO/ILO/OECD/World Bank manual carries CC BY-NC-SA 3.0 IGO and excludes third-party cover/map material from the blanket grant.
- WHO fact-sheet public accessibility is not a reuse licence.
- NIST/SEMATECH joint publication rights must be reviewed for the exact handbook content.
- Education Systems needs a source-record design decision for its distinct UNESCO pages and an explicit Claim C scope choice.
- All 10 slices require independent subject/editorial review and Human View in the rendered reader before any release decision.
- Project-level rights holder, content/data licence, software boundary, contributor terms, editorial owner, release approver, correction/withdrawal contact, attribution policy and rights-evidence storage remain governed by the separate owner-decision register.

## 8. Execution order

1. **Low-risk locator work:** Governance A/B and Historical Geography A–C; then Cultural Anthropology A/C and Education A, subject to exact source/rights checks.
2. **Source identity and locator work:** Settlement Geography and AMR; retain their non-commercial/rights boundaries.
3. **Claim refinements:** Cultural Anthropology B, Governance C, Geometry C and Statistics C.
4. **High-substance Claim replacements:** Electromagnetism A–C and Fluid Mechanics A–C, after subject-matter review.
5. **Education Systems:** owner/editor selects the narrow single-source method claim or authorizes the broader multi-source graph before any canonical edit.
6. After all approved changes, perform one consolidated exact-version graph check, update the exact-version candidate register and remediation record, and preserve HOLD.

## 9. Explicit non-actions

This packet does **not**:
- authorize or perform any canonical Claim, Evidence Use, Source, Context or Scope change;
- authorize new canonical Source IDs;
- change any Claim wording or version;
- change any publication/completion status;
- change any INCLUDE/HOLD/EXCLUDE disposition;
- create or modify a public or private preview allowlist;
- approve rights, licensing, legal correctness, scientific correctness or publication;
- change `main`, merge PR #22, deploy, or launch a public edition.

**Decision requested from project owner:** approve, reject or amend the bounded scope slice-by-slice. Silence or a general instruction to continue is not treated as permission to exceed existing canonical change controls.
