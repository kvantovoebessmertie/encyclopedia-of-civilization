# Foundational Sciences — Motion, Cell Biology and Statistics: Bounded Evidence Audit

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `127bd5d7856febbb2dea49178bb39c710a376e1b`  
Status: READ-ONLY EVIDENCE AND SEMANTIC AUDIT — NO CANONICAL WRITES AUTHORIZED

## 1. Purpose and scope

This package advances three foundational domains that can give the first edition genuine breadth beyond the Survival opening:

- Motion basics — reference frames, average motion and acceleration.
- Cell basics — cell theory, prokaryotic/eukaryotic distinction and cell structures.
- Statistics basics — description of data, variation, assumptions, experimental design and interpretation.

The audit re-fetched the canonical JSON records in the three slices and inspected the official source material and applicable OpenStax licensing statements. It is a bounded evidence/semantic screen, not full scientific peer review, rights clearance, a complete corpus dependency audit or publication approval.

No canonical record, candidate register, coverage manifest, decision, status or allowlist was changed. All candidates remain HOLD.

## 2. Motion basics — nine-record slice

### 2.1 Exact records re-fetched

| Record | Version | Type | Canonical blob SHA |
|---|---:|---|---|
| `CLM-MOTION_BASICS-A` | 1 | Claim | `2822a90fd7f9cc0081ec012c0cf8ca1956017c94` |
| `CLM-MOTION_BASICS-B` | 1 | Claim | `cd773f4b05117f152618d32b0f91459aabee3407` |
| `CLM-MOTION_BASICS-C` | 1 | Claim | `b19fb4053688914fc3fc7aad19e7a3ba039f651f` |
| `EU-MOTION_BASICS-A` | 1 | Evidence Use | `549bd88b51a89cbbeaed07805cf0e4de7b9e5004` |
| `EU-MOTION_BASICS-B` | 1 | Evidence Use | `fba51b0d7a6692947b8a13becf2ba1c5f4153af5` |
| `EU-MOTION_BASICS-C` | 1 | Evidence Use | `6e7003bc349606bed613f0e62c14efba3909f733` |
| `SRC-MOTION_BASICS` | 1 | Source | `08826cd7cd259af2425cdecb59a444d1bb966885` |
| `CTX-MOTION_BASICS` | 1 | Context | `2120a1f1da7b2aec652273c1caa5593e74fd496a` |
| `SCP-MOTION_BASICS` | 1 | Scope | `e2ba2e3cc419a6e87d4bf7094fe6c0f4ea8149ff` |

### 2.2 Claim-level findings

**Claim A — reference frame**

Current statement: «Положение объекта задаётся относительно выбранной системы отсчёта.»

- Directly supported by OpenStax Physics, §2.1 “Relative Motion, Distance, and Displacement”.
- The section defines position relative to a reference frame and explains that the description of motion depends on the selected frame.
- Current EU is generic and does not pin §2.1.
- Context A appropriately says kinematic quantities are interpreted relative to a reference frame and that a description of motion does not itself explain its cause. Context and Scope both target Claim A only.

Disposition: **HOLD — strong source fit; EU pinpoint remediation required.**

**Claim B — average speed / average velocity semantic mismatch**

Current statement: «Средняя скорость определяется отношением изменения положения к соответствующему интервалу времени.»

This is the material blocker in this slice.

- OpenStax Physics §2.2 explicitly distinguishes average speed from average velocity.
- Average speed = total distance travelled / elapsed time.
- Average velocity = displacement / elapsed time, where displacement is change in position.
- The current Claim describes displacement divided by time, but calls it «средняя скорость». In Russian educational usage this wording may be read as scalar average speed, while the formula corresponds to average velocity. The distinction matters: for a round trip, average speed is positive while average velocity may be zero.
- The EU currently cites only the broad chapter source and has no pinpoint.
- The Claim must not be treated as a safe, unambiguous statement until an editor resolves the intended quantity.

Recommended editorial alternatives for a future authorized version:
1. If the intended quantity is average velocity: «Средняя векторная скорость равна отношению перемещения к интервалу времени.»
2. If the intended quantity is average path speed: «Средняя путевая скорость равна отношению пройденного пути к затраченному времени.»

These are proposals for review, not canonical replacements. Do not silently rewrite Claim B or assume the intended meaning.

Disposition: **HOLD — terminology/semantic ambiguity is a substantive correction blocker.**

**Claim C — acceleration**

Current statement: «Ускорение описывает изменение скорости во времени.»

