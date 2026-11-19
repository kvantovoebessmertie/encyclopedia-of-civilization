# First Edition — Batch 12: Macroeconomics, Microeconomics, Money and Organizational Behavior

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: current PR branch at report creation  
Status: **12 CLAIMS / 12 EUS ACROSS FOUR CANDIDATE SLICES REVIEWED; STRONG DIRECT LOCATOR ROUTES FOR 10 CLAIMS; MACROECONOMICS NEEDS SOURCE-GRAPH EXPANSION; ORGANIZATIONAL-BEHAVIOR CLAIM C NEEDS NARROWING OR A METHOD SOURCE; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and duplicate control

After the prior source-fit dossiers and bounded authorizations were excluded, four candidate slices with current `canonical_json_snapshot` entries remained without a corresponding claim-specific evidence-depth dossier in the inspected RELEASE tree:

- macroeconomics-basics — Claims A–C / EUs A–C;
- microeconomics-basics — Claims A–C / EUs A–C;
- money-and-banking-basics — Claims A–C / EUs A–C;
- organizational-behavior-basics — Claims A–C / EUs A–C.

**Total: 12 Claims / 12 EUs / 4 existing Sources.** Exact Claim, EU and Source IDs and v1 record types were fetched from the current branch. All 12 EUs use generic material descriptions rather than claim-specific pinpoint locators.

The existing Batch 10 and Batch 11 dossiers, the Domain Audit covering climate science / Solar System / remote sensing, and all active bounded authorizations were excluded from this pass. This report does not re-open those scopes.

No new dependency nodes were found. All 12 Claims and 12 EUs already appear in the exact-version master. Master total remains 1,129 rows = 1,058 candidate keys + 71 dependency records; Part II slice coverage remains 124/385. All four slices remain HOLD.

## 2. Macroeconomics Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM-MACROECONOMICS_BASICS-A/B/C@1`
- EUs: `EU-MACROECONOMICS_BASICS-A/B/C@1`
- Source: `SRC-MACROECONOMICS_BASICS@1`

Current Source identity is a generic Russian description of macroeconomics; the URI points to the IMF *Finance & Development* “Back to Basics” series page. The series landing page is not itself a claim-specific locator for all three propositions.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A | Macroeconomics studies aggregate indicators of output, income, employment and prices | IMF *Finance & Development*, “Micro and Macro: The Economic Divide” → Overview and “How micro and macro differ in focus and method”; explicitly identifies employment, GDP, inflation, national income, savings and overall price level | Direct |
| B | GDP measures the market value of final goods and services produced in an economy over a period | IMF *Finance & Development*, “Gross Domestic Product: An Economy’s All” → “Measuring GDP”; defines monetary value of final goods and services produced within a country in a given quarter/year | Direct |
| C | Inflation describes a sustained change in the general price level, measured by a selected indicator | IMF *Finance & Development*, “Inflation: Prices on the Rise” → “What is inflation and how it is measured”; defines inflation as the rate of increase in prices over a period and distinguishes CPI, core inflation and GDP deflator | Direct with wording boundary |

Sources:
- IMF, “Micro and Macro: The Economic Divide”: https://www.imf.org/en/Publications/fandd/issues/Series/Back-to-Basics/micro-and-macro
- IMF, “Gross Domestic Product: An Economy’s All”: https://www.imf.org/en/Publications/fandd/issues/Series/Back-to-Basics/gross-domestic-product-gdp
- IMF, “Inflation: Prices on the Rise”: https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/inflation

**Source-graph issue:** one existing IMF series Source can accurately represent the “Back to Basics” series, but Claim B and C rely on two distinct articles with their own authors, dates and stable page identities. The preferred canonical graph is:
1. retain/version the existing Source as the exact IMF article used for Claim A, or define it explicitly as the IMF F&D Back to Basics series landing page;
2. allocate separate Source records for the IMF GDP article and IMF Inflation article;
3. allocate corresponding Evidence Use records for Claims B/C, with exact page/section locators and support limits.

