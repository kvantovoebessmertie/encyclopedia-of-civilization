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

## Current decision

No real record is allowlisted for the pilot by this register. The plant-biology claim is a promising low-complexity candidate, but its generic Evidence Use and unresolved OpenStax reuse terms are release blockers. Do not add it to the reader build until those gates are resolved and the exact ID/version is explicitly approved.

## Review discipline

- Do not change canonical Claim, Evidence Use, or Source JSON as part of this screening.
- A rights decision applies to the specific use and distribution model; do not assume the licence is compatible.
- Approval of this Claim does not approve the entire slice or adjacent records.
- Keep the synthetic preview clearly labelled as synthetic until an explicit real-record allowlist and project-level release authorization exist.
