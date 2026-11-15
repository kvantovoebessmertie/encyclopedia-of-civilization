# M13 Geophysics C USGS source checkpoint

Date: 2026-11-15
Authorization: `M13-GEOPHYSICS-C-USGS-001`
Basis HEAD: `9f4173fd3446197160449471637c429d18684109`
Authorization registry correction: `e7217bc0899267b7e5595eeaea9a7dce7845c760`

## Source and exact locator

Added the official U.S. Geological Survey project page *Geophysical Mapping of Geologic Systems Host to Critical Mineral Deposits, Southern Midcontinent, US*, dated September 27, 2024.

Pinpoints: “Science Issue and Relevance” and “Methods to Address Issue.” The page describes high-resolution airborne and regional ground geophysical methods for concealed geology; collection, modelling and interpretation of airborne and ground data; drill-core examination where available; airborne magnetic/radiometric surveys; airborne electromagnetics; ground magnetotellurics; and 3D inversions.

USGS-authored information is in the U.S. public domain with attribution. Separately copyrighted third-party images and media are excluded.

## Evidence boundary

Versioned `EU-GEOPHYSICS_BASICS-C` from v1 to v2 and redirected its active source/provenance references to the new USGS project Source. The description presents this as one regional project example, not a universal workflow; drill-core examination is conditional on availability. Claim C wording and assessment status were not changed.

## Corpus reconciliation

The new Source increases the corpus to 4,851 records and Sources to 627. The cross-slice audit count was synchronized to 4,851; 483 slices and 57 Relations were preserved. This is count-only reconciliation, not a new substantive Relation audit.

## Preflight and verification state

The first Offline Edition attempt on the preceding commit was blocked because `geophysics-basics` had not yet been added to the machine-readable `authorized_slices` list. The authorization document and registry purpose were present, but the preflight guard specifically reads `RELEASE/EDITORIAL-CORRECTION.json.authorized_slices`. The slug was added under this exact authorization. Content preflight then passed and Offline Edition completed successfully on `e7217bc0899267b7e5595eeaea9a7dce7845c760`.

Reference Tests and Release Conformance Gate were cancelled during branch updates and are not counted as successful. Re-run all required checks on one final exact HEAD, including the geophysics-basics slice regression, full Reference Tests, Release Conformance Gate and Offline Edition. Independently verify the changed-file list and unchanged `main`.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged. `main` remains unchanged.
