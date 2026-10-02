# CONTENT GAP MAP — 2026-10-02 R1

## Purpose

This artifact defines the current content-gap map for the Encyclopedia of Civilization after the clean 248-slice / 2187-record checkpoint.

It is a planning artifact, not a claim that the encyclopedia can ever be exhaustively complete. “Gap” means a material coverage opportunity identified against the current DOMAIN-ROADMAP, the actual 248-slice corpus, the Authoring Contract, and the current corpus audit.

## Current baseline

- vertical slices: 248
- records: 2187
- registered Record types: 19
- directly covered Record types: 19/19
- blocking findings: 0
- architecture change required: no
- current state: CLEAN_CONFORMING

## 1. Roadmap reconciliation

The historical DOMAIN-ROADMAP contains many candidate domains that are already present in CONTENT. Those are not reopened merely because they remain named in older roadmap text.

The current 248-slice registry is the source of truth for presence.

Result:
- historical roadmap coverage: substantially closed
- architectural coverage: closed
- new-domain discovery: still open
- depth and linkage coverage: materially open

## 2. Gap classes

### G1 — Missing subject domains

Priority candidates for future controlled slices, selected because they add materially different questions rather than simple renaming:

#### Human / health
- pathology-basics
- pharmacology-information-basics
- public-health-surveillance-basics
- rehabilitation-basics
- reproductive-health-information-boundaries
- environmental-health-basics

Safety boundary: general information, evidence and limitations; no individualized diagnosis or treatment.

#### Society / institutions
- political-economy-basics
- comparative-law-basics
- administrative-law-basics
- international-law-basics
- civil-society-basics
- social-policy-basics
- taxation-basics
- labor-economics-basics
- migration-and-mobility-basics

Political and legal material must remain descriptive, jurisdiction/date bounded and non-electoral.

#### History / civilization / culture
- comparative-civilizations-basics
- historical-geography-basics
- economic-history-basics
- history-of-science-basics
- history-of-technology-basics
- religious-studies-basics
- literature-basics
- cultural-anthropology-basics

Historical claims require temporal scope and must not silently convert sequence into causation.

#### Physical / life sciences
- particle-physics-basics
- nuclear-physics-information-basics
- physical-chemistry-basics
- analytical-chemistry-basics
- molecular-biology-basics
- physiology-of-systems-basics
- marine-biology-basics
- environmental-biology-basics

Hazard-sensitive areas require strengthened safety review.

#### Technology / information
- web-systems-basics
- information-security-operations-basics
- software-architecture-basics
- version-control-basics
- human-ai-interaction-basics
- information-retrieval-basics
- computer-graphics-basics
- embedded-systems-basics
- sensor-systems-basics

Cybersecurity content remains defensive/descriptive and must not become operational abuse guidance.

#### Infrastructure / material world
- water-infrastructure-basics
- electrical-grid-basics
- transportation-infrastructure-basics
- waste-infrastructure-basics
- housing-systems-basics
- industrial-safety-basics
- supply-and-demand-infrastructure-basics

## 3. G2 — Depth gaps inside existing slices

The standard 9-record profile is a useful minimum pattern, not a semantic completeness guarantee.

Depth review should test whether important existing slices contain, where applicable:

1. definition;
2. mechanism or structure;
3. conditions of applicability;
4. limitations;
5. uncertainty;
6. counterexample or boundary case;
7. historical/contextual scope;
8. relation to adjacent concepts;
9. evidence quality and source role.

Slices with non-standard profiles are not automatically defective. They should be reviewed according to subject-specific Definition of Done.

## 4. G3 — Cross-domain linkage gaps

A dedicated linkage pass should look for evidence-supported relationships across major clusters.

### Physical world
physics ↔ chemistry ↔ materials ↔ engineering ↔ energy ↔ infrastructure

### Earth systems
geology ↔ climate ↔ atmosphere ↔ ocean ↔ hydrology ↔ soil ↔ agriculture

### Life and health
cell biology ↔ genetics ↔ evolution ↔ microbiology ↔ immunology ↔ epidemiology ↔ public health

