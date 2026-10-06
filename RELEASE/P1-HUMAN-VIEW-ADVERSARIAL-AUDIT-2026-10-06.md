# P1 Human View / Adversarial Audit — 2026-10-06

## Scope
Five remaining P1 slices were tested as if an ordinary person were using the corpus under time pressure, without reading the architecture:
- hand-tool-safety
- home-fire-smoke-safety
- emergency-lighting-safety
- emergency-alert-warning
- septic-system-emergency

## Adversarial scenarios
1. Defective hand tool: the user must know not to continue using a damaged tool. The slice gives an explicit remove-from-use boundary and does not invite repair beyond the documented limit. PASS.
2. Active home fire / smoke alarm: the user must know the immediate priority is evacuation, staying outside, contacting the fire service, and not re-entering. PASS after the previous substantive correction.
3. Power outage / burning candle: the user may leave the room or become sleepy while the candle is still burning. This boundary was previously implicit. CLOSED by adding CLM-LIGHTING-EXTINGUISH with direct USFA evidence.
4. Emergency alert received: the user must distinguish information from action and follow current competent-authority instructions rather than inventing an evacuation/shelter decision. PASS; the slice explicitly defers individual action to current authorities.
5. Flooded / damaged septic system: the user may encounter standing water contaminated by sewage. The corpus previously covered pump/repair boundaries but did not give an explicit no-contact rule. CLOSED by adding CLM-SEPTIC-SEWAGE-CONTACT with direct CDC evidence.

## Human View criteria
- Can a person identify the immediate safe action? PASS after corrections.
- Are stop/leave/stay-out boundaries explicit where high consequence? PASS.
- Are escalation/professional boundaries explicit? PASS.
- Does the text avoid pretending to be an individualized professional assessment? PASS.
- Does any scenario encourage a dangerous DIY action? PASS.
- Are important actions supported by direct evidence? PASS.

## Findings
- P1-HUMAN-001 — CLOSED: two usability/safety boundary gaps were corrected in emergency-lighting-safety and septic-system-emergency.
- Blocking findings: 0.
- Critical contradictions: 0.
- Exact duplicate clusters: 0.
- Human View findings remaining: 0.

## Gate status
This is the final substantive P1 gate. It is not yet the final technical closure: full 3/3 CI must pass on the correction commit, then a dedicated P1 CLEAN checkpoint must be created. P2 remains blocked until that checkpoint is green.