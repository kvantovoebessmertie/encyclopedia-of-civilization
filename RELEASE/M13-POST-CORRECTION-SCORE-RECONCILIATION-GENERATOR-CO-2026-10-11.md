# M13 Post-Correction Score Reconciliation — Generator CO Emergency Claim

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **score reconciliation open; no M13 acceptance implied**

## Trigger

The bounded correction authorization `M13-CORRECTION-AUTHORIZATION-GENERATOR-CO-2026-10-10.md` authorized narrowing the Claim and Evidence Use to the CDC support actually established by the recorded source. The Claim no longer contains the former clause “в помещение нельзя возвращаться до проверки безопасности.” The linked Evidence Use now specifically describes immediate exit/fresh air and emergency medical assistance.

## Confirmed audit inconsistency

The earlier Batch 19 review, `M13-CLAIM-REVIEW-BATCH-19-GENERATOR-CO-HYPOTHERMIA-2026-10-10.md`, assigns D=2, E=3, B=3 and justifies the result partly by saying the Claim has “a clear no-return boundary until safety is confirmed.” That statement is no longer true of the corrected Claim. The consolidated working ledger repeats the same stale rationale.

This is a **post-correction score-rationale mismatch**, not proof that the prior numerical scores must all change. The old scores cannot be treated as final without re-adjudication against the corrected Claim and Evidence Use.

## Registry reconciliation

The generator correction authorization stated that the machine-readable authorization was recorded in `RELEASE/EDITORIAL-CORRECTION.json`, but the registry's `findings` array contained `M13-CHEM-WATER-EVIDENCE-001` and did not contain `M13-GENERATOR-CO-EVIDENCE-001`; its purpose text also described only the chemical-water correction. This discrepancy has now been corrected in the registry on this branch: the generator finding was added and the purpose text now describes both bounded M13 authorizations. The generator scope remains restricted to the exact files in its authorization; no Source, unrelated Claim, new Record, or Relation change was made.

## Required reconciliation

1. Re-score D/E/B for `CLM-GENERATOR-CO-ALARM-EMERGENCY` from the corrected Claim and Evidence Use, with fresh rationale that does not refer to the removed no-re-entry clause.
2. Update the consolidated ledger only after the revised row has been reviewed; preserve the old report as historical evidence and point to this addendum.
3. Verify the dedicated generator regression, content preflight, Reference implementation tests, Release Conformance Gate and Offline Edition on the same exact final HEAD.
4. Independently verify that PR #21 remains open/draft/unmerged and `main` remains unchanged.

## Protected-state boundary

This addendum changes no Claim, Evidence Use, Source or Relation record. It records the effect of an already authorized correction on downstream audit artifacts. The existing score row remains provisional until re-adjudicated. M13 remains open.
