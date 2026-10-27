# M13 Batch 13 — source-fit triage (rows 621–623): governance

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; Claims A/B have a plausible direct OECD source fit, Claim C has a material evidence-chain gap**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON is unchanged.

## Source trail and exact public-source locations

All three Claims reference `SRC-GOVERNANCE_BASICS@1`, whose URI is the OECD *Policy Framework on Sound Public Governance* full report:
https://www.oecd.org/en/publications/policy-framework-on-sound-public-governance_c03e01b3-en/full-report.html

Relevant source locations reviewed:
- **Introduction → “What is Sound Public Governance for the OECD?”** defines sound public governance in terms of formal/informal rules, procedures, practices and interactions that frame public authority and decision-making in the public interest, and describes the framework as three connected elements: values, enablers, instruments and tools. A section-level link is available at https://www.oecd.org/en/publications/policy-framework-on-sound-public-governance_c03e01b3-en/full-report/component-4.html
- **Part II: Sound Public Governance for Policy Formulation, Implementation and Evaluation** explicitly covers formulation, implementation, communication and evaluation of government policies.
- For the comparative-indicator limitation in Claim C, the linked OECD source is not sufficient by itself. The World Bank Worldwide Governance Indicators documentation says the WGI are composite estimates, reports standard errors / confidence intervals, and cautions that broad cross-country indicators are not definitive government ratings or substitutes for country-specific diagnostics: https://www.worldbank.org/en/publication/worldwide-governance-indicators/documentation and https://www.worldbank.org/en/publication/worldwide-governance-indicators/usage-advisory

The stored Evidence Use records contain descriptive summaries but no precise paragraph pinpoints. Claim C's Evidence Use text mentions WGI as an additional source, but its `source_ref` still points only to `SRC-GOVERNANCE_BASICS`; this is a source-chain mismatch that must be resolved explicitly, not treated as if the World Bank source were already linked.

## 1. `CLM-GOVERNANCE_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Публичное управление охватывает то, как государственные институты организуют принятие решений, взаимодействие между участниками и реализацию политики.”

**Assessment:** The claim gives a concise high-level synthesis rather than explaining institutional mechanisms or differences across systems (D2). The OECD introduction directly supports public governance as rules, practices and interactions framing public authority and decision-making; Part II supports policy implementation. Evidence fit is strong for a summary of the OECD framework (E3). However, the claim is phrased as a general description of public governance, while the stored source specifically defines *sound public governance in the OECD framework*. Keep that scope explicit and avoid implying this is the only universal definition (B2).

**Disposition:** Retain provisionally. Add separate section/paragraph pinpoints for the definition and policy-cycle material to Evidence Use; consider wording “В рамке OECD…” to align the scope with the cited source.

## 2. `CLM-GOVERNANCE_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “В рамках концепции OECD публичное управление рассматривается через взаимосвязанные ценности, обеспечивающие условия и инструменты государственной политики.”

**Assessment:** This is a compact representation of the framework's three elements, but it does not explain the individual values, enablers, or tools (D2). The OECD source directly identifies the connected elements as values, enablers, and instruments and tools, so the central proposition is strongly supported (E3). The phrase “обеспечивающие условия” may blur the technical category “enablers”; retain the framework-specific scope and preferably align terminology with the source's named three-part structure (B2).

**Disposition:** Strong candidate to retain. Add a pinpoint to the OECD introduction's three-element definition and verify Russian terminology against the intended translation.

## 3. `CLM-GOVERNANCE_BASICS-C` — provisional **D2 / E1 / B2**

**Claim:** “Сравнение публичного управления между странами использует определённые показатели и оценки; их следует интерпретировать с учётом методологии и неопределённости, а не как окончательный рейтинг правительств.”

**Assessment:** The claim states an important methodological caution but does not identify a specific indicator framework or explain uncertainty (D2). The linked OECD framework is not the direct source for cross-country governance-indicator methodology or statistical uncertainty. The Evidence Use description itself says the claim should be read with the World Bank Worldwide Governance Indicators, but no World Bank source record is referenced in the Evidence Use record. Therefore the current canonical evidence chain does not substantiate the full proposition (E1). The boundary is sound and aligns with the World Bank's warning that WGI are estimates with uncertainty, not definitive government ratings; however, this support is external to the currently linked source chain (B2).

**Disposition:** **HOLD for release-grade evidence.** Add a separate versioned World Bank Source record and explicit Evidence Use link with a pinpoint to the WGI methodology/usage advisory, or narrow the Claim to what the OECD source alone establishes. Do not silently change canonical records as part of this triage note.

## Batch accounting

- Individual Claims triaged in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use pinpoints verified in the stored records: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.

## Integrity note — mislabelled rows 618–620 report

The existing file `M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-618-620-GEODESY-2026-10-11.md` actually assesses `CLM-GEODESY_BASICS-A/B/C`, which are inventory rows **591–593**, not rows 618–620. The worklist identifies rows 618–620 as `CLM-GEOTECHNICAL_ENGINEERING_BASICS-A/B/C`. Treat the geodesy report as a duplicated/mislabelled artifact, not as a review of rows 618–620. Those geotechnical-engineering candidates remain pending until reviewed against their own Claim, Evidence Use and Source records. No existing report was overwritten and no canonical data was changed.
