# M5 Relation Audit — 2026-10-09

## Decision
**PASS.** Existing Relations remain valid. One new Relation was added only after claim-level review because the two endpoints express a direct critical-infrastructure dependency.

## Preserved Relations
- `REL-CROSS-SETTLEMENT-ENERGY`: settlement-system claim ↔ `energy-systems-basics` Claim A. Claim A's identifier and core system framing remain intact.
- `REL-CROSS-SETTLEMENT-TRANSPORTATION`: settlement-system claim ↔ `transportation-basics` Claim A. Claim A's identifier and movement-system framing remain intact.
- `REL-CROSS-WATER-QUALITY-TREATMENT`: water-quality Claim A ↔ water-treatment Claim B. The treatment Claim's identifier and raw-water/contaminant dependence remain intact.
- `REL-CROSS-SANITATION-WASTEWATER` and `REL-CROSS-SANITATION-HYGIENE`: existing sanitation-related endpoints remain intact; the new service-chain Claim D does not invalidate or duplicate these links.

## M5 Relation added
- `REL-CROSS-TELECOM-ENERGY-RESILIENCE` connects `CLM-M5-TELECOM-CONTINUITY-D` with `CLM-M5-ENERGY-GRID-RESILIENCE-D`.
- Justification: the telecommunications claim addresses continuity dependencies, while the energy claim addresses grid resilience; CISA's communications-sector guidance describes reciprocal dependencies between communications and energy systems. This is a claim-level dependency, not merely topical adjacency.
- The Relation uses the existing `CTX-CROSS-SLICE-LINKAGE` frame, has two Claim participants, and does not replace either Claim's direct Evidence Use.
- The dedicated cross-slice regression asserts the new Relation ID, both endpoints and the explicit frame.

## Candidate Relation decisions
- Materials science ↔ manufacturing: conceptually adjacent, but no additional Relation was added; the current claims do not require a more specific dependency for correctness.
- Transportation ↔ supply chains: the World Bank transport claim and OECD visibility claim are complementary, but topical relevance alone is insufficient.
- Water treatment/sanitation/environmental engineering: shared water/wastewater themes do not justify duplicate links beyond the existing sanitation/wastewater and water-quality/treatment Relations.

## Checks
- Existing Relation IDs and endpoints remain intact.
- Cross-slice linkage contains 57 Relation records plus its shared Context; total corpus Relation count is 64.
- No Relation is used as a substitute for direct source evidence.
- No duplicate Relation was added.

## Decision
**Relation audit PASS.** Exact-head Reference, Release Gate, Offline and final post-CI re-audit remain mandatory before M5 CLEAN.
