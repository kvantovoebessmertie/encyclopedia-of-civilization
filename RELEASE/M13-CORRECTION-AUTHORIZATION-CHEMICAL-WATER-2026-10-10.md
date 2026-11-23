# M13 Controlled Correction Authorization — Chemical Water Evidence — 2026-10-10

## Authorization basis

This is a bounded correction authorization for the evidence-linkage mismatch identified during the M13 system-wide depth audit and recorded as `M13-CHEM-WATER-EVIDENCE-001`. The user approved proceeding with the M13 correction work. The machine-readable registry entry is recorded in `RELEASE/EDITORIAL-CORRECTION.json`.

## Confirmed mismatch

- Claim: `CLM-CHEM-WATER-NO-DRINK` states that when a “do not drink” advisory is associated with possible chemical contamination, commercially bottled water should be used for drinking and food preparation.
- Evidence Use: `EU-CHEM-WATER-NO-DRINK` previously described CDC's distinction between advisory types and the fact that boiling does not remove chemical contaminants. That is relevant to the neighboring no-boil Claim, but it did not directly describe the recommendation represented by this Claim.
- Source: `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024`, CDC “Drinking Water Advisories: An Overview”, recorded canonical URL remains unchanged.

## Exact authorized file list

1. `CONTENT/vertical-slices/chemical-water-advisory/records/EU-CHEM-WATER-NO-DRINK.json`
2. `REFERENCE/tests/test_m13_evidence_linkage_audit.py`
3. `RELEASE/EDITORIAL-CORRECTION.json` — record this bounded authorization only.
4. This authorization document.

## Authorized correction

- Rewrite only the material description in `EU-CHEM-WATER-NO-DRINK` to describe the CDC do-not-drink advisory recommendation in a claim-specific way, preserve the recorded Source locator, and explicitly defer any additional restrictions to the specific local advisory.
- Add a targeted regression that checks the exact Claim, Source and Evidence Use references, the support role, the CDC locator, and the claim-specific content of the description.
- Preserve all record IDs, Claim text, Source identity and URL, provenance methods, references, evidence role, Context/Scope, Relations, record counts, coverage and all other slices.

## Exclusions

No Claim wording changes, no Source record changes, no additional sources or Records, no new Relations or Record types, no release-gate weakening, no unrelated content changes, no changes to `main`, and no PR merge. This authorization does not resolve other M13 evidence-linkage findings.

## Acceptance gates

1. Verify the exact changed paths and the protected invariants above.
2. Run the dedicated evidence-linkage regression and full content preflight.
3. Run Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
4. Independently verify PR #21 remains open/draft/unmerged and `main` is unchanged.
5. Report the correction as accepted only if all three CI workflows pass on the same final SHA.

**Status: authorized for this exact bounded correction; acceptance remains pending exact-head verification.**
