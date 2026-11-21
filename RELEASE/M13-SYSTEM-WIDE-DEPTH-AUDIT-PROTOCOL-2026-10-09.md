# M13 System-Wide Depth Audit Protocol — 2026-10-09

## Status and authority

**STATUS: protocol and baseline lock initiated; no substantive audit result is claimed yet.** This is the planning/control document for a system-wide depth audit, not a maturity acceptance or a statement that the corpus has passed.

- Audit branch: `m13-system-wide-depth-audit-2026-10-09`
- Frozen starting candidate SHA: `e87e5bba60c9ed1101ecd4d53493c968c4760dac`
- Starting branch: `m12-human-factors-source-and-human-view-2026-10-09`
- M12 PR #20 remains open/draft/unmerged; M13 is stacked on its candidate, not on `main`.
- `main` remains protected at `203a7028e08da394fd44630fe38727be07bc8849`.
- The starting SHA has successful Reference implementation tests, Release Conformance Gate and Offline Edition runs attached to that exact SHA. Those results are baseline evidence only; any M13 commit requires its own exact-head gate before M13 can be called CLEAN.

## Why this audit exists

The corpus has broad structural coverage and repeated focused audits, but prior M8 depth scoring was a 12-slice, 43-Claim purposive diagnostic. It cannot establish depth across the entire corpus. This audit must determine where the current corpus provides explanatory knowledge rather than only labels/assertions, where claims are well-supported and bounded, and which verified gaps deserve correction.

The audit must not optimize for record counts, force a fixed number of findings, or rewrite material merely to improve scores. Structural conformance, substantive depth, evidence fit, boundaries, Human View and integration are separate dimensions. No single “completion percentage” is authorized.

## Audit scope

### A. Whole-corpus inventory — census

Inventory all registered vertical slices and all Record JSONs at the frozen SHA. Record per slice:
- directory/registry identity and README presence;
- total records by actual Record type (read JSON `type` fields; do not infer type solely from filenames);
- Claim count and Claim IDs;
- linked Evidence Use and Source counts, including links and unmatched/orphaned records;
- Context and Scope presence and target references;
- Relation endpoints and justifications;
- dedicated regression presence and the relevant authorization/coverage registry entries;
- prior audit/maturity/debt history, distinguishing historical findings from currently open debt.

Reconcile tree inventory against `RELEASE/CONTENT-COVERAGE.json`, the slice registry, and actual JSON content. Report every discrepancy; do not silently normalize one authority to match another.

### B. Claim-level depth and epistemic audit — census

Review **every Claim in the frozen corpus**, not a sample and not a hand-picked subset. Current tree inventory identifies 1,494 Claim files, subject to verification from each JSON record's actual `type`. Score every Claim on D/E/B below and record Claim ID, slice, SHA, reviewer rationale, linked Evidence Use and Source IDs. If a claim is malformed, unlinked, duplicate, or cannot be scored, retain it in the denominator and explain why; never silently omit it.

#### D — explanatory depth (0–3)
- **0:** no usable proposition, incoherent statement, or too underspecified to assess.
- **1:** label/basic assertion; little mechanism, conditions, distinctions or practical meaning.
- **2:** meaningful mechanism/process or relevant conditions, with at least one material limitation or distinction.
- **3:** appropriately scoped explanation with key conditions, exceptions/trade-offs or causal links explicit for its stated introductory scope.

#### E — claim-specific evidence fit (0–3)
- **0:** no traceable support, broken reference, or source plainly does not support the claim.
- **1:** source exists but the linked Evidence Use is vague, generic, misaligned, or does not accurately describe support.
- **2:** claim-specific Evidence Use identifies relevant support and represents source scope accurately.
- **3:** level 2 plus material independent corroboration where warranted, or an explicit defensible reason additional corroboration is not materially needed. Source count alone never earns a higher score.

#### B — boundary and epistemic discipline (0–3)
- **0:** important limits, uncertainty or safety boundaries are absent/misleading.
- **1:** generic caveat with little help deciding when the claim applies.
- **2:** meaningful context/scope, applicability or uncertainty boundaries are visible and accurate.
- **3:** important known/unknown distinctions, context dependencies, exceptions and likely misuse/overgeneralization are explicitly bounded.

Score D, E and B independently. Provide a short rationale for each score; do not replace the rubric with a single aggregate grade.

### C. High-consequence overlay — census of identified risk-relevant claims

