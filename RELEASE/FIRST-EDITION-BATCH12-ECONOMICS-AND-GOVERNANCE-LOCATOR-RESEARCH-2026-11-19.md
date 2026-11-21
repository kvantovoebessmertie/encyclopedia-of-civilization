# First Edition — Batch 12 Economics, Money, Organizations and Public Budgeting Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `257ce340e097993850dddd98b8e4fff46de4b6ef`  
Status: **15 CANDIDATE CLAIMS / 15 EUS RESEARCHED ACROSS FIVE SLICES; DIRECT LOCATOR CANDIDATES FOUND; SOURCE-GRAPH EXPANSION AND CLAIM NARROWING IDENTIFIED; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Batch 12 selects 15 Claims from five candidate slices present in the exact-version master and not covered by Batches 1–11 or active bounded authorizations:

- macroeconomics-basics — Claims A–C;
- microeconomics-basics — Claims A–C;
- money-and-banking-basics — Claims A–C;
- organizational-behavior-basics — Claims A–C;
- public-budgeting-basics — Claims A–C.

All 15 Claim records, 15 Evidence Use records and five current Source records were re-fetched from the current PR branch and confirmed present in the exact-version master. The EUs use generic descriptions and do not contain claim-specific `material.locator` values.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All five slices remain HOLD.

## 2. Aggregate findings

| Slice | Claims / EUs | Result |
|---|---:|---|
| macroeconomics-basics | 3 / 3 | IMF Back to Basics GDP, inflation and unemployment articles provide direct locators; narrow inflation wording |
| microeconomics-basics | 3 / 3 | OpenStax Principles of Economics 3e §§3.1–3.2 directly support demand, supply and equilibrium; narrow Claim C |
| money-and-banking-basics | 3 / 3 | Federal Reserve 2026 note directly supports monetary aggregates/liquidity for B/C; Claim A needs an additional IMF “What Is Money?” source |
| organizational-behavior-basics | 3 / 3 | Current APA Source is less direct than OpenStax Organizational Behavior; §§1.4, 7.1, 11.1 and 16.1 support the Claims after Source correction |
| public-budgeting-basics | 3 / 3 | OECD Budgetary Governance Recommendation, PEFA Framework and IMF PFM Guidelines provide direct locators; current single IMF portal Source is too broad for the full graph |

**Total:** 15 Claims / 15 EUs / five existing Sources. No new canonical dependency records were created or discovered.

## 3. Macroeconomics Basics — Claims A–C

Current records:
- `CLM-MACROECONOMICS_BASICS-A/B/C@1`
- `EU-MACROECONOMICS_BASICS-A/B/C@1`
- `SRC-MACROECONOMICS_BASICS@1`

Current Source identity: IMF Finance & Development “Back to Basics” series. The source is appropriate, but each EU needs exact article-level locators.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Macroeconomics examines aggregate indicators such as production, income, employment and prices | IMF Back to Basics: “Gross Domestic Product: An Economy’s All” → “Measuring GDP” and production/income approaches; “Unemployment: The Curse of Joblessness” opening; “Inflation: Prices on the Rise” opening definition |
| B | GDP measures the market value of final goods and services produced within a country over a period | IMF “Gross Domestic Product: An Economy’s All” → “Measuring GDP” |
| C | Inflation is a sustained increase in the general price level | IMF “Inflation: Prices on the Rise” → “What is inflation and how it is measured” |

Sources:
- IMF Back to Basics series: https://www.imf.org/external/pubs/ft/fandd/basics/index-0629.htm
- GDP: https://www.imf.org/en/Publications/fandd/issues/Series/Back-to-Basics/gross-domestic-product-gdp
- Unemployment: https://www.imf.org/external/pubs/ft/fandd/basics/unemploy.htm
- Inflation: https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/inflation

**Claim B wording boundary:** IMF defines GDP as the *monetary value* of final goods and services produced in a country during a period. The current phrase “market value” may overstate the market-only boundary because GDP includes certain non-market government services (for example, defense and education). Recommended narrowing:

