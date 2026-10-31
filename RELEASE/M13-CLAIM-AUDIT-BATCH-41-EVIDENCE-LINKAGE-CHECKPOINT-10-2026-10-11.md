# M13 Batch 41 — Evidence-Linkage Checkpoint 10 — 2026-10-11

## Scope and gate
Diagnostic review of Art History Basics Claims A–C. Verified Claim record types/internal IDs, Evidence Use links, Source identity/URI, and relevant Smarthistory material. No D/E/B scores assigned; no content records modified. Batch 41 remains open.

## Findings

### A — `CLM-ART_HISTORY_BASICS-A`
- Claim: “История искусства исследует произведения искусства в их визуальном, историческом, культурном и социальном контексте.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ART_HISTORY_BASICS-A` points to the intended Claim and `SRC-ART_HISTORY_BASICS`; role `supports`.
- Smarthistory's “Understanding art, an introduction” distinguishes visual/formal analysis from contextual analysis and states that much art-historical research examines artworks as cultural artifacts in relation to historical context, including time/place, why/by whom made, original function and later cultural significance. This supports the visual + historical/cultural core. The exact adjective “social” is not isolated as a separate explicit element in the passage reviewed, but is compatible with the broader cultural-context synthesis.
- **Disposition:** source fit PASS for the core synthesis. The stored source is a curated guide landing page rather than a pinpoint to the explanatory essay; the Evidence Use locator is generic.

### B — `CLM-ART_HISTORY_BASICS-B`
- Claim: “Формальный анализ рассматривает такие элементы, как линия, форма, цвет, пространство, текстура, свет и композиция.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ART_HISTORY_BASICS-B` points to the intended Claim and Source; role `supports`.
- Smarthistory's formal-analysis introduction explicitly lists composition, viewpoint, figure and space, form, line, color, light and texture. It directly supports nearly all the Claim's terms. “Shape” is closely related to form; “composition” is explicit.
- **Disposition:** source fit PASS, close match. Exact essay-level locator should be recorded for reproducibility.

### C — `CLM-ART_HISTORY_BASICS-C`
- Claim: “Иконография и другие методы интерпретации помогают связывать визуальные мотивы и формы с историческими и культурными значениями.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ART_HISTORY_BASICS-C` points to the intended Claim and Source; role `supports`.
- Smarthistory explicitly explains iconography as interpreting the meaning of image subject matter and notes that when meaning is obscure, art historians use historical context, texts and other imagery from the period. This directly supports the main claim.
- **Disposition:** source fit PASS for the core statement. “Other methods” is broad but the source's discussion of contextual comparison supports it as a synthesis. The Evidence Use record lacks a precise locator.

## Structural and metadata observations
- All Claim IDs match filenames and all Claim → Evidence Use → Source pointers resolve correctly.
- The same generic Evidence Use description is repeated across all three Claims and does not identify which essay or section of the curated guide supports the statement.
- Stored Source URI https://smarthistory.org/curated-guide/the-basics-of-art-history/ is a current curated guide. More direct source locators for the reviewed propositions are:
  - Formal and contextual analysis: https://smarthistory.org/introduction-to-art-historical-analysis/
  - Formal analysis terminology: https://smarthistory.org/introduction-to-art-historical-analysis/
  - Iconography/contextual interpretation: same introduction, “Subject matter / iconography” section.
- No D/E/B scores assigned. No content JSON changed. Locator changes must wait for a separately authorized correction scope.

## Public sources consulted
- Smarthistory, “The Basics of Art History”: https://smarthistory.org/curated-guide/the-basics-of-art-history/
- Smarthistory, “Understanding art, an introduction”: https://smarthistory.org/introduction-to-art-historical-analysis/
