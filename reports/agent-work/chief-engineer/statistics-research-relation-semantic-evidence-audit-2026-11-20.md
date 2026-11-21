# Statistics–Research Cross-Slice Relation — Semantic and Evidence Audit

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `75e75e127c5ba54f7de8bfd8e30e22a95a95b468`  
Status: **REPORT-ONLY FINDING — RELATION HOLD; NO CANONICAL CHANGE AUTHORIZED OR MADE**

## 1. Purpose and boundary

Re-examine the exact current endpoint pair and evidence chain for `REL-CROSS-M2-STATISTICS-RESEARCH@3` after identifying a possible mismatch between the Relation type and its second Claim.

This is a report-only semantic/evidence audit. It does not authorize changes to canonical Content, the Relation, Context, Evidence Use, Source, standards, tests, candidate membership, the Part II denominator, any allowlist, or publication decisions. No record is promoted. Preserve HOLD.

## 2. Exact current canonical records re-fetched

All records below were fetched from branch `mvp-public-contribution-design-2026-10-11`, whose tip at inspection was `75e75e127c5ba54f7de8bfd8e30e22a95a95b468`.

| Record | Exact version | Verified content relevant to this review |
|---|---:|---|
| `REL-CROSS-M2-STATISTICS-RESEARCH` | @3 | Relation type `statistics_and_research_design_link`; participants Statistics Basics Claim C @1 and Research Methods Claim B @2; undirected |
| `CTX-REL-CROSS-M2-STATISTICS-RESEARCH` | @2 | Relation-specific condition; target_ref points exactly to Relation @3 |
| `CLM-STATISTICS_BASICS-C` | @1 | Experimental design and data analysis are linked; inference quality depends on study formulation, not calculations alone |
| `EU-STATISTICS_BASICS-C` | @1 | Supports Statistics Claim C, but its material description is generic and contains no section/page locator |
| `SRC-STATISTICS_BASICS` | @1 | NIST/SEMATECH Engineering Statistics Handbook; public-reference identity |
| `CLM-RESEARCH_METHODS_BASICS-B` | @2 | Reproducibility and replicability are important aspects of evaluating reliability of scientific results |
| `EU-RESEARCH_METHODS_BASICS-B` | @3 | Exact Claim @2 / Source @1 linkage; pinpoint locator to National Academies (2019), Chapter 3, pp. 42–46 and Box 3-1, p. 48 |
| `SRC-RESEARCH_METHODS_BASICS` | @1 | National Academies, *Reproducibility and Replicability in Science* |

## 3. Semantic finding

**Finding: endpoint-to-Relation-type alignment is not demonstrated.**

The Relation type explicitly states a link between statistics and research design. The first endpoint is aligned: Statistics Claim C explicitly concerns experimental design and analysis. The second endpoint, Research Methods Claim B @2, concerns reproducibility and replicability as dimensions of reliability. Its current wording does not state a proposition about research design, experimental planning, choice of factors, study formulation, or design-analysis integration.

The National Academies locator in EU-RESEARCH_METHODS_BASICS-B@3 is appropriately specific for the reproducibility/replicability Claim. That improved evidence locator does not convert the Claim into a research-design Claim and does not establish the intended Relation semantics.

This is a semantic alignment concern, not a claim that reproducibility is unrelated to research practice in general. A broader conceptual association is insufficient to establish that this particular typed Relation accurately represents the selected endpoint pair.

## 4. Evidence finding and defensible locator

The current EU for Statistics Claim C has no pinpoint locator. The existing canonical Source is the NIST/SEMATECH Engineering Statistics Handbook.

A directly relevant official section was checked:

- NIST/SEMATECH Engineering Statistics Handbook, §5.1.1, “What is experimental design?”
- Direct locator: https://itl.nist.gov/div898/handbook/pri/section1/pri11.htm
- The section defines design of experiments as an efficient procedure for planning experiments so collected data can be analyzed to yield valid and objective conclusions; it also describes selecting objectives and process factors and laying out the experimental plan in advance.

This section directly supports the experimental-design portion of Statistics Claim C. It is a strong candidate for a future, separately authorized, versioned Evidence Use locator correction. It does not resolve the Relation's second-endpoint mismatch, and this report does not alter EU-STATISTICS_BASICS-C@1.

## 5. Candidate-scope boundary

The Part II exact-version master register includes `CLM-STATISTICS_BASICS-C@1` as a dependency row, marked HOLD, sourced from the cross-slice Relation dependency inventory. It does not list `CLM-RESEARCH_METHODS_BASICS-B@2` as a Part II candidate or dependency row. The `research-methods-basics` slice is not among the represented 124 Part II slices. The separate `research-design-basics` slice is also outside the current master.

Therefore:

- Do not infer first-edition candidate eligibility for Research Methods Claim B from its appearance as a Relation endpoint.
- Do not add the research-methods or research-design slice to the candidate denominator.
- Do not replace the endpoint with a Claim from the out-of-scope research-design slice.
- Any endpoint replacement, candidate-scope expansion, or canonical version change requires explicit owner authorization and the normal exact-version/evidence/rights review.

## 6. Disposition and safe next steps

**Disposition: retain `REL-CROSS-M2-STATISTICS-RESEARCH@3` and its relation-specific Context @2 on HOLD.**

No canonical record, test, standard, register row, candidate key, or decision state was changed by this audit.

Recommended sequence, only after the relevant bounded authorization:

1. Decide whether the Relation type should be narrowed to the actual reproducibility/research-reliability relationship, or whether an eligible, in-scope research-design endpoint exists. Do not silently choose either path.
2. If a type or endpoint change is approved, version the Relation and its target-specific Context together, preserving all unrelated fields and HOLD.
3. Separately consider adding the NIST §5.1.1 pinpoint to the Statistics Claim's Evidence Use through a bounded versioned correction.
4. Re-fetch all exact Claim/EU/Source/Relation/Context records, validate reciprocal references, and run exact-head CI.
5. Keep rights, editorial review, Human View, candidate eligibility and release approval as separate gates.

## 7. Acceptance

Accept this report only as a report-only identification of:
- a typed-Relation / second-endpoint semantic mismatch requiring owner adjudication;
- a missing pinpoint in the Statistics Claim's current Evidence Use, with an official NIST section identified as a strong locator candidate;
- an explicit candidate-scope boundary: Research Methods Claim B and Research Design Basics are not admitted to the current Part II master.

**All affected material remains HOLD. No publication or merge authorization is implied.**
