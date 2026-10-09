# M10 Controlled Correction Scope Lock — 2026-10-09

## Status

**IMPLEMENTED; post-correction desk audit recorded. Exact-head CI and independent final verification are pending.** M10 is isolated on `m10-gap-map-2026-10-09`, based on M9 candidate HEAD `40537f67ad8e4faf5f3b840aa49946f1902a236a`. M9 remains CLEAN on its own branch/PR state; this successor does not rewrite M9, alter `main`, or change protected M4/M5/M7/M8 checkpoints.

## Basis

M8's frozen 43-Claim diagnostic rated `human-settlement-systems-basics` as an unresolved explanatory-depth/integration opportunity: Claim A was a broad system definition with limited mechanisms/examples; Claim B named components but not dependency pathways; Claim C stated integrated planning but lacked a concrete explanation. M10's read-only review of the current 11-record slice confirms that the dedicated regression checks counts and links but does not protect these explanatory properties. This is a confirmed depth/contract gap, not a claim that the slice is false or unsafe.

Official source scope checked against the existing canonical locators:
- UN — Human Settlements: settlements serve protective, economic, resource-management and social functions; settlement outcomes include infrastructure, services, inequality and environmental dimensions.
- World Bank Group — Infrastructure / Urban Development: existing Evidence Use describes energy, transport, water, sanitation, basic services and urban systems as interdependent.
- OECD — Sustainable urban development: existing Evidence Use describes coordination across water, housing, transport, infrastructure, energy and land use and the need to address sectoral fragmentation.

## Implemented scope

The first CI preflight correctly rejected the edited existing slice because the shared editorial correction registry did not yet authorize M10. The registry is now updated on this M10 branch only, adding the three M10 finding IDs and the single authorized slice. This is an explicit authorization record, not an expansion of content scope.

1. The three existing Claims now explain settlement functions, interdependence among housing/basic services/infrastructure, and the purpose and limits of integrated planning.
2. The three linked Evidence Use descriptions now state the source-specific contribution and avoid implying that broad global sources prescribe local designs or guarantee local outcomes.
3. The README now gives a Russian-facing orientation, a bounded illustrative dependency example and an explicit local-data/specialist boundary.
4. The dedicated regression preserves the original count/type/linkage checks and now asserts explanatory mechanisms, source limits and the human-facing boundary.

All original IDs, provenance methods, claim/source references, `supports` roles, canonical source identities/URLs, Context/Scope records and target refs were preserved.

## Non-negotiable limits and verification

- No new Record type, Source, Evidence Use, Context, Scope or Relation was added.
- The shared `RELEASE/EDITORIAL-CORRECTION.json` was updated only to record this explicit M10 authorization. No unrelated registry entries were changed.
- No other slice, release gate, architecture, `main`, or prior accepted checkpoint was changed.
- No numeric thresholds, universal outcomes, engineering recommendations or site-specific prescriptions were added.
- The correction is limited to the three Claims, their three Evidence Use descriptions, README, dedicated regression and the single required M10 authorization entry in `RELEASE/EDITORIAL-CORRECTION.json`.
- Post-correction claim/evidence/source-scope/Human View/Relation desk audit is recorded in `M10-POST-CORRECTION-AUDIT-2026-10-09.md`.
- Run the targeted regression, reconcile actual coverage, then run Reference tests, Release Conformance Gate and Offline Edition on the exact same final HEAD.
- Record M10 CLEAN only after exact-head 3/3 PASS and independent PR/base/main/diff verification. Any commit after CI invalidates the gate and requires a fresh 3/3 run. Do not merge or promote this branch as part of the checkpoint.
