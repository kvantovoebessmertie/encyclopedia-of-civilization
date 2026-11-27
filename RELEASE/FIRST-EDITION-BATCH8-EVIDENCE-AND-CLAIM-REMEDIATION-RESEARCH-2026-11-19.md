# First Edition — Batch 8 Evidence and Claim Remediation Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection baseline: `846cefd71ae320f0aa8d39b93507ac78f2d591bf`  
Audit: `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH8-2026-11-19.md`  
Status: **15/15 LOCATOR / SOURCE / CLAIM REMEDIATION ROUTES RESEARCHED; 6 PLACEHOLDER CLAIM REPLACEMENT PROPOSALS; ALL HOLD; NO CANONICAL CHANGE AUTHORIZED**

## 1. Purpose and controls

Batch 8 verified 15 exact Claim→Evidence Use→Source chains, but none of the 15 EUs had a claim-specific locator. This dossier supplies a bounded remediation route for all five slices:

- electromagnetism-basics — three generic placeholder Claims;
- fluid-mechanics-basics — three generic placeholder Claims;
- geometry-basics — three substantive Claims with a Source identity/fit mismatch;
- governance-basics — three substantive Claims needing exact OECD locators;
- historical-geography-basics — three substantive Claims needing direct map-analysis passages.

All recommendations are research only.

- No canonical Claim, Evidence Use, Source, Context, Scope or Relation was changed.
- No record ID or version was changed.
- No INCLUDE or EXCLUDE decision was made.
- All 15 Claims remain HOLD.
- No source's access status is treated as a reuse licence.
- Any canonical edit requires bounded authorization, exact proposed diff, rights review and independent review.

## 2. Electromagnetism — replace three metadata placeholders with subject Claims

Current Source: OpenStax *University Physics Volume 2*, Chapter 13, “Electromagnetic Induction”. The current Source URI points only to the Chapter 13 introduction; use the exact section locators below.

| Existing Claim | Proposed substantive proposition for owner/editor review | Direct locator |
|---|---|---|
| `CLM-ELECTROMAGNETISM_BASICS-A@1` | Изменение магнитного потока через замкнутый контур вызывает индуцированную электродвижущую силу (ЭДС). | §13.1 “Faraday’s Law” — https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law |
| `CLM-ELECTROMAGNETISM_BASICS-B@1` | Направление индуцированной ЭДС соответствует такому направлению тока, при котором создаваемое им магнитное поле противодействует изменению магнитного потока, вызвавшему ЭДС. | §13.2 “Lenz’s Law” — https://openstax.org/books/university-physics-volume-2/pages/13-2-lenzs-law |
| `CLM-ELECTROMAGNETISM_BASICS-C@1` | Для прямого проводника длины (l), движущегося со скоростью (v) перпендикулярно однородному магнитному полю (B), модуль двигательной ЭДС равен (arepsilon = Blv). | §13.3 “Motional Emf” — https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf |

**Assessment:** these are real, falsifiable physics propositions and match the chapter subject far better than the current generic slice-introduction, context caveat and specialist-verification statements. The proposed third Claim deliberately states the perpendicular-motion condition so that the simple (arepsilon=Blv) formula is not overgeneralized; for arbitrary orientation the angular factor must be considered.

**Rights:** the current OpenStax online preface states CC BY-NC-SA 4.0 and also says the book may not be used for LLM training/ingestion or generative-AI offerings without prior written permission. Non-commercial reuse requires attribution and ShareAlike; commercial use requires permission. The project distribution model and AI policy remain owner decisions. No diagrams or other third-party artwork are proposed for reuse.

## 3. Fluid mechanics — replace three metadata placeholders with subject Claims

Current Source: OpenStax *University Physics Volume 1*, Chapter 14, “Fluid Mechanics”. The current Source URI points to §14.5, but the three proposed Claims need different direct sections.

| Existing Claim | Proposed substantive proposition for owner/editor review | Direct locator |
|---|---|---|
| `CLM-FLUID_MECHANICS_BASICS-A@1` | Для несжимаемой жидкости объёмный расход (Q) равен произведению площади поперечного сечения потока (A) на среднюю скорость (v): (Q=Av). | §14.5 “Fluid Dynamics” — https://openstax.org/books/university-physics-volume-1/pages/14-5-fluid-dynamics |
| `CLM-FLUID_MECHANICS_BASICS-B@1` | Для идеальной несжимаемой жидкости без вязкости вдоль линии тока сумма давления, кинетической энергии на единицу объёма и потенциальной энергии на единицу объёма остаётся постоянной. | §14.6 “Bernoulli’s Equation” — https://openstax.org/books/university-physics-volume-1/pages/14-6-bernoullis-equation |
| `CLM-FLUID_MECHANICS_BASICS-C@1` | Вязкость характеризует внутреннее трение в жидкости; ламинарное течение происходит слоями, а турбулентное сопровождается вихрями и перемешиванием слоёв. | §14.7 “Viscosity and Turbulence” — https://openstax.org/books/university-physics-volume-1/pages/14-7-viscosity-and-turbulence |

