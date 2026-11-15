# M13 Geophysics C USGS source-fit authorization

Date: 2026-11-15
Authorization ID: M13-GEOPHYSICS-C-USGS-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `9f4173fd3446197160449471637c429d18684109`
Status: AUTHORIZED FOR ONE SOURCE AND ONE VERSIONED EVIDENCE USE UPDATE

## Finding

Package 29 marks `CLM-GEOPHYSICS_BASICS-C` PARTIAL because the registered USGS glossary lists individual geophysical methods but does not establish the integrated use of surface/ground observations, remote measurements and models to interpret concealed subsurface areas.

The USGS project page *Geophysical Mapping of Geologic Systems Host to Critical Mineral Deposits, Southern Midcontinent, US* (September 27, 2024) explicitly describes high-resolution airborne and regional ground geophysical methods; collecting, modelling and interpreting airborne and ground data; drill-core examination where available; airborne magnetic/radiometric surveys; airborne electromagnetics; ground magnetotellurics; and 3D inversions. It is a concrete regional project example, not a universal workflow. USGS-authored information is public domain in the United States with proper credit; separately copyrighted third-party images/media are excluded.

## Exact authorized changes

1. Add only `CONTENT/vertical-slices/geophysics-basics/records/SRC-USGS-GEOPHYSICAL-MAPPING-SOUTHERN-MIDCONTINENT.json` as Source v1 with the official USGS project page URI.
2. Version only `EU-GEOPHYSICS_BASICS-C` from v1 to v2. Change only `record_version`, `provenance.created_from[0]`, `content.source_ref`, and `content.material.description`. Preserve Claim C@1, evidence_role, record ID, schema, statuses and all other fields. The description must identify this as a regional example and preserve the limitation that drill-core examination is conditional on availability.
3. Update only `CONTENT/vertical-slices/geophysics-basics/README.md` to identify the added source and its scope limit.
4. Add only `REFERENCE/tests/test_content_geophysics_basics_vertical_slice.py` to verify exact source/evidence lineage, the 10-record slice structure and the stated scope limitation.
5. Update only `RELEASE/CONTENT-COVERAGE.json` actual totals: total records 4,850 → 4,851 and Source count 626 → 627. Keep Claims, Evidence Use, slice count and all other counts unchanged.
6. Update only `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json` corpus.records from 4,850 to 4,851 and explanatory corpus-scope/next-step text. Preserve 483 slices, 57 Relations, prior findings and epistemic boundary; describe this as count reconciliation, not a new substantive Relation audit.
7. Register this exact authorization and finding ID in `RELEASE/EDITORIAL-CORRECTION.json`.
8. Add a checkpoint recording the source, pinpoint, rights boundary, scope limitation, count reconciliation and required checks.

## Exclusions

Do not change Claim C or any other Claim, other Source/Evidence Use, Context, Scope, Relation, risk metadata, D/E/B ledger, or other README/test. Do not generalize the USGS regional project into a universal geophysics rule. No publication/release approval, main update or PR merge is authorized. M13 remains OPEN / NOT RELEASE-READY.
