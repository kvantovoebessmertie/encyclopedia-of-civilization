# First Edition — Research Methods / Statistical Inference Relation Locator Research

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `f2c24fbac23c331461022b37f4d92bf8cf20bff9`  
Status: **RESEARCH COMPLETE FOR CURRENT SOURCE LOCATORS; RELATION ENDPOINT CHANGE PROPOSED ONLY; NO CANONICAL RECORDS CHANGED**

## 1. Purpose and boundaries

Complete the priority-board task to resolve the research-methods Evidence Use locators from the National Academies source before considering a change to `REL-CROSS-RESEARCH-STATISTICS`.

This report is a source/locator and semantic research result only. It does not authorize:
- changing Claims, Evidence Use, Sources, Relation or Context records;
- changing any publication/completion status or HOLD disposition;
- changing the first-edition master, allowlist or release package;
- merging PR #22, changing `main`, or publishing any material.

The Relation remains HOLD.

## 2. Exact current records re-fetched

### Research Methods

- `SRC-RESEARCH_METHODS_BASICS@1` — National Academies of Sciences, Engineering, and Medicine (2019), *Reproducibility and Replicability in Science*, DOI 10.17226/25303.
- `CLM-RESEARCH_METHODS_BASICS-A@1`
- `CLM-RESEARCH_METHODS_BASICS-B@1`
- `CLM-RESEARCH_METHODS_BASICS-C@1`
- `EU-RESEARCH_METHODS_BASICS-A/B/C@1`

All three Evidence Use records currently reference the exact current Claim and Source versions, but none contains a claim-specific `material.locator`.

### Statistical Inference

- `SRC-STATISTICS_INFERENCE_BASICS@1` — NIST/SEMATECH, *e-Handbook of Statistical Methods*.
- `CLM-STATISTICS_INFERENCE_BASICS-A/B/C@1`
- `EU-STATISTICS_INFERENCE_BASICS-A/B/C@1`

All three Evidence Use records currently reference the exact current Claim and Source versions, but none contains a claim-specific `material.locator`.

### Relation and Context

- `REL-CROSS-RESEARCH-STATISTICS@2`
- `CTX-REL-CROSS-RESEARCH-STATISTICS@1`

Current Relation participants:
1. `CLM-RESEARCH_METHODS_BASICS-B@1` — reproducibility and repeatability are important aspects of evaluating reliability.
2. `CLM-STATISTICS_INFERENCE_BASICS-A@1` — statistical inference uses sample data to obtain information about a wider population or model.

The Context @1 targets Relation @2. The Relation's type is `research_and_statistical_inference_link`, direction undirected, roles `linked_record` / `linked_record`.

## 3. National Academies locators for the three Research Methods Claims

Official source:  
https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science  
Online full text: https://www.nationalacademies.org/read/25303

| Evidence Use | Claim | Exact locator candidate | Support boundary |
|---|---|---|---|
| `EU-RESEARCH_METHODS_BASICS-A@1` | Systematic formulation of questions, obtaining data and assessing evidence | Chapter 2, “Scientific Methods and Knowledge”, pp. 27–29: “What Is Science?”; systematic observation/experimentation; observation, measurement and analysis; collection/characterization of evidence; analysis of collected data and review of methods/results | Directly supports a broad account of scientific inquiry. The chapter expressly says there is no single fixed sequence of steps followed by all scientists; do not imply a universal linear method. |
| `EU-RESEARCH_METHODS_BASICS-B@1` | Reproducibility and repeatability as aspects of reliability | Chapter 3, “Understanding Reproducibility and Replicability”, pp. 42–46: “Defining Reproducibility and Replicability”, committee definitions and Conclusion 3-1; Box 3-1, p. 48, for the separate metrology meaning of repeatability | Supports the importance of reproducibility and replicability, but reveals a terminology issue: the report distinguishes replicability (new data in a new study) from reproducibility (same input data/computational methods) and treats metrological repeatability as a separate measurement concept. |
| `EU-RESEARCH_METHODS_BASICS-C@1` | Reliability of conclusions depends on methods, data, assumptions and limitations | Chapter 2, pp. 28–34: evidence collection/characterization, uncertainty, data analysis, scientific scrutiny and Conclusion 2-1; Chapter 3, pp. 42–46, for method variation and limits of generalizability | Supports the need to assess methods, evidence, uncertainty and study context. It does not imply that every research result is unreliable or that one set of methods applies to all fields. |

### Claim B terminology correction proposal

The current Russian wording says “воспроизводимость и повторяемость”. The National Academies report's adopted distinction is:
- **reproducibility** — consistent results using the same input data, computational steps, methods and code;
- **replicability** — consistent results across studies that collect their own data;
- **repeatability** — a separate metrology concept discussed in Box 3-1, involving repeated measurements under specified conditions.

Therefore the proposed wording for editorial consideration is:

