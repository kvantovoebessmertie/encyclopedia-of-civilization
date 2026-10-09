# M5 Unified Debt Map — 2026-10-09

## Current state
M5 content authoring and content-level audits are implemented on `m5-content-maturation-2026-10-09`. The three release workflows passed together on audit target `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; release documents were then synchronized, creating a new HEAD that still requires exact-head CI.

- Prior protected baseline: M4 CLOSED CLEAN accepted content HEAD `83b2e3185cd92c55d53a5ce661be384508870e1a`.
- Current content snapshot: **479 vertical slices / 4754 Records / 19 Record types / 601 Sources / 1634 Evidence Use / 64 Relations**.
- Cross-slice linkage: 57 Relation records plus one shared Context.
- M5 scope: nine existing slices only; no new slice or Record type.
- M4 remains closed and protected.

## Debt and gate ledger

| ID | Gate / debt | Status | Evidence / next action |
|---|---|---|---|
| M5-D1 | Substantive depth in nine slices | PASS — content level | `M5-POST-CORRECTION-SUBSTANTIVE-AUDIT-2026-10-09.md`; re-check after CI |
| M5-D2 | Independent evidence tracks and claim-specific Evidence Use | PASS — slice level | `M5-EVIDENCE-INDEPENDENCE-AUDIT-2026-10-09.md`; single-source claims explicitly listed |
| M5-D3 | Human View / overgeneralization boundaries | PASS — content level | `M5-HUMAN-VIEW-ADVERSARIAL-AUDIT-2026-10-09.md`; re-check after CI |
| M5-D4 | Relation correctness | PASS | `M5-RELATION-AUDIT-2026-10-09.md`; one justified telecom ↔ energy Relation added and covered by regression |
| M5-D5 | Dedicated regression coverage for all nine slices | PASS on audit target | Reference run #2489 passed all repository-defined tests on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; rerun on final documentation-synchronized HEAD |
| M5-D6 | Corpus totals and M5 registry synchronization | TREE AUDIT PASS; exact-head rerun pending | `M5-POST-CI-CORPUS-AND-RELEASE-AUDIT-2026-10-09.md`; 4,754 JSON record files and 479 record-bearing slice directories verified from complete tree; registry total and 19 type counts sum to 4,754 |
| M5-D7 | Reference implementation tests | PASS on audit target; final HEAD rerun required | Run #2489 success on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; rerun after release-document sync |
| M5-D8 | Release Conformance Gate | PASS on audit target; final HEAD rerun required | Run #2539 success on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; rerun after release-document sync |
| M5-D9 | Offline Edition | PASS on audit target; final HEAD rerun required | Run #1962 success on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; package, manifest and offline validation steps all passed; rerun after release-document sync |
| M5-D10 | Final post-CI audit synchronization | IN PROGRESS | `M5-POST-CI-CORPUS-AND-RELEASE-AUDIT-2026-10-09.md` records tree-level reconciliation and prior exact-target CI; repeat checks after documentation-synchronized HEAD passes all three gates |
| M5-D11 | M5 CLEAN checkpoint | NOT CLAIMED | Create only after D1–D10 close and exact-head 3/3 CI is GREEN |

## Non-negotiable gates
- Do not merge or promote the M5 branch before the exact-head gates pass.
- Do not declare CLEAN from record counts or documentation alone.
- Do not weaken tests, schema, semantic rules or conformance to obtain GREEN.
- If CI finds a defect, fix it on the M5 branch, rerun all required gates on the new exact HEAD and update this map.
- Keep the protected M4 accepted content HEAD unchanged.

## Decision
M5 is **not CLEAN yet**. Content-level audits and all three CI workflows passed on `6dcf8dc678ac87b08fb8f0c89fbf47fd69aa00dd`; the documentation updates create a new HEAD, so exact-head 3/3 CI and final re-audit must still be completed before any CLEAN decision.
