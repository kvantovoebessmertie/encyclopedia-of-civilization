# R7 Labour Economics — Rights-Compatible Source Replacement Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Affected slice: `labor-economics-basics`  
Authorization: `REMAINING-R7-SOURCE-REMEDIATION-001`  
Status: **RESEARCH ONLY — NO OWNER PATH SELECTED; NO CANONICAL JSON CHANGED**

## 1. Purpose

The current authorization's OpenStax rights boundary was corrected to an explicit unresolved status. This report screens a possible Path B source replacement so the owner can make a concrete decision. It does not select Path B, allocate canonical IDs, amend the authorized source graph, or authorize canonical edits.

The three existing Claims remain unchanged:
- A: labour economics studies labour-market functioning, employment, wages and related institutions.
- B: wages are both workers' income and part of employers' labour costs.
- C: labour-market analysis uses employment, earnings, working time, productivity and labour-underutilization indicators.

## 2. OpenStax findings — do not treat another edition as an automatic workaround

The official *Principles of Economics 3e* HTML Preface states CC BY-NC-SA 4.0 and requires prior written permission for LLM training/ingestion and generative-AI offerings. A separately hosted PDF asset displays CC BY 4.0. The conflict remains unresolved and no permissive notice is selected by default.

A check of *Principles of Economics 2e* shows a similar internal inconsistency: the official HTML Preface initially says CC BY 4.0, but its “Citation/Attribution” section later says reuse is only for noncommercial purposes under ShareAlike and that LLM training/ingestion requires prior written permission. Therefore 2e is **not** a clean substitute without written clarification either.

Official references:
- `https://openstax.org/books/principles-economics-3e/pages/preface`
- `https://assets.openstax.org/oscms-prodcms/media/documents/principles-economics-3e_-_WEB.pdf`
- `https://openstax.org/books/principles-economics-2e/pages/preface`

## 3. Strongest rights-compatible candidate family: U.S. Bureau of Labor Statistics

The BLS states that its publications, in print and electronic form, are public domain except for previously copyrighted photographs and illustrations; no specific permission is needed to use BLS public-domain material, and attribution is requested. Its emblem remains a registered trademark and should not be reused.

Official rights statement:
- `https://www.bls.gov/opub/copyright-information.htm`

This is a comparatively strong rights position for text-only factual paraphrase and citations. It is not global subject-matter authority: all substantive examples below are U.S.-specific and must be presented as such. Third-party photos/illustrations and marks remain excluded.

### Candidate source A — labour-market concept and institutions

**U.S. Bureau of Labor Statistics, Monthly Labor Review, “Measuring labor market concentration using the QCEW” (3 October 2024).**

- URL: `https://www.bls.gov/opub/mlr/2024/article/measuring-labor-market-concentration-using-the-qcew.htm`
- Direct locator: subsection “Labor market definition”.
- The article describes labour markets using geographic and industry/occupation dimensions; workers sell labour in exchange for wages and benefits, while businesses use labour as an input.
- Supports a bounded illustration of labour-market functioning, employment, wages and employer demand.
- Boundary: the article is about U.S. labour-market concentration and competition, not a general definition of the academic discipline of labour economics or a global institutional taxonomy.

### Candidate source B — wages as worker income and employer cost

**U.S. Bureau of Labor Statistics, “Employer Cost for Employee Compensation — Help and Information”.**

- URL: `https://www.bls.gov/help/one_screen/cm.htm`
- Direct locator: opening definition of ECEC and subsections on wages/salaries and benefits.
- It distinguishes wages/salaries from employer-paid benefits and describes the ECEC as employer costs for wages/salaries and benefits.
- Pair with the 2024 Monthly Labor Review article above, which describes workers selling labour in exchange for wages and benefits.
- Boundary: these are U.S. compensation-statistics definitions. They do not establish the level or composition of compensation for a particular worker or employer in another jurisdiction.

### Candidate source C — indicator families

**U.S. Bureau of Labor Statistics, Information Guide, “Productivity”.**

- URL: `https://www.bls.gov/information-guide/home.htm`
- Direct locator: Productivity section, key takeaways and “Data available”.
- Lists labour productivity, output per hour, hours worked, employment, labour composition, labour compensation and unit labour costs.

**U.S. Bureau of Labor Statistics, “Concepts and Definitions (CPS)”.**

