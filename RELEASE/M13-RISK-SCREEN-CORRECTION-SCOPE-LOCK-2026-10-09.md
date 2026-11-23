# M13 Finding-Specific Correction Scope Lock — Risk Screen
Date: 2026-10-09
Branch: m13-system-wide-depth-audit-2026-10-09
Status: scoped method correction prepared for implementation and regression validation.

## Finding
The current machine risk screen is a triage aid but does not explicitly cover nuclear/radiological safety, communications/information continuity, shelter/evacuation, or transport/access. It also classifies claims using only the statement and Evidence Use material, excluding linked Context/Scope text and source identity. This can produce systematic false negatives in the high-consequence candidate list.

## Authorized narrow scope
1. Modify only REFERENCE/m13_claim_audit_inventory.py for this finding.
2. Add explicit keyword domains for:
   - nuclear/radiological hazards;
   - communications and information continuity;
   - shelter/evacuation;
   - transport/access.
3. Build the reproducible risk-screen text from the Claim statement, linked Evidence Use descriptions, linked Source identities, and referenced Context/Scope content where available.
4. Add dedicated regression tests in REFERENCE/tests/test_m13_claim_audit_inventory.py covering the new domains and inclusion of Context/Scope/Source identity.
5. Preserve existing patterns and flags; do not weaken existing checks.
6. Do not edit Claim, Source, Evidence Use, Context, Scope, Relation, schema or record-type content in this correction.
7. Treat the expanded machine screen as candidate discovery only. It does not replace manual false-negative review, the full high-consequence census, or the full 1,494-Claim D/E/B audit.

## Acceptance
- New tests pass.
- Existing Reference implementation tests, Release Conformance Gate and Offline Edition pass on one exact final SHA.
- The generated worksheet reports the same Claim denominator as the full corpus and retains all claims; only risk-domain/triage fields change.
- The independent risk-frame review checks false negatives and confirms the screen is not being treated as a semantic severity score.

## Boundary
This scope lock authorizes only the described audit-method correction. It does not authorize content corrections, new Relations, new Record types, changes to main, merging M12, or post-M13 gap-map work. M13 remains open until the full protocol is completed.
