# M13 — strict passage/locator review package 03

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input queue: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`  
Scope: 9 exact Claim/Evidence Use/Source triples from the 47-item strict generic-EU passage/locator queue.  
State: **desk-level source-passage, rights and risk-routing review only; no canonical edits, no D/E/B changes, no specialist sign-off, no release clearance.**

## 1. Exact records and identity checks

The following v1 Claim, Evidence Use and Source JSON records were retrieved from the active M13 branch. For all nine entries, Claim → EU → Source IDs and versions resolve and match. The Evidence Use records contain generic descriptions rather than reproducible passage locators.

| Slice | Claim | Evidence Use | Source |
|---|---|---|---|
| acoustics-basics | `CLM-ACOUSTICS_BASICS-C@1` | `EU-ACOUSTICS_BASICS-C@1` | `SRC-ACOUSTICS_BASICS@1` |
| algebra-basics | `CLM-ALGEBRA_BASICS-A@1` | `EU-ALGEBRA_BASICS-A@1` | `SRC-ALGEBRA_BASICS@1` |
| algebra-basics | `CLM-ALGEBRA_BASICS-B@1` | `EU-ALGEBRA_BASICS-B@1` | `SRC-ALGEBRA_BASICS@1` |
| algebra-basics | `CLM-ALGEBRA_BASICS-C@1` | `EU-ALGEBRA_BASICS-C@1` | `SRC-ALGEBRA_BASICS@1` |
| anatomy-basics | `CLM-ANATOMY_BASICS-A@1` | `EU-ANATOMY_BASICS-A@1` | `SRC-ANATOMY_BASICS@1` |
| anatomy-basics | `CLM-ANATOMY_BASICS-B@1` | `EU-ANATOMY_BASICS-B@1` | `SRC-ANATOMY_BASICS@1` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-A@1` | `EU-ARCHIVAL_SCIENCE-A@1` | `SRC-ARCHIVAL_SCIENCE@1` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-B@1` | `EU-ARCHIVAL_SCIENCE-B@1` | `SRC-ARCHIVAL_SCIENCE@1` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-C@1` | `EU-ARCHIVAL_SCIENCE-C@1` | `SRC-ARCHIVAL_SCIENCE@1` |

## 2. Claim-by-Claim findings

### 2.1 Acoustics — noise recommendations are source-, duration-, context- and framework-dependent

**Claim:** `CLM-ACOUSTICS_BASICS-C@1`  
**Claim text:** “Рекомендации по шуму зависят от источника, времени воздействия, контекста и применимой нормативной системы.”  
**Registered Source:** WHO, *Environmental Noise Guidelines for the European Region* (2018), https://www.who.int/europe/publications/i/item/9789289053563

**Passage result: PARTIAL / scope-aligned, not complete.** WHO's overview states that the guidelines cover environmental noise from road traffic, railways, aircraft, wind turbines and leisure sources. The guideline's recommendations distinguish source categories and exposure metrics, including average exposure, night exposure and short-term/weekly leisure-noise exposure. The WHO compendium's environmental-noise section further lists source-specific average and night values and mitigation measures including time restrictions and reduced exposure duration: https://cdn.who.int/media/docs/default-source/who-compendium-on-health-and-environment/who_compendium_noise_01042022.pdf.

The registered WHO guideline supports source, duration and environmental/public-health context. It does **not** establish the Claim's broader phrase “applicable regulatory system”: WHO guidance is not itself the full set of national occupational, environmental or local legal requirements. WHO environmental-noise guidance also excludes occupational workplace noise from its environmental-noise scope.

**Risk route: MODERATE.** The Claim could influence interpretation of health and exposure recommendations. Keep the environmental/occupational distinction explicit and do not present WHO guideline values as binding legal limits in every jurisdiction.

**Disposition:** HOLD pending a bounded EU locator to the WHO overview and the source-specific exposure recommendation sections. Consider narrowing the Claim to “environmental-noise recommendations” and separately identifying that applicable legal requirements vary by jurisdiction and exposure setting. Do not silently treat a WHO guideline as a universal regulatory code.

### 2.2 Algebra — expressions

