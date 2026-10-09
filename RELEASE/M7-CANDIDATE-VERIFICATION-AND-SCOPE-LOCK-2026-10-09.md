# M7 Candidate Verification and Scope Lock — 2026-10-09

## Status
**Scope locked for audit/content planning on the isolated M7 branch only.** This authorizes only the four listed M7 targets. It does not authorize changes to `main`, accepted M6 CLEAN, or protected M4/M5 states. Scope lock is not a claim that the new content is complete or CLEAN.

## Baseline
M7 branch starts from accepted M6 CLEAN HEAD `cda7c10a24a2c48249e6a781a9e5976da69d4562`. The current map records 479 slices, 4,763 records, 19 record types, 605 Sources, 1,639 Evidence Use and 64 Relations. These are structural counts only.

## Verification method and limits
- Scanned the complete registered `CONTENT/vertical-slices` tree for equivalent slice names and inspected representative claims in adjacent materials, manufacturing, construction, forestry, chemistry and hand-tool safety slices.
- Checked whether credible public source families exist for the proposed introductory subject and whether the subject has a distinct user goal.
- Reviewed visible source material for source relevance and high-level safety boundaries.
- This is candidate-level verification, not a claim-by-claim content audit. Exact source locators and claim-specific evidence must be checked during authoring and the substantive/evidence audits.

## Locked scope — four candidates

| Target | Decision | User need and non-duplicate boundary | Initial source basis | Required safety / scope limits |
|---|---|---|---|---|
| `woodworking-basics` | INCLUDE | Understand wood selection, moisture/drying, joining, basic shaping, maintenance and repair. Existing `forestry-basics` addresses forest management; `timber-engineering-basics` and `construction-basics` address structural/building contexts; `hand-tool-safety` addresses tool safety. None is a general wood craft/process slice. | USDA Forest Service Forest Products Laboratory, *Wood Handbook* (2021), including drying/moisture, fastenings, and wood use; Illinois 4-H introductory woodworking material. | Distinguish craft guidance from structural design; tools and machines require the existing safety boundaries; no unsafe machine instructions. |
| `papermaking-basics` | INCLUDE | Understand how fibres become paper and how pulp, sheet formation, pressing and drying fit together. Distinct from `digital-preservation-basics` and `archival-science-basics`, which concern preserving information/records rather than producing paper. | Deutsches Technikmuseum Berlin papermaking exhibition; Museum of Fine Arts Boston handmade-paper educational guide; Museo della Carta historical process description. | Identify traditional versus industrial methods; no unsupported claims about durability or archival permanence; control tool/chemical detail if processes expand. |
| `ceramics-basics` | INCLUDE | Understand clay preparation, forming, drying, firing, material properties and limits of ceramic vessels/components. Existing `materials-science-basics` is general and `construction-basics` is building-focused; neither is a ceramics process overview. | University environmental-health-and-safety resources from Princeton and Western Connecticut State University document ceramic process stages and material hazards; source coverage for the process sequence must be supplemented by an authoritative ceramics/materials reference during content drafting. | Explicit silica-dust, glaze/toxic-metal, kiln/combustion, hot-surface and finished-ware leaching boundaries. Avoid presenting improvised kiln/firing procedures as generally safe. |
| `textile-fibre-processing-basics` | INCLUDE | Explain how plant/animal fibres are prepared and transformed into yarn/textile, with variation by fibre and process. No dedicated textile/fibre-processing slice was found in the registry. Distinguish from `materials-science-basics` and `manufacturing-basics` by focusing on fibre preparation and textile process stages rather than general material properties or factory operations. | FAO technical material on coir-fibre processing; FAO AGRIS bibliographic record for a technical manual on long vegetable fibres, plus The Metropolitan Museum of Art's substantive Plant Fibers overview covering flax, hemp, cotton and ramie. The FAO bibliographic record is used only for scope-level corroboration, not detailed process parameters. | Do not universalize one fibre's processing sequence to all fibres; clearly label historical methods and region/material-specific variation; flag chemical, dust and machinery hazards where relevant. |

## Screened but deferred/excluded from M7 scope

