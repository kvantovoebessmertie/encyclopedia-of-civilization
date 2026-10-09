# M10 Controlled Correction Scope Lock — 2026-10-09

## Status

**SCOPE LOCKED; implementation and post-correction audit not yet complete.** M10 is isolated on `m10-gap-map-2026-10-09`, based on M9 candidate HEAD `40537f67ad8e4faf5f3b840aa49946f1902a236a`. M9 remains CLEAN on its own branch/PR state; this successor does not rewrite M9, alter `main`, or change protected M4/M5/M7/M8 checkpoints.

## Basis

M8's frozen 43-Claim diagnostic rated `human-settlement-systems-basics` as an unresolved explanatory-depth/integration opportunity: Claim A was a broad system definition with limited mechanisms/examples; Claim B named components but not dependency pathways; Claim C stated integrated planning but lacked a concrete explanation. M10's read-only review of the current 11-record slice confirms that the dedicated regression checks counts and links but does not protect these explanatory properties. This is a confirmed depth/contract gap, not a claim that the slice is false or unsafe.

Official source scope checked against the existing canonical locators:
- UN — Human Settlements: settlements serve protective, economic, resource-management and social functions; settlement outcomes include infrastructure, services, inequality and environmental dimensions.
- World Bank Group — Infrastructure / Urban Development: existing Evidence Use describes energy, transport, water, sanitation, basic services and urban systems as interdependent.
- OECD — Sustainable urban development: existing Evidence Use describes coordination across water, housing, transport, infrastructure, energy and land use and the need to address sectoral fragmentation.

## Authorized target files and actions

1. `CONTENT/vertical-slices/human-settlement-systems-basics/records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-A.json`
   - Clarify the settlement as a socio-spatial system and explain at least one mechanism linking residents, shared services/resources and the surrounding environment.
   - Keep the claim introductory and broadly applicable; do not imply every settlement has the same structure.

2. `CONTENT/vertical-slices/human-settlement-systems-basics/records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-B.json`
   - Make at least one dependency pathway explicit (for example, land use/location affecting access to transport and services) using only support warranted by existing linked sources.
   - Do not turn an illustrative relationship into a universal causal guarantee.

3. `CONTENT/vertical-slices/human-settlement-systems-basics/records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-C.json`
   - Explain what integrated planning coordinates across sectors and why isolated decisions can conflict, without presenting a policy preference as a universal technical fact.

4. The three corresponding Evidence Use records:
   - Replace list-like descriptions with claim-specific explanations of what each source supports.
   - Preserve the existing claim/source references, `supports` roles, record IDs, provenance methods, canonical source identities and URLs.
   - State source limits; do not imply the three broad sources prove local outcomes or prescribe a specific settlement design.

5. `CONTENT/vertical-slices/human-settlement-systems-basics/README.md`, Context and Scope:
   - Provide a concise Russian-facing explanation and one clearly marked illustrative dependency example.
   - Keep the existing boundary: this is foundational systems knowledge, not a site-specific design, engineering calculation, legal opinion or operational instruction.

6. `REFERENCE/tests/test_content_human_settlement_systems_basics_vertical_slice.py`
   - Retain the existing 11-record/type/linkage checks.
   - Add assertions for the intended explanatory mechanisms, dependency pathway, integrated-planning distinction and explicit illustrative/boundary language.
   - Do not weaken any existing assertion to make the correction pass.

## Non-negotiable limits

- No new Record type.
- No new Source, Evidence Use, Context, Scope or Relation is authorized in this pass.
- Do not change any other slice, shared registry, release gate, architecture, `main`, or prior accepted checkpoint.
- Do not change canonical source identity or URL to improve presentation.
- Do not add unsupported numeric thresholds, universal outcomes, engineering recommendations or site-specific prescriptions.
- If an intended detail is not adequately supported by the existing linked sources, omit it rather than broaden the scope.
- After implementation: run the targeted regression, audit claim/evidence/source scope and Human View, verify no structural/Relation delta, reconcile coverage, then run Reference tests, Release Conformance Gate and Offline Edition on the exact same final HEAD.
- Record M10 CLEAN only after exact-head 3/3 PASS and independent PR/base/main/diff verification. Any commit after CI invalidates the gate and requires a fresh 3/3 run. Do not merge or promote this branch as part of the checkpoint.

## Expected structural delta

Zero new or deleted Records, Sources, Relations, or Record types; zero slice-count change. Text changes are limited to the three Claims, their three linked Evidence Use descriptions, the slice README and dedicated regression. Context/Scope may be clarified only if their existing boundary becomes inconsistent with the revised wording; any such change must remain within these two files and must not alter target refs.
