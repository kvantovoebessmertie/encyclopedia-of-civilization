# M13 — Package 30 partial-claim source-fit and rights follow-up

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Canonical records inspected at HEAD: `640a24355365164336d39cd34a4c5bd0bbfe2dc8`
Scope: five partial Claims from Unassessed-Risk Content Screen Package 30.

## 1. Status and guardrails

This report records source-passage fit and rights findings for the five Package 30 partial Claims. It is a noncanonical review artifact only.

No Claim, Evidence Use, Source, Context, Scope, Relation, provenance, risk metadata, D/E/B score, or publication status is changed. No source candidate is promoted to an approved evidence source. No rights clearance or release approval is granted.

## 2. Claim-by-claim findings

### 2.1 Insurance C — source content fit confirmed; rights not cleared

Claim: `CLM-INSURANCE_BASICS-C@1`

Statement: `Страхование не устраняет сам риск и не гарантирует возмещение за события вне условий покрытия.`

Current chain:
- `EU-INSURANCE_BASICS-C@1`
- `SRC-INSURANCE_BASICS@1` — OECD Insurance topic page

The candidate NAIC consumer page, “How Does Insurance Work?”, directly states:
- insurance begins with a contract/policy and premiums/deductibles (page lines 36–42);
- insurance covers only events listed in the policy, and some policies identify what is not covered (lines 45–50);
- an insurer reviews a claim and pays its share if the policy covers the event (lines 159–166).

This is a close conceptual fit for the Claim’s contract-coverage boundary. The NAIC page is U.S.-consumer guidance; it must not be generalized into a universal legal rule or substitute for the wording of an actual policy and governing law.

Rights finding: no clear reuse licence was located for this specific consumer page. A NAIC Connect terms page restricts reuse of content on that service, but it is not established that those terms govern this public consumer page. Do not infer permission either way. Keep the candidate on RIGHTS REVIEW HOLD until page-specific terms or written permission are verified.

Candidate: https://content.naic.org/consumer/how-does-insurance-work

### 2.2 Labor Economics B — direct content fit; page-specific rights review required

Claim: `CLM-LABOR_ECONOMICS_BASICS-B@1`

Statement: `Заработная плата является одновременно доходом работников и частью затрат работодателей на труд.`

The ILOSTAT “Wages and Working Time Statistics” page directly distinguishes:
- earnings as a measure of employee income and purchasing power;
- labour cost as an estimate of employers’ expenditure on employing the workforce;
- earnings exclude employer contributions to social-security and pension schemes, which is an important boundary against equating wages with total labour cost.

This directly supports the two-sided accounting proposition, with the important qualification that wages/earnings are not identical to total employer labour costs.

Rights finding: ILO’s Open Access policy says publications published from 3 May 2023 are generally CC BY 4.0 unless otherwise indicated; pre-3 May 2023 publications do not automatically receive that licence and require item-specific checking. The ILOSTAT page is indexed as an older page (approximately 2022), and its own page-specific licence was not established in this review. Keep it on RIGHTS REVIEW HOLD pending page-specific confirmation. Do not assume that the general post-2023 policy retroactively licences this page.

Candidate: https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/
Rights policy: https://www.ilo.org/rights-and-permissions

### 2.3 Labor Economics C — four indicator families supported; productivity needs its own scoped source

Claim: `CLM-LABOR_ECONOMICS_BASICS-C@1`

Statement: `Анализ рынка труда использует показатели занятости, заработков, рабочего времени, производительности и недоиспользования труда.`

The same ILOSTAT page provides definitions and indicators for:
- employment;
- earnings/wages;
- hours actually worked and other working-time measures;
- labour underutilization, including time-related underemployment.

It does not, in the accessible material reviewed here, fully define the productivity indicator in the Claim. Add a separate productivity source rather than implying the ILOSTAT wages/working-time page covers it.

A suitable candidate is OECD Compendium of Productivity Indicators 2025, which defines labour productivity as GDP per hour worked and explains the labour-input concept. OECD’s Open Access policy says most written content published from 1 July 2024 is generally CC BY 4.0, subject to the copyright page and third-party exceptions. Verify the exact Compendium copyright page and third-party material before use.

Candidates:
- ILOSTAT wages/working time: https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/
- OECD Compendium 2025 productivity chapter: https://www.oecd.org/en/publications/oecd-compendium-of-productivity-indicators-2025_b024d9e1-en/full-report/cross-country-comparisons-of-labour-productivity-levels_b2fdb493.html
- OECD Open Access policy: https://www.oecd.org/en/about/oecd-open-by-default-policy.html

The Claim should remain on HOLD until the ILOSTAT page rights are resolved and a precise productivity locator is registered. The productivity measure must retain its denominator and scope (e.g. GDP per hour worked); it must not be interpreted as an individual worker’s personal effort or ability.