- OpenStax Physics §2.4 defines acceleration as the rate at which velocity changes.
- The source clarifies that velocity is a vector: acceleration may reflect a change in magnitude (speed), direction, or both. Thus an object moving at constant speed around a curve is still accelerating.
- The current Russian word «скорость» can be read as scalar speed. For a physics definition, the intended vector quantity should be explicit.
- The EU is generic and should pin §2.4. The reader should not reduce acceleration to “speeding up”.

Recommended editorial clarification, subject to authorization: «Ускорение характеризует скорость изменения вектора скорости во времени.» This is not a canonical edit.

Disposition: **HOLD — direct source support, but precision of Russian wording and EU pinpoint require review.**

### 2.3 Motion source and rights

Current Source v1 points to OpenStax Physics, “Introduction to One-Dimensional Kinematics”:
https://openstax.org/books/physics/pages/2-introduction-to-one-dimensional-kinematics

More precise official OpenStax locators:

- §2.1 Reference frames, position and displacement:
  https://openstax.org/books/physics/pages/2-1-relative-motion-distance-and-displacement
- §2.2 Speed and velocity:
  https://openstax.org/books/physics/pages/2-2-speed-and-velocity
- §2.4 Acceleration:
  https://openstax.org/books/physics/pages/2-4-acceleration
- Chapter 2 summary:
  https://openstax.org/books/physics/pages/2-section-summary
- Physics book preface and licence:
  https://openstax.org/books/physics/pages/preface

The Physics book preface identifies CC BY 4.0. This is materially different from OpenStax titles that use CC BY-NC-SA. It permits reuse/adaptation with attribution under the licence, subject to checking each separately credited image/asset and preserving required attribution. The proposed reader needs only independently authored factual paraphrases and bibliographic metadata; no textbook figures, images, problem sets or video content are proposed.

This licence finding applies to the identified OpenStax Physics source, not to the whole Encyclopedia or to other OpenStax books.

### 2.4 Motion closure and next work

The nine-record slice has a simple apparent graph: three Claim→EU→one Source chains, plus Context/Scope targeting Claim A. Before selection, verify whether the existing reader's dependency model requires Context/Scope for each selected Claim or whether the current target-relative model is intentionally Claim-A-only. Do not display CTX/SCP as automatically governing Claims B and C.

Required bounded remediation:
1. Version EU A/B/C with section-level pinpoints only after the Evidence Use locator schema is confirmed.
2. Resolve Claim B's average-speed/average-velocity meaning through explicit owner/editor authorization.
3. Clarify Claim C's vector-velocity meaning through explicit authorization if the project requires strict terminology.
4. Re-run exact dependency, schema, rights and reader checks.
5. Keep all three Claims HOLD until review is complete.

## 3. Cell basics — nine-record slice

### 3.1 Exact records re-fetched

| Record | Version | Type | Canonical blob SHA |
|---|---:|---|---|
| `CLM-CELL_BASICS-A` | 1 | Claim | `9108bc405fcd2de7cec8db6adaddabb3ae517d19` |
| `CLM-CELL_BASICS-B` | 1 | Claim | `d0b6c070766dccfa64c5cfcdbd0eea1dc6951bf9` |
| `CLM-CELL_BASICS-C` | 1 | Claim | `e4db4f3dc5cdb7e90eed838b53c7bc8b99274d1d` |
| `EU-CELL_BASICS-A` | 1 | Evidence Use | `c1513749a3bb194378bf238c806d1708200d27e9` |
| `EU-CELL_BASICS-B` | 1 | Evidence Use | `4b9fbe2a66efa47e98002158c2d56c246da0f42c` |
| `EU-CELL_BASICS-C` | 1 | Evidence Use | `ef2e4cd3f1655932998059fa59b2bcd943868c19` |
| `SRC-CELL_BASICS` | 1 | Source | `2d31e612aa1e3a2846f7ef6fff35c90a1ff22fb1` |
| `CTX-CELL_BASICS` | 1 | Context | `14efe43b2daa3aa836f2ab4480b5ad5a01128931` |
| `SCP-CELL_BASICS` | 1 | Scope | `596e3a28685a72d896e169d520edf1863a154505` |

### 3.2 Claim-level findings

**Claim A — cell as the basic structural and functional unit**

Current statement: «Клетка является основной структурной и функциональной единицей живых организмов.»

- OpenStax Biology 2e §4.1 states that a cell is the smallest unit of a living thing, cells are the basic building blocks of organisms, and the cell theory identifies the cell as the basic unit of life.
- The wording “structural and functional unit” is a standard introductory formulation, but the exact selected section should be checked for the complete formulation rather than treating a paraphrase as a verbatim source statement.
- EU A currently points to the chapter introduction rather than §4.1 and is otherwise generic.
- Context and Scope target Claim A only. Context says biological claims apply to the stated cell type and organizational level and warns against confusing the presence of a structure with an observed state. This is useful but should not be propagated automatically to Claims B/C.

