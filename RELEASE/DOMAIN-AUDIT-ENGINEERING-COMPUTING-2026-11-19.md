# Domain audit — software engineering, algorithms, databases, distributed systems and AI (Part II engineering/computing)

Date: 2026-11-19  
Branch: mvp-public-contribution-design-2026-10-11  
PR workstream: #22, Work Package 1  
Audited revision: ebd6eab3980f480ade883adb40853cb7d83741c7  
Disposition: **HOLD — six slices / 54 records screened; no canonical records changed**

## Plan and duplicate-control

This is the next Part II engineering/computing batch. Prior screens for civil-engineering-basics, mechanics-basics, networks-basics and cybersecurity-basics were not repeated. The six slices below were checked at exact version 1.

## Scope

- software-engineering-basics — 9 records
- computer-science-algorithms-basics — 9 records
- databases-basics — 9 records
- distributed-systems-basics — 9 records
- artificial-intelligence-basics — 9 records
- computer-networks-basics — 9 records

Total: **54 records** (18 Claims, 18 Evidence Use, 6 Sources, 6 Context, 6 Scope).

## 1. software-engineering-basics — 9 records

Claims:
- A: software engineering includes requirements, design, implementation, testing and software maintenance.
- B: testing provides evidence about software behaviour under the conditions tested.
- C: changes in requirements or environment may require software-system re-verification.

Current Source: NIST Information Technology Laboratory landing page  
https://www.nist.gov/itl

Additional NIST material checked:
- NIST, “Procedure for Software Quality Assurance”: https://www.nist.gov/system/files/documents/2018/01/12/procedure-for-software-qa-20180101.pdf
- NIST, “Guidelines on Minimum Standards for Developer Verification of Software”: https://www.nist.gov/publications/guidelines-minimum-standards-developer-verification-software

Findings:
- Claim A is directly supported by NIST software lifecycle guidance: requirements, design, construction, testing, installation/validation, operations/maintenance and retirement are lifecycle phases.
- Claim B is consistent with software verification/validation guidance, but should state that tests provide evidence only for the tested inputs, environments and conditions; testing does not prove absence of defects.
- Claim C is plausible and consistent with lifecycle/change-control practice, but the current NIST ITL landing page does not directly support the proposition. It needs a precise change-impact/reverification source and locator.
- All three EUs point to the generic ITL landing page and provide no claim-specific locators.
- Context and Scope target Claim A only.

Decision: **HOLD — strong candidate, current source mapping inadequate.** Use exact NIST software-lifecycle/verification material through authorized Source/EU records and preserve the limitation that testing evidence is bounded by test conditions.

## 2. computer-science-algorithms-basics — 9 records

Claims:
- A: the slice introduces basic concepts and relations needed to orient the reader in algorithms.
- B: interpretation depends on source, context and applicability boundaries.
- C: basic knowledge does not replace specialized checking when conclusions depend on conditions, measurements or professional assessment.

Current Source: NIST glossary, “Algorithm”  
Stored URL: https://www.nist.gov/glossary-term/algorithm

Authoritative NIST entry found:
https://csrc.nist.gov/glossary/term/algorithm

Findings:
- All three Claims are editorial descriptions of the slice and evidence boundaries, not falsifiable propositions about algorithms.
- NIST's glossary defines an algorithm as a clearly specified mathematical process for computation, but the current Claims do not state that or any other algorithmic proposition.
- The stored source URL does not match the current NIST CSRC glossary URL surfaced in this review.
- All EUs are generic; Context/Scope target Claim A only.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires owner/editor-authorized substantive algorithm Claims and matching source-specific EUs. A source URL correction alone would not fix the epistemic defect.

## 3. databases-basics — 9 records

Claims:
- A: a database stores organized data managed by a defined system.
- B: a database schema describes data structure and relationships between elements.
- C: a query retrieves or transforms data according to specified conditions.

Current Source: NIST Information Technology Laboratory landing page  
https://www.nist.gov/itl

Additional NIST entry checked:
- NIST CSRC Glossary, “Database”: https://csrc.nist.gov/glossary/term/Database

Findings:
- The current ITL landing page is not a database definition source and does not provide direct locators for the three Claims.
- The NIST glossary Database entry gives a direct repository/information definition and can support part of Claim A, but it does not directly establish the schema and query propositions in B/C.
- All three EUs use generic descriptions and point only to the ITL landing page.
- Context and Scope target Claim A only.

Decision: **HOLD.** Claim A has a better-fitting NIST glossary source available, while B/C need direct database-schema and query references (for example, an authoritative SQL/database standard or technical reference). Add exact sources/EUs only through authorized versioned corrections.

## 4. distributed-systems-basics — 9 records

Claims:
- A: a distributed system includes multiple computing components that interact over a network.
- B: network latency and partial failures are characteristic conditions of distributed systems.
- C: data consistency and availability depend on the selected architecture and interaction model.

