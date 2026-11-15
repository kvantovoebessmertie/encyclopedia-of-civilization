# M13 risk-management B GAO source checkpoint

Date: 2026-11-15
Authorization: `M13-RISK-MANAGEMENT-B-GAO-001`
Basis HEAD: `933200a7053e9a34ffa60d42c660096b32df74c7`

## Source and exact locator

Added the official U.S. Government Accountability Office *Standards for Internal Control in the Federal Government*, GAO-25-107721 (May 2025), at `https://www.gao.gov/assets/gao-25-107721.pdf`.

The registered pinpoint is paragraph 7.02, page 44. GAO defines risk in the U.S. federal internal-control context as the possibility of an event that adversely affects achievement of objectives. It further states that management considers entity objectives and risk tolerances when determining the scope and frequency of risk assessments.

## Evidence boundary

Versioned `EU-RISK_MANAGEMENT_BASICS-B` from v2 to v3 and redirected its active source/provenance references to the GAO Source. The description explicitly limits support to adverse-event/objective and context-dependent assessment aspects. It does not establish positive/opportunity risk or the full general uncertainty formulation in Claim B.

ISO 31000 remains registered as historical source identity but is not used in the current Evidence Use. Its RIGHTS HOLD remains unresolved. Claim B remains UNASSESSED and partial/HOLD. No D/E/B value or publication status was changed.

## Verification

Run the risk-management-basics slice regression, M13 evidence-linkage regression, Content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one exact successor HEAD. Independently verify that only the authorized files changed.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged. `main` remains unchanged.
