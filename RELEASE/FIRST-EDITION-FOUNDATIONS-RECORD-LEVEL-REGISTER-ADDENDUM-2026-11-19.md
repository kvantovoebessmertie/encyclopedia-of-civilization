# First Edition Foundations — Record-Level Candidate Register Addendum 2026-11-19

Status: **3 additional Part II slices screened; 27/27 records inspected; all 3 slices HOLD**  
Workstream: PR #22, Work Package 1 — first-edition candidate selection  
Branch: mvp-public-contribution-design-2026-10-11

## Scope and duplicate control

This addendum records the next targeted screens after the Part I coverage reconciliation. It does not reopen M1/M2 or prior candidate reviews.

| Part II family | Slice | Records | Disposition |
|---|---|---:|---|
| Mathematics and measurement | units-and-measurement | 9 | HOLD |
| Mathematics and measurement | geometry-basics | 9 | HOLD |
| Mathematics and measurement | calculus-basics | 9 | HOLD |
| **Total** | **3 slices** | **27** | **3 HOLD** |

Record types: 9 Claims, 9 Evidence Use, 3 Sources, 3 Context, 3 Scope.

## Findings

### units-and-measurement

Audit: DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md

- Claim B is directly supported by the current NIST SI Units source.
- Claim A needs a measurement-definition/procedure source (VIM 2.1).
- Claim C needs direct measurement-result/uncertainty evidence (VIM 2.9 and NIST measurement uncertainty).
- All existing EUs point only to NIST SI Units and lack claim-specific pinpoints.
- Decision: HOLD pending authorized additional Source/EU records and precise locators.

### geometry-basics

Audit: DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md

- The current OpenStax Precalculus 2e source is an analytic-geometry/conic-sections chapter, not a direct general-geometry source for points/lines/angles or perimeter/area.
- Claim C is overly broad and needs a more precise proposition or explicit context.
- The stored source URL is not the current canonical Chapter 10 URL.
- EUs lack pinpoints; Context/Scope target A only.
- Decision: HOLD pending a better-fitting general-geometry source and precise evidence mapping; do not make a cosmetic URL-only correction.

### calculus-basics

Audit: DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md

- Claims A/B/C have direct OpenStax Calculus Volume 1 section support: §§2.2, 3.1 and 5.2 respectively.
- EUs still use generic descriptions and require those exact section pinpoints.
- Context/Scope target Claim A only.
- OpenStax CC BY-NC-SA 4.0, attribution, noncommercial and ShareAlike terms, plus the stated restriction on LLM ingestion/training, require explicit rights handling for the planned distribution model.
- Decision: HOLD; strongest direct-source candidate in this batch, but not release-cleared.

## Duplicate-control record

Not re-audited:
- ratios-and-percentages and probability-basics — prior M1 substantive/evidence-independence/Human View work exists.
- algebra-basics — prior M2 substantive review exists.
- statistics-basics and measurement-uncertainty-basics — prior first-edition candidate screens exist.

No historical assessment was replaced and no M13 batch was started.

## Work-package boundary

These screens are evidence for candidate selection only. They do not authorize canonical changes, publication or promotion to INCLUDE. Any future correction to Claim/Evidence Use/Source must be separately authorized, versioned and tested. No canonical content record, Relation, allowlist, preview, publication status or main-branch content was changed. PR #22 remains Draft.