> ВВП измеряет денежную стоимость конечных товаров и услуг, произведённых внутри страны за определённый период.

**Claim C wording boundary:** IMF defines inflation as the rate of increase in prices over a given period, usually measured through a broad price index. The word “sustained” is not necessary for the direct definition. Recommended narrowing:

> Инфляция — это темп роста общего уровня цен за определённый период времени.

Claim A can retain its aggregate-indicator wording if the EU lists all three direct IMF articles. GDP provides production and income approaches; unemployment provides the employment indicator; inflation provides the price-level indicator. Do not imply that GDP alone measures employment or prices.

Rights: IMF Finance & Development articles are copyrighted publications. Use source-specific attribution and factual paraphrase; do not reproduce article text or images without permission.

## 4. Microeconomics Basics — Claims A–C

Current records:
- `CLM-MICROECONOMICS_BASICS-A/B/C@1`
- `EU-MICROECONOMICS_BASICS-A/B/C@1`
- `SRC-MICROECONOMICS_BASICS@1`

The current OpenStax *Principles of Economics 3e* Source is appropriate. The EUs need exact sections.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Demand and supply describe relationships between prices and quantities demanded/supplied | §3.1 “Demand, Supply, and Equilibrium in Markets for Goods and Services” → “Demand for Goods and Services” and “Supply of Goods and Services” |
| B | Markets coordinate buyer and seller decisions through exchange and prices | §3.1 → “Equilibrium Price and Quantity”; §3.5 “Demand, Supply, and Efficiency” for market adjustment/efficiency |
| C | Market equilibrium depends on demand, supply and the chosen market definition | §3.1 → equilibrium price and quantity; §3.2 “Shifts in Demand and Supply for Goods and Services” → ceteris paribus and market-wide shifts |

Sources:
- §3.1: https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- §3.2: https://openstax.org/books/principles-economics-3e/pages/3-2-shifts-in-demand-and-supply-for-goods-and-services
- §3.5: https://openstax.org/books/principles-economics-3e/pages/3-5-demand-supply-and-efficiency

Claim C is too broad as currently worded. Recommended narrowing:

> Рыночное равновесие достигается при цене, при которой количество товара, которое покупатели готовы приобрести, равно количеству, которое продавцы готовы предложить.

The direct source defines equilibrium as the intersection of supply and demand where quantity demanded equals quantity supplied. The chosen market boundary matters analytically, but the cited section does not establish a general rule about all possible market-definition choices. If that clause is retained, add a source on market definition and scope.

Rights: OpenStax *Principles of Economics 3e* is CC BY 4.0 in the current book preface; attribution is required and third-party components may be excluded. Verify the exact current preface and do not reproduce third-party figures.

## 5. Money and Banking Basics — Claims A–C

Current records:
- `CLM-MONEY_AND_BANKING_BASICS-A/B/C@1`
- `EU-MONEY_AND_BANKING_BASICS-A/B/C@1`
- `SRC-MONEY_AND_BANKING_BASICS@1`

Current Source: Federal Reserve FEDS Note, “New Forms of Money and the U.S. Monetary Aggregates” (September 4, 2026). This is a strong source for B/C, but it is not the clearest general source for the three traditional functions of money in Claim A.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Money serves as a medium of exchange, unit of account and store of value | IMF “What Is Money?” → opening definition and three functions |
| B | Monetary aggregates classify monetary and near-money assets by liquidity and function | Federal Reserve FEDS Note → “Overview” and “Background on the U.S. Monetary Aggregates” |
| C | Different forms of money and financial assets differ in liquidity and use | Federal Reserve FEDS Note → M1 as the narrowest/most liquid transaction measure; M2 as M1 plus less-liquid savings-type assets; “Part 1: Functional Classification” |

Sources:
- IMF, “What Is Money?”: https://www.imf.org/external/pubs/ft/fandd/2012/09/basics.htm
- Federal Reserve FEDS Note (September 4, 2026): https://www.federalreserve.gov/econres/notes/feds-notes/new-forms-of-money-and-the-u-s-monetary-aggregates-20260904.html

