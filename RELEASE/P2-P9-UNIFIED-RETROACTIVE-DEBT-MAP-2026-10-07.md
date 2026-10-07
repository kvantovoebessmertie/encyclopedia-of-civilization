# P2–P9 UNIFIED RETROACTIVE DEBT MAP — 2026-10-07

## Status

**AUDIT PHASE — CONFIRMED DEBT REGISTER**

This map converts the P2–P9 Maturity Gap Scan into confirmed findings. Historical waves are not reopened wholesale.

## Confirmed debt

### MG-01 — Evidence Use material-boundary specificity

**Status:** CLOSED — RE-AUDITED
**Closure HEAD:** `8631bfa7968363468f18e7f0ce58acf692b66989`
**Technical gate:** Reference #1838 + Release Conformance Gate #2127 + Offline Edition #1307 = **3/3 GREEN**
**Correction scope:** 35 Evidence Use records corrected in `b32668e369be0d85b7e841e991505958144e83e7`.

**Severity:** MEDIUM  
**Class:** evidence traceability / semantic material boundary  
**Scope:** P2–P9 historical target clusters, prioritized verification

The retroactive spot-check confirmed that some legacy Evidence Use records use generic material descriptions such as:

> «Источник используется в пределах заявленного материала.»

This wording identifies neither the specific material supporting the linked Claim nor the evidentiary boundary. It is weaker than the mandatory semantic-area requirement in STANDARD/004 §4 and the reverse-traceability requirement in §17–18.

Confirmed examples inspected:
- pathology-basics: A/B/C baseline Evidence Use;
- pharmacology-information-basics: A/B/C baseline Evidence Use.

This was a real conformance debt. It did not imply that the underlying Claims were false or that the sources were invalid.

### MG-01 closure evidence

A record-level re-audit on the current `main` confirmed that the corrected Evidence Use material boundaries are claim-specific and bounded. The previously identified generic material wording is absent from the current tree, and the inspected legacy examples retain their Claim/Source identities after correction. The current HEAD passes the independent three-contour technical gate: Reference #1838, Release Conformance Gate #2127, and Offline Edition #1307 — all GREEN.

MG-01 is therefore CLOSED. No further P2–P9 rewrite is authorized under this finding.

### MG-02 — Human View consistency

**Status:** NOT YET CONFIRMED AS CONTENT DEBT.

Historical P2–P9 Human View audits are strong. A targeted adversarial consistency pass is still required before either closing this item or opening a correction.

### MG-03 — Relation baseline reconciliation

**Status:** CLOSED — NO FINDING.

Current tree independently reconciles:
- global Relation records: **38**;
- dedicated Cross-Slice Linkage Relation records: **37**;
- valid non-Cross-Slice Relation: emergency-water-storage-state/REL-CONTAINER-WATER-STORAGE.json.

No Relation count defect is present.

## Explicit non-findings

- No evidence currently supports reopening P2–P9 wholesale.
- Historical single-source slices are not automatically defective.
- Historical lack of a technical locator is not defective when semantic material is explicit.
- Existing justified Relations are not to be expanded merely to improve counts.
- P9's already mature Evidence Use records are not assumed defective without record-level confirmation.
- No claim content rewrite is authorized merely because an Evidence Use description is weak.

## Correction policy

For MG-01:
1. identify all affected P2–P9 Evidence Use records by record-level scan;
2. rewrite only descriptions whose material is genuinely too generic;
3. preserve Claim/Source identity, evidence role and historical provenance;
4. make each description claim-specific and bounded;
5. run dedicated regression before closure.

For MG-02:
1. run P10 adversarial scenarios against high-consequence P2–P9 slices;
2. open a correction only for an observed interpretation failure.

## Gate

MG-01 is CLOSED after record-level correction, re-audit, and 3/3 GREEN technical validation on the closure HEAD.

MG-02 remains an audit item, not an open defect.

MG-03 is CLOSED.

No P11 start until MG-02 Human View verification is closed and the resulting corrected tree passes full technical validation and a CLEAN checkpoint.
