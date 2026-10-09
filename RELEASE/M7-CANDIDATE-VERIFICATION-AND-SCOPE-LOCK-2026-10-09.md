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


## M7 post-correction audit record — 2026-10-09

This section supersedes the pre-authoring checklist above for the four locked M7 slices only. It records the completed desk-based audits after the source-fit corrections. Prior candidate HEAD df3babfe246dea4ce8e58ed21eb03ad400915041 passed Content preflight and all three CI workflows. The later status-reconciliation HEAD 08e94930b55fb070c3361d6d03042cfee7131d79 also passed Reference tests #2667, Release Conformance Gate #2590 and Offline Edition #2141. This checkpoint-candidate commit creates a new HEAD; final CLEAN acceptance requires all three workflows green on that exact resulting HEAD and independent verification of PR/base/main.

### 1. Substantive claim audit

| Slice / Claim | Result | Source-fit and boundary |
|---|---|---|
| woodworking A | PASS | USDA Forest Products Laboratory Wood Handbook covers moisture, drying and dimensional change; no universal shrinkage value is claimed. |
| woodworking B | PASS WITH BOUNDARY | Wood Handbook supports variability in properties. Visual inspection is explicitly not a substitute for structural design. |
| woodworking C | PASS | Illinois 4-H supports a basic operations overview; no machine settings or universal tool prescription. |
| woodworking D | PASS AFTER CORRECTION | Claim narrowed to wood-dust exposure and linked to OSHA; controls remain process- and jurisdiction-specific. |
| papermaking A | PASS | MFA and Deutsches Technikmuseum support the broad handmade sheet-forming, pressing and drying sequence. |
| papermaking B | PASS | Museum sources support fibre preparation and process variation; no universal pulp formula. |
| papermaking C | PASS | Both sources distinguish forming, pressing and drying; no quantitative settings inferred. |
| papermaking D | PASS AS EPISTEMIC BOUNDARY | Available sources do not certify archival permanence or food-contact suitability; claim warns against inferring those properties from sheet formation alone. |
| ceramics A | PASS | WCSU and Princeton EHS support dry-clay dust hazards; no universal exposure limit. |
| ceramics B | PASS | University EHS sources support checking the actual glaze composition and safety information; no claim that all glazes are identical. |
| ceramics C | PASS | WCSU and Princeton EHS support process-specific firing hazards; no universal kiln or ventilation design. |
| ceramics D | PASS | Princeton EHS and FDA support the narrow leaching/food-contact boundary; not a product certification. |
| textile A | PASS WITH SCOPE LIMIT | FAO coir is a specific example; The Met adds broader plant-fibre context. Operations vary by fibre. |
| textile B | PASS AFTER CORRECTION | Wording now describes possible preparation operations and fibre-specific variation; unsupported uniformity mechanism removed. |
| textile C | PASS AFTER CORRECTION | Wording now follows The Met's accessible scope on joining/twisting fibres into yarn and later processing; FAO AGRIS is not treated as detailed process evidence. |
| textile D | PASS AFTER CORRECTION | Wording now states that fibres and processing differ and yarn suitability should be assessed against the intended product, not categorical non-interchangeability. |

### 2. Evidence independence and diversity

- Woodworking: USDA Wood Handbook is a suitable source for bounded introductory moisture/property claims; Illinois 4-H is a separate educational source for craft operations; OSHA is the direct occupational-hazard source for wood dust. The USDA claims are not falsely described as independently corroborated by another institution.
- Papermaking: MFA and Deutsches Technikmuseum are complementary sources from distinct institutions for the broad handmade process. Neither establishes industrial settings or special-purpose product suitability.
- Ceramics: WCSU and Princeton EHS provide complementary institutional hazard coverage. FDA is used only for the foodware/leaching boundary, not as a general ceramics-process source.
- Textile: The Met is the substantive accessible source for Claims B–D. FAO AGRIS is a bibliographic record and is counted only for topic/scope corroboration, not detailed technical parameters. The FAO coir page remains a fibre-specific source for Claim A.
- No source-count quota was applied. A single source is accepted where its authority and the narrow claim make additional corroboration low-value; safety-relevant claims receive complementary evidence where it materially improves support.

### 3. Human View / adversarial review

**Desk-based PASS WITH LIMITATIONS.** Local READMEs and Scope/Context records identify each subject and its limits without requiring a reader to understand the architecture. Four English-language Evidence Use descriptions (ceramic Claim A corroboration and textile Claims B–D) were normalized to Russian. The textile claims were also narrowed to reduce unsupported inferences. Canonical source identities and titles remain unchanged.

Adversarial cases considered: visual wood inspection mistaken for structural approval; handmade paper mistaken as archival/food-contact certified; fired ceramics mistaken as automatically food-safe; one fibre's process generalized to all plant fibres; this introductory material mistaken for kiln/ventilation engineering instructions. The current records explicitly bound these interpretations. This is not an observed novice usability study; task-based testing remains future work before treating the slices as polished public-facing how-to guides.

### 4. Relation endpoint, justification and duplicate audit

No M7 Relation records were added or modified, and none of the four M7 slices participates in existing Relations. Therefore M7 introduces no new endpoints, dangling references or duplicate participant pairs. The synchronized cross-slice audit records 57 Relations in the cross-slice-linkage slice; the broader corpus coverage manifest records 64 Relations total. The carried-forward linkage baseline reports no confirmed broken endpoints, duplicate unordered participant pairs, exact duplicate clusters or critical contradictions. No Relation was added merely to increase counts.

### 5. Remaining release gate

These audits are recorded, but final CLEAN acceptance is conditional. The final checkpoint-record commit changes the tree; rerun all three workflows on its exact resulting HEAD and independently verify the SHA, workflow results, PR/base, and protected branch state. Do not reuse prior-head CI as acceptance. Do not merge PR #12 as part of this checkpoint.
