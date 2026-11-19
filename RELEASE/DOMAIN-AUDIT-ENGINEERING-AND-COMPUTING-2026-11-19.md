# Engineering and Computing Domain Audit — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Scope: eight Part II candidate slices; exact current canonical JSON records in the PR branch.

## Scope and method

Reviewed all 72 records in the following eight slices:

- `mechanics-basics`
- `civil-engineering-basics`
- `software-engineering-basics`
- `computer-science-algorithms-basics`
- `databases-basics`
- `cybersecurity-basics`
- `distributed-systems-basics`
- `artificial-intelligence-basics`

Each slice contains one Source, three Claims, three Evidence Use records, one Context and one Scope. The review checked exact record identity/version, provenance and reference alignment, Claim substance, source identity/locator quality, Evidence Use specificity, and Context/Scope usefulness. This was a record-level screening pass, not an external-source substantiation or rights clearance.

## Record inventory

| Slice | Records | Source | Claims | Evidence Use | Context | Scope | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| mechanics-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| civil-engineering-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| software-engineering-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| computer-science-algorithms-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| databases-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| cybersecurity-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| distributed-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| artificial-intelligence-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| **Total** | **72** | **8** | **24** | **24** | **8** | **8** | **0 INCLUDE / 8 HOLD / 0 EXCLUDE** |

## Findings by slice

### mechanics-basics — HOLD

- The three Claims are editorial/meta statements about what the slice introduces, source/context dependence, and the need for specialist review. They are not mechanics propositions and cannot be tested against the cited Newton's Laws chapter.
- The Source identifies OpenStax University Physics Volume 1, Chapter 5, but the Evidence Use records contain only generic descriptions and no section, equation, example, or passage locators.
- Context and Scope are generic and do not delimit a concrete mechanics concept or applicability boundary.

Required remediation: replace the three meta-Claims with source-bounded mechanics propositions, select exact Newton's Laws passages, and version the corresponding Source/Evidence Use/Context/Scope records under explicit correction authorization.

### civil-engineering-basics — HOLD

- All three Claims are generic editorial/meta statements, not civil-engineering facts.
- The Source points to the OpenStax subject catalogue rather than an identifiable engineering-mechanics or civil-engineering text/chapter. It is not a pinpoint source for the Claims.
- All Evidence Use descriptions are generic; no exact passage, figure, equation, or standard clause is identified.
- Context and Scope do not define a meaningful civil-engineering domain boundary or exclude unsafe design/construction use.

Required remediation: identify a specific authoritative educational or standards source, define the intended introductory subject boundary, replace the meta-Claims with substantive propositions, and add exact locators.

### software-engineering-basics — HOLD

- Claims A–C are substantive at a high level: lifecycle activities, testing as evidence about observed behavior, and retesting after changes. Their wording still needs precise definitions and boundaries.
- The Source is the NIST ITL landing page, not a directly identified software-engineering standard, body of knowledge, or publication. It does not provide traceable support as recorded.
- All three Evidence Use records lack pinpoint locators and do not state which passage supports each proposition.
- Context and Scope are boilerplate rather than a meaningful lifecycle, system, or assurance boundary.

Required remediation: choose a specific source such as an applicable software-engineering body of knowledge or lifecycle standard, distinguish verification, validation, testing and maintenance where relevant, and add passage/section-level Evidence Use.

### computer-science-algorithms-basics — HOLD

- All three Claims are generic editorial/meta statements, not algorithm definitions or properties.
- The NIST glossary algorithm entry is a potentially relevant source identity, but the Claims do not actually state the algorithm definition or a supported property.
- Evidence Use records contain no exact glossary entry text/locator or other pinpoint support.
- Context and Scope are generic.

Required remediation: replace the meta-Claims with a bounded algorithm definition and carefully selected foundational properties, then attach exact NIST or textbook locators. Avoid claiming complexity, correctness, or optimality without separate support.

### databases-basics — HOLD

- Claims A–C contain substantive introductory propositions about organized data, schemas/relationships, and queries.
- The Source points to the NIST ITL homepage, not a database publication or technical specification. The current source identity and locator do not establish the three propositions.
- Evidence Use records are generic and contain no chapter, section, or documentation locator.
- Context and Scope do not identify the database model or delimit relational versus non-relational concepts.

Required remediation: select a directly relevant authoritative database text/specification, define the model being described, and map each Claim to exact passages. Avoid treating all database systems as relational.

### cybersecurity-basics — HOLD

