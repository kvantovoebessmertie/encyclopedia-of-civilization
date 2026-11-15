# M13 risk-management B rights-compatible alternative authorization

Date: 2026-11-15
Authorization ID: M13-RISK-MANAGEMENT-B-GAO-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `933200a7053e9a34ffa60d42c660096b32df74c7`
Status: AUTHORIZED FOR ONE LIMITED SOURCE REPLACEMENT PATH

## Finding

Package 31 records `CLM-RISK_MANAGEMENT_BASICS-B` as RIGHTS HOLD because its active Evidence Use relies on ISO 31000 material that is not cleared for this AI-assisted evidence workflow. The Claim is: «Риск связан с влиянием неопределённости на цели, поэтому оценка риска зависит от целей и контекста.»

A current official U.S. Government Accountability Office source is available: *Standards for Internal Control in the Federal Government* (GAO-25-107721, May 2025), paragraph 7.02, page 44. It defines risk in its federal internal-control context as the possibility of an event adversely affecting achievement of objectives and says assessment scope/frequency considers entity objectives and risk tolerances. The document states that it is a U.S. government work not subject to copyright protection in the United States, subject to separately copyrighted material.

This source is narrower than the Claim: it covers adverse events, not positive opportunities, and does not reproduce the full broad uncertainty formulation. It can support only the adverse-event/objective and context-dependent assessment components. The Claim must remain UNASSESSED and partial/HOLD; the ISO rights hold remains in force.

## Exact authorized changes

1. Add only `CONTENT/vertical-slices/risk-management-basics/records/SRC-GAO-GREEN-BOOK-2025.json` as Source v1 with URI `https://www.gao.gov/assets/gao-25-107721.pdf`.
2. Version only `EU-RISK_MANAGEMENT_BASICS-B` from v2 to v3. Change only `record_version`, `provenance.created_from[0]`, `content.source_ref`, and `content.material.description`. Preserve Claim B@1, evidence_role, ID, schema, statuses and all other fields. Set the Source reference to `SRC-GAO-GREEN-BOOK-2025@1`.
3. Update only the risk-management-basics README to describe the ISO rights hold and the narrow GAO scope.
4. Update only `REFERENCE/tests/test_content_risk_management_basics_vertical_slice.py` for the one new Source and v3 Evidence Use, and `REFERENCE/tests/test_m13_evidence_linkage_audit.py` for the exact versioned source lineage.
5. Update only `RELEASE/CONTENT-COVERAGE.json` actual totals: total records 4,849 → 4,850 and Source count 625 → 626. Keep Claims, Evidence Use, slice count and all other counts unchanged.
6. Register this exact authorization and finding ID in `RELEASE/EDITORIAL-CORRECTION.json`.
7. Add a checkpoint recording the source, locator, scope limitation and required checks.

## Exclusions

Do not change any Claim wording, other Source or Evidence Use, Context, Scope, Relation, other README/test, rights metadata for ISO, or D/E/B ledger. Do not mark the Claim assessed or cleared; do not use ISO 31000 content. No publication/release approval, main update or PR merge is authorized. M13 remains OPEN / NOT RELEASE-READY.
