# M2 CROSS-DOMAIN RELATION AUDIT — 2026-10-08

## Baseline

- M2 scope lock: `8e6e887e186eab40f60e8d0b2107397a7b6a3397`
- Substantive audit: `6ff368342dc6b62d2f727d5389e57c38176a0224`
- Evidence audit: `265f817825814d5921c86ef00ec096778e516401`
- Human View audit: `4e3e29b1536d1497222a0d3f6e57aaac54db0a1a`

## Audit rule

A Relation is justified only when it expresses a reusable semantic dependency between Claims, not merely topical similarity.

The audit checked the existing cross-slice linkage inventory and evaluated whether the six M2 slices have material dependencies that are currently absent from the linkage layer.

## Findings

### R1 — measurement uncertainty ↔ measurement science / calibration — MATERIAL

Measurement uncertainty is a direct foundational dependency for interpreting measurement processes and calibration results.

Current linkage inventory contains related measurement/calibration relations, but the existing relation participants do not use the new `measurement-uncertainty-basics` Claims.

**Finding:** a new relation is materially justified if it links a specific measurement-uncertainty Claim to the existing measurement-science or calibration foundation.

### R2 — statistics ↔ research/statistical inference — MATERIAL

The current linkage inventory already connects research methods with statistical inference, but `statistics-basics` itself is not represented in that relation.

The M2 slice explicitly states that study design affects conclusions, making the relationship to research methods/statistical inference semantically reusable.

**Finding:** a new relation is materially justified, provided it connects a concrete M2 Claim to the existing research/statistical-inference foundation rather than duplicating the existing relation.

### R3 — risk management ↔ risk analysis / systems thinking — MATERIAL

Risk management and risk analysis are adjacent but distinct layers: management frames objectives, context and treatment; analysis supplies techniques for understanding risk.

The existing linkage inventory contains risk-analysis/systems-thinking material but does not directly anchor `risk-management-basics`.

**Finding:** a direct relation is materially justified if it expresses this dependency without conflating ISO 31000 management guidance with IEC 31010 analysis techniques.

### R4 — agriculture ↔ soil / water / food systems — MATERIAL

The agriculture Claims explicitly identify soil, water, biological factors, climate and management as interacting determinants.

Existing corpus domains include soil, water-resource and food-system foundations.

**Finding:** at least one direct relation is materially justified, but only the most reusable dependency should be added. Do not create multiple Relations merely because several neighboring domains exist.

### R5 — energy security ↔ energy systems / infrastructure resilience — MATERIAL

Energy security is explicitly framed in terms of supply disruption, infrastructure and regional context.

Existing corpus domains include energy systems and infrastructure resilience.

**Finding:** a direct relation is materially justified where a Claim establishes the dependency between energy-security assessment and system resilience/infrastructure context.

### R6 — geographic coordinates ↔ geodesy / surveying / GIS — MATERIAL

The geographic-coordinate slice explicitly states that coordinate-system choice and precision depend on the task.

Existing geodesy/surveying and GIS foundations provide the natural technical continuation.

**Finding:** one direct relation to the geodesy/surveying foundation is materially justified. GIS may remain a downstream domain rather than requiring a second Relation.

## Anti-duplication check

No existing relation with the target slice names was found in the cross-slice linkage filename inventory. Existing neighboring relations are therefore not being duplicated by name.

Before authoring any Relation record, the exact participant Claims must be checked against the current tree and the resulting Relation must receive dedicated regression coverage.

## Result

**CROSS-DOMAIN RELATION AUDIT: 6 material candidate dependencies confirmed.**

No Relation has been authored by this audit.

The next controlled step is the **unified M2 Debt Map**, combining:
- 5 evidence-independence debts;
- 1 Gap Map synchronization debt;
- 6 material Relation candidates;
- 0 Human View debts;
- 0 substantive Claim corrections.