Disposition: **HOLD — strong foundational fit; EU §4.1 pinpoint and rights review required.**

**Claim B — prokaryotic vs eukaryotic nucleus**

Current statement: «Прокариотические клетки не имеют мембранного ядра, тогда как эукариотические клетки имеют ядро.»

- OpenStax Biology 2e §4.2 describes prokaryotic cells as lacking a nucleus and other membrane-bound organelles.
- §4.3 describes eukaryotic cells as having a membrane-bound nucleus and other membrane-bound organelles.
- This is a direct and precise match.
- Current EU B points to the broad chapter introduction and needs both precise section locators.
- A reader explanation should avoid implying that prokaryotes have no DNA: their DNA is present in a nucleoid region and is not enclosed by a nuclear membrane.

Disposition: **HOLD — direct source fit; EU pinpoint and explicit DNA/nucleus distinction needed in reader treatment.**

**Claim C — cellular structures perform different functions**

Current statement: «Клеточные структуры выполняют различные функции внутри клетки.»

- OpenStax Biology 2e §4.3 describes membrane-bound organelles and their roles; Chapter 4 summary provides examples including ribosomes in protein synthesis, mitochondria in cellular respiration, and vesicles/vacuoles in storage and transport.
- The statement is very broad. The source supports differentiated functions of cellular components, but the Claim does not name which structures or functions. It may be true but is low-information and risks serving as an empty placeholder.
- Current EU C is generic and should pin §4.3 or an appropriately bounded set of sections.
- The current Context/Scope do not target Claim C. Do not imply that their restrictions govern C without a separate applicability review.

Disposition: **HOLD — broad but supportable proposition; editorial value and exact evidence scope need review.**

### 3.3 Cell source and rights

Current Source v1 points to:
https://openstax.org/books/biology-2e/pages/4-introduction

More precise official locators:

- §4.1 Studying Cells / cell theory:
  https://openstax.org/books/biology-2e/pages/4-1-studying-cells
- §4.2 Prokaryotic Cells:
  https://openstax.org/books/biology-2e/pages/4-2-prokaryotic-cells
- §4.3 Eukaryotic Cells:
  https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells
- Chapter 4 summary:
  https://openstax.org/books/biology-2e/pages/4-chapter-summary
- Biology 2e preface and licence:
  https://openstax.org/books/biology-2e/pages/preface

The official Biology 2e preface identifies CC BY-NC-SA 4.0. It permits noncommercial distribution, remixing and adaptation with attribution and ShareAlike; commercial use is not permitted by that licence. The preface separately states that the book may not be used for LLM training or ingestion into generative-AI offerings without prior written permission. Separately credited assets may carry additional terms.

Consequences:
- This source is useful for factual verification, but it is not automatically compatible with a commercial or mixed commercial/noncommercial first-edition distribution model.
- The licence does not automatically attach to every independently authored factual statement merely because the source was consulted; however, no derivative text, figures, images, tables, questions or other protected textbook material should be copied into the product without a documented rights analysis.
- The project must determine whether it will use only independently authored factual paraphrases and bibliographic citation, seek permission for any derivative use, or select a different source with compatible rights.
- No rights clearance is inferred by this audit.

### 3.4 Cell closure and next work

The nine-record slice contains three Claim→EU→Source chains and one Context/Scope pair targeting Claim A. The reader and selection model must preserve that target boundary.

Required bounded remediation:
1. Version EU A to §4.1; EU B to §§4.2–4.3; EU C to §4.3 / chapter summary, subject to exact locator schema.
2. Decide whether Claim C adds sufficient information for the first edition or should remain HOLD pending a more informative proposition; no deletion or rewrite is authorized.
3. Perform an explicit rights compatibility decision for Biology 2e CC BY-NC-SA 4.0 before any redistribution decision.
4. Verify all Claim/EU/Source exact versions and Context/Scope applicability in the actual reader.
5. Keep all three Claims HOLD until the rights and editorial gates are closed.

## 4. Statistics basics — eleven-record slice

### 4.1 Exact records re-fetched

