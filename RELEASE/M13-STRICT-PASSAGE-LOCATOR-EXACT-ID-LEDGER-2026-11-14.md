# M13 — exact strict passage/locator queue reconciliation ledger

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `04ef30d5cb8a48654d03607a6ba5b01eb01bc87c`  
Queue source: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`

## 1. Deterministic reconciliation

This ledger maps every exact Claim/Evidence Use/Source triple in the 47-row queue to one review package. Package 07 is a broader 20-Claim risk-screen artifact; only six of its IDs are members of this specific 47-row strict queue. The other 14 Package 07 IDs are deliberately excluded from this ledger.

| Measure | Result |
|---|---:|
| Source queue rows parsed | 47 |
| Exact Claim IDs | 47 |
| Duplicate Claim IDs in queue | 0 |
| Rows assigned to one strict-review package | 47 |
| Unassigned rows | 0 |
| Strict queue coverage | 47/47 |

Expected package allocation: Package 01 = 7; Package 02 = 6; Package 03 = 9; Package 04 = 3; Package 05 = 16; Package 06 = 6. Total = 47.

## 2. Exact row ledger

| Slice | Claim | Evidence Use | Source | Review package |
|---|---|---|---|---|
| acoustics-basics | `CLM-ACOUSTICS_BASICS-C@1` | `EU-ACOUSTICS_BASICS-C@1` | `SRC-ACOUSTICS_BASICS@1` | Package 03 |
| algebra-basics | `CLM-ALGEBRA_BASICS-A@1` | `EU-ALGEBRA_BASICS-A@1` | `SRC-ALGEBRA_BASICS@1` | Package 03 |
| algebra-basics | `CLM-ALGEBRA_BASICS-B@1` | `EU-ALGEBRA_BASICS-B@1` | `SRC-ALGEBRA_BASICS@1` | Package 03 |
| algebra-basics | `CLM-ALGEBRA_BASICS-C@1` | `EU-ALGEBRA_BASICS-C@1` | `SRC-ALGEBRA_BASICS@1` | Package 03 |
| anatomy-basics | `CLM-ANATOMY_BASICS-A@1` | `EU-ANATOMY_BASICS-A@1` | `SRC-ANATOMY_BASICS@1` | Package 03 |
| anatomy-basics | `CLM-ANATOMY_BASICS-B@1` | `EU-ANATOMY_BASICS-B@1` | `SRC-ANATOMY_BASICS@1` | Package 03 |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-A@1` | `EU-ARCHIVAL_SCIENCE-A@1` | `SRC-ARCHIVAL_SCIENCE@1` | Package 03 |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-B@1` | `EU-ARCHIVAL_SCIENCE-B@1` | `SRC-ARCHIVAL_SCIENCE@1` | Package 03 |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-C@1` | `EU-ARCHIVAL_SCIENCE-C@1` | `SRC-ARCHIVAL_SCIENCE@1` | Package 03 |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-A@1` | `EU-ASSET_MANAGEMENT_BASICS-A@1` | `SRC-ASSET_MANAGEMENT_BASICS@1` | Package 04 |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-B@1` | `EU-ASSET_MANAGEMENT_BASICS-B@1` | `SRC-ASSET_MANAGEMENT_BASICS@1` | Package 04 |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-C@1` | `EU-ASSET_MANAGEMENT_BASICS-C@1` | `SRC-ASSET_MANAGEMENT_BASICS@1` | Package 04 |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-A@1` | `EU-BEHAVIORAL_BIOLOGY_BASICS-A@1` | `SRC-BEHAVIORAL_BIOLOGY_BASICS@1` | Package 05 |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-B@1` | `EU-BEHAVIORAL_BIOLOGY_BASICS-B@1` | `SRC-BEHAVIORAL_BIOLOGY_BASICS@1` | Package 05 |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-C@1` | `EU-BEHAVIORAL_BIOLOGY_BASICS-C@1` | `SRC-BEHAVIORAL_BIOLOGY_BASICS@1` | Package 05 |
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `SRC-BEHAVIORAL_ECONOMICS_BASICS@1` | Package 06 |
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-C@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-C@1` | `SRC-BEHAVIORAL_ECONOMICS_BASICS@1` | Package 06 |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-A@1` | `EU-BIODIVERSITY_BASICS-A@1` | `SRC-BIODIVERSITY_BASICS@1` | Package 06 |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-B@1` | `EU-BIODIVERSITY_BASICS-B@1` | `SRC-BIODIVERSITY_BASICS@1` | Package 06 |
| calibration-basics | `CLM-CALIBRATION_BASICS-A@1` | `EU-CALIBRATION_BASICS-A@1` | `SRC-CALIBRATION_BASICS@1` | Package 02 |
| calibration-basics | `CLM-CALIBRATION_BASICS-B@1` | `EU-CALIBRATION_BASICS-B@1` | `SRC-CALIBRATION_BASICS@1` | Package 06 |
| calibration-basics | `CLM-CALIBRATION_BASICS-C@1` | `EU-CALIBRATION_BASICS-C@1` | `SRC-CALIBRATION_BASICS@1` | Package 06 |
| cell-basics | `CLM-CELL_BASICS-A@1` | `EU-CELL_BASICS-A@1` | `SRC-CELL_BASICS@1` | Package 05 |
| cell-basics | `CLM-CELL_BASICS-B@1` | `EU-CELL_BASICS-B@1` | `SRC-CELL_BASICS@1` | Package 05 |
| cell-basics | `CLM-CELL_BASICS-C@1` | `EU-CELL_BASICS-C@1` | `SRC-CELL_BASICS@1` | Package 05 |
| civil-society-basics | `CLM-CIVIL_SOCIETY_BASICS-A@1` | `EU-CIVIL_SOCIETY_BASICS-A@1` | `SRC-CIVIL_SOCIETY_BASICS@1` | Package 05 |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-A@1` | `EU-DIGITAL_COMMUNICATIONS_BASICS-A@1` | `SRC-DIGITAL_COMMUNICATIONS_BASICS@1` | Package 02 |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-B@1` | `EU-DIGITAL_COMMUNICATIONS_BASICS-B@1` | `SRC-DIGITAL_COMMUNICATIONS_BASICS@1` | Package 02 |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-C@1` | `EU-DIGITAL_COMMUNICATIONS_BASICS-C@1` | `SRC-DIGITAL_COMMUNICATIONS_BASICS@1` | Package 02 |
| electronics-basics | `CLM-ELECTRONICS_BASICS-B@1` | `EU-ELECTRONICS_BASICS-B@1` | `SRC-ELECTRONICS_BASICS@1` | Package 02 |
| electronics-basics | `CLM-ELECTRONICS_BASICS-C@1` | `EU-ELECTRONICS_BASICS-C@1` | `SRC-ELECTRONICS_BASICS@1` | Package 02 |
| emergency-management-basics | `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1` | `EU-EMERGENCY_MANAGEMENT_BASICS-B@1` | `SRC-EMERGENCY_MANAGEMENT_BASICS@1` | Package 01 |
| emergency-management-basics | `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1` | `EU-EMERGENCY_MANAGEMENT_BASICS-C@1` | `SRC-EMERGENCY_MANAGEMENT_BASICS@1` | Package 01 |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-A@1` | `EU-HISTORY_OF_MEDICINE-A@1` | `SRC-HISTORY_OF_MEDICINE@1` | Package 05 |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-B@1` | `EU-HISTORY_OF_MEDICINE-B@1` | `SRC-HISTORY_OF_MEDICINE@1` | Package 05 |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-C@1` | `EU-HISTORY_OF_MEDICINE-C@1` | `SRC-HISTORY_OF_MEDICINE@1` | Package 05 |
| humanitarian-logistics-basics | `CLM-HUMANITARIAN_LOGISTICS_BASICS-C@1` | `EU-HUMANITARIAN_LOGISTICS_BASICS-C@1` | `SRC-HUMANITARIAN_LOGISTICS_BASICS@1` | Package 05 |
| hydropower-basics | `CLM-HYDROPOWER_BASICS-A@1` | `EU-HYDROPOWER_BASICS-A@1` | `SRC-HYDROPOWER_BASICS@1` | Package 01 |
| migration-and-mobility-basics | `CLM-MIGRATION_AND_MOBILITY_BASICS-A@1` | `EU-MIGRATION_AND_MOBILITY_BASICS-A@1` | `SRC-MIGRATION_AND_MOBILITY_BASICS@1` | Package 05 |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-A@1` | `EU-SCIENTIFIC_PUBLISHING_BASICS-A@1` | `SRC-SCIENTIFIC_PUBLISHING_BASICS@1` | Package 05 |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-B@1` | `EU-SCIENTIFIC_PUBLISHING_BASICS-B@1` | `SRC-SCIENTIFIC_PUBLISHING_BASICS@1` | Package 05 |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-C@1` | `EU-SCIENTIFIC_PUBLISHING_BASICS-C@1` | `SRC-SCIENTIFIC_PUBLISHING_BASICS@1` | Package 05 |
| shelter-basics | `CLM-SHELTER_BASICS-A@1` | `EU-SHELTER_BASICS-A@1` | `SRC-SHELTER_BASICS@1` | Package 01 |
| shelter-basics | `CLM-SHELTER_BASICS-B@1` | `EU-SHELTER_BASICS-B@1` | `SRC-SHELTER_BASICS@1` | Package 01 |
| shelter-basics | `CLM-SHELTER_BASICS-C@1` | `EU-SHELTER_BASICS-C@1` | `SRC-SHELTER_BASICS@1` | Package 01 |
| urban-planning-basics | `CLM-URBAN_PLANNING_BASICS-A@1` | `EU-URBAN_PLANNING_BASICS-A@1` | `SRC-URBAN_PLANNING_BASICS@1` | Package 05 |
| water-security-basics | `CLM-WATER_SECURITY-B@1` | `EU-WATER_SECURITY-B@1` | `SRC-WATER_SECURITY@1` | Package 01 |

## 3. Interpretation boundary

- This ledger proves exact-ID coverage of the **desk-review routing queue**, not successful evidence validation.
- A package assignment means the triple was inspected and dispositioned at desk level; it does not mean the source supports the Claim, the EU has a valid canonical pinpoint, or the Claim is safe to publish.
- All packages report zero canonical JSON edits, zero D/E/B score changes, zero risk-metadata changes, zero rights permissions and zero specialist approvals.
- Every one of the 47 triples must remain HOLD until its package-specific source, locator, rights and review conditions are resolved.
- The 711-row unassessed-risk queue is a separate denominator and is not covered by this 47-row ledger.

## 4. Machine-check result

Generated from the queue table and the exact ID sets in strict review Packages 01–06. The corrected parser finds 47 queue rows, 47 unique Claim IDs, 0 duplicate IDs, 47 assigned rows and 0 unassigned rows. Allocations are Packages 01–06 only.

This is an auditable reconciliation artifact, not M13 closure or release approval.
