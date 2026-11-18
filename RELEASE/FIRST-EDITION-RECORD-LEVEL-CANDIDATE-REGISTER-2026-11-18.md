# First Edition — Record-Level Candidate Register
Date: 2026-11-18
Branch: mvp-public-contribution-design-2026-10-11
Status: WORKING SCREEN; no public INCLUDE approved by this register.

## Decision vocabulary
- INCLUDE: exact version and its complete dependency closure have passed identity, evidence, scope, consequence, rights, and reader checks.
- HOLD: structurally suitable, but at least one release condition remains unresolved.
- EXCLUDE: unsuitable for this edition; retain canonical history and record the reason.
- A slice being complete, published, or CI-clean is not an INCLUDE decision.

## Current record-level screening

### 1. Units and measurement — HOLD
Candidate Claims (all record_version 1; type_version 1.0):
- CLM-UNITS_AND_MEASUREMENT-A@1 — “Измерение выражает величину количественно относительно принятой единицы и процедуры измерения.”
- CLM-UNITS_AND_MEASUREMENT-B@1 — “Международная система единиц SI определяет согласованный набор единиц для выражения физических величин.”
- CLM-UNITS_AND_MEASUREMENT-C@1 — “Результат измерения не следует трактовать как точное знание без учёта используемой единицы, метода и неопределённости измерения.”

Dependency closure:
- EU-UNITS_AND_MEASUREMENT-A@1 → SRC-UNITS_AND_MEASUREMENT@1
- EU-UNITS_AND_MEASUREMENT-B@1 → SRC-UNITS_AND_MEASUREMENT@1
- EU-UNITS_AND_MEASUREMENT-C@1 → SRC-UNITS_AND_MEASUREMENT@1
- CTX-UNITS_AND_MEASUREMENT@1; SCP-UNITS_AND_MEASUREMENT@1

Verified source identity and locator:
- NIST — SI Units; https://www.nist.gov/pml/owm/metric-si/si-units
- The three Evidence Use records currently contain only generic descriptions (“source ... used ... without going beyond the material”); they do not identify a page section, table, definition, or inspected passage supporting each individual Claim.
- Claim A/C also extend beyond a simple SI-unit listing into measurement procedure and uncertainty; the linked source fit must be demonstrated rather than assumed.

Reason for HOLD:
1. Evidence Use lacks claim-specific pinpoint locators and inspected passage notes.
2. No per-Claim passage-fit record is established here.
3. Rights/attribution for the exact release bundle remain subject to the project-level publication decision.
4. No release-specific Human View result is attached to these exact versions in this register.

Required closure: inspect NIST source and identify exact supporting sections for each Claim; if the NIST page does not support A/C as worded, do not silently rewrite canonical records—retain HOLD or select a better existing source through authorized review. Then complete rights and Human View checks.

### 2. Motion basics — HOLD
- CLM-MOTION_BASICS-A@1 — “Положение объекта задаётся относительно выбранной системы отсчёта.”
- EU-MOTION_BASICS-A@1 → SRC-MOTION_BASICS@1
- Source identity: OpenStax Physics, “one-dimensional kinematics”
- Locator: https://openstax.org/books/physics/pages/2-introduction-to-one-dimensional-kinematics

The Claim/EU/Source identity chain is present. The Evidence Use is a generic summary and does not specify the inspected section or passage. Scope record SCP-MOTION_BASICS@1 exists (basic educational slice, not exhaustive); exact context/scope dependency closure and rights/release review remain to be recorded. HOLD until pinpoint and exact dependency closure are verified.

### 3. Cell basics — HOLD
- CLM-CELL_BASICS-A@1 — “Клетка является основной структурной и функциональной единицей живых организмов.”
- EU-CELL_BASICS-A@1 → SRC-CELL_BASICS@1
- Source identity: OpenStax Biology 2e, “cell structure and function”
- Locator: https://openstax.org/books/biology-2e/pages/4-introduction

The Claim/EU/Source identity chain is present. The Evidence Use is a generic summary without the inspected section/passage. Exact context/scope closure, pinpoint verification, rights and release Human View are not established in this register. HOLD pending those checks.