- URL: `https://www.bls.gov/cps/definitions.htm`
- Direct locator: “Alternative measures of labor underutilization (U-1 through U-6)”.
- Defines progressively broader U-1–U-6 measures, including discouraged and marginally attached workers and people working part time for economic reasons.

Boundary: BLS measures are U.S. statistical constructs. They illustrate indicator families but must not be represented as globally interchangeable with ILO statistical standards.

## 4. Independent / international-source options

### ILOSTAT / ILO

The ILO's current Open Access policy states that ILO knowledge products published or made available on or after 3 May 2023 are reusable under CC BY 4.0 unless otherwise indicated; earlier publications do not automatically receive that licence and require item-level checking. Third-party components remain separately controlled.

Official rights policy:
- `https://www.ilo.org/global/copyright/lang--en/index.htm`

Relevant ILOSTAT pages already identified in the existing authorization:
- Concepts and Definitions: `https://ilostat.ilo.org/methods/concepts-and-definitions/`
- Wages and Working Time Statistics (COND): `https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/`
- Labour Force Statistics (LFS): `https://ilostat.ilo.org/databases/lfs/description/`
- Labour underutilization: `https://www.ilo.org/resource/labour-underutilization`

The COND page expressly distinguishes earnings as an employee-income measure from labour cost as employers' expenditure on the workforce. The ILO labour-underutilization page describes time-related underemployment, unemployment and potential labour force. However, the identified pages are not all clearly dated as post-3-May-2023 knowledge products; do not assume CC BY 4.0 applies to each. Check exact page/publication date, ownership and third-party components before treating any as licensed material.

### World Bank

The current World Bank Group terms, amended 25 July 2025, permit noncommercial use with attribution for general site materials but prohibit derivative or commercial use without prior written consent unless a specific publication/dataset licence applies.

Official terms:
- `https://www.worldbank.org/ext/en/legal/terms-conditions`

The existing independent Source points to the World Bank Jobs and Development topic page. Its exact page-level scope and rights basis need re-screening; do not treat the generic topic page as CC BY or as a global textbook definition.

## 5. Proposed Path B architecture — for owner approval only

A conservative candidate structure would be:
1. Replace the OpenStax primary Source with a BLS Source record identifying only the exact official BLS pages above, with each Claim's support boundary clearly marked U.S.-specific.
2. Retain or replace the independent Source only after exact ILO/World Bank item-level terms and scope are checked.
3. Keep Claim statements unchanged only if an independent reviewer confirms that U.S.-specific evidence plus the selected international source adequately supports the general wording. If not, a separate owner-approved Claim wording authorization is needed; the current authorization prohibits changing Claim statements.
4. Create no new canonical Source IDs until the owner approves the exact graph topology and canonical IDs.
5. Use only independently worded factual paraphrase, attribution and text locators; no source text, charts, photos, graphics or logos.

This proposal is **not yet an implementation authorization**. BLS's U.S.-specific scope does not alone establish the general, international scope of all three Claims.

## 6. Owner decision still required

Choose one path:
- **A — permission:** obtain written OpenStax permission/clarification for the exact 3e asset, AI workflow and intended distribution.
- **B — replacement:** approve a BLS-based primary source graph and an independently rights-screened international source, with any necessary revised bounded authorization and canonical ID allocation.
- **C — citation-only / unused branch:** leave the OpenStax branch unused unless an owner/legal review explicitly approves the proposed AI-assisted workflow and final citation-only use.

No path is selected here. Labour Economics remains HOLD. No canonical record, Relation, candidate membership, allowlist or release decision was changed.

## 7. Source evidence summary

- BLS public-domain statement: `https://www.bls.gov/opub/copyright-information.htm`
- BLS labour-market definition: `https://www.bls.gov/opub/mlr/2024/article/measuring-labor-market-concentration-using-the-qcew.htm`
- BLS employer compensation: `https://www.bls.gov/help/one_screen/cm.htm`
- BLS productivity indicators: `https://www.bls.gov/information-guide/home.htm`
- BLS underutilization definitions: `https://www.bls.gov/cps/definitions.htm`
- ILO open-access policy: `https://www.ilo.org/global/copyright/lang--en/index.htm`
- World Bank terms: `https://www.worldbank.org/ext/en/legal/terms-conditions`