- Claims A–C are substantive introductory propositions concerning security risk, confidentiality/integrity/availability, and risk management.
- The NIST Cybersecurity Framework URL is a relevant high-level source candidate, but the canonical Source does not identify a specific version or section. CIA terminology and risk-management lifecycle may require distinct NIST glossary/framework locators.
- Evidence Use records are generic and do not identify CSF 2.0 functions/categories or exact supporting material.
- Context and Scope are boilerplate. The slice must not imply that the framework is a complete operational security procedure.

Required remediation: pin the exact NIST CSF edition and relevant sections; use separate authoritative definitions where the CSF itself is not the direct source; add precise locators and explicit non-prescriptive scope.

### distributed-systems-basics — HOLD

- Claims A–C are substantive but broad: interacting networked components, latency/partial failure, and consistency/availability trade-offs.
- The Source is the NIST ITL homepage and does not identify a distributed-systems publication.
- Evidence Use records have no pinpoint locators. Claim B requires direct support for partial failure/latency; Claim C needs careful separation of consistency models, availability and system-specific design choices.
- Context and Scope do not define the distributed-system model or the limits of the trade-off statement.

Required remediation: use a recognized distributed-systems text or primary technical source, define the consistency/availability vocabulary precisely, and attach claim-specific locators.

### artificial-intelligence-basics — HOLD

- Claims A–C are substantive high-level propositions about models/algorithms, dependence on data/model/goals/context, and evaluation criteria.
- The Source points to a NIST AI landing page but does not pin a specific NIST AI publication or framework version.
- Evidence Use records are generic and lack exact sections. The three Claims may require separate support from AI RMF, lifecycle, measurement/validation or data-quality material.
- Context and Scope are generic and do not distinguish AI system types, intended use, or risk context.

Required remediation: pin the NIST AI RMF edition and relevant sections, add direct support for each proposition, and clarify that the slice is introductory rather than a complete technical or safety standard.

## Cross-slice findings

1. **Reference integrity:** all 72 records use the expected 9-record structure; Claim provenance points to the slice Source, Evidence Use points to the corresponding Claim and Source, and Context/Scope target the slice's Claim A at the current version. No stale version reference was identified in this eight-slice sample.
2. **Source quality:** four slices have generic or mismatched Source identities (civil engineering, software engineering, databases, distributed systems). Mechanics, algorithms, cybersecurity and AI have relevant source candidates, but their exact version/section locators are absent.
3. **Evidence Use quality:** all 24 Evidence Use records lack claim-specific pinpoint locators. Generic statements that a source is used within its material do not establish what passage supports the Claim.
4. **Claim substance:** mechanics and algorithms each contain three editorial/meta Claims. The other six slices contain substantive but broad Claims requiring source-level verification and tighter scope.
5. **Context and Scope:** all eight pairs are generic or insufficiently domain-specific. They need to delimit the concepts and applicability rather than repeat a generic educational disclaimer.
6. **Rights and editorial review:** public availability of an external source does not establish permission to redistribute or adapt it. Rights, attribution, independent editorial review and Human View remain open.
7. **Publication boundary:** existing `publication_status=published` values are not first-edition approval. All eight slices remain HOLD; no record is promoted to INCLUDE.

## Aggregate decision

**0 INCLUDE / 8 HOLD / 0 EXCLUDE.**

No canonical JSON was modified in this audit. No publication state, first-edition allowlist, or release decision was changed. This report does not authorize Claim replacement, source substitution, or versioned corrections. Those changes require a bounded correction authorization and exact record-level evidence.

## Next remediation order

1. Select and authorize precise source replacements/locators for all eight slices.
2. Replace the six editorial/meta Claims in mechanics and algorithms with substantive, source-bounded Claims.
3. Tighten broad Claims in software engineering, databases, cybersecurity, distributed systems and AI only where source review requires it.
4. Version all dependent Evidence Use, Context and Scope records with correct references.
5. Re-run exact-head preflight, Reference tests, Release Conformance Gate and Offline Edition.
6. Keep all eight slices HOLD until rights and independent editorial/Human View gates are resolved.


## Remediation follow-up — 2026-11-19

The bounded remediation for all eight slices was subsequently completed under `ENGINEERING-COMPUTING-REMEDIATION-001`. Source, Claims, Evidence Use, Context and Scope records were versioned; claim-specific locators and exact version references were added; and the eight slice READMEs were aligned. See `RELEASE/ENGINEERING-COMPUTING-REMEDIATION-ADDENDUM-2026-11-19.md` for the complete source map, record counts, reference-integrity verification, rights limits and remaining release gates.

The original audit decisions remain unchanged: 0 INCLUDE / 8 HOLD / 0 EXCLUDE. The remediation does not grant publication approval.
