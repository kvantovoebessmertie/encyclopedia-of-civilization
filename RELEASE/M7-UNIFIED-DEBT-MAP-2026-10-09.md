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
- **M7-EV-005 — RESOLVED.** Human-facing Evidence Use descriptions are normalized to Russian across the four M7 slices; canonical source identities and titles remain unchanged.
- **M7-HV-001 — RESOLVED.** Human View review found English-language descriptions in the ceramic Claim A corroboration and textile Claims B–D Evidence Use records. These four descriptions were translated to Russian without changing claim/source links or evidentiary scope.
- **M7-DOC-001 — RESOLVED.** The shared editorial-authorization registry incorrectly stated that M6 remained OPEN, and ROADMAP.md repeated the stale M6 status. Both were reconciled with the independently accepted M6 CLEAN checkpoint; M6 history and authorizations were retained, while M7 remains OPEN.
- **M7-SUB-001 — RESOLVED.** Textile Claim B no longer asserts that alignment necessarily creates a more uniform fibre flow; it now describes preparation operations and fibre-specific variation.
- **M7-SUB-002 — RESOLVED.** Textile Claim C was narrowed to the yarn-formation and later-processing scope supported by The Met; the FAO AGRIS bibliographic record is not treated as detailed process evidence.
- **M7-SUB-003 — RESOLVED.** Textile Claim D was narrowed from categorical non-interchangeability to fibre/process differences and assessment against the intended product's requirements.

## Human View, substantive and relation audit results

**Substantive audit: PASS AFTER CONTROLLED CORRECTIONS.** All 16 Claims were reviewed against recorded source identities, claim-linked Evidence Use and source-scope limits. Woodworking claims remain bounded to moisture/properties, introductory operations and OSHA wood-dust hazards. Papermaking claims describe the handmade process without industrial parameters; Claim D is an epistemic boundary, not product-suitability certification. Ceramic claims cover dust, glaze hazards, firing hazards and the narrow food-contact/leaching boundary without universal exposure limits, kiln designs or glaze recipes. Textile claims were tightened where necessary to accessible source scope; no quantitative settings are asserted.

**Evidence independence audit: PASS WITH SOURCE-SCOPE LIMITS.** Papermaking uses complementary MFA and Deutsches Technikmuseum material. Ceramics uses WCSU/Princeton EHS and FDA only for its narrow foodware boundary. Woodworking uses the USDA Wood Handbook for bounded introductory material claims, Illinois 4-H for craft operations and OSHA for dust hazards. The Met is the substantive source for textile Claims B–D; FAO AGRIS is bibliographic-only and is not counted as detailed technical corroboration. No source-count quota or artificial corroboration was used.

**Human View/adversarial audit: DESK-BASED PASS WITH LIMITATIONS.** Local READMEs and Scope/Context records make the subject and limits discoverable without reading the architecture. Four English-language Evidence Use descriptions were normalized to Russian. Adversarial cases considered unsafe transfer from visual wood inspection to structural use, paper sheet formation to archival/food suitability, ceramic firing to food-contact safety, and one fibre's process to all plant fibres. These are introductory record-based slices, not step-by-step public-facing guides; live novice testing remains future work and is not claimed complete.

**Relation audit: PASS FOR M7 DELTA; PRIOR LINKAGE BASELINE CARRIED FORWARD.** No M7 Relation records or participants exist, and no Relations were added or modified. The synchronized cross-slice audit records 57 Relations in the cross-slice-linkage slice; the broader coverage manifest records 64 Relations total. The prior baseline reports no confirmed broken endpoints or duplicate unordered participant pairs. M7 adds no new endpoint or pair.

## Final verification status

The prior candidate HEAD `df3babfe246dea4ce8e58ed21eb03ad400915041` passed Content preflight, the four dedicated regressions through the Reference suite, Reference implementation tests #2656, Release Conformance Gate #2585, and Offline Edition #2130. All three workflows completed successfully on that same prior SHA.

This status-reconciliation commit changes the candidate HEAD. Required next steps are therefore: (1) rerun all three workflows on the exact resulting HEAD; (2) independently verify that all results refer to that SHA and verify PR #12 remains open/draft/unmerged against the accepted M6 base, with protected main and M4/M5 states unchanged; (3) only then prepare any final CLEAN acceptance record and repeat exact-head CI if that record changes the tree.

M7 remains OPEN. The audit results above are recorded, but prior-head CI cannot be reused as proof for a later SHA.
