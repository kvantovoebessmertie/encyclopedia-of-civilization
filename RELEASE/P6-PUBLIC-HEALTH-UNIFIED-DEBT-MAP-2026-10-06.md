# P6 Public Health & Health Resilience — Unified Debt Map — 2026-10-06

## Baseline

- P6 Gap Map commit: `4bda4e7021fdba3188ede5989ea03cbb90f34512`
- P5 CLEAN checkpoint: `b0da033bc3e566c5a2259598e660c4abcfef63fc`
- Corpus: 478 slices / 4390 Records / 19 types.

## Findings

### P6-EVIDENCE-001 — public-health-basics
Current claims are represented from one WHO source. Add genuinely independent institutional evidence and preserve the distinction between population-level public health and individualized care.

### P6-EVIDENCE-002 — public-health-surveillance-basics
Current claims are represented from one WHO emergency-surveillance source. Add independent CDC surveillance evidence and make signal interpretation/current-authority boundaries explicit.

### P6-EVIDENCE-003 — epidemiology-basics
Current claims are represented from one CDC source, including one generic introductory statement. Add independent WHO epidemiological evidence and strengthen the distinction between description, association and causal inference.

### P6-EVIDENCE-004 — environmental-health-basics
Current claims are represented from one WHO environmental-health source. Add independent EPA exposure/health evidence and make exposure-pathway and uncertainty boundaries explicit.

### P6-EVIDENCE-005 — disaster-behavioral-health-basics
Current claims are represented from one SAMHSA source. Add independent WHO emergency mental-health evidence and preserve the boundary between descriptive information and individualized mental-health care.

### P6-CONTENT-006 — target-cluster depth
The five slices follow the canonical 9-record profile but are mostly introductory. Where warranted, add source-supported mechanism, applicability, uncertainty, limitation or failure-boundary claims rather than expanding for record-count symmetry.

### P6-HUMAN-007 — population-health interpretation
The cluster needs an explicit adversarial pass against common misreadings: surveillance signal as diagnosis, population association as individual causation, environmental exposure as deterministic disease prediction, and disaster mental-health information as individualized treatment advice.

## Scope rules

- No unsupported medical thresholds, dosages, exposure limits or emergency commands.
- No individualized diagnosis or treatment.
- No artificial Relations.
- No reopening P1–P5 absent verified regression.
- Every accepted correction must synchronize README, regression contracts, coverage and audit registries.

## Closure requirement

All findings above must be CLOSED by one correction pass, followed by a complete substantive re-audit. No P6 CLEAN declaration is valid before substantive findings and Human View findings are zero and the full 3/3 technical gate passes.
