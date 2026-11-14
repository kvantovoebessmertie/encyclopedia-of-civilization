# M13 Batch 13 — source-fit triage (rows 606–608): geometry basics

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional triage; all three Claims have source-scope/pinpoint gaps**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional audit notes, not finalized ledger scores. No canonical JSON changed.

## Source trail

All three Claims cite `SRC-GEOMETRY_BASICS`, whose stored locator is `https://openstax.org/books/precalculus-2e/pages/10-introduction`. The current canonical OpenStax page is titled *Introduction to Analytic Geometry* and is located at `https://openstax.org/books/precalculus-2e/pages/10-introduction-to-analytic-geometry`. Its chapter outline covers ellipses, hyperbolas, parabolas, rotation of axes, and conic sections in polar coordinates. This is a relevant mathematical source in a broad sense, but its visible scope does not directly substantiate the three introductory claims about points/lines/angles/shapes, perimeter/area, or dependence on definitions and units. The exact stored locator should be normalized after source-identity reconciliation, and each Claim needs a claim-specific passage. The Evidence Use records contain only boilerplate and no pinpoint.

## 1. `CLM-GEOMETRY_BASICS-A` — **D1 / E0 / B1**

**Claim:** “Геометрические объекты описываются через точки, линии, углы и фигуры.”

**Assessment:** This is a broad introductory statement, but it does not explain how the listed primitives relate or distinguish geometric objects (D1). The linked analytic-geometry chapter introduction discusses conic sections and their equations, not the asserted general taxonomy; no pinpoint is supplied (E0). “Геометрические объекты” and the list are broad and undefined (B1).

**Disposition:** Keep provisional; replace with a directly relevant introductory geometry source and exact section, or narrow the Claim to what the OpenStax chapter actually covers.

## 2. `CLM-GEOMETRY_BASICS-B` — **D2 / E0 / B2**

**Claim:** “Периметр характеризует длину границы плоской фигуры, а площадь — размер её области.”

**Assessment:** The Claim gives a useful high-level distinction between boundary length and area (D2), with a reasonable conceptual boundary (B2). The cited source's chapter scope is analytic geometry/conic sections and does not directly support these general definitions; the Evidence Use has no pinpoint (E0).

**Disposition:** Replace or supplement the source with a geometry reference that explicitly defines perimeter and area, then record the exact passage. Do not treat the existing link as adequate evidence.

## 3. `CLM-GEOMETRY_BASICS-C` — **D1 / E0 / B1**

**Claim:** “Измерительные свойства фигуры зависят от выбранных определений и единиц.”

**Assessment:** The statement is too compressed to make the intended dependency clear: it does not distinguish definitions, measurement conventions, and units (D1). The linked chapter introduction does not establish this general claim and no pinpoint is present (E0). The phrase “измерительные свойства” is ambiguous without a named property or context (B1).

**Disposition:** Clarify the intended mathematical meaning and cite a source explicitly explaining the relevant measurement/property and unit convention.

## Batch accounting

- Individual Claims triaged in this checkpoint: **3**.
- New provisional D/E/B assessments recorded in this checkpoint: **3**.
- Source identity/URL reconciliation: **open**; the stored slug differs from the current canonical page slug.
- Exact source pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
