# M13 Claim Audit — Batch 41 Scored Block 01
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: Batch 41 candidates 1–6, acid-base basics and acoustics basics.
Status: **6 Claims scored; Batch 41 remains in progress.** This block does not certify overall corpus closure.

## Method
D = explanatory depth, E = claim-specific evidence fit, B = boundary discipline; each independently scored 0–3. Reviewed each Claim JSON, linked Evidence Use JSON and Source JSON. External sources were checked for claim-specific support. Generic Evidence Use descriptions lower E where the material is not pinpointed. No Claim, Evidence Use, Source, or Relation JSON was modified.

## Claim-level results

| # | Claim ID | D | E | B | Rationale and disposition |
|---:|---|---:|---:|---:|---|
| 1 | `CLM-ACID_BASE_BASICS-A` | 2 | 2 | 3 | OpenStax Chemistry 2e section 14.1 directly defines a Brønsted–Lowry acid as a proton donor and base as a proton acceptor. The claim is accurate and appropriately introductory. The linked Evidence Use description is generic and omits the section locator, so traceability is not fully represented in the record. Keep the definition tied to the Brønsted–Lowry framework rather than treating it as the only acid/base theory. |
| 2 | `CLM-ACID_BASE_BASICS-B` | 3 | 3 | 3 | The claim carefully states pH in terms of hydrogen-ion activity and limits concentration as an approximation to explicitly bounded conditions. The OpenStax chapter summary provides introductory pH context; the separate IUPAC Gold Book pH source directly supports the activity-based definition. The additional Evidence Use record identifies the metrological definition and precision boundary, making the evidence path stronger than a generic single-source link. Retain the conditions qualifier; do not reduce the claim to pH being universally defined by concentration alone. |
| 3 | `CLM-ACID_BASE_BASICS-C` | 2 | 2 | 3 | OpenStax section 14.6 directly states that solutions with appreciable amounts of a weak conjugate acid-base pair are buffers and experience only slight pH changes after small additions of acid or base. The claim closely matches this scope. The Evidence Use description is generic and does not name section 14.6; buffer capacity also means this should not be generalized to large additions. |
| 4 | `CLM-ACOUSTICS_BASICS-A` | 2 | 2 | 3 | WHO/Europe states that environmental noise is an important public-health risk and documents effects on health and well-being. This supports the core claim that noise exposure can be an environmental factor affecting health and well-being. The stored WHO guideline locator is valid but the Evidence Use description does not identify a relevant passage. The claim is appropriately qualified with “can.” |
| 5 | `CLM-ACOUSTICS_BASICS-B` | 1 | 1 | 2 | WHO guidance distinguishes sources such as road, rail, aircraft, wind turbines and leisure noise, and uses exposure indicators including long-term averages and night exposure. This supports source and temporal distinctions, but the broader wording “by place, time and nature of activity” is not directly established as a complete general rule by the linked guideline landing page. The statement is plausible but underspecified; evidence fit is weak until a precise passage or better-matched source is linked. Do not treat this score as a finding that the statement is false. |
| 6 | `CLM-ACOUSTICS_BASICS-C` | 2 | 2 | 3 | WHO's guideline recommendations are source-specific and use exposure/time indicators, supporting the claim that recommendations depend on noise source and exposure context. The claim additionally names applicable regulatory systems; that clause is not fully established by the single WHO source record and should be supported with jurisdiction-specific regulatory material if retained as a substantive proposition. The boundary is appropriately cautious, but the Evidence Use record is generic. |

## Source references checked
- OpenStax Chemistry 2e, section 14.1: https://openstax.org/books/chemistry-2e/pages/14-1-bronsted-lowry-acids-and-bases
- OpenStax Chemistry 2e, chapter 14 summary including sections 14.2 and 14.6: https://openstax.org/books/chemistry-2e/pages/14-summary
- IUPAC Gold Book, pH: https://goldbook.iupac.org/terms/view/P04524
- WHO/Europe, Environmental noise guidelines for the European Region: https://www.who.int/europe/publications/i/item/9789289053563
- WHO/Europe, Noise topic overview: https://www.who.int/europe/health-topics/noise

## Block tally
- Candidates in this block: 6 (Batch 41 worklist #1–6).
- Scored with D/E/B and individual rationale: 6/6.
- Claim/Evidence Use/Source/Relation records changed: 0.
- Batch 41 cumulative scored candidates: 6/100, pending final prior-score/alias reconciliation.
- Remaining candidates to score in Batch 41: 94, subject to the gate for prior-score overlap and source fit.

## Limitations / next actions
- These scores assess the quality and traceability of the represented claims in this corpus; they are not professional certification or a substitute for domain-specific assessment.
- Improve Evidence Use locators for acid-base A/C and acoustics A/C; obtain better claim-specific support for acoustics B and the regulatory-system clause in C.
- Continue with candidates 7–20 in efficient blocks, preserving individual rationales and logging overlap or source-fit exclusions before counting candidates as eligible.
- Keep PR #21 open as Draft and do not change `main`. M13 is not complete.