| Record | Version | Type | Canonical blob SHA |
|---|---:|---|---|
| `CLM-STATISTICS_BASICS-A` | 1 | Claim | `6160b12cabedbf2480295e1ae538ba450f8e1101` |
| `CLM-STATISTICS_BASICS-B` | 1 | Claim | `e676ab4f6115208c517659ecca8179fd3f832511` |
| `CLM-STATISTICS_BASICS-C` | 1 | Claim | `70670ac73c7bdf6397dedfc39546c1c73332b55d` |
| `EU-STATISTICS_BASICS-A` | 1 | Evidence Use | `be6e99ea6f0ac9ab9233ec9e647bb959a75362ff` |
| `EU-STATISTICS_BASICS-B` | 1 | Evidence Use | `c9e5cb8021bb3c946b0cc781a55c087faee002d9` |
| `EU-STATISTICS_BASICS-C` | 1 | Evidence Use | `8ee43d821178e7ce536455893aae1cc80c7b5ee8` |
| `EU-STATISTICS_BASICS-OPENSTAX` | 1 | Evidence Use | `3bec42010f7c9adc7f776432b760f44788385412` |
| `SRC-STATISTICS_BASICS` | 1 | Source | `3e5396831b7de4d8caa26fe5c9e3e1da5a368b7f` |
| `SRC-OPENSTAX-STATISTICS-BASICS` | 1 | Source | `32d82f2606b0c1c27d8d9e0b50178b72c9a5a32f` |
| `CTX-STATISTICS_BASICS` | 1 | Context | `0d9a68d31fbe8c5adebf3574824660f4f2c8962a` |
| `SCP-STATISTICS_BASICS` | 1 | Scope | `d392030615d92db4eeccb7d4588a80109afa876d` |

### 4.2 Claim-level findings

**Claim A — descriptive methods, variation and quantitative conclusions**

Current statement: «Статистика предоставляет методы для описания данных, анализа вариации и количественного обоснования выводов.»

- NIST/SEMATECH Engineering Statistics Handbook describes statistical methods for scientists and engineers, including design of experiments and appropriate analysis, and says it is intended to help users understand procedures, assumptions and interpretation.
- NIST Handbook Chapter 1 includes Exploratory Data Analysis and quantitative techniques. Section 1.3.5.6 “Measures of Scale” explicitly describes characterizing the spread/variability of a data set.
- OpenStax Introductory Statistics 2e §1.1 provides an independent basic definition of statistics as collection, analysis, interpretation and presentation of data.
- The current EU A is generic. An additional OpenStax EU exists and targets Claim A, but its rights and exact scope must be assessed independently.
- The Claim is a broad introductory summary. The NIST Handbook is engineering-oriented; OpenStax provides broader introductory framing. The final evidence text should not imply that either source exhausts all statistical methods or guarantees causal conclusions.

Disposition: **HOLD — source complementarity is promising; both Evidence Use records need precise locators and rights review.**

**Claim B — assumptions and data collection**

Current statement: «Статистический анализ требует явного внимания к предположениям метода и к способу получения данных.»

- NIST/SEMATECH Handbook explicitly includes assumptions and data collection across several analytical chapters. Its detailed table of contents lists EDA assumptions, process characterization assumptions and data collection, process modeling assumptions, and design-of-experiments assumptions.
- This supports the general importance of assumptions and data-collection design, but the Claim is broad and must not be read as a universal fixed checklist. Assumptions depend on the chosen method and study design.
- EU B is generic and does not identify the relevant NIST chapter/section.
- OpenStax EU does not target Claim B; do not propagate its Claim-A support.

Disposition: **HOLD — plausible direct support; exact NIST chapter/section pinpoints and a method-relative scope statement are required.**

**Claim C — experimental design and analysis are connected**

Current statement: «Экспериментальный дизайн и анализ данных связаны: качество вывода зависит не только от вычислений, но и от постановки исследования.»

- NIST Handbook Chapter 5, Process Improvement, includes “What is experimental design?”, “What are the steps of DOE?”, “Assumptions”, “Choosing an experimental design” and “Analysis of DOE Data”.
- Section 5.3 explicitly describes choosing an experimental design to obtain the results needed, with steps including objectives, process variables/levels and selection of design.
- This supports the connection between study design and analysis. The phrase “quality of inference” is broader than any one design recipe and should be presented as a methodological principle, not as a guarantee that a good design alone ensures valid conclusions.
- EU C is generic and needs exact pinpoints. The additional OpenStax EU A does not support Claim C.

Disposition: **HOLD — strong NIST conceptual fit; precise EU locator and boundary against overclaiming are required.**

### 4.3 Statistics sources and rights

**NIST/SEMATECH Engineering Statistics Handbook**

- Handbook landing page:
  https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook
- Detailed table of contents:
  https://www.itl.nist.gov/div898/handbook/dtoc.htm
