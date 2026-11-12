# M13 thematic source-passage review — Statistics Inference Basics — 2026-11-12

## Status and boundary

Reviewed the three Claims and linked Evidence Uses in `statistics-inference-basics` against the M13 branch content at parent revision `3900b9f3576426ecdf23af0b64f2b777bd5da38c`.

**Disposition: all three Claims remain HOLD.** The NIST/SEMATECH e-Handbook is a relevant and authoritative source, and direct passages were located for sampling-based inference, method assumptions, confidence intervals, and hypothesis tests. The current Evidence Uses nevertheless point only to the handbook home page and provide no exact locators. No canonical records, manifests, scores, or publication states were changed.

## Claim-by-claim findings

### CLM-STATISTICS_INFERENCE_BASICS-A@1

**Claim:** Statistical inference uses sample data to obtain information about characteristics of a wider population or model.

- NIST e-Handbook §1.3.5 “Quantitative Techniques” explicitly describes estimating a population parameter from a sample and distinguishes interval estimation from hypothesis testing.
- NIST §7.1.4 “What are confidence intervals?” explains that a random sample is used to approximate a population mean and that a confidence interval describes uncertainty around the estimate.
- Existing `EU-STATISTICS_INFERENCE_BASICS-A@1` only names the e-Handbook generally. It has no chapter/section locator or description of the relevant sample-to-population passage.
- **Disposition: HOLD.** Direct support exists; the Evidence Use is not reproducible as written.

### CLM-STATISTICS_INFERENCE_BASICS-B@1

**Claim:** Statistical methods require explicit assumptions about data and model, and applicability depends on those conditions being met.

- NIST §7.1.2 “What assumptions are typically made?” states that the validity of the tests described in that chapter depends on assumptions about a single process/distribution, normality, and lack of temporal correlation. It also explains checking for departures from normality.
- NIST §1.3.6 “Probability Distributions” states that intervals and tests may rely on distributional assumptions and that those assumptions should be verified for the dataset before applying the method.
- These passages support the Claim, with an important scope limitation: assumptions are method-specific. The NIST §7.1.2 assumptions must not be generalized to all statistical procedures.
- Existing `EU-STATISTICS_INFERENCE_BASICS-B@1` does not identify either passage.
- **Disposition: HOLD.** Good direct passages located; exact locators and method-specific qualification are missing from the Evidence Use.

### CLM-STATISTICS_INFERENCE_BASICS-C@1

**Claim:** Statistical uncertainty must be considered when interpreting estimates and hypothesis tests.

- NIST §1.3.5 “Quantitative Techniques” explicitly identifies interval estimation and hypothesis tests as approaches to uncertainty in sample estimates.
- NIST §1.3.5.2 “Confidence Limits for the Mean” explains how an interval expresses uncertainty in an estimated population mean and distinguishes the confidence level of the procedure from the probability interpretation of a particular realized interval.
- NIST §7.1.5 explains the relationship between hypothesis tests and confidence intervals; §7.1.3 explains the role and limits of hypothesis tests.
- Existing `EU-STATISTICS_INFERENCE_BASICS-C@1` only refers to the handbook generally, without identifying these sections.
- **Disposition: HOLD.** The Claim has direct support, but the current Evidence Use does not identify the passages and should preserve the distinction between estimation uncertainty and the interpretation of a test result.

## Cross-record findings

1. All three Evidence Uses point to the intended Claim and Source IDs.
2. All three Evidence Use descriptions are near-identical generic statements. They do not preserve claim-specific evidence or pinpoint locations.
3. The NIST Source URI is a handbook landing page. It is an appropriate source identity but insufficient as a record-level locator for the specific propositions.
4. The Context and Scope records are generic and do not add evidentiary support.
5. Do not equate “not rejected” with “accepted as true”; NIST's hypothesis-testing discussion explicitly warns against that inference.

## Required next steps

- Version each Evidence Use with the relevant NIST chapter, section number, heading, and a concise description of the exact support.
- For Claim B, make the method-specific nature of assumptions explicit and do not imply one universal set of assumptions.
- For Claim C, preserve the distinction between confidence intervals, sampling uncertainty, significance tests, and practical significance.
- Any canonical edit requires bounded authorization, versioned record changes, required test/manifest updates, and exact-head CI. This desk review does not authorize canonical changes.

## Sources reviewed

- NIST e-Handbook §1.3.5 “Quantitative Techniques”: https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm
- NIST e-Handbook §1.3.6 “Probability Distributions”: https://www.itl.nist.gov/div898/handbook/eda/section3/eda36.htm
- NIST e-Handbook §1.3.5.2 “Confidence Limits for the Mean”: https://itl.nist.gov/div898/handbook/eda/section3/eda352.htm
- NIST e-Handbook §7.1.2 “What assumptions are typically made?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc12.htm
- NIST e-Handbook §7.1.3 “What are statistical tests?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm
- NIST e-Handbook §7.1.4 “What are confidence intervals?”: https://itl.nist.gov/div898/handbook/prc/section1/prc14.htm
- NIST e-Handbook §7.1.5 “What is the relationship between a test and a confidence interval?”: https://www.itl.nist.gov/div898/handbook/prc/section1/prc15.htm
