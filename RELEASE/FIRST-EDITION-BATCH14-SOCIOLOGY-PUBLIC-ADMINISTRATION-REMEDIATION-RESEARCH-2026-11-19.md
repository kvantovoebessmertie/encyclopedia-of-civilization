# First Edition — Batch 14: Sociology and Public Administration Source/Claim Remediation Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: current PR branch at report creation  
Status: **6 CLAIMS / 6 EUS / 18 CANONICAL RECORDS REVIEWED ACROSS TWO SLICES; DIRECT LOCATOR ROUTES FOUND; SOCIOLOGY NEEDS SUBSTANTIVE CLAIM REPLACEMENT; PUBLIC ADMINISTRATION NEEDS SOURCE REPLACEMENT AND LOCATORS; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and duplicate control

The existing Society and Institutions audits identified two residual slices that were not covered by active bounded authorization or the earlier substantive remediation packages:

- `sociology-basics`: Claims A–C are editorial/meta placeholders; the ASA source is relevant but the canonical EUs have no pinpoints.
- `public-administration-basics`: Claims A–C are substantive but broad; the current OECD Directorate landing page is not a precise source and all EUs lack locators.

This follow-up converts those two audit findings into direct source and locator proposals. It does not repeat law, governance, demography, education, democratic institutions, public budgeting or the five-slice economics work.

**Exact scope:** 18 records — two Sources, six Claims, six EUs, two Contexts and two Scopes. All exact IDs, versions and record types were re-fetched from the current branch. All are v1. No canonical record, version, publication/completion state, Relation, allowlist or candidate decision was changed. Both slices remain HOLD.

## 2. Sociology Basics — 3 placeholder Claims / 3 EUs

Current records:
- `SRC-SOCIOLOGY_BASICS@1`
- `CLM-SOCIOLOGY_BASICS-A/B/C@1`
- `EU-SOCIOLOGY_BASICS-A/B/C@1`
- `CTX-SOCIOLOGY_BASICS@1`
- `SCP-SOCIOLOGY_BASICS@1`

Current Source: American Sociological Association, “What Is Sociology?” (canonical URI points to an ASA page). The current three Claims are editorial metadata rather than sociology propositions and cannot be made substantive by adding locators.

### Direct source

American Sociological Association, *Sociology: A 21st Century Major* (brochure PDF, 2023):
https://www.asanet.org/wp-content/uploads/2023/11/Brochure_Sociology_21st_Century_Major.pdf

The first page provides three direct passages:
- “What is Sociology?” — definition of sociology as the scientific study of social life; study of social structure, social change, interaction among societies and effects on individuals (PDF page 1, opening section).
- Research methods — posing a question/hypothesis and testing it through theoretical frameworks and scientific methods, including statistical analysis, surveys, ethnography, conversational analysis and content analysis (PDF page 1, paragraph beginning “The sociological journey…”).
- Research contribution — results of sociological investigations help develop theories and inform social policy, programmes and laws (PDF page 1, paragraph beginning “The results…”).

### Proposed replacement Claims for editor approval

| Claim | Proposed statement | Locator |
|---|---|---|
| A | Социология — научное изучение социальной жизни; социологи исследуют структуру обществ, их изменения и взаимодействия, а также влияние этих процессов на индивидов. | ASA brochure, p. 1, “What is Sociology?” and the two following sentences |
| B | Социологические исследования используют теоретические рамки и научные методы, включая статистический анализ, опросы, этнографию, анализ разговоров и контента. | ASA brochure, p. 1, paragraph beginning “The sociological journey…” |
| C | Результаты социологических исследований могут способствовать развитию теорий и информировать социальную политику, программы и законы. | ASA brochure, p. 1, paragraph beginning “The results of sociological investigations…” |

The proposals are factual paraphrases, not copied ASA text. Claim C must retain “могут”: the source describes potential contribution, not a guaranteed effect of every sociological study.

### Proposed canonical remediation