Current Source: NIST Information Technology Laboratory landing page  
https://www.nist.gov/itl

Findings:
- The current source is a general ITL landing page and does not provide a direct distributed-systems definition or technical treatment of partial failure, latency, consistency or availability.
- Claim A is conceptually standard but lacks a direct source locator.
- Claim B is technically important and needs a source that distinguishes network delay, process failure and partial network partitions; avoid presenting all distributed systems as having identical failure behaviour.
- Claim C is broad and risks compressing distinct consistency/availability models into an oversimplified trade-off. It needs a clearly bounded model and direct technical source; do not imply a universal simple rule.
- All EUs are generic and have no specific technical locators.
- Context and Scope target Claim A only.

Decision: **HOLD — evidence and precision gap.** Requires technically precise sources and narrower Claims where necessary. No generic source replacement is sufficient.

## 5. artificial-intelligence-basics — 9 records

Claims:
- A: AI systems can use models and algorithms to process data and produce outputs.
- B: system behaviour depends on data, model, objectives and conditions of use.
- C: AI-system evaluation should account for context, data limitations and quality criteria.

Current Source: NIST, “Artificial Intelligence”  
https://www.nist.gov/artificial-intelligence

Additional NIST material checked:
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF 1.0: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

Findings:
- Claim A is conceptually supported by NIST's AI overview, but the current EU does not identify a precise definition or source passage.
- Claim B is broadly consistent with the AI lifecycle and context-sensitive risk framework, but it needs direct evidence and more precise treatment of intended purpose, data, model, deployment context and human interaction.
- Claim C is strongly aligned with the NIST AI RMF MAP/MEASURE functions, which call for context, validity/reliability, testing, metrics, limitations, performance and risk evaluation. The current Source record, however, points only to the general NIST AI landing page.
- All three EUs are generic and have no NIST AI RMF section/subcategory locators.
- Context and Scope target Claim A only.
- NIST AI RMF is guidance, not a guarantee that a system is safe or trustworthy; the Claims must not imply certification or automatic assurance.

Decision: **HOLD — good candidate with a clear authoritative source family.** Use the NIST AI RMF 1.0 and exact MAP/MEASURE subcategories through authorized Source/EU records; narrow broad Claims and preserve the non-guarantee boundary.

## 6. computer-networks-basics — 9 records

Claims:
- A: the slice introduces basic concepts and relations needed to orient the reader in computer networks.
- B: interpretation depends on source, context and applicability boundaries.
- C: basic knowledge does not replace specialized checking when conclusions depend on conditions, measurements or professional assessment.

Current Source: NIST CSRC Glossary, “Network”  
https://csrc.nist.gov/glossary/term/network

Findings:
- All three Claims are editorial descriptions of the slice and its evidence boundaries, not falsifiable propositions about computer networks.
- The NIST Network glossary entry can support a substantive network definition, but the current Claims do not assert one.
- The slice is distinct from networks-basics screened earlier; no prior adjudication is transferred between the two.
- All EUs are generic and do not identify a substantive network proposition.
- Context and Scope target Claim A only.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires owner/editor-authorized substantive network propositions (for example, packet switching, addressing, routing or protocol-layer functions) with direct evidence. Do not reuse the earlier networks-basics screen as a substitute.

## Cross-slice and integrity checks

- All 54 inventory-listed files were read at version 1; local Claim/EU/Source references resolve to the corresponding listed record.
- No new Relation was created; subject adjacency does not establish a typed semantic relation.
- Prior civil-engineering-basics, mechanics-basics and networks-basics screens were not repeated.
- Prior cybersecurity-basics M4 substantive review was not repeated.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was edited.
- No INCLUDE decision, allowlist, preview or publication status was changed.
- main was not changed; PR #22 remains Draft.

## Group result

| Slice | Records | Main finding | Decision |
|---|---:|---|---|
| software-engineering-basics | 9 | Lifecycle evidence exists; current NIST ITL source too broad; EUs generic | HOLD |
| computer-science-algorithms-basics | 9 | All Claims editorial; stored glossary URL mismatch | HOLD |
| databases-basics | 9 | Claim A has a direct NIST glossary source; B/C lack direct schema/query evidence | HOLD |
| distributed-systems-basics | 9 | Current source not relevant enough; B/C require technical precision | HOLD |
| artificial-intelligence-basics | 9 | NIST AI RMF supports key concepts; exact subcategory locators absent | HOLD |
| computer-networks-basics | 9 | All Claims editorial; distinct from earlier networks-basics slice | HOLD |
| **Total** | **54** | **No public INCLUDE decisions** | **HOLD** |

Next Part II family: proceed to social systems and public institutions only after excluding public-risk communication, transportation/public transport, epidemiology/public health and other already screened slices. Do not repeat prior reviews or start new M13 batches.
