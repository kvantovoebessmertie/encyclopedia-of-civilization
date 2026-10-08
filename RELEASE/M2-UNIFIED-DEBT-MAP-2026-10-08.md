# M2 UNIFIED DEBT MAP — 2026-10-08

## Status

**M2 — OPEN**

## Baseline

M2 scope lock: `9277308cd73673492ea4d2674f9b90cb0a7c7633`
Substantive audit: `4725f1beacf65c421cde01dcc06f6c68f560e4de`

## Confirmed debts

| ID | Slice | Debt | Priority | Required closure |
|---|---|---|---|---|
| M2-01 | air-quality-basics | single evidence track + AQI/jurisdiction boundary | P1 | independent WHO track + explicit source-role boundary |
| M2-02 | agriculture-basics | single evidence track + applicability boundary | P1 | independent agricultural evidence + bounded wording |
| M2-03 | anatomy-basics | single evidence track + descriptive/clinical boundary | P1 | independent anatomy evidence + Human View boundary |
| M2-04 | antimicrobial-resistance-basics | single evidence track + individual-treatment boundary | P0 | independent public-health evidence + explicit non-treatment boundary |
| M2-05 | acid-base-basics | pH formulation + single evidence track + model boundary | P0 | IUPAC corroboration + semantic correction |
| M2-06 | analytical-chemistry-basics | single evidence track + metrological/uncertainty boundary | P1 | IUPAC corroboration + applicability boundary |
| M2-07 | algebra-basics | single evidence track + model/interpretation boundary | P1 | independent mathematical evidence + bounded interpretation |
| M2-08 | agrifood-systems-basics | single evidence track + system/causal boundary | P1 | independent systems evidence + causal boundary |
| M2-09 | architecture-basics | self-referential Claim A + single evidence track + code boundary | P1 | substantive claim correction + independent architecture evidence |
| M2-10 | ancient-civilizations-basics | causal claim + single evidence track + evidence boundary | P1 | independent archaeology/history evidence + causal qualification |

## Global M2 debts

1. Evidence diversity: 10/10 slices have only one source track.
2. Human View: health, chemistry, architecture and historical boundaries require explicit preservation after correction.
3. Semantic precision: acid-base pH definition and ancient-civilization causal wording require direct correction, not merely another source.
4. No architectural debt identified.
5. No new Record type required.
6. No artificial Relation is justified yet.

## Closure rule

A debt is closed only when the canonical content, Evidence Use provenance, regression, documentation and audit evidence agree. A second source by itself does not close a semantic debt.
