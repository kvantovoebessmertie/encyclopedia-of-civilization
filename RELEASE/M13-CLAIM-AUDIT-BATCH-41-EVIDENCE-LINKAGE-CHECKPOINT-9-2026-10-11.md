# M13 Batch 41 — Evidence-Linkage Checkpoint 9 — 2026-10-11

## Scope and gate
Diagnostic review of Archival Science Claims A–C. Verified Claim record types/internal IDs, Evidence Use pointers, Source identity/URI, and the official Society of American Archivists (SAA) “Archives 101: Basic Principles” page. No D/E/B scores assigned; no content records modified. Batch 41 remains open.

## Findings

### A — `CLM-ARCHIVAL_SCIENCE-A`
- Claim: “Архивная работа включает функции оценки, комплектования, упорядочивания, описания, сохранения и предоставления доступа к материалам.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHIVAL_SCIENCE-A` points to the intended Claim and `SRC-ARCHIVAL_SCIENCE`; role `supports`.
- The SAA “Archives 101” page explicitly describes processing as appraisal, arrangement, description and preservation, and explains acquisition/appraisal and making collections accessible. This supports the core list, though the page distinguishes acquisition from the four processing activities; the Claim appropriately says archival work “includes” the functions rather than asserting they are all one processing stage.
- **Disposition:** substantive source fit PASS. Evidence Use should point to the relevant paragraphs/sections for auditability.

### B — `CLM-ARCHIVAL_SCIENCE-B`
- Claim: “Принцип происхождения требует сохранять различимость материалов разных создателей и не смешивать их происхождение в описании.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHIVAL_SCIENCE-B` points to the intended Claim and Source; role `supports`.
- The SAA page explicitly defines provenance and states that documents of one provenance must not be intermingled with another; it also says that origin should remain intelligible to researchers.
- **Disposition:** substantive source fit PASS, close textual match. A precise locator is still missing from the Evidence Use record.

### C — `CLM-ARCHIVAL_SCIENCE-C`
- Claim: “Архивное описание связано с контекстом создания и структурой коллекции, поэтому архивные материалы рассматриваются не только как отдельные документы.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHIVAL_SCIENCE-C` points to the intended Claim and Source; role `supports`.
- The SAA page describes intellectual control as understanding what items are, where they came from and how they fit together; it also explains that arrangement organizes collection components into a whole and that description creates a guide to the collection. This directly supports the claim's central context/collection-level point.
- **Disposition:** substantive source fit PASS. Exact locator absent.

## Structural and metadata observations
- All Claim IDs match filenames and all Claim → Evidence Use → Source pointers resolve correctly.
- All three Evidence Use descriptions repeat the same source-level wording without a section/paragraph locator. Here the underlying source fit is generally strong, but the records still do not provide reproducible passage-level traceability.
- Stored Source URI https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles resolves to the intended SAA page. The page is explicitly marked “PRELIMINARY DRAFT”; this status should be preserved in any later source-quality evaluation rather than treating the page as a formally adopted standard.
- No D/E/B scores assigned. No content JSON changed. Any source replacement, locator addition, or wording change must wait for a separately authorized correction scope.

## Public sources consulted
- Society of American Archivists, “Archives 101: Basic Principles”: https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles
- SAA, “Core Archival Functions”: https://www2.archivists.org/node/14804
- SAA Dictionary, “provenance”: https://dictionary.archivists.org/entry/provenance.html
