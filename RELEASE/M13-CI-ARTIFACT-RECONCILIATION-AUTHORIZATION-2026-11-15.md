# M13 CI artifact reconciliation authorization

Date: 2026-11-15
Authorization ID: M13-CI-RECONCILIATION-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `22aadf4055a588390c7d1b41e736e853970ca39d`
Status: AUTHORIZED FOR TWO REGRESSION/REPORT RECONCILIATIONS ONLY

## Findings

The exact-head CI run on `22aadf4055a588390c7d1b41e736e853970ca39d` found two failures caused by stale audit artifacts after the already-authorized NIST Source deduplication and current corpus growth:
- `REFERENCE/tests/test_m13_evidence_linkage_audit.py` still attempts to load the deleted local Source ID `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP`, although its Evidence Use now correctly references the canonical Source in `materials-science-basics`.
- `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json` reports 4,834 records while the actual corpus and `RELEASE/CONTENT-COVERAGE.json` both report 4,849. The cross-slice Relation set remains 57.

## Exact authorized changes

1. Update only `REFERENCE/tests/test_m13_evidence_linkage_audit.py` so the affected Evidence Use is loaded from `materials-basics` and its canonical Source is loaded from `materials-science-basics`; preserve all other assertions and test cases.
2. Update only `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json` to record 4,849 current corpus records and accurately describe this as count reconciliation after M13 bounded source-fit additions and NIST Source deduplication. Preserve the 483-slice count, 57-Relation count, prior findings, and epistemic boundary. Do not imply a new substantive Relation audit.
3. Register this exact bounded authorization and finding ID in `RELEASE/EDITORIAL-CORRECTION.json`.
4. Add a checkpoint documenting the two CI failures, exact corrections, and required exact-head verification.

## Exclusions

No canonical Claim, Source, Evidence Use, Relation, Context, Scope, README, risk metadata, D/E/B ledger, or other test is authorized to change. No publication/release approval, main update, or PR merge is authorized. M13 remains OPEN / NOT RELEASE-READY.