No new canonical IDs are proposed or created here. If the project chooses not to expand the graph, then the current single-Source chain must not be described as direct support for all three Claims.

**Claim boundaries:**
- GDP is domestic production within a territory, not production by nationals wherever they live; distinguish GDP from GNP/GNI.
- GDP counts final goods and services, not the gross value of all intermediate transactions; it omits or imperfectly captures some non-market and informal activity.
- Inflation is a rate of increase in prices over time, not merely a one-time rise in one product's price. A selected price index has a defined coverage; CPI, producer prices and the GDP deflator are not interchangeable.

## 3. Microeconomics Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM-MICROECONOMICS_BASICS-A/B/C@1`
- EUs: `EU-MICROECONOMICS_BASICS-A/B/C@1`
- Source: `SRC-MICROECONOMICS_BASICS@1`

The current Source identity is a generic definition of microeconomics and the URI points to OpenStax *Principles of Economics 3e*. The most precise direct locator is OpenStax *Principles of Microeconomics 3e*, Chapter 3.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A | Demand and supply describe relationships between price and quantity under specified conditions | §3.1 “Demand, Supply, and Equilibrium in Markets for Goods and Services”; demand and supply schedules/curves and the laws of demand and supply | Direct |
| B | Markets coordinate buyer and seller decisions through exchange and prices | §3.1; definitions of demand, supply, market interaction and equilibrium price/quantity | Direct, but keep the statement descriptive rather than claiming that all markets coordinate perfectly |
| C | Market equilibrium depends on demand, supply and the selected market definition | §3.1 equilibrium price and quantity where quantity demanded equals quantity supplied; §3.2 “Shifts in Demand and Supply” explains changes in the curves and equilibrium | Direct for demand/supply dependence; “selected market definition” is not established as a separate theorem by these sections |

Sources:
- OpenStax, *Principles of Microeconomics 3e*, §3.1: https://openstax.org/books/principles-microeconomics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- §3.2: https://openstax.org/books/principles-microeconomics-3e/pages/3-2-shifts-in-demand-and-supply-for-goods-and-services
- §3.3: https://openstax.org/books/principles-microeconomics-3e/pages/3-3-changes-in-equilibrium-price-and-quantity-the-four-step-process
- Book preface/licence: https://openstax.org/books/principles-microeconomics-3e/pages/preface

**Recommended Source correction:** identify the exact book as *Principles of Microeconomics 3e* (David Shapiro, Daniel MacDonald and Steven A. Greenlaw; OpenStax, 2022) and point the Source URI to the book/section, not the broader *Principles of Economics 3e* title. Then version the three EUs with §3.1–§3.3 claim-specific locators.

**Claim C narrowing, if approved:**

> Рыночное равновесие в заданном рынке соответствует цене и количеству, при которых объём спроса равен объёму предложения.

This removes the unsupported extra phrase “and the selected definition of market” while retaining the actual equilibrium proposition. The source explains equilibrium within a specified market model; it does not define a universal market-boundary selection method.

**Rights:** OpenStax *Principles of Microeconomics 3e* is CC BY-NC-SA 4.0. The current preface explicitly prohibits using the book to train or otherwise ingest it into LLMs or generative-AI offerings without prior written permission. Commercial reuse is also not granted by the NonCommercial licence. This is a material rights blocker for this project's AI-assisted production and distribution model. Do not treat public access or a pinpoint locator as rights clearance.

## 4. Money and Banking Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM-MONEY_AND_BANKING_BASICS-A/B/C@1`
- EUs: `EU-MONEY_AND_BANKING_BASICS-A/B/C@1`
- Source: `SRC-MONEY_AND_BANKING_BASICS@1`

