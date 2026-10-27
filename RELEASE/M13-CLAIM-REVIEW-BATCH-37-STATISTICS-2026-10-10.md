# M13 Claim Review Batch 37 — Statistics Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed. This is a bounded review batch, not domain closure.**

## Method
Reviewed the three Claims in `statistics-basics`, their linked Evidence Use records, source identity, Context and Scope. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-STATISTICS_BASICS-A` | 1 | 1 | 2 | The statement summarizes several purposes of statistics but does not explain descriptive versus inferential methods, variation, uncertainty, or how conclusions are quantified. Its Evidence Use text is generic and supplies no specific handbook section or passage. The Scope appropriately describes the slice as introductory. |
| `CLM-STATISTICS_BASICS-B` | 3 | 2 | 3 | This Claim appropriately ties inference to method assumptions and data quality/representativeness, while avoiding the implication that all methods share the same assumptions. Its Evidence Use text is substantially more specific about exploratory analysis and model assumptions. However, it still does not identify exact sections, and the source identity/locator is only the handbook landing page, so source-level traceability remains incomplete. |
| `CLM-STATISTICS_BASICS-C` | 3 | 2 | 3 | The Claim usefully distinguishes explanatory variables and outcomes in experiments, identifies random assignment as a way to reduce hidden-factor influence, and cautions that observed differences alone do not prove causality. Evidence Use is more specific about experimental design, but refers to an additional OpenStax material without a separate linked Source record/locator in the reviewed record set. Exact passages and design limits are not specified. |

## Findings
1. **Evidence specificity is uneven:** Claim A has generic Evidence Use text, while B and C are more explanatory. The latter still need exact source-section/passages to make claim-level verification reproducible.
2. **Source-linkage gap:** the Evidence Use description for C mentions OpenStax, but the reviewed Evidence Use record's `source_ref` points only to `SRC-STATISTICS_BASICS` (NIST/SEMATECH). A source mentioned in prose but not represented as a separately linked Source record is harder to verify and maintain.
3. **Practical depth gaps:** the slice does not yet provide a worked example moving from a research question and sampling design through descriptive summaries, uncertainty/intervals, model assumptions, effect size, and a properly qualified conclusion. For experimental claims, distinguish random assignment from random sampling; the former supports causal comparisons under design assumptions, while the latter concerns population representation.
4. **Boundary:** no single statistical method fits every data type or study design. Observational association does not by itself establish causality; random assignment reduces some confounding risks but does not guarantee flawless execution, adequate power, generalizability or absence of bias. Real-data analysis and research ethics/legal requirements remain outside this introductory slice's scope.
5. **No content Records were changed.** Three additional Claims now have explicit D/E/B scores. The frozen denominator remains 1,494; 108/1,494 (7.23%) have explicit scores in tracked batches. This is scoring coverage only, not completion of M13.

## Records inspected
- `CONTENT/vertical-slices/statistics-basics/records/CLM-STATISTICS_BASICS-A.json`
- `CONTENT/vertical-slices/statistics-basics/records/CLM-STATISTICS_BASICS-B.json`
- `CONTENT/vertical-slices/statistics-basics/records/CLM-STATISTICS_BASICS-C.json`
- `CONTENT/vertical-slices/statistics-basics/records/EU-STATISTICS_BASICS-A.json`
- `CONTENT/vertical-slices/statistics-basics/records/EU-STATISTICS_BASICS-B.json`
- `CONTENT/vertical-slices/statistics-basics/records/EU-STATISTICS_BASICS-C.json`
- `CONTENT/vertical-slices/statistics-basics/records/SRC-STATISTICS_BASICS.json`
- `CONTENT/vertical-slices/statistics-basics/records/CTX-STATISTICS_BASICS.json`
- `CONTENT/vertical-slices/statistics-basics/records/SCP-STATISTICS_BASICS.json`

## Source identity reviewed
- NIST/SEMATECH Engineering Statistics Handbook: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook

## Acceptance status
Three additional Claim rows have explicit D/E/B scores and rationales. No content Records were modified. Continue Claim scoring and continuous high-consequence screening; perform the planned methodology calibration at 747/1,494; after all Claims are scored, complete the integrated defect ledger, Relation endpoint checks, evidence diversity/independence, Human View/adversarial review, independent re-review, authorized corrections with regression tests, and final exact-head 3/3 CI plus tree/PR/base/main verification. Survival/offline readiness remains a separate post-M13 phase. M13 remains open and is not CLEAN.
