# First Edition — Cross-Slice Relation Semantic Review — Batch 5

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `53aa8006f17e82122724c7d4831bf29a15fde07a`

## Scope and method

Eight additional unreviewed Relation records were fetched from canonical JSON. Both participant Claims were fetched from their owning slices and checked for exact ID, version, and type. The participant Claim provenance Source records were also fetched and checked. Relation provenance, role labels, direction, and frame references were inspected.

This is a semantic navigation review, not an evidence or publication approval. Relations do not prove their participant Claims and do not establish causation unless separately supported. No canonical JSON, allowlist, or publication decision was changed; all Claims remain HOLD.

## Exact verification

- 8/8 Relation records: exact ID, version, and `record_type=relation`.
- 16/16 participant Claims: exact ID, version, and `record_type=claim`.
- 16 participant Claim provenance Source references fetched; 15 unique Source records because `SRC-MEASUREMENT_SCIENCE_BASICS@1` is shared by two Relations.
- All fetched Source records match exact ID, version, and `record_type=source`.
- For seven Relations, both Relation `created_from` entries are the exact Source records used by their participant Claims.
- **Provenance-shape exception:** `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2` uses its two participant Claim IDs in Relation `provenance.created_from`, rather than the two Source IDs used by the Claims. The participant references themselves are exact, but the provenance convention is inconsistent with the other seven Relations and must be normalized or explicitly permitted by the applicable schema before release use. No canonical correction was made.
- 8/8 Relations reference `CTX-CROSS-SLICE-LINKAGE@1`; the shared frame applicability ambiguity remains open.

## Relation-by-relation semantic findings

| Relation/version | Exact participant pair | Semantic assessment | Release-use disposition |
|---|---|---|---|
| `REL-CROSS-M2-STATISTICS-RESEARCH@1` | Statistics Claim C; Research Methods Claim B | Statistics Claim C explicitly connects experimental design and data analysis, but the selected research-methods Claim concerns reproducibility and repeatability. These are related methodological concerns, but the second endpoint does not directly substantiate the named research-design link. | HOLD — endpoint mismatch; select a research-design Claim or narrow the relation description before reconsideration. |
| `REL-CROSS-MANUFACTURING-HUMAN-FACTORS@1` | Manufacturing Processes Claim B; Human Factors Claim A | Manufacturing is described as a sequence of processes with controls and result requirements; human factors examines interactions between people, systems, equipment, environment, and organization. The relationship is direct at the work-system level. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; do not infer a specific ergonomic or safety outcome; retain HOLD for publication eligibility. |
| `REL-CROSS-MEASUREMENT-CALIBRATION@1` | Measurement Science Claim A; Calibration Claim A | Metrology concerns measurement and its applications; calibration relates instrument indications to corresponding measured values. This is a direct foundational link. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-MECHANICAL-METALLURGY@1` | Mechanical Engineering Claim A; Metallurgy Claim A | Mechanical engineering explicitly applies materials science; metallurgy studies metals, alloys, their structure, properties, and processing. The disciplinary interface is clear. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; do not imply that all mechanical engineering is metallurgy; retain HOLD for publication eligibility. |
| `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2` | Migration and Mobility Claim C@2; Labor Economics Claim C@1 | Migration Claim C is about definitions, time periods, geography, and measuring migration flows/stocks. Labor Claim C lists labor-market indicators but does not connect them to migration. The broad relationship is plausible, but the selected pair does not establish a migration/labor measurement link. The Relation also has the provenance-shape exception above. | HOLD — semantic specificity and provenance convention both require resolution. |
| `REL-CROSS-PLANTPATH-ENTOMOLOGY@1` | Plant Pathology Claim A; Entomology Claim A | One Claim defines plant pathology and the other defines entomology. Insects can be relevant to plant health, but neither selected statement addresses pests, vectors, transmission, or plant–insect interactions. Shared domain adjacency alone is insufficient. | HOLD — no specific relationship is stated by the selected endpoints. |
| `REL-CROSS-POLITICAL-ECONOMY-TAXATION@2` | Political Economy Claim B@2; Taxation Claim B@2 | Political Economy Claim B describes how interests and institutions influence economic-policy choices; Taxation Claim B describes tax revenue and effects on work, investment, and innovation incentives. This is a coherent institutional-policy interface. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; do not imply a particular tax effect without jurisdictional and empirical evidence; retain HOLD for publication eligibility. |
| `REL-CROSS-QUANTUM-MEASUREMENT@1` | Quantum Mechanics Claim A; Measurement Science Claim B | The quantum Claim describes quantum-scale systems and probabilistic effects; the metrology Claim says measurement results need information for interpretation and comparison. The latter is generic and does not address quantum measurement, measurement disturbance, observables, or quantum-specific uncertainty. | HOLD — too generic for the specific quantum-measurement link named. |

## Cross-cutting frame limitation

The eight Relations reference `CTX-CROSS-SLICE-LINKAGE@1`, whose `target_ref` names `REL-CROSS-WATER-CHEMICAL@1` specifically. The shared frame's applicability to all other Relations is not established by the matching frame ID/version alone. Do not treat this target as a wildcard. Schema and Context-scope resolution remains a release blocker.

## Result

- Structurally exact: 8 Relations and 16 participant Claims.
- Claim provenance Sources: 16 references, 15 unique exact-version Source records.
- Semantic dispositions: 4 contextual-navigation candidates; 4 HOLD for release use.
- One Relation provenance-shape inconsistency identified: `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2`.
- No canonical records changed.
- No Claim or Relation promoted to INCLUDE.
- No Relation approved for release.

## Remaining work

Continue the remaining unreviewed Relations. Track provenance conformance separately from participant identity and semantic validity. Resolve both the migration Relation provenance exception and shared Context target-scope ambiguity before any affected Relation can be considered release-eligible.
