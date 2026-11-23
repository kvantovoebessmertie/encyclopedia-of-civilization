# First Edition — Cell Basics and Statistics Basics: Source, Rights and Record-Level Recheck

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `1c21f33b5ec3f9da430fcffba0b4e9aa83a6cb00`  
Status: BOUNDED READ-ONLY EVIDENCE / RIGHTS SCREEN — NO CANONICAL WRITES

## 1. Purpose and limits

This package advances two existing foundational candidates together because both can be screened from compact nine-/eleven-record subgraphs. It re-fetches every listed record at the inspection HEAD, checks claim-to-evidence links, tests exact source locators against accessible official material, and screens publication rights.

It is not a scientific peer review, legal opinion, complete slice audit, rights clearance, release approval, or authorization to change canonical records. The current canonical JSON is left untouched. No INCLUDE/EXCLUDE decision, allowlist entry, or public release permission is created.

## 2. Cell basics — exact nine-record closure

### 2.1 Re-fetched record identity

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-CELL_BASICS-A | 1 | Claim | `9108bc405fcd2de7cec8db6adaddabb3ae517d19` |
| CLM-CELL_BASICS-B | 1 | Claim | `d0b6c070766dccfa64c5cfcdbd0eea1dc6951bf9` |
| CLM-CELL_BASICS-C | 1 | Claim | `e4db4f3dc5cdb7e90eed838b53c7bc8b99274d1d` |
| EU-CELL_BASICS-A | 1 | Evidence Use | `c1513749a3bb194378bf238c806d1708200d27e9` |
| EU-CELL_BASICS-B | 1 | Evidence Use | `4b9fbe2a66efa47e98002158c2d56c246da0f42c` |
| EU-CELL_BASICS-C | 1 | Evidence Use | `ef2e4cd3f1655932998059fa59b2bcd943868c19` |
| SRC-CELL_BASICS | 1 | Source | `2d31e612aa1e3a2846f7ef6fff35c90a1ff22fb1` |
| CTX-CELL_BASICS | 1 | Context | `14efe43b2daa3aa836f2ab4480b5ad5a01128931` |
| SCP-CELL_BASICS | 1 | Scope | `596e3a28685a72d896e169d520edf1863a154505` |

### 2.2 Claim-level evidence findings

**Claim A — cell as basic structural and functional unit**

Canonical wording: «Клетка является основной структурной и функциональной единицей живых организмов.»

- OpenStax Biology 2e §4.1, “Studying Cells”, supports the narrower foundational propositions that the cell is the smallest unit of life, cells are the basic building blocks of organisms, and the cell is the basic unit of life.
- This is a close conceptual fit, but the exact phrase “structural and functional unit” should not be represented as a verbatim formulation from the cited passage without a separate source that explicitly states both terms.
- Current EU-A points only to the broad chapter introduction and has no pinpoint.

**Finding:** strong basic proposition; current evidence locator is inadequate and the wording needs a source-precise editorial formulation.

**Claim B — prokaryotic / eukaryotic nucleus distinction**

Canonical wording: «Прокариотические клетки не имеют мембранного ядра, тогда как эукариотические клетки имеют ядро.»

- OpenStax Biology 2e §4.2 describes prokaryotic cells as lacking a nucleus; §4.3 describes eukaryotic cells as having a membrane-bound nucleus.
- The canonical statement is a close match. “Мембранного ядра” is understandable, though “мембранной оболочки ядра” / “ядра, ограниченного мембраной” may be more precise Russian phrasing.
- EU-B currently points only to the chapter introduction; it should identify both sections if this source were ever cleared for use.

**Finding:** scientifically well-bounded at introductory level; evidence pinpoint and terminology review remain.

**Claim C — cellular structures have different functions**

Canonical wording: «Клеточные структуры выполняют различные функции внутри клетки.»

- This is too broad to be a useful, independently checkable claim as written. It does not identify which structures, which functions, or whether “cellular structures” includes organelles, membranes, cytoskeletal elements, ribosomes, and other components.
- OpenStax sections 4.3–4.6 discuss particular eukaryotic structures and functions, but the generic sentence does not map to a bounded passage or a stable proposition.
- EU-C is generic and provides no pinpoint.

**Finding:** semantic underspecification. A future editor should split this into specific structure/function propositions or narrow the statement; do not infer a rewrite.