- Chapter 1 / exploratory data analysis detailed contents:
  https://www.itl.nist.gov/div898/handbook/eda/eda_d.htm
- Measures of scale / variability:
  https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm
- Process improvement / design of experiments:
  https://itl.nist.gov/div898/handbook/pri/section3/pri3.htm

NIST Handbook is a strong technical reference, but its coverage is primarily engineering/statistical methods. The final EU must cite the exact chapter and section appropriate to each Claim, not only the broad landing page. This audit does not infer a blanket licence for all NIST-hosted materials; check the specific work's reuse notice and any third-party content before redistribution.

**OpenStax Introductory Statistics 2e**

- §1.1 definitions:
  https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms
- Book preface / licence:
  https://openstax.org/books/introductory-statistics-2e/pages/preface

The exact edition's rights notice must be captured before any use. Do not assume the licence of OpenStax Physics (CC BY) applies to Introductory Statistics 2e. The OpenStax secondary Evidence Use currently targets Claim A only; it is not a blanket source for Claims B and C.

### 4.4 Statistics closure and next work

The 11-record slice contains three Claim→EU→NIST Source chains, an additional Claim-A→EU→OpenStax Source chain, and Context/Scope targeting Claim A only.

Required bounded remediation:
1. EU A: pin NIST Handbook EDA/variation material and OpenStax §1.1 separately; preserve source-specific scope and rights.
2. EU B: identify the exact NIST sections on assumptions and data collection relevant to the statement; distinguish method assumptions from universal rules.
3. EU C: pin Chapter 5 sections 5.1.1, 5.1.3, 5.2 and 5.3 as needed; avoid implying design alone guarantees valid inference.
4. Verify the actual current NIST page paths and applicable reuse notices.
5. Inspect whether the current Source record and EU schema support all required exact locators; version rather than overwrite records.
6. Preserve Context/Scope as Claim-A-only unless separately authorized and justified.
7. Keep the whole slice HOLD pending source, rights, editorial and reader review.

## 5. Cross-slice conclusions

| Slice | Best candidate strength | Blocking issue | Next action | Disposition |
|---|---|---|---|---|
| Motion | OpenStax Physics source is precise and CC BY 4.0 | Claim B average-speed/average-velocity ambiguity; Claim C vector precision; generic EUs | Prepare narrow versioned EU corrections and separate Claim-B editorial authorization request | HOLD |
| Cell | Strong introductory biology support from Biology 2e §§4.1–4.3 | CC BY-NC-SA 4.0 rights compatibility; Claim C information value; Context/Scope target only A | Prepare versioned EU pinpoint proposal and item-level rights decision | HOLD |
| Statistics | NIST handbook directly covers variation, assumptions, data collection and experimental design; OpenStax independently supports Claim A | Generic EUs, NIST engineering scope, OpenStax NC-SA rights and Claim-specific source boundaries | Prepare versioned EU locator proposal and rights/source review | HOLD |

## 6. Change-control and verification

- Exact record files were retrieved from the PR branch and their blob SHAs are recorded above.
- Motion: 9 records re-fetched and parsed.
- Cell: 9 records re-fetched and parsed.
- Statistics: 11 records re-fetched and parsed.
- Official OpenStax source pages and book prefaces were inspected; NIST Handbook table of contents and relevant sections were inspected.
- No canonical JSON was written or changed.
- No Claim text, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference or Decision was changed.
- No candidate register, denominator, coverage manifest, allowlist or release state was changed.
- No INCLUDE/EXCLUDE disposition was assigned; all three slices remain HOLD.
- No private preview was built or claimed in this package.
- No merge, deployment, public distribution or main-branch update occurred.
- Documentation-only changes do not establish exact-head CI PASS.

## 7. Next execution queue

1. SI private preview: pursue only the already-authorized private seven-record preview; do not change its allowlist, distribution boundary or public-release state.
2. Motion: draft a separate, narrow owner decision packet for Claim B terminology and versioned EU pinpoints for A/B/C.
3. Cell: draft a versioned EU pinpoint proposal and rights compatibility options for the Biology 2e NC-SA source.
4. Statistics: draft versioned EU locator proposals and inspect the precise NIST reuse/attribution boundary plus OpenStax 2e rights.
5. Reconcile all new exact-version records with the first-edition candidate master only after any authorized canonical changes; never count a proposal as a new canonical record or INCLUDE decision.

**Final disposition: three additional foundational domains substantively screened; all remain HOLD. Evidence paths are now specific enough to prepare controlled remediation, but no publication admission is justified.**