### 4. Water treatment basics — HOLD (high consequence)
- CLM-WATER_TREATMENT_BASICS-A@1
- CLM-WATER_TREATMENT_BASICS-B@1
- CLM-WATER_TREATMENT_BASICS-C@1
- EU-WATER_TREATMENT_BASICS-A/B/C@1; linked to SRC-WATER_TREATMENT_BASICS@1 (WHO Water Treatment)
- EU-EPA-WATER-TREATMENT-B@1 links an independent EPA source to Claim B.
- Existing cross-slice relation: REL-CROSS-WATER-QUALITY-TREATMENT@1.

The existing WHO/EPA material and historical review work are preserved; no prior adjudication is recreated. However, the evidence-use descriptions inspected for A/B/C are generic, and the topic can directly affect health. Do not publish practical treatment instructions from these Claims until each claim's source passage, contaminants/applicability limits, independent support, and qualified high-consequence review are explicitly verified. The independent EPA linkage is useful but does not by itself close all three Claims.

## Previously identified HOLD candidates — do not re-review here
- CLM-PLANT_BIOLOGY_BASICS-A@1
- CLM-STATISTICS_BASICS-A@1
- CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1
- CLM-CLIMATE_BASICS-A@1

Their earlier HOLD state is retained. This register does not supersede their prior review artifacts.

## Release decision at this checkpoint
- INCLUDE: none approved by this register.
- HOLD: all exact candidates listed above.
- EXCLUDE: none newly assigned.
- The current evidence does not justify pretending that a first-edition allowlist is ready. Do not generate a public allowlist containing HOLD records.
- This is a bounded record-screen result, not a request to restart M13 or launch another Batch.

## Next bounded closure work
1. Use existing audit reports and candidate decisions first; do not repeat closed adjudications.
2. For low-risk foundational candidates, close exact source pinpoint and reader checks; prioritize breadth after evidence quality, not record count.
3. For survival-opening high-consequence material, apply enhanced source, applicability, and safety review; keep unresolved procedures out while allowing appropriately bounded explanatory material only when its own record chain passes.
4. Resolve publication license, attribution policy, accountable editor, correction/takedown route, and rollback before public distribution.
5. Freeze an allowlist only after records actually reach INCLUDE. Keep all other records visibly outside the release bundle.


### 5. SI units — HOLD (best-developed bounded private-preview candidate)
Exact candidate dependency closure:
- CLM-SI-SEVEN-BASE@1
- EU-SI-SEVEN-BASE@2 → SRC-NIST-SI-UNITS@1
- CLM-SI-DERIVED@1
- EU-SI-DERIVED@2 → SRC-NIST-SI-UNITS@1
- CTX-SI@1; SCP-SI@1

Evidence-use quality:
- EU-SI-SEVEN-BASE@2 identifies NIST sections “Defining Constants” and “Base and Derived Units”, and explicitly distinguishes seven base units from seven defining constants.
- EU-SI-DERIVED@2 identifies “Base and Derived Units” and limits “22” to derived units with special names and symbols, not all possible derived units.
- Source: NIST — SI Units, https://www.nist.gov/pml/owm/metric-si/si-units.
- The existing PR #22 private preview builder enforces the exact seven-record ID/version set and these pinpoint/boundary strings. This is a technical preview fixture, not publication approval.

Why still HOLD:
1. The fixture explicitly sets every record to `preview_only` and says it is not editorial approval or publication permission.
2. CTX-SI@1 and SCP-SI@1 target Claim A only; the builder correctly prevents silently extending them to Claim B. A separate applicability check for Claim B is still needed or the displayed context/scope must remain limited to Claim A.
3. The available material establishes a bounded evidence chain, but no completed independent Human View/editorial sign-off for the actual release bundle is attached here.
4. Rights/attribution and project-level publication decisions remain open.

This is the strongest current low-risk candidate for a first reader artifact once the bounded review and governance decisions close. Do not change preview_only to INCLUDE by inference from the builder or CI.