**Assessment:** all three proposed propositions have direct section-level support. Keep the incompressibility and ideal-fluid assumptions explicit in Claims/EUs; do not generalize Bernoulli’s equation to viscous or compressible flow without the corresponding model conditions.

**Rights:** the current OpenStax University Physics online preface identifies CC BY-NC-SA 4.0 and restricts LLM ingestion/AI offerings without prior written permission. Attribution and ShareAlike are required for non-commercial reuse; commercial reuse requires permission. Item/version rights must be checked against the exact current book edition.

## 4. Geometry — substantive Claims retained; replace the mismatched Source identity

Current Source record identity says “Геометрия изучает формы, размеры и пространственные отношения” and points to the introduction of OpenStax *Precalculus 2e* Chapter 10. That URL is not a suitable general-geometry source for all three current Claims.

**Recommended Source identity for owner review:** OpenStax, *Contemporary Mathematics*, Chapter 10 “Geometry”, sections 10.1–10.6.  
Book chapter: https://openstax.org/books/contemporary-mathematics/pages/10-introduction

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| `CLM-GEOMETRY_BASICS-A@1` / `EU-GEOMETRY_BASICS-A@1` | Геометрические объекты описываются через точки, линии, углы и фигуры. | §10.1 “Points, Lines, and Planes”; §10.2 “Angles”; §10.3 “Triangles”. | Direct support. |
| `CLM-GEOMETRY_BASICS-B@1` / `EU-GEOMETRY_BASICS-B@1` | Периметр характеризует длину границы плоской фигуры, а площадь — размер её области. | §10.4 “Polygons, Perimeter, and Circumference”; §10.6 “Area”. | Direct support. |
| `CLM-GEOMETRY_BASICS-C@1` / `EU-GEOMETRY_BASICS-C@1` | Измерительные свойства фигуры зависят от выбранных определений и единиц. | §10.4 and §10.6, including the distinction between linear perimeter units and square area units. | Current wording is too abstract. Consider narrowing to: “Периметр выражается в линейных единицах, а площадь — в квадратных единицах.” |

**Rights:** OpenStax *Contemporary Mathematics* is identified in its preface as CC BY-NC-SA 4.0. Non-commercial use requires attribution and ShareAlike; commercial use is not granted by that licence. The project distribution model remains unresolved.

## 5. Governance — direct OECD section locators

Current Source: OECD (2020), *Policy Framework on Sound Public Governance: Baseline Features of Governments that Work Well*. The Source URI is appropriate; the three EUs need specific locators.

Official PDF: https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/12/policy-framework-on-sound-public-governance_931b05fc/c03e01b3-en.pdf  
Official full report: https://www.oecd.org/en/publications/policy-framework-on-sound-public-governance_c03e01b3-en/full-report.html

| Claim / EU | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| `CLM-GOVERNANCE_BASICS-A@1` / `EU-GOVERNANCE_BASICS-A@1` | Public governance concerns how governments structure decision-making, relationships and policy implementation. | Introduction, “What is Sound Public Governance for the OECD?”, printed pp. 15–16; definition in Box 1.1, printed p. 21. | Direct support: formal/informal rules, procedures, practices and interactions within the State and between State, non-state institutions and citizens frame public authority and decision-making in the public interest. |
| `CLM-GOVERNANCE_BASICS-B@1` / `EU-GOVERNANCE_BASICS-B@1` | OECD describes governance through interconnected values, enablers, and policy instruments and tools. | Introduction, “What is Sound Public Governance for the OECD?”, printed p. 15; Figure 0.2; Executive Summary, printed pp. 9–10. | Direct support for the three-element framework. |
| `CLM-GOVERNANCE_BASICS-C@1` / `EU-GOVERNANCE_BASICS-C@1` | Governance arrangements vary across institutional and national contexts. | Foreword, printed p. 3; Introduction, printed p. 12; Chapter 1 “The Values of Sound Public Governance”, printed pp. 20–21. | Partial support. OECD notes each government has distinct strengths/areas for improvement, reforms should reflect national conditions, and governance values are context-dependent. Consider narrowing the Claim to those precise statements rather than asserting a broad rule about all governance arrangements. |

