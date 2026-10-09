# M7 Unified Debt Map — 2026-10-09

Status: OPEN / AUDIT CANDIDATE. This document is not a CLEAN acceptance. Work remains isolated on `m7-gap-map-2026-10-09`; `main`, accepted M6 CLEAN, and protected M4/M5 states are unchanged.

## Scope and snapshot

Four focused slices were authored: `woodworking-basics`, `papermaking-basics`, `ceramics-basics`, and `textile-fibre-processing-basics`. Current candidate target: 4,827 records, 483 slices, 19 record types. No new record type or Relation was introduced; existing Relations were not changed.

## Finding ledger

- **M7-CORR-001 — RESOLVED.** The woodworking dust claim was narrowed and linked to OSHA hazard guidance. Regression and coverage were synchronized; the correction is explicitly authorized.
- **M7-EV-001 — RESOLVED.** Papermaking claims now have claim-specific evidence links across the MFA handmade-paper guide and Deutsches Technikmuseum overview. These sources do not establish industrial settings or special-purpose product suitability.
- **M7-EV-002 — RESOLVED.** Ceramic dust, glaze and firing claims have complementary WCSU/Princeton EHS evidence; FDA material supports the food-contact boundary. No kiln recipes, glaze formulations or universal safety guarantees are asserted.
- **M7-EV-003 — RESOLVED.** The Met Plant Fibers overview now directly supports textile claims B–D. The FAO AGRIS bibliographic record is used only for scope-level corroboration.
- **M7-EV-004 — RESOLVED.** Textile Claim C was narrowed to the process scope supported by accessible sources, without quantitative operating parameters.
- **M7-EV-005 — RESOLVED.** Supplementary Evidence Use descriptions were normalized to Russian; canonical source titles remain unchanged.

## Human View and relation delta

Each slice has a README, Scope/Context boundaries, four Claims, claim-linked Evidence Use and a dedicated regression. Ceramic hazards are framed as boundaries, not instructions for kiln firing or glaze formulation. Paper claims do not infer archival permanence or food-contact suitability from sheet formation. Textile claims do not generalize one fibre's process to all fibres. These are introductory record-based slices, not polished public-facing procedural guides; non-expert usability testing remains a future quality check.

No Relations were added or modified. No M7 record is a Relation participant, so M7 introduces no new Relation endpoints or duplicate participant pairs.

## Post-correction verification required

1. Exact-head schema and semantic preflight, unique record identities, link/provenance checks, coverage and registrations.
2. Content package/recovery preflight and all dedicated regressions.
3. Reference tests, Release Conformance Gate and Offline Edition must all pass on the same final SHA.
4. Independently verify exact SHA, all three results, and PR/base/main state.

M7 remains OPEN until these checks pass on the same final HEAD. Do not add a docs-only commit after successful exact-head CI and call that the accepted checkpoint.