**Claim:** `CLM-ALGEBRA_BASICS-A@1`  
**Claim text:** “Алгебраические выражения состоят из чисел, переменных и операций над ними.”  
**Registered Source:** OpenStax, *College Algebra 2e*, https://openstax.org/details/books/college-algebra-2e

**Passage result: DIRECT mathematical fit at desk level.** OpenStax *College Algebra 2e*, Chapter 1 Key Concepts, section 1.1 “Real Numbers: Algebra Essentials,” defines algebraic expressions as constants and variables combined using addition, subtraction, multiplication and division: https://openstax.org/books/college-algebra-2e/pages/1-key-concepts. The wording is conceptually direct; “numbers” is a less precise substitute for “constants,” and the Claim does not enumerate the operations.

**Risk route: LOW DIRECT CONSEQUENCE.** Foundational mathematics; no direct operational hazard in the statement.

**Disposition: HOLD — RIGHTS BLOCKER.** The online book's current attribution section expressly says the book may not be used to train large language models or otherwise be ingested into LLMs or generative-AI offerings without OpenStax's prior written permission. It is also CC BY-NC-SA, with noncommercial and ShareAlike conditions. This is a material restriction for an AI-enabled knowledge system. Do not treat a direct mathematical match as rights clearance. Obtain written permission or replace the registered source with a suitable source whose rights permit the intended use. No canonical locator proposal should be accepted until rights are resolved.

### 2.3 Algebra — equations

**Claim:** `CLM-ALGEBRA_BASICS-B@1`  
**Claim text:** “Уравнение задаёт условие равенства двух выражений и решается относительно неизвестных при допустимых преобразованиях.”

**Passage result: DIRECT mathematical fit at desk level.** OpenStax *College Algebra 2e*, Chapter 1, section 1.1, subsection “Formulas,” states that an equation is a mathematical statement indicating that two expressions are equal and that solutions are values making the equation true: https://openstax.org/books/college-algebra-2e/pages/1-1-real-numbers-algebra-essentials. The source also relates finding solutions to properties of real numbers and other results. The Claim's “permissible transformations” is a sound mathematical boundary but is not separately pinned by the current generic EU description.

**Risk route: LOW DIRECT CONSEQUENCE.**

**Disposition: HOLD — same OpenStax AI-ingestion and license restriction as Claim A.** The source passage supports the mathematical proposition, but this is not permission to ingest, adapt or publish source-derived material in the Encyclopedia. Obtain prior written permission or select an alternative source with compatible rights. Do not add a canonical locator while the rights decision remains unresolved.

### 2.4 Algebra — functions, domain and range

**Claim:** `CLM-ALGEBRA_BASICS-C@1`  
**Claim text:** “Функция связывает элементы области определения с элементами области значений по заданному правилу.”

**Passage result: DIRECT mathematical fit at desk level.** OpenStax *College Algebra 2e*, section 3.1 “Functions and Function Notation,” defines a function as a relation in which each possible input value leads to exactly one output value. Section 3.2 “Domain and Range” identifies domain as input values and range as output values: https://openstax.org/books/college-algebra-2e/pages/3-1-functions-and-function-notation and https://openstax.org/books/college-algebra-2e/pages/3-2-domain-and-range. The Claim is an acceptable introductory paraphrase, though “по заданному правилу” is less exact than the single-output-per-input condition and should not replace that defining condition.

**Risk route: LOW DIRECT CONSEQUENCE.**

**Disposition: HOLD — same OpenStax AI-ingestion and license restriction.** Direct passage fit does not resolve rights. The source must not be used for AI ingestion without prior written permission. Seek permission or replace it before canonical locator correction.

### 2.5 Anatomy — tissues and cells

**Claim:** `CLM-ANATOMY_BASICS-A@1`  
**Claim text:** “Ткани состоят из клеток, организованных для выполнения определённых функций.”  
**Registered Source:** NIGMS, *Cells, tissues, organs and systems*, https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx

