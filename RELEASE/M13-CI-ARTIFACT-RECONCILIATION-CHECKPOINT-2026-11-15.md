# M13 CI artifact reconciliation checkpoint

Date: 2026-11-15
Authorization: `M13-CI-RECONCILIATION-001`
Basis HEAD: `22aadf4055a588390c7d1b41e736e853970ca39d`

## Exact-head findings

Reference Tests on the basis HEAD completed with 1,019 passed and 2 failed:
- the cross-slice audit artifact still reported 4,834 records while the coverage manifest and actual corpus reported 4,849;
- the M13 evidence-linkage regression attempted to load the removed duplicate Source `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP` locally instead of resolving the canonical Source in `materials-science-basics`.

Release Conformance Gate was PARTIAL solely because the shared pytest suite failed. Its corpus coverage synchronization gate passed at 4,849 records / 483 slices, and slice registration passed. Offline Edition and M13 Review Queue succeeded.

## Bounded remediation

- Updated the evidence-linkage regression to distinguish the Evidence Use slice from the Source slice and resolve the shared NIST Source in `materials-science-basics`.
- Synchronized `CONTENT-CROSS-SLICE-AUDIT.json` to 4,849 records while preserving 483 slices, 57 cross-slice Relations and the prior Relation findings. The artifact explicitly describes this as count reconciliation, not a new substantive Relation audit.
- No canonical content records or D/E/B scores were changed.

## Verification required

Run Content preflight, the two affected regressions, full Reference Tests, Release Conformance Gate and Offline Edition on one exact successor HEAD. Then independently verify the PR head, base branch and unchanged `main`.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged. `main` remains unchanged.
