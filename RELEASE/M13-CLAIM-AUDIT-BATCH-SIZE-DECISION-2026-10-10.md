# M13 Claim Audit Batch-Size Decision — 2026-10-10

## Decision
Starting after the completed Batch 40, use target batches of **100 previously unscored Claims** instead of 30. This changes packaging only; it does not change the scoring method, acceptance criteria, frozen denominator, or required audit passes.

## Current recorded position
- Frozen Claim denominator: 1,494.
- Explicitly scored Claims recorded through Batch 40: 156.
- Remaining Claims to score: 1,338.
- Next batch number: 41.
- Calibration checkpoint: 747 of 1,494 Claims scored.
- Current M13 PR remains open/draft/unmerged; `main` and protected historical checkpoints must remain unchanged.

## Batch construction and review rules
1. Build Batch 41 from exactly 100 unique Claims not already scored in the existing review artifacts. Record every Claim ID before scoring and verify there are no overlaps with prior batches.
2. Preserve individual D, E, and B scores (0–3), claim-specific rationales, evidence/source identity and locator checks, and disposition notes for every Claim.
3. Machine triage can prioritize and flag records but must never be substituted for semantic review or D/E/B scoring.
4. Continue the high-consequence review overlay in parallel; do not defer urgent safety-relevant findings until the general census is complete.
5. At 747 scored Claims, perform the planned calibration: inspect scoring consistency and rationales, and re-review prior batches if warranted. Do not change the denominator to hide missing or unreviewable Claims.
6. After all 1,494 Claims have been scored, complete the integrated defect ledger, Relation endpoint/semantic review, evidence diversity and independence checks, Human View/adversarial review, independent re-review, authorized narrow corrections with dedicated regressions, and final exact-HEAD 3/3 CI plus final tree/PR/base/main verification.
7. Do not declare M13 complete based on batch count or CI alone. Do not start post-M13 survival-readiness work until M13 is formally closed.

## Expected batch arithmetic
From 1,338 remaining Claims, use 13 batches of 100 and a final batch of 38, subject to the no-overlap check and any documented exceptions. The arithmetic is a planning target, not evidence that any batch has been reviewed.

## Status
This file records the process decision only. It does not claim Batch 41 has been selected or completed, and it does not change content Records.
