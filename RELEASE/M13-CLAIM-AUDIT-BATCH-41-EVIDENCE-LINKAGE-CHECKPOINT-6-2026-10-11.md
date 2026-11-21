# M13 Batch 41 — Evidence-Linkage Checkpoint 6 — 2026-10-11

## Scope and gate
Diagnostic review of Archaeology Basics Claims A–C. Verified Claim record types/internal IDs, each Evidence Use pointer, stored Source identity/URI, and the linked official Smithsonian Tropical Research Institute page. No D/E/B scores assigned; no content records modified. Batch 41 remains open.

## Findings

### A — `CLM-ARCHAEOLOGY_BASICS-A`
- Claim: “Археология изучает прошлые человеческие общества через материальные и другие сохранившиеся свидетельства.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHAEOLOGY_BASICS-A` points to the intended Claim and `SRC-ARCHAEOLOGY_BASICS`; role `supports`.
- Smithsonian Tropical Research Institute's Archaeology page describes archaeological work on past societies using comparative analysis of human and animal bones, material culture, plant microfossils, and genetic/biochemical analysis. This supports the central synthesis, although the page is a research-discipline overview rather than a formal general definition.
- **Disposition:** source fit PASS for the broad synthesis; pinpoint remains weak because the Evidence Use description gives no exact section or passage.

### B — `CLM-ARCHAEOLOGY_BASICS-B`
- Claim: “Археологическое исследование может объединять анализ артефактов, останков, растений, генетических и биохимических данных.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHAEOLOGY_BASICS-B` points to the intended Claim and Source; role `supports`.
- The STRI page directly lists comparative studies of human/animal bones and material culture, plant microfossil classification, and genetic and biochemical analysis. This is a close match to the Claim's list. “Артефакты” is a broad rendering of “material culture”; “plants” is more precisely represented in the source as plant microfossils/classification.
- **Disposition:** substantive source fit PASS. Evidence Use still needs a specific page/paragraph locator if the schema supports it.

### C — `CLM-ARCHAEOLOGY_BASICS-C`
- Claim: “Интерпретация археологических свидетельств требует связывать материальные находки с контекстом их обнаружения и другими независимыми линиями данных.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHAEOLOGY_BASICS-C` points to the intended Claim and Source; role `supports`.
- STRI explicitly describes a multidisciplinary approach and comparative analysis across material culture, bones, plant microfossils, and genetic/biochemical analysis. This supports the value of combining different evidence types. However, the page does not explicitly establish the stronger normative phrase “requires ... context of discovery,” nor does it characterize those lines as “independent.”
- **Disposition:** partial source fit. The multi-method component is supported; “requires,” discovery context, and independence are not directly established by the linked page. This is an evidence-fit limitation, not proof the methodological claim is false. A methods-focused source or corpus policy is needed before treating the whole sentence as fully supported.

## Structural and metadata observations
- All three Claim IDs match filenames and all Claim → Evidence Use → Source pointers resolve to the intended records.
- The three Evidence Use descriptions are identical and generic; none identifies the actual source passage. This weakens auditability even where topical/substantive support is good.
- Stored Source URI https://stri.si.edu/discipline/archaeology resolves to the official Smithsonian Tropical Research Institute Archaeology page.
- No D/E/B scores assigned. No content JSON changed. Any source addition, locator refinement, or Claim wording change must wait for a separately authorized correction scope.

## Public source consulted
- Smithsonian Tropical Research Institute, “Archaeology”: https://stri.si.edu/discipline/archaeology
- Smithsonian Tropical Research Institute, 2026 Visitors Guide, “Anthropology & Archaeology” (supporting context for multidisciplinary evidence types): https://stri.si.edu/sites/default/files/stri_visitors_guide_2026.pdf