**Passage result: DIRECT conceptual support from an authoritative supplementary source; registered-source retrieval unresolved.** The registered NIGMS URL could not be retrieved during this desk check, so its current page text and exact locator are not confirmed. An authoritative NCBI Bookshelf medical terminology chapter defines a tissue as a group of similar cells that work together to perform a specific function: https://www.ncbi.nlm.nih.gov/books/NBK607445/. This directly supports the Claim's core proposition, but it is a supplementary source, not the Source record currently linked by the EU. Do not silently substitute it.

**Risk route: LOW DIRECT CONSEQUENCE.** Foundational anatomy. Avoid implying that every tissue consists only of one cell type or that function is determined solely by cell similarity.

**Disposition: HOLD.** Recheck the registered NIGMS page through a stable official endpoint and record a reproducible section locator. If it is unavailable or insufficient, prepare a separately versioned Source/EU proposal for the NCBI Bookshelf or another suitable authoritative source, with rights and source identity reviewed.

### 2.6 Anatomy — organs and multiple tissue types

**Claim:** `CLM-ANATOMY_BASICS-B@1`  
**Claim text:** “Органы состоят из нескольких типов тканей, работающих совместно.”

**Passage result: DIRECT conceptual support from an authoritative supplementary source; registered-source retrieval unresolved.** The NCBI Bookshelf chapter states that an organ is an anatomically distinct structure composed of two or more tissue types and performs one or more physiological functions: https://www.ncbi.nlm.nih.gov/books/NBK607445/. This directly supports the statement. As above, the registered NIGMS page could not be retrieved during this check, and the NCBI Bookshelf reference is not currently registered in the Claim → EU → Source chain.

**Risk route: LOW DIRECT CONSEQUENCE.**

**Disposition: HOLD pending registered-source verification or a bounded, versioned Source/EU proposal.** Preserve the distinction between an organ's tissue composition and the coordinated function of the organ; do not infer that all organs contain the same tissue types.

### 2.7 Archival science — core archival functions

**Claim:** `CLM-ARCHIVAL_SCIENCE-A@1`  
**Claim text:** “Архивная работа включает функции оценки, комплектования, упорядочивания, описания, сохранения и предоставления доступа к материалам.”  
**Registered Source:** Society of American Archivists (SAA), *Archives 101: Basic Principles*, https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles

**Passage result: DIRECT conceptual support.** SAA describes processing as the work of taking intellectual and physical control of a collection to preserve it and make it accessible. It identifies appraisal, arrangement, description and preservation as four distinct activities. Its appraisal section also discusses acquiring new collections and evaluating whether to accept them. The source therefore supports the functions in the Claim, although “комплектование” is broader than the source's short discussion of acquisition and should not be read as a complete acquisition policy.

**Risk route: LOW DIRECT CONSEQUENCE.** General professional description; no direct physical hazard. The statement may affect archival workflow design, so specialist review is appropriate before turning it into a mandatory procedure.

**Disposition: HOLD pending exact EU locator and scope note.** Use the processing discussion and the appraisal/acquisition passage as distinct locators. Do not imply that this short community-archives guide exhausts all archival functions or all national archival standards.

### 2.8 Archival science — provenance

**Claim:** `CLM-ARCHIVAL_SCIENCE-B@1`  
**Claim text:** “Принцип происхождения требует сохранять различимость материалов разных создателей и не смешивать их происхождение в описании.”

**Passage result: DIRECT support.** SAA's *Archives 101: Basic Principles* explicitly states that documents of one provenance must not be intermingled with documents of another provenance. It explains that keeping materials created by an individual or organization together enables researchers to understand the creator and authenticate the materials' origins. This is a close and direct match to the Claim.

**Risk route: MODERATE.** Provenance errors can undermine authenticity, context and evidentiary value of archival records. The Claim is not itself a complete archival arrangement or description standard.

**Disposition: HOLD pending exact EU locator.** Cite the “Principle of Provenance” passage. Keep provenance distinct from original order; both may be relevant but are not interchangeable.

### 2.9 Archival science — description, creation context and collection structure

**Claim:** `CLM-ARCHIVAL_SCIENCE-C@1`  
**Claim text:** “Архивное описание связано с контекстом создания и структурой коллекции, поэтому архивные материалы рассматриваются не только как отдельные документы.”