Identify safety-sensitive or high-consequence Claims across all slices (health, emergency response, water/food/sanitation, fire/CO, electricity/energy, construction/materials/tools, chemicals, legal/financial decisions, and other risk-bearing topics discovered in the inventory). Review every claim identified by the risk-screen, including:
- claim/source fit and currentness where relevant;
- prerequisites, local/jurisdictional dependencies, operating conditions and failure modes;
- explicit do-not-infer/do-not-do boundaries where needed;
- whether the content could reasonably be mistaken for operational instructions beyond its evidence.

The risk-screen itself must be documented and reviewed so that high-consequence content is not limited to a preselected list of familiar topics.

### D. Human View — structured coverage, not false user-study claims

Perform a desk-based Human View review of:
- every high-consequence slice;
- every slice with a material D/E/B score of 0 or 1 or a structural/linkage anomaly;
- a frozen, stratified set spanning old and new content, practical and conceptual topics, and different domain families.

Record H1 Findability, H2 Comprehension and H3 Safe interpretation separately (0–3), the task a reader is trying to complete, likely misinterpretation, and the concrete evidence for the finding. Desk inspection is not live novice testing or external peer review. Do not claim otherwise.

### E. Integration and relationships

Inventory all Relations and verify endpoints, duplicates, semantic justification and user-relevant meaning. Also identify material cross-domain dependencies not captured by current Relations. A missing Relation is a finding only when the link would materially improve navigation, explanation or practical reasoning; topical proximity alone is insufficient.

## Workflow and audit stages

1. **M13 baseline lock:** freeze exact SHA; verify branch/PR/base/main state; inventory tree, actual Record types and registries; reconcile all counts; publish slice manifest and audit execution plan.
2. **M13 risk-frame lock:** define and record reproducible risk-screen rules; enumerate high-consequence candidates; independent check of the risk-frame before scoring.
3. **Claim audit batches:** score all Claims in fixed, non-overlapping batches; freeze each batch's IDs before review; preserve raw scores and rationale. Track reviewed/total by SHA, not by memory.
4. **High-consequence and Human View passes:** perform the census overlay and targeted desk review, retaining explicit limitations.
5. **Integration pass:** audit all Relations and material missing dependencies.
6. **Synthesis:** report distributions and counts by dimension, slice/domain, age/wave, risk class and prior maturity status; distinguish confirmed findings, hypotheses, not-applicable cases and unresolved uncertainty.
7. **Independent review:** independently recheck scoring consistency, high-severity findings, denominator, selection rules and a subset of raw evidence trails. Expand/re-score if reviewer disagreement or systematic defects appear.
8. **Correction scope lock:** only after audit findings are verified, authorize narrow corrections with dedicated regressions. No bulk rewrite or new topics by quota.
9. **Post-correction audit and release gate:** rerun affected audits and all three workflows on one identical final SHA; independently verify diff, coverage, relations, authorization, PR/base/main. No documentation-only commit after final gate unless all three workflows are rerun.

## Reporting requirements

- Publish exact SHA, date, inventory version, rubric version, batch manifest, reviewer, denominator, exclusions (normally zero), score distributions and rationales.
- Report D/E/B/H1/H2/H3 and integration separately. Provide counts of 0/1 scores and high-consequence findings; means, if shown, must include distributions and denominators.
- Separate corpus structure from knowledge quality. A CI pass proves only what the relevant checks actually test.
- Never claim statistical population estimates from purposive samples; the Claim review is intended as a census.
- Never claim live usability, external peer review, domain certification or comprehensive risk assessment without evidence of those activities.
- Distinguish a source that is unavailable from a source that is disproven; distinguish a missing relation from a confirmed substantive defect.
- A new commit invalidates exact-head CI acceptance evidence.

## Non-negotiable invariants

- Do not modify `main`, merge M12, or change protected historical checkpoints.
- Work on this isolated M13 branch; any future content corrections require explicit, finding-specific authorization and regressions.
- No Record type changes, count targets, or new Relations are authorized by this protocol.
- Do not weaken tests, schemas, evidence rules or acceptance gates.
- Do not mark a prior OPEN debt resolved merely because it is mentioned in a historical audit; recheck current content.
- Do not mark the entire encyclopedia “complete” on the basis of corpus counts or this protocol.

## Initial acceptance state

M13 is **IN PROGRESS**. The baseline inventory and protocol are not a CLEAN checkpoint. M13 can close only when its authorized audit outputs are complete, the final independent review passes, and Reference implementation tests, Release Conformance Gate and Offline Edition all pass on the same exact final HEAD with branch/PR/base/main and tree checks independently verified.
