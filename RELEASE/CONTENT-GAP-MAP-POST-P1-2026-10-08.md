# Post-P1 Content Gap Map — 2026-10-08

## Baseline

- Protected P1 CLEAN checkpoint: `3209950f23ffce503ab6e5a448be40364e656b24`
- Corpus: 479 vertical slices / 4601 Records / 19 Record types
- Relations: 51 total
- P1 emergency/high-consequence maturation is CLOSED and is not reopened without verified regression.

## Audit method

This Gap Map was produced against the current repository tree after P1 CLEAN.

Priority is not assigned by an artificial number of slices. Candidate work is selected where the current corpus shows a material maturity asymmetry that affects reuse, evidence diversity, applicability, or Human View.

## Findings

### G1 — Thin foundational subject slices

Six subject slices remain at the older 7-record profile:

1. `probability-basics`
2. `ratios-and-percentages`
3. `seed-storage-basics`
4. `si-units-basics`
5. `time-standard-basics`
6. `water`

The first five are foundational knowledge slices with only two Claims and one source/evidence track. The `water` slice is safety-relevant and contains three Claims, but still has a single source/evidence track.

This is a genuine maturity asymmetry because the corpus now contains a large population of expanded slices with stronger claim depth and independent evidence, while these six remain materially thinner.

### G2 — Evidence diversity

For the six candidates, verify whether a second genuinely independent source materially improves reuse.

- Mathematics/standards slices: prefer independent standards or institutional/scientific sources where the claims warrant corroboration.
- Seed storage: prefer an independent agricultural/scientific institutional source with clearly bounded applicability.
- Water safety: prioritize independent corroboration because the topic is high-consequence.
- No second source is added merely to increase a count.

### G3 — Claim depth and applicability

Audit whether each candidate needs:
- a mechanism/dependency claim;
- conditions or limitations;
- an explicit uncertainty/applicability boundary;
- a third Claim where materially useful.

No quota of three Claims is imposed. Existing claims are not rewritten unless the audit finds a real semantic defect.

### G4 — Cross-domain linkage

Evaluate only material dependencies:
- probability ↔ statistics/measurement;
- ratios/percentages ↔ measurement/units;
- SI units ↔ measurement/uncertainty;
- time standards ↔ astronomy/geospatial/computing where a real dependency is present;
- seed storage ↔ agriculture/food systems;
- water ↔ emergency water storage/water infrastructure/public health.

Relations are added only when they improve conceptual reuse and do not merely connect coexisting topics.

### G5 — Human View

The six slices must remain educational and bounded:
- mathematical/standards content must not imply unsupported real-world precision;
- seed-storage content must not become crop-specific professional advice without scope;
- water content must retain hazard boundaries and emergency escalation where relevant;
- no live/local authority instruction is inferred from static knowledge.

## Priority decision

The six slices form the next controlled maturation package.

**Package name: M1 — Foundational and Water Safety Maturation.**

This package is deliberately small and targeted. It does not add new subject breadth until this maturity asymmetry is resolved.

## Explicit exclusions

- no artificial ten-slice expansion;
- no reopening P1;
- no new Record Type;
- no mass rewrite of the 479-slice corpus;
- no Relation created for metrics or superficial topical overlap.

## Next step

Create the M1 scope, then perform the substantive audit before authoring corrections:
1. content-depth;
2. evidence independence/diversity;
3. applicability/Human View;
4. cross-domain linkage;
5. unified M1 Debt Map.

Only confirmed findings are corrected.
