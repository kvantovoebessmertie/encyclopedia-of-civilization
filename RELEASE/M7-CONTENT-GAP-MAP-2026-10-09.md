# M7 Content Gap Map — 2026-10-09

## Status
**PLANNING / CANDIDATE SCREEN ONLY — scope not locked; no content edits authorized.**

M7 is planned from accepted M6 CLEAN HEAD `cda7c10a24a2c48249e6a781a9e5976da69d4562`. M6 remains accepted and closed. M4/M5 protected states and `main` must not be changed. This map is a new M7 planning artifact on branch `m7-gap-map-2026-10-09`.

## Baseline
At accepted M6 HEAD, `RELEASE/CONTENT-COVERAGE.json` reports:
- 479 vertical slices
- 4,763 records
- 19 record types, all 19 with direct corpus coverage
- 605 Sources
- 1,639 Evidence Use
- 64 Relations

These counts measure corpus structure, not truth, completeness, or practical usability. The previous M6 map identified domain breadth as expandable and stated that coverage is representative rather than exhaustive. The project readiness roadmap prioritizes depth, independent evidence, integration and Human View alongside new breadth.

## Selection method
A read-only scan of the accepted M6 tree found no dedicated slices matching the following candidate production/craft processes: textile/fibre production, ceramics/pottery, papermaking, glassmaking, soapmaking, leather processing, woodworking, natural dyeing, lime/mortar production, and hand-tool manufacture. Existing adjacent coverage includes materials science, metallurgy, manufacturing, forestry, construction, chemistry, food systems, and hand-tool safety. Adjacent coverage must be inspected for conceptual overlap before any candidate is admitted.

This is a preliminary gap signal, not proof that each topic warrants a separate slice. The candidates are selected because durable craft and production processes connect raw materials to tools, shelter, sanitation, storage, repair and small-scale manufacturing—central capabilities for the encyclopedia's stated long-term purpose.

## M7 candidate set — not yet authorized
| Candidate | Why it may matter | Overlap / risk to resolve before scope lock |
|---|---|---|
| `textile-production-basics` | Fibres, yarn, weaving/knitting, durability and repair; clothing, coverings and cordage | Distinguish fibre/textile processes from existing materials, agriculture, and manufacturing slices |
| `ceramics-basics` | Clay preparation, forming, firing, vessels and durable components | Keep safe, descriptive process boundaries; distinguish from materials science and construction |
| `papermaking-basics` | Plant fibre, pulp, sheet formation, drying and durable knowledge transmission | Separate traditional process knowledge from industrial paper chemistry and archival preservation |
| `glassmaking-basics` | Silica-based materials, forming, annealing and use cases | High-temperature hazards; no unsupported furnace recipes or unsafe procedural detail |
| `soapmaking-basics` | Hygiene-related production, fats/oils, alkali chemistry and quality boundaries | Chemical burn/caustic hazards; must use authoritative chemistry/safety sources and clear limits |
| `leather-processing-basics` | Preservation and transformation of hides, material properties and repair | Environmental/chemical hazards; overlap with animal systems, conservation and manufacturing |
| `woodworking-basics` | Selecting, drying, joining and repairing wood; practical construction and tool use | Distinguish from timber engineering, forestry, construction and hand-tool safety |
| `natural-dyeing-basics` | Colourants, fibre compatibility, mordants and reproducibility | Toxicity and environmental effects; avoid implying natural means safe |
| `lime-and-mortar-basics` | Lime, aggregates, binders, curing and repair of masonry | Overlap with construction/materials; safety and historic formulations need clear context |
| `hand-tool-manufacture-basics` | Basic tool design, material selection, edge/handle concepts, maintenance and repair | Distinguish tool manufacture from hand-tool safety and manufacturing systems; avoid hazardous construction detail |

