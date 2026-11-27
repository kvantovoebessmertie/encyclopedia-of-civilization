# MVP SI Units — Human View Desk Review — 2026-10-12

## Status

**Internal editorial desk review only; not an independent reader test and not publication approval.** This review examines the wording and likely comprehension of the three existing SI-unit Claims. It does not change canonical records or create a publication allowlist.

## Scope reviewed

- `CLM-SI-SEVEN-BASE@1`
- `CLM-SI-DERIVED@1`
- `CLM-SI-ACCURACY-BOUNDARY@1`
- Their current Evidence Use, Context and Scope records on branch `mvp-public-contribution-design-2026-10-11`.

## Claim-by-Claim findings

### 1. Seven base units — conditional candidate

**Current wording:** “SI состоит из семи базовых единиц, определения которых выражены через фиксированные значения определяющих констант.”

- **Likely comprehension:** A reader with a basic science background can understand the overall point. “Определяющие константы” and “фиксированные значения” may be opaque to a general reader without a short explanation.
- **Misreading risk:** A reader could think the seven base units are themselves the seven constants. The Claim says their definitions are expressed through fixed values of defining constants; it does not equate the two lists.
- **Reader-facing gloss to test in the renderer:** “В SI семь базовых единиц. Их определения связаны с точно зафиксированными значениями физических констант.”
- **Source note required:** The NIST page’s “Defining Constants” and “Base and Derived Units” sections. The existing Evidence Use description is relevant but does not yet record these pinpoints.
- **Desk disposition:** **PASS WITH CLARIFICATION** for wording, conditional on exact pinpoint, rights/attribution review and a rendered-page check.

### 2. Derived units — conditional candidate

**Current wording:** “Помимо семи базовых единиц, SI включает производные единицы; NIST отмечает 22 производные единицы со специальными названиями и символами.”

- **Likely comprehension:** Understandable if the page explains that derived units are built from base units.
- **Important boundary:** “22” refers to derived units with special names and symbols in the NIST classification, **not to the total number of derived units**. This distinction must remain visible and must not be lost in a summary or search snippet.
- **Reader-facing gloss to test in the renderer:** “Производные единицы получают из базовых единиц. NIST отдельно выделяет 22 такие единицы со специальными названиями и символами; это не общее число всех возможных производных единиц.”
- **Source note required:** The NIST “Base and Derived Units” section, with exact pinpoint in Evidence Use. The current EU description does not yet record the section.
- **Desk disposition:** **PASS WITH CLARIFICATION** for wording, conditional on preserving the count boundary, exact pinpoint, rights/attribution review and a rendered-page check.

### 3. Unit definition vs. measurement accuracy — HOLD

**Current wording:** “Выбор единицы SI задаёт единицу измеряемой величины, но сам по себе не устанавливает точность или неопределённость конкретного измерения; практическая реализация единиц относится к отдельному уровню метрологии.”

- **Likely comprehension:** The distinction is important but comparatively technical. A general reader may not know how “точность” differs from “неопределённость” or what “практическая реализация” means.
- **Evidence state:** The existing BIPM Evidence Use is a general description and does not identify a precise section. Rights/attribution and source-fit review are also unresolved in the candidate register.
- **Reader-facing gloss to test after source review:** “Единица задаёт, в чём выражают результат. Она сама по себе не гарантирует, насколько близок результат к истинному значению или насколько точно известно измеренное значение.”
- **Required next steps:** Verify this wording against a specific BIPM section, distinguish accuracy from measurement uncertainty without conflating them, record exact pinpoints, complete rights/attribution review, then conduct a rendered-page and specialist review.
- **Desk disposition:** **HOLD / EXCLUDE FROM FIRST PILOT** until those steps are complete.

## Reader-view requirements for the prototype

1. Show Claim A and Claim B as separate statements, not as one blended paragraph.
2. Explain “base unit”, “derived unit” and “defining constant” with a short, non-normative gloss.
3. Preserve the qualification that NIST’s 22 is the count of derived units with special names and symbols, not every derived unit.
4. Show source name, exact section pinpoint, and the limitation that this is an introductory account of SI structure.
5. Keep the distinction between technical build conformance, source fit, Human View review and editorial approval visible.
6. Do not display Claim C as “reviewed” or include it in the first real-record pilot while its source and wording remain on HOLD.

## Exit state

- Claims desk-reviewed: **3/3**.
- Wording disposition: **2 conditional candidates; 1 HOLD**.
- Independent user testing: **not performed**.
- Canonical Claim/Evidence Use/Source edits: **none**.
- Real-record preview allowlist: **not created**.
- Public reader, hosting and intake: **not deployed**.

Next step: add exact NIST pinpoints to the two conditional candidates only under an explicit bounded content authorization, then render the private prototype and conduct an actual comprehension check with a non-specialist reviewer before editorial sign-off.