### Mind and society
neuroscience ↔ psychology ↔ learning ↔ sociology ↔ economics ↔ institutions

### Civilization
agriculture ↔ food systems ↔ trade ↔ urbanization ↔ state formation ↔ writing ↔ archaeology ↔ history

### Technology
mathematics ↔ algorithms ↔ computing ↔ networks ↔ software engineering ↔ AI ↔ human-computer interaction

### Risk and resilience
hazard science ↔ emergency management ↔ infrastructure ↔ public-risk communication ↔ health

Relations are added only when the relation semantics are actually supported; no graph inflation for its own sake.

## 5. G4 — Record-type depth

All 19 Record types have direct coverage, but several specialized types have intentionally sparse representation.

This is not an architectural gap.

It is a candidate content-depth question:
- where are Assessment records genuinely useful?
- where are Inference records justified?
- where do Decision/Action/Result/Event/State/Process records materially improve understanding?
- where are Relation records needed to express verified cross-domain structure?
- where are Provenance/Authorship/Trust records useful beyond the dedicated provenance slice?

The answer must come from content semantics, not from target counts.

## 6. G5 — Evidence and source diversity

Future expansion should deliberately diversify source roles where the subject requires it:

- primary sources;
- standards and institutional documentation;
- scientific literature;
- statistical sources;
- historical/archival sources;
- methodological sources;
- jurisdiction-specific official sources.

A source-count increase without a meaningful evidence role is not considered gap closure.

## 7. G6 — Human View / safety depth

The current machine conformance is green, but domain-specific editorial review remains necessary for:

- medical information;
- emergency and safety information;
- hazardous technical domains;
- cybersecurity;
- legal/jurisdiction-dependent material;
- historical claims with contested causality;
- claims where uncertainty materially changes interpretation.

The Human View must preserve limitations, uncertainty and source role rather than only the headline claim.

## 8. G7 — Geographic / jurisdictional representation

Some domains cannot be considered sufficiently covered by a single generalized context.

Candidate dimensions:
- multiple legal systems;
- different institutional models;
- different measurement/standards contexts;
- regional environmental conditions;
- historical periods and regions;
- global South / global North evidence diversity where relevant.

This is a contextual coverage issue, not a request to multiply slices mechanically.

## 9. Prioritization rule

Future waves should be selected by:

1. material user-question coverage;
2. non-duplication;
3. cross-domain leverage;
4. evidence availability;
5. semantic richness;
6. safety / misuse risk;
7. jurisdiction or temporal sensitivity;
8. expected improvement in Human View;
9. ability to test existing Standard rules;
10. ability to strengthen the corpus as a connected knowledge system.

## 10. Proposed accelerated closure strategy

Do not return to a blind “ten slices forever” loop.

Use:

GAP MAP
→ select 20–40 highest-value non-duplicate domains
→ divide into controlled 10-slice CI units
→ validate each unit automatically
→ accumulate clean units
→ deep cross-domain audit
→ content-depth audit
→ adversarial semantic/safety review
→ full corpus regression
→ Reference Tests
→ Release Gate
→ CLEAN checkpoint.

This preserves the existing quality gate while reducing repeated full-audit overhead.

## 11. Definition of “gap closed”

A gap is closed only when the relevant evidence exists in the corpus and survives:

- schema validation;
- semantic conformance;
- evidence/provenance checks;
- Human View;
- package/recovery;
- dedicated regression where appropriate;
- corpus-wide regression;
- deep cross-domain review when the gap concerns relationships.

A topic merely being named in a roadmap does not close a gap.

## 12. Current conclusion

The 248/2187 corpus is architecturally conforming and broad.

The next stage is not “add as many records as possible”. It is:

- close high-value missing domains;
- deepen important existing slices;
- strengthen cross-domain relations;
- diversify evidence roles;
- close domain-specific Human View/safety gaps;
- test geographic, jurisdictional and temporal boundaries.

This map is the planning baseline for the next controlled content expansion.
