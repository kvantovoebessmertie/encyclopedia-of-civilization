# M13 — bounded remediation proposal: environmental economics, epidemiology and food distribution

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Proposal baseline HEAD: `afaf338cdbee3d6765adefb4c3b386028635121a`

## 1. Purpose and boundary

This is a noncanonical, evidence-backed remediation proposal for three unresolved findings from Unassessed-Risk Content Screen Package 28.

It does not authorize canonical writes. No Claim, Evidence Use, Source, Context, Scope or Relation JSON is changed by this document. No official D/E/B score is assigned or changed. All three Claims remain HOLD. Rights, specialist, independent-review, Human View and publication gates remain separate.

The purpose is to replace vague remediation instructions with exact source candidates, reproducible locators, proposed Claim boundaries and required validation.

## 2. Environmental Economics C

### Current canonical state

- Claim: `CLM-ENVIRONMENTAL_ECONOMICS_BASICS-C@1`
- Evidence Use: `EU-ENVIRONMENTAL_ECONOMICS_BASICS-C@1`
- Source: `SRC-ENVIRONMENTAL_ECONOMICS_BASICS@1`
- Current Claim: “Оценка экологической политики зависит от выбранных целей, временного горизонта, данных и метода оценки.”
- Current Source identity: “World Bank — Environment”; URI: `https://www.worldbank.org/en/topic/environment`
- Current EU has no claim-specific locator.

### Finding

The broad World Bank Environment landing page does not establish the full methodology proposition. A directly inspectable World Bank Group guide provides bounded support for evaluation of integrated land-use initiatives, not for every form of environmental policy.

### Proposed source

World Bank. 2021. *Toward a Holistic Approach to Sustainable Development: A Guide to Integrated Land-Use Initiatives*. Report No. P171124.  
URI: `https://documents1.worldbank.org/curated/en/831591628501365387/pdf/Toward-a-Holistic-Approach-to-Sustainable-Development-A-Guide-to-Integrated-Land-Use-Initiatives.pdf`

Exact locators:
- Chapter 2.7, “Monitoring, Evaluation, and Learning”, printed pp. 38–43.
- Subsection “A. Develop a monitoring and evaluation strategy”: the purpose/objectives of the framework determine which indicators are included, how data are gathered and what MRV framework is designed.
- Overview of §2.7: long-term impact measures and short-term process indicators are both needed for initiatives with multiple goals and scales.
- Subsection “i. Identify Tools and Methods”: identifies tools/methods for data collection and analysis.

### Bounded proposal

Do not retain the universal phrase “экологической политики” on the strength of this one guide. Prepare a versioned Claim proposal narrowed to integrated land-use initiatives, for example:

“При оценке интегрированных инициатив по землепользованию цели и масштаб инициативы влияют на выбор показателей: для оценки используются как долгосрочные показатели воздействия, так и краткосрочные показатели процессов.”

Prepare a distinct Source record for the World Bank guide and a distinct Evidence Use link with the exact §2.7 locators. Keep the existing broad Environment Source separate; do not silently redefine its identity or URI.

### Rights and validation

The guide states that non-commercial reproduction is permitted with full attribution, while other rights/licensing queries are directed to World Bank Publications. This is not blanket permission for unrestricted adaptation, ingestion or redistribution. Record rights review as OPEN. Validate source title, report number, section and locator against the PDF before any authorization.

## 3. Epidemiology A

### Current canonical state

- Claim: `CLM-EPIDEMIOLOGY_BASICS-A@1`
- Evidence Use: `EU-EPIDEMIOLOGY_BASICS-A@1`
- Source: `SRC-EPIDEMIOLOGY_BASICS@1`
- Current Claim: “Срез epidemiology-basics описывает базовые понятия предметной области и их взаимосвязи.”
- Current Source identity: “CDC — Principles of Epidemiology”; URI: `https://www.cdc.gov/training-publichealth101/php/lessons/principles-of-epidemiology.html`

### Finding

The current Claim is a meta-description of the slice, not a discrete, falsifiable proposition. The current Evidence Use repeats that description; it cannot turn the meta-description into a substantive epidemiological Claim.

### Proposed source and locator

CDC, *Principles of Epidemiology*, Lesson 1: Introduction to Epidemiology, Section 1: “Definition of Epidemiology”.  
URI: `https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html`

The archived page gives the standard definition at the opening of Section 1 and explains its terms under “Distribution”, “Determinants”, “Health-related states or events”, “Specified populations” and “Application”. It records “Last Reviewed: May 18, 2012”; preserve that historical/version context rather than presenting it as a newly updated CDC page.

### Bounded proposal

Replace the meta-description with a substantive, falsifiable definition, for example:

“Эпидемиология изучает распределение и детерминанты состояний и событий, связанных со здоровьем, в определённых популяциях, а также применение этих знаний для контроля проблем здоровья.”

