# M13 — data visualization basics: source-passage reassessment

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Records: `CLM-DATA_VISUALIZATION_BASICS-A/B/C@1`, `EU-DATA_VISUALIZATION_BASICS-A/B/C@1`, `SRC-DATA_VISUALIZATION_BASICS@1`
Status: **source-passage desk review; all three propositions have direct passages in the linked NIST page, but canonical EU locators remain absent. No records or D/E/B scores changed.**

## 1. Current chain

All three Claim versions and EU versions are 1 and point to `SRC-DATA_VISUALIZATION_BASICS@1`. The current Evidence Use descriptions are generic and do not identify a passage.

The Source is “NIST — Visualization”:
https://www.nist.gov/programs-projects/visualization

The live NIST page is titled “Visualization”, describes an Information Technology Laboratory (ITL) research project, and states that it was created 18 October 2010 and updated 26 March 2025. It is not a generic dictionary definition; it is a NIST project page with a concise summary that directly addresses all three Claim propositions.

## 2. Claim-by-Claim passage review

### Claim A — `CLM-DATA_VISUALIZATION_BASICS-A@1`

Claim: “Визуализация научных данных может помогать исследовать и понимать наблюдаемые структуры и эффекты в данных.”

Direct passage:
- NIST “Visualization”, “Summary”, opening sentence: ITL researchers recognize that visualization of scientific data can provide an understanding of the phenomenon or data being studied.
- The following sentence says visualization can be approached qualitatively, with an example of qualitative effects seen in experiments.

Assessment:
- Direct support for the stated purpose and exploratory/interpretive role.
- The modal “может помогать” is appropriately cautious; visualization does not guarantee correct interpretation or prove a phenomenon by itself.
- Proposed locator: “Summary”, first two sentences.
- Passage status: **DIRECT**.

### Claim B — `CLM-DATA_VISUALIZATION_BASICS-B@1`

Claim: “Визуализация может использоваться не только качественно, но и как объект количественного анализа и сравнения.”

Direct passage:
- NIST “Visualization”, “Summary”: explicitly says visualizations can be treated as objects of study and examined quantitatively.
- The tissue-engineered scaffold example states that measurements and analyses on visualizations enabled comparison of key scaffold descriptors across images.

Assessment:
- Direct support for both quantitative examination and comparison.
- The source's example is specific to tissue-engineered scaffolds; it supports the general methodological possibility, not a claim that every visualization is quantitatively comparable without a defined measurement model.
- Proposed locator: “Summary”, sentence beginning “But visualizations can also be treated as objects of study…” and the following scaffold example.
- Passage status: **DIRECT, with example-scope note**.

### Claim C — `CLM-DATA_VISUALIZATION_BASICS-C@1`

Claim: “Неопределённость измерений и анализа должна учитываться при интерпретации визуального представления данных.”

Direct passage:
- NIST “Visualization”, “Summary”, following the tissue-engineered scaffold example: describes development of methods for quantification of uncertainty in visualization and says this provides information needed to understand measurement and analysis in visualization.

Assessment:
- Direct support for accounting for uncertainty when interpreting measurement and analysis in visualization.
- Editorial precision: the source describes quantification methods and the information they provide; the Claim's “должна учитываться” is a normative formulation. Consider whether the intended statement is methodological necessity or merely the role of uncertainty quantification. A precise alternative is: “Оценка неопределённости визуализации помогает корректно интерпретировать результаты измерений и анализа, представленные визуально.”
- Proposed locator: “Summary”, paragraph beginning “The development of methods for the quantification of uncertainty…”.
- Passage status: **DIRECT, with normative/epistemic wording note**.

## 3. Source identity and rights

The existing Source identity “NIST — Visualization” is recognizable but can be made more reproducible by recording:
- Issuer/organization: National Institute of Standards and Technology, Information Technology Laboratory.
- Page title: “Visualization”.
- Page type: research project summary.
- Created: 2010-10-18.
- Updated: 2025-03-26.
- URI: https://www.nist.gov/programs-projects/visualization

Do not infer that every linked project image, dataset, publication or external resource has the same rights status as the page text. The present remediation can cite and summarize the factual passages with attribution; any reproduction of NIST images, project outputs or third-party materials requires an item-level rights check.

## 4. Proposed Evidence Use remediation

If separately authorized:
1. Add versioned EU-A pinpointing the NIST “Summary” opening sentence and qualitative-effects example.
2. Add versioned EU-B pinpointing the quantitative-examination sentence and tissue-engineered scaffold comparison example.
3. Add versioned EU-C pinpointing the uncertainty-quantification passage.
4. Preserve the example's subject scope and do not turn it into a claim that every chart or visualization is analytically valid.
5. Run Claim/EU/Source linkage, source identity, offline edition and release-conformance regressions.
6. Reassess E under the current rubric only after exact locators are present in canonical EU records and the passages have been rechecked.

## 5. Disposition

| Claim | Passage result | Current canonical locator | Status |
|---|---|---|---|
| A | Direct | Missing | HOLD |
| B | Direct, example-scope note | Missing | HOLD |
| C | Direct, wording precision note | Missing | HOLD |

- Generic Evidence Use records reviewed: 3/3.
- Direct source-passage coverage: 3/3.
- Canonical EU locators added: 0.
- Canonical Claim/EU/Source records changed: 0.
- Historical D/E/B assessments changed: 0.
- Independent visualization/metrology specialist review, Human View and release clearance: 0.

All three Claims remain **HOLD** until authorized versioned locators are added and regression-tested. This desk review does not assign new D/E/B scores or grant release approval.
