# Research–Statistics Relation — Second-Pass Semantic Review

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Exact inspected PR #22 HEAD: `d95499761bfafb16306b805957119607684ab037`  
Scope: `REL-CROSS-RESEARCH-STATISTICS@3` only  
Status: **SECOND-PASS DESK REVIEW COMPLETE; STRONG CONTEXTUAL-NAVIGATION CANDIDATE; INDEPENDENT SUBJECT-MATTER REVIEW AND RIGHTS REVIEW STILL REQUIRED; HOLD PRESERVED**

## 1. Exact current graph

- Relation: `REL-CROSS-RESEARCH-STATISTICS@3`
- Relation type: `research_and_statistical_inference_link`
- Participants, in order:
  1. `CLM-RESEARCH_METHODS_BASICS-A@1`
  2. `CLM-STATISTICS_INFERENCE_BASICS-A@1`
- Relation-specific Context: `CTX-REL-CROSS-RESEARCH-STATISTICS@2`, exact target Relation @3.
- Relation provenance Sources:
  - `SRC-RESEARCH_METHODS_BASICS@1` — National Academies, *Reproducibility and Replicability in Science* (2019).
  - `SRC-STATISTICS_INFERENCE_BASICS@1` — NIST/SEMATECH e-Handbook.
- Research Methods EU A@2 supports Claim A@1 using National Academies Chapter 2, pp. 27–29.
- Statistics Inference EU A@2 supports Claim A@1 using NIST/SEMATECH §3.1.3.4, “Populations and Sampling”.

No endpoint, participant order, Relation, Context, Source or Evidence Use was modified during this review.

## 2. Endpoint fit

### Research Methods endpoint

Claim A states that scientific methods include systematic question formulation, obtaining data and evaluating evidence according to the research task.

The National Academies Chapter 2 locator is directly relevant:
- Printed p. 27 describes the broader process of gaining, questioning and modifying scientific knowledge and expressly highlights statistical inference.
- Printed pp. 27–29 describe scientific inquiry, systematic observation/experimentation, observation, measurement, analysis, evidence collection/characterization and critical review.
- Printed p. 35 has a dedicated section, “Statistical Inference and Hypothesis Testing”, and describes statistical inference as a conceptual and computational framework for scientific questions.

The exact current EU A@2 locator includes pp. 27–29, not p. 35. The existing locator nevertheless includes the p. 27 statement explicitly highlighting statistical inference; p. 35 is an additional corroborating passage in the same cited chapter, not a prerequisite for the current Claim A. Do not modify the EU locator without a separate authorization.

### Statistical Inference endpoint

Claim A states that statistical inference uses sample data to obtain information about characteristics of a wider population or model.

NIST/SEMATECH §3.1.3.4 explicitly explains sampling from a target population to make inferences about that population, and cautions that sample facts are not automatically population facts. It identifies representativeness, sample size, population variability and desired precision as attributes of sample adequacy.

This is a direct match to the current Claim's stated concept and supports the necessary caution about inference.

## 3. Relation-level semantic judgment

The two endpoints are connected at the level of scientific inquiry: statistical inference is one of the analytical frameworks used to answer scientific questions and evaluate evidence. The Relation type `research_and_statistical_inference_link` accurately describes that relationship.

The current graph should be interpreted as a **contextual navigation link**, not as any of the following:
- a claim that all research uses statistical inference;
- a claim that statistical inference is the only or necessary method of evaluating evidence;
- a claim that every research design requires population inference;
- a fixed linear scientific-method sequence;
- a guarantee that sample-based results generalize without assumptions or uncertainty.

The two sources are complementary: National Academies situates inference inside scientific inquiry; NIST explains a specific sample-to-population inference concept. This is a stronger and more direct fit than generic adjacency between two disciplines.

**Second-pass disposition:** retain as a strong contextual-navigation candidate. Do not promote to INCLUDE. The Relation and both affected slices remain HOLD pending independent scientific/editorial review, rights/distribution review and Human View.

## 4. Rights and reuse boundary

National Academies Press identifies the 2019 work as copyrighted and all rights reserved. This review proposes only bibliographic citation, exact locator and hyperlink, with independently written factual paraphrase. Do not redistribute the PDF, reproduce chapter prose, tables or figures, or include substantial excerpts without a documented permission basis.

Rights page: https://www.nationalacademies.org/request-rights-and-permissions

NIST/SEMATECH e-Handbook is used as a cited technical reference. This report does not make a blanket rights determination for any third-party assets embedded in the handbook.

## 5. Important distinction: separate M2 Relation remains unresolved

`REL-CROSS-M2-STATISTICS-RESEARCH@3` is a different Relation and was not reviewed as the same candidate.

Its current endpoints are:
- `CLM-STATISTICS_BASICS-C@1` — statistics/data-analysis foundations;
- `CLM-RESEARCH_METHODS_BASICS-B@2` — reproducibility/replicability research-methods proposition.

The previously recorded endpoint-fit mismatch remains separate. The Research–Statistics A/A contextual-navigation finding does not cure, transfer to, or authorize changes to this M2 Relation. Preserve its HOLD and existing endpoint references until its own evidence/semantic review and bounded authorization.

## 6. Change-control and next action

- No canonical records or versions changed.
- No Relation or Context changed.
- No allowlist, publication state or release disposition changed.
- No rights decision or licence was made.
- No authorization is inferred.

Next action: request a qualified independent scientific/editorial reviewer to confirm that the A/A Relation is useful and non-misleading as a contextual-navigation link. If approved, record that review separately; retain HOLD until all other release gates close.