> Воспроизводимость и реплицируемость являются важными аспектами оценки надёжности научных результатов.

This is a proposal only. Do not version Claim B until a bounded authorization is recorded. If the project intentionally means metrological repeatability, it needs a different and explicit measurement-science formulation and source.

## 4. Statistical Inference locator

The existing NIST/SEMATECH Source is a broad engineering-statistics handbook. A direct, claim-specific section was located:

- NIST/SEMATECH e-Handbook, Chapter 3, §3.1.3.4, “Populations and Sampling”:
  https://www.itl.nist.gov/div898/handbook/ppc/section1/ppc134.htm
- The section explicitly describes taking samples from a target population and using sample information to make inferences about that population; it also states that sample facts are not automatically population facts and identifies representativeness, sample size, population variability and desired precision as adequacy considerations.

Candidate locator for `EU-STATISTICS_INFERENCE_BASICS-A@1`:

> NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 3 “Production Process Characterization”, §3.1.3.4 “Populations and Sampling”: target populations, sample observations and inference from a sample to the target population.

Scope boundary: the NIST example is situated in survey/process/manufacturing contexts. Keep the Claim's general statistical statement abstract, and do not imply that any arbitrary sample supports a valid population inference regardless of sampling design.

## 5. Relation semantic assessment and endpoint alternative

The current pair is weak for the declared Relation type:
- Research Methods Claim B concerns reproducibility/repeatability.
- Statistical Inference Claim A concerns inference from sample to population/model.
- The National Academies report treats statistical inference and reproducibility/replicability as related parts of scientific practice, but they are not equivalent concepts. A general topical association alone is not sufficient to establish a direct endpoint relation.

A stronger existing exact-version endpoint pair is available:

1. `CLM-RESEARCH_METHODS_BASICS-A@1`: scientific methods include systematic questions, data collection and evidence assessment.
2. `CLM-STATISTICS_INFERENCE_BASICS-A@1`: statistical inference uses sample data to obtain information about a wider population or model.

Why this pair is stronger:
- National Academies Chapter 2, pp. 27–29, describes scientific inquiry, observation, measurement, evidence and data analysis.
- The same chapter, p. 34, explicitly describes statistical inference as a conceptual and computational framework for addressing scientific questions.
- NIST/SEMATECH §3.1.3.4 provides a direct locator for the statistical inference Claim.

Proposed relation meaning: statistical inference is one methodological framework used within scientific inquiry to draw bounded conclusions from sample data. This is a contextual/methodological link, not a claim that all scientific methods are statistical or that statistical inference proves a hypothesis.

**Recommendation:** if the owner authorizes a Relation correction, consider replacing only the first participant from Research Methods Claim B @1 to Research Methods Claim A @1, preserving Statistical Inference Claim A @1, relation type, roles and undirected direction. Keep the Relation HOLD after correction pending independent semantic review.

Alternative: retain the existing pair only if an editor can articulate and evidence a narrower Relation meaning that genuinely links reproducibility to statistical inference. Current evidence does not justify assuming that link.

## 6. Exact-version Context implications

The current `CTX-REL-CROSS-RESEARCH-STATISTICS@1` targets Relation @2. If a bounded authorization later permits Relation @3:
- Context must be versioned to target the exact new Relation version;
- Relation must frame the exact new Context version;
- participant/source provenance, type, roles, direction and all unrelated semantics must remain unchanged;
- apply the project's coordinated versioning convention and run the relation/context conformance regression.

Do not edit Relation alone while leaving a stale Context target or frame reference.

## 7. Rights and attribution boundary

- National Academies Press report is copyrighted (2019). Use factual paraphrase, exact citation and links only; do not copy report text, tables or figures into the corpus without separate permission.
- NIST/SEMATECH e-Handbook is publicly accessible and hosted by NIST. Preserve exact institutional attribution and link to the relevant section; do not assume every embedded third-party item is reusable.
- Public accessibility does not itself resolve the project's content licence, downstream distribution model or rights-review requirement.
- No named human rights review or project-level licence decision is inferred.

## 8. Result and next actions

Completed:
- Re-fetched both Claim/Evidence Use/Source chains and current Relation/Context at the inspection HEAD.
- Located precise National Academies sections for all three Research Methods Claims.
- Located a direct NIST/SEMATECH section for Statistical Inference Claim A.
- Identified a terminology issue in Research Methods Claim B.
- Identified a more defensible existing endpoint pair for the research/statistics Relation.

Not done:
- No canonical record was changed.
- No Claim or Evidence Use was versioned.
- No Relation/Context was changed.
- No HOLD was promoted; no allowlist or publication decision was made.
- No legal or editorial approval was invented.

Next bounded action: obtain the required authorization for the proposed Research Methods Claim B terminology correction and/or the Relation endpoint substitution. Until then, preserve all exact current records and keep `REL-CROSS-RESEARCH-STATISTICS` HOLD.