### 2.3 Context and scope applicability

CTX-CELL_BASICS and SCP-CELL_BASICS both target Claim A v1 only. Their useful caution about cell type and organizational level must not be automatically displayed as if it governed Claims B and C. The apparent record graph is three Claim→EU edges to one Source, plus Context/Scope→Claim A.

### 2.4 Rights finding — material publication blocker

The current Source v1 points to OpenStax Biology 2e, Chapter 4 introduction. Its official pages carry an explicit notice that the book may not be used to train large language models or otherwise be ingested into LLMs or generative-AI offerings without OpenStax's prior written permission. The same pages state CC BY-NC-SA licensing for book content and separately describe reuse limitations for images and other assets.

This project is being developed with AI assistance. The repository's use of the textbook as source material therefore cannot be treated as rights-cleared merely because the proposed public text is paraphrased or the source page is publicly readable. The exact scope and applicability of the notice to any prior processing or future use requires rights-holder clarification; this report does not make a legal determination.

An alternative located during this review is the NCBI Bookshelf chapter “The Origin and Evolution of Cells” (Molecular Biology of the Cell), which supports the nucleus distinction and describes cell structures. However, NCBI Bookshelf hosting does not itself make the underlying publisher-authored textbook public domain or grant redistribution rights. The NCBI record identifies a commercial publisher and copyrighted work. It is a research lead, not a cleared substitute. No rights-compatible source for all three Claims was established in this pass.

### 2.5 Cell disposition

**HOLD — all three Claims.** Reasons: explicit OpenStax LLM-ingestion permission issue; no cleared replacement source established; EU pinpoints absent; Claim A wording is broader than its exact locator; Claim C is underspecified. No canonical record changes are authorized by this audit.

## 3. Statistics basics — exact eleven-record closure

### 3.1 Re-fetched record identity

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-STATISTICS_BASICS-A | 1 | Claim | `6160b12cabedbf2480295e1ae538ba450f8e1101` |
| CLM-STATISTICS_BASICS-B | 1 | Claim | `e676ab4f6115208c517659ecca8179fd3f832511` |
| CLM-STATISTICS_BASICS-C | 1 | Claim | `70670ac73c7bdf6397dedfc39546c1c73332b55d` |
| EU-STATISTICS_BASICS-A | 1 | Evidence Use | `be6e99ea6f0ac9ab9233ec9e647bb959a75362ff` |
| EU-STATISTICS_BASICS-B | 1 | Evidence Use | `c9e5cb8021bb3c946b0cc781a55c087faee002d9` |
| EU-STATISTICS_BASICS-C | 1 | Evidence Use | `8ee43d821178e7ce536455893aae1cc80c7b5ee8` |
| EU-STATISTICS_BASICS-OPENSTAX | 1 | Evidence Use | `3bec42010f7c9adc7f776432b760f44788385412` |
| SRC-STATISTICS_BASICS | 1 | Source | `3e5396831b7de4d8caa26fe5c9e3e1da5a368b7f` |
| SRC-OPENSTAX-STATISTICS-BASICS | 1 | Source | `32d82f2606b0c1c27d8d9e0b50178b72c9a5a32f` |
| CTX-STATISTICS_BASICS | 1 | Context | `0d9a68d31fbe8c5adebf3574824660f4f2c8962a` |
| SCP-STATISTICS_BASICS | 1 | Scope | `d392030615d92db4eeccb7d4588a80109afa876d` |

### 3.2 Claim-level evidence findings

**Claim A — purpose and scope of statistics**

Canonical wording: «Статистика предоставляет методы для описания данных, анализа вариации и количественного обоснования выводов.»

- NIST/SEMATECH e-Handbook describes itself as a reference for statistical methods, experiment design, appropriate analysis, understanding procedures and their assumptions, and interpreting scientific and engineering results.
- Its top-level structure includes Exploratory Data Analysis, process characterization, modeling, improvement, comparisons and reliability.
- OpenStax's introductory definition source is conceptually relevant, but the existing EU-OPENSTAX only corroborates Claim A and does not create evidence for Claims B/C.
- Both current EU records are generic rather than pinpointed.

**Finding:** broad conceptual fit to NIST, but the claim bundles several functions and needs specific handbook chapter/section locators for each phrase.

**Claim B — assumptions and data collection**

