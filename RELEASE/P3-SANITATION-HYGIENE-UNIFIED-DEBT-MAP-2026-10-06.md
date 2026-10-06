# P3 Sanitation & Emergency Hygiene — Unified Debt Map — 2026-10-06

## Audit baseline

- Audit commit: `9546d98259342c83180afff8aad06b9f23a0a14b`
- P3 cluster: sanitation-basics; emergency-hand-hygiene; emergency-waste-sanitation; disaster-response-basics; disaster-response-logistics-basics.
- Baseline corpus: 478 vertical slices / 4370 Records / 19 Record types.
- Rule: complete the finding map before correction; all open findings are corrected together in one pass.

## Findings

### P3-SOURCE-001 — OPEN FOR CORRECTION
**Slice:** disaster-response-basics
**Class:** evidence independence / duplicate source provenance

Two Source records represent the same UNDRR “Definition: Response” URL:
- `SRC-DISASTER_RESPONSE_BASICS`
- `SRC-DISASTER_RESPONSE_UNDRR`

This is not independent triangulation. The canonical UNDRR source should be represented once, with all relevant UNDRR-backed Claims/Evidence Use pointing to that canonical source. The FEMA source remains the genuinely independent second institutional line.

**Correction:** consolidate the duplicate UNDRR source representation; repoint affected provenance/evidence; synchronize README and audit metadata.

### P3-EVIDENCE-002 — OPEN FOR CORRECTION
**Slice:** sanitation-basics
**Class:** evidence independence / maturity depth

The slice contains three foundational sanitation Claims supported only by one source. For a high-consequence sanitation-resilience anchor, the current general statements would benefit from one genuinely independent institutional evidence line, especially for the health-risk and sanitation-chain/planning boundary. WHO emergency/WASH and sanitation-safety material provides an independent institutional line without requiring unsupported procedural expansion.

**Correction:** add only source/evidence that materially triangulates the existing Claims; do not inflate record count or add unsupported operational detail.

### P3-EVIDENCE-003 — OPEN FOR CORRECTION
**Slice:** disaster-response-logistics-basics
**Class:** evidence independence / high-consequence operational boundary

The slice has three broad disaster-logistics Claims backed by a single OCHA landing-page source. Because logistics is an operational emergency domain, independent triangulation is warranted. Current OCHA material explicitly addresses disaster logistics and humanitarian coordination.

**Correction:** add a directly relevant independent institutional source/evidence line supporting an existing logistics Claim; preserve the general, context-bounded nature of the slice.

### P3-DOC-004 — OPEN FOR CORRECTION
**Slices:** emergency-hand-hygiene; disaster-response-basics
**Class:** documentation drift

- emergency-hand-hygiene README says 1 Source / 1 Evidence Use, while the current records contain 2 Sources and 2 Evidence Use records.
- disaster-response-basics README describes a single UNDRR source / canonical profile while the current slice contains the FEMA independent line and the duplicate UNDRR source representation.

**Correction:** synchronize READMEs with the corrected record topology and evidence model.

## No-finding checks

### P3-FLOWS-005 — NO FINDING
Emergency waste currently has CDC + WHO evidence with distinct claim roles. No evidence-padding or duplicate URL found in the reviewed source/evidence paths.

### P3-HUMAN-006 — NO FINDING
Reviewed Human View boundaries do not expose unsupported concentrations, times, dosages, or universal procedural guarantees. Emergency hand hygiene remains contextual; waste handling remains bounded to risk reduction rather than unsafe technical instructions; logistics remains descriptive.

### P3-LINK-007 — NO FINDING
Existing cross-domain Relations materially connect sanitation ↔ hygiene and flooded septic systems ↔ flood cleanup/sanitation. No additional Relation is required merely for metric expansion.

### P3-DEPTH-008 — NO FINDING
sanitation-basics and disaster-response-logistics-basics remain intentionally general rather than artificially expanded. Their open evidence findings are about independent triangulation, not a requirement to turn them into procedural manuals.

## Correction rule

All four OPEN findings must be corrected in one pass. After correction:
1. repeat full P3 substantive audit;
2. only if zero findings remain, run Reference + Release Gate + Offline;
3. create dedicated P3 CLEAN checkpoint;
4. independently run 3/3 CI on that checkpoint.

P3 is not CLEAN until step 4 is GREEN.
