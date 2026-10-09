# M5 Relation Audit — 2026-10-09

## Decision
**PASS.** Existing Relations remain valid. No new Relation is required by the M5 claim changes, and no artificial Relation was added.

## Preserved Relations
- `REL-CROSS-SETTLEMENT-ENERGY`: settlement-system claim ↔ `energy-systems-basics` Claim A. Claim A's identifier and core system framing remain intact.
- `REL-CROSS-SETTLEMENT-TRANSPORTATION`: settlement-system claim ↔ `transportation-basics` Claim A. Claim A's identifier and movement-system framing remain intact.
- `REL-CROSS-WATER-QUALITY-TREATMENT`: water-quality Claim A ↔ water-treatment Claim B. The treatment Claim's identifier and raw-water/contaminant dependence remain intact.
- `REL-CROSS-SANITATION-WASTEWATER` and `REL-CROSS-SANITATION-HYGIENE`: existing sanitation-related endpoints remain intact; the new service-chain Claim D does not invalidate or duplicate these links.

## Candidate Relation review
- Materials science ↔ manufacturing: conceptually adjacent, but the new claims do not establish a sufficiently specific dependency that requires a new Relation for correctness.
- Energy ↔ telecommunications: infrastructure interdependence is discussed at a high level, but the new Claim does not assert a precise claim-to-claim dependency requiring a new Relation. A future Relation would need a specific endpoint and useful navigation/reasoning benefit.
- Transportation ↔ supply chains: the World Bank transport claim and OECD visibility claim are complementary, but topical relevance alone is not sufficient for a Relation.
- Water treatment/sanitation/environmental engineering: shared water/wastewater themes are not used to create duplicate links. Existing relations are preserved; any future Relation must identify a precise Claim-level dependency and correct endpoints.

## Checks
- No M5 Relation record was added.
- Existing Relation IDs and endpoints were not rewritten by M5.
- Relation count remains 63.
- No Relation is used as a substitute for direct source evidence.

## Decision
**Relation audit PASS.** Exact-head Reference, Release Gate, Offline and final post-CI re-audit remain mandatory before M5 CLEAN.