Register the archived CDC lesson as a distinct Source unless the current Source is proven to identify this exact archived edition. Create a claim-specific Evidence Use locator to Lesson 1, Section 1, opening definition, with supporting subsections as needed. Do not silently change the existing Source URI.

### Rights and validation

The cited CDC archive page is publicly accessible, but this proposal does not infer an unrestricted reuse licence. Verify source identity and any applicable reuse terms before reproducing substantial text or media. Keep rights status OPEN.

## 4. Food Distribution C

### Current canonical state

- Claim: `CLM-FOOD_DISTRIBUTION_BASICS-C@1`
- Evidence Use: `EU-FOOD_DISTRIBUTION_BASICS-C@1`
- Source: `SRC-FOOD_DISTRIBUTION_BASICS@1`
- Current Claim: “Доступность продовольствия в конкретном месте не определяется только объёмом производства.”
- Current Source identity: “FAO — Food Systems”; URI: `https://www.fao.org/food-systems/en/`
- Current EU has no claim-specific locator.

### Finding

The FAO Food Systems hub is a broad entry point. The proposition is directly supported by a more specific FAO High Level Panel of Experts report, which distinguishes food availability from physical and economic access and describes storage/distribution, transport infrastructure and markets as separate elements of food systems.

### Proposed source and locators

High Level Panel of Experts on Food Security and Nutrition (HLPE). 2017. *Nutrition and food systems*. HLPE Report 12.  
URI: `https://www.fao.org/fileadmin/user_upload/hlpe/hlpe_documents/HLPE_Reports/HLPE-Report-12_EN.pdf`

Exact locators:
- Chapter 1, §1.2.1 “Food supply chains”, printed p. 24: the chain includes production; storage and distribution; processing and packaging; retail and markets. Decisions at one stage affect others and the dimensions of food security.
- Chapter 1, §1.2.2 “Food environments”, printed p. 28: food availability at national/international level does not itself guarantee food security at community/household level; physical and economic access also matter.
- Chapter 5, §5.1.2 “Storage and distribution”, printed pp. 88–89: storage and distribution affect access to safe and nutritious food; inadequate storage, transport conditions and infrastructure contribute to food losses and waste.

### Bounded proposal

The existing wording is directionally supported, but can be made more precise and directly testable. Proposed versioned Claim wording:

“Наличие продовольствия на национальном или международном уровне само по себе не гарантирует продовольственную безопасность на уровне сообщества или домохозяйства: важны также физический и экономический доступ.”

Register HLPE Report 12 as a distinct Source and add a distinct Evidence Use link with the §1.2.2 locator. If the slice also intends to explain supply-chain mechanisms, use separate locators/Evidence Use links for §1.2.1 and §5.1.2 rather than implying that one passage establishes every mechanism.

### Rights and validation

The report says non-commercial uses are authorized free of charge upon request; reproduction for resale or other commercial purposes may incur fees. Public access is not blanket permission for unrestricted reuse or AI ingestion. Keep rights status OPEN and record the required permission/attribution decision before reuse.

## 5. Proposed bounded work package and acceptance

| Claim | Proposed action | Canonical write now |
|---|---|---|
| Environmental Economics C | New specific World Bank Source; exact §2.7 locator; narrow Claim scope | NO — authorization required |
| Epidemiology A | Replace meta-description with epidemiology definition; register exact CDC archived lesson edition and locator | NO — authorization required |
| Food Distribution C | New FAO HLPE Report 12 Source; exact §1.2.2 locator; refine Claim boundary | NO — authorization required |

Before any canonical update:
1. Re-fetch all current Claim/EU/Source files and confirm their blob SHAs still match this proposal baseline.
2. Check the applicable Record, Source, Evidence Use and editorial-correction standards.
3. Create an exact bounded correction authorization naming each record, permitted fields, proposed versions and regression tests.
4. Preserve old versions and source identities; do not repoint an existing Source to a different publication.
5. Add regression tests for exact Claim/EU/Source refs, source identity, pinpoint text, scope limits and rights/HOLD separation.
6. Run local schema/reference/regression checks after the authorized batch; then run Reference Tests, Release Conformance Gate and Offline Edition on one exact final HEAD.
7. Independently verify the diff, base, PR state and unchanged `main`.

## 6. Evidence reviewed

- World Bank guide, §2.7 and subsection A: `https://documents1.worldbank.org/curated/en/831591628501365387/pdf/Toward-a-Holistic-Approach-to-Sustainable-Development-A-Guide-to-Integrated-Land-Use-Initiatives.pdf`
- CDC, *Principles of Epidemiology*, Lesson 1, Section 1: `https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html`
- FAO HLPE Report 12, §§1.2.1, 1.2.2 and 5.1.2: `https://www.fao.org/fileadmin/user_upload/hlpe/hlpe_documents/HLPE_Reports/HLPE-Report-12_EN.pdf`

**Disposition:** proposal only; all three Claims remain HOLD; canonical_write_permitted = NO; no D/E/B change; no rights, specialist, independent-review, Human View or publication clearance.