### 2.4 Logistics A — direct conceptual fit; rights not cleared

Claim: `CLM-LOGISTICS_BASICS-A@1`

Statement: `Логистика охватывает организацию перемещения и хранения товаров и связанные функции в цепочках поставок; конкретный набор операций зависит от цепочки и условий перевозки.`

The CSCMP FAQ page directly defines logistics management as planning, implementing and controlling forward/reverse flow and storage of goods, services and related information from origin to consumption. It also enumerates transportation, warehousing, materials handling, order fulfilment, network design, inventory management, supply/demand planning and third-party logistics. This is a strong conceptual fit for the Claim.

The World Bank LPI 2.0 report remains useful for performance measurement and comparison, but should not remain the sole definitional source.

Rights finding: no explicit open licence for the CSCMP FAQ page was located. Public accessibility is not reuse permission. Keep the CSCMP candidate on RIGHTS REVIEW HOLD pending a page-specific licence or permission. Do not copy the definition verbatim into the corpus.

Candidate: https://cscmp.org/CSCMP/CSCMP/Develop/Starting_Your_Career/Frequently_Asked_Questions.aspx

### 2.5 Manufacturing Systems A — existing NIST glossary is complementary, not sufficient

Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-A@1`

Statement: `Производственная система объединяет процессы, оборудование, людей и информационные элементы, которые совместно обеспечивают выпуск продукции.`

The NIST CSRC “Manufacturing Operations” glossary defines manufacturing operations broadly to include facility operation, system processes, materials input/output, maintenance, supply/distribution, health and safety, emergency response, human resources, security and information technology. NIST’s general information policy says NIST web-page information is public information unless marked copyrighted.

This glossary is useful complementary support for the breadth of manufacturing-enterprise functions, but it does not explicitly define a manufacturing system as the integrated combination of processes, equipment, people and information. It therefore does not, by itself, close the Claim’s gap.

A NIST GCR report (NIST GCR 16-007) contains a more direct smart-manufacturing definition involving electronic information, human-system interfaces, production data, decision-making and performance optimization. However, the report was prepared by RTI International under contract, not authored solely by NIST employees. NIST’s general public-information notice must not be assumed to clear contractor-authored material. Do not use this report until its specific rights statement is verified.

Candidates:
- NIST CSRC Manufacturing Operations glossary: https://csrc.nist.gov/glossary/term/Manufacturing_Operations
- NIST GCR 16-007: https://nvlpubs.nist.gov/nistpubs/gcr/2016/NIST.GCR.16-007.pdf
- NIST general use policy: https://www.nist.gov/copyrights-disclaimers

Disposition: keep the Claim PARTIAL/HOLD. The glossary can be considered complementary only; the contractor-authored GCR report remains RIGHTS REVIEW HOLD until its item-specific rights are established.

## 3. Rights review summary

| Candidate | Content fit | Rights disposition |
|---|---|---|
| NAIC consumer insurance page | Direct conceptual fit for policy-defined coverage | RIGHTS REVIEW HOLD — no page-specific reuse licence verified |
| ILOSTAT wages/working-time page | Direct for earnings vs labour cost; strong for employment/hours/underutilization | RIGHTS REVIEW HOLD — older page; pre-2023 material not automatically CC BY 4.0 |
| OECD Compendium 2025 | Suitable productivity definition | Candidate only — verify exact CC licence page and third-party exclusions |
| CSCMP logistics FAQ | Direct conceptual fit for logistics scope | RIGHTS REVIEW HOLD — no explicit open licence verified |
| NIST CSRC glossary | Complementary manufacturing operations coverage | Candidate for use subject to source/page review; NIST public-information notice applies except marked content |
| NIST GCR 16-007 (RTI-authored) | Strong conceptual fit for smart-manufacturing information/human/system integration | RIGHTS REVIEW HOLD — contractor-authored report; NIST general notice is insufficient |

## 4. Required next actions

1. Keep all five Claims UNASSESSED/HOLD; do not convert conceptual fit into D/E/B scores.
2. Resolve item-specific rights for NAIC, ILOSTAT and CSCMP before adding them as approved evidence.
3. Verify the OECD Compendium 2025 copyright page and exact productivity passage.
4. For Manufacturing Systems A, identify a rights-compatible source that directly defines the manufacturing system boundary and the role of equipment, people, processes and information; the NIST glossary alone is not enough.
5. Only after rights and source fit are resolved, create a bounded authorization naming the exact Source/Evidence Use files, permitted fields, version increments, README/coverage changes and regression tests.
6. Re-fetch all canonical records at the then-current branch HEAD before any authorized write.

## 5. Validation and disposition

This report is a noncanonical evidence-review artifact. It does not authorize canonical writes, alter the Package 30 results, clear any Claim, or close any M13 gate.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged; `main` must remain unchanged.
