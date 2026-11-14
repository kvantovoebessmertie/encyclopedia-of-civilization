# M13 Claim Review Batch 38 — Biostatistics Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed. This bounded batch is not domain closure.**

## Method
Reviewed three Claims in `biostatistics-basics`, linked Evidence Use records, source identity, Context and Scope. D = explanatory depth, E = claim-specific evidence fit, B = boundary discipline, each 0–3. This is an epistemic/content audit, not clinical guidance or validation of a statistical analysis.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM_BIOSTATISTICS_BASICS_A` | 1 | 1 | 2 | The statement gives a broad definition of biostatistics but no examples of methods, data types, or research questions. The linked Evidence Use description is generic, and the NCBI MeSH topic page identifies the subject rather than documenting a specific supporting passage. The educational Scope is clear. |
| `CLM_BIOSTATISTICS_BASICS_B` | 2 | 1 | 2 | The listed analytical purposes are reasonable but compressed: the Claim does not distinguish descriptive summaries, interval estimation, hypothesis tests, association measures, effect estimates or assumptions. The Evidence Use record repeats the same generic text and provides no claim-specific passage. Avoid reading “evaluate effects” as automatically establishing causality or clinical importance. |
| `CLM_BIOSTATISTICS_BASICS_C` | 3 | 1 | 3 | This is the strongest statement: it explicitly names study design, measurement quality, sampling, model assumptions and target population as interpretation constraints. However, its Evidence Use record is still generic and the cited MeSH landing page is not a claim-specific methodological source. Preserve the boundary; the listed factors are necessary considerations but not a complete bias assessment. |

## Findings
1. **Confirmed generic Evidence Use debt:** all three records use the same sentence, “Источник используется в пределах заявленного материала.” No source passage, definition, section, or methodological recommendation is identified.
2. **Source-type mismatch/limitation:** the linked NCBI MeSH page is a controlled-vocabulary/topic resource. It can help identify the field but, as represented here, does not establish detailed analytical claims. A future correction should use methodological sources tied to the particular proposition and preserve explicit source links.
3. **Practical depth gap:** the slice does not show a worked path from research question and target population through design, sampling, variable definitions, missing-data handling, uncertainty, model diagnostics, effect size, and a qualified interpretation. These are audit findings, not permission to add Records now.
4. **High-consequence boundary:** biostatistical outputs can influence medical/public-health decisions. Association is not automatically causation; statistical significance is not the same as effect magnitude, clinical relevance or public-health importance; and a model result does not override study limitations, ethical requirements, clinical judgement or applicable regulation. This introductory slice is not a substitute for qualified analysis of real health data.
5. No content Records were changed. Three additional Claims now have explicit D/E/B scores. Frozen denominator: 1,494 Claims; 111/1,494 (7.43%) have explicit scores in tracked batches. This percentage is scoring coverage only, not overall M13 completion.

## Records inspected
- `CONTENT/vertical-slices/biostatistics-basics/records/CLM-BIOSTATISTICS_BASICS-A.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/CLM-BIOSTATISTICS_BASICS-B.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/CLM-BIOSTATISTICS_BASICS-C.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/EU-BIOSTATISTICS_BASICS-A.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/EU-BIOSTATISTICS_BASICS-B.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/EU-BIOSTATISTICS_BASICS-C.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/SRC-BIOSTATISTICS_BASICS.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/CTX-BIOSTATISTICS_BASICS.json`
- `CONTENT/vertical-slices/biostatistics-basics/records/SCP-BIOSTATISTICS_BASICS.json`

## Source identity reviewed
- NCBI MeSH — Biostatistics: https://www.ncbi.nlm.nih.gov/mesh/?term=Biostatistics

## Acceptance status
Three additional Claim rows have explicit D/E/B scores and rationales. Keep continuous high-consequence screening active. Continue remaining Claim scoring; conduct methodology calibration at 747/1,494; after full scoring, complete the integrated defect ledger, Relation endpoint checks, evidence diversity/independence, Human View/adversarial review, independent re-review, authorized corrections with regression tests, and exact-head 3/3 CI plus final tree/PR/base/main verification. Survival/offline readiness remains a separate post-M13 phase. M13 remains open and is not CLEAN.