**Source graph requirement:** add a separate IMF Source/Evidence Use chain for Claim A under canonical ID allocation. Keep the existing Federal Reserve Source for B/C. Do not repoint the Federal Reserve Source to the IMF article or combine two publishers in one Source record.

Support boundary: the Federal Reserve note concerns U.S. monetary aggregates and current U.S. classifications (monetary base, M1, M2). Do not generalize those exact aggregate definitions to every country. Claim C should explicitly retain the U.S. scope if it names M1/M2.

Rights: Federal Reserve and IMF publications require source-specific attribution/reuse review. Public access does not automatically permit reproduction of figures or third-party material.

## 6. Organizational Behavior Basics — Claims A–C

Current records:
- `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-A/B/C@1`
- `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-A/B/C@1`
- `SRC-ORGANIZATIONAL_BEHAVIOR_BASICS@1`

The current Source points to an APA organizational-psychology page. That is relevant background, but OpenStax *Organizational Behavior* directly matches the three Claims and provides exact chapter/section locators.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Organizational behavior studies how individuals, groups and organizational structures influence behavior in organizations | §1.4 “A Model of Organizational Behavior and Management” → “What Is Organizational Behavior?” and “Building Blocks of Organizations” |
| B | Motivation, communication and task/organizational structure influence workplace behavior | §7.1 “Motivation: Direction and Intensity”; §11.1 “The Process of Managerial Communication”; §16.1 “Organizational Structures and Design” |
| C | Conclusions about organizational behavior depend on the research group and conditions of observation | §1.4 describes individual, group and organization levels of analysis; it does not directly establish the current research-method formulation |

Recommended Claim C narrowing, if approved:

> Организационное поведение изучается на индивидуальном, групповом и организационном уровнях; вывод должен указывать, к какому уровню анализа он относится.

Sources:
- §1.4: https://openstax.org/books/organizational-behavior/pages/1-4-a-model-of-organizational-behavior-and-management
- §7.1: https://openstax.org/books/organizational-behavior/pages/7-1-motivation-direction-and-intensity
- §11.1: https://openstax.org/books/organizational-behavior/pages/11-1-the-process-of-managerial-communication
- §16.1: https://openstax.org/books/organizational-behavior/pages/16-1-organizational-structures-and-design
- Book: https://openstax.org/books/organizational-behavior

**Source correction:** version the current Source identity/URI from the APA topic page to the exact OpenStax *Organizational Behavior* book identity. Version Claims A–C only as needed to align `provenance.created_from` to Source @2; version the three EUs with exact section locators. If the APA source is retained as an independent source, it needs a separate Source/EU chain and a specific support boundary.

Claim C's current phrase about observation conditions is a methodological statement not directly supported by §1.4; do not pretend that a levels-of-analysis section proves all research-method limitations.

Rights: verify the exact OpenStax *Organizational Behavior* preface and licence. The book contains credited third-party material; no figures or images are proposed for reuse.

## 7. Public Budgeting Basics — Claims A–C

Current records:
- `CLM-PUBLIC_BUDGETING_BASICS-A/B/C@1`
- `EU-PUBLIC_BUDGETING_BASICS-A/B/C@1`
- `SRC-PUBLIC_BUDGETING_BASICS@1`

The current IMF Public Financial Management portal is a broad landing page and does not provide adequate claim-specific locators for all three Claims. Three official sources offer a direct support route.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Public budgets connect revenue/expenditure planning with government priorities and available resources | OECD Recommendation on Budgetary Governance, Principle 1(II)(d) and Principle 2; PEFA Framework §1.2, “Strategic allocation of resources” |
| B | The public-budget process includes preparation, approval/authorization, execution and control of public finances | IMF *Digital Solutions Guidelines for Public Financial Management*, Annex Table 2.1: “Fiscal forecasting and budget preparation”, “Budget execution and control”, “Accounting and financial reporting”, “Audit planning”; PEFA Framework Pillars IV–VII |
| C | Budget decisions are constrained by available resources and rules; announced priorities do not automatically become funded outcomes | OECD Recommendation Principles 1 and 2; PEFA Pillar I “Budget reliability”; OECD Peru report section on budget modifications and divergence between voted and actual spending |

