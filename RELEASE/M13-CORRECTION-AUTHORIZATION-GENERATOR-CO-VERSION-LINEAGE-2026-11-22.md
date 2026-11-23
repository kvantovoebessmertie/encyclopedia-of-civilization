# M13 Controlled Correction Authorization — Generator CO Version Lineage — 2026-11-22

## Authorization

Owner approval received in the project conversation on 2026-11-22 for the narrowly bounded correction below. Machine-readable authorization: `M13-GENERATOR-CO-VERSION-LINEAGE-002` in `RELEASE/EDITORIAL-CORRECTION.json`.

## Finding

The historical Claim `CLM-GENERATOR-CO-ALARM-EMERGENCY@1` was semantically changed in commit `a58294e3...` without incrementing `record_version`. The original historical version and its Blob SHA remain preserved in Git history and the Phase 3 crosswalk. This correction restores the safety clause only as a new version; it does not rewrite the historical version.

## Exact authorized changes

1. Advance `CLM-GENERATOR-CO-ALARM-EMERGENCY` from record version 1 to version 2. Version 2 retains the CDC-supported immediate fresh-air/emergency-medical response and restores the no-re-entry instruction, now supported by the already-existing official CPSC Source.
2. Advance `EU-GENERATOR-CO-ALARM-EMERGENCY` from version 1 to version 2 and keep it strictly limited to the CDC-supported immediate exit/fresh-air and emergency medical response.
3. Add exactly one Evidence Use record, `EU-GENERATOR-CO-ALARM-EMERGENCY-CPSC-2026@1`, linking Claim @2 to the already-existing `SRC-CPSC-CO-ALARM-EMERGENCY-2026@1`. Its scope is only the instruction not to re-enter until emergency responders permit it.
4. Add targeted regression assertions for the Claim/Evidence Use versions, exact cross-slice CPSC reference, CDC/CPSC scope separation, and preservation of the no-re-entry warning.
5. Update this authorization, the machine-readable authorization registry, the generator slice README record count/boundary, and `RELEASE/CONTENT-COVERAGE.json` by exactly +1 total record and +1 Evidence Use for the one new Evidence Use; update M13 checkpoint/PR documentation for this exact correction.

## Exact files

- `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/CLM-GENERATOR-CO-ALARM-EMERGENCY.json`
- `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/EU-GENERATOR-CO-ALARM-EMERGENCY.json`
- `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/EU-GENERATOR-CO-ALARM-EMERGENCY-CPSC-2026.json` (new)
- `REFERENCE/tests/test_m13_evidence_linkage_audit.py`
- `RELEASE/EDITORIAL-CORRECTION.json`
- `RELEASE/M13-CORRECTION-AUTHORIZATION-GENERATOR-CO-VERSION-LINEAGE-2026-11-22.md`

## Explicit exclusions

No Source record is created or modified; no duplicate CPSC Source is created; no other Claim, Evidence Use, slice, Relation, Context, Scope, Assessment, risk record, D/E/B score, publication allowlist, or coverage field other than total_records and evidence_use.count incremented by exactly one is changed. No main update, branch synchronization, PR merge, deployment, or publication approval is authorized.

## Acceptance

- Preserve the prior Claim@1 and EU@1 contents in Git history.
- Verify only the exact paths above changed.
- Run targeted regressions and full content preflight.
- Require Reference Tests, Release Conformance Gate, Offline Edition, and the M13 audit workflow to complete on the final exact HEAD.
- Verify PR #21 remains open/draft/unmerged and main remains unchanged.
- This correction does not clear the Claim for first-edition publication; its publication status remains subject to independent content, safety, rights, and editorial gates.
