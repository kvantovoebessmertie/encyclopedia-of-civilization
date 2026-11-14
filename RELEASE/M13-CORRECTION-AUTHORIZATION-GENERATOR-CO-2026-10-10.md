# M13 Controlled Correction Authorization — Generator CO Emergency Evidence — 2026-10-10

## Authorization basis

This is a bounded correction authorization for finding `M13-GENERATOR-CO-EVIDENCE-001` identified during the M13 system-wide evidence-linkage review. The machine-readable authorization is recorded in `RELEASE/EDITORIAL-CORRECTION.json`. Work is confined to the existing generator carbon-monoxide safety slice.

## Confirmed mismatch

- `CLM-GENERATOR-CO-ALARM-EMERGENCY` currently says to leave for fresh air and seek emergency medical help, and additionally says not to return until the space has been checked for safety.
- `SRC-CDC-GENERATOR-CO-2026` points to CDC's power-outage safety guidance. It supports the immediate exit / fresh-air response and prompt emergency medical assistance for suspected CO poisoning.
- The recorded CDC locator does not establish the separate no-re-entry-until-inspected clause. That clause must not be presented as supported by this Source without direct source support.

## Exact authorized file list

1. `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/CLM-GENERATOR-CO-ALARM-EMERGENCY.json`
2. `CONTENT/vertical-slices/generator-carbon-monoxide-safety/records/EU-GENERATOR-CO-ALARM-EMERGENCY.json`
3. `REFERENCE/tests/test_m13_evidence_linkage_audit.py`
4. `RELEASE/EDITORIAL-CORRECTION.json` — this bounded authorization only.
5. This authorization document.

## Authorized correction

- Narrow only the Claim statement to the emergency advice directly supported by the recorded CDC source: leave for fresh air immediately when a CO alarm sounds or symptoms suggest possible CO poisoning during generator use, and seek emergency medical assistance. Remove the unsupported no-re-entry-until-inspected clause; do not replace it with a new unsourced instruction.
- Rewrite only the linked Evidence Use material description so it accurately explains the CDC guidance for immediate exit/fresh air and emergency medical assistance.
- Add a targeted regression that checks the exact Claim/Evidence Use/Source references, support role, CDC locator, claim-specific description, and absence of the unsupported clause in the Claim.

## Exclusions

No Source record changes, no new Sources or Records, no new Relations or Record types, no unrelated Claim edits, no Context/Scope changes, no schema or release-gate changes, no unrelated slices, no changes to `main`, and no PR merge. Preserve all record IDs, provenance methods, source identity/URL, references, evidence role, corpus counts and coverage.

## Acceptance gates

1. Verify the exact changed paths and protected invariants.
2. Run targeted regressions and full content preflight.
3. Run Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
4. Independently verify PR #21 remains open/draft/unmerged and `main` is unchanged.
5. Report the correction as accepted only if all three CI workflows pass on the same final SHA.

**Status: authorized for this exact bounded correction; acceptance remains pending exact-head verification.**