**Rights:** the PDF states © OECD 2020 and that use is governed by OECD Terms and Conditions; no blanket CC licence is stated in the inspected publication front matter. Treat this as rights-screened but not cleared for reproduction/adaptation until the exact terms and intended use are reviewed.

## 6. Historical geography — direct Library of Congress map-analysis guide

The current Source points to the general LOC map collections portal. A better direct source for these three methodological Claims is the Library of Congress classroom resource **“Maps from the World Digital Library — Teacher’s Guide”**:

https://www.loc.gov/classroom-materials/maps-from-the-world-digital-library/

| Claim / EU | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| `CLM-HISTORICAL_GEOGRAPHY-A@1` / `EU-HISTORICAL_GEOGRAPHY-A@1` | Исторические карты являются источниками пространственной информации, связанной с определённым временем и местом. | Teacher’s Guide, “Maps as Primary Sources”; “A First Look at Maps”. | Direct support: maps represent places at particular times and can serve as primary sources for studying change over time and the people who made them. |
| `CLM-HISTORICAL_GEOGRAPHY-B@1` / `EU-HISTORICAL_GEOGRAPHY-B@1` | Картографические материалы могут показывать физическую среду и культурные элементы территории в конкретный исторический момент. | Teacher’s Guide, “Some Types of Maps”. | Direct support: panoramic maps may show terrain, landscape features, streets, buildings, transport, parks and educational/religious facilities; other map types record settlement, migration, communication and transport networks. |
| `CLM-HISTORICAL_GEOGRAPHY-C@1` / `EU-HISTORICAL_GEOGRAPHY-C@1` | Интерпретация исторической карты зависит от даты, масштаба, происхождения и назначения материала. | Teacher’s Guide, “A First Look at Maps”; “Point of View”; “Suggestions for Teachers”. | Direct support: title/date, author/source, scale, map purpose, detail, chronology and point of view are all identified as interpretation factors. |

The LOC resource is a teaching guide, not a substitute for the specific historical map itself when a Claim asserts a particular event, border, settlement or historical condition. For such claims, add the exact map item/catalog record as the evidence source. The LOC page says its primary-source set is intended for classroom use and asks users to review copyright/fair-use guidance for use beyond a single classroom. Do not reuse map images or scans without item-level rights checks.

## 7. Consolidated remediation decisions

| Slice | Research result | Canonical work still required | Disposition |
|---|---|---|---|
| Electromagnetism | 3 direct section locators; 3 substantive Claim proposals | Replace three metadata placeholders, add EU locators, verify conditions and rights | HOLD |
| Fluid mechanics | 3 direct section locators; 3 substantive Claim proposals | Replace three metadata placeholders, add EU locators, verify assumptions and rights | HOLD |
| Geometry | 3 direct locator candidates | Correct Source identity/URI; add EU locators; narrow Claim C | HOLD |
| Governance | 3 direct locator candidates | Add EU locators; narrow Claim C; complete OECD rights decision | HOLD |
| Historical geography | 3 direct locator candidates | Replace generic Source with the LOC map-analysis guide or a more suitable pinned source; add EU locators; check item-level map rights | HOLD |

## 8. Recommended execution order after authorization

1. **Governance and Historical Geography:** low-risk locator-only changes can be proposed first, with a bounded Source/EU diff and rights note.
2. **Geometry:** correct the Source identity/URI and add locators; narrow Claim C only with explicit approval.
3. **Electromagnetism and Fluid Mechanics:** prepare six exact Claim replacement proposals and six EU locator changes; require subject-matter review before any canonical edit.
4. Re-fetch all affected records at one frozen HEAD; validate exact IDs, versions, types, Claim→EU→Source references and Context/Scope applicability.
5. Preserve HOLD until rights, independent review, Human View and high-consequence gates are closed.
6. Run affected slice tests and all release gates on the final immutable HEAD after any authorized canonical changes.

## 9. Final result

- Batch 8 Claims: **15/15** reviewed for a concrete remediation route.
- Direct locator candidates: **15/15**.
- Generic placeholder Claims with replacement proposals: **6/6**.
- Source identity/fit corrections proposed: **2** (Geometry and Historical Geography).
- Claim wording narrowing proposals: **2** (Governance C and Geometry C).
- Canonical records changed: **0**.
- INCLUDE / EXCLUDE decisions: **0 / 0**.
- Disposition: **15/15 HOLD pending authorization, canonical implementation, rights review and independent subject/editorial review**.