## Reuse of completed substantive and Human View audits (2026-11-18 verification)

The following existing reports were read on this branch. They are reused as prior review evidence; no adjudication was repeated.

### Survival opening — P1 emergency cluster
Existing completed substantive review:
- `hand-tool-safety`
- `home-fire-smoke-safety`
- `emergency-lighting-safety`
- `emergency-alert-warning`
- `septic-system-emergency`

Report: `RELEASE/P1-REMAINDER-SUBSTANTIVE-AUDIT-2026-10-06.md`
- P1 depth findings: closed.
- Evidence diversity: PASS (OSHA/CCOHS; USFA/NFPA; IPAWS/FEMA/Red Cross; CDC/EPA).
- Scope/limits: PASS.
- Natural cross-domain links: closed; no artificial hand-tool relation.
- The report explicitly says that audit round is not final closure by itself.

Existing Human View/adversarial closure is recorded in `RELEASE/CLEAN-CHECKPOINT-P1-2026-10-06.md`:
- Human View/adversarial findings: 0 remaining.
- Content depth, evidence diversity, cross-domain integration and Human View: PASS.
- However, that checkpoint itself labels its state **CLEAN — VALIDATION PENDING** and says its own commit must pass the three release-layer workflows. The checkpoint text cites prior correction-baseline runs, not a verified status for the checkpoint commit itself.
- A live status/run lookup for the checkpoint blob commit `2974a8e9d4c69c6f8bf922ba7b405d6afe55de4b` and correction commit `b83a37df4d44c151cda8e4d74e370390902dcc44` returned no status records and no PR workflow runs in the connected GitHub view.

Decision for first edition: these five slices are substantively mature candidates for the opening survival section, but remain **HOLD — checkpoint validation evidence not independently retrievable in this review**. Do not repeat their substantive/Human View audit. Retrieve or restore the exact checkpoint workflow evidence; if it cannot be recovered, run the required validation on a current reviewed commit without reopening the content audit.

### Survival opening — P2 food resilience cluster
Existing report: `RELEASE/P2-FOOD-SAFETY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`
- `food-safety-basics`: introductory and source-bounded; FDA/CDC tracks separated.
- `food-preservation-basics`: general principles only; risky procedures excluded; no artificial second-source requirement.
- `flood-food-safety`: CDC/FDA evidence and conservative contamination boundaries.
- `power-outage-food`: USDA/FDA/Health Canada evidence; time thresholds bounded by closed-door conditions, outage uncertainty, repeated opening and actual temperature.
- Cross-domain flood-food ↔ flood-cleanup relation is semantically justified.
- Human View/adversarial: PASS; no open substantive or Human View findings.

The associated `RELEASE/CLEAN-CHECKPOINT-P2-2026-10-06.md` is explicitly a **CLEAN CHECKPOINT CANDIDATE**, not final P2 CLEAN. It requires independent 3/3 validation of the checkpoint commit itself before next-priority work. A live status/run lookup for cited commits `3e2971a87119d746c277c6607875a56673dfe764` and `b7ccf467a3a1452c020be9b5dc414b2d4f702a79` returned no status records and no PR workflow runs in the connected GitHub view.

Decision for first edition: the four food slices are substantive candidates for the survival opening, but remain **HOLD — checkpoint validation evidence not independently retrievable in this review**. Do not redo the P2 audit; recover exact checkpoint validation evidence or validate a current reviewed commit.

### Broader encyclopedia breadth
The existing M4 gap map names infrastructure, construction, building science, agricultural engineering, food safety, health systems and cybersecurity as verification candidates, but it does not itself establish per-record acceptance. Those domains remain structural candidates only until exact record-level screening is completed.

## Net status after audit reuse
- Previously completed P1/P2 substantive and Human View reviews are reused, not restarted.
- Their content candidates are now explicitly identified for the first-edition opening section.
- No exact public INCLUDE is assigned yet because checkpoint validation evidence, release-specific rights, and editorial approval are not closed.
- The next technical task is checkpoint-evidence recovery/validation, not another M13 batch and not a repeated content audit.