| Candidate | Decision | Reason |
|---|---|---|
| `soapmaking-basics` | DEFER | High-consequence caustic chemistry. NIOSH/ATSDR sources establish serious sodium-hydroxide hazards, but this pass does not yet establish a sufficiently bounded, independently supported instructional scope. Reconsider only with a dedicated safety-source plan and precise applicability boundaries. |
| `glassmaking-basics` | DEFER | Strong high-temperature/process hazards and overlap with material science. Requires a narrower, separately justified scope and expert source review. |
| `natural-dyeing-basics` | DEFER | Mordants and colourants create toxicity/environmental boundaries; “natural” must not imply safe. Need a specific, source-backed user task before inclusion. |
| `leather-processing-basics` | DEFER | Potentially valuable but requires source and environmental/chemical boundary work; lower priority than the four selected process chains for this pass. |
| `lime-and-mortar-basics` | DEFER | Significant overlap with construction/materials; inspect construction and historic repair needs in a later targeted map before making a distinct slice. |
| `hand-tool-manufacture-basics` | DEFER | Tool design/manufacture may be too broad and overlaps with manufacturing and hand-tool safety; requires a narrower user task. |

Four candidates are intentionally selected; no target count is imposed. Deferred topics are not declared unnecessary or fully covered.

## Required work for the four locked targets
1. Confirm canonical IDs, record schema and dedicated regression pattern from current neighboring slices.
2. Draft only the claims justified by identified sources; no fixed claim/source count.
3. Create claim-specific Evidence Use descriptions with locators and inferential roles.
4. Add Context and Scope boundaries that make regional, material, process and safety limits visible.
5. Conduct substantive claim-by-claim audit.
6. Conduct evidence-independence/diversity audit per Claim; document when independent corroboration is or is not materially necessary.
7. Conduct Human View/adversarial review for novice comprehension, missing prerequisites and unsafe interpretation.
8. Audit corpus-wide Relations for valid endpoints, justified links and duplicate participant pairs; add none unless materially useful.
9. Consolidate confirmed debts into one M7 Unified Debt Map; perform one controlled correction pass and post-correction audit.
10. Synchronize registry, coverage, README, provenance and dedicated regressions only as required by actual changes.
11. Run Reference tests, Release Conformance Gate and Offline Edition on the exact same final HEAD; independently verify all three and record CLEAN without a post-CI docs-only commit.

## Maturity accounting rule
M7 reports breadth, depth, evidence maturity and Human View/integration separately. Do not use the historical conversational estimates “30–40%” or “45–55%” as measured baselines. Do not claim that adding new slices increases total maturity by the same proportion, or that new introductory slices make already accepted slices less deep. A reproducible scoring rubric, sample, denominator and exact SHA must be established before reporting a numerical maturity score.

## Non-negotiable constraints
- No changes to `main`, accepted M6 CLEAN, or protected M4/M5 states.
- No new Record type without a separately justified architecture decision.
- No fixed record quotas, metric-driven Relations, mass rewrites or weakened tests.
- Scope lock authorizes only these four targets on the isolated M7 branch.
- M7 is CLEAN only after all confirmed debts are closed, audits pass, metadata/regressions match, and all three CI workflows pass on the exact same final HEAD with independent verification.


## M7 authoring/audit update — 2026-10-09

The evidence review added complementary museum evidence for papermaking, university and FDA evidence for ceramics, and substantive plant-fibre material from The Met. Textile Claim C was narrowed to the process scope supported by accessible sources. Supplementary Evidence Use descriptions were normalized to Russian while canonical source titles remain in their original language.


## M7 final audit and CLEAN acceptance — 2026-10-09

**Accepted CLEAN at exact HEAD `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.** This section supersedes the earlier candidate-state and pending-gate wording in this file. It records the final state without changing the historical audit details above.

### Exact-head release verification
- Reference implementation tests #2683 — SUCCESS, run `37917466776`.
- Release Conformance Gate #2597 — SUCCESS, run `37917466763`.
- Offline Edition #2157 — SUCCESS, run `37917466890`.
- All three completed successfully on the same exact HEAD `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
- PR #12 remains open, draft, and unmerged; its head is `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`, and its base is accepted M6 CLEAN `cda7c10a24a2c48249e6a781a9e5976da69d4562`.
- Independent compare: M7 is 50 commits ahead of M6 and 0 behind; `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`, unchanged by this candidate.
- Coverage manifest parses and reports 483 slices / 4,827 Records / 19 Record types.

### Audit outcome and limits
Substantive audit: PASS after controlled corrections. Evidence independence/diversity: PASS with source-scope limits. Human View/adversarial: desk-based PASS with limitations; no live novice study is claimed. Relation delta: PASS; M7 added or changed no Relations. Confirmed M7 debts are resolved as recorded in the unified debt map.

Acceptance was recorded outside the code tree in [PR #12 discussion](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/12#issuecomment-6079202174), preserving the accepted SHA. Do not merge PR #12 as part of M8 setup.