## Required candidate verification before scope lock
For every proposed candidate:
1. Search the complete current slice registry and aliases for duplicates or existing equivalent coverage.
2. Inspect adjacent slices and existing cross-slice Relations; do not split a topic merely to create breadth.
3. Identify credible, traceable sources that actually support the intended introductory claims. Source availability is not assumed by this map.
4. Define a concrete user question and a domain-appropriate Scope/Context boundary.
5. Assess safety and misuse risks, especially caustic chemistry, high-temperature processes, dust, tools and toxic treatments.
6. Decide INCLUDE or EXCLUDE with a written reason. If fewer than ten candidates survive, do not fill the set by quota.
7. Lock scope only after the verification table is complete.

## M7 sequence
1. Candidate verification and duplicate/overlap scan.
2. Scope lock (planning only; no content edits before authorization).
3. Controlled content maturation only for confirmed candidates.
4. Substantive claim-by-claim audit.
5. Evidence independence/diversity audit per Claim.
6. Human View and adversarial audit.
7. Relation endpoint, justification and duplicate audit.
8. Unified M7 Debt Map containing confirmed findings only.
9. One controlled correction pass, then post-correction re-audit.
10. Synchronize registry, coverage, README, provenance and dedicated regressions where actually changed.
11. Run Reference tests, Release Conformance Gate and Offline Edition on the exact same final HEAD.
12. Independently verify exact SHA and all three results; record CLEAN acceptance without a docs-only commit after successful CI.

## Non-negotiable constraints
- No fixed Record/Claim/Source quota and no expansion merely to increase counts.
- No new Record type without a separately justified architecture decision.
- No speculative or metric-driven Relations.
- No mass rewrite or unrelated corrections.
- No weakened schemas, semantic checks, regressions or CI.
- Preserve accepted M6 CLEAN; do not modify `main`, protected M4/M5 states, or the M6 accepted checkpoint.
- M7 must be judged by user value, evidence quality, applicability boundaries and regressions—not record count alone.

## Definition of Done
M7 is CLEAN only when every confirmed debt in its unified map is resolved, post-correction audits pass, metadata and regressions match actual content, and Reference + Release Gate + Offline Edition are all GREEN on the exact same final HEAD with independent verification. This Gap Map alone does not claim M7 completion.


## Maturity measurement — prevent breadth from masking depth

M7 must not interpret a lower average maturity caused by newly added introductory slices as regression in already accepted knowledge. Nor may adding slices be presented as evidence that the whole encyclopedia is proportionally more complete.

Track four separate dimensions, with a stable definition and explicit denominator:
1. **Breadth:** registered domains/slices, plus a documented map of uncovered high-value user needs. Slice count is descriptive, not a completeness percentage.
2. **Depth:** proportion of audited Claims with direct, traceable support, meaningful Scope/Context, known/unknown boundaries, and domain-appropriate explanation. Report audited sample and total; do not infer whole-corpus depth from a few M stages.
3. **Evidence maturity:** claim-level source fit and independent corroboration where materially needed; distinguish single-source claims with a justified rationale from unresolved evidence debt.
4. **Human usability/integration:** audited ability to find, understand, and safely apply knowledge, plus justified cross-domain Relations. CI conformance is necessary but not a proxy for these dimensions.

For each dimension, record numerator, denominator, audit method, date, and exact corpus SHA. Do not collapse the four dimensions into one “project completion” percentage until a defensible weighting model exists. Historical conversational estimates such as “30–40%” or “45–55%” are not measured baselines and must not be compared as if they were. The M7 baseline is therefore **not yet numerically scored**; first establish a reproducible sampling and scoring method on representative existing slices, including previously matured high-consequence slices and ordinary introductory slices.

### M7 operating choice

Do not automatically create ten new slices. Candidate verification may result in a smaller batch, a targeted depth pass on existing slices, or a mixed scope. Prefer the option that closes the largest verified user-value gap without lowering quality. Existing accepted slices are never rewritten merely to raise a score; any correction requires a concrete finding.