The current Source points to a very recent Federal Reserve FEDS Notes article, *New Forms of Money and the U.S. Monetary Aggregates* (4 September 2026). Unlike the other slices, the existing source is closely matched to the Claims and directly covers the concepts. The missing element is pinpoint precision and a clear U.S.-specific boundary.

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A | Money is used as a means of payment and a way to store value | Article “Overview”: defines money supply as safe assets with stable values used to make payments or hold as short-term investments; “Analytical Approach — Part 1: Functional Classification” distinguishes medium of exchange and store of value | Direct |
| B | Monetary aggregates classify money and near-money assets by liquidity and function | “Overview” and “Background on the U.S. Monetary Aggregates”; explains monetary base, M1 and M2, liquidity and functional classification | Direct, but specifically the U.S. Federal Reserve's monetary aggregates |
| C | Different forms of money and financial assets differ in liquidity and use | “Background on the U.S. Monetary Aggregates”; “Functional Classification”; subsections on tokenized deposits, tokenized money market funds and payment stablecoins | Direct, with U.S. policy/regulatory and 2026 article-date boundary |

Official source:
- Federal Reserve FEDS Notes, *New Forms of Money and the U.S. Monetary Aggregates*, 4 September 2026: https://www.federalreserve.gov/econres/notes/feds-notes/new-forms-of-money-and-the-u-s-monetary-aggregates-20260904.html

**Recommended remediation:**
1. Correct Source identity to the exact article title, authors (Kristen Payne and Mary-Frances Styczynski), publisher (Federal Reserve Board) and date.
2. Pin EU A to “Overview” and “Functional Classification”.
3. Pin EU B to “Background on the U.S. Monetary Aggregates” and the M1/M2 definitions.
4. Pin EU C to the tokenized-deposit, tokenized-money-market-fund and payment-stablecoin sections; preserve the fact that liquidity depends on convertibility, payment functionality and redemption time.
5. Narrow Claim B to “В США Федеральная резервная система классифицирует денежные агрегаты по ликвидности и функциям активов” or explicitly state that M1/M2 are U.S.-specific measures. Do not present the U.S. aggregate definitions as a universal global standard.
6. Preserve the time boundary: the article describes U.S. monetary aggregates and digital-asset policy/market conditions as of September 2026; its examples should not be frozen as timeless descriptions of all jurisdictions.

The article itself distinguishes immediately spendable M1 assets from less liquid M2 savings assets, and notes that money-market fund redemption can require one to two business days. Do not collapse “liquid”, “convertible” and “immediately usable for payments” into synonyms.

## 5. Organizational Behavior Basics — 3 Claims / 3 EUs

Canonical records:
- Claims: `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-A/B/C@1`
- EUs: `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-A/B/C@1`
- Source: `SRC-ORGANIZATIONAL_BEHAVIOR_BASICS@1`

Current Source identity is a generic description of organizational behavior and the URI points to the APA “Organizational Psychology” topic page. This is a relevant professional-domain portal, but it does not directly locate the full set of three claims. A more precise educational source is OpenStax *Organizational Behavior* (J. Stewart Black and David S. Bright, 2019).

| Claim / EU | Current proposition | Direct locator candidate | Fit |
|---|---|---|---|
| A | Organizational behavior studies interactions among people, groups and organizational conditions | OpenStax §1.4 “A Model of Organizational Behavior and Management”: explicitly defines organizational behavior and examines individuals, groups and the organization as a whole; also identifies tasks/technology and organization design | Direct |
| B | Motivation, communication and task structure can influence work behavior | §7.1 “Motivation: Direction and Intensity”; §11.1 “The Process of Managerial Communication”; §9.2 “Work Group Structure”; §16.1 “Organizational Structures and Design” | Direct across multiple sections |
| C | Conclusions about organizational behavior depend on the group studied and observation conditions | §1.4 distinguishes levels of analysis and identifies individual/group/organization differences, tasks, technology and organizational context. It does not directly establish a general research-method rule about observation conditions | Partial. Narrow the Claim to the supported levels/context or add a distinct organizational-research-method source |