Sources:
- OECD Recommendation on Budgetary Governance: https://legalinstruments.oecd.org/public/doc/319/body-text.en.html
- PEFA 2016 Framework: https://www.pefa.org/sites/default/files/news/files/PEFA-Framework_English.pdf
- IMF *Digital Solutions Guidelines for Public Financial Management* (2023), Annex Table 2.1: https://www.imf.org/-/media/files/publications/tnm/2023/english/tnmea2023007.pdf
- OECD, *Public Financial Management in Peru*, section on budget modifications: https://www.oecd.org/en/publications/public-financial-management-in-peru_d51d43b1-en/full-report/component-6.html

Direct support:
- OECD Principle 1(II)(d) says policies should be aligned with available resources for each year of a medium-term fiscal horizon and that revenue/expenditure targets should be consistent with those resources.
- OECD Principle 2 says budgets should align with medium-term strategic priorities and that expenditure boundaries should be grounded in realistic forecasts.
- PEFA's seven pillars separate budget reliability, policy-based fiscal strategy/budgeting, predictability/control in execution, accounting/reporting and external scrutiny/audit.
- IMF Annex Table 2.1 lists the subfunctions of budget preparation, authorization of expenditure, execution/control, accounting/reporting and audit planning.
- OECD's Peru analysis shows how frequent budget modifications can make actual spending diverge from voted amounts and stated strategic priorities. Keep this as an example, not a universal claim about every budget system.

Recommended Claim C narrowing, if approved:

> Бюджетные решения должны укладываться в доступные ресурсы и фискальные ограничения; фактические расходы могут отличаться от первоначально утверждённых при изменении бюджета.

**Source graph requirement:** retain the existing IMF PFM Source only for its actual scope; add distinct OECD, PEFA and IMF Guidelines Source/Evidence Use chains as required by the approved graph. Do not combine the three publishers into the existing Source or invent canonical IDs.

Rights: OECD, IMF and PEFA publications require source-specific attribution/reuse review. The IMF Guidelines are a Technical Note and Manual whose disclaimer states that the views are those of the authors and do not necessarily represent IMF management or the Executive Board. Do not treat them as a formal IMF policy position.

## 8. Rights, scope and editorial gates

- IMF Back to Basics articles are copyrighted; use precise citations and paraphrase, not copied prose.
- OpenStax *Principles of Economics 3e* identifies CC BY 4.0 in its current preface; check third-party figures/components.
- Federal Reserve FEDS Note is U.S.-specific and does not define universal monetary aggregates.
- IMF “What Is Money?” is a separate publisher/source from the Federal Reserve note.
- OpenStax *Organizational Behavior* needs edition/licence and third-party component review; APA and OpenStax are not interchangeable source identities.
- OECD, PEFA and IMF public-budget sources have distinct institutional status and rights terms; keep each source and EU separate.
- All five slices remain HOLD pending canonical locator implementation, source/rights review, independent editorial review and Human View.

## 9. Recommended execution order after owner authorization

1. Locator-only: Macroeconomics A/B/C, Microeconomics A/B, Money and Banking B/C.
2. Source graph: add IMF “What Is Money?” for Money A; add OECD/PEFA/IMF source chains for Public Budgeting A–C.
3. Source identity correction: Organizational Behavior from APA topic page to OpenStax book; align Claims/EUs to current Source version.
4. Claim wording decisions: narrow Macroeconomics B/C, Microeconomics C, Organizational Behavior C and Public Budgeting C before canonical version changes.
5. Re-fetch all authorized records at one frozen HEAD, apply only approved versioned changes, validate Claim→EU→Source edges, run affected-slice tests and then full release gates on the final immutable HEAD.

## 10. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change Claim statements or versions;
- create new canonical Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve or amend the 15 locator/source changes; separately approve the Money A source addition, Organizational Behavior Source replacement, Public Budgeting multi-source graph, and the proposed Claim narrowings.
