# Content Domain Roadmap — Ten-Slice Audit — 2026-09-30

## Scope

This audit covers the first ten-slice working set from CONTENT/DOMAIN-ROADMAP.md:
ratios-and-percentages, probability-basics, motion-basics, energy-basics, matter-basics, cell-basics, earth-system-basics, anatomy-basics, economics-basics, computing-basics.

## Corpus delta

- New vertical slices: 10
- New Records: 86
- New Record types: 0
- Resulting control point: 187 vertical slices / 1634 Records / 19 Record types

## Structural audit

- Every slice has a README and a records directory.
- Ratios-and-percentages and probability-basics each contain 7 Records: Source + 2 Claims + 2 Evidence Use + Context + Scope.
- The remaining eight slices each contain 9 Records: Source + 3 Claims + 3 Evidence Use + Context + Scope.
- 86/86 Records were checked for JSON validity, record envelope, schema version, publication status, completion status, record identity, record type and provenance presence: PASS.
- 10/10 dedicated vertical-slice regression tests are present.

## Semantic audit

The expansion reuses the existing Source → Claim → Evidence Use → Context → Scope pattern and introduces no new semantic type. Claims are scoped as introductory educational statements and evidence use is explicitly marked as support without inference beyond the source. No slice introduces a hazardous operational procedure or a new high-consequence instruction class.

## Domain-specific boundaries

- Mathematical slices remain descriptive and educational; percentage and probability statements are not presented as universal conclusions outside their defined models.
- Motion and energy statements remain within the classical introductory physics frame and retain system/reference-frame boundaries.
- Matter and cell slices distinguish basic classifications without turning descriptive science into laboratory procedure.
- Earth-system claims describe interacting spheres and observation/modeling rather than operational hazard instructions.
- Anatomy is descriptive and educational, not individualized medical advice.
- Economics distinguishes micro/macro scope and treats models as assumption-dependent representations.
- Computing describes algorithms and system components without operational cyber abuse procedures.

## Result

The ten-slice content block is structurally and semantically ready for the corpus-wide Reference regression and Release Conformance Gate. Promotion to v2.2 baseline is intentionally deferred until those gates return green.
