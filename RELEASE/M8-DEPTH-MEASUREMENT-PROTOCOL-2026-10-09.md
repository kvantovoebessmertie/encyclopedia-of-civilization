# M8 Depth Measurement Protocol — 2026-10-09

## Purpose and baseline lock

This protocol establishes a repeatable baseline for content maturity. It does not measure whether the encyclopedia is a given percentage “complete.” Breadth, claim depth, evidence maturity, Human View/usability, and cross-domain integration are reported separately.

- Accepted M7 baseline SHA: `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
- Corpus snapshot at that SHA: 483 vertical slices / 4,827 Records / 19 Record types; 616 Sources / 1,668 Evidence Use / 64 Relations.
- M7 is accepted CLEAN by the recorded exact-head 3/3 CI gate. M8 planning and measurement occur on a successor branch; the accepted M7 tree is not rewritten.
- Baseline reference: [M7 accepted CLEAN record](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/12#issuecomment-6079202174).

## Measurement principles

1. **Do not collapse dimensions.** A large number of shallow records cannot compensate for missing evidence or unsafe applicability boundaries.
2. **Claim-level denominator.** Score each reviewed Claim, not each JSON file or Evidence Use record. Also report the number of slices, claims and linked Evidence Use records actually reviewed.
3. **Scope-aware evidence.** A source locator is not itself evidence. Check whether the source supports the exact claim and whether the stated evidence role is justified.
4. **Independent corroboration is conditional.** Do not reward source-count quotas. Require independent corroboration where it materially reduces uncertainty or is warranted by consequence; a narrow claim may justify a single authoritative source if the rationale is explicit.
5. **High-consequence weighting is a separate lens.** Report safety-critical gaps explicitly; do not hide them inside an average.
6. **Human View claims require evidence.** Desk inspection is not a live novice study. Never label it as one.
7. **Version every result.** Record the exact corpus SHA, date, sampling frame, inclusion rules, raw rubric values, reviewer notes, denominator and limitations.
8. **No score inflation by rewrite.** Accepted slices are not changed merely to improve metrics. Corrections require a specific, auditable finding and dedicated regression where appropriate.

## Sampling design

Use a **stratified, purposive diagnostic sample**, not a probability sample. It is designed to expose maturity differences and failure modes, not to estimate the population-wide percentage with statistical confidence.

Initial strata (12-slice design):
- **H — high-consequence/practical:** water, hygiene, fire/CO, flood/food or equivalent safety-relevant knowledge.
- **M — prior maturation:** selected slices from M6 or earlier maturity passes.
- **I — cross-domain/infrastructure:** domains whose use depends on relationships across systems.
- **G — general introductory knowledge:** ordinary scientific, quantitative or social-science slices.
- **N — newest additions:** all four M7 slices, to compare newly authored introductory content against older material.

Initial M8 baseline: 12 slices: two each from H, M, I and G, plus all four newest M7 slices in N. The N stratum is intentionally oversampled because the immediate question is whether recent additions preserve depth while older high-consequence and previously matured content provide comparison. This is a diagnostic design, not a population-weighted estimate. If a slice belongs to multiple strata, assign it once to its primary stratum and document the choice. Freeze the list before scoring. Inspect every Claim in each selected slice; do not cherry-pick individual claims after seeing their content. If a slice has no Claim records, report that fact and do not replace it silently.

The sample is diagnostic and does not represent every domain, language, record type, standard rule combination, or risk class. After the first pass, expand the sample only where the results reveal material uncertainty or high-consequence risk.

## Claim-level rubric (0–3 per dimension)

### D — explanatory depth
- **0:** no usable proposition, incoherent statement, or content too underspecified to assess.
- **1:** basic assertion or label; little explanation of mechanism, conditions, or practical meaning.
- **2:** meaningful explanation of mechanism/process or relevant conditions, with at least one material limitation or distinction.
- **3:** well-bounded explanation with important conditions, exceptions/trade-offs or causal links made explicit; suitable depth for the stated introductory scope.

### E — claim-specific evidence fit
- **0:** no traceable support, broken link, or source plainly does not support the claim.
- **1:** source locator exists but claim-specific material/role is missing, vague, or weakly aligned.
- **2:** claim-specific Evidence Use identifies relevant support and accurately represents the source’s scope.
- **3:** level 2 plus material corroboration from an independent source where warranted, or an explicit, defensible reason why additional corroboration is not materially needed. Source count alone never earns this score.

### B — boundary and epistemic discipline
- **0:** material applicability limits, uncertainty, or safety boundaries are absent or misleading.
- **1:** generic caveat with little help determining when the claim applies.
- **2:** meaningful Context/Scope and explicit applicability or uncertainty boundaries.
- **3:** important known/unknown distinctions, context dependencies, and likely misuse/overgeneralization are anticipated and bounded.

For each claim record raw D/E/B scores and a short rationale. **Do not combine D/E/B into a project-completion percentage.** A descriptive mean may be reported only with the full distribution, denominator, strata and exact SHA; median and counts of 0/1 scores should also be shown.

## Slice-level review

For every sampled slice, separately record:
- **H1 Findability (0–3):** can a reader identify the topic and locate the relevant claim without reading architecture documents?
- **H2 Comprehension (0–3):** are terms, sentence structure, context and source roles understandable to the intended non-specialist?
- **H3 Safe interpretation (0–3):** are prerequisites, limitations and high-consequence warnings visible where relevant?
- **I Integration:** list material cross-domain dependencies; score no higher merely because Relations exist. Each reviewed Relation must have a justified user-relevant meaning and valid endpoints.
- **Regression need:** concrete testable failures only; no test is weakened to improve the result.

H1–H3 anchors: 0 = materially unusable/misleading; 1 = significant barriers; 2 = usable with specific gaps; 3 = clear and appropriately bounded for the stated scope. These are desk-review scores unless a separately documented user study is conducted.

## Reporting format

For each dimension publish:
- numerator/denominator and distribution;
- slice and claim IDs reviewed;
- stratum;
- rubric and reviewer rationale;
- known limitations and excluded scope;
- exact HEAD SHA and date;
- confirmed findings, severity, correction authorization and regression ID if applicable.

Breadth is reported as registered slice inventory and a map of uncovered user needs, not a completeness fraction. Human View desk review and live user testing are distinct evidence types. Cross-domain Relation counts are descriptive, not proof of integration quality.

## Decision gates

1. Freeze the M7 baseline SHA and sample list.
2. Verify slice/claim inventory and exact claim/Evidence Use links.
3. Score the frozen sample using D/E/B and H1–H3.
4. Independently recheck high-consequence scores and all proposed severity-1 findings.
5. Build M8 Gap Map from confirmed evidence, not assumptions or a quota.
6. Choose depth maturation, new slices, integration work or a mixed batch according to user value and risk.
7. Make authorized changes on the M8 branch only; run substantive, evidence, Human View, Relation, regression and exact-head 3/3 CI gates as applicable.
8. Record CLEAN outside the code tree after independent final verification, or rerun all gates if any post-CI tree change is made.

## Explicit non-claims

This protocol does not prove corpus truth, completeness, statistical representativeness, live usability, professional safety, or century-scale preservation. It is a repeatable diagnostic instrument whose validity must itself be reviewed after the first scored pass.
