# R14 Substantive Audit — 2026-10-04

Status: **AUDIT COMPLETE — NON-BLOCKING CONTENT DEBT**

Target: 398 vertical slices / 3557 records / 19 Record types.
Wave: R14 controlled ten-slice expansion.

## Pass 1 — Structure and epistemic boundaries

**PASS.** All ten R14 slices use the intended 9-record contract:
1 Source + 3 Claim + 3 Evidence Use + Context + Scope.
Each Claim has source-based provenance; each Evidence Use links one Claim to the slice Source with role `supports`. No new Record type was introduced.

## Pass 2 — Source / Claim alignment

**PASS.** Manual review of all 30 R14 Claims found them appropriately scoped as basic documented facts. The claims are definition-, mechanism-, limitation-, or context-oriented and avoid unsupported quantitative precision or universal prescriptions.

Examples of boundary-preserving formulations include:
- insurance does not remove risk and coverage depends on contract conditions;
- water-treatment method selection depends on source water and target contaminants;
- medical-device regulation varies by jurisdiction;
- public-data availability does not guarantee analytical fitness;
- traceability identifiers alone do not establish complete or truthful chain records.

The linked source identities are authoritative/public domain sources appropriate to the subject areas.

## Pass 3 — Content depth

**PASS WITH BOUNDARIES.** Each slice establishes a useful conceptual minimum rather than a complete domain treatment. The three-claim pattern generally covers definition plus mechanism/context plus limitation. This is sufficient for the controlled introductory slice contract, but not for operational or professional use.

## Pass 4 — Cross-domain semantic audit

**PASS.** No claim was found to silently generalize across jurisdictions, sectors, or use contexts. Several R14 topics naturally connect to existing domains (risk, energy, water, food, health, governance, economics), but the new records do not merge Claims across domains or create unsupported causal links.

No architectural change is required.

## Pass 5 — Evidence diversity

**PASS WITH NON-BLOCKING DEBT.** The wave uses multiple authoritative source families across ten domains: OECD, ILO, IEA, WHO, FAO, UN Statistics Division, World Bank, and GS1. However, each individual slice currently relies on one primary source. Independent second-source triangulation is therefore deferred for higher-consequence reuse.

## Pass 6 — Human View / adversarial applicability

**PASS WITH NON-BLOCKING DEBT.** The records are understandable without reading the architecture, and Scope/Context boundaries reduce over-interpretation. Adversarial review found no obvious invitation to treat the educational claims as universal professional instructions.

Carried-forward editorial debt:
- domain-specific warning text could be stronger for water treatment and medical-device material;
- insurance, disaster-financing, social-protection and regulatory topics would benefit from jurisdiction-specific examples in future depth passes;
- operational examples and failure modes are intentionally absent from this introductory wave.

## Findings

Blocking findings: **0**
Architectural changes: **0**
New deterministic validator classes: **0**
Editorial corrections required now: **0**
Current CI/preflight defects after correction: **0**

## Disposition

R14 is substantively acceptable for the controlled-wave contract and ready for the final full-regression / release-gate sequence. This document alone does **not** declare R14 CLEAN. The R14 checkpoint may be declared only after the audit commit itself passes the complete Reference, Release Gate, and Offline contours.