- Source v1→v2: exact bibliographic identity “American Sociological Association, *Sociology: A 21st Century Major* (2023)” and direct PDF URI.
- Claims A–C v1→v2: replace the three non-falsifiable editorial statements with the proposed subject-matter statements above; keep `claim_type: documented_fact`.
- EUs A–C v1→v2: exact page/paragraph locators above, concise support boundaries, Claim v2 and Source v2 references.
- Context v1→v2: define sociology as a social science studying social life, structures, interactions and change; distinguish empirical description from normative political judgement.
- Scope v1→v2: limit the slice to introductory sociology and the named methods/topics; exclude individual diagnosis, prescriptive policy advice and claims about every society unless separately sourced.

### Rights boundary

The ASA brochure is copyrighted. The proposal uses factual paraphrases and exact bibliographic/locator metadata only; it does not copy text, layout, images or graphics. Source reuse/attribution terms must be checked before publication. All three Claims remain HOLD pending editor approval and rights review.

## 3. Public Administration Basics — 3 substantive Claims / 3 EUs

Current records:
- `SRC-PUBLIC_ADMINISTRATION_BASICS@1`
- `CLM-PUBLIC_ADMINISTRATION_BASICS-A/B/C@1`
- `EU-PUBLIC_ADMINISTRATION_BASICS-A/B/C@1`
- `CTX-PUBLIC_ADMINISTRATION_BASICS@1`
- `SCP-PUBLIC_ADMINISTRATION_BASICS@1`

Current Source identity is a generic sentence about public administration and its URI is the OECD Directorate for Public Governance landing page. That page is not a precise publication or instrument and is not sufficient to support all three Claims.

### Direct official source

United Nations Economic and Social Council, Committee of Experts on Public Administration, *Definition of Basic Concepts and Terminologies in Governance and Public Administration*, Note by the Secretariat, E/C.16/2006/4, 5 January 2006:
https://digitallibrary.un.org/record/566603/files/E_C.16_2006_4-EN.pdf

Relevant direct passages:
- §I “Introduction”, paras. 1–3, pp. 1–2: terminology is not static and does not apply uniformly in all places and cultures; meanings vary by context.
- §III “Public administration”, paras. 18–21, pp. 4–5: public administration concerns government policies/programmes and officials; processes, organizations and people associated with carrying out laws and rules; UNDP definitions include the machinery of policies, rules, procedures, systems, structures and personnel, and the management/implementation of government activities and public-service provision.
- §VI “Decentralization”, paras. 36–37, pp. 8–9: powers, functions, responsibilities and resources may be transferred from central to local governments and other decentralized entities; forms differ by the extent and type of authority transferred.

### Claim-level mapping

| Claim / EU | Current proposition | Direct locator candidate | Assessment |
|---|---|---|---|
| A / EU A | Public administration is related to carrying out government functions and providing public services | §III paras. 18–21, especially paras. 20–21(b), pp. 4–5 | Direct |
| B / EU B | Administrative processes operate within established powers and procedures | §III paras. 19–21, pp. 4–5; para. 21(a) identifies policies, rules, procedures, systems and structures; para. 21(b) identifies implementation of laws, regulations and government decisions | Direct |
| C / EU C | Content and powers of public bodies depend on jurisdiction and applicable rules | §I paras. 1–3, pp. 1–2; §VI paras. 36–37, pp. 8–9 | Direct at the comparative/conceptual level; not a statement of any specific country's law |

The current Claim statements are substantively appropriate and do not need wording changes for this locator pass. Preserve the jurisdictional boundary: the UN paper is a 2006 conceptual compendium, not a current legal source for the powers of any named state or public authority.

### Proposed canonical remediation

- Source v1→v2: exact identity “United Nations Economic and Social Council, Committee of Experts on Public Administration, *Definition of Basic Concepts and Terminologies in Governance and Public Administration*, E/C.16/2006/4 (2006)” and direct UN Digital Library PDF URI.
- Claims A–C v1→v2: statements unchanged; provenance-only version increments to align `provenance.created_from` with Source v2.
- EUs A–C v1→v2: claim-specific locators above, support boundaries, exact Claim v2 and Source v2 references.
- Context v1→v2: distinguish comparative concepts of public administration from domestic legal authority; note that terminology and institutional arrangements vary by jurisdiction and context.
- Scope v1→v2: introductory comparative overview only; not a legal opinion, jurisdiction-specific delegation-of-authority guide, administrative procedure manual or current public-service operational instruction.