Canonical wording: «Статистический анализ требует явного внимания к предположениям метода и к способу получения данных.»

- The NIST/SEMATECH handbook overview explicitly says the handbook helps users understand statistical procedures and their underlying assumptions and design experiments / carry out appropriate analyses.
- That overview is a high-level statement of purpose, not sufficient pinpoint evidence for every method-specific assumption or every data-collection design.
- This Claim should be bounded to a general methodological principle, not read as a universal checklist or claim that all statistical methods share the same assumptions.

**Finding:** concept supported at handbook-overview level; EU-B requires chapter-level locators and narrower scope language.

**Claim C — experimental design and analysis**

Canonical wording: «Экспериментальный дизайн и анализ данных связаны: качество вывода зависит не только от вычислений, но и от постановки исследования.»

- NIST/SEMATECH explicitly treats design of experiments and statistical analysis as connected tasks; Handbook 151's stated scope includes experimental design.
- The claim's general warning that inference quality depends on study design is sound in direction, but the present sentence is broad and not tied to a specific design principle or example.
- EU-C is generic. The current source record does not identify a particular NIST chapter or section.

**Finding:** relevant source family exists; exact claim support and locator remain incomplete.

### 3.3 Source and rights review

**NIST/SEMATECH e-Handbook**

- The current NIST project page describes the handbook's purpose and chapter structure.
- NIST identifies Handbook 151 as a 2002 publication, with the record updated in 2021. This is a substantial age/currentness qualification: it remains a useful methodological reference but must not be described as a newly maintained comprehensive standard.
- The NIST landing page and publication metadata do not, by themselves, settle the rights status of every part of the handbook. SEMATECH and other contributors may be involved. Do not assume that every hosted passage, graphic, example or software component is automatically public domain. Obtain item-level rights evidence or use independently written factual paraphrases only after a rights review.

**OpenStax Introductory Statistics 2e**

- The current live preface says CC BY-NC-SA 4.0 and includes the explicit prohibition on LLM training/ingestion or generative-AI use without prior written permission.
- The downloadable PDF surfaced in this review states CC BY 4.0 for textbook content. This conflicts with the current live preface and should not be silently reconciled by selecting the more permissive statement.
- Both representations include the explicit LLM-ingestion permission notice. The project's AI-assisted workflow makes this a material unresolved issue regardless of the apparent CC license discrepancy.
- Do not use this source as a public-release rights basis without written permission and version-specific clarification. No figures, exercises, tables or textbook prose are proposed for reuse.

### 3.4 Context, scope and graph boundary

CTX-STATISTICS_BASICS and SCP-STATISTICS_BASICS target Claim A v1 only. The second OpenStax Evidence Use also targets Claim A only. It cannot be treated as corroboration for Claims B or C. The NIST source and three EU records form the apparent primary claim chains, but the record-level graph and actual full-slice dependencies should be validated again before any selection.

### 3.5 Statistics disposition

**HOLD — all three Claims.** Reasons: generic EUs without locators; source age/currentness qualification; unresolved NIST/SEMATECH rights at item level; explicit OpenStax LLM-ingestion restriction; and a live-preface/PDF license discrepancy for OpenStax Statistics 2e. No canonical record changes are authorized by this audit.

## 4. Consolidated next actions

1. Cell basics: locate a source with clear reuse and AI-processing permissions, or obtain written OpenStax permission; then pin §4.1, §4.2–4.3 and structure/function locators only if the chosen source supports them.
2. Cell basics: replace or split Claim C only under explicit editorial authorization; clarify Claim A's “structural and functional” wording against the exact evidence.
3. Statistics: investigate a rights-compatible source for the broad methods claims; do not assume NIST/SEMATECH material is uniformly public domain.
4. Statistics: if considering any OpenStax Statistics edition, resolve the exact edition/version license and LLM-ingestion permission in writing. Do not infer permission from a CC BY line in a PDF when the current live page says otherwise.
5. For both slices, version new Evidence Use records with precise locators rather than editing v1 records in place; preserve target-specific Context/Scope boundaries.
6. Re-run schema, dependency closure, rights, reader rendering and independent Human View only after the source and editorial blockers are resolved.

**Final disposition: 20 records inspected across the two slices; zero canonical writes; zero INCLUDE decisions; all six Claims remain HOLD.**
