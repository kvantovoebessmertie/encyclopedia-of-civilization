# M4 Substantive Audit — 2026-10-08

## Scope
Six locked M4 slices:
- infrastructure-basics
- construction-basics
- building-science-basics
- agricultural-engineering-basics
- health-systems-basics
- cybersecurity-basics

Excluded: food-safety-basics, because prior P2 maturation/correction and evidence-independence work already established its protected maturity.

## Baseline
Post-correction re-audit HEAD: `22dcc99c545b6f434df514e0031290a0cd2bf970`.
M3 remains protected and is not reopened.

## Pass 1 — Claims and substantive depth

### infrastructure-basics — MATURATION REQUIRED
Current claims correctly establish infrastructure as an interconnected societal system, but the slice is too shallow for its cross-domain importance.
Key gaps:
- explicit dependency/cascade examples;
- criticality and service-continuity concepts;
- redundancy, maintenance and lifecycle concepts;
- distinction between infrastructure asset, service and network/system;
- failure-mode framing without turning into site-specific engineering advice.

### construction-basics — MATURATION REQUIRED
Current claims establish interaction of materials, loads, connections and use conditions and include a good professional-review boundary.
Key gaps:
- structural vs non-structural distinction;
- foundations/site conditions;
- moisture/weather exposure and durability;
- construction sequence/quality control/inspection concepts;
- common failure-mode taxonomy at educational level;
- clearer separation of conceptual knowledge from code-specific requirements.

### building-science-basics — MATURATION REQUIRED
Current claims correctly frame heat, air, moisture, enclosure, mechanical systems, occupancy and climate as interacting factors.
Key gaps:
- explicit hygrothermal interaction and condensation risk as a concept;
- ventilation and indoor-air-quality relationship;
- thermal comfort versus energy trade-offs;
- measurement/diagnostic concepts;
- seasonal/climate context and uncertainty;
- clearer distinction between building-science concepts and building-specific assessment.

### agricultural-engineering-basics — MATURATION REQUIRED / EVIDENCE ALIGNMENT FLAG
Current claims establish the field and its major application areas.
Key gaps:
- machinery safety and maintenance boundaries;
- irrigation efficiency and drainage trade-offs;
- soil compaction/erosion implications;
- energy/water/labor trade-offs;
- basic reliability and lifecycle concepts.
Important evidence issue for the next Evidence Independence pass: the registered source is FAO Land and Water Management, while Claim B also asserts coverage of machinery, storage and processing. This requires direct source-to-claim verification before acceptance; do not assume the single FAO locator independently supports every listed subdomain.

### health-systems-basics — MATURATION REQUIRED
Current claims correctly define a health system and identify major functions.
Key gaps:
- access, continuity and referral pathways;
- workforce and supply-chain dependencies;
- information/surveillance functions;
- resilience and surge capacity;
- equity/context variation;
- explicit boundary between system-level knowledge and individual medical advice.

### cybersecurity-basics — MATURATION REQUIRED
Current claims correctly establish risk, confidentiality/integrity/availability and risk management.
Key gaps:
- authentication/access control;
- patching and configuration management;
- backups/recovery and incident response;
- threat/vulnerability distinction;
- basic defensive hygiene and operational boundaries;
- explicit statement that the slice is foundational and not a complete security program.

## Pass 2 — Context and scope
All six slices have context and scope records with the correct target references. Construction has the strongest explicit safety boundary. Infrastructure also explicitly excludes engineering/project assessment. The other four use broader foundational/specialized-analysis boundaries; M4 should strengthen these where Human View review identifies likely over-application.

## Pass 3 — Source / Evidence Use alignment
All six have one registered source and three Evidence Use records in the canonical structure. Baseline evidence independence is therefore limited: repeated Evidence Use links to one source do not constitute independent triangulation.
Agricultural engineering has the most immediate source-to-claim alignment risk because its claim set spans machinery/storage/processing while the registered source locator is specifically FAO Land and Water Management.

## Pass 4 — Cross-domain role
All six are legitimate high-reuse dependency nodes:
- infrastructure → water, energy, transport, housing, health, resilience;
- construction → shelter, buildings, infrastructure, materials;
- building science → shelter, construction, energy, moisture, habitability;
- agricultural engineering → agriculture, water, energy, machinery, food continuity;
- health systems → public health, workforce, medicines, information, governance;
- cybersecurity → information, infrastructure, health, governance, continuity.

No new Relation is authorized by this audit. Relation audit remains a later dedicated M4 stage.

## Pass 5 — Human View / adversarial risk
Risk ranking for M4 attention:
- High: infrastructure, construction, agricultural engineering, health systems.
- Medium-high: building science, cybersecurity.
The principal risk is not malicious use; it is over-generalization of foundational claims into site-, patient-, farm-, building-, or system-specific decisions.

## Pass 6 — Findings
- Blocking architectural defects: 0
- Immediate acceptance-blocking content defects: 0
- Substantive maturation findings: 6
- Evidence-independence work required: 6
- Immediate source-to-claim alignment flag: 1 (agricultural engineering)
- Relation audit: pending
- Human View audit: pending
- Unified Debt Map: pending

## Decision
M4 remains open. No CLEAN status is claimed.
Next sequence:
1. Evidence independence audit, with direct source-to-claim verification;
2. Human View/adversarial audit;
3. Relation audit;
4. Unified Debt Map;
5. controlled corrections;
6. re-audit;
7. documentation/coverage/regressions;
8. exact-head 3/3 CI;
9. M4 CLEAN checkpoint.