**Passage result: PARTIAL / strong conceptual alignment.** SAA's source explains that provenance preserves the relationship to the creator, original order preserves the collection's organizational relationships, and description produces an inventory and guide to the collection. It also refers to historical/biographical context, related materials and collection significance in a finding aid. These passages support the Claim's collection-level orientation. The source does not, in one explicit definition, state the full relationship between archival description, context of creation and aggregate collection structure exactly as worded.

**Risk route: MODERATE.** A weak description can obscure context and relationships among records. Avoid presenting this short guide as a complete descriptive standard or a substitute for applicable archival standards.

**Disposition: HOLD pending exact EU locator and, if the Claim is intended as a formal professional principle, a more authoritative archival description standard.** Preserve the distinction between provenance, original order, arrangement and description.

## 3. Consolidated disposition

| Claim | Passage result | Risk route | Rights/source issue | Disposition |
|---|---|---|---|---|
| Acoustics C | Partial | Moderate | WHO environmental scope does not establish every legal framework; occupational noise excluded | HOLD |
| Algebra A | Direct | Low direct consequence | OpenStax prior written permission required for LLM/generative-AI ingestion; CC BY-NC-SA | HOLD |
| Algebra B | Direct | Low direct consequence | Same OpenStax restriction | HOLD |
| Algebra C | Direct | Low direct consequence | Same OpenStax restriction | HOLD |
| Anatomy A | Direct supplementary support | Low direct consequence | Registered NIGMS URL not retrievable in this check; supplementary source not registered | HOLD |
| Anatomy B | Direct supplementary support | Low direct consequence | Same NIGMS/source identity issue | HOLD |
| Archival A | Direct | Low direct consequence | Claim scope slightly broader than short guide; locator absent | HOLD |
| Archival B | Direct | Moderate | Exact provenance passage available; locator absent | HOLD |
| Archival C | Partial | Moderate | Collection/context concepts supported, full wording not fully pinned | HOLD |

## 4. Exact change and completion boundary

- Claims reviewed: **9**.
- Evidence Use records reviewed: **9**.
- Source records reviewed: **5**.
- Claim/EU/Source identity and version links: **9/9 resolve and match**.
- Generic/non-pinpoint EUs: **9/9**.
- Direct or partial passage support located: **9/9** (including supplementary-source support where the registered source page was not retrievable).
- Canonical Claim/Evidence Use/Source records changed: **0**.
- Canonical passage locators added: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Risk metadata assigned or changed: **0**.
- Independent specialist reviews completed: **0**.
- Rights permissions obtained: **0**.
- Human View / release approval: **0**.

## 5. Queue reconciliation

The 47-item strict queue had 19 rows touched by prior Packages 07, 01 and 02 (6 + 7 + 6). This package reviews 9 additional exact rows. Therefore:

- Strict-queue rows touched: **28/47**.
- Strict-queue rows not yet reviewed in a dedicated package: **19/47**.
- These are report-level review counts, not canonical locator corrections or approvals.
- All nine rows remain on HOLD until the relevant rights/source identity issues, exact locators, versioned authorization and any required specialist review are resolved.

## 6. Required next actions

1. Keep the three Algebra Claims on rights HOLD. Do not ingest OpenStax source content into an LLM or generative-AI workflow without prior written permission. Identify a rights-compatible alternative or obtain permission.
2. Resolve the NIGMS registered-page retrieval and source identity for Anatomy A/B; do not silently replace the source with NCBI Bookshelf.
3. Prepare exact passage locator proposals for the SAA processing, provenance and description passages, with scope notes.
4. Narrow or supplement Acoustics C so environmental guidance, occupational exposure and jurisdiction-specific legal requirements are not conflated.
5. Continue the remaining 19 strict-queue triples in content-driven packages, checking prior report coverage and exact record versions before selection.
6. Keep all canonical JSON unchanged until rights, source identity, exact passage, bounded authorization and regression scope are documented.

This package is a desk review and routing artifact. It is not an independent technical certification, a full risk assessment, a rights clearance, a canonical correction, a Human View approval or M13 closure.
