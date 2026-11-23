# M13 Duplicate-Score Adjudication — Nuclear Physics A–C
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: report-level adjudication only; original review reports and content records remain unchanged.

## Scope and rule
Batch 12 and Batch 17 independently scored the same three nuclear-physics Claims. This report reconciles the score conflicts against the stated 0–3 rubric and the actual Claim statements. It does not claim independent expert review. Scores remain reviewer judgments for triage.

## Adjudicated scores

| Claim | Batch 12 D/E/B | Batch 17 D/E/B | Adjudicated D/E/B | Reason |
|---|---:|---:|---:|---|
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A` | 1/1/2 | 2/1/2 | **1/1/2** | Statement defines the field and names its subject matter, but does not explain a mechanism or distinguish nuclear structure, reactions and decay. D=1 better matches “label-level proposition” in Batch 12. E=1 because EU is generic and IAEA locator broad. B=2: scope is reasonable but there are few explicit boundaries. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B` | 2/1/3 | 2/1/2 | **2/1/3** | Statement supplies a meaningful mechanism (nuclear-state changes may emit particles or electromagnetic radiation) and qualifies it by nucleus and transition. D=2 is consistent across both reviews. E=1 because the EU description is generic. B=3 is better supported: “may” and the nucleus/transition qualification avoid claiming every transition emits the same output. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C` | 1/1/3 | 2/1/2 | **1/1/3** | Statement is a methodological boundary, not an explanation of a nuclear mechanism. It names useful distinctions but offers no worked example; D=1 better reflects its abstract, principle-level nature. E=1 because the broad IAEA page is not mapped to this methodological recommendation. B=3 because it explicitly distinguishes mechanism, measurement and experimental conditions and cautions against treating everyday analogy as quantitative evidence. |

## Cross-checks performed
- Fetched each of the three Claim JSON records and corresponding Evidence Use records from the audit branch.
- Each Claim’s internal ID matches its Evidence Use `claim_ref`; all three Evidence Use records point to `SRC_NUCLEAR_PHYSICS_INFORMATION_BASICS` and use `supports`.
- The stored Source record points to the broad IAEA nuclear-science overview: https://www.iaea.org/topics/nuclear-science
- All three Evidence Use descriptions are generic (“Источник используется в пределах заявленного материала.”). This justifies the low evidence-fit score but does not alone establish that the factual claims are false.
- Batch 12 additionally identifies IAEA radiation-basics material for Claim B: https://www-ns.iaea.org/downloads/iec/radiation-basics-leaflet_e.pdf. The audit trail should pin the exact passage in a later evidence-quality pass.

## Disposition
1. Use the adjudicated scores above as the single report-ledger value for these three duplicated IDs; retain original Batch 12 and Batch 17 scores as provenance/history.
2. Do not count the duplicate rows as six distinct Claims.
3. During the separately authorized correction pass, improve the three Evidence Use descriptions with claim-specific passages and decide whether Claim C should be supported by an editorial/methodological reference rather than the IAEA topic page.
4. No Claim, Evidence Use, Source, Relation, or other content JSON was changed.
5. This resolves one report-score conflict only. It does not close full-corpus inventory reconciliation, semantic duplicate review, Relation audit, Human View, independent review, or M13.
