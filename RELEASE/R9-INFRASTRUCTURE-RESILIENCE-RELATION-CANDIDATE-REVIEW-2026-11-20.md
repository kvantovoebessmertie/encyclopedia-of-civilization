# R9 — Infrastructure Resilience Relation Candidate: Source Identity and Evidence Review

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Inspected HEAD: `8e5f58aafd1b29e3bb2bff8b3d92a7e978fb2984`

## Scope

This is a research and remediation proposal only. No canonical Infrastructure Resilience record, Claim, Evidence Use, Source, Relation, Context, Scope, allowlist or release decision was changed.

## 1. Candidate endpoint

`CLM-INFRASTRUCTURE_RESILIENCE-D@1` states:

> Оценка устойчивости инфраструктуры должна учитывать зависимости между секторами и то, как отказ или восстановление одной услуги меняет риск и восстановление других функций сообщества.

This is more specific to infrastructure interdependency than `CLM-INFRASTRUCTURE_RESILIENCE-A@1`, which describes community resilience generally. It is therefore a plausible endpoint candidate for the held emergency-management / infrastructure-resilience linkage, subject to evidence and authorization.

## 2. Source identity defect

The current `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1` identifies its source as “FEMA — Infrastructure Dependency Primer” and points to a FEMA URL.

The inspected official PDF is hosted on the CISA domain and identifies the publication as *The Infrastructure Dependency Primer*, with an “As of June 2, 2023” date. Its Overview says the primer helps planners understand how infrastructure dependencies can affect community risk and resilience and how to incorporate that understanding into planning. Its Learn module covers essential community functions/services, supporting infrastructure systems, and how systems depend on one another.

The source identity must not continue to attribute this document to FEMA without documentary evidence establishing FEMA as the issuing author. The directly inspected document supports CISA attribution.

Official source:
- CISA, *The Infrastructure Dependency Primer*, PDF, p. 1, “Overview” and “A Web-Based Educational Resource” / “Learn” module.
- Direct PDF: https://www.cisa.gov/sites/default/files/2023-06/InfrastructureDependencyPrimerFS_June23_508c.pdf

The CISA Infrastructure Resilience Planning Framework (IRPF) v1.2, February 2024, p. 22, Table 6, provides concrete examples of dependencies among water, electricity, finance, communications, roads, emergency services, cyber/IT and commodity/manpower systems. It is useful as a potential additional source if the Claim is to retain detailed examples of dependencies and their operational consequences:
- https://www.cisa.gov/sites/default/files/2024-02/Infrastructure%20Resilience%20Planning%20Framework%20v1.2_JAN2024_508c.pdf

## 3. Evidence fit and support boundary

The CISA Primer p. 1 directly supports the general proposition that infrastructure systems depend on one another and that those dependencies can affect community risk and resilience planning.

However, the present Claim D wording is stronger and more causal than the exact introductory passage: it specifically asserts that failure or restoration of one service changes risk and recovery of other community functions. The Primer overview alone does not fully establish every element of that formulation.

Therefore:
- do not silently treat the current Evidence Use D as fully supported merely by adding a page locator;
- either narrow Claim D to the proposition directly supported by the CISA Primer, or add a second inspected source with pinpoint support for disruption/recovery propagation;
- distinguish direct source statements from any project-level inference;
- do not claim that the source provides a quantitative risk model or universal causal law.

A conservative source-bounded candidate wording for owner consideration is:

“Зависимости между инфраструктурными системами могут влиять на риски для сообщества и должны учитываться при планировании устойчивости.”

This is a proposed wording only; it is not authorized or applied.

## 4. Proposed bounded remediation — requires owner approval

If approved, the minimum defensible package would be:

1. Version `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1` to @2, correcting the identity to CISA and pinning the official PDF, publication title, date and p. 1 locator.
2. Version `CLM-INFRASTRUCTURE_RESILIENCE-D@1` to @2 only if the owner approves the conservative source-bounded wording above; preserve the Claim ID and `documented_fact` type.
3. Version `EU-INFRASTRUCTURE_RESILIENCE-D@1` to @2 with exact current Claim/Source references, locator “p. 1, Overview and Learn module”, concise independent paraphrase, and explicit support limits.
4. Keep all other Claims, Sources, Evidence Use records, Context, Scope and Relations untouched unless a separately authorized dependency correction is demonstrably necessary.
5. Keep the Infrastructure Resilience slice and every affected Relation on HOLD; no INCLUDE decision or release eligibility follows.

The existing NIST Community Resilience Program Source and Claim A are not changed under this proposal. No cross-slice Relation is changed in this research pass.

## 5. Rights and release boundaries

The PDF's public accessibility is not itself a project-level reuse licence. Record bibliographic identity and factual locator metadata; do not reproduce PDF prose, graphics, diagrams or page layout. Item-level rights and project-distribution compatibility remain to be reviewed.

Independent infrastructure editorial review, Human View and all applicable first-edition gates remain required. Technical CI does not establish substantive correctness or publication eligibility.

## Conclusion

The Infrastructure Resilience candidate has a promising direct conceptual fit, but its current source identity is misattributed and its current Claim D wording needs a tighter evidence match. The safe next action is a bounded owner-approved source/evidence correction, not a Relation promotion. No canonical Infrastructure Resilience changes have been made in this report.
