# M4 Candidate Verification and Scope Lock — 2026-10-08

## Verification baseline
- M3 CLOSED CLEAN tree: `2434f3a06618543b4534ff4b12a45ad0b87e10f4`
- Current main before this scope-lock commit: `19508a501d01caa446a3e5fced520277bc789ffa`
- Baseline: 479 vertical slices / 4655 Records / 19 Record types.
- Record count is a screening signal, not a promotion quota.

## Verification method
Each candidate was checked for:
1. claims and substantive coverage;
2. source and Evidence Use structure;
3. scope/context boundaries;
4. existing cross-domain role;
5. Human View/adversarial risk;
6. evidence independence and maturation history.

## Results

### 1. infrastructure-basics — INCLUDE
- Three foundational claims cover infrastructure as a societal functional system, major infrastructure classes, and interdependence between systems.
- Source: NIST Infrastructure; all three claims point to the same source and Evidence Use records explicitly bind claim to source.
- Scope explicitly limits the slice to basic education and excludes engineering/project assessment.
- Cross-domain role is high: infrastructure is a dependency hub for water, energy, transport, health, housing and resilience.
- Human View risk: high because readers may mistake foundational statements for site-specific engineering guidance.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation rather than exclusion.
- Decision: substantive maturation target.

### 2. construction-basics — INCLUDE
- Three claims cover building-science interaction, dependence on materials/joints/load/use conditions, and the boundary against replacing calculations, codes, or qualified review.
- Source: NIST Building Science; Evidence Use binds the claims to that source.
- Scope contains an explicit professional-safety boundary.
- Cross-domain role is high across shelter, buildings, infrastructure and resilience.
- Human View risk: high because construction guidance can be operationalized beyond the educational scope.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation.
- Decision: substantive maturation target.

### 3. building-science-basics — INCLUDE
- Three claims cover building-system interactions with people/materials/energy/moisture/environment, heat-air-moisture flows, and interaction among enclosure, mechanical systems, occupancy and climate.
- Source: NIST Building Science; Evidence Use is structurally linked to that source.
- Scope limits the slice to foundational concepts and excludes specialized analysis.
- Cross-domain role is high for construction, shelter, energy, moisture, habitability and environmental conditions.
- Human View risk: medium-high because simplified building-performance claims can be over-applied to specific buildings.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation.
- Decision: substantive maturation target.

### 4. agricultural-engineering-basics — INCLUDE
- Three claims cover engineering principles in agriculture/resource management, machinery/irrigation/drainage/storage/processing, and dependence on crop/soil/water/climate/energy/labor conditions.
- Source: FAO land and water management; Evidence Use is structurally linked to that source.
- Scope limits the slice to foundational concepts and excludes specialized analysis.
- Cross-domain role is high for agriculture, water, machinery, energy, food continuity and infrastructure.
- Human View risk: high because users may turn general engineering concepts into field-specific operating instructions.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation.
- Decision: substantive maturation target.

### 5. food-safety-basics — EXCLUDE FROM M4
- This slice is materially more mature than the canonical 9-record candidates (12 records) and contains multiple evidence tracks.
- It already passed prior P2 maturation/correction and evidence-independence work.
- Re-selecting it would duplicate completed maturation rather than address an unresolved M4 asymmetry.
- Decision: retain as protected prior-maturation result; do not reopen in M4.

### 6. health-systems-basics — INCLUDE
- Three claims cover the health-system definition, major system functions, and interaction with context.
- Source: WHO Health systems; Evidence Use is structurally linked to that source.
- Scope limits the slice to foundational concepts and excludes specialized analysis.
- Cross-domain role is high for public health, health services, workforce, information, medicines, financing and governance.
- Human View risk: high because general system descriptions can be mistaken for medical, policy, or operational recommendations.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation.
- Decision: substantive maturation target.

### 7. cybersecurity-basics — INCLUDE
- Three claims cover cybersecurity risk, confidentiality/integrity/availability, and risk identification/evaluation/treatment.
- Source: NIST Cybersecurity Framework; Evidence Use is structurally linked to that source.
- Scope states that the slice is educational and not exhaustive.
- Cross-domain role is high because cybersecurity affects information, infrastructure, health, governance and continuity systems.
- Human View risk: medium-high because defensive concepts can be misunderstood as complete security guidance.
- Evidence independence: weak at baseline (single source); suitable for M4 maturation.
- Decision: substantive maturation target.

## M4 locked scope
Six slices are authorized for M4 maturation:
1. infrastructure-basics
2. construction-basics
3. building-science-basics
4. agricultural-engineering-basics
5. health-systems-basics
6. cybersecurity-basics

food-safety-basics is explicitly excluded because its prior maturation is already established.

## Scope boundary
This lock authorizes audit work only. It does not authorize new Records, Sources, Evidence Use, or Relations by itself. Any additions must arise from substantive audit findings and pass the normal evidence, Human View, relation, debt-map, regression, and CI gates.

## M4 sequence
Scope lock → substantive audit → evidence independence → Human View/adversarial audit → Relation audit → Unified Debt Map → controlled correction → re-audit → documentation/coverage/regressions → exact-head 3/3 CI → CLEAN checkpoint.
