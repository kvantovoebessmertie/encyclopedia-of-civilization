# M4 Unified Debt Map — 2026-10-08

## Status
M4 remains OPEN. This map consolidates findings from substantive, evidence-independence, Human View and Relation audits. It is a correction control document, not a CLEAN declaration.

## Debts

| ID | Area | Finding | Priority | Required correction |
|---|---|---|---|---|
| D1 | Evidence independence | Six M4 slices rely on one registered source each; repeated Evidence Use is not independent triangulation. | High | Add claim-relevant independent sources/Evidence Use where they materially improve support. |
| D2 | Agricultural engineering evidence alignment | Claim B spans machinery, irrigation, drainage, storage and processing while the registered FAO locator is land/water focused. | High | Split claim scope or add claim-specific sources so every material assertion is directly supported. |
| D3 | Cybersecurity source-version alignment | Baseline framing does not explicitly anchor to current NIST CSF 2.0 terminology. | Medium-high | Align foundational framing to Govern, Identify, Protect, Detect, Respond and Recover; retain non-exhaustive boundary. |
| D4 | Human View boundaries | Infrastructure, construction, agricultural engineering and health systems can be over-applied to real-world decisions. | High | Strengthen prominent educational/professional boundaries in context/scope without suppressing useful knowledge. |
| D5 | Building science overgeneralization | Generic heat/moisture/ventilation statements can be applied to a particular building without adequate context. | Medium | Add explicit building-specific assessment/measurement boundary. |
| D6 | Substantive depth asymmetry | Six high-reuse slices are shallower than their cross-domain importance warrants. | Medium-high | Add only evidence-supported claims/context needed to close identified gaps; no record-count quota. |

## Relation outcome
Relation audit found no blocking defects and no justified need for artificial M4 relations. Existing infrastructure ↔ settlement linkage is valid. Any new relation must arise from corrected, claim-specific evidence.

## Correction order
1. D2 source-to-claim alignment.
2. D1 independent evidence, incorporating D2.
3. D3 cybersecurity terminology/source alignment.
4. D4/D5 Human View boundary strengthening.
5. D6 substantive depth additions where evidence supports them.
6. Re-run substantive, evidence independence, Human View, Relation and debt-map audits.
7. Synchronize coverage/regressions/documentation.
8. Exact-head 3/3 CI.
9. M4 CLEAN checkpoint only after all gates pass.

## Acceptance rule
No debt is marked CLOSED merely because a file changed. Each debt requires post-correction audit evidence and exact-head CI compatibility.