### Rights and source-quality boundary

The UN document is an official ECOSOC Secretariat paper and is publicly accessible through the UN Digital Library. Public access is not a blanket permission to reproduce the full document or third-party material. Use factual paraphrase, attribution and exact paragraph locators only. The paper itself cautions that the terminology inventory is limited and that concepts are not applied uniformly. Do not treat its 2006 definitions as an exhaustive or current legal standard.

## 4. Cross-slice implementation matrix

| Slice | Source action | Claim action | EU action | Context/Scope action | Owner approval |
|---|---|---|---|---|---|
| Sociology | Source v1→v2, exact ASA brochure identity | Replace Claims A–C v1→v2 | EU A–C v1→v2 with p. 1 paragraph locators | v1→v2, social-science boundary | Required for substantive replacements |
| Public Administration | Source v1→v2, replace generic OECD landing page with UN E/C.16/2006/4 | Claims A–C v1→v2, statements unchanged for provenance alignment | EU A–C v1→v2 with exact UN paragraphs | v1→v2, comparative/jurisdictional boundary | Required for source substitution and version alignment |

## 5. Exact bounded authorization requested

Approve only these 18 records and changes:

1. `SRC-SOCIOLOGY_BASICS` v1→v2: replace generic ASA page identity with the exact 2023 ASA brochure title and PDF URI.
2. `CLM-SOCIOLOGY_BASICS-A/B/C` v1→v2: replace the three editorial/meta statements with the proposed factual statements in §2.
3. `EU-SOCIOLOGY_BASICS-A/B/C` v1→v2: add the exact page 1 locators and exact current Claim/Source references.
4. `CTX-SOCIOLOGY_BASICS` and `SCP-SOCIOLOGY_BASICS` v1→v2: update target_ref to Claim A v2 and apply the boundaries in §2.
5. `SRC-PUBLIC_ADMINISTRATION_BASICS` v1→v2: replace generic identity/ODCD portal with the exact UN E/C.16/2006/4 identity and URI.
6. `CLM-PUBLIC_ADMINISTRATION_BASICS-A/B/C` v1→v2: statements unchanged; version solely to align provenance with Source v2.
7. `EU-PUBLIC_ADMINISTRATION_BASICS-A/B/C` v1→v2: add the exact locators and support boundaries in §3, and exact Claim/Source v2 references.
8. `CTX-PUBLIC_ADMINISTRATION_BASICS` and `SCP-PUBLIC_ADMINISTRATION_BASICS` v1→v2: update target_ref to Claim A v2 and apply the comparative/jurisdictional boundaries in §3.

## 6. Explicit prohibited changes

- No records outside the two named slices.
- No additional Source, Claim, EU or Relation IDs.
- No publication_status or completion_status changes.
- No first-edition allowlist changes or INCLUDE/EXCLUDE decisions; both slices remain HOLD.
- No changes to any Claim outside the three authorized Sociology replacements and the three provenance-only Public Administration version increments.
- No copying, translation or reproduction of ASA or UN source prose, images, figures or layouts.
- No validator, storage, recovery, package or release-gate changes.
- No merge, deployment or release approval.

## 7. Validation after approval

- Re-fetch all 18 records at a frozen HEAD.
- Confirm exact ID, version, type and publication/completion states.
- Verify every Claim provenance points to the exact current Source version.
- Verify each EU's `claim_ref`, `source_ref` and `provenance.created_from` match the current Claim/Source versions and each `material.locator` is non-empty and claim-specific.
- Verify Context and Scope target Claim A v2.
- Run affected-slice preflight/tests and exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests.
- Keep both slices HOLD pending rights review, independent subject-matter/editorial review and Human View.

**Owner decision required:** approve or reject this exact 18-record bounded scope. No canonical changes are made by this research report.
