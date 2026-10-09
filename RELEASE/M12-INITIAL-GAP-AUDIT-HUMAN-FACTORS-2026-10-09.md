# M12 Initial Gap Audit — Human Factors — 2026-10-09

## Candidate and baseline

Candidate: `CONTENT/vertical-slices/human-factors-basics`.
Baseline is M11 amended CLEAN candidate HEAD `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`, branch `m11-gap-map-after-m10-human-view-2026-10-09`. M12 is isolated on `m12-human-factors-source-and-human-view-2026-10-09`; no changes to `main`, M11, or protected earlier checkpoints.

## Read-only findings

- `M12-HF-001` — the README is a machine-facing stub, not a Russian-facing explanation for an ordinary reader.
- `M12-HF-002` — all three Evidence Use descriptions are generic and do not identify claim-specific source contributions.
- `M12-HF-003` — Claim B states that limits of perception, attention and decision-making affect safety and system effectiveness. The recorded locator has not been independently retrieved, so this wording is not sufficiently source-bounded.
- `M12-HF-004` — the dedicated regression needs content contracts for README orientation, claim/evidence/source linkage, evidence specificity, and applicability boundaries.
- `M12-HF-005` — the Source record points to `https://www.nasa.gov/reference/human-factors/`, which was not independently retrievable in the prior M11 review. This is an unresolved locator/source-fit limitation, not proof that the URL is broken.

## Independent source verification

An official NASA Johnson Space Center page, **Human Factors & Performance**, is currently retrievable at:
`https://www.nasa.gov/reference/jsc-human-factors-performance/`

The page explicitly discusses human capabilities, limitations and behavior; human-system interactions including displays, controls, workstations, vehicles and habitats; human-centered design; human-systems integration; workload, usability, fatigue, situation awareness and human error; task analysis and human-in-the-loop evaluation. This source is a better direct fit for a bounded introductory slice than the unverified locator. It does not support every broad phrase in the existing Claims as currently written, so Claims must be narrowed to the page's actual content.

Official NASA source reviewed: https://www.nasa.gov/reference/jsc-human-factors-performance/ (retrieved 2026-10-09). A separate NASA technical standard exists, but this pass does not claim independent multi-source triangulation; all three Claims remain explicitly single-source unless additional source records are separately authorized.

## Structural inventory

The existing slice contains nine records: one Source, three Claims, three Evidence Use, one Context and one Scope. It uses the existing registered Record types. No new Record type is warranted for this bounded correction.

## Proposed bounded M12 scope

Correct the existing human-factors slice and its dedicated regression only after a written authorization:
- replace the unverified locator with the verified official NASA JSC Human Factors & Performance page, preserving the Source record ID and explicitly documenting why the locator changed;
- narrow existing Claim wording to statements directly supported by that page;
- make each existing Evidence Use claim-specific and state its evidence boundary;
- replace the stub README with a Russian-facing explanation, a bounded illustrative example and clear limits;
- strengthen the existing dedicated regression;
- add M12 audit/authorization/debt metadata.

No new Records or Sources are planned in this pass. No Context/Scope edits, Relation edits, record ID changes, provenance changes, or Record-type changes are authorized by this initial audit.

## Acceptance gates

1. Scope lock and authorization committed before content correction.
2. Review every changed Claim, Evidence Use, README and regression against the exact NASA page.
3. Verify IDs, provenance, Claim/Source refs, evidence roles, Context/Scope, coverage and Relations.
4. Run targeted regression and all three release workflows on one identical final HEAD.
5. Independently verify exact diff, branch/base/PR state and unchanged `main`.
6. Keep M12 candidate unmerged and draft until the acceptance evidence is complete.

**Initial decision: findings confirmed; correction is not yet authorized by this audit alone.**
