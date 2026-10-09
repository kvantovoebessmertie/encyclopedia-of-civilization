# M10 Human View Task Audit — 2026-10-09

## Status

**CURRENT POST-CORRECTION RESULT: HV-M10-01 THROUGH HV-M10-08 PASS FOR THE TESTED BEHAVIORS IN DESK SIMULATION. This is not a live novice study. Exact-HEAD CI and overall acceptance must be read from the current workflow and PR state; this file does not assert a static CI result.**

Target: `human-settlement-systems-basics` at prior M10 content HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`.
Method: adversarial task simulation from the perspective of a reader unfamiliar with repository architecture. This is not a live novice study and is not represented as one. Findings are based on the README, all three Claims, all three Evidence Use records, Context, Scope and the dedicated regression.

## Scenario results

### HV-M10-01 — Cold start
- **Task:** After reading only the README, explain what a settlement system is.
- **Expected:** The reader understands that a settlement is more than buildings and includes people, housing, services, infrastructure, governance and environmental/social/economic conditions.
- **Observed:** The README explains that housing, transport, water, sanitation, other services, governance and environment interact. A reasonable reader can give a basic explanation.
- **Result:** PASS (desk simulation).
- **Evidence:** README sections “Для чего нужен этот срез” and “Пример взаимозависимости”.
- **Limitation:** No real novice participant was observed.

### HV-M10-02 — Dependency reasoning
- **Task:** Given housing without a functioning water service, identify what else must be checked.
- **Expected:** The reader sees that housing alone does not ensure safe water, sanitation or transport, and that networks/services/governance and local conditions matter.
- **Observed:** The README provides this illustrative example and says dependencies vary by place. It communicates the central idea, but it does not guide the reader through a simple dependency chain or ask them to check service availability, capacity, access and interdependencies.
- **Result:** PARTIAL.
- **Evidence:** README “Пример взаимозависимости”; Claim B.
- **Debt:** Add one short, clearly illustrative step-by-step example that demonstrates the reasoning without turning into local design guidance.

### HV-M10-03 — Use in a real decision
- **Task:** Decide whether a specific site is ready for a housing project.
- **Expected:** The reader does not treat this slice as sufficient and identifies local data, applicable requirements and qualified expertise as necessary.
- **Observed:** The README explicitly states those limits. Scope says this is not a site project, engineering calculation, legal opinion or operational instruction.
- **Result:** PASS for boundary recognition (desk simulation).
- **Evidence:** README “Границы применения”; Scope record.
- **Limitation:** It does not provide a next-step checklist for gathering local information; that is a usability opportunity, not authority to add project-specific advice.

### HV-M10-04 — Evidence traceability
- **Task:** For the claim about integrated planning, find which source supports it and what that source does not establish.
- **Expected:** A reader can identify the OECD-backed claim and distinguish source support from local proof.
- **Observed:** The Claim and Evidence Use record explicitly name OECD and state that the source supports coordination but does not guarantee outcomes or replace local analysis. However, the README itself does not provide human-facing links from each claim to its source; a reader must know how to navigate records and understand their IDs/types.
- **Result:** PARTIAL.
- **Evidence:** Claim C, Evidence Use C; README only describes the record pattern.
- **Debt:** Add a novice-facing “Как проверить основание утверждения” section with readable claim/source labels and navigable links where repository conventions permit, without changing canonical source identity or provenance.

### HV-M10-05 — Misinterpretation / adversarial reading
- **Task:** Try to infer that integrated planning guarantees good outcomes everywhere.
- **Expected:** The text blocks this inference.
- **Observed:** Claim C says coordination does not guarantee identical results across places; Evidence Use C says it does not guarantee a specific outcome and does not replace local analysis.
- **Result:** PASS for this tested inference (desk simulation).
- **Evidence:** Claim C; Evidence Use C.
- **Limitation:** One blocked inference does not establish that every possible misreading is blocked.

### HV-M10-06 — Failure and uncertainty
- **Task:** Identify what remains unknown when evaluating a real settlement.
- **Expected:** The reader recognizes that local context, local data, requirements and specialist assessment are needed.
- **Observed:** Context and Scope make this boundary explicit. The README names local data, requirements and expertise, but does not turn these into a short, usable list of questions to take forward.
- **Result:** PARTIAL.
- **Evidence:** Context, Scope and README.
- **Debt:** Add a compact “Что проверить дальше” prompt list framed as questions, not as a universal design recipe.

### HV-M10-07 — Navigation and recovery
- **Task:** A reader who does not know record types, IDs or repository architecture tries to find the source and the next useful step.
- **Expected:** The reader can follow a clear, human-facing path without learning the internal schema first.
- **Observed:** README says “Source → 3 Claims → 3 Evidence Use → Context → Scope”, which describes internal structure rather than a reader journey. It does not itself provide source links, a glossary or a next-step route.
- **Result:** FAIL.
- **Evidence:** README “Состав среза”.
- **Debt:** Replace or demote the internal schema pattern in the user-facing path; provide simple navigation to claims/sources and a bounded next-step route. Retain any required architecture description only as a clearly labelled technical note if necessary.

### HV-M10-08 — Boundary and safety
- **Task:** Try to use the slice as a site-specific engineering calculation, legal conclusion or operational instruction.
- **Expected:** The slice makes clear that it is introductory and insufficient for those uses.
- **Observed:** README and Scope explicitly deny those uses and require local data, applicable requirements and specialist expertise.
- **Result:** PASS for explicit boundary (desk simulation).
- **Evidence:** README “Границы применения”; Scope record.
- **Limitation:** This does not validate any specific real-world project decision.

## Consolidated findings

1. **HV-M10-02 — dependency reasoning is only partially operationalized.** One example is present, but no short reasoning path is provided.
2. **HV-M10-04 — evidence traceability is understandable to a repository-aware reviewer but not reliably to a novice.** Claim/source links are encoded in records, not surfaced as a reader path in the README.
3. **HV-M10-06 — uncertainty boundaries are explicit but not actionable as a next-step prompt.**
4. **HV-M10-07 — navigation is an architecture description, not a novice user journey.** This is the strongest Human View defect.
5. **HV-M10-LIMITATION — no live novice study was conducted.** Do not report one. A task-based desk simulation and regressions can improve confidence but cannot substitute for observed novice use.

## Proposed bounded correction scope — NOT YET AUTHORIZED FOR IMPLEMENTATION

Potential targets:
- `CONTENT/vertical-slices/human-settlement-systems-basics/README.md`
- `REFERENCE/tests/test_content_human_settlement_systems_basics_vertical_slice.py`
- M10 post-correction audit and unified debt map addenda, if needed.

No Claim, Evidence Use, Source, Context, Scope, Relation, ID, provenance, source URL, record count, coverage or record-type change is proposed by this audit. Before editing, record explicit authorization for the exact file list and define regression assertions for novice navigation, dependency reasoning, traceability and the local-decision boundary.

## Acceptance decision

**M10 full maturity acceptance remains OPEN.** The earlier exact-HEAD technical CI pass is valid only for the checks it executed. It does not resolve the Human View findings above. The proposed correction must be implemented on this follow-up branch, audited again, and all three required CI workflows must pass on one identical final HEAD. Keep the PR open/draft/unmerged; do not modify `main` or the protected M10 branch.

## Post-correction task re-run — 2026-10-09

The README now provides a plain-language route, a five-step bounded dependency example, readable links to each Claim/Evidence Use/source pair, a “what to check next” question list, and an explicitly labelled technical structure note.

- HV-M10-01 Cold start: **PASS in desk simulation** — definition remains prominent and plain-language.
- HV-M10-02 Dependency reasoning: **PASS in desk simulation** — the housing example gives a bounded sequence from housing to services, access, local conditions and system-level caution.
- HV-M10-03 Real decision: **PASS for boundary recognition in desk simulation** — local data, applicable requirements and qualified expertise are named; no site-specific recommendation is made.
- HV-M10-04 Evidence traceability: **PASS in desk simulation** — each of the three Claims links to its Evidence Use and canonical Source record; source limits are stated in the README.
- HV-M10-05 Adversarial guarantee inference: **PASS for the tested inference** — the text states coordination does not guarantee the same outcome and local analysis is required.
- HV-M10-06 Failure/uncertainty: **PASS in desk simulation** — the reader receives questions about availability, dependencies, local data, requirements, affected people and expert review.
- HV-M10-07 Navigation/recovery: **PASS in desk simulation** — the reader journey is now primary; internal record structure is demoted to a technical note.
- HV-M10-08 Boundary/safety: **PASS for the explicit boundary** — the material disclaims site-specific design, engineering calculations, legal opinions and operational instructions.

**Method limitation remains:** these are desk-based task simulations against repository content, not observed results from a live novice participant. Do not claim a live usability study occurred. The dedicated regression and three required CI workflows are acceptance gates; verify their result against the exact current HEAD before declaring acceptance.