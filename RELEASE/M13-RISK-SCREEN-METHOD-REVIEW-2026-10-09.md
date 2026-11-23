# M13 Risk-Screen Method Review — 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: review of the current machine triage implementation in `REFERENCE/m13_claim_audit_inventory.py`.
Review type: audit-method review. No code or corpus records changed.

## Summary
The current script is useful as a **triage aid**, but its regular-expression screen must not be treated as a complete high-consequence inventory. The M13 protocol requires a reproducible risk screen and an independent check that high-consequence claims are not omitted because the screen only covers familiar categories.

## Observed method
The script scans the Claim statement plus linked Evidence Use material descriptions and flags several predefined domains: health/medical, emergency/fire/CO, water/food/sanitation, electricity/energy, construction/tools/materials, chemicals/hazards, and legal/financial. It also flags prescriptive wording and generic/short evidence descriptions. The script itself correctly labels these flags as machine triage rather than semantic scores.

## Confirmed method limitations

### 1. Missing explicit nuclear / radiological domain
The current risk-domain patterns do not explicitly include nuclear, radiation, radioactive contamination, radionuclides, fallout, radiological emergency, iodine prophylaxis, or decontamination. Therefore a high-consequence claim may not be flagged by the risk-domain screen unless it happens to match another term. The presence of a nuclear-physics educational slice does not solve this classification problem.

### 2. Missing explicit communication / information continuity domain
The patterns do not explicitly identify telecommunications outage, internet outage, emergency radio, official alert reception, family communication plans, or misinformation/source-verification claims. Some may be caught by “emergency” or “electricity” terms, but that is incidental and not a reproducible domain rule.

### 3. Other risk domains are not explicitly represented
The current list does not separately represent shelter/evacuation decisions, transportation and access, environmental exposure, radiation/chemical cross-contamination, or food-chain disruption. Some terms overlap with construction, emergency, water or health patterns; overlap does not guarantee recall.

### 4. The screen omits important record context
The script's combined text for risk detection is the Claim statement plus linked Evidence Use material. It does not include the linked Context and Scope text or source identity/metadata when determining risk domains. A claim whose safety significance is made explicit only by context/scope or source framing can therefore be missed.

### 5. Keyword flags are not semantic risk judgments
The screen can produce false positives for broad conceptual claims and false negatives for claims phrased without listed terms. It does not assess severity, exposure, reversibility, vulnerable populations, actionability, or how a claim could be misused. The script should remain a candidate-discovery mechanism, not a final list of all high-consequence Claims.

## Required follow-up before risk-screen lock
1. Expand the domain taxonomy to include at least nuclear/radiological safety and communication/information continuity; consider transport/access, shelter/evacuation, and environmental exposure as distinct candidate domains.
2. Include Claim Context and Scope text in candidate discovery where available, while preserving a reproducible rule and avoiding duplicate counting.
3. Retain all current Claims in the denominator and report both machine-flagged and manually added candidates.
4. Manually review false negatives using a slice/keyword sweep and document the inclusion/exclusion rationale.
5. Independently check the risk-frame before the full high-consequence D/E/B overlay.
6. Add regression tests for risk-screen coverage and false-negative examples; do not weaken existing checks.
7. Do not treat the machine-flagged set as a complete high-consequence census until these steps pass.

## Audit boundary
Finding and method review only. No script, schema, test, Claim or other corpus record was changed. This is a finding-specific correction candidate; code changes require a correction scope lock and regression tests. M13 remains open.
