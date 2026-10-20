# MVP — first real-record pilot candidate register

Date: 2026-10-18  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **SCREENING IN PROGRESS — no record approved for publication**

## Purpose

Record individual candidate screening for a small reader pilot. This register is deliberately separate from canonical content and from the synthetic preview fixtures. A candidate is not approved merely because its source is authoritative or its JSON links resolve.

## Candidate review

### Candidate 001 — plant transport basics

- **Candidate record:** `CLM-PLANT_BIOLOGY_BASICS-A@1`
- **Evidence Use:** `EU-PLANT_BIOLOGY_BASICS-A@1`
- **Source:** `SRC-PLANT_BIOLOGY_BASICS@1`
- **Claim:** “Растения перемещают воду, растворённые вещества и продукты фотосинтеза между органами.”
- **Current linked source:** OpenStax, *Biology 2e*, section 30.5, “Transport of Water and Solutes in Plants”: https://openstax.org/books/biology-2e/pages/30-5-transport-of-water-and-solutes-in-plants
- **Exact passage inspected:** The section introduction says roots, stems and leaves facilitate transport of water, nutrients and photosynthates throughout the plant; it identifies xylem and phloem as the main tissues responsible for this movement. Sections “Movement of Water and Minerals in the Xylem” and “Transportation of Photosynthates in the Phloem” give further detail. The current claim is a reasonable concise summary of that material.
- **Chain integrity:** Claim → Evidence Use → Source references resolve at version 1.
- **Evidence-fit issue:** The canonical Evidence Use contains only a generic description and no passage locator. The source is directly relevant, but the stored evidence chain does not preserve the pinpoint.
- **Rights issue:** OpenStax states that *Biology 2e* is licensed CC BY-NC-SA; reuse requires attribution and the same license for derivatives, and commercial use requires permission. The project has not recorded a rights determination for this use. This cannot be treated as automatically cleared.
- **Risk / scope:** Foundational plant biology, low direct consequence as currently worded. Keep the summary narrow; do not infer that transport mechanisms are identical across all plants or conditions.
- **Decision:** **HOLD — promising candidate, not approved.**
- **Required before reconsideration:** (1) record a precise section locator in an appropriately authorized/versioned Evidence Use correction, (2) complete and document the rights/attribution decision for the intended distribution model, (3) check the final reader rendering preserves source and scope, and (4) obtain independent review against the exact candidate commit.

### Candidate 002 — statistics basics

- **Candidate record:** `CLM-STATISTICS_BASICS-A@1`
- **Evidence Use:** `EU-STATISTICS_BASICS-A@1`
- **Primary Source:** `SRC-STATISTICS_BASICS@1` — NIST/SEMATECH Engineering Statistics Handbook
- **Additional source chain:** `EU-STATISTICS_BASICS-OPENSTAX@1` → `SRC-OPENSTAX-STATISTICS-BASICS@1`
- **Claim:** “Статистика предоставляет методы для описания данных, анализа вариации и количественного обоснования выводов.”
- **Passage review:** OpenStax *Introductory Statistics 2e*, section 1.1 directly supports the broad definition of statistics and the distinction between descriptive and inferential statistics. The current chain does not yet pinpoint the NIST passage for variation, and the full Claim is broader than the exact OpenStax passage reviewed.
- **Rights:** OpenStax identifies the textbook as CC BY-NC-SA 4.0; the intended distribution model and permitted reuse have not been cleared.
- **Preliminary D/E/B:** 1/1/1, recorded in `MVP-REAL-RECORD-PILOT-CANDIDATE-TRIAGE-001-STATISTICS-BASICS-2026-10-18.md`.
- **Decision:** **HOLD — candidate review only, not approved for pilot.**
- **Required before reconsideration:** locate exact NIST passages or propose a separately authorized narrower summary; add a claim-specific Evidence Use locator; record rights/attribution decision; obtain independent review; then rebuild and run release gates on the exact candidate commit.


### Candidate 003 — measurement uncertainty

- **Candidate record:** `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- **Evidence Use:** `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- **Source:** `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` — NIST Technical Note 1297
- **Claim:** “Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.”
- **Passage review:** NIST TN 1297 section 2.1 directly says a measurement result is complete only when accompanied by a quantitative statement of its uncertainty. Section 7 provides reporting requirements. The canonical Source record currently points only to the TN 1297 landing page, and the Evidence Use has no pinpoint locator.
- **Separate source caution:** The BIPM/JCGM VIM source is linked through a different Evidence Use to Claim B. It is not counted as corroboration for this Claim unless the record chain is deliberately and validly updated.
- **Preliminary D/E/B:** 1/2/1, documented in `MVP-REAL-RECORD-PILOT-CANDIDATE-TRIAGE-002-MEASUREMENT-UNCERTAINTY-2026-10-20.md`.
- **Decision:** **HOLD — promising candidate, not approved for pilot.**
- **Required before reconsideration:** add an exact section locator through the authorized/versioned correction workflow; document rights/attribution for the intended distribution; inspect final reader rendering; obtain independent review against the exact candidate commit.



### Candidate 004 — climate basics

- **Candidate record:** `CLM-CLIMATE_BASICS-A@1`
- **Evidence Use:** `EU-CLIMATE_BASICS-A@1`
- **Source:** `SRC-CLIMATE_BASICS@1` — NASA Science, “Climate Change”
- **Claim:** “Климат описывает долгосрочные характеристики и изменения погодных условий в системе Земли.”
- **Passage review:** NASA's linked overview discusses long-term observations and says multi-year data reveal patterns of a changing climate, but it does not directly define climate in the Claim's full terms. The canonical Evidence Use has no pinpoint locator.
- **Preliminary D/E/B:** 1/1/1, documented in `MVP-REAL-RECORD-PILOT-CANDIDATE-TRIAGE-004-CLIMATE-BASICS-2026-10-20.md`.
- **Decision:** **HOLD — source-fit and locator issue; not approved for pilot.**
- **Required before reconsideration:** identify a direct definition with an exact locator or propose a separately authorized, versioned narrowing; record rights/attribution for the planned use; inspect reader rendering; obtain independent review.

## Current decision

No real record is allowlisted for the pilot by this register. The plant-biology claim is a promising low-complexity candidate, but its generic Evidence Use and unresolved OpenStax reuse terms are release blockers. Do not add it to the reader build until those gates are resolved and the exact ID/version is explicitly approved.

## Review discipline

- Do not change canonical Claim, Evidence Use, or Source JSON as part of this screening.
- A rights decision applies to the specific use and distribution model; do not assume the licence is compatible.
- Approval of this Claim does not approve the entire slice or adjacent records.
- Keep the synthetic preview clearly labelled as synthetic until an explicit real-record allowlist and project-level release authorization exist.