Sources:
- OpenStax, *Organizational Behavior*, §1.4: https://openstax.org/books/organizational-behavior/pages/1-4-a-model-of-organizational-behavior-and-management
- §7.1: https://openstax.org/books/organizational-behavior/pages/7-1-motivation-direction-and-intensity
- §9.2: https://openstax.org/books/organizational-behavior/pages/9-2-work-group-structure
- §11.1: https://openstax.org/books/organizational-behavior/pages/11-1-the-process-of-managerial-communication
- §16.1: https://openstax.org/books/organizational-behavior/pages/16-1-organizational-structures-and-design
- Book preface/licence: https://openstax.org/books/organizational-behavior/pages/preface

**Claim C narrowing, if approved:**

> Анализ организационного поведения различает индивидуальный, групповой и организационный уровни и учитывает задачи, технологии и структуру организации.

This is directly supported by §1.4 and avoids asserting a research-method conclusion that the current source does not establish. If the current wording about observation conditions is retained, add a distinct source on organizational research design, sampling, context and observation methods; do not stretch the textbook's conceptual model to support it.

**Rights:** OpenStax *Organizational Behavior* is CC BY-NC-SA 4.0. Its preface explicitly prohibits LLM training/ingestion and use in generative-AI offerings without prior written permission. Commercial reuse is not granted by the NonCommercial licence. This is a material rights blocker for the project; do not treat it as cleared merely because the pages are public. A rights-compatible substitute source may be preferable to changing the canonical Source to OpenStax.

## 6. Cross-slice results and next actions

| Slice | Direct locator readiness | Required action before canonical update |
|---|---|---|
| Macroeconomics | A–C direct in three IMF articles | Add two Source/EU dependency branches for GDP and inflation; preserve GDP/CPI boundaries |
| Microeconomics | A/B direct; C direct after narrowing | Correct exact book identity/URI; decide Claim C wording; resolve OpenStax rights restriction |
| Money and Banking | A–C direct in one current Federal Reserve article | Correct exact Source identity and add claim-specific locators; make U.S. scope explicit |
| Organizational Behavior | A/B direct; C partial | Correct Source identity only if rights are approved; otherwise choose a rights-compatible source; narrow C or add a methods source |

### Recommended implementation order

1. Money and Banking — lowest graph complexity and strongest current source fit; locator-only plus exact source identity and U.S. scope review.
2. Macroeconomics — prepare a three-source graph and direct EU locators; no new IDs until canonical allocation.
3. Microeconomics — prepare locator-only updates but keep on HOLD pending explicit OpenStax AI-use and licence compatibility decision.
4. Organizational Behavior — decide whether OpenStax is legally usable in the project; otherwise find a rights-compatible alternative. Claim C must be narrowed or separately sourced.

## 7. Rights and editorial gates

- IMF and Federal Reserve sources require exact attribution and source-specific reuse review; no blanket permission to reproduce graphics or full text is inferred.
- OpenStax *Principles of Microeconomics 3e* and *Organizational Behavior* both carry CC BY-NC-SA 4.0 terms and explicit restrictions on LLM ingestion/generative-AI use without prior written permission.
- Do not copy textbook passages, figures, tables or diagrams into the corpus. Factual paraphrase still needs a rights-policy decision where the source explicitly restricts AI ingestion or project reuse.
- Macroeconomics, inflation and monetary aggregates are time- and jurisdiction-sensitive. Preserve dates, statistical definitions, national scope and the difference between general concepts and U.S.-specific measurement systems.
- All four slices remain HOLD. Source fit and locator completeness do not establish factual truth, rights clearance, evidence diversity or release eligibility.

## 8. Explicit non-actions

No canonical JSON, version, publication/completion status, Relation, Context, Scope, allowlist, candidate disposition or release decision changed. No new Source/EU ID was created or guessed. No code, validator, test, coverage manifest or release-gate semantics changed. PR #22 remains Draft and unmerged; `main` was not modified.
