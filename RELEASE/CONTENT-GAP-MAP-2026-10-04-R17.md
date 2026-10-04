# Gap Map R17 — controlled Wave 17

Date: 4 October 2026

Baseline: **418 vertical slices / 3737 records / 19 Record types / 0 blocking findings**.

## Selection basis

R17 is selected by reconciling candidate domains against the current `CONTENT/vertical-slices` tree after the R16 CLEAN checkpoint.

Priorities:
1. material knowledge coverage;
2. non-duplication with R1–R16;
3. cross-domain leverage;
4. strong authoritative-source availability;
5. semantic richness for existing Standard rules;
6. Human View / safety value;
7. no architectural expansion.

## Controlled ten-slice set

1. `vertical-slices/open-science-basics` — open research practices, access, transparency and evidence boundaries.
2. `vertical-slices/research-integrity-basics` — integrity, responsible conduct, correction and research record boundaries.
3. `vertical-slices/science-policy-basics` — science-policy interfaces, evidence-to-policy translation and uncertainty.
4. `vertical-slices/data-ethics-basics` — ethical use of data, fairness, accountability and contextual limits.
5. `vertical-slices/information-ethics-basics` — information harms, responsibilities, access and ethical information practices.
6. `vertical-slices/health-technology-assessment-basics` — comparative assessment of health technologies; descriptive, non-prescriptive.
7. `vertical-slices/public-health-ethics-basics` — ethical principles in population health decisions; context and jurisdiction bounded.
8. `vertical-slices/economic-geography-basics` — spatial organization of economic activity and regional evidence.
9. `vertical-slices/urban-economics-basics` — cities, land, housing, agglomeration and urban incentives; descriptive.
10. `vertical-slices/ecotoxicology-basics` — pollutants, exposure pathways, ecological effects and uncertainty; no hazardous operational procedures.

## Controlled slice contract

Each slice follows:

**Source → 3 Claims → 3 Evidence Use → Context → Scope + dedicated regression test**

No new Record type is planned.

## Expected increment

**10 slices / 90 records**

Target after authoring:

**428 vertical slices / 3827 records / 19 Record types**

## Domain boundaries

- Open science and research integrity distinguish transparency, provenance, correction and evidential status; openness is not treated as proof of truth.
- Science policy distinguishes evidence from policy judgment and preserves uncertainty and value choices.
- Data/information ethics remains descriptive and avoids individualized legal advice or political persuasion.
- Health technology assessment and public-health ethics remain general informational content, not individualized medical or treatment advice.
- Economic and urban geography/economics claims remain spatial, temporal and institutional-context bounded.
- Ecotoxicology remains descriptive; no actionable instructions for producing, concentrating or deploying hazardous substances are introduced.

## Definition of Done

R17 remains open until:
- all ten slices satisfy the canonical content contract;
- dedicated regressions pass;
- corpus coverage is synchronized;
- Human View and provenance/evidence boundaries pass;
- package/recovery integrity passes;
- Reference Tests, Release Gate and Offline Edition pass;
- substantive R17 audit finds 0 blocking findings;
- the resulting CLEAN checkpoint is evidenced on the canonical commit.

The full R1–R17 project/corpus audit remains deferred to the planned R20 gate.
