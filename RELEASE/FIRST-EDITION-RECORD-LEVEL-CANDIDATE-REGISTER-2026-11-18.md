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


### 6. Foundational and cross-domain domains — reuse of M3 completed review
The existing M3 work is reused as a bounded six-domain review, not restarted.

Reviewed domains:
- `fire-safety-basics`
- `shelter-basics`
- `water-resources-basics`
- `food-preservation-basics`
- `scientific-method-basics`
- `emergency-management-basics`

Evidence in repository:
- `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`: post-correction D1/D2 resolved; fire, shelter, food preservation and emergency management had no mandatory Claim rewrite; water resources and scientific method had identified substantive debts.
- `RELEASE/M3-DEBT-MAP-2026-10-08.md`: D1/D2 marked RESOLVED after controlled correction; D3–D8 evidence-independence tracks marked RESOLVED; R1–R6 Relations present and regression-covered.
- `RELEASE/M3-HUMAN-VIEW-AUDIT-2026-10-08.md`: PASS 6/6, no confirmed Human View debt.
- `RELEASE/M3-CLEAN-CHECKPOINT-2026-10-08.md`: records 4,674 Records / 583 Sources / 1,588 Evidence Use / 63 Relations and says substantive, evidence, Human View and Relation work is complete. It is explicitly **M3 CLEAN CANDIDATE** and requires independent exact-head 3/3 verification.

M3 candidate checkpoint blob commit: `bb3a348afc4ff3470ae16c5f90421a0796bc5403`. The connected GitHub status and PR-workflow lookup returned no statuses/runs for this commit. Therefore do not describe M3 as independently verified CLEAN.

First-edition use:
- `fire-safety-basics`, `shelter-basics`, `food-preservation-basics`, `emergency-management-basics`: **HOLD — candidate pending checkpoint validation and record-level rights/manifest review**. These are especially relevant to the survival opening and can provide explanatory foundation without inventing operational advice.
- `water-resources-basics`: **HOLD — same technical/governance gates**. Its post-correction content should be checked against its exact current Claim/EU versions and source locators before inclusion; do not reapply the old D1 finding.
- `scientific-method-basics`: **HOLD — same technical/governance gates**. It belongs in the broader Encyclopedia after the survival opening, not as a substitute for practical survival content.

M3's six candidate Relations are recorded as present and regression-covered by the post-correction debt map. Preserve the existing Relation records; do not create duplicate links. The Relation audit's original candidate list alone is not publication evidence.

### 7. Existing M4/M5/M6 wider-domain work
The current M4 gap map selects infrastructure, construction, building science, agricultural engineering, food safety, health systems and cybersecurity as verification candidates. This is a priority map, not record-level approval.
M3 provides stronger completed substantive/Human View evidence for the six domains above. For the wider domains, no exact first-edition INCLUDE is assigned in this register until the existing audit artifacts and current record dependency closure are checked. Do not infer readiness from a roadmap entry, slice count or published status.

## Revised first-edition curation posture
- Survival opening has already-audited content candidates across fire, shelter, food resilience, emergency management, alerts, lighting, tools and sanitation.
- The next layer can include foundational fire/shelter/water/food/scientific-method/emergency-management material where exact current records and technical validation are confirmed.
- The Encyclopedia remains broad: foundational science, engineering, living systems, human/social knowledge, history and culture are retained in the architecture. First edition selection is curated; it is not a claim that every slice is included.
- No exact public INCLUDE is assigned until exact-head release validation and owner governance gates are closed.


### 8. Emergency alert warning — exact-record spot check (not a repeated P1 audit)
This spot check reuses the closed P1 substantive/Human View review and tests the current exact dependency chain.

Records inspected:
- CLM-IPAWS-ALERT-CONTENT@1 → EU-IPAWS-ALERT-CONTENT@1 → SRC-PUBLIC-ALERT-GUIDANCE@1 (FEMA/IPAWS PDF).
- CLM-IPAWS-ALERT-ELEMENTS@1 → EU-IPAWS-ALERT-ELEMENTS@1 → SRC-PUBLIC-ALERT-GUIDANCE@1.
- CLM-ALERTS-ENABLE-RESPOND@1 → EU-ALERTS-ENABLE-RESPOND@1 → SRC-RED-CROSS-ALERTS-2026@1.
- CTX-IPAWS-ALERTS@1 and SCP-IPAWS-ALERTS@1 exist; both target CLM-IPAWS-ALERT-CONTENT@1. The Scope provenance lists both FEMA Claims, but its target_ref is only Claim CONTENT. Do not silently apply this Context/Scope to the Red Cross Claim.

Current exact-chain limitations:
1. EU-IPAWS-ALERT-CONTENT@1 and EU-IPAWS-ALERT-ELEMENTS@1 describe the source generically; neither identifies an exact PDF section/page or quoted/paraphrased passage.
2. EU-ALERTS-ENABLE-RESPOND@1 identifies the Red Cross recommendation generically; no exact page/section locator is recorded.
3. Source records identify canonical URLs, but the record-level evidence text does not yet provide pinpoint locators for the exact Claims.
4. The P1 audit reports direct support and Human View PASS, but the exact current EU records above do not carry the passage-level detail needed for a reproducible release review.

Decision: **HOLD — strong survival-opening candidate; prior P1 audit reused, but exact Evidence Use pinpointing and Claim-specific Context/Scope closure are incomplete for publication.** Do not rewrite canonical Claims or Evidence Use without a controlled correction decision. This is a narrowly scoped record-level gap, not a reason to repeat the P1 audit.

The alert slice remains an important early chapter of the opening survival section because it teaches the user to follow current official instructions rather than inventing evacuation/shelter decisions.


## 9. SI units — exact source-pinpoint and dependency recheck (2026-11-18)

This is a narrow release-screening check of the existing seven-record private-preview candidate. It does not repeat the substantive audit and does not modify canonical records.

Exact versions inspected on this branch:
- `CLM-SI-SEVEN-BASE@1`
- `EU-SI-SEVEN-BASE@2`
- `CLM-SI-DERIVED@1`
- `EU-SI-DERIVED@2`
- `SRC-NIST-SI-UNITS@1`
- `CTX-SI@1`
- `SCP-SI@1`

### Source passage verification

The canonical NIST page was checked directly on 2026-11-18:
- Source: NIST, “SI Units,” https://www.nist.gov/pml/owm/metric-si/si-units
- Claim A / EU A pinpoint: section **“Defining Constants”** (seven defining constants) together with **“Base and Derived Units”** (definitions of all seven base units use explicit-constant formulation; the seven base units are separately enumerated).
- Claim B / EU B pinpoint: section **“Base and Derived Units”** (seven base units define 22 derived units with special names and symbols; generic derived units such as area, volume, velocity and acceleration are distinct).
- NIST's wording directly supports the two current Claim statements. The Evidence Use boundary is correct: seven defining constants are not the same thing as seven base units; 22 refers to derived units with special names and symbols, not every possible derived unit.
- Independent terminology cross-check: NIST SP 330, Section 2, §2.3.4, “Derived units,” separately states that Table 4 lists 22 SI units with special names and that all other SI units are combinations of the 29 core units. This corroborates the boundary, but is not represented as a second independent authority because it is another NIST publication.

### Exact dependency and applicability check

- EU A references exactly Claim A v1 and Source v1.
- EU B references exactly Claim B v1 and Source v1.
- CTX-SI v1 and SCP-SI v1 both target **Claim A only**. Their provenance mentioning Claim B does not broaden their target. They must not be displayed as applying to Claim B.
- The private-preview builder enforces the exact seven-record ID/version set, both Claim/EU references, both EU/Source references, and the Claim-A-only Context/Scope targets. It also checks the NIST section names and the “22 is not the total number” boundary.
- No missing record-version edge was found within this seven-record set. The seven-record set is not permission to publish; it is the exact private-preview closure currently encoded.

### Updated screening decision

**Evidence pinpoint: PASS. Claim/source fit: PASS. Versioned Claim/EU/Source identity: PASS. Context/Scope boundary: PASS for Claim A and explicitly NOT applicable to Claim B.**

Overall candidate remains **HOLD**, not INCLUDE, because:
1. a release reader must visibly associate CTX-SI/SCP-SI with Claim A only and must not imply those records govern Claim B;
2. the exact release-facing Human View/editorial sign-off is not yet recorded;
3. item-level rights/attribution and the project owner's publication/licence decision remain open.

The existing private preview remains `preview_only`, offline and non-redistributable. Do not change its status based on this review. Do not alter canonical Claim, Evidence Use, Source, Context or Scope JSON. Do not repeat the SI substantive audit.


### 10. Emergency water — exact-record dependency and evidence-use spot check (2026-11-19)

This is a read-only inspection of the current canonical JSON records in `CONTENT/vertical-slices/water/records/`. It does not repeat the substantive water audit and does not modify canonical records.

Exact versions inspected (all `record_version: 1`, `type_version: 1.0`):
- `CLM-WATER-BOILING-EFFECTIVE@1`
- `EU-WATER-BOILING-EFFECTIVE@1` → `SRC-CDC-WATER-EMERGENCY-2024@1`
- `CLM-WATER-BOILING-TIME@1`
- `EU-WATER-BOILING-TIME@1` → `SRC-CDC-WATER-EMERGENCY-2024@1`
- `CLM-WATER-CHEMICAL-LIMIT@1`
- `EU-WATER-CHEMICAL-LIMIT@1` → `SRC-CDC-WATER-EMERGENCY-2024@1`
- `CLM-WATER-INDEPENDENT-CORROBORATION@1`
- `EU-WATER-INDEPENDENT-CORROBORATION@1` → `SRC-EPA-EMERGENCY-WATER-2026@1`
- `SRC-CDC-WATER-EMERGENCY-2024@1`
- `SRC-EPA-EMERGENCY-WATER-2026@1`

### What the exact records establish
- Four Claims have one-to-one Evidence Use links and explicit version-1 source references.
- Three Claims use CDC; a fourth Claim has a separate EPA source and EU record. The EPA record is a distinct agency source, not a second locator within the CDC record.
- Claim statements preserve important safety distinctions: pathogen reduction by boiling; the CDC time recommendation and its high-altitude condition; boiling does not neutralize fuel/chemical/radioactive contamination; and EPA corroboration is bounded to many pathogens and does not remove some chemical contaminants.
- The slice README expressly excludes universal purification schemes, reagent dosages, local water-quality claims and individualized medical decisions.

### Release-critical gaps found in the inspected records
1. All four EU records contain only a generic material description. None records a precise page section, heading, table, inspected passage or page locator. The source URLs identify official pages, but do not alone make the Claim-to-passage mapping reproducible.
2. The inspected `water/records/` directory contains exactly these ten files; no Context or Scope record is present in this slice directory. No claim-specific Context/Scope target is established by this exact ten-record set. Do not infer one from the README or another slice.
3. Claim B's specific time and altitude wording is a consequential operational threshold. It must remain visibly attributed to the cited CDC recommendation and its stated conditions; do not generalize it into a universal rule for all jurisdictions or circumstances.
4. The source records preserve external URLs rather than archived source snapshots. Availability and the exact current source passage should be rechecked at release freeze.
5. The presence of `publication_status: published` in the canonical JSON is not a first-edition publication decision. This register's decision vocabulary governs this curated release screen.

### Decision
**HOLD — all four Claims and their linked Evidence Use/Source records. No INCLUDE assigned.**

The source identities and versioned Claim→EU→Source edges are present, and the safety boundary is promising. However, the evidence pinpointing is not reproducible at passage level, the inspected set has no explicit Context/Scope records, and the high-consequence water-treatment topic requires qualified review of applicability and contaminant limits before operational guidance is released.

Required closure:
- inspect CDC and EPA source pages and record exact Claim-specific headings/passages in controlled Evidence Use corrections (without silently editing canonical records);
- establish explicit Context/Scope applicability boundaries for the exact Claims or formally document why a given Claim does not require them under the project's standard;
- independently verify the current source wording and conditions at release freeze;
- obtain qualified high-consequence review and complete release rights/attribution and reader checks.

No canonical JSON was changed. No prior water-treatment adjudication was recreated. This is a bounded exact-record screening result, not a replacement for the existing water-slice audit.


### 11. Chemical-water advisory — exact-record dependency and scope-boundary spot check (2026-11-19)

Read-only inspection of all nine JSON records in `CONTENT/vertical-slices/chemical-water-advisory/records/`. No canonical records were changed and no prior substantive audit was repeated.

Exact versions inspected (all `record_version: 1`, `type_version: 1.0`):
- `CLM-CHEM-WATER-NO-BOIL@1`
- `EU-CHEM-WATER-NO-BOIL@1` → `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024@1`
- `EU-CHEM-WATER-NO-BOIL-EPA@1` → `SRC-EPA-EMERGENCY-DISINFECTION-WATER@1`
- `CLM-CHEM-WATER-NO-DRINK@1`
- `EU-CHEM-WATER-NO-DRINK@1` → `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024@1`
- `CTX-CHEMICAL-WATER@1` → target is **CLM-CHEM-WATER-NO-DRINK@1 only**
- `SCP-CHEMICAL-WATER@1` → target is **CLM-CHEM-WATER-NO-DRINK@1 only**
- `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024@1`
- `SRC-EPA-EMERGENCY-DISINFECTION-WATER@1`

### Verified strengths
- The Claim that boiling does not make chemically contaminated water safe has two distinct agency evidence links, CDC and EPA.
- The “do not drink” Claim has its own CDC Evidence Use record and explicit Context and Scope records.
- The Context and Scope correctly target only the “do not drink” Claim. They must not be silently extended to the separate “no boil” Claim, even though both Claims appear in the same slice.
- Scope excludes DIY removal of particular chemicals, self-determination of safety without official data, and medical diagnosis. This is an appropriate conservative boundary.
- The README's stated policy—follow local authorities and use a safe alternative source; no DIY chemical removal recipes—is consistent with the record-level exclusions.

### Release-critical gaps
1. All three EU records use general prose descriptions. None identifies an exact CDC/EPA heading, section, passage, table or other pinpoint locator. The external URLs establish source identity, not reproducible Claim-specific passage fit.
2. The “no boil” Claim has no Context or Scope record in this nine-record slice. Existing CTX/SCP records explicitly target the “do not drink” Claim only. Do not treat their shared slice membership as applicability to the other Claim.
3. The “do not drink” Claim's statement specifically recommends commercially bottled water for drinking and food preparation. The evidence and Context/SCP should be checked to ensure that the exact official advisory category and local authority conditions are preserved in the reader-facing wording; do not generalize this into a universal response to every water advisory.
4. Both Source records point to external canonical pages rather than preserved snapshots. Recheck the exact page text and availability at release freeze.

### Decision
**HOLD — both Claims and all linked Evidence Use/Source/Context/Scope records. No INCLUDE assigned.**

The independent CDC/EPA support and Claim-specific CTX/SCP for the “do not drink” Claim are positive. The current EU locators are not passage-level, and Context/Scope are deliberately limited to one Claim. This is a high-consequence public-health topic and must not be promoted to release based on slice-level completeness or `publication_status: published`.

Required closure:
- add reproducible, Claim-specific CDC/EPA pinpoint locators through controlled review;
- independently decide whether the “no boil” Claim needs its own Context/Scope records or a documented standard-based reason for their absence;
- verify the exact advisory category and conditions for the bottled-water recommendation;
- obtain qualified review and complete project-level rights/attribution and release-reader checks.

This screening preserves the existing Claim boundaries and does not create or infer cross-Claim applicability.


### 12. Burn first aid — exact-record dependency and source-pinpoint spot check (2026-11-19)

Read-only inspection of the complete `burn-first-aid/records/` set on the PR #22 working branch. The existing P1 substantive, evidence-diversity and Human View audits are reused; no substantive adjudication is repeated and no canonical JSON is changed.

Exact inventory: **12 JSON records** (the README count is correct; the first partial retrieval had omitted the ABA Evidence Use record):
- Claims: `CLM-BURN-EMERGENCY@1`, `CLM-BURN-COOL-WATER@1`, `CLM-BURN-AVOID-HOME-REMEDIES@1`.
- Evidence Use: `EU-BURN-EMERGENCY@1` → `SRC-RED-CROSS-BURNS-2026@1`; `EU-BURN-EMERGENCY-ABA@1` → `SRC-AMERICAN-BURN-ASSOCIATION-2026@1`; `EU-BURN-COOL-WATER@1` → `SRC-RED-CROSS-BURNS-2026@1`; `EU-BURN-AVOID-HOME-REMEDIES@1` → `SRC-MAYO-BURNS-2026@1`.
- Sources: `SRC-RED-CROSS-BURNS-2026@1`, `SRC-AMERICAN-BURN-ASSOCIATION-2026@1`, `SRC-MAYO-BURNS-2026@1`.
- Applicability: `CTX-BURNS@1` and `SCP-BURNS@1`; both target **`CLM-BURN-COOL-WATER@1` only**.

### Direct source checks and pinpoints

The three external pages were checked directly on 2026-11-19:
- American Red Cross, “Burns: How To Help,” https://www.redcross.org/take-a-class/resources/learn-first-aid/burns — “Emergency Steps” (burn severity/escalation), “Giving First Aid Care — Cooling” (clean, cool running water; 5–20 minutes), “Chemical Burns,” “Electrical Burns,” and FAQ “Should I use ice to cool the burn?” / “Should I put butter or cream on a burn?”
- American Burn Association, “Burn First Aid,” https://www.ameriburn.org/patients/burn-first-aid — “Minor Burns,” “Serious Burns,” “First Aid for Minor Burns,” and “First Aid Facts: What NOT to Do.” It supports running-water cooling, avoiding ice, and urgent specialist/medical care for large, deep, face/hand/foot/genital, chemical, electrical and inhalation burns.
- Mayo Clinic, “Burns: First aid,” https://www.mayoclinic.org/first-aid/first-aid-burns/basics/art-20056649 — “When to get emergency help,” “Minor burns,” and “What to avoid.” The page is dated April 7, 2026. It supports the listed anatomic/severity/emergency boundaries and avoiding cold water, butter, toothpaste and oil.

### Exact-chain findings

1. The emergency Claim has two Evidence Use records, including the distinct ABA source. The initial apparent missing ABA link was a retrieval omission, not a repository defect.
2. The cooling Claim is supported by Red Cross. Its wording does not encode a cooling duration, which avoids collapsing the different source-specific recommendations (Red Cross 5–20 minutes; ABA at least 5 minutes; Mayo about 10 minutes) into a false universal threshold.
3. The home-remedies Claim links only to Mayo. Mayo supports butter, toothpaste and oil prohibitions, and says not to use cold water. The specific “ледяной водой” wording is most explicitly supported by the Red Cross/ABA pages, but neither is linked by this Claim's current EU. The current Evidence Use therefore does not document the strongest direct pinpoint for that exact ice-specific wording.
4. `CTX-BURNS@1` and `SCP-BURNS@1` target the cooling Claim only. Their presence in the slice does not establish applicability for the emergency Claim or home-remedies Claim.
5. The Source record `SRC-RED-CROSS-BURNS-2026@1` stores the older URL `https://www.redcross.org/take-a-class/first-aid/performing-first-aid/burns.html`, which did not resolve in this check. The currently accessible Red Cross article is at the `/resources/learn-first-aid/burns` path above. Treat this as a source-identity/locator maintenance issue requiring controlled source-record correction, not as permission to edit the canonical JSON in this screening pass.
6. All four Evidence Use records contain general descriptions rather than the exact page headings/sections above. The direct page inspection demonstrates plausible support, but the current EU records do not yet preserve reproducible passage-level locators.

### Decision

**HOLD — all three Claims and their complete linked dependency closure. No INCLUDE assigned.**

The prior P1 content-depth, evidence-diversity and Human View results remain reusable and are not reopened. The exact-record release screen remains blocked by generic EU descriptions, the stale Red Cross source URL, and the fact that Context/Scope explicitly cover only the cooling Claim. The ice-specific wording in the home-remedies Claim also needs a claim-to-source locator correction through the controlled process.

Required closure:
- correct/verify the Red Cross source locator through the authorized source-record correction process and preserve the prior version history;
- add exact Claim-specific headings/sections/passages to each EU record through controlled review;
- either link the existing ABA source to the ice-specific home-remedies Claim through a controlled Evidence Use decision, or establish that the current Mayo wording fully supports the exact statement;
- explicitly review Context/Scope applicability for the emergency and home-remedies Claims; do not silently broaden the existing targets;
- complete qualified medical review, item-level rights/attribution and release-facing reader checks.

No canonical JSON was changed. No P1 substantive or Human View audit was repeated.

### 13. Generator and carbon-monoxide safety — exact-record dependency and source-pinpoint spot check (2026-11-19)

Read-only inspection of the complete `generator-carbon-monoxide-safety/records/` set on the PR #22 working branch. The existing P1 substantive, evidence-diversity and Human View audits are reused; no substantive adjudication is repeated and no canonical JSON is changed.

Exact inventory: **12 JSON records**:
- Claims: `CLM-GENERATOR-OUTSIDE-20FT@1`, `CLM-GENERATOR-NO-INDOOR@1`, `CLM-GENERATOR-REFUEL-COOL@1`, `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`.
- Evidence Use: `EU-GENERATOR-OUTSIDE-20FT@1` → `SRC-CDC-GENERATOR-CO-2026@1`; `EU-GENERATOR-NO-INDOOR@1` → `SRC-CDC-GENERATOR-CO-2026@1`; `EU-GENERATOR-REFUEL-COOL@1` → `SRC-CPSC-GENERATOR-2026@1`; `EU-GENERATOR-CO-ALARM-EMERGENCY@1` → `SRC-CDC-GENERATOR-CO-2026@1`.
- Sources: `SRC-CDC-GENERATOR-CO-2026@1`, `SRC-CPSC-GENERATOR-2026@1`.
- Applicability: `CTX-GENERATOR-CO@1` and `SCP-GENERATOR-CO@1`; both target **`CLM-GENERATOR-OUTSIDE-20FT@1` only**.

### Direct source checks and pinpoints

The source pages were checked directly on 2026-11-19:
- CDC, “What to Do to Protect Yourself During a Power Outage,” https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html (page dated August 26, 2026): section “Carbon monoxide poisoning,” including the prohibition on use inside the home/basement/garage or within 20 feet of a window, door or vent; battery-powered or backup CO detector recommendation; symptoms and emergency-response text.
- U.S. CPSC, “CPSC Warns of Generator, Carbon Monoxide and Fire Hazards Ahead of Hurricane Season,” https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Warns-of-Generator-Carbon-Monoxide-and-Fire-Hazards-Ahead-of-Hurricane-Season (May 27, 2026): “Loss of Power—Using a Generator Safely” (outdoors, at least 20 feet, exhaust directed away from openings; never indoors) and “Check Carbon Monoxide and Smoke Alarms” (install/test alarms; leave immediately and call 911 if an alarm sounds).
- A separate CPSC “Carbon-Monoxide-Questions-and-Answers” page is linked in the neighboring heating-safety slice, not in this generator slice's Claim dependency closure: https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Carbon-Monoxide-Questions-and-Answers. Its alarm section explicitly says not to re-enter until emergency responders give permission. This external page is useful for locating the missing support, but the neighboring slice's Source/Evidence Use and a cross-slice Relation do **not** become dependencies of a generator Claim by proximity.

### Exact-chain findings

1. The outdoor/20-foot Claim and no-indoor Claim have direct CDC Evidence Use links. CDC's current page explicitly supports the 20-foot distance and the no-indoor boundary, including the warning that opening doors/windows does not make enclosed-space operation safe.
2. CPSC's 2026 release independently corroborates outdoor operation at least 20 feet away and exhaust directed away from windows, doors and vents. The existing generator slice has a CPSC Source record, but no CPSC Evidence Use link for either of those two Claims. The current CDC links remain direct; the CPSC corroboration must not be described as part of the recorded Claim dependency closure until explicitly linked.
3. The refuelling Claim is linked to the 2026 CPSC press release, but the inspected page does not state the specific “turn off and let the engine cool before refuelling” instruction. Its relevant section covers placement, operation and alarms, not this refuelling condition. The current EU description is generic and does not identify a supporting passage. This is a source-fit gap, not a minor locator omission.
4. The emergency Claim links only to the CDC power-outage page. That page supports CO hazards, symptoms, use of a detector and urgent response, but the inspected text does not provide the complete alarm sequence or the explicit “do not re-enter until responders permit it” boundary stated in the Claim. The separate CPSC Q&A page does support that boundary, but it is not currently linked to this Claim by a Source/Evidence Use pair in this slice. The existing cross-slice Relation `REL-CROSS-CO-EMERGENCY-ESCALATION@1` is navigation/semantic linkage, not evidence.
5. `CTX-GENERATOR-CO@1` and `SCP-GENERATOR-CO@1` target the outdoor/20-foot Claim only. Their provenance lists both outdoor and no-indoor Claims, but the target_ref is narrower. They do not automatically apply to no-indoor, refuelling or emergency Claims.
6. The README lists a battery-powered or backup CO detector as a slice boundary, but there is no separate Claim for that recommendation in the 12-record inventory. Do not present this README bullet as an independently screened Claim.
7. All four Evidence Use records are descriptive summaries, not passage-level locators. The current external source pages were reachable, but the canonical EU records do not preserve the exact sections/passages required for a reproducible release review.
8. The CPSC 2026 release and CDC page are external live sources, not preserved snapshots. Recheck current wording and source availability at release freeze.

### Decision

**HOLD — all four Claims and their linked Evidence Use/Source/Context/Scope records. No INCLUDE assigned.**

The prior P1 substantive, evidence-diversity and Human View work is reused and not repeated. The outdoor/20-foot and no-indoor statements have direct current CDC support, but their recorded EU locators remain generic and Context/Scope are narrower than the full slice. The refuelling Claim has an apparent source-fit gap. The emergency Claim's no-re-entry condition is not fully supported by its current linked CDC source; the direct CPSC Q&A evidence located in the neighboring slice is not a substitute for an explicit dependency link.

Required closure:
- add precise CDC headings/passages to the three CDC Evidence Use records through controlled review;
- identify a direct source passage for the refuelling/cool-down Claim, or retain HOLD until an appropriate source is added through authorized record correction;
- establish an explicit direct Evidence Use dependency for the generator emergency/no-re-entry boundary if that wording is retained; do not treat a Relation as evidence;
- review whether Context/Scope records are required for no-indoor, refuelling and emergency Claims, or document a standard-based reason for their absence;
- decide whether the README's detector recommendation is merely contextual or should have its own versioned Claim/Evidence Use pair;
- complete qualified safety review, item-level rights/attribution and release-reader checks.

No canonical JSON was changed. No P1 substantive or Human View audit was repeated.


### 14. Disaster response basics — exact-record dependency and source-pinpoint spot check (2026-11-19)

Read-only inspection of all 12 JSON records in `CONTENT/vertical-slices/disaster-response-basics/records/` on the PR #22 working branch. The prior P3 substantive, evidence-independence, Human View/adversarial and correction work is reused; this is not a restart of P3 and no canonical JSON is changed.

Exact inventory (all inspected records are `record_version: 1`, `type_version: 1.0`):
- Claims:
  - `CLM-DISASTER_RESPONSE_BASICS-A@1`
  - `CLM-DISASTER_RESPONSE_BASICS-B@1`
  - `CLM-DISASTER_RESPONSE_BASICS-C@1`
  - `CLM-DISASTER_RESPONSE_FEMA_A@1`
- Evidence Use:
  - `EU-DISASTER_RESPONSE_BASICS-A@1` → `SRC-DISASTER_RESPONSE_BASICS@1`
  - `EU-DISASTER_RESPONSE_BASICS-B@1` → `SRC-DISASTER_RESPONSE_BASICS@1`
  - `EU-DISASTER_RESPONSE_BASICS-C@1` → `SRC-DISASTER_RESPONSE_BASICS@1`
  - `EU-DISASTER_RESPONSE_FEMA-A@1` → `SRC-FEMA-RESPONSE-GLOSSARY@1`
- Sources:
  - `SRC-DISASTER_RESPONSE_BASICS@1` — UNDRR, “Definition: Response”
  - `SRC-FEMA-RESPONSE-GLOSSARY@1` — FEMA Emergency Management Institute, “Glossary”
- Applicability:
  - `CTX-DISASTER_RESPONSE_BASICS@1` → **Claim A only**
  - `SCP-DISASTER_RESPONSE_BASICS@1` → **Claim A only**

Inventory reconciles exactly to the slice README and its dedicated regression test: 4 Claims + 4 Evidence Use + 2 Sources + 1 Context + 1 Scope = 12 Records. The regression test checks the 12-record topology, two distinct source URLs, Claim provenance and Claim→Evidence Use→Source identity links.

### Reused P3 work — do not repeat

The following existing artifacts were inspected:
- `RELEASE/P3-SANITATION-HYGIENE-CORRECTION-AUDIT-2026-10-06.md`
- `RELEASE/P3-SANITATION-HYGIENE-UNIFIED-DEBT-MAP-2026-10-06.md`
- `RELEASE/CLEAN-CHECKPOINT-P3-2026-10-06.md`
- `REFERENCE/tests/test_content_disaster_response_basics_vertical_slice.py`

The prior duplicate UNDRR representation was consolidated to one canonical UNDRR Source; FEMA is the distinct institutional corroboration. P3 reports the source-duplication, evidence-independence, documentation, Human View and cross-slice findings closed, with the target slice included in the completed P3 substantive re-audit. No new duplicate-source finding is raised here.

The P3 checkpoint records technical PASS runs on its cited commits, but its own text still requires independent 3/3 validation of the checkpoint commit. A fresh connected GitHub status/workflow lookup for checkpoint commit `d8600b53c225fefb7c1beae924a85556ceb1d4d6` returned no status records and no PR workflow runs. Therefore this first-edition screen reuses the P3 substantive result but does **not** assert independently retrievable checkpoint validation.

### Direct source and passage checks

The canonical external pages were checked on 2026-11-19:
- UNDRR, “Definition: Response,” https://www.undrr.org/terminology/response
  - Definition paragraph: actions taken directly before, during or immediately after a disaster to save lives, reduce health impacts, ensure public safety and meet basic subsistence needs.
  - Annotation paragraph beginning “Disaster response is predominantly focused on immediate and short-term needs”: response relies on disaster-risk-informed preparedness and development of response capacities.
  - Final annotation paragraph: the division between response and recovery is not clear-cut; temporary housing and water supply actions may extend into recovery.
- FEMA Emergency Management Institute, “Glossary,” https://training.fema.gov/is/course/glossary.aspx
  - Glossary entry **“Response”**: capabilities necessary to save lives, protect property and the environment, and meet basic human needs after an incident has occurred.

These passages support the substance and intended distinctions of the four Claims. The FEMA wording is a separate institutional definition, not an independent duplicate of the UNDRR URL. UNDRR is the single canonical source for Claims A/B/C; its annotation, not only the short definition sentence, is necessary for the support of Claims B and C.

### Exact-chain and applicability findings

1. Claim A is directly represented by the UNDRR definition paragraph. Its “directly before, during or immediately after” wording and life/public-safety/basic-needs purposes align with the source.
2. Claim B is supported by the UNDRR annotation on preparedness measures and response capacities. The current Evidence Use does not identify this annotation; a locator to the short definition paragraph alone would be insufficient.
3. Claim C is supported by the final UNDRR annotation paragraph on the indistinct response/recovery boundary and examples of actions extending into recovery. Again, the current Evidence Use does not identify this paragraph.
4. The FEMA Claim is directly supported by the FEMA Glossary entry “Response.” Its scope is narrower in temporal wording (“after an incident has occurred”) than UNDRR's definition, which includes directly-before actions. Keep the two definitions attributed to their own institutions; do not blend them into one universal definition.
5. All four Evidence Use records currently contain general descriptions rather than pinpoint locators. The current direct source checks establish plausible passage fit, but the canonical EU records do not preserve the exact definition/annotation/entry needed for reproducible release review.
6. Context and Scope target Claim A only. They must not be silently applied to Claims B, C or the FEMA Claim. The claims are descriptive and relatively low operational risk, but exact applicability must still be represented accurately in the reader and in the release dependency manifest.
7. The slice README correctly states the descriptive boundary: application-specific decisions require context, applicable requirements, validation and professional judgment. Do not turn these definition Claims into operational instructions or assume they replace local emergency plans, incident command, or jurisdiction-specific response doctrine.
8. The slice has no separate Relation records. No cross-slice relation is required merely to make this definition slice appear connected; the existing response/logistics and emergency-alert pathways must be grounded in their own records.

### Decision

**HOLD — all four Claims and their complete linked dependency closure. No INCLUDE assigned.**

P3 substantive and Human View work is reused, not repeated. The exact inventory, source identities, two distinct institutional URLs and Claim→Evidence Use→Source edges are present, and the direct passages support the four Claims. The release blocker is that the canonical Evidence Use records still lack reproducible paragraph/entry locators, and the current Context/Scope records explicitly cover Claim A only. The checkpoint's own independent 3/3 status is also not independently retrievable in the current connected GitHub status view.

Required closure:
- through controlled Evidence Use correction, identify the UNDRR definition paragraph for Claim A, the preparedness/capacities annotation paragraph for Claim B, and the response/recovery annotation paragraph for Claim C;
- identify the FEMA Glossary “Response” entry for the FEMA Claim;
- explicitly decide and record applicability Context/Scope for Claims B, C and the FEMA Claim, or document the standard-based reason they do not need separate records; never broaden the existing Claim-A targets by inference;
- recover verifiable exact-checkpoint 3/3 evidence or validate the current reviewed checkpoint through the authorized technical process;
- complete release rights/attribution and reader-facing review.

No canonical JSON was changed. No P3 substantive, Human View or historical M13 audit was repeated.


### 15. Disaster response logistics basics — exact-record dependency and source-identity spot check (2026-11-19)

Read-only inspection of all 13 JSON records in `CONTENT/vertical-slices/disaster-response-logistics-basics/records/` on the PR #22 working branch. The prior P3/P5 substantive, evidence-independence, Human View and correction work is reused; no historical audit is repeated and no canonical JSON is changed.

Exact inventory (all records inspected at `record_version: 1`, `type_version: 1.0`):
- Claims:
  - `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1`
  - `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1`
  - `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1`
- Evidence Use:
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` → `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1`
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` → `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1`
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` → `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1`
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A_FEMA@1` → `SRC-FEMA-DISASTER-LOGISTICS-2026@1`
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_B_FEMA@1` → `SRC-FEMA-DISASTER-LOGISTICS-2026@1`
  - `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_C_FEMA@1` → `SRC-FEMA-DISASTER-LOGISTICS-2026@1`
- Sources:
  - `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` — labeled “UN OCHA — Humanitarian coordination”
  - `SRC-FEMA-DISASTER-LOGISTICS-2026@1` — FEMA EMI, “Introduction to Disaster Logistics and Supply Chain Management” (IS-52)
- Applicability:
  - `CTX_DISASTER_RESPONSE_LOGISTICS_BASICS@1` → **Claim A only**
  - `SCP_DISASTER_RESPONSE_LOGISTICS_BASICS@1` → **Claim A only**

Inventory reconciles to the README and dedicated regression contract: 13 Records = 2 Sources + 3 Claims + 6 Evidence Use + Context + Scope. The regression validates schema and semantic structure, all three Claim provenance paths, and at least one valid Evidence Use path per Claim. It does not validate passage-level source fit or whether the Source identity/URL is sufficiently specific.

### Reused prior audit work

The following existing reports were inspected:
- `RELEASE/P5-DISASTER-RECOVERY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`
- `RELEASE/P5-DISASTER-RECOVERY-UNIFIED-DEBT-MAP-2026-10-06.md`

P5 explicitly records that FEMA's independent evidence line was extended to all three Claims, that the slice remains descriptive and requires current situational information and coordination, and that no unsupported operational instructions were introduced. P5 substantive, evidence-independence and Human View findings are reported as zero remaining. Reuse this work; do not redo the P5 content audit.

The P5 re-audit states that P5 CLEAN was not yet declared and required fresh Reference + Release Gate + Offline validation, followed by a dedicated checkpoint and independent validation. No P5 checkpoint artifact or exact checkpoint validation evidence was independently established in this spot check. Do not label this slice's first-edition release gate technically verified solely from the substantive re-audit.

### Direct source checks and source-identity issue

The external source pages were checked on 2026-11-19:
- FEMA EMI, “Introduction to Disaster Logistics and Supply Chain Management” (IS-52), https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-52&lang=en
  - Course overview: disaster logistics and supply-chain management, emergency-response challenges.
  - Course objectives: disaster-specific supply-chain components and interdependencies; risks and vulnerabilities; resilience strategies; governance and public-private collaboration; systems thinking; rapid sourcing, transport rerouting and real-time situational awareness.
- The current Source record `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` points only to the OCHA homepage, https://www.unocha.org/, while identifying the source as “UN OCHA — Humanitarian coordination.” This is not a pinpoint to a logistics document, page or passage and does not make the asserted logistics support reproducible.
- A relevant operational source was located at the Logistics Cluster website, “The Logistics Cluster,” https://logcluster.org/en/who-we-are/cluster-approach/logistics-cluster. It describes coordination, information management and access to common logistics services. The page states that the Cluster Approach brings together humanitarian organisations, UN agencies, NGOs and other stakeholders; it also identifies WFP as the global lead agency and host of the Logistics Cluster team. This is relevant evidence, but it is **not interchangeable with an OCHA source identity**. Do not silently relabel the current OCHA Source as WFP/Logistics Cluster or substitute the new URL without a controlled Source correction/version decision.

### Claim-specific fit and boundaries

1. Claim A states that disaster-response logistics coordinates movement/management of people, supplies, equipment and information. FEMA IS-52 supports disaster-specific logistics components, supply chains and information/situational awareness; the Logistics Cluster page supports coordination, information management and common services. However, the current OCHA Source URL is only the institutional homepage, and the current EU records do not identify the exact FEMA course objective or relevant Logistics Cluster section.
2. Claim B states that decisions are constrained by needs, access, infrastructure, time and available resources. FEMA IS-52 supports risk/vulnerability, interdependencies, resilience and real-time situational awareness; the Logistics Cluster material describes access constraints, gaps/bottlenecks and service availability. The current Evidence Use descriptions do not identify the passages that support each enumerated constraint. Do not infer that every listed constraint is supported by a generic homepage.
3. Claim C states that effective response logistics requires coordination among organizations and visibility of resources/requirements. FEMA IS-52 supports governance frameworks and public-private collaboration; the Logistics Cluster page directly describes multi-actor coordination and information management. The current OCHA URL and EU descriptions do not preserve these pinpoint mappings.
4. Each Claim has both an OCHA-labeled and a FEMA Evidence Use record. The FEMA line is a distinct institution and is correctly represented for all three Claims after the P5 correction. However, the first line's exact source identity is unresolved: an OCHA homepage is not a precise logistics evidence locator, and the directly relevant Logistics Cluster page identifies WFP as global lead agency.
5. All six Evidence Use records use generic descriptions, not passage-level locators. The current Source→EU→Claim identity edges exist and version-match, but source passage fit cannot be reproduced from the canonical EU records.
6. Context and Scope target Claim A only. They do not automatically apply to Claims B and C. The README's boundary—operational decisions require current situational information, applicable authorities, coordination and professional judgment—is valuable but does not broaden the exact Context/Scope target references.
7. The Claims are descriptive, not operational dispatch instructions. Do not use them to direct cargo priorities, convoy routes, border crossings, procurement, access negotiations, resource allocation or live incident command. Such decisions depend on current local authority, security, access, capacity and humanitarian coordination conditions.

### Decision

**HOLD — all three Claims and their complete linked dependency closure. No INCLUDE assigned.**

The P5 substantive/evidence/Human View work is reused. The exact 13-record topology, versioned Claim→Evidence Use→Source edges, and FEMA's independent line to all three Claims are present. The first-edition blocker is a material source-identity/locator problem in the OCHA line (homepage URL rather than an identifiable logistics source), combined with generic Evidence Use descriptions and Claim-A-only Context/Scope targets.

Required closure:
- resolve the OCHA Source identity through controlled review: identify a specific OCHA publication/page that directly supports the intended claims, or authorize a new/updated Source for the relevant WFP-led Logistics Cluster material; do not silently change the existing Source identity;
- add exact FEMA IS-52 course-objective/overview locators to the three FEMA Evidence Use records;
- add exact section/paragraph locators for the independently selected coordination/logistics source to each corresponding Evidence Use record;
- ensure each Claim's specific wording (including people, supplies, equipment, information; needs/access/infrastructure/time/resources; coordination/resource visibility) is supported by the passages actually cited;
- explicitly decide Context/Scope applicability for Claims B and C or document a standard-based reason separate records are unnecessary; do not broaden Claim A's targets by inference;
- recover/complete the applicable P5 technical checkpoint validation evidence, and complete rights/attribution and reader-facing release review.

No canonical JSON was changed. No P3/P5 substantive, Human View or historical M13 audit was repeated.


### 16. Emergency management basics — exact-record and source-fit screen (2026-11-19)

This screen reuses the M3 substantive, evidence-independence, Human View and Relation work. It does not restart M3 and does not change canonical JSON.

Exact inventory inspected on this branch (all records `record_version: 1`, `type_version: 1.0`):
- Claims: `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1`, `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1`, `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1`.
- Evidence Use:
  - `EU-EMERGENCY_MANAGEMENT_BASICS-A@1` → `SRC-EMERGENCY_MANAGEMENT_BASICS@1`
  - `EU-EMERGENCY_MANAGEMENT_BASICS-B@1` → `SRC-EMERGENCY_MANAGEMENT_BASICS@1`
  - `EU-EMERGENCY_MANAGEMENT_BASICS-C@1` → `SRC-EMERGENCY_MANAGEMENT_BASICS@1`
  - `EU_EMERGENCY_MANAGEMENT_BASICS_UNDRR@1` → `SRC_UNDRR_EMERGENCY_MANAGEMENT@1`, targeting Claim A only.
- Sources:
  - `SRC-EMERGENCY_MANAGEMENT_BASICS@1` — FEMA IS-230.E, Fundamentals of Emergency Management.
  - `SRC_UNDRR_EMERGENCY_MANAGEMENT@1` — UNDRR, “Definition: Disaster management”.
- Applicability:
  - `CTX-EMERGENCY_MANAGEMENT_BASICS@1` → Claim A only.
  - `SCP-EMERGENCY_MANAGEMENT_BASICS@1` → Claim A only.
- Relation: `REL_M3_EMERGENCY_INFRASTRUCTURE@1`, linking Claim A to `CLM-INFRASTRUCTURE_RESILIENCE-A@1` under `CTX-CROSS-SLICE-LINKAGE@1`.

Inventory: 12 records = 2 Sources + 3 Claims + 4 Evidence Use + Context + Scope + 1 Relation. The dedicated regression checks the 12-record count, two Sources, provenance and at least one valid Evidence Use per Claim. It does not test passage-level locators or prove that each listed phrase is supported by the source passage.

#### Reused audit evidence

- `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`: emergency-management-basics PASS; no mandatory Claim rewrite; existing Claims cover preparation/response/coordination/recovery, multi-actor roles and jurisdiction/event/institution dependence.
- `RELEASE/M3-DEBT-MAP-2026-10-08.md`: D8 independent UNDRR evidence marked RESOLVED; R1–R6 marked present and regression-covered.
- `RELEASE/M3-HUMAN-VIEW-AUDIT-2026-10-08.md`: Human View PASS 6/6, no confirmed debt.
- `RELEASE/M3-CLEAN-CHECKPOINT-2026-10-08.md`: M3 CLEAN CANDIDATE, not final closure; requires independent exact-head 3/3 verification. The checkpoint SHA `bb3a348afc4ff3470ae16c5f90421a0796bc5403` had no independently retrievable status/workflow evidence in the earlier live check. Do not repeat the M3 content audit or call M3 technically closed.

#### Direct source passage checks

- FEMA IS-230.E course overview:
  - course overview and objectives, especially “principles and authorities”, “different partners” and “roles of each partner” (official page lines 40–52);
  - resource planning/management/coordination and emergency/day-to-day functions are explicit course objectives.
  - URL: https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-230.e&lang=en
- UNDRR “Definition: Disaster management”:
  - definition: organization, planning and application of measures preparing for, responding to and recovering from disasters;
  - annotation distinguishes emergency management usage and disaster-management context.
  - URL: https://www.undrr.org/terminology/disaster-management

#### Claim-level fit and boundary findings

1. Claim A is substantially supported across the two sources: FEMA course objectives include response resource planning/coordination and emergency-management functions; UNDRR explicitly covers preparation, response and recovery. The existing UNDRR Evidence Use is attached only to Claim A, correctly. However both Evidence Use descriptions remain generic and do not preserve the exact passages.
2. Claim B says effective management “requires” distribution of roles among state, private and public/community actors. FEMA's overview says partners contribute in a community and describes roles of each partner, but the overview does not itself enumerate the precise state/private/community categories or establish the stronger “requires” wording. The detailed course may contain this material, but no lesson/module locator is recorded in the current EU. Claim B therefore has a source-fit/pinpoint gap, not a demonstrated falsehood.
3. Claim C says specific powers, plans and procedures are determined by jurisdiction, event type and active management systems. FEMA's overview names principles and authorities, community partners and emergency-operations plans; UNDRR distinguishes disaster management from some emergency contexts. The exact three-part formulation is not pinpointed in the current EU. Avoid presenting the sentence as a universal legal rule.
4. Context and Scope target Claim A only. They must not be silently inherited by Claims B/C.
5. The existing M3 Relation is retained; no duplicate Relation is justified. Its presence does not substitute for evidence or extend Context/Scope.
6. This is descriptive foundational material, not a live incident command plan. The existing Scope appropriately excludes local plans, official warnings and professional instructions.

#### Decision

**HOLD — all three Claims and their exact dependency closures. No INCLUDE assigned.**

The prior M3 content/Human View/Relation findings are reused. The blockers are the generic Evidence Use descriptions, incomplete pinpointing of the exact FEMA lesson passages for Claims B/C, and Claim-A-only Context/Scope applicability. The source identity and version edges are structurally sound.

Required closure: add reproducible FEMA course-objective/lesson locators and the UNDRR definition/annotation locator to the corresponding EU records through a controlled correction/version process; decide whether Claims B/C need their own Context/Scope or a documented standards-based applicability rationale; then recover/complete M3 exact-head technical validation and project rights/editorial gates.

No canonical JSON changed in this screen.

### 17. Disaster risk reduction basics — exact-record screen with source-term reconciliation (2026-11-19)

This screen reuses the P5 substantive, evidence-independence and Human View re-audit. It does not repeat the P5 content audit and does not modify canonical records.

Exact inventory inspected (all records `record_version: 1`, `type_version: 1.0`):
- Claims: `CLM-DISASTER_RISK_REDUCTION_BASICS-A@1`, `CLM-DISASTER_RISK_REDUCTION_BASICS-B@1`, `CLM-DISASTER_RISK_REDUCTION_BASICS-C@1`, `CLM-DISASTER_RISK_REDUCTION_BASICS-D@1`.
- Evidence Use:
  - `EU-DISASTER_RISK_REDUCTION_BASICS-A@1` → `SRC-DISASTER_RISK_REDUCTION_BASICS@1`
  - `EU-DISASTER_RISK_REDUCTION_BASICS-B@1` → `SRC-DISASTER_RISK_REDUCTION_BASICS@1`
  - `EU-DISASTER_RISK_REDUCTION_BASICS-C@1` → `SRC-DISASTER_RISK_REDUCTION_BASICS@1`
  - `EU-DISASTER_RISK_REDUCTION_BASICS-D@1` → `SRC-FEMA-HAZARD-MITIGATION-2026@1`
- Sources:
  - `SRC-DISASTER_RISK_REDUCTION_BASICS@1` — UNDRR Sendai Framework overview, URI currently `https://www.undrr.org/implementing-sendai-framework/what-sendai-framework`.
  - `SRC-FEMA-HAZARD-MITIGATION-2026@1` — FEMA Hazard Mitigation Planning page, URI currently `https://www.fema.gov/emergency-managers/risk-management/hazard-mitigation-planning`.
- Applicability: `CTX-DISASTER_RISK_REDUCTION_BASICS@1` and `SCP-DISASTER_RISK_REDUCTION_BASICS@1` target Claim A only.

Inventory: 12 records = 2 Sources + 4 Claims + 4 Evidence Use + Context + Scope. The dedicated regression checks count, two distinct Source IDs, provenance and valid Claim→EU→Source edges. It does not validate exact source passages or conceptual equivalence among different risk vocabularies.

#### Reused audit evidence

- `RELEASE/P5-DISASTER-RECOVERY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: risk-reduction slice included in the P5 re-audit; substantive findings 0, evidence-independence findings 0 and Human View/adversarial findings 0.
- `RELEASE/P5-DISASTER-RECOVERY-UNIFIED-DEBT-MAP-2026-10-06.md`: P5-EVIDENCE-002 marked CLOSED after adding independent FEMA hazard-mitigation evidence and a source-bounded planning Claim.
- P5 CLEAN was not declared. The P5 re-audit requires fresh Reference + Release Gate + Offline validation, then a dedicated checkpoint and independent exact-head validation. Do not represent P5 as technically closed based on the substantive report.

#### Direct source passage checks and locator correction

- UNDRR “Definition: Disaster risk reduction” directly states prevention of new risk, reduction of existing risk and management of residual risk; annotation describes strategies, goals, objectives, targets, indicators and time frames. This is the direct terminology page for Claim A:
  https://www.undrr.org/terminology/disaster-risk-reduction
- UNDRR “Definition: Disaster risk” defines risk as potential losses determined probabilistically as a function of hazard, exposure, vulnerability and capacity; its annotation explains contextual and social/economic factors:
  https://www.undrr.org/terminology/disaster-risk
- UNDRR “Definition: Disaster risk governance” describes institutions, mechanisms, policy/legal frameworks and arrangements that guide, coordinate and oversee DRR:
  https://www.undrr.org/terminology/disaster-risk-governance
- FEMA 2025 Local Mitigation Planning Handbook:
  - Task 4, “Conduct a Risk Assessment”, pp. 42–44 / PDF text lines 1853–1946: risk, impacts, vulnerabilities, hazards, assets, local knowledge and jurisdiction-specific differences.
  - Task 1/2 and Task 4: planning process depends on data, technology, resources, local knowledge and participating jurisdictions.
  - Task 6, “Develop a Mitigation Strategy”, begins p. 82; mitigation actions address vulnerabilities identified in the local plan.
  - URL: https://www.fema.gov/sites/default/files/documents/fema_hmd_2025-local-mitigation-planning-handbook_06122025.pdf
- The current FEMA Source page URL returned HTTP 403 in the live fetch, while the official 2025 handbook PDF is directly readable. A controlled source-locator update or a versioned Source record pointing to the handbook is needed for reproducibility.

#### Claim-level fit and boundary findings

1. Claim A closely matches the UNDRR DRR definition, but the current Source URI is the general Sendai Framework overview, not the terminology entry that supplies the exact wording. The right supporting passage exists and is public; the canonical Source/EU chain needs a precise locator/version decision.
2. Claim B combines terms that must not be treated as interchangeable without explanation. UNDRR's formal risk formulation uses hazard, **exposure**, vulnerability and capacity. The Claim currently uses hazard, “impact”, vulnerability and “potential/capacity” wording. FEMA's local planning handbook separately describes hazards, impacts, assets and vulnerabilities. The current wording may blend the UNDRR risk model with FEMA planning vocabulary; the distinction between exposure, impact and capacity must be explicitly adjudicated before release. The existing EU is generic and does not identify the exact UNDRR or FEMA terminology passages.
3. Claim C is directionally consistent with FEMA's local planning handbook: approaches depend on data, technology and available resources; local knowledge and stakeholder input matter; jurisdictions have distinct hazards and vulnerabilities. But the exact phrase “measures depend on hazard, territory, vulnerability, resources and institutional context” is not pinpointed in the current EU. The current Source page also needs a reproducible locator.
4. Claim D is an English-language, FEMA-specific statement: FEMA describes hazard-mitigation planning as identifying hazards, vulnerabilities and risks and developing long-term strategies to reduce future losses. It is directly supported by the 2025 handbook's Task 4 risk assessment and Task 6 mitigation strategy. It is not a substitute for UNDRR's broader international terminology. The language shift from the three Russian Claims should be reviewed for edition consistency.
5. Context and Scope target Claim A only; they do not automatically extend to Claims B/C/D. The README boundary is descriptive and correctly states that actual priorities/measures depend on hazard, vulnerability, jurisdiction, resources and current planning requirements.
6. The slice is about risk reduction and planning, not incident response or disaster management as a whole. Do not convert mitigation planning guidance into universal prescriptions or local engineering/regulatory advice.

#### Decision

**HOLD — all four Claims and their exact dependency closures. No INCLUDE assigned.**

P5 substantive/evidence/Human View work is reused. The material is substantively valuable and the direct official passages exist, but the current EU descriptions are generic, the UNDRR Source points to a broad Sendai overview rather than the exact terminology entries, the FEMA Source page was not reproducibly fetchable in the live check, and Claim B's risk vocabulary needs explicit reconciliation. Claim D also needs Russian-language editorial consistency review. Context/Scope apply to Claim A only.

Required closure: controlled locator/source correction for UNDRR DRR/risk terminology and FEMA's 2025 Local Mitigation Planning Handbook; explicit adjudication of exposure vs impact vs capacity in Claim B; exact locators per EU; decide Context/Scope applicability for B/C/D; complete the P5 technical checkpoint and project-level rights/editorial gates.

No canonical JSON changed in this screen.

### 18. Humanitarian logistics basics — exact-record screen and direct WFP passage verification (2026-11-19)

This is an exact-record first-edition screen of the R22 controlled slice. No substantive R22 audit was found in the inspected release artifacts; the R22 gap map is a scope/DoD document, not an approval. No canonical record is changed.

Exact inventory inspected (all records `record_version: 1`, `type_version: 1.0`):
- Claims: `CLM-HUMANITARIAN_LOGISTICS_BASICS-A@1`, `CLM-HUMANITARIAN_LOGISTICS_BASICS-B@1`, `CLM-HUMANITARIAN_LOGISTICS_BASICS-C@1`.
- Evidence Use:
  - `EU-HUMANITARIAN_LOGISTICS_BASICS-A@1` → `SRC-HUMANITARIAN_LOGISTICS_BASICS@1`
  - `EU-HUMANITARIAN_LOGISTICS_BASICS-B@1` → `SRC-HUMANITARIAN_LOGISTICS_BASICS@1`
  - `EU-HUMANITARIAN_LOGISTICS_BASICS-C@1` → `SRC-HUMANITARIAN_LOGISTICS_BASICS@1`
- Source: `SRC-HUMANITARIAN_LOGISTICS_BASICS@1` — WFP Logistics Cluster, `https://www.wfp.org/logistics-cluster`.
- Applicability: `CTX-HUMANITARIAN_LOGISTICS_BASICS@1` and `SCP-HUMANITARIAN_LOGISTICS_BASICS@1` target Claim A only.

Inventory: 9 records = 1 Source + 3 Claims + 3 Evidence Use + Context + Scope. The dedicated regression checks record count, one Source, three Claims, three Evidence Use and valid dependency edges. It does not check source passage fit or user-facing editorial quality.

#### Direct source passage verification

The current WFP Logistics Cluster page was checked directly:
- “Logistics Cluster” overview:
  - WFP identifies the Cluster's purpose as overcoming humanitarian logistics constraints and supporting humanitarian actors at global, regional and local levels.
  - “Before crises”: strengthening humanitarian response capacity.
  - “In crises”: leadership, coordination, information management and access to common logistics services where local capacities are exceeded.
  - “After crises”: evaluation, areas for improvement, sharing good practices/solutions, learning and preparedness for future emergencies.
  - URL: https://www.wfp.org/logistics-cluster
- The Logistics Cluster's own “The Logistics Cluster” page independently clarifies the institutional mandate: coordination, information management, access to common services; multi-actor cluster approach; WFP is the designated global lead agency and hosts the team.
  - URL: https://logcluster.org/en/about-us
- The WFP page directly supports the three Claims at the level of their current high-level wording. The additional Logistics Cluster page is useful corroboration/context, but both pages describe the same WFP-led Cluster system; do not count them as independent institutional evidence tracks.

#### Claim-level fit and boundary findings

1. Claim A says humanitarian logistics helps overcome logistical constraints in delivering assistance to affected populations. WFP explicitly describes the Cluster's purpose as supporting actors in overcoming logistics constraints to delivery of global humanitarian assistance. Direct fit is strong.
2. Claim B says coordination, information exchange and access to common logistics services support humanitarian operations. WFP explicitly identifies leadership, coordination, information management and access to common logistics services during crises. The Logistics Cluster mandate page provides further operational description of coordination and information management. Direct fit is strong.
3. Claim C says post-crisis evaluation is used to identify improvements, share practices and prepare for future emergencies. WFP explicitly states all these post-crisis functions. Direct fit is strong.
4. All three current Evidence Use descriptions remain generic; they do not record the precise WFP page section/paragraph that supports each Claim.
5. All three Claim statements contain the editorial suffix `(humanitarian-logistics-basics)`. This is not part of the factual statement and must not appear in the reader-facing edition. This is a real editorial defect requiring controlled Claim correction/versioning; do not silently strip it from the canonical JSON.
6. Context and Scope target Claim A only. Do not silently apply them to Claims B/C. The current Scope is a sensible descriptive boundary but does not itself prove that each Claim has an applicability record.
7. The single WFP source is not automatically a defect or quota failure: one authoritative source directly supports this low-level descriptive slice. The second Cluster page is corroboration, not independent-source diversity.
8. Claims remain descriptive. They do not authorize operational cargo prioritization, routing, access negotiation, convoy decisions, procurement or live resource allocation. Such decisions depend on local coordination, security, access, available capacity and current humanitarian principles/requirements.

#### Decision

**HOLD — all three Claims and their exact dependency closures. No INCLUDE assigned.**

This is the strongest source-fit result among the three slices screened in this block: WFP directly supports all three high-level statements. HOLD is retained because Evidence Use lacks exact locators, all three Claims carry an editorial suffix, and Context/Scope are explicitly attached only to Claim A. The R22 gap map and passing topology test are not substitutes for a substantive audit or release approval.

Required closure: controlled Claim correction/versioning to remove the editorial suffix; update each EU with the exact WFP section/paragraph locator; decide whether Claims B/C need their own Context/Scope or a documented standards-based rationale; then complete R22 substantive/Human View and release-specific rights, attribution and editorial review.

No canonical JSON changed in this screen.


### 19. Disaster recovery basics — exact-record screen and source reconciliation (2026-11-19)

This is a record-level first-edition screen. The P5 substantive/evidence/Human View re-audit is reused; it is not repeated.

Exact inventory inspected (all `record_version: 1`, `type_version: 1.0`):
- Claims:
  - `CLM-DISASTER_RECOVERY_BASICS-A@1`
  - `CLM-DISASTER_RECOVERY_BASICS-B@1`
  - `CLM-DISASTER_RECOVERY_BASICS-C@1`
  - `CLM-DISASTER_RECOVERY_BASICS-D@1`
- Evidence Use:
  - `EU-DISASTER_RECOVERY_BASICS-A@1` → `SRC-DISASTER_RECOVERY_BASICS@1`
  - `EU-DISASTER_RECOVERY_BASICS-B@1` → `SRC-DISASTER_RECOVERY_BASICS@1`
  - `EU-DISASTER_RECOVERY_BASICS-C@1` → `SRC-DISASTER_RECOVERY_BASICS@1`
  - `EU-DISASTER_RECOVERY_BASICS-D@1` → `SRC-UNDRR-RECOVERY-2026@1`
- Sources: FEMA IS-2900.A, National Disaster Recovery Framework Overview; UNDRR “Definition: Recovery”.
- Applicability: `CTX-DISASTER_RECOVERY_BASICS@1` and `SCP-DISASTER_RECOVERY_BASICS@1` target Claim A only.

Inventory: 12 records = 2 Sources + 4 Claims + 4 Evidence Use + Context + Scope. The regression enforces the 12-record profile, two Sources, four Claims, four EUs, provenance, full Claim coverage and two distinct Source IDs. It does not validate exact passage locators.

#### Reused P5 closure and exact checkpoint validation

- `RELEASE/P5-DISASTER-RECOVERY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: substantive P5 findings 0, evidence-independence findings 0, Human View/adversarial findings 0, documentation/coverage findings 0.
- `RELEASE/P5-DISASTER-RECOVERY-UNIFIED-DEBT-MAP-2026-10-06.md`: P5-EVIDENCE-001 closed after adding the independent UNDRR recovery line and source-bounded Claim D.
- `RELEASE/P5-CLEAN-CHECKPOINT-2026-10-06.md`: checkpoint artifact was created in commit `b0da033bc3e566c5a2259598e660c4abcfef63fc`.
- Exact-checkpoint workflow runs were retrieved live and all three completed successfully on that exact SHA: Reference #1620, Release Gate #1913, Offline #1089. This closes the previously unverified P5 technical checkpoint condition; do not continue describing P5 as technically unvalidated.

#### Direct source passage checks

- FEMA IS-2900.A course overview:
  - NDRF is a national approach to meeting the needs of individuals, families, communities and states during recovery;
  - objectives include recovery continuum/timelines, recovery principles, roles and responsibilities of stakeholders across community sectors, local/state/tribal/federal leadership, planning principles and flexible Recovery Support Functions.
  - URL: https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-2900.a&lang=en
- UNDRR “Definition: Recovery”:
  - directly defines recovery as restoring or improving livelihoods, health, economic/physical/social/cultural/environmental assets, systems and activities, aligned with sustainable development and avoiding/reducing future risk.
  - URL: https://www.undrr.org/terminology/recovery

#### Claim-level fit and boundary findings

1. Claim A is directionally and substantively supported by FEMA's whole-community recovery approach and UNDRR's definition. The current EU paraphrases the Claim but does not cite the exact FEMA course overview/objective.
2. Claim B is directly supported by FEMA's objectives concerning recovery timelines, stakeholders across sectors, local/state/tribal/federal roles, planning principles and flexible support functions. The EU description is generic and has no exact objective locator.
3. Claim C is supported at a high level by FEMA's whole-community approach and local/state/tribal/federal leadership roles. The precise formulation about local context, affected-community needs, event and jurisdiction is not pinpointed in the current EU; avoid turning it into a universal legal/planning rule.
4. Claim D closely follows the UNDRR recovery definition. The EU says the independent source supports the definition but does not record the exact terminology entry locator.
5. Claim D is in English while Claims A–C are Russian. This is an editorial consistency issue for a Russian-first edition, not evidence that the definition is false.
6. Context and Scope target Claim A only. They do not automatically apply to Claims B/C/D.
7. The P5 technical checkpoint is now verified 3/3 on its exact checkpoint commit. That is repository conformance evidence, not a substitute for exact record-level source locators or factual judgement.

#### Decision

**HOLD — all four Claims and their exact dependency closures. No INCLUDE assigned.**

P5 substantive, evidence-independence, Human View and technical checkpoint closure are reused and verified. The remaining first-edition blockers are the generic EU material descriptions/no pinpoint locators, English-only Claim D in a Russian-first edition, and Context/Scope targeting Claim A only. The claims themselves are substantively supported by the two official institutional sources.

Required closure: add FEMA course-objective locators and the exact UNDRR “Recovery” entry locator through controlled Evidence Use corrections; review/translate Claim D through a versioned editorial process; decide Context/Scope applicability for B/C/D without silently broadening Claim A's records.

No canonical JSON changed in this screen.

### 20. Electrical grid basics — exact-record screen and jurisdiction boundary (2026-11-19)

The P5 substantive/evidence/Human View re-audit is reused. This is not a repeat of the P5 content audit.

Exact inventory inspected (all `record_version: 1`, `type_version: 1.0`):
- Claims:
  - `CLM_ELECTRICAL_GRID_BASICS_A@1`
  - `CLM_ELECTRICAL_GRID_BASICS_B@1`
  - `CLM_ELECTRICAL_GRID_BASICS_C@1`
  - `CLM_ELECTRICAL_GRID_BASICS_D@1`
- Evidence Use:
  - `EU_ELECTRICAL_GRID_BASICS_A@1` → `SRC_ELECTRICAL_GRID_BASICS@1`
  - `EU_ELECTRICAL_GRID_BASICS_B@1` → `SRC_ELECTRICAL_GRID_BASICS@1`
  - `EU_ELECTRICAL_GRID_BASICS_C@1` → `SRC_ELECTRICAL_GRID_BASICS@1`
  - `EU_ELECTRICAL_GRID_BASICS_D@1` → `SRC-DOE-ELECTRIC-GRIDS-2026@1`
- Sources: U.S. EIA, “How electricity is delivered to consumers”; U.S. Department of Energy, “Electric Grids”.
- Applicability: `CTX_ELECTRICAL_GRID_BASICS@1` and `SCP_ELECTRICAL_GRID_BASICS@1` target Claim A only.

Inventory: 12 records = 2 Sources + 4 Claims + 4 Evidence Use + Context + Scope. The regression checks the exact count/profile, all provenance and Claim coverage, and two distinct Source IDs. It does not check exact passage locators or whether U.S.-specific system descriptions are clearly bounded for international readers.

#### Reused P5 closure and exact checkpoint validation

- `RELEASE/P5-DISASTER-RECOVERY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: P5 substantive, evidence-independence, Human View and documentation findings all 0.
- `RELEASE/P5-DISASTER-RECOVERY-UNIFIED-DEBT-MAP-2026-10-06.md`: P5-EVIDENCE-003 closed after adding independent DOE grid reliability/resilience evidence and a bounded Claim.
- Exact P5 checkpoint commit `b0da033bc3e566c5a2259598e660c4abcfef63fc` has exact-head Reference #1620, Release Gate #1913 and Offline #1089 all successful. The technical checkpoint is verified.

#### Direct source passage checks

- U.S. EIA, “How electricity is delivered to consumers”:
  - grid connects producers and consumers through substations, transformers and power lines;
  - power plants generate electricity; transmission lines carry it over distance; distribution lines deliver lower-voltage electricity; substation transformers step voltage up/down;
  - U.S. interconnections, supply/demand balancing, system operators and regional structure are explicitly described.
  - URL: https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php
- U.S. DOE, “Electric Grids”:
  - describes a reliable/resilient grid made of transmission/distribution lines, transformers, sensors, software and communications connecting generators to customers;
  - describes systems/components/controls that must remain in balance, essential services, reliability/resilience and operator coordination of supply/demand.
  - URL: https://www.energy.gov/topics/electric-grids

#### Claim-level fit and boundary findings

1. Claim A is directly supported by EIA's grid overview and generation/delivery description.
2. Claim B is directly supported by EIA's sections on transmission/distribution lines and transformers at substations, including voltage step-up/step-down.
3. Claim C is directly supported by EIA's description of interconnected networks, balancing supply and demand, regional interconnections and different operating organizations.
4. Claim D is directly supported at a high level by DOE's grid overview, reliability/resilience and supply-demand balancing. The current DOE EU description is generic and lacks a pinpoint.
5. All four EU descriptions either paraphrase the Claim or state a general source role; none records an exact section/paragraph locator.
6. The sources describe the **United States** grid. Claim C explicitly says structure depends on region, but Claims A/B/D can read as universal. The reader-facing first-edition text must identify the U.S. source context or add a separate globally valid source line; do not silently universalize the U.S. network model.
7. Claim D is English while A–C are Russian. Review translation/editorial consistency.
8. Context and Scope target Claim A only. They do not automatically apply to B/C/D.
9. The slice remains educational. It is not an outage-response, utility-restoration, electrical-work or grid-operator instruction. No user should infer permission to intervene in electrical infrastructure.

#### Decision

**HOLD — all four Claims and their exact dependency closures. No INCLUDE assigned.**

P5 substantive/evidence/Human View and exact technical checkpoint are closed. First-edition blockers are exact EU locators, explicit U.S. jurisdiction/source boundary, English-only Claim D in a Russian-first edition and Claim-A-only Context/Scope targeting.

Required closure: add EIA/DOE section locators to each EU; make the U.S. scope explicit or add a separately sourced general claim; review/translate Claim D; decide Context/Scope applicability for B/C/D through controlled records.

No canonical JSON changed in this screen.

### 21. Infrastructure resilience basics — exact-record screen after P11 closure (2026-11-19)

This screen reuses the P11 substantive, evidence-depth, cross-slice and Human View re-audit. It does not reopen P11.

Exact inventory inspected (all `record_version: 1`, `type_version: 1.0`):
- Claims:
  - `CLM-INFRASTRUCTURE_RESILIENCE-A@1`
  - `CLM-INFRASTRUCTURE_RESILIENCE-B@1`
  - `CLM-INFRASTRUCTURE_RESILIENCE-C@1`
  - `CLM-INFRASTRUCTURE_RESILIENCE-D@1`
- Evidence Use:
  - `EU-INFRASTRUCTURE_RESILIENCE-A@1` → `SRC-INFRASTRUCTURE_RESILIENCE@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-A-2@1` → `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-B@1` → `SRC-INFRASTRUCTURE_RESILIENCE@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-B-2@1` → `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-C@1` → `SRC-INFRASTRUCTURE_RESILIENCE@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-C-2@1` → `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`
  - `EU-INFRASTRUCTURE_RESILIENCE-D@1` → `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`
- Sources: NIST Community Resilience Program; FEMA Infrastructure Dependency resource.
- Applicability: `CTX-INFRASTRUCTURE_RESILIENCE@1` and `SCP-INFRASTRUCTURE_RESILIENCE@1` target Claim A only.

Inventory: 15 records = 2 Sources + 4 Claims + 7 Evidence Use + Context + Scope. The dedicated regression checks record count minimum, record types, source/claim existence, provenance and at least one valid EU per Claim. It does not verify exact source passage fit or locator specificity.

#### Reused P11 closure and exact checkpoint validation

- `RELEASE/P11-RE-AUDIT-2026-10-07.md`: infrastructure resilience substantive debt closed; independent FEMA evidence added; dependency/cascade mechanism added; Human View PASS.
- `RELEASE/P11-UNIFIED-DEBT-MAP-2026-10-07.md`: initial P11-D06 called out single-source dependence, insufficient dependency/cascade/recovery mechanism and need for explicit performance/hazard limits; P11 re-audit says these debts closed.
- `RELEASE/CLEAN-CHECKPOINT-MATURATION-P11-2026-10-07.md`: exact checkpoint commit `d612f15847b6adbd3265e2902a840f995a04c8b7`.
- Exact-checkpoint workflow runs were retrieved live and all three completed successfully on that exact SHA: Reference #1877, Release Gate #2166, Offline #1346. P11 technical checkpoint is verified; do not describe it as awaiting exact-head validation.
- The existing M3 Relation between emergency management and infrastructure resilience is reused; no duplicate Relation is created.

#### Direct source passage checks

- NIST, “Community Resilience Program”:
  - defines community resilience as preparing for anticipated hazards, adapting, withstanding and recovering within a specified time;
  - describes hazard effects cascading through infrastructure and society;
  - states community social/economic functions and recovery should inform resilient performance requirements, including resuming operations within a specified time;
  - identifies dependencies between physical, social and economic systems and the need to address them in design/operation.
  - URL: https://www.nist.gov/programs-projects/community-resilience-program
- The current FEMA Source URI `https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency` returned HTTP 403 in the live fetch. It is therefore not independently reproducible from this check.
- Relevant official public supporting material was found outside the current Source chain:
  - FEMA P-2090/NIST SP-1254 discusses interdependent lifeline systems and cascading failure consequences.
  - CISA Infrastructure Resilience Planning Framework and Infrastructure Dependency Primer describe cross-sector dependencies and planning methods.
  - These are useful leads, not permission to silently substitute or relabel the existing FEMA Source.
  - CISA IRPF: https://www.cisa.gov/sites/default/files/2024-03/infrastructure-resilience-planning-framework03-22-2024.pdf
  - NIST SP 1190 Vol. II: https://www.nist.gov/system/files/documents/2017/05/09/NIST-SP-1190v2.pdf

#### Claim-level fit and boundary findings

1. Claim A closely matches the NIST definition of community resilience. NIST directly supports preparing for hazards, adapting, withstanding disruptions and recovering within a specified time.
2. Claim B is supported by NIST's description of effects cascading through infrastructure and society and the impact of infrastructure on social/economic functions. The current NIST EU does not point to the exact paragraphs.
3. Claim C is supported by NIST's statement that community functions should inform performance requirements and that time to recover functions should be addressed; the Claim's contrast with individual-object properties is supported by the NIST discussion of limitations of asset-only approaches. The EU lacks a locator.
4. Claim D is directly relevant to NIST's description of interconnections/dependencies and cascade effects, but the current canonical EU for D points only to the FEMA Source, whose current URI could not be fetched. NIST is not currently linked by an EU to Claim D. The NIST evidence cannot be silently borrowed across the dependency graph.
5. The 7 EU records are claim-linked and version-matched, but their descriptions are generic (“additional independent support”, “primary source directly supports”) and do not record exact section/paragraph locators.
6. Context and Scope target Claim A only. Do not apply them automatically to Claims B/C/D.
7. Claim D is a normative “should” statement. Keep it as a source-bounded planning principle, not a universal legal/engineering requirement.
8. The P11 audit's substantive/Human View PASS and exact 3/3 checkpoint are preserved. The first-edition screen is narrower and asks whether a reader can reproduce the source passage from each EU; it does not invalidate the prior P11 closure.

#### Decision

**HOLD — all four Claims and their exact dependency closures. No INCLUDE assigned.**

P11 substantive, evidence-depth, cross-slice, Human View and exact technical checkpoint are closed. The remaining first-edition blockers are generic Evidence Use descriptions, a non-retrievable FEMA Source URI, missing NIST EU linkage for Claim D despite direct NIST support, and Context/Scope records targeting Claim A only.

Required closure: controlled replacement/repair of the FEMA Source locator or a new correctly identified Source; add exact NIST locators to the existing NIST EUs and, if authorized, an NIST EU for Claim D; exact FEMA/CISA/NIST passage mapping; decide Context/Scope applicability for B/C/D. No silent source substitution or graph-edge borrowing.

No canonical JSON changed in this screen.

### 22. Cross-cutting checkpoint verification and emergency-alert locator addendum (2026-11-19)

#### Exact CLEAN checkpoint workflow retrieval

Earlier notes in this register described some checkpoint validation as unavailable because only source HEADs or summary reports had been checked. A direct GitHub API retrieval of the commits containing the checkpoint artifacts now resolves that uncertainty. The following exact checkpoint commits each have all three required workflows completed successfully on that exact SHA:

| Wave | Exact checkpoint commit | Reference | Release Gate | Offline |
|---|---|---:|---:|---:|
| P1 | `0169c9189cf2867a4387c46f8d71f1af64260adf` | #1542 PASS | #1835 PASS | #1011 PASS |
| P2 | `412658c041206715455ac39239b40b9ede5f0926` | #1550 PASS | #1843 PASS | #1019 PASS |
| M3 | `2434f3a06618543b4534ff4b12a45ad0b87e10f4` | #2163 PASS | #2450 PASS | #1632 PASS |
| P5 | `b0da033bc3e566c5a2259598e660c4abcfef63fc` | #1620 PASS | #1913 PASS | #1089 PASS |
| P11 | `d612f15847b6adbd3265e2902a840f995a04c8b7` | #1877 PASS | #2166 PASS | #1346 PASS |

The GitHub combined commit-status endpoint returns `pending` with zero classic status entries for these commits, but the three corresponding GitHub Actions workflow runs are each completed with `conclusion: success` and their `head_sha` exactly matches the checkpoint commit. The workflow runs, not the empty classic status endpoint, are the evidence for the 3/3 result.

This resolves the exact-head technical validation uncertainty for these checkpoints. It does not turn every record in those waves into a first-edition INCLUDE; substantive audit closure and record-level publication eligibility remain separate decisions.

#### Emergency-alert-warning source-locator addendum to the earlier alert screen

The prior P1/P5 substantive and Human View work is reused. The exact P1 checkpoint commit `0169c9189cf2867a4387c46f8d71f1af64260adf` has exact-head Reference #1542, Release Gate #1835 and Offline #1011 all PASS. The P5 cluster checkpoint is also exact-head 3/3 PASS as recorded above.

New direct source comparison:
- FEMA TIP 44, “Best Practices for Alerting Authorities Using Wireless Emergency Alerts”:
  - section II, paragraphs A–B explicitly require sufficient information to validate the incident/risk and clearly communicate trusted source, event, location, protective action and guidance/expiration time or duration;
  - section I.B–D states alert issuance and content decisions belong to authorized local alerting authorities and local plans/policies/procedures.
  - URL: https://www.fema.gov/sites/default/files/documents/fema_ipaws-tip-44-best-practices-wea.pdf
- The current Red Cross Source record points to the general “How to Prepare for Emergencies” page. A more precise official Red Cross “Be Informed” page was found:
  - identify how local authorities notify the public and how to receive information;
  - know the difference between watches and warnings and the actions appropriate to each.
  - URL: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/be-informed.html
- The precise Red Cross page supports knowing notification channels and distinguishing alert types/actions, but it does not establish a universal instruction to enable a specific phone setting. The current Claim's “включить аварийные уведомления на телефоне” wording needs either a separate direct source for the phone/app setting or a controlled wording correction to the more general, source-supported notification-channel concept.
- The current general Red Cross Source URL is not the precise “Be Informed” page, and the existing EU does not record the specific paragraph. The current source identity may remain American Red Cross, but the URI/EU locator requires controlled correction.
- Context and Scope in this slice target `CLM-IPAWS-ALERT-CONTENT@1` only; they do not apply to the user-preparedness Claim or the separate alert-elements Claim.

**Decision remains HOLD for the earlier alert candidate set until the Red Cross source locator/Claim wording and exact FEMA TIP 44 locators are corrected through controlled records.** The existing P1/P5 substantive and Human View PASS and exact 3/3 checkpoints are not reopened.

No canonical JSON changed in this addendum.


### 23. Water resources, quality, treatment, infrastructure, security and management — six-slice record-level block (2026-11-19; mixed Part I and ancillary screens)

This block covers six adjacent water-system layers. The prior M3/P4/P8 substantive audits and their Human View/evidence findings are reused. The current pass checks exact records, current Source URIs, claim-to-EU-to-source edges, source scope, and first-edition applicability. It does not repeat the prior substantive audits.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

**23.1 water-resources-basics — 12 records**
- Claims: `CLM_WATER_RESOURCES_BASICS_A@1`, `CLM_WATER_RESOURCES_BASICS_B@1`, `CLM_WATER_RESOURCES_BASICS_C@1`.
- Evidence Use:
  - `EU_WATER_RESOURCES_BASICS_A@1` → `SRC-WATER_RESOURCES_BASICS@1`
  - `EU_WATER_RESOURCES_BASICS_B@1` → `SRC-WATER_RESOURCES_BASICS@1`
  - `EU_WATER_RESOURCES_BASICS_C@1` → `SRC-WATER_RESOURCES_BASICS@1`
  - `EU_WATER_RESOURCES_BASICS_EPA@1` → `SRC_EPA_WATER_RESOURCES@1`, also Claim A.
- Context/Scope: `CTX-WATER_RESOURCES_BASICS@1`, `SCP-WATER_RESOURCES_BASICS@1`, both target Claim A.
- Relation: `REL_M3_WATER_RESOURCES_HYDROLOGY@1`.

**23.2 water-quality-basics — 12 records**
- Claims: `CLM_WATER_QUALITY_BASICS_A@1`, `CLM_WATER_QUALITY_BASICS_B@1`, `CLM_WATER_QUALITY_BASICS_C@1`, `CLM_WATER_QUALITY_WHO_A@1`.
- Evidence Use:
  - `EU_WATER_QUALITY_BASICS_A@1`, `..._B@1`, `..._C@1` → `SRC_WATER_QUALITY_BASICS@1`.
  - `EU_WATER_QUALITY_WHO_A@1` → `SRC_WATER_QUALITY_WHO@1`.
- Context/Scope: `CTX_WATER_QUALITY_BASICS@1`, `SCP_WATER_QUALITY_BASICS@1`, both target Claim A.

**23.3 water-treatment-basics — 11 records**
- Claims: `CLM-WATER_TREATMENT_BASICS-A@1`, `...-B@1`, `...-C@1`.
- Evidence Use:
  - `EU-WATER_TREATMENT_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-WATER_TREATMENT_BASICS@1`.
  - `EU-EPA-WATER-TREATMENT-B@1` → `SRC-EPA-WATER-TREATMENT-2026@1`, Claim B.
- Context/Scope: `CTX-WATER_TREATMENT_BASICS@1`, `SCP-WATER_TREATMENT_BASICS@1`, both target Claim A.

**23.4 water-infrastructure-basics — 11 records**
- Claims: `CLM-WATER_INFRASTRUCTURE_BASICS-A@1`, `...-B@1`, `...-C@1`.
- Evidence Use:
  - `EU-WATER_INFRASTRUCTURE_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-WATER_INFRASTRUCTURE_BASICS@1`.
  - `EU-EPA-WATER-INFRASTRUCTURE-B@1` → `SRC-EPA-WATER-INFRASTRUCTURE-RESILIENCE@1`, Claim B.
- Context/Scope: `CTX-WATER_INFRASTRUCTURE_BASICS@1`, `SCP-WATER_INFRASTRUCTURE_BASICS@1`, both target Claim A.

**23.5 water-security-basics — 11 records**
- Claims: `CLM-WATER_SECURITY-A@1`, `CLM-WATER_SECURITY-B@1`, `CLM-WATER_SECURITY-C@1`.
- Evidence Use:
  - `EU-WATER_SECURITY-A@1`, `...-B@1`, `...-C@1` → `SRC-WATER_SECURITY@1`.
  - `EU-EPA-WATER-SECURITY-B@1` → `SRC-EPA-WATER-SECURITY@1`, Claim B.
- Context/Scope: `CTX-WATER_SECURITY@1`, `SCP-WATER_SECURITY@1`, both target Claim A.

**23.6 water-resource-management-basics — 9 records**
- Claims: `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_A@1`, `..._B@1`, `..._C@1`.
- Evidence Use: `EU_WATER_RESOURCE_MANAGEMENT_BASICS_A@1`, `..._B@1`, `..._C@1` → `SRC_WATER_RESOURCE_MANAGEMENT_BASICS@1`.
- Context/Scope: `CTX_WATER_RESOURCE_MANAGEMENT_BASICS@1`, `SCP_WATER_RESOURCE_MANAGEMENT_BASICS@1`, both target Claim A.

Combined inspected inventory: **66 records** (12 + 12 + 11 + 11 + 11 + 9), 20 Claims, 25 Evidence Use, 12 Sources, 6 Context, 6 Scope, and 1 Relation. The dedicated tests verify their declared record counts, record types, claim/source references, provenance and dependency coverage. The tests do not verify source passage locators, global applicability, or factual truth.

#### Reused audit and exact checkpoint validation

- M3:
  - `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md` identified D1 substantive debt in water-resources-basics: claims were too meta-level and carried an editorial suffix.
  - `RELEASE/M3-DEBT-MAP-2026-10-08.md` records D1 resolved by adding source-supported domain substance, removing the suffix, adding EPA as a complementary source and retaining the water-resources ↔ hydrology Relation.
  - Exact M3 closure commit `2434f3a06618543b4534ff4b12a45ad0b87e10f4` has exact-head Reference #2163, Release Gate #2450 and Offline #1632 all successful.
- P4:
  - `RELEASE/P4-WATER-SAFETY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md` reports zero substantive, evidence, Human View and documentation findings after correction for water-quality, water-treatment, water-infrastructure and water-security.
  - `RELEASE/P4-CLEAN-CHECKPOINT-2026-10-06.md` is in exact checkpoint commit `6100afea739e63044ca23e2817b7706a98466f3a`; exact-head Reference #1594, Release Gate #1887 and Offline #1063 all successful.
- P8:
  - `RELEASE/P8-WATER-SECURITY-SANITATION-SUBSTANTIVE-RE-AUDIT-2026-10-06.md` reports zero blocking/substantive/Human View/evidence/provenance/documentation/regression findings for water-security, water-quality and water-treatment.
  - `RELEASE/CLEAN-CHECKPOINT-MATURATION-P8-2026-10-06.md` is in exact checkpoint commit `b29f7c8628d2f3b5e171eb184df715d557375643`; exact-head Reference #1717, Release Gate #2007 and Offline #1186 all successful.
- `water-resource-management-basics` is not covered by those closed audits; it is a distinct 9-record slice with a broad UNESCO landing-page Source and no independent/complementary Source. It remains pending its own substantive maturation audit. Do not treat P4/P8 as covering it.

#### Direct source passage checks

- USGS, “Water Resources Mission Area”:
  - identifies streamflow, groundwater, water quality, water use and availability as monitored/assessed water-resource conditions.
  - URL: https://www.usgs.gov/mission-areas/water-resources
- EPA, “Report on the Environment: Water” is the current secondary line for broad environmental water indicators; the existing EPA source is linked only to Claim A and does not establish Claims B/C.
  - URL: https://www.epa.gov/report-environment/water
- EPA, “Basic Information on Water Quality Criteria”:
  - pollutant-specific criteria are developed for human health, aquatic life and aquatic-dependent wildlife; aquatic-life criteria consider harmful concentrations and short-/long-term exposure.
  - URL: https://www.epa.gov/wqc/basic-information-water-quality-criteria
- EPA, “What are Water Quality Standards?”:
  - defines U.S. water-quality standards as legal provisions; explicitly identifies designated uses, criteria and antidegradation as the three core components.
  - This is the direct source for Claim C, but it is **not** the current `SRC-WATER_QUALITY_BASICS@1` URI. The current Source URI is the criteria page, not the standards page.
  - URL: https://www.epa.gov/wqs-tech/what-are-water-quality-standards
- WHO, “Drinking-water quality guidelines”:
  - describes health-based targets, preventive risk management/water safety plans from catchment to consumer, and independent surveillance.
  - The current WHO source URL is a direct guidelines page, but its EU description remains generic.
  - URL: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/drinking-water-quality-guidelines
- WHO Guidelines, fourth edition with 2026 addenda, section 4.2.4 “Treatment”:
  - describes treatment processes including disinfection and physical removal of hazards, and identifies pretreatment, coagulation, flocculation, sedimentation, filtration and disinfection as possible control measures.
  - This is a direct, better locator/source candidate than the current WHO WASH homepage for water-treatment-basics.
  - URL: https://www.who.int/publications/i/item/9789240121225
- EPA, “Emergency Disinfection of Drinking Water”:
  - states that emergency boiling/disinfection addresses most disease-causing microorganisms but does not remove heavy metals, salts and most chemicals; instructions are explicitly for emergency drinking-water use.
  - This source is narrow emergency disinfection guidance, not a universal source for all water treatment, industrial/wastewater use or every treatment method.
  - URL: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water
- EPA, “Drinking Water Distribution System Tools and Resources”:
  - directly defines distribution systems as connecting treatment plants/sources to customers via pipes, storage, valves and pumps;
  - says distribution systems are a final barrier against contamination and must be operated/maintained to reduce contamination risk;
  - lists water age, storage, pressure, corrosion, cross-connections and backflow as relevant themes.
  - URL: https://www.epa.gov/dwreginfo/drinking-water-distribution-system-tools-and-resources
- EPA, “Drinking Water Infrastructure Resilience and Sustainability Research”:
  - describes contaminants/biofilm in tanks and pipes, corrosion, deterioration/leaks, water age and effects on water quality; discusses system resilience, preparedness, response and recovery.
  - URL: https://www.epa.gov/water-research/drinking-water-infrastructure-resilience-and-sustainability-research
- UN-Water, “Water Security and the Global Water Agenda”:
  - working definition directly covers adequate quantities and acceptable quality, livelihoods/well-being/development, protection against water pollution and water-related disasters, and ecosystem preservation.
  - URL: https://www.unwater.org/publications/water-security-and-global-water-agenda
- EPA, “Water Security”:
  - covers contamination threats to public health, interruption of water/wastewater utilities, natural and human-made disasters, and water infrastructure resilience.
  - URL: https://www.epa.gov/emergency-response-research/water-security
- UNEP, “Integrated Water Resources Management”:
  - directly describes coordinated management of water, land and related resources; multiple interdependent uses; ecosystem protection; social/economic welfare; and competing sectoral demands.
  - This is a better specific source candidate than the current UNESCO general `/en/water` landing page for water-resource-management-basics.
  - URL: https://www.unep.org/en/what-we-do/fresh-water/water-resources-management/integrated-water-resources-management

#### Claim-level fit, duplication and boundary findings

1. **water-resources-basics**
   - M3 D1 is genuinely resolved at the content level: the current Claims now describe resource components, quantity/distribution/quality characteristics and monitoring with spatial/temporal interpretation; the prior editorial suffix is gone.
   - USGS supports the broad domain and current EPA source adds complementary support for Claim A. The EU descriptions still name a broad USGS Mission Area rather than the specific page material. Claims B/C have only the USGS EU and no pinpoint locator.
   - The Relation to hydrology is retained and regression-covered; no new Relation is needed.
2. **water-quality-basics**
   - Claims A/B are supported by the EPA criteria page. Claim C is supported by the EPA water-quality-standards page, but the current canonical Source URI points to the separate criteria page. Do not treat criteria and standards as interchangeable.
   - Claim C is expressly jurisdictional and the current source is U.S. EPA/Clean Water Act context. Context/Scope target Claim A only and do not automatically establish applicability for Claim C.
   - WHO Claim D is an international drinking-water public-health guideline claim, a different domain from EPA surface-water criteria. Keep drinking-water guidelines distinct from ambient/surface-water criteria.
   - All four Claims are in English; review Russian-first edition language consistency.
3. **water-treatment-basics**
   - Claim A's purpose statement and Claim B's dependence on source quality/contaminants/target quality are broadly consistent with WHO's catchment-to-consumer risk framework and EPA's emergency disinfection caveat.
   - The current WHO Source is a broad WASH landing page, not a specific treatment guideline. The WHO 2026 GDWQ treatment section is a much better direct source locator.
   - The EPA EU for Claim B points to emergency disinfection guidance. That evidence is bounded to emergency drinking water and pathogen disinfection; it cannot support a universal statement about all water-treatment applications.
   - Claim C (“no method is universally suitable without analysis of the specific water”) is a defensible safety boundary, but the current EU links only to the broad WHO landing page and does not identify a direct source passage.
   - Do not add treatment recipes, concentrations, contact times or method-selection instructions to close this gap.
4. **water-infrastructure-basics**
   - Claim A is directly supported by the EPA distribution-system definition.
   - Claim B is supported by EPA's statement that distribution systems are the final barrier against contamination and must be operated/maintained to reduce contamination risk; EPA resilience research adds detail on biofilm/corrosion/contaminant accumulation.
   - Claim C is strongly supported by EPA's listed themes and resilience research, including water age, storage, pressure, corrosion and backflow.
   - The EU descriptions are generic; exact paragraph/section locators are missing. These Sources are U.S. drinking-water distribution system sources, not a universal description of all water infrastructure.
5. **water-security-basics**
   - Claim A closely matches the UN-Water working definition.
   - Claim B is supported by UN-Water's protection against pollution/disasters and ecosystem preservation, with EPA's water-contamination/disaster line as complementary evidence.
   - Claim C's exact factor list (water cycle, population, infrastructure, environment, social context) is broader than the current EU's unlocated reference to the UN-Water brief. The brief is a 2013 working definition; preserve its date and source-defined status rather than present it as an immutable universal metric.
   - Context/Scope target Claim A only; Claims B/C must not inherit them silently.
6. **water-resource-management-basics**
   - The current UNESCO Source URI is the general `https://www.unesco.org/en/water` portal, not a specific source passage for the three Claims.
   - The Claims overlap water-resources-basics (resource components) and water-security-basics (multiple uses/quality/availability). They may be complementary, but the distinct purpose must be explicit: integrated management of competing uses, land/water interactions and ecosystem constraints. The UNEP IWRM page is a precise source candidate for Claim B and the management mechanism; USGS/UNEP may support A/C with separate, exact links.
   - This slice has not received the prior P4/P8 substantive re-audit. Its 9-record topology test verifies schema/semantic validity and links, not substantive sufficiency or evidence diversity.
   - No INCLUDE is justified until its own substantive audit and source correction are completed.

#### Decisions

- **water-resources-basics: HOLD — all three Claims and dependency closures.** M3 substantive D1, evidence-independence D5, Human View and exact technical checkpoint are closed. Remaining blocker is record-level pinpointing in all three USGS EUs and the EPA Claim-A EU.
- **water-quality-basics: HOLD — all four Claims and dependency closures.** P4/P8 substantive and exact technical checkpoints are closed. Remaining blockers are the current Source URI mismatch for Claim C, exact EPA/WHO locators, U.S. jurisdiction boundary for the standards Claim, and Russian-first editorial consistency.
- **water-treatment-basics: HOLD — all three Claims and dependency closures.** P4/P8 substantive and exact technical checkpoints are closed. Remaining blockers are the broad WHO Source URI, the emergency-only scope of the EPA line, exact locators, and direct evidence for Claim C.
- **water-infrastructure-basics: HOLD — all three Claims and dependency closures.** P4 substantive and exact technical checkpoint are closed. Remaining blockers are generic EUs and U.S. drinking-water distribution-system boundary.
- **water-security-basics: HOLD — all three Claims and dependency closures.** P4/P8 substantive and exact technical checkpoints are closed. Remaining blockers are generic EUs, exact UN-Water/EPA locators, and precise dating/definition boundary.
- **water-resource-management-basics: HOLD — all three Claims and dependency closures.** No substantive maturation audit; UNESCO homepage URI is too broad; overlap with adjacent slices needs explicit scope separation.

No canonical JSON changed in this screen.



### 24. Food security, food systems, distribution, nutrition and preservation — five-slice record-level block (2026-11-19)

> Superseded by Section 25, which adds the separately screened food-safety slice and consolidates the complete six-slice block.


This block reuses the P7 and M3 substantive/evidence/Human View work. It does not repeat those audits. It checks current record versions, exact dependency paths, current source pages, source boundaries, and first-edition readiness.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

**24.1 food-security-basics — 12 records**
- Claims: `CLM-FOOD_SECURITY_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: `EU-FOOD_SECURITY_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-FOOD_SECURITY_BASICS@1`; `EU-FOOD_SECURITY_BASICS-D@1` → `SRC-FOOD_SECURITY_USDA@1`.
- Sources: FAO Food Security Information and Early Warning System Handbook; USDA Economic Research Service Food Security in the U.S. — Measurement.
- Context/Scope: `CTX-FOOD_SECURITY_BASICS@1`, `SCP-FOOD_SECURITY_BASICS@1`, target Claim A.

**24.2 food-systems-basics — 12 records**
- Claims: `CLM-FOOD_SYSTEMS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: `EU-FOOD_SYSTEMS-A@1`, `...-B@1`, `...-C@1` → `SRC-FOOD_SYSTEMS@1`; `EU-FOOD_SYSTEMS-D@1` → `SRC-FOOD_SYSTEMS_WB@1`.
- Sources: FAO Agrifood Systems; World Bank, “The Future of Food: Shaping the Global Food System to Deliver Improved Nutrition and Health”.
- Context/Scope: `CTX-FOOD_SYSTEMS@1`, `SCP-FOOD_SYSTEMS@1`, target Claim A.

**24.3 food-distribution-basics — 12 records**
- Claims: `CLM-FOOD_DISTRIBUTION_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: `EU-FOOD_DISTRIBUTION_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-FOOD_DISTRIBUTION_BASICS@1`; `EU-FOOD_DISTRIBUTION_BASICS-D@1` → `SRC-FOOD_DISTRIBUTION_WFP@1`.
- Sources: FAO Food Systems; WFP, “Supply chain and delivery procurement infographics”.
- Context/Scope: `CTX-FOOD_DISTRIBUTION_BASICS@1`, `SCP-FOOD_DISTRIBUTION_BASICS@1`, target Claim A.
- The P7 Relation to humanitarian logistics is retained; no duplicate Relation is created.

**24.4 nutrition-basics — 12 records**
- Claims: `CLM-NUTRITION_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: `EU-NUTRITION_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-NUTRITION_BASICS@1`; `EU-NUTRITION_BASICS-D@1` → `SRC-NUTRITION_WHO@1`.
- Sources: NIH/NIEHS “Nutrition, Health, and Your Environment”; WHO “Healthy diet”.
- Context/Scope: `CTX-NUTRITION_BASICS@1`, `SCP-NUTRITION_BASICS@1`, target Claim A.

**24.5 food-preservation-basics — 12 records**
- Claims: `CLM-FOOD_PRESERVATION_BASICS-A@1`, `...-B@1`, `...-C@1`.
- Evidence Use: `EU-FOOD_PRESERVATION_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-FOOD_PRESERVATION_BASICS@1`; `EU_FOOD_PRESERVATION_BASICS_FDA@1` → `SRC_FDA_FOOD_STORAGE_SAFETY@1`, Claim B.
- Sources: USDA FSIS “Food Safety Basics”; FDA “Are You Storing Food Safely?”.
- Context/Scope: `CTX-FOOD_PRESERVATION_BASICS@1`, `SCP-FOOD_PRESERVATION_BASICS@1`, target Claim A.
- Relation: `REL_M3_FOOD_PRESERVATION_SAFETY@1`.

Combined inspected inventory: **60 records** (12 × 5), 19 Claims, 20 Evidence Use, 10 Sources, 5 Context, 5 Scope and 1 Relation. Dedicated regressions enforce the 12-record profiles, record types, provenance and Claim→EU→Source paths. They do not establish passage-level support or reader-facing editorial quality.

#### Reused audit and exact checkpoint validation

- P7:
  - `RELEASE/P7-FOOD-SECURITY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: five-slice P7 substantive re-audit PASS; 0 critical, blocking, substantive, evidence-depth, Human View, linkage or documentation/regression findings.
  - `RELEASE/P7-FOOD-SECURITY-UNIFIED-DEBT-MAP-2026-10-06.md`: P7-EVIDENCE-001–005, P7-CONTENT-006, P7-LINKAGE-007, P7-HUMAN-008 and P7-DOC-009 all closed.
  - Exact checkpoint commit `b79792577bca6cdda9b1bcffc15c74a2414ac235` has exact-head Reference #1698, Release Gate #1991 and Offline #1167 all successful.
- M3:
  - `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`: food-preservation-basics PASS, no mandatory Claim rewrite; existing Scope excludes risky preservation instructions.
  - `RELEASE/M3-DEBT-MAP-2026-10-08.md`: D6 independent FDA evidence marked RESOLVED; M3 Relation R4 is present and regression-covered.
  - Exact M3 closure commit `2434f3a06618543b4534ff4b12a45ad0b87e10f4` has exact-head Reference #2163, Release Gate #2450 and Offline #1632 all successful.
- The P7 and M3 exact checkpoint workflows are now verified on the commits containing the checkpoint artifacts. This does not remove newly observed editorial or record-level locator gaps.

#### Direct source passage checks

- FAO, “Handbook for Defining and Setting up a Food Security Information and Early Warning System”:
  - section 1.4 defines food security as physical/economic access to sufficient, safe and nutritious food and names availability, stability, access and biological utilization (lines 53–57);
  - section 2 describes monitoring, forecasting, warning signals and information to support decisions (lines 58–67);
  - section 3.1 describes production, markets, vulnerable populations, nutritional surveillance, stocks and infrastructure as components of food-security monitoring (lines 83–90).
  - URL: https://www.fao.org/4/x8622e/x8622e04.htm
- USDA ERS, “Food Security in the U.S. — Measurement”:
  - defines household food security as access by all members at all times to enough food for an active, healthy life; includes availability of nutritionally adequate/safe foods and assured ability to acquire acceptable foods (lines 104–109).
  - The page is explicitly a U.S. household measurement source.
  - URL: https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/measurement
- FAO, “Agrifood Systems”:
  - directly covers people, activities, investments and choices involved in producing/delivering food; activities from growing/harvesting through processing, packaging, transport, distribution, trade, purchase, preparation, eating and disposal (lines 5–7).
  - URL: https://www.fao.org/food-systems/en
- World Bank, “The Future of Food: Shaping the Global Food System to Deliver Improved Nutrition and Health”:
  - describes food-system interventions across the production-to-consumption continuum, including producers, post-harvest handlers, processors, distributors and consumers; highlights improved storage and food-loss reduction.
  - URL: https://www.worldbank.org/en/topic/agriculture/publication/the-future-of-food-shaping-the-global-food-system-to-deliver-improved-nutrition-and-health
- WFP, “Supply chain”:
  - explicitly lists planning, procurement, transport, storage and delivery; describes the transport network, warehouses/logistics hubs, last-mile delivery and emergency supply-chain operations.
  - This is the precise source candidate for Claim D, not the current procurement-infographics Source URI.
  - URL: https://www.wfp.org/supply-chain
- NIEHS, “Nutrition, Health, and Your Environment”:
  - nutrition is consuming, absorbing and using nutrients (lines 31–33);
  - macronutrients are protein, carbohydrate and fat; micronutrients are vitamins and minerals (lines 34–38);
  - excess or deficiency of certain nutrients can affect health (line 21).
  - URL: https://www.niehs.nih.gov/health/topics/nutrition
- WHO, “Healthy diet”:
  - identifies adequacy, balance, moderation and diversity as four core principles; diet composition varies with individual characteristics, culture, locally available foods and customs.
  - URL: https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet
- FDA, “Are You Storing Food Safely?”:
  - explains that safe storage prevents foodborne illness and that temperature controls slow microbial growth; includes product-specific storage and power-outage guidance.
  - URL: https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely
- USDA FSIS “Food Safety Basics” URI returned HTTP 403 in the direct live fetch. Official FSIS public Q&A pages independently expose related food handling, cross-contamination, refrigeration and temperature information, but those pages are not the current Source URI and must not be silently substituted.

#### Claim-level fit, duplication and boundary findings

1. **food-security-basics**
   - FAO section 1.4 directly supports Claim A and the four-pillar structure behind Claim B. FAO sections 2 and 3 directly support Claim C's monitoring/early-warning role and decision support.
   - USDA ERS directly supports Claim D, but its definition is a U.S. household food-security measurement definition. The Claim currently reads as a universal household definition; its source jurisdiction must be visible or a global source added.
   - Claims A/B/C all retain the editorial suffix `(food-security-basics)`. It is not factual content and must not appear in the reader-facing edition. This is an unclosed editorial defect despite P7 substantive PASS.
   - All four EUs are generic source descriptions without exact section locators. The direct FAO/USDA passages exist and can be recorded precisely.
2. **food-systems-basics**
   - FAO directly supports Claims A/B. The current FAO landing page is a valid source identity, but its EU descriptions do not identify the exact definition paragraph.
   - Claim C's list of natural resources, technologies, trade and access is broader than the top-level FAO definition. FAO's 2026 interactive “interconnected agrifood systems” page has more specific system building blocks, but it is not the current Source URI/EU locator.
   - The current World Bank Source URI is correctly identified as the “improved nutrition and health” publication. It supports production-to-consumption actors, post-harvest handlers, processing, distribution and improved storage/food-loss reduction. It does not itself establish every item in Claim D's longer list (especially the explicit transport/logistics/retail sequence); a different World Bank publication, “deliver jobs”, does contain that longer sequence. Do not conflate those two publications.
   - All four EU descriptions are generic; no exact source section/paragraph is recorded.
3. **food-distribution-basics**
   - FAO supports the broad connection between production, transport, distribution, trade and access, but the current EUs do not pinpoint the relevant sections.
   - Claim B's full list (transport, storage, infrastructure, markets, rules and food losses) is broader than the FAO landing-page summary. Add exact support for the distinct factors rather than relying on the general food-systems identity.
   - Claim C (local availability is not determined by production volume alone) needs a precise source passage on access, market/transport constraints or distribution bottlenecks; the current EU points only to the broad FAO page.
   - Claim D's full sequence of procurement, storage, transportation and delivery is directly stated on WFP's “Supply chain” page. The current WFP Source URI is instead the procurement-infographics page, which describes procurement and delivery but does not provide the complete direct passage. A controlled Source/EU update is required.
   - Keep the slice's boundary: this is descriptive distribution knowledge, not live routing, procurement, warehouse, security or humanitarian operational instruction.
4. **nutrition-basics**
   - NIEHS directly supports Claims A–C; WHO directly supports Claim D's four principles and variation by individual/cultural context.
   - The EU descriptions remain generic, but the exact source passages are available.
   - README and Scope explicitly exclude individual medical, dietary and therapeutic advice. Context/Scope records target Claim A only; do not silently inherit them, but the broader README boundary remains explicit for the slice. No individual recommendation is introduced by the current Claims.
   - The four Claims are Russian and source lines are authoritative international/U.S. explanatory materials; no unsupported numerical diet targets are added.
5. **food-preservation-basics**
   - The Claims remain appropriately general and do not contain risky canning, fermentation or preservation recipes. M3 substantive PASS is reused.
   - FDA directly supports the relationship between handling/storage/time/temperature and microbial growth. USDA FSIS is the primary source identity, but its current URI was not directly retrievable in the live check; an official FSIS public Q&A page is available as a lead, not a silent replacement.
   - EU descriptions remain generic. Claim C is a reader-safety boundary and should be supported/presented as a Scope principle rather than left as a factual claim with no pinpoint source.
   - A documentation defect was found: the README declared a single Source and did not expose the 4 Evidence Use / Relation topology, while the canonical records contain 2 Sources, 3 Claims, 4 Evidence Use, Context, Scope and one Relation. This was corrected without changing canonical JSON in commit `6612f5ce5e7db405fc34ea4aafc18d0c0e9b7287`; the README now matches the 12-record inventory and identifies both sources and the Relation.

#### Decisions

- **food-security-basics: HOLD — all four Claims and dependency closures.** P7 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining blockers: editorial suffix on Claims A/B/C, generic EU locators, and the U.S.-specific USDA definition currently phrased as universal.
- **food-systems-basics: HOLD — all four Claims and dependency closures.** P7 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining blockers: exact FAO locators, stronger direct source for Claim C's system factors, full Claim D source-fit reconciliation between two different World Bank publications, and generic EUs.
- **food-distribution-basics: HOLD — all four Claims and dependency closures.** P7 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining blockers: generic FAO EUs, specific support for Claim B/C, and current WFP procurement-infographics Source URI not matching the direct WFP supply-chain passage for Claim D.
- **nutrition-basics: HOLD — all four Claims and dependency closures.** P7 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining blocker: generic EU locators; substantive support is direct and the slice boundary is adequate.
- **food-preservation-basics: HOLD — all three Claims and dependency closures.** M3 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining blockers: exact USDA/FDA locators, live retrieval/source-locator confirmation for the USDA page, and Claim C's scope-like status. README topology mismatch is corrected in the documented commit.

No canonical JSON changed in this screen. The only non-register content change in this block is the food-preservation README synchronization described above.


### 25. Food security, food systems, distribution, nutrition, food safety and preservation — six-slice record-level block (2026-11-19)

This block screens the complete five-slice P7 Food Security & Nutrition Resilience cluster plus the adjacent M3 food-preservation slice. P7's substantive re-audit, evidence-independence review, Human View, cross-slice linkage and regression synchronization are reused; they are not repeated. This pass checks exact record versions, current Claim wording, graph edges, current Source URIs, direct source passages and first-edition editorial/applicability constraints.

#### 24.1 Exact inventory

All inspected records have `record_version: 1` and `type_version: 1.0`.

**food-security-basics — 12 records**
- Claims: `CLM-FOOD_SECURITY_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: `EU-FOOD_SECURITY_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-FOOD_SECURITY_BASICS@1`; `EU-FOOD_SECURITY_BASICS-D@1` → `SRC-FOOD_SECURITY_USDA@1`.
- Sources: FAO FSIEWS Handbook; USDA ERS food-security measurement.
- Context/Scope both target Claim A only.

**food-systems-basics — 12 records**
- Claims: `CLM-FOOD_SYSTEMS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: A/B/C → `SRC-FOOD_SYSTEMS@1` (FAO); D → `SRC-FOOD_SYSTEMS_WB@1` (World Bank).
- Sources: FAO Agrifood Systems; World Bank, *The Future of Food*.
- Context/Scope both target Claim A only.

**food-distribution-basics — 12 records**
- Claims: `CLM-FOOD_DISTRIBUTION_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: A/B/C → `SRC-FOOD_DISTRIBUTION_BASICS@1` (FAO); D → `SRC-FOOD_DISTRIBUTION_WFP@1` (WFP).
- Sources: FAO Food Systems; WFP 2024 Procurement Infographics.
- Context/Scope both target Claim A only.

**nutrition-basics — 12 records**
- Claims: `CLM-NUTRITION_BASICS-A@1`, `...-B@1`, `...-C@1`, `...-D@1`.
- Evidence Use: A/B/C → `SRC-NUTRITION_BASICS@1` (NIH/NIEHS); D → `SRC-NUTRITION_WHO@1` (WHO).
- Sources: NIH/NIEHS Nutrition, Health, and Your Environment; WHO Healthy Diet.
- Context/Scope both target Claim A only.

**food-safety-basics — 12 records**
- Claims: `CLM-FOOD_SAFETY_BASICS-A@1`, `...-B@1`, `...-C@1`, and separate English Claim `CLM_FOOD_SAFETY_CDC_A@1`.
- Evidence Use: A/B/C → FDA Source `SRC-FOOD_SAFETY_BASICS@1`; CDC Claim → `SRC_FOOD_SAFETY_CDC@1`.
- Sources: FDA Food Safety at Home; CDC Preventing Food Poisoning.
- Context/Scope both target Claim A only.
- README and regression explicitly preserve FDA and CDC as separate evidence tracks; CDC is not misrepresented as independent corroboration of FDA Claims A/B/C.

**food-preservation-basics — 12 records**
- Claims: `CLM-FOOD_PRESERVATION_BASICS-A@1`, `...-B@1`, `...-C@1`.
- Evidence Use: A/B/C → `SRC-FOOD_PRESERVATION_BASICS@1` (USDA FSIS); additional FDA EU for Claim B → `SRC_FDA_FOOD_STORAGE_SAFETY@1`.
- Sources: USDA FSIS Food Safety Basics; FDA Are You Storing Food Safely?
- Context/Scope both target Claim A only.
- Relation: `REL_M3_FOOD_PRESERVATION_SAFETY@1`.

Combined inspected inventory: **72 records** — six slices × 12 records each; 23 Claims, 24 Evidence Use, 12 Sources, 6 Context, 6 Scope and 1 Relation. The dedicated regression tests enforce the record counts/profiles, claim coverage, provenance and dependency edges. The food-safety test additionally enforces the separation of FDA and CDC evidence. These tests do not establish pinpoint source locators, source passage truth or first-edition eligibility.

#### 24.2 Reused audits and exact technical checkpoints

**P7 Food Security & Nutrition Resilience**
- `RELEASE/P7-FOOD-SECURITY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: all five P7 target slices (food security, food systems, food distribution, food safety, nutrition) re-audited; substantive, evidence-depth, Human View, linkage and documentation/regression findings all 0.
- `RELEASE/P7-FOOD-SECURITY-UNIFIED-DEBT-MAP-2026-10-06.md`: P7-EVIDENCE-001 through 005, CONTENT-006, LINKAGE-007, HUMAN-008 and DOC-009 all closed. FDA/CDC separation is intentionally preserved.
- `RELEASE/P7-CLEAN-CHECKPOINT-2026-10-06.md`: checkpoint artifact commit `b79792577bca6cdda9b1bcffc15c74a2414ac235`.
- Exact-head GitHub Actions runs retrieved for that checkpoint SHA: Reference #1698 PASS, Release Gate #1991 PASS, Offline #1167 PASS. Each run's `head_sha` exactly matches the checkpoint commit.
- The checkpoint document itself says independent 3/3 validation is required. The exact-head workflow result is confirmed; do not claim a separate human/independent audit beyond the recorded workflows.

**M3 food-preservation**
- `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`: food-preservation-basics PASS, no mandatory Claim rewrite; the three Claims appropriately cover contamination/growth factors, product/time/temperature/method dependence and product-specific authoritative guidance. Scope excludes risky preservation instructions.
- `RELEASE/M3-DEBT-MAP-2026-10-08.md`: D6 independent FDA evidence added as a complementary source to USDA FSIS; the M3 audit reports D3–D8 evidence tracks resolved, Human View PASS, and the food-preservation ↔ food-safety Relation present and regression-covered.
- Exact M3 checkpoint `2434f3a06618543b4534ff4b12a45ad0b87e10f4` has exact-head Reference #2163, Release Gate #2450 and Offline #1632 all successful.
- These prior results are reused; no M3/P7 content audit is restarted.

#### 24.3 Direct source passage verification

- **FAO FSIEWS Handbook**, section 1.4 “Definition of Food Security”: the 1996 World Food Summit definition covers physical/economic access to sufficient, safe and nutritious food; the same section identifies availability, stability, access and biological utilization. Sections 2 and 5 describe forecasting, monitoring and information systems across those dimensions.
  - https://www.fao.org/4/x8622e/x8622e04.htm
- **USDA ERS**, “Food Security in the U.S. — Measurement”: household food security means all members have access at all times to enough food for an active, healthy life; the page also describes U.S. household measurement scales and resource-constrained food insecurity.
  - https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/measurement
- **FAO Agrifood Systems FAQ**, “What are agrifood systems?”: explicitly covers interconnected components and activities from growing/raising/harvesting through processing, packaging, transport, distribution, trade, purchase, preparation, consumption and disposal/reuse; also people, activities, investments and choices, and dependencies on environmental, economic, health and social systems.
  - https://www.fao.org/food-systems/faq/en
- **World Bank**, *The Future of Food*: describes the production-to-consumption continuum and off-farm activities, including storage, processing, distribution, transport, logistics and retail; emphasizes that context-specific combinations of interventions are needed.
  - https://www.worldbank.org/en/topic/agriculture/publication/the-future-of-food-shaping-the-global-food-system-to-deliver-improved-nutrition-and-health
- **WFP Supply Chain**: directly identifies planning, procurement, transport, storage and delivery as the four supply-chain steps; describes warehouses/logistics hubs, local partners and last-mile delivery.
  - https://www.wfp.org/supply-chain
- **NIH/NIEHS**, “Nutrition, Health, and Your Environment”: defines nutrition as consuming, absorbing and using nutrients; describes macronutrients (protein, carbohydrate, fat), micronutrients and effects of nutrient deficiency/excess.
  - https://www.niehs.nih.gov/health/topics/nutrition
- **WHO**, “Healthy diet” (26 January 2026): states four core principles—adequacy, balance, moderation and diversity—and says the exact diet varies with individual characteristics, cultural context, locally available foods and dietary customs.
  - https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet
- **FDA**, “Food Safety at Home”: directly enumerates Clean, Separate, Cook and Chill; explicitly describes keeping raw foods apart, safe internal temperatures and use of a food thermometer, and prompt refrigeration.
  - https://www.fda.gov/consumers/womens-health-topics/food-safety-home
- **CDC**, “Preventing Food Poisoning” (24 November 2025): independently describes Clean, Separate, Cook and Chill, cross-contamination prevention, thermometer use and prompt refrigeration.
  - https://www.cdc.gov/food-safety/prevention/index.html
- **USDA FSIS**, “How do I keep my foods safe to eat?”: directly supports cleaning, separation, safe cooking temperatures and chilling; the current canonical Source URI is the broader FSIS Food Safety Basics page.
  - https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics
- **FDA**, “Are You Storing Food Safely?”: directly supports product/time/temperature-dependent storage, refrigeration/freezing, and the fact that appearance/smell alone cannot establish safety.
  - https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely

#### 24.4 Claim-level fit, cross-slice distinction and editorial findings

1. **food-security-basics**
   - FAO section 1.4 directly supports Claim A's access/sufficient/safe/nutritious food formulation and Claim B's availability/stability/access dimensions. FAO sections 2/5 support Claim C's information/forecasting/early-warning mechanism.
   - USDA ERS directly supports Claim D's household-level definition. Preserve the distinction: USDA ERS is a U.S. measurement context, while FAO's definition is international and population-level.
   - Claims A, B and C still contain the editorial suffix `(food-security-basics)`; it is not part of the factual proposition and must not appear in the reader-facing edition. Do not silently edit canonical Claim @1.
   - The four EU descriptions are generic and do not record section 1.4, sections 2/5, or the USDA definition heading/measurement context. Context/Scope target Claim A only.
2. **food-systems-basics**
   - FAO directly supports Claims A/B/C: connected activities from farm to table, people/activities/investments/choices, and interdependence with natural resources and other systems.
   - World Bank supports Claim D's off-farm chain components. The World Bank source is an older 2016 publication; it is still directly relevant to the high-level chain description but should not be used for current statistics or current policy claims.
   - Claim D is close to Claim A and to the separate food-distribution slice. Keep the conceptual distinction: this slice defines the whole system; food-distribution focuses on one functional link. The EU descriptions are generic; Context/Scope target Claim A only.
3. **food-distribution-basics**
   - FAO's system definition supports the high-level relation between production and consumers (Claim A), and shows multiple linked activities and actors. Claims B/C need precise source passages explaining transport/storage/markets and why local availability is not equivalent to production volume; the current FAO landing page is too broad to act as a pinpoint locator.
   - Claim D is strongly supported by the WFP supply-chain page, which explicitly lists planning, procurement, transport, storage and delivery. However, the canonical WFP Source URI currently points to 2024 Procurement Infographics, not the WFP Supply Chain page that directly supports the complete claim. This is a source-locator mismatch, not a source-identity defect.
   - Preserve the boundary between general food distribution and humanitarian last-mile operations. Claim D is specifically humanitarian; the other Claims are broader system-level statements. Context/Scope target Claim A only.
4. **nutrition-basics**
   - NIEHS directly supports Claim A's consumption/absorption/use definition, Claim B's macro/micronutrient categories and Claim C's deficiency/excess effect. WHO directly supports Claim D's four principles and its individual/cultural/local variation qualification.
   - The source fit is strong, but the EU descriptions do not identify the relevant NIEHS sections or WHO principles paragraph. Context/Scope target Claim A only; they do not automatically extend to Claims B/C/D.
   - The slice is general population-level information, not individualized dietetic or therapeutic advice. The README/Scope correctly preserve this boundary.
5. **food-safety-basics**
   - FDA directly supports Claims A/B/C at the level of the four basic steps, separation and product/process-dependent requirements. CDC directly supports the separate CDC Claim on internal temperatures and thermometer use.
   - The FDA and CDC evidence tracks are intentionally separate and regression-protected. Do not merge them into a false two-source corroboration claim for A/B/C.
   - The FDA and CDC pages are U.S. public-health guidance. Avoid presenting exact temperature values or regulatory requirements as universal across jurisdictions; the current Claims A/B/C do not state numerical thresholds.
   - The EU descriptions for the FDA Claims are generic. The CDC EU description is more precise about evidence independence, but still does not cite the exact CDC prevention sections. Context/Scope target Claim A only.
6. **food-preservation-basics**
   - USDA FSIS supports general food-safety principles and the need to control conditions; FDA directly supports Claim B's time/temperature/storage dependence. Claim C is a conservative boundary statement consistent with both sources.
   - The additional FDA evidence is a distinct agency source and is correctly attached to Claim B only. The Relation to food-safety-basics is justified and regression-covered.
   - The EUs remain generic and do not identify the USDA/FDA passages. Context/Scope target Claim A only. The slice correctly excludes risky preservation procedures and must not be expanded into unvalidated canning/fermentation recipes or processing times.

#### 24.5 Decisions

- **food-security-basics: HOLD — all four Claims and exact dependency closures.** P7 substantive audit and exact-head 3/3 workflow checkpoint are reused. Remaining blockers: editorial suffix on Claims A/B/C, generic EUs/no pinpoint locators, U.S.-specific household measurement boundary for Claim D, and Context/Scope attached only to Claim A.
- **food-systems-basics: HOLD — all four Claims and exact dependency closures.** P7 substantive audit and exact-head 3/3 workflow checkpoint are reused. Remaining blockers: generic EU locators, older World Bank publication context, and editorial distinction from food-distribution.
- **food-distribution-basics: HOLD — all four Claims and exact dependency closures.** P7 substantive audit and exact-head 3/3 workflow checkpoint are reused. Remaining blockers: generic FAO locators for A/B/C, WFP Source URI mismatch for D, and separation of general distribution from humanitarian supply-chain operations.
- **nutrition-basics: HOLD — all four Claims and exact dependency closures.** P7 substantive audit and exact-head 3/3 workflow checkpoint are reused. Remaining blockers: generic NIEHS/WHO locators and Context/Scope applicability only on Claim A.
- **food-safety-basics: HOLD — all four Claims and exact dependency closures.** P7 substantive audit and exact-head 3/3 workflow checkpoint are reused. FDA/CDC track separation is correct and must be preserved. Remaining blockers: generic FDA/CDC locators, U.S. jurisdiction boundary and Context/Scope applicability only on Claim A.
- **food-preservation-basics: HOLD — all three Claims and exact dependency closures.** M3 substantive/Human View, FDA evidence addition, Relation and exact technical checkpoint are reused. Remaining blockers: generic USDA/FDA locators and Context/Scope applicability only on Claim A.

No canonical JSON changed in this screen. No INCLUDE assigned. The P7/M3 substantive audit results are not invalidated; this is a stricter first-edition record-level eligibility decision.


### 26. Sanitation, solid-waste management and wastewater systems — six-slice record-level block (2026-11-19)

This block screens six adjacent foundational slices: sanitation-basics, waste-management-basics, waste-infrastructure-basics, wastewater-basics, wastewater-engineering-basics and wastewater-treatment-basics. It reuses the closed substantive conclusions where P3/P8 already covered sanitation and wastewater; it does not restart those audits. The additional first-edition screen checks current Claim text, exact record topology, Claim → Evidence Use → Source paths, canonical Source URI resolution, direct official source passages, source jurisdiction/age, and the boundary between adjacent slices.

#### 26.1 Exact inventory and topology

The branch tree and the six dedicated regression tests identify **60 records** across the six slices. The record profiles are:

| Slice | Records | Claims | Sources | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| sanitation-basics | 11 | 3 | 2 | 4 | 1 | 1 |
| waste-management-basics | 9 | 3 | 1 | 3 | 1 | 1 |
| waste-infrastructure-basics | 9 | 3 | 1 | 3 | 1 | 1 |
| wastewater-basics | 13 | 3 | 2 | 6 | 1 | 1 |
| wastewater-engineering-basics | 9 | 3 | 1 | 3 | 1 | 1 |
| wastewater-treatment-basics | 9 | 3 | 1 | 3 | 1 | 1 |
| **Total** | **60** | **18** | **8** | **22** | **6** | **6** |

All inspected Claim records declare record_version 1 and type_version 1.0. The dedicated tests enforce the stated slice counts and minimum graph shapes. The sanitation and wastewater-engineering tests additionally run schema and semantic validation and check Claim provenance plus Evidence Use → Source paths. The waste-management test checks one Source, three Claims, three EUs and the Claim/source links. The wastewater-basics test checks two Sources and requires every Claim to link to both. The waste-infrastructure and wastewater-treatment tests mainly enforce counts/type profiles and basic links; they do not establish locator precision or claim truth.

The Context and Scope records inspected in sanitation-basics and wastewater-basics target Claim A only. Do not extend their applicability to Claims B/C without explicit records. The other four slices also have one Context and one Scope in their canonical nine-record shape; their presence does not cure generic Evidence Use descriptions.

#### 26.2 Reused substantive audits and prior findings

**P3 Sanitation & Emergency Hygiene**
- RELEASE/P3-SANITATION-HYGIENE-CORRECTION-AUDIT-2026-10-06.md records that CDC independent evidence was added to sanitation-basics for the health/exposure boundary, the README was synchronized, and regression tests were strengthened.
- RELEASE/P3-SANITATION-HYGIENE-UNIFIED-DEBT-MAP-2026-10-06.md records the post-correction substantive re-audit as clean, with no new substantive, evidence-independence, Human View, Relation, duplicate-source or documentation findings. It explicitly distinguishes substantive cleanliness from the still-required technical 3/3 CLEAN checkpoint.
- The current sanitation topology is 2 Sources / 3 Claims / 4 EUs / Context / Scope and matches the README and regression test. The CDC line remains attached only to Claim B; it is not independent support for Claims A/C.

**P8 Water Security & Sanitation**
- RELEASE/P8-WATER-SECURITY-SANITATION-SUBSTANTIVE-RE-AUDIT-2026-10-06.md records zero blocking, substantive, Human View/adversarial, evidence/provenance, documentation/regression findings across five slices, including sanitation-basics and wastewater-basics.
- The P8 report confirms the two-source wastewater-basics correction and that all three Claims are linked to both EPA and WHO Sources.
- P8 substantive results are reused. They do not waive the present record-level locator check or the requirement to distinguish source identity, direct passage and first-edition applicability.

No equivalent prior substantive audit was found in the RELEASE file inventory for waste-management-basics, waste-infrastructure-basics, wastewater-engineering-basics or wastewater-treatment-basics. Their findings below are new record-level screening findings, not claims that a prior audit passed.

#### 26.3 Direct source verification

**Sanitation**
- WHO, Sanitation, current fact sheet dated 5 November 2026: the overview and challenges sections describe safely managed sanitation, human excreta/wastewater management, disease transmission, contamination of drains and groundwater, and the need for policy, regulation, financing, monitoring and capable service systems. The sanitation service-chain and safe-management framing supports the general Claims, with exact material in the overview/challenges/WHO response sections.
  - Canonical URI in Source: https://www.who.int/news-room/fact-sheets/detail/sanitation
- CDC, Global Sanitation: the current Source record identifies the CDC public-health page as a separate line of evidence for the health/exposure boundary. Its Evidence Use description is materially more specific than the WHO EUs, but the CDC source remains attached only to Claim B.
  - Canonical URI in Source: https://www.cdc.gov/global-water-sanitation-hygiene/about/about-global-sanitation.html

**Solid-waste management**
- UNEP, Solid waste management: the canonical URI resolves by redirect to the current UNEP page. It describes harm from inadequate collection and disposal, environmental and health contamination, waste minimisation, recovery of materials/energy, remanufacturing, recycling and integrated local systems.
  - Canonical URI currently stored: https://www.unep.org/explore-topics/resource-efficiency/what-we-do/cities/solid-waste-management
  - Current destination: https://www.unep.org/en/solid-waste-management
- US EPA, Sustainable Materials Management: the canonical URI is a broad topic landing page. EPA's more directly useful current materials are Sustainable Materials Management Basics (life-cycle stages and waste management) and Non-Hazardous Materials and Waste Management Hierarchy (source reduction/reuse, recycling/composting, energy recovery, treatment and disposal). These pages show why the generic EPA SMM landing page is not a pinpoint for the waste-infrastructure Claims.
  - Canonical URI currently stored: https://www.epa.gov/smm
  - Direct hierarchy locator checked: https://www.epa.gov/smm/sustainable-materials-management-non-hazardous-materials-and-waste-management-hierarchy
  - Direct basics locator checked: https://www.epa.gov/smm/sustainable-materials-management-basics

**Wastewater**
- US EPA, Wastewater 101: The Fundamentals: the page describes converting wastewater back to water and the hydrologic cycle. It links a transcript and a PDF presentation; the Source record currently stores only the general page URI.
  - https://www.epa.gov/septic/wastewater-101-fundamentals
- WHO, Guidelines for the safe use of wastewater, excreta and greywater: the Source URI identifies the WHO guideline family. The current WHO sanitation-safety-planning page explains risk-based management along the sanitation chain: toilet, containment/storage/treatment, conveyance, treatment, end use or disposal; it also identifies local risk prioritisation, operational monitoring and regulatory oversight.
  - Canonical URI in Source: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/sanitation-safety/guidelines-for-safe-use-of-wastewater-greywater-and-excreta
  - Current related WHO locator checked: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/sanitation-safety/sanitation-safety-planning/
- US EPA, Municipal Wastewater: current page (last updated 10 March 2026) describes collection of domestic sewage/wastewater by sewers, delivery to treatment facilities, discharge or reuse, combined and separate sanitary sewer systems, infiltration/inflow, overflows, and NPDES discharge permits/limits/conditions. It links the Primer for Municipal Wastewater Treatment Systems (EPA 832-R-04-001, September 2004).
  - https://www.epa.gov/npdes/municipal-wastewater
- EPA Primer, Primer for Municipal Wastewater Treatment Systems, September 2004: pages 5–6 describe municipal collection and delivery to treatment; the Basic Wastewater Treatment Processes section (printed page 10; PDF page 9) directly describes physical, biological and chemical processes. Its contents and later sections also cover primary/secondary/advanced treatment, decentralized systems, onsite/septic treatment, operation and maintenance. The Primer is old and US-specific; it can support stable process fundamentals but not current universal regulatory requirements or current design parameters.
  - https://www.epa.gov/sites/default/files/2015-09/documents/primer.pdf

#### 26.4 Claim-level fit, boundary and evidence findings

1. **sanitation-basics**
   - Claim A's definition of sanitation as systems/services for safe management of human excreta and associated wastewater fits WHO's service-chain and safely managed sanitation framing.
   - Claim B's pathogen/exposure and environmental-contamination boundary is supported by WHO's disease and contamination discussion; the separate CDC EU adds independent support for the health/exposure aspect. Preserve the graph: CDC supports B only.
   - Claim C's local-condition, service-chain, infrastructure, operation/maintenance and safe end-use/disposal formulation is broadly consistent with WHO sanitation safety planning. However, its EU is generic and does not identify the relevant WHO sections. The WHO material supports risk-based local planning and the full service chain, but the Claim's combined list should be pinned to exact passages rather than treated as one undifferentiated definition.
   - Both WHO EUs use the generic text “Source supports the claim within the stated scope.” Only the CDC EU has substantive source-specific material. Context and Scope target Claim A only.
2. **waste-management-basics**
   - Claim A's collection, processing, recovery and safe disposal are broadly supported by UNEP's discussion of collection/disposal, recovery, recycling and integrated waste management.
   - Claim B's prevention/minimisation and material recovery are directly supported by UNEP's minimisation-first and recovery/recycling framing.
   - Claim C's dependence on waste composition, local infrastructure and impact risks is only partly covered by the current UNEP page: complexity and hazardous streams are discussed, but the precise local-infrastructure dependency is not established as a direct locator for this complete proposition.
   - The Source URI redirects to the current UNEP page; record the redirect/canonical destination in the Evidence Use locator during a controlled correction rather than treating the old path as a dead source. All three EUs remain broad descriptions and do not identify the supporting passages.
3. **waste-infrastructure-basics**
   - Claim A lists collection, transport, treatment, disposal and resource recovery. The stored EPA Source is only the general SMM landing page. EPA's specific hierarchy page directly supports reuse/recycling/composting, energy recovery, treatment and disposal, but it does not by itself establish the full infrastructure chain or collection/transport as framed in Claim A.
   - Claim B's materials-stream/local-condition formulation and Claim C's environmental/economic/operational constraints are too broad for the generic SMM landing-page EU descriptions. EPA's life-cycle page supports a materials life-cycle perspective, not every listed infrastructure design dependency.
   - This slice overlaps substantially with waste-management-basics. Keep a defensible distinction: waste-management-basics covers functions and decision hierarchy; waste-infrastructure-basics should cover physical assets, collection/transfer/treatment/disposal capacity and system constraints. Current Claims and the single broad EPA Source do not yet make that distinction evidence-tight.
4. **wastewater-basics**
   - Claim A's collection/treatment and return to the hydrologic cycle fits EPA Wastewater 101 and WHO's wastewater/sanitation-chain framing. EPA's current page is a presentation landing page; the exact supporting transcript/PDF passage should be identified in the EU.
   - Claim B's risk-reduction purpose is supported by WHO's safe-use and health-risk framing and EPA's wastewater fundamentals. The canonical graph correctly links each Claim to both EPA and WHO; the test explicitly requires both source identities for all three Claims.
   - Claim C's dependence on wastewater composition, system, intended use and local regulatory conditions is consistent with WHO's risk-based local planning and EPA's permit/discharge context, but the EU descriptions are generic and do not distinguish international health guidance from US regulatory examples.
   - P8's substantive and evidence-independence conclusions are reused. Remaining first-edition work is exact locator specificity and a clearer distinction from the separate engineering and treatment slices.
5. **wastewater-engineering-basics**
   - Claim A says wastewater engineering applies engineering methods to collection, treatment and management. EPA Municipal Wastewater directly documents sewer collection and delivery to treatment facilities; the linked Primer describes the collection/treatment system and operator/engineering functions. The current EU remains generic.
   - Claim B's physical/biological/chemical treatment processes are directly supported by the EPA Primer's Basic Wastewater Treatment Processes section (printed page 10; PDF page 9). This is a strong exact passage candidate.
   - Claim C combines influent characteristics, treatment objectives, hydraulics, climate, regulations, resources and receiving-environment constraints. EPA supports pollutant/contaminant variability, treatment objectives and discharge/receiving-water context, but the current single Source and generic EU do not establish every listed design variable, especially climate and resources. The Claim is broader than its demonstrated locator.
   - The current source family is US municipal wastewater guidance, and the Primer is from 2004. Use it for stable process fundamentals only; avoid presenting it as universal current design/regulatory guidance.
6. **wastewater-treatment-basics**
   - Claim A's physical, biological and chemical processes and pollutant reduction are directly supported by the EPA Primer's process section and the current Municipal Wastewater page's linked treatment overview.
   - Claim B's dependence on incoming wastewater characteristics and pollutants is supported in general by the Primer's discussion of changing contaminant character/quantity and treatment process selection. The EU should identify the relevant passages rather than only naming the Source.
   - Claim C's effluent requirements and discharge conditions are directly supported by EPA Municipal Wastewater's NPDES permits, discharge limits and conditions. This is explicitly a United States regulatory example, not a universal rule; the Claim must preserve that jurisdiction boundary or cite a broader international source.
   - The single Source is the same EPA Municipal Wastewater page used by wastewater-engineering-basics. This is valid reuse of a source, not independent corroboration. The EUs are generic and do not identify the Primer, permit section or relevant passages.

#### 26.5 Cross-slice integrity and first-edition decisions

- **Sanitation ↔ wastewater:** these are linked but not identical. Sanitation covers safe management of human excreta and the broader service chain; wastewater-basics focuses on wastewater collection/treatment and the hydrologic/health framing. The WHO source family supports both, but the reader-facing text must not collapse sanitation into sewered wastewater only; onsite systems, faecal sludge and non-sewered services remain in scope.
- **Waste management ↔ waste infrastructure:** the conceptual boundary is not sufficiently explicit. The first is about waste-management functions and hierarchy; the second should describe physical assets, collection/transfer/treatment/disposal capacity and system constraints. The current claims and broad sources overlap.
- **Wastewater basics ↔ engineering ↔ treatment:** the natural hierarchy is service/system overview → engineering discipline and design constraints → treatment processes and discharge requirements. Current Claims overlap, and the latter two both rely on the same EPA municipal page/Primer family. This is source reuse, not evidence independence.
- No canonical JSON was changed in this screen. No Claim was upgraded to INCLUDE. The presence of publication_status: published, completion_status: complete, valid record counts or passing topology tests does not establish first-edition eligibility.

**Decisions**
- **sanitation-basics: HOLD — all three Claims and dependency closures.** P3/P8 substantive results are reused. Blockers: generic WHO EU locators for A/C; CDC remains correctly limited to B; exact WHO passage pinpoints and Claim C's combined list require explicit source mapping.
- **waste-management-basics: HOLD — all three Claims and dependency closures.** UNEP broadly supports A/B; C's local-infrastructure dependency is not fully pinned. All EUs need exact section/passages; canonical URI should be normalized to the current redirect destination in a controlled edit.
- **waste-infrastructure-basics: HOLD — all three Claims and dependency closures.** The generic EPA SMM Source does not directly establish the full infrastructure chain and constraints; EUs are generic; conceptual separation from waste-management-basics is incomplete.
- **wastewater-basics: HOLD — all three Claims and dependency closures.** P8 substantive/evidence-independence results are reused. Remaining blockers: exact EPA/WHO passages in six generic EUs, current EPA transcript/PDF locator, and a tighter boundary against engineering/treatment.
- **wastewater-engineering-basics: HOLD — all three Claims and dependency closures.** Claim B has a direct EPA Primer passage; A is broadly supported; C over-combines design variables not all established by the current source. EUs are generic; source is US-specific and the Primer dates to 2004.
- **wastewater-treatment-basics: HOLD — all three Claims and dependency closures.** EPA directly supports the treatment-process and discharge framework, but EUs are generic, Claim C is US-regulatory in substance, and the slice boundary from wastewater-engineering-basics needs tightening.

No canonical JSON was changed. No INCLUDE assigned. P3/P8 substantive conclusions are preserved; the new first-edition decision remains stricter and record-level.


### 27. Agriculture, agrifood, soil, seed and energy foundations — nine-slice record-level block (2026-11-19; mixed Part I and ancillary screens)

This block reuses M1/M2/M4/R6/R12/P13 audit evidence where the exact slice is in scope. It does not treat a prior substantive PASS as automatic record-level publication approval.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| agriculture-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| agrifood-systems-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| agricultural-engineering-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| soil-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| soil-science-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| soil-microbiology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| seed-storage-basics | 10 | 2 | 3 | 3 | 1 | 1 |
| energy-security-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| energy-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **88** | **13** | **27** | **30** | **9** | **9** |

All Claim→Evidence Use→Source references and version-1 edges were inspected. Dedicated regressions enforce the slice-specific record counts, types, provenance and dependency coverage. They do not establish exact passage support, current Source URI validity, or substantive correctness.

#### Reused audits and exact checkpoint verification

- **M1 / seed-storage-basics**
  - `RELEASE/M1-SUBSTANTIVE-RE-AUDIT-2026-10-08.md`: 6/6 M1 debts closed, including seed-storage applicability boundary and independent agricultural evidence.
  - `RELEASE/M1-UNIFIED-DEBT-MAP-2026-10-08.md`: M1-03 closed; Human View PASS; no new Relation required.
  - Exact checkpoint commit `0019aa2376fd45ecc063f3f6ee680e087ab8d729` has exact-head Reference #2034, Release Gate #2321 and Offline #1503 all successful.
- **M2 / agriculture-basics and energy-security-basics**
  - `RELEASE/M2-SUBSTANTIVE-AUDIT-2026-10-08.md`: both slices PASS substantively; no Claim rewrite authorized.
  - `RELEASE/M2-EVIDENCE-INDEPENDENCE-AUDIT-2026-10-08.md`: agriculture-basics PASS with two source tracks; energy-security-basics originally had one IEA source and required an independent policy/operational track. The current tree now contains the European Commission source/EU record, bounded to EU policy context.
  - `RELEASE/M2-HUMAN-VIEW-AUDIT-2026-10-08.md`: both slices PASS; no individualized agronomic or local-grid instruction.
  - `RELEASE/M2-POST-CORRECTION-SUBSTANTIVE-AUDIT-2026-10-08.md`: confirms agriculture and energy-security substantive PASS.
  - Exact M2 checkpoint commit `bfd0578ca6f8dae9093a96de4f2bf6139589a40f` has exact-head Reference #2153, Release Gate #2440 and Offline #1622 all successful.
  - **Scope caution:** the inspected M2 reports do not all describe the same target set. The six-slice post-correction audit includes agriculture and energy security; the separate M2 unified debt map lists a ten-slice scope including agrifood systems. A closure in one M2 artifact must not be transferred to a different slice unless that slice is actually named in the corresponding audit/debt map.
- **M2 / agrifood-systems-basics**
  - `RELEASE/M2-UNIFIED-DEBT-MAP-2026-10-08.md`: M2-08 single-source/system-causal boundary marked CLOSED after an independent World Bank source and bounded causal framing.
  - This closure is retained as historical audit evidence, but the current World Bank Source page was re-opened and found to be a broad FoodSystems 2030 programme page, not a direct definition/technical passage for all current Claim wording. This new record-level source-fit discrepancy requires a targeted re-audit; it does not invalidate the historical M2 work.
- **M4 / agricultural-engineering-basics**
  - `RELEASE/M4-SUBSTANTIVE-AUDIT-2026-10-08.md`: MATURATION REQUIRED; specifically flags source-to-Claim alignment because the registered FAO land/water source may not support machinery, storage and processing assertions. M4 remains open. No M4 CLEAN or exact 3/3 checkpoint is claimed.
- **R6 / soil-science-basics**
  - `RELEASE/FULL-CORPUS-AUDIT-2026-10-03-R6.md`: soil-science-basics included in the 10-slice R6 substantive/evidence/Human View PASS.
  - Exact R6 checkpoint commit `ade2d4e66dc36a8c6c0fc8c736cb651d9ce94bcb` has exact-head Reference #823, Release Gate #1042 and Offline #201 all successful.
- **R12 / soil-microbiology-basics**
  - `RELEASE/CONTENT-GAP-MAP-2026-10-04-R12.md` selects soil-microbiology-basics as one of ten planned slices and specifies a 9-record contract. The inspected R12 artifact is a scope/gap map, not a substantive audit or approval. No substantive/Human View closure was located in the inspected release artifacts.
- **P13 / energy-systems-basics**
  - `RELEASE/P13-FINAL-MATURATION-RE-AUDIT-2026-10-07.md`: energy-systems-basics listed as NO-CHANGE among ten existing targets; no substantive regression identified.
  - P13 is an integration audit anchored to P12 CLEAN, not a new dedicated energy-systems checkpoint. Its NO-CHANGE result does not remove the current Source URI/pinpoint and language issues below.
- **soil-basics**: not named in the inspected R6/M1/M2/M4/R12/P13 substantive target lists. Do not borrow the R6 soil-science PASS or R12 soil-microbiology scope as an audit of soil-basics.

#### Direct source passage checks

- FAO “Agriculture” URI currently stored in agriculture-basics:
  - `https://www.fao.org/agriculture/` returned HTTP 404 in the live check.
  - USDA Climate Hubs “Manage crops to cope with warmer and drier conditions” directly supports climate/soil/water/crop management dependence and location/commodity variation, but it does not replace a valid FAO general agriculture source for Claim A.
  - URL: https://www.climatehubs.usda.gov/approach/manage-crops-cope-warmer-and-drier-conditions
- FAO “Agrifood Systems”:
  - directly defines agrifood systems as people, activities, investments and choices involved in producing/delivering food and agricultural goods; explicitly lists growing, harvesting, processing, packaging, transport, distribution, trade, purchase, preparation, consumption and disposal.
  - URL: https://www.fao.org/food-systems/en
- World Bank “FoodSystems 2030” current Source URI:
  - describes a multi-donor trust fund supporting country-led food-system transformation and SDG progress; the landing page does not itself provide a claim-level definition of the whole food chain or independently substantiate all current system/causal wording.
  - URL: https://www.worldbank.org/en/programs/food-systems-2030
- FAO Land and Water Management Source URI for agricultural engineering:
  - `https://www.fao.org/land-water/land/soil-water-management/en/` could not be retrieved in the live check.
  - The M4 audit's source-fit concern remains open; no inference is made that this source supports machinery, storage and processing.
- USDA NRCS “What is Soil?”:
  - defines soil as mineral/organic solids, liquids and gases; explains soil horizons and the influence of climate, relief and living organisms; describes soil functions including sustaining life, regulating water, filtering/buffering pollutants and nutrient cycling.
  - URL: https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil
  - The current soil-basics Source URI `https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/soils` could not be retrieved; the above is a better exact source candidate but is not currently the canonical Source URI.
- FAO SOILS PORTAL “Soil properties”:
  - explicitly says soil quality includes physical, chemical and biological properties; quality varies with management; soil quality has inherent and dynamic characteristics; defines soil health by productivity, diversity and ecosystem services.
  - URL: https://www.fao.org/soils-portal/data-hub/soil-properties/en/
- USDA NRCS “Soil Health Starter Kit”:
  - pp. 1–2 / PDF lines 4–19: soil is a living ecosystem containing bacteria, fungi and other organisms; it cycles nutrients, absorbs/drains/retains water and supports biological diversity;
  - PDF lines 102–124: biodiversity includes plants, animals and microorganisms; microbial diversity contributes to soil health.
  - URL: https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil-Health-Starter-Kit-reduced.pdf
- University of Minnesota Extension “Saving vegetable seeds”:
  - lines 241–247: seed-saving depends on plant type and life cycle;
  - lines 309–314: seeds should be stored dry/cool and labelled with name, variety and collection date; germination/vigor decline with age.
  - URL: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/saving-vegetable-seeds
- The current USDA NRCS seed source `https://www.nrcs.usda.gov/plant-materials/using-seed-to-save-seeds` was not retrievable in the live check. Do not silently substitute the UMN source for the USDA Source record. UMN is Minnesota vegetable-seed guidance and does not establish universal conditions for all agricultural, native or wild seed species.
- IEA “Energy Security”:
  - lines 40–48: reliable, affordable access to fuels and energy sources; IEA monitors geopolitical risks, cyberattacks, supply-chain disruptions and extreme weather;
  - lines 82–90: electricity security risks, system flexibility, storage, supply chains and resilience to cyberattacks/extreme weather.
  - URL: https://www.iea.org/topics/energy-security
- European Commission DG Energy “In focus: EU energy security explained”:
  - dated 20 April 2026; defines security of supply as sufficient supplies, describes geopolitical, cyber and physical threats, extreme weather, preparedness, diversification, storage and EU crisis-coordination mechanisms.
  - The EU context is explicit and must remain bounded to EU policy, not universalized.
  - URL: https://energy.ec.europa.eu/news/focus-eu-energy-security-explained-2026-04-20_en
- IEA “Energy system”:
  - the current official page is `https://www.iea.org/energy-system`, with sections “Energy Supply & Transformation” and “Uses of Energy” (transport, industry, buildings);
  - the current canonical Source URI in energy-systems-basics is `https://www.iea.org/topics/energy-system`, which was not accessible in the live check. The current page is a better Source locator but its high-level taxonomy alone does not pinpoint every Claim component, especially storage and demand.
  - URL: https://www.iea.org/energy-system

#### Claim-level fit, overlap and boundary findings

1. **agriculture-basics**
   - M2 substantive, evidence-independence and Human View work is reused; two source records are present and the USDA Climate Hubs line is claim-specific.
   - The FAO Source URI for the broad agriculture definition is dead (404). USDA climate-adaptation material supports the environmental/management context, not the full Claim A definition.
   - EU descriptions remain generic. Repair the FAO Source URI through a controlled version/source correction and add exact FAO/USDA locators.
2. **agrifood-systems-basics**
   - FAO directly supports the system definition and the chain of activities from production to disposal.
   - The World Bank programme landing page does not itself substantiate all Claim wording. This conflicts with the M2 debt map's recorded closure of the independent systems-evidence debt; reopen only this source-fit point, not the entire M2 substantive audit.
   - The FAO page is also used by food-systems-basics and food-distribution-basics. This is not automatically a defect, but the agrifood-specific role must remain the broad agricultural-food system definition and transformation layer, not duplicate food-systems or distribution Claims.
   - P13 explicitly treats the agricultural production chain as integration/targeted deepening rather than a reason for another generic standalone system layer. Keep this boundary visible; do not create metric-only Relations.
3. **agricultural-engineering-basics**
   - M4 expressly identifies source-to-Claim mismatch: FAO land/water management does not visibly cover all machinery, irrigation, drainage, storage and processing subdomains.
   - This is not a closed audit. The current Source URL was not retrievable; Claims cannot be accepted until each asserted subdomain has direct evidence or is narrowed.
   - The slice is not an operational manual for machinery, irrigation, drainage, storage or processing.
4. **soil-basics**
   - The current NRCS Source URI could not be retrieved. NRCS “What is Soil?” directly supports the basic definition and core functions and is a precise replacement candidate.
   - The current EUs are generic. Claim C's spatial/depth variation needs the relevant soil horizons/classification passage, not just a general definition.
   - Soil-basics is the general introductory layer; soil-science-basics is the more specific properties/quality/functions layer. Keep them distinct and avoid duplicate Claims.
5. **soil-science-basics**
   - The current FAO page directly supports physical/chemical/biological properties and inherent/dynamic quality characteristics.
   - Claim C lists functions including productivity, water regulation, nutrient cycling, biodiversity and ecosystem services. The top-level FAO page directly mentions productivity, diversity and ecosystem services, while the more detailed functional items require exact linked property/function passages.
   - All three Claims are in English; review Russian-first edition consistency. EU descriptions are generic.
6. **soil-microbiology-basics**
   - The current USDA NRCS PDF directly supports all three high-level Claims: soil microbial community, decomposition/nutrient cycling, and biodiversity as part of soil ecosystem function.
   - The 9-record R12 contract is structurally complete, but the inspected R12 document is only a gap map. No substantive/Human View audit was located.
   - All three EU descriptions identify the same PDF but do not give page/paragraph locators. The current Scope is foundational and correctly excludes exhaustive/specialized use.
7. **seed-storage-basics**
   - M1 substantive, evidence-independence and Human View debts are closed; exact M1 checkpoint is 3/3.
   - UMN Extension directly supports seed-type differences, dry/cool storage and labeling by name/variety/date. Its page is specifically about vegetable seed saving in Minnesota.
   - The USDA NRCS Source URI used for Claims B/C could not be retrieved. Claim C says identify crop and batch/lot; the UMN page explicitly says name, variety and date, not batch/lot. The current USDA line cannot be treated as proven without a working locator.
   - Context/Scope target Claim B (dry storage) only. They do not automatically extend to Claim A (seed applicability) or Claim C (labeling).
   - The Claim's general statement must not be converted into one universal temperature/humidity prescription for all species or seed types.
8. **energy-security-basics**
   - IEA directly supports reliable/affordable access and the named threat classes. The European Commission source provides a second institutional track for supply-security/preparedness/resilience and is correctly bounded to EU policy.
   - The additional EU Evidence Use currently targets Claim A only; do not borrow it for Claims B/C. IEA supports the threat categories in B, while Claim C's fuel/infrastructure/time-horizon/region formulation needs a precise IEA passage.
   - All EU descriptions are generic. The current Source pair is valid and independent, but exact locator work remains.
9. **energy-systems-basics**
   - P13 recorded NO-CHANGE and found no substantive regression. The current IEA Source URI is stale/unavailable; the current IEA page is a better source locator but its top-level headings do not by themselves pinpoint all Claim components.
   - All Claims are English while the encyclopedia's primary reader-facing language is Russian. EUs are generic.
   - Keep the slice as a foundational system architecture layer; do not duplicate energy-security risk concepts or electricity-grid operational instructions.

#### Decisions

- **agriculture-basics: HOLD — all three Claims and dependency closures.** M2 substantive/evidence/Human View and exact checkpoint are reused; current FAO Source URI returns 404 and exact EU locators are missing.
- **agrifood-systems-basics: HOLD — all three Claims and dependency closures.** Historical M2 closure is preserved, but the current World Bank programme Source is not claim-level evidence for all asserted system/causal material; targeted source-fit re-audit and exact FAO/World Bank locators required.
- **agricultural-engineering-basics: HOLD — all three Claims and dependency closures.** M4 remains open; explicit source-to-Claim alignment debt is unresolved.
- **soil-basics: HOLD — all three Claims and dependency closures.** Current NRCS Source URI is not retrievable; exact locator/source correction required.
- **soil-science-basics: HOLD — all three Claims and dependency closures.** R6 substantive/evidence/Human View and exact 3/3 checkpoint are closed; remaining blockers are exact FAO function/property locators and Russian-first editorial consistency.
- **soil-microbiology-basics: HOLD — all three Claims and dependency closures.** R12 selected the slice but no substantive/Human View closure was located; exact USDA PDF locators and full audit required.
- **seed-storage-basics: HOLD — all three Claims and dependency closures.** M1 substantive/evidence/Human View and exact 3/3 checkpoint are closed; remaining blockers are non-retrievable USDA Source URI, claim-to-source locator fit for labeling/batch language, and Claim-A/C applicability not covered by Claim-B Context/Scope.
- **energy-security-basics: HOLD — all three Claims and dependency closures.** M2 substantive/Human View and exact checkpoint are reused; the IEA/European Commission source pair exists, but EU locators are generic and the EU source is limited to Claim A.
- **energy-systems-basics: HOLD — all three Claims and dependency closures.** P13 NO-CHANGE is reused; current IEA Source URI is not retrievable, EU locators are generic and English-language Claims need Russian-first editorial review.

No canonical JSON changed in this screen.


### 28. Electricity, energy, storage, electrical machines, power electronics and power systems — seven-slice block (2026-11-19; mixed Part I and ancillary screens)

This block checks seven related slices and reuses prior M1/M3/P1/R6/R12 evidence. It does not repeat closed audits. It checks exact Claim/EU/Source paths, current source locators, technical scope and cross-slice duplication.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| electricity-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| energy-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| energy-storage-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| electrical-machines-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| power-electronics-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| power-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| electrical-safety-basics | 15 | 3 | 5 | 5 | 1 | 1 |
| **Total** | **69** | **9** | **23** | **23** | **7** | **7** |

The six 9-record slices have one Source, three Claims, three Evidence Use, Context and Scope. Electrical safety has 15 records: 3 Sources, 5 Claims, 5 Evidence Use, Context and Scope. All exact Claim→EU→Source edges were inspected. Dedicated tests check record counts/types and dependency topology, not exact passage locators or cross-record semantic duplication.

#### Reused audits and checkpoint evidence

- **P1 / electrical-safety-basics**
  - `RELEASE/MATURATION-AUDIT-2026-10-05.md`: the high-consequence slice was previously matured; NIOSH and genuinely independent OSHA evidence were intended to close the earlier provenance defect. P1 content/Human View and cross-domain maturation are closed.
  - The exact P1 checkpoint commit `0169c9189cf2867a4387c46f8d71f1af64260adf` has exact-head Reference #1542, Release Gate #1835 and Offline #1011 all successful.
  - The current record graph is narrowly re-opened below because the supposed correction still leaves duplicate NIOSH Source records and attaches the OSHA evidence to a parallel English Claim instead of the corresponding Russian Claim. This is a verified record-graph defect, not a reason to repeat the whole P1 audit.
- **R6 / power-electronics-basics**
  - `RELEASE/FULL-CORPUS-AUDIT-2026-10-03-R6.md`: included in the R6 full-corpus substantive/evidence/Human View PASS.
  - Exact R6 checkpoint commit `ade2d4e66dc36a8c6c0fc8c736cb651d9ce94bcb` has exact-head Reference #823, Release Gate #1042 and Offline #201 all successful.
- **R12 / electrical-machines-basics and power-systems-basics**
  - `RELEASE/CONTENT-GAP-MAP-2026-10-04-R12.md` selects both as planned 9-record foundational slices. The inspected R12 artifact is a gap map, not a substantive/Human View approval. Do not treat R12 selection as a PASS.
- **M3 / energy-basics**
  - `RELEASE/M3-MATURATION-SCOPE-2026-10-08.md` says energy-basics was screened but not selected: kinetic energy, potential energy and work are basic physics concepts, and the 9/1 structural profile alone did not justify a separate high-priority maturation asymmetry. This is not a record-level source-locator audit.
- **Other four slices**
  - No dedicated substantive audit was located in the inspected release artifacts for electricity-basics, energy-storage-basics or the current record-level profile of power-systems-basics. The source/record screen below is not a substitute for the required substantive/Human View gate.
  - Exact P1/R6/M1/M2 checkpoints previously recorded in sections 22 and 25 remain the only checkpoint evidence used here.

#### Direct source passage checks

- U.S. DOE, “Electricity”:
  - electricity powers homes, businesses and critical infrastructure in the United States;
  - electricity moves from power plants through transmission lines, substations and distribution systems;
  - grid operators continuously balance supply and demand and monitor system conditions in real time.
  - URL: https://www.energy.gov/topics/electricity
- OpenStax physics:
  - kinetic energy is (K=\frac12 mv^2) for non-relativistic motion;
  - potential energy is stored energy associated with position/configuration;
  - work is energy transfer through force acting over displacement.
  - The current Source URI in energy-basics is `https://openstax.org/books/physics/pages/9-introduction-to-work-energy-and-energy-resources`, which was not retrievable in the live check. More precise OpenStax sections were found:
    - https://openstax.org/books/college-physics/pages/7-2-kinetic-energy-and-the-work-energy-theorem
    - https://openstax.org/books/college-physics/pages/9-1-work-power-and-the-work-energy-theorem
  - These are candidate pinpoint/source locators; do not silently replace the current Source URI.
- U.S. DOE, “Solar Integration: Solar Energy and Storage Basics”:
  - section “What Is Energy Storage?” defines capture, storage in another form and later release; explicitly identifies chemical, thermal and mechanical storage and energy/power capacity;
  - later sections describe conversion losses and technologies including pumped hydro, batteries, thermal storage, flywheels and compressed air.
  - URL: https://www.energy.gov/cmei/systems/solar-integration-solar-energy-and-storage-basics
- U.S. DOE, “Electric Motors”:
  - line 7 defines an electric motor as a machine converting electrical power to rotational mechanical power;
  - lines 66–69 identify U.S. DOE energy conservation standards and test procedures under 10 CFR 431;
  - lines 74–81 cover labeling, records and certification requirements.
  - The page explicitly applies to specified motor categories under U.S. federal regulation and excludes other categories.
  - URL: https://www.energy.gov/cmei/buildings/electric-motors
- U.S. DOE, “Power Electronics and Balance of System Hardware Technologies”:
  - lines 8–13 describe PV inverters converting DC to AC, setting current/voltage and matching AC to the utility network;
  - lines 27–31 describe inverter/grid compatibility, interoperability, ride-through and reliability.
  - The page is explicitly about solar photovoltaic power electronics and was last updated in 2014.
  - URL: https://www.energy.gov/cmei/systems/power-electronics-and-balance-system-hardware-technologies
- NREL, “The North American Electric Power System: The Grid”:
  - current Source URI: https://docs.nrel.gov/docs/fy12osti/52409-4.pdf
  - the direct live fetch returned HTTP 502. Do not treat the NREL passage as independently re-read in this screen; the current EU only identifies the report and contains no page/section locator.
- CDC/NIOSH, “Electrical Safety in the Workplace”:
  - key points say only qualified people should work on energized equipment using appropriate PPE; identifies electric shock, burns, arcing and fire; says unqualified persons should not work on energized parts.
  - URL: https://www.cdc.gov/niosh/electrical-safety/about/
- OSHA, 29 CFR 1910.333:
  - paragraph (c)(2) says only qualified persons may work on circuit parts/equipment that have not been de-energized under the specified procedures, and requires relevant precautions/PPE/insulated tools.
  - URL: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333

#### Claim-level fit, overlap and boundary findings

1. **electricity-basics**
   - DOE directly supports all three Claims: critical infrastructure, generation/transmission/substations/distribution, and continuous supply-demand balancing.
   - The Source is explicitly U.S.-specific. The Claims read generally; the reader-facing text must either label this as a U.S. example or add an international source.
   - The EUs say only that the DOE page is used “within the specified material”; they do not point to the exact DOE paragraphs. Context/Scope target Claim A only.
2. **energy-basics**
   - The three Russian Claims are basic physics definitions and are not a high-consequence operational instruction.
   - OpenStax directly supports the concepts, but the current Source URI was not retrievable and the EUs contain no section locators. A precise OpenStax source/section chain is needed. Context/Scope target Claim A only; do not infer that formulas are valid outside their stated physical assumptions.
3. **energy-storage-basics**
   - DOE directly supports all three Claims at a high level: capture/store/release; energy capacity versus power capacity; conversion losses and different technologies/constraints.
   - The source is a solar-integration page, but it explicitly defines energy storage generally and then gives multiple technologies. The Claim C wording is broader than the examples, so the EU must identify the general definition and technology sections rather than imply an exhaustive catalogue.
   - The EUs are generic. Context/Scope target Claim A only; no technology-specific safety or installation instructions are included.
4. **electrical-machines-basics**
   - DOE directly supports Claim A and the U.S. regulatory requirements/testing in Claims B/C.
   - The page applies to specified U.S. motor categories and explicitly excludes small motors and dedicated-purpose pool-pump motors. The reader-facing text must not imply that DOE rules are global or apply to every motor.
   - Context/Scope target Claim A only, while Claims B/C are explicitly regulatory and jurisdiction-dependent. Add a clear U.S./10 CFR 431 boundary and exact regulatory locators.
5. **power-electronics-basics**
   - DOE directly supports the PV-inverter conversion mechanism, voltage/current control and grid matching.
   - It does **not** establish the full breadth of Claim C across transportation, industrial systems, consumer devices and all renewable-energy/grid applications. The page is solar-PV-specific and dates to 2014.
   - Claim A's “solid-state switching” and the general scope of Claim B also need a source that treats power electronics as a broader engineering field, not only PV inverters.
   - R6 PASS is preserved, but the current first-edition record-level screen identifies a source-scope mismatch that must be resolved by narrowing Claims or adding a genuinely broad source line.
6. **power-systems-basics**
   - Claim A is consistent with basic grid architecture, and DOE's Electricity page supports generation/transmission/distribution and balancing.
   - Claim B adds measurement, information and control systems; the current NREL Source is the only linked evidence for that systems-of-systems wording and could not be retrieved in this check.
   - Claim C's load variability and equipment-failure interaction needs an exact NREL/other authoritative locator. The generic EU description does not identify the passage.
   - This slice overlaps electrical-grid-basics, but has a distinct possible role: broader system-of-systems architecture, monitoring/control and balancing. Preserve that distinction; do not repeat the simpler grid component Claim.
7. **electrical-safety-basics**
   - NIOSH directly supports Russian Claims A–C at a high level; OSHA 1910.333 directly supports qualified-person and energized-work requirements.
   - Two current Source records point to the **same exact NIOSH URL** and represent the same CDC/NIOSH source:
     - `SRC-ELECTRICAL_SAFETY_BASICS@1` → `https://cdc.gov/niosh/electrical-safety/about/`
     - `SRC_ELECTRICAL_SAFETY_NIOSH@1` → the same URL.
     - Their source identities differ only in wording (“Электробезопасность: CDC/NIOSH” vs “CDC/NIOSH — Electrical Safety”). They are not independent evidence tracks.
   - The P1 maturation report says the duplicate provenance defect was corrected. The exact current record inventory shows that the duplicate Source representation remains. Preserve historical records; do not silently delete/merge them. This is a narrow, verified record-graph discrepancy against the prior closure report.
   - The independent OSHA line is attached to `CLM-ELECTRICAL_SAFETY_OSHA_A@1`, a separate English Claim, rather than as an additional Evidence Use to the Russian Claim `CLM-ELECTRICAL_SAFETY_BASICS-B@1`. Thus the OSHA source is independent, but it does not triangulate the Russian Claim B through the current dependency graph.
   - `CLM-ELECTRICAL_SAFETY_NIOSH_A@1` is an English restatement of the Russian hazard Claim A; `CLM-ELECTRICAL_SAFETY_OSHA_A@1` is a more specific English regulatory restatement of Russian Claim B. The slice currently has five Claims, not just the three core Russian Claims.
   - Context/Scope target only the Russian Claim A. The safety boundary is relevant to all Claims, including the two English Claims, and must not be silently inherited.
   - Do not add operational electrical-work instructions. The current high-level safety boundary is appropriate; only the source graph, locators and applicability records need controlled reconciliation.

#### Decisions

- **electricity-basics: HOLD — all three Claims and dependency closures.** DOE source supports the content; remaining blockers are exact paragraph locators and explicit U.S. boundary.
- **energy-basics: HOLD — all three Claims and dependency closures.** OpenStax supports the physics concepts, but the current Source URI is not retrievable and exact section locators are absent.
- **energy-storage-basics: HOLD — all three Claims and dependency closures.** DOE supports the general storage concepts; exact section locators and a non-exhaustive/solar-source boundary are needed.
- **electrical-machines-basics: HOLD — all three Claims and dependency closures.** DOE supports the claims, but the U.S. regulatory category and exclusions must be explicit; no R12 substantive/Human View closure located.
- **power-electronics-basics: HOLD — all three Claims and dependency closures.** R6 PASS is reused; the current DOE source is PV-inverter-specific and does not support the full scope of Claim C or the broad wording of A/B.
- **power-systems-basics: HOLD — all three Claims and dependency closures.** R12 gap-map selection is not approval; NREL source could not be retrieved, exact locators are missing, and Claim B's system-of-systems mechanism remains unverified in the current source chain.
- **electrical-safety-basics: HOLD — all five Claims and dependency closures pending a narrow graph correction.** P1 substantive/Human View and exact 3/3 checkpoint remain closed; the duplicate NIOSH Source records and separate English OSHA Claim prevent the intended independent evidence from being cleanly attached to the Russian Claim graph.

No canonical JSON changed in this screen.


### 29. Controlling Part I scope reconciliation and record-level progress (2026-11-19)

The controlling scope remains `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md`: **94 vertical slices and 980 record files**. This is the first-edition denominator. The broader repository, M4/M5 gap maps and ancillary screens are not allowed to silently expand the Part I denominator.

#### Part I record-level progress

- **94 of 94 Part I slices** now have an exact-record screen or a reused exact-version manifest in this register.
- Those 94 slices contain **980 of 980 Part I record files**.
- **0 slices / 0 record files** remain at filename-inventory level in the controlling Part I inventory.
- All 94 screened Part I slices remain **HOLD**. No public INCLUDE is assigned by this progress update.
- The 9-slice exact-version manifest (112 records) is reused, not repeated. The 85 additional exact-record screens account for the remaining 868 records in the 94-slice screened set.
- Prior substantive audits, Human View results and exact-head CI checkpoints are reused where cited. A PASS in those gates does not replace the current record-level source-locator and applicability checks.

#### Exact-screened Part I slices

1. `emergency-alert-warning` — exact-version manifest; §§8, 22.
2. `hand-tool-safety` — exact-version manifest.
3. `home-fire-smoke-safety` — exact-version manifest.
4. `emergency-lighting-safety` — exact-version manifest.
5. `septic-system-emergency` — exact-version manifest.
6. `food-safety-basics` — exact-version manifest and current record-level screen; §25.
7. `food-preservation-basics` — exact-version manifest and current record-level screen; §25; README synchronized.
8. `flood-food-safety` — exact-version manifest.
9. `power-outage-food` — exact-version manifest.
10. `water` — §10.
11. `chemical-water-advisory` — §11.
12. `burn-first-aid` — §12.
13. `generator-carbon-monoxide-safety` — §13.
14. `disaster-response-basics` — §14.
15. `emergency-management-basics` — §16.
16. `disaster-risk-reduction-basics` — §17.
17. `humanitarian-logistics-basics` — §18.
18. `water-resources-basics` — §23.
19. `water-treatment-basics` — §§4, 23.
20. `water-infrastructure-basics` — §23.
21. `food-security-basics` — §25.
22. `nutrition-basics` — §25.
23. `sanitation-basics` — §26.
24. `waste-management-basics` — §26.
25. `wastewater-basics` — §26.
26. `wastewater-engineering-basics` — §26.
27. `agriculture-basics` — §27.
28. `soil-basics` — §27.
29. `seed-storage-basics` — §27.
30. `energy-systems-basics` — §27.
31. `electricity-basics` — §28.
32. `electrical-safety-basics` — §28.
33. `energy-basics` — §28.
34. `energy-storage-basics` — §28.
35. `water-filter-assessment` — §30.
36. `emergency-water-storage-state` — §30.
37. `emergency-hand-hygiene` — §30.
38. `emergency-waste-sanitation` — §30.
39. `hydrology-basics` — §30.
40. `shelter-basics` — §31.
41. `fire-safety-basics` — §31.
42. `wildfire-smoke-safety` — §31.
43. `extreme-heat-safety` — §31.
44. `cold-weather-hypothermia` — §31.
45. `carbon-monoxide-heating-safety` — §31.
46. `weather-basics` — §31.
47. `food-science-basics` — §33.
48. `nutrition-science-basics` — §33.
49. `public-health-basics` — §33.
50. `environmental-health-basics` — §33.
51. `anatomy-basics` — §33.
52. `physiology-basics` — §33.
53. `microbiology-basics` — §33.
54. `epidemiology-basics` — §33.
55. `sleep-basics` — §33.
56. `construction-basics` — §34.
57. `housing-systems-basics` — §34.
58. `architecture-basics` — §34.
59. `civil-engineering-basics` — §34.
60. `human-settlement-systems-basics` — §34.
61. `early-agriculture` — §35.
62. `plant-biology-basics` — §35.
63. `plant-physiology-basics` — §35.
64. `forestry-basics` — §35.
65. `fisheries-basics` — §35.
66. `livestock-systems-basics` — §35.
67. `zoology-basics` — §35.
68. `ecology-basics` — §35.
69. `ecosystems-basics` — §35.
70. `food-fermentation-basics` — §35.
71. `fire` — §36.
72. `renewable-energy-basics` — §36.
73. `materials-basics` — §36.
74. `materials-science-basics` — §36.
75. `manufacturing-basics` — §36.
76. `manufacturing-systems-basics` — §36.
77. `robotics-basics` — §36.
78. `earthquake-protective-action` — §37.
79. `earthquake-aftershock-safety` — §37.
80. `flood` — §37.
81. `flood-cleanup-safety` — §37.
82. `climate-basics` — §37.
83. `geology-basics` — §37.
84. `seismology-basics` — §37.
85. `volcanology-basics` — §37.
86. `ocean-basics` — §37.
87. `maps-and-navigation-basics` — §39.
88. `geographic-coordinates-basics` — §39.
89. `telecommunications-basics` — §39.
90. `networks-basics` — §39.
91. `public-risk-communication-basics` — §39.
92. `transportation-basics` — §39.
93. `public-transport-basics` — §39.
94. `infrastructure-basics` — §39.
#### Ancillary screens outside the 94-slice Part I denominator

These screens are retained as useful wider-encyclopedia work, but **they are not Part I candidates and are not counted in the 86/94 progress above**:

- `disaster-response-logistics-basics` — §15.
- `disaster-recovery-basics`, `electrical-grid-basics`, `infrastructure-resilience-basics` — §§19–21.
- `water-quality-basics`, `water-security-basics`, `water-resource-management-basics` — §23.
- `food-systems-basics`, `food-distribution-basics` — §§24–25. Section 24 is explicitly superseded by the expanded Section 25; do not count both as separate screens.
- `waste-infrastructure-basics`, `wastewater-treatment-basics` — §26.
- `agrifood-systems-basics`, `agricultural-engineering-basics`, `soil-science-basics`, `soil-microbiology-basics`, `energy-security-basics` — §27.
- `electrical-machines-basics`, `power-electronics-basics`, `power-systems-basics` — §28.
- Section 32 is a superseded working screen for the overlapping hazard slices; it is retained for traceability but is not counted separately from Section 31.

These ancillary screens must not be used to claim that Part I is complete. Conversely, their findings remain useful for later volumes and cross-slice consistency.

#### Remaining Part I work

The next passes must continue from the 8 unscreened Part I slices in the controlling inventory, not from the ancillary list above. Priority order should be determined by first-edition dependency closure and consequence: remaining health and first-aid topics; communications/transport; any remaining energy and infrastructure topics.

No canonical JSON changed in this scope reconciliation.
### 30. Emergency water filters, stored water, hand hygiene and waste sanitation — five-slice block (2026-11-19)

All five slices are Part I candidates in the controlling 94-slice inventory. Hydrology-basics also supplies the other endpoint of the M3 water-resources Relation. The P3/P4/R23 substantive and technical checkpoints are reused. This screen checks current source passages and exact dependency edges.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

**31.1 water-filter-assessment — 11 records (Part I)**
- Claims: `CLM-WATER-FILTER-LIMITS@1`, `CLM-WATER-FILTER-WHO-PERFORMANCE@1`.
- Evidence Use: `EU-WATER-FILTER-LIMITS@1` → `SRC-CDC-WATER-FILTER-2025@1`; `EU-WATER-FILTER-WHO-PERFORMANCE@1` → `SRC-WHO-HWT-EVALUATION@1`.
- Context/Scope: `CTX-WATER-FILTER@1`, `SCP-WATER-FILTER@1`.
- Additional epistemic records: `ASM-WATER-FILTER-APPLICABILITY@1`, `INF-WATER-FILTER-NOT-UNIVERSAL@1`, `ACTOR-WATER-FILTER-ANALYST@1`.
- The dedicated test checks the 11-record profile, Assessment target, Inference premises, attribution and limitations, plus publication-package preservation of citations.

**31.2 emergency-water-storage-state — 12 records (Part I)**
- Claim: `CLM-WATER-STORAGE-CONTAINER@1`.
- Evidence Use: `EU-WATER-STORAGE-CONTAINER@1` → `SRC-CDC-WATER-STORAGE-2025@1`; `EU-EPA-EMERGENCY-WATER-STORAGE@1` → `SRC-EPA-EMERGENCY-WATER-SUPPLY-2011@1`.
- Context/Scope: `CTX-WATER-STORAGE-EMERGENCY@1`, `SCP-WATER-STORAGE-EMERGENCY@1`.
- Object/State/Relation/Identity: `OBJ-WATER-CONTAINER@1`; `ST-WATER-CONTAINER-SANITIZED@1`; `ST-WATER-CONTAINER-STORED@1`; `REL-CONTAINER-WATER-STORAGE@1`; `ID-WATER-CONTAINER-CONTINUITY@1`.
- The dedicated test checks 12 records, schema/semantic validity, both State subject references to the same Object, two Relation participants and Identity continuity/uncertainty.

**31.3 hydrology-basics — 9 records (ancillary; not Part I)**
- Claims: `CLM-HYDROLOGY_BASICS-A@1`, `...-B@1`, `...-C@1`.
- Evidence Use: `EU-HYDROLOGY_BASICS-A@1`, `...-B@1`, `...-C@1` → `SRC-HYDROLOGY_BASICS@1`.
- Context/Scope: `CTX-HYDROLOGY_BASICS@1`, `SCP-HYDROLOGY_BASICS@1`.
- The dedicated test checks the 9-record profile, one Source and complete Claim→EU→Source links.
- The M3 water-resources ↔ hydrology Relation is preserved; no duplicate Relation is created.

**31.4 emergency-hand-hygiene — 11 records (Part I)**
- Claim: `CLM-HANDWASH-20SEC@1`.
- Evidence Use: `EU-HANDWASH-20SEC@1` → `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1`; `EU-HANDWASH-20SEC-WHO@1` → `SRC-WHO-HYGIENE-EMERGENCY-2013@1`.
- Context/Scope: `CTX-HANDWASH-EMERGENCY@1`, `SCP-HANDWASH-EMERGENCY@1`.
- Process/Action/Result: `PRC-HANDWASH-SOAP-WATER@1`; `ACT-HANDWASH-WET-SOAP@1`; `ACT-HANDWASH-SCRUB-20SEC@1`; `RES-HANDWASH-CLEANING@1`.
- The dedicated test checks the 11-record profile, schema/semantic validity and the Process→Action→Result reference frame.

**31.5 emergency-waste-sanitation — 12 records (Part I)**
- Claims: `CLM-WASTE-ASSESS-STREAMS@1`, `CLM-WASTE-HAND-HYGIENE@1`, `CLM-WASTE-HAZARDOUS-ESCALATION@1`, `CLM-WASTE-SANITARY-HANDLE@1`.
- Evidence Use: `EU-WASTE-ASSESS-STREAMS@1`, `...-HAND-HYGIENE@1`, `...-HAZARDOUS-ESCALATION@1`, `...-SANITARY-HANDLE@1`.
- Sources: `SRC-WHO-WASTE-EMERGENCY-2026@1` and `SRC-EMERGENCY-WASTE-SANITATION-2026@1`.
- Context/Scope: `CTX-EMERGENCY-WASTE@1`, `SCP-EMERGENCY-WASTE@1`, both target `CLM-WASTE-SANITARY-HANDLE@1`.
- The dedicated test checks the 12-record profile, schema and semantic validity, but not source passage fit or Context/Scope coverage across Claims A–C.

Combined inspected inventory: **55 Part I records** (11 + 12 + 9 + 11 + 12). All five slices are included in the Part I progress denominator.

#### Reused audits and exact checkpoint verification

- **P4 / water-filter-assessment and emergency-water-storage-state**
  - `RELEASE/P4-WATER-SAFETY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`: water-filter assessment/inference boundaries and emergency storage State/Relation/Identity semantics were explicitly re-audited; P4 substantive, evidence, documentation and Human View findings 0.
  - `RELEASE/P4-WATER-SAFETY-UNIFIED-DEBT-MAP-2026-10-06.md`: P4-EVIDENCE-004 closed with independent EPA emergency-water-supply evidence; water-filter-assessment retains CDC + WHO evidence.
  - Exact P4 checkpoint commit `6100afea739e63044ca23e2817b7706a98466f3a` has exact-head Reference #1594, Release Gate #1887 and Offline #1063 all successful.
- **P3 / emergency-hand-hygiene and emergency-waste-sanitation**
  - `RELEASE/P3-SANITATION-HYGIENE-CORRECTION-AUDIT-2026-10-06.md` and `RELEASE/P3-SANITATION-HYGIENE-UNIFIED-DEBT-MAP-2026-10-06.md`: P3 source, evidence, README, test, Human View and duplicate-source findings were closed; the exact checkpoint artifact records 0 open findings.
  - Exact P3 checkpoint commit `8bd1a889e83406a43b9d511b54da233f51e86cc9` has exact-head Reference #1563, Release Gate #1856 and Offline #1032 all successful.
  - The current source-passage check below narrowly reopens the hazardous-waste Claim/EU fit. It does not repeat the full P3 audit or invalidate the hand-hygiene PASS.
- **R23 / emergency-water-storage-state Relation**
  - `RELEASE/WAVE-23-SUBSTANTIVE-AUDIT-2026-10-05.md` explicitly distinguishes 26 cross-slice Relations from 27 total Relations, with the one pre-existing domain Relation in emergency-water-storage-state. It states the State/Relation/Identity semantics and dedicated linkage regression passed.
  - Exact R23 checkpoint commit `3d33198b4e4d1391926b678a2fb75020aa619457` has exact-head Reference #1515, Release Gate #1808 and Offline #984 all successful.
- **Ancillary hydrology-basics**
  - No dedicated substantive audit was located in the inspected release artifacts. Its use in the M3 water-resources Relation is not a substitute for a hydrology content audit.

#### Direct source passage checks

- CDC, “How to Make Water Safe in an Emergency”:
  - lines 139–151: portable filters do not remove all pathogens; they do not remove viruses; absolute pore size thresholds are stated separately for bacteria (0.3 micron or smaller) and parasites (1 micron or smaller); CDC says to add chemical disinfection after filtration to address viruses/bacteria.
  - URL: https://www.cdc.gov/water-emergency/about/index.html
- WHO, “International Scheme to Evaluate Household Water Treatment Technologies”:
  - lines 206–209: Scheme evaluates microbial performance against WHO health-based criteria; HWT methods vary in ability to remove bacteria, viruses and protozoa; performance is classified at 1-, 2- and 3-star levels.
  - URL: https://www.who.int/tools/international-scheme-to-evaluate-household-water-treatment-technologies
- CDC, “How to Create an Emergency Water Supply”:
  - lines 52–66: FDA-approved food-grade containers; container must not transfer toxic substances; do not use containers previously used for toxic chemicals;
  - lines 68–94: wash, sanitize, dry, fill and close;
  - lines 95–110: label drinking water and storage date, replace every six months, keep cool/away from sunlight/toxic substances, avoid contaminating stored water when drawing it.
  - URL: https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html
- US EPA, “Planning for an Emergency Drinking Water Supply”:
  - lines 748–757: bulk water transport options, NSF/ANSI 61 for potable-water tanks, licensed/food-grade haulers and state-specific requirements.
  - URL: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100VJ2T.txt
- USGS, “Hydrology”:
  - defines hydrology as the study of water and its movement/distribution/properties on Earth, including surface water and groundwater.
  - URL: https://www.usgs.gov/special-topics/water-science-school/science/hydrology
- CDC, “Guidelines for Personal Hygiene During an Emergency”:
  - lines 27–41: emergency hygiene/handwashing importance; soap and water for at least 20 seconds; safe-water caveat and sanitizer limitations.
  - URL: https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html
- WHO, Technical Note 10, “Hygiene Promotion in Emergencies”:
  - lines 34–47: handwashing after defecation and before food preparation as key emergency hygiene practice;
  - lines 135–154: ten handwashing steps and explicit minimum 20-second wash.
  - URL: https://cdn.who.int/media/docs/default-source/wash-documents/who-tn-10-hygiene-promotion-in-emergencies.pdf
- CDC, “Guidelines for Cleaning Safely After a Disaster”:
  - lines 113–123: wash with soap and water after cleanup; wash exposed cuts; use safe water during boil-water advisories; links to emergency personal hygiene guidance.
  - URL: https://www.cdc.gov/natural-disasters/safety/index.html
- WHO, Technical Note 7, “Solid Waste Management in Emergencies”:
  - lines 16–32: definition and examples of general/emergency disaster waste;
  - lines 33–38: medical waste from hospitals and toxic industrial waste require urgent attention but are explicitly **not covered by this technical note**;
  - lines 78–108: assess waste streams/types/volumes/current disposal/responsibility/resources and identify hazardous waste needing special attention;
  - lines 114–141: disposal/removal of disaster rubble and safety measures;
  - lines 154–160: protect the workforce from physical injury with PPE.
  - URL: https://www.who.int/docs/default-source/wash-documents/wash-in-emergencies/technical-notes-on-wash-in-emergencies/who-tn-07-solid-waste-management-in-emergencies.pdf

#### Claim-level fit, boundaries and narrow reopening

1. **water-filter-assessment**
   - CDC directly supports Claim A's central limit and the exact bacteria/parasite pore-size distinctions. The claim is safe because it says filters are not universal and does not prescribe a specific model.
   - WHO directly supports Claim B's independent performance-evaluation role and the three pathogen classes.
   - The Assessment and Inference correctly keep the conclusion separate from the source statement and state limitations. The test protects this epistemic architecture.
   - EUs still have generic descriptions/no page-line locators. The exact lines are available and should be entered into the EUs. Claim B is English in a Russian-first edition and needs controlled translation.
   - Context/Scope target Claim A only; Claim B is a WHO Scheme description, not a universal product-performance claim.
2. **emergency-water-storage-state**
   - CDC directly supports the container material, cleaning/sanitizing, closure, labelling, replacement and contamination-prevention boundaries. EPA adds bulk transport and state-specific standards, not a universal rule for every household container.
   - The two State records share the same Object; Identity explicitly records continuity/uncertainty. P4 and R23 audits and the dedicated regression accept this domain relation. No Relation change is proposed.
   - EUs are generic and lack exact CDC/EPA locators. Keep U.S.-specific FDA/NSF/state standards visibly jurisdiction-bounded.
3. **hydrology-basics (ancillary)**
   - USGS directly supports the three introductory Claims, but EUs have no exact section locators.
   - The README URL was stale; it has been synchronized to the current USGS page in commit `77d75e4dedf7540187735673b44c593f2ecf4650`.
   - This slice is not in the 94-slice Part I inventory. Its only current first-edition relevance is as the other end of the M3 water-resources Relation.
4. **emergency-hand-hygiene**
   - Both CDC and WHO directly support the 20-second minimum in an emergency/hygiene context. The WHO PDF explicitly states “at least 20 seconds”; there is no conflict between the two sources.
   - Process/Action/Result topology is valid and regression-covered. The README topology is accurate.
   - EUs remain generic and should identify the exact CDC paragraph and WHO Technical Note 10 figure/text. Context/Scope target the only Claim and therefore cover the slice's single assertion.
5. **emergency-waste-sanitation**
   - Claim A is directly supported by WHO Technical Note 7's assessment section: waste streams, types/volumes, current disposal, responsibilities/resources and hazardous-waste screening.
   - Claim B is supported by CDC's instruction to wash with soap and water after cleanup; WHO TN10 also provides the emergency handwashing boundary, but the current EU for Claim B only uses CDC.
   - Claim C is **not fully supported by its current WHO EU**. TN7 says medical and toxic industrial wastes need urgent attention but are outside the technical note's scope. It does not provide specialist handling/transfer procedures. A general instruction to escalate such waste is prudent, but it needs a separate source on healthcare/chemical hazardous-waste management or must be narrowed to the source-supported “identify and refer to competent specialist authorities” boundary.
   - Claim D's current CDC EU supports handwashing after cleanup and personal safety during disaster cleanup, but not the full waste collection/disposal risk-reduction proposition. WHO TN7 directly discusses safe waste disposal and environmental/public-health hazards, but the current Claim D EU does not link to that WHO source. The dependency graph should be corrected rather than borrowing source support across Claims.
   - Context/Scope target Claim D only. The specialized-waste exclusion and local-authority boundary are materially relevant to Claim C as well; do not assume D's Scope applies to C.
   - P3's slice-level evidence-independence PASS is preserved, but the claim-level source mismatch and TN7 explicit exclusion are new, reproducible evidence-fit findings. Reopen only the affected Claim C and Claim D dependency closures.

#### Decisions

- **water-filter-assessment: HOLD — both Claims and dependency closures.** P4 substantive/evidence/Human View and exact 3/3 checkpoint are closed. Remaining first-edition blocker: exact CDC/WHO EU locators and Russian-first translation of Claim B.
- **emergency-water-storage-state: HOLD — Claim and dependency closure.** P4/R23 substantive, State/Relation/Identity and exact checkpoint gates are closed. Remaining blocker: exact CDC/EPA EU locators and visible U.S./state-specific boundary.
- **hydrology-basics: HOLD — all three Part I Claims and dependency closures.** No dedicated substantive audit was located; the USGS source is directly relevant to the M3 Relation, but the EUs have no exact section locators.
- **emergency-hand-hygiene: HOLD — Claim and dependency closure.** P3 substantive/Human View and exact 3/3 checkpoint are closed; direct CDC/WHO support is strong. Remaining blocker: exact EU locators, not content accuracy.
- **emergency-waste-sanitation: HOLD — all four Claims and dependency closures; narrowly reopen P3-EVIDENCE-002/Claim C and Claim D source fit.** P3 exact 3/3 checkpoint remains closed as a technical checkpoint. New blockers are WHO TN7's explicit exclusion of medical/toxic specialist waste, missing specialized evidence for Claim C, missing WHO disposal Evidence Use for Claim D, and Claim-C applicability not covered by the current Scope.

Documentation-only corrections in this block:
- water-filter-assessment README corrected: 11 records contain an Actor, not a standalone Assumption record; assumptions are inside the Assessment. Commit `bf551d445cd8705933e716ab436b3bd75a9cee4b`.
- hydrology README current USGS URL synchronized in commit `77d75e4dedf7540187735673b44c593f2ecf4650`.

No canonical JSON changed in this screen.


### 31. Shelter, fire, wildfire smoke, heat, cold, carbon-monoxide and weather foundations — seven-slice record-level block (2026-11-19)

This block screens seven **Part I** slices in the controlling 94-slice inventory: `shelter-basics`, `fire-safety-basics`, `wildfire-smoke-safety`, `extreme-heat-safety`, `cold-weather-hypothermia`, `carbon-monoxide-heating-safety` and `weather-basics`. The exact record files, current Claim versions, dependency edges, dedicated tests, source identities, Context/Scope targets and existing Relation records were inspected. The block does not repeat the already-screened `home-fire-smoke-safety`, `emergency-lighting-safety` or `generator-carbon-monoxide-safety` slices. The previous six-slice working screen is retained below as superseded Section 32; use this expanded Section 31 for current decisions.

#### 31.1 Exact inventory and topology

| Slice | Records | Claims | Sources | Evidence Use | Context | Scope | Relation |
|---|---:|---:|---:|---:|---:|---:|---:|
| shelter-basics | 12 | 3 | 2 | 4 | 1 | 1 | 1 |
| fire-safety-basics | 12 | 3 | 2 | 4 | 1 | 1 | 1 |
| wildfire-smoke-safety | 12 | 4 | 2 | 4 | 1 | 1 | 0 |
| extreme-heat-safety | 10 | 3 | 2 | 3 | 1 | 1 | 0 |
| cold-weather-hypothermia | 14 | 4 | 3 | 5 | 1 | 1 | 0 |
| carbon-monoxide-heating-safety | 13 | 4 | 3 | 4 | 1 | 1 | 0 |
| weather-basics | 9 | 3 | 1 | 3 | 1 | 1 | 0 |
| **Total** | **82** | **24** | **15** | **27** | **7** | **7** | **2** |

All inspected records use record_version 1 and type_version 1.0. Dedicated tests were inspected for all seven slices:
- fire-safety-basics: exact 12-record profile, six record types including Relation, unique IDs, schema validation, semantic validation, Claim provenance and Claim→EU→Source paths;
- shelter-basics: 12 records, two Sources, three Claims, four EUs, Relation and Claim provenance / evidence-path checks;
- wildfire-smoke-safety: exact 12-record profile, four Claims/four EUs/two Sources, schema and semantic validation, complete Claim provenance and dependency paths;
- extreme-heat-safety: 10 records, schema and semantic validation, direct EU coverage for all Claims, explicit scope-domain assertion;
- cold-weather-hypothermia: 14 records, exact types, schema/semantic validation, explicit adult population scope;
- carbon-monoxide-heating-safety: 13 records, schema and semantic validation;
- weather-basics: 9 records, one Source, three Claims, three EUs and Claim provenance/evidence-path checks.

These tests establish structural/semantic integrity within their implemented assertions. They do not prove the external source's exact passage supports every Claim, the jurisdiction is suitable for a global encyclopedia, or sibling Claims inherit Context/Scope.

The two existing Relation records were preserved:
- `REL_M3_FIRE_SAFETY_EMERGENCY_MANAGEMENT@1` links fire-safety Claim B to emergency-management Claim A.
- `REL_M3_SHELTER_SETTLEMENT@1` links shelter Claim A to human-settlement Claim B.
No duplicate Relation was added.

#### 31.2 Direct source verification and current locators

**Fire safety**
- U.S. Fire Administration, *Home Fires*: the current page is a topic-level collection covering fire learning, preparation, smoke alarms, prevention and recovery. The current canonical Source URI is a general prevention landing page, not a claim-level locator.
  - Source URI: https://www.usfa.fema.gov/prevention/
  - More precise USFA material checked: *Home Fire Escape Plans* (escape routes, two exits, meeting place and practice): https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/
  - More precise USFA material checked: *Smoke Alarms* (placement, testing, replacement and early warning): https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/
- National Fire Protection Association, *Home Fire Safety / Escape Planning*: the current Source points to the escape-planning topic. It is independently useful for Claim B's planning/evacuation component, but does not by itself establish every listed measure in Claim B or the broad site/building-decision variables in Claim C.
  - Source URI: https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning

**Shelter**
- Ready.gov, *Emergency Preparedness*: the Source record points to the Ready.gov homepage, which is too broad to pinpoint the three Claims.
  - Source URI: https://www.ready.gov/
- American Red Cross, *Disaster Shelters*: the current page directly describes shelter services, including a safe place to sleep, meals, water, health and emotional support, help reconnecting with family, accessibility, and local evacuation/shelter coordination. This is relevant to Claim A's disaster shelter function; it does not establish Claim B's ventilation/site-selection factors or Claim C's universal non-applicability proposition.
  - Source URI: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html
- A Ready.gov CERT training guide distinguishes shelter-in-place, extended stay and community/mass-care sheltering and discusses supplies for those scenarios. It is a more useful source candidate for the different shelter modes, but its 2019 date and U.S. preparedness context must be visible if selected.
  - Candidate locator: https://www.ready.gov/sites/default/files/2019.CERT_.Basic_.IG_.FINAL_.508c.pdf
- UNHCR, “Emergency Shelter Solutions and Standards” (21 Jan 2026), directly addresses climate, culture, local resources, hazard risk, privacy, thermal comfort, safety, weather protection and differentiated ventilation/space requirements. Candidate locator: https://emergency.unhcr.org/emergency-assistance/settlement-and-shelter/guidance-shelter/emergency-shelter-solutions-and-standards
- Sphere Handbook, “Location and settlement planning”, provides direct site-safety, access, hazard-minimization, ventilation and drainage standards. Candidate locator: https://disasterlaw.ifrc.org/sites/default/files/media/disaster_law/2021-01/Sphere-Handbook-2018-EN.pdf

**Wildfire smoke**
- CDC “Safety Guidelines: Wildfires and Wildfire Smoke” (24 Aug 2026), lines 29–43: monitor local weather and Air Quality Index, follow local emergency-management instructions, stay inside when directed, reduce smoke exposure and account for higher-risk groups. https://www.cdc.gov/wildfires/safety/how-to-safely-stay-safe-during-a-wildfire.html
- EPA “Create a Clean Room to Protect Indoor Air Quality During a Wildfire”, lines 46–48 onward: a clean room is kept closed to prevent smoke entry and may contain a portable air cleaner; further sections specify cleaner/DIY choices and limitations. https://www.epa.gov/emergencies-iaq/create-clean-room-protect-indoor-air-quality-during-wildfire

**Extreme heat**
- CDC, *About Heat and Your Health* (20 July 2026): supports staying cool, staying hydrated, recognising heat illness symptoms and accessing cooling locations; its symptom guidance supports Claim A and its prevention content supports Claim C. The page includes population-specific risk information and cautions such as fan use above 90°F, so generic advice must not erase those conditions.
  - Source URI: https://www.cdc.gov/heat-health/about/index.html
- National Weather Service, *Excessive Heat Awareness and Safety*: the page directly describes heat-exhaustion symptoms and first aid, and heat-stroke signs, emergency escalation, cooling, and the warning not to give fluids to a person with heat stroke.
  - Source URI: https://www.weather.gov/btv/heat
- The current NWS page is hosted by the Burlington, Vermont forecast office. It is a U.S. public-safety source and should be treated as a U.S. example rather than as a global emergency-number standard.

**Cold and hypothermia**
- CDC, *Preventing Hypothermia*: the current page states that hypothermia can occur above 40°F when a person becomes chilled by rain, sweat or cold-water immersion; lists adult warning signs; and says a body temperature below 95°F requires immediate medical attention.
  - Current directly checked locator: https://www.cdc.gov/winter-weather/prevention/index.html
  - Current Source record instead points to the CDC winter-storm safety page: https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html
- CDC, *Stay Alert for Hypothermia*: the Source record is used for the emergency Claim and states the medical-emergency/95°F threshold.
  - https://www.cdc.gov/natural-disasters/psa-toolkit/stay-alert-for-hypothermia.html
- National Weather Service, *During Extremely Cold Weather*: supports staying dry, changing wet clothing, covering exposed skin and seeking shelter from wind. It does not, by itself, establish every medical-emergency proposition in the Claim.
  - https://www.weather.gov/safety/cold-during

**Carbon monoxide and fuel-burning heating**
- CDC, *Carbon Monoxide (CO) Poisoning Basics* (current page dated 26 October 2026): describes CO as colourless/odourless, common household and heating sources, symptoms, detector placement, annual qualified servicing of fuel-burning heating appliances, and outdoor generator placement more than 20 feet from windows, doors and vents.
  - Source URI: https://www.cdc.gov/carbon-monoxide/about/index.html
- CPSC, *Carbon Monoxide Questions and Answers*: supports the emergency sequence when an alarm sounds: move outside to fresh air, call emergency services, account for everyone, and do not re-enter until responders permit it.
  - Source URI: https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Carbon-Monoxide-Questions-and-Answers
- CPSC, *Carbon Monoxide Fact Sheet*: supports CO alarm placement on every level and outside sleeping areas, and states that alarms do not replace proper use/upkeep of appliances.
  - Source URI: https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet

**Weather**
- NOAA, *Weather & Atmosphere*: the current Source URI points to a broad educational collection. NOAA's current *Weather Observations* page directly states that weather observations describe atmospheric conditions at a time/place and lists temperature, humidity, precipitation, air pressure, wind speed and direction. NOAA's weather tutorial distinguishes a forecast (prediction of future conditions) from observations (conditions that actually occurred at a particular time and location).
  - Source URI in record: https://www.noaa.gov/education/resource-collections/weather-atmosphere
  - Direct observations locator: https://www.noaa.gov/education/resource-collections/weather-atmosphere/weather-observations
  - Forecast/observation distinction locator: https://www.noaa.gov/education/resource-collections/data/tutorials/weather-gov

#### 31.3 Claim-level fit, applicability and record findings

1. **fire-safety-basics**
   - Claim A's broad statement about prevention, consequence limitation, safe response and evacuation is consistent with USFA's fire-prevention and home-fire preparation material, but the stored Source URI is a general landing page and its EU is wholly generic.
   - Claim B lists prevention, detection, suppression, compartmentation, evacuation planning and emergency response. USFA's home-fire materials directly support smoke alarms and escape planning; NFPA's escape-planning Source independently supports only part of the listed categories. The current graph attaches the NFPA EU to Claim B only, which is appropriately narrow. Neither Source/EU as currently recorded pinpoints suppression and compartmentation.
   - Claim C combines hazards, building/site characteristics, occupants, detection/suppression systems and applicable requirements. The current USFA landing-page EU does not identify passages establishing this full design-dependency list.
   - Context/Scope target Claim A only. Claims B/C must not silently inherit the same applicability statement.
   - README count/topology was corrected to 12 records, two Sources, four EUs and one Relation in commit `dc91267e325983acccabcf9a5da7d9985ca13df4`. The stale test function name was corrected to `twelve_record_shape` without changing assertions in commit `8d651687d206f3fa746560bf8be8d6486cea63dd`.
   - The M3 Relation to emergency management is preserved; no need to recreate the cross-slice audit.
2. **shelter-basics**
   - Claim A's basic disaster-shelter function is directly corroborated by Red Cross's description of safe sleeping accommodation, meals, water and support. Ready.gov's homepage is not a pinpoint.
   - Claim B's combined requirements (weather, water access, ventilation and site safety) are not established by the current generic Ready.gov EU or the Red Cross shelter-services page. These are distinct considerations and need source-specific passages, not a broad inference from “shelter”.
   - Claim C's assertion that suitability depends on the specific hazard/environment and there is no universal safe shelter for all scenarios is a sensible boundary, but its Ready.gov EU is generic and no exact passage is identified. Shelter-in-place and community shelter are different hazard responses; the CERT guide can help establish the distinction but needs controlled citation and scope.
   - Context/Scope target Claim A only. The hazard-specific qualification is important to Claims B/C as well, but cannot be inherited without explicit applicability links.
   - The M3 shelter ↔ settlement Relation is retained. The README topology was corrected to 12 records / 2 Sources / 3 Claims / 4 EUs / Context / Scope / Relation in commit `20a725812ec2b3ca21e2fc62b4ec4b373d5940f6`.
3. **wildfire-smoke-safety**
   - CDC directly supports local AQI monitoring, emergency-management instructions, exposure reduction and higher-risk groups; EPA directly supports a closable clean room and portable air cleaner.
   - Claim C's DIY box-fan filter is a temporary alternative only; it must not be presented as equivalent to a certified portable air cleaner or as an exhaustive/permanent solution. Pin the EPA limitations and sizing guidance.
   - Claim D contains health-escalation guidance. Context/Scope target Claim A only; Claim D needs an explicit medical/escalation boundary.
   - EUs are generic despite direct CDC/EPA passages; exact locators are required.
4. **extreme-heat-safety**
   - Claim A's listed symptoms and escalation language are supported by CDC's heat-health guidance. “Fainting” and worsening symptoms should be tied to the exact CDC section, and the Claim should not be read as an exhaustive symptom list.
   - Claim B's emergency character and rapid cooling are supported by the NWS heat-safety page. The source also says call emergency services immediately and do not give fluids in heat stroke; the Claim does not prescribe fluids, but its Evidence Use should point to the full emergency section and not omit the call-for-help requirement.
   - Claim C's cool/hydration prevention message is supported by CDC. It remains a general public-health recommendation, not an instruction to override individual medical fluid restrictions or heat-risk plans.
   - Context/Scope target Claim C only, although Context provenance mentions Claims C and A. Claim B's emergency guidance has no explicit Context/Scope target in this slice.
   - EUs are source-specific summaries but do not give exact section/heading locators. This is better than a generic placeholder, but not yet sufficient for a first-edition release record.
5. **cold-weather-hypothermia**
   - Claim A's emergency escalation and below-95°F threshold are supported by CDC and NWS; the conversion 95°F = 35°C is correct. It should be explicit that 95°F/35°C is the stated medical threshold, not a universal safe/unsafe outdoor ambient temperature.
   - Claim B's adult warning signs match CDC's list. The Claim correctly limits the population to adults; CDC separately gives different infant signs.
   - Claim C's wetness/cool-weather risk is supported by CDC's current page, which says hypothermia can occur above 40°F if rain, sweat or cold water chills the person. The current EU instead links NWS, whose page supports the cold/wet exposure framing but should be pinned more precisely.
   - Claim D's advice to limit outdoor time during winter storms is consistent with CDC winter-storm safety recommendations, but the EU's description does not pinpoint the relevant section. It should not become a universal maximum-time rule.
   - Context/Scope target only Claim B (adult signs). Emergency Claim A, wetness Claim C and outdoor-exposure Claim D do not inherit that adult-only scope. Claim A has an independent medical threshold; C/D require their own applicability boundaries.
6. **carbon-monoxide-heating-safety**
   - Claim A's alarm placement (near each sleeping area and on every level) is directly supported by CDC and CPSC. The exact CPSC page says every level and outside sleeping areas; “near each sleeping zone” should be reconciled with the source wording.
   - Claim B's alarm/symptom emergency response is directly supported by CPSC. The EU text is specific and preserves the no-re-entry-until-authorised boundary. It should make the source's “call emergency services/fire department” sequence explicit and must not imply that merely leaving and waiting is sufficient.
   - Claim C's servicing and detector limitation are supported by CDC/CPSC. CDC specifies annual servicing by a qualified technician for heating systems, water heaters and other gas/oil/coal-burning appliances; avoid broadening that frequency to every possible device without source support.
   - Claim D's indoor-use prohibition is supported by CDC for generators, charcoal, portable camp stoves and unvented appliances, and by CPSC for specified fuel-burning devices. The current claim's phrase “other fuel-burning devices” is broad; the EU should list the covered categories and not imply every fuel-burning appliance is prohibited indoors.
   - Context/Scope target Claim D only. Claims A–C have no explicit applicability records despite being equally important prevention/emergency guidance.
   - The dedicated test checks schema/semantic validity, but not per-Claim source fit or Context/Scope closure.
7. **weather-basics**
   - Claim A's time-and-place definition is directly supported by NOAA's Weather & Atmosphere overview.
   - Claim B's temperature, pressure, humidity, wind and precipitation list is directly supported by NOAA's Weather Observations page.
   - Claim C's distinction between forecast and past/current observation is directly supported by NOAA's weather.gov tutorial transcript.
   - All three current EUs refer only to the broad NOAA collection and do not identify the relevant Weather Observations or forecast/observation passage. The current Source URI is a collection, not the direct page supporting Claims B/C.
   - Context/Scope target Claim A only. The concepts in B/C are related but require their own explicit applicability mapping if the project standard requires one per Claim.

#### 31.4 Cross-slice boundaries and first-edition decisions

- **Fire safety vs home-fire-smoke-safety / emergency-lighting-safety:** this slice is the high-level fire-safety framework and must not duplicate detailed household smoke-alarm, candle or lighting claims already screened in the opening manifest. Its current Claims are broader than its source pinpoints.
- **Shelter vs housing/settlement:** shelter is an immediate, hazard-dependent protective function; housing systems and human settlements are longer-lived systems. Keep the M3 Relation but do not treat it as evidence for the shelter Claims.
- **Heat vs cold:** both are medical/high-consequence exposure topics. Their claims should retain explicit emergency escalation and population boundaries; neither should be reduced to weather-only background.
- **CO heating vs generator CO:** CO heating covers household fuel-burning appliances, alarm placement, servicing and alarm response; generator-carbon-monoxide-safety covers generator placement and operation. Keep their boundaries distinct and avoid duplicating generator-specific distance rules here.
- **Wildfire smoke vs weather/climate:** weather observations and AQI are decision inputs for smoke exposure, but wildfire smoke is a separate health hazard with indoor-air controls and medical escalation; do not collapse it into generic weather.
- **Weather vs climate:** weather describes atmospheric conditions at a particular time and place; climate is a longer-term pattern and must remain a separate slice.
- The seven slices together contain 82 records, but structural completeness and passing tests do not close evidence, source-rights, translation, jurisdiction or reader review.

**Decisions**
- **fire-safety-basics: HOLD — all three Claims and dependency closures.** Strong direct candidates exist for evacuation and smoke alarms; generic USFA EUs, unpinned suppression/compartmentation coverage, broad Claim C, and stale README count (9 vs 12) remain.
- **shelter-basics: HOLD — all three Claims and dependency closures.** Red Cross directly supports Claim A; Ready.gov homepage is not a pinpoint; Claims B/C and Context/Scope applicability remain under-evidenced.
- **wildfire-smoke-safety: HOLD — all four Claims and dependency closures.** P1 substantive/evidence/Human View and exact 3/3 checkpoint are reused; CDC/EPA directly support the core claims. Remaining blockers are exact EU locators, Claim-C DIY limitations and Claim-D medical Scope coverage.
- **extreme-heat-safety: HOLD — all three Claims and dependency closures.** CDC/NWS support the core content; exact passage locators and Context/Scope coverage of the emergency Claim B remain unresolved.
- **cold-weather-hypothermia: HOLD — all four Claims and dependency closures.** CDC directly supports adult signs, wetness risk and the 95°F emergency threshold; EU pinpoints and Claim A/C/D applicability remain incomplete.
- **carbon-monoxide-heating-safety: HOLD — all four Claims and dependency closures.** CDC/CPSC directly support the main safety boundaries; exact locators and Context/Scope coverage for Claims A–C remain incomplete, and Claim D's category wording needs tight source alignment.
- **weather-basics: HOLD — all three Claims and dependency closures.** NOAA directly supports the concepts, but all three EUs use the broad collection URI rather than the direct observation/forecast passages; Context/Scope targets Claim A only.

No canonical JSON changed. No INCLUDE assigned. Existing M3 Relations were preserved. No previously closed P1/P2/M3 substantive audit was repeated.


> Superseded by Section 31, which consolidates the overlapping shelter/fire/heat/cold/CO screens, includes the additional weather-basics slice, and retains the unique wildfire-smoke-safety findings. Use Section 31 for current decisions and progress counts; this block is retained as a working audit trail and must not be counted as a separate screen.

### 32. Superseded working screen — shelter, fire safety, wildfire smoke, extreme heat, cold and carbon monoxide (2026-11-19)

All six slices are in the controlling Part I inventory. M3 and P1 substantive/Human View/evidence work is reused where applicable; the current screen checks the exact record graph, source URLs, passage fit and Claim-specific Context/Scope targets.

Exact inventories inspected (all records `record_version: 1`, `type_version: 1.0`):

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope | Relation |
|---|---:|---:|---:|---:|---:|---:|---:|
| shelter-basics | 12 | 2 | 3 | 4 | 1 | 1 | 1 |
| fire-safety-basics | 12 | 2 | 3 | 4 | 1 | 1 | 1 |
| wildfire-smoke-safety | 12 | 2 | 4 | 4 | 1 | 1 | 0 |
| extreme-heat-safety | 10 | 2 | 3 | 3 | 1 | 1 | 0 |
| cold-weather-hypothermia | 14 | 3 | 4 | 5 | 1 | 1 | 0 |
| carbon-monoxide-heating-safety | 13 | 3 | 4 | 4 | 1 | 1 | 0 |
| **Total** | **73** | **14** | **21** | **24** | **6** | **6** | **2** |

Dedicated tests check record counts/types, schema and semantic validity, complete Claim→Evidence Use→Source paths, Relation topology and (where present) scope-domain fields. They do not establish passage-level source fit or automatic inheritance of Context/Scope across Claims.

#### Reused audits and exact checkpoint verification

- **M3 / shelter-basics and fire-safety-basics**
  - `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`, `RELEASE/M3-UNIFIED-DEBT-MAP-2026-10-08.md` and `RELEASE/M3-HUMAN-VIEW-AUDIT-2026-10-08.md`: prior substantive, evidence and Human View PASS reused.
  - `RELEASE/M3-CROSS-DOMAIN-RELATION-AUDIT-2026-10-08.md`: the two domain Relations are among the accepted cross-slice relation set; no new Relation is created in this screen.
  - Exact M3 closure commit `2434f3a06618543b4534ff4b12a45ad0b87e10f4` has exact-head Reference #2163, Release Gate #2450 and Offline #1632 all successful.
- **P1 / wildfire-smoke-safety, extreme-heat-safety, cold-weather-hypothermia and carbon-monoxide-heating-safety**
  - `RELEASE/P1-REMAINDER-SUBSTANTIVE-AUDIT-2026-10-06.md`, `RELEASE/P1-UNIFIED-DEBT-MAP-2026-10-06.md`, `RELEASE/P1-EVIDENCE-DIVERSITY-AUDIT-2026-10-06.md` and `RELEASE/P1-HUMAN-VIEW-AUDIT-2026-10-06.md`: prior substantive/evidence/Human View closure reused.
  - Exact P1 checkpoint commit `0169c9189cf2867a4387c46f8d71f1af64260adf` has exact-head Reference #1542, Release Gate #1835 and Offline #1011 all successful.
  - New findings below are record-level source-locator and Context/Scope-target issues; they do not reopen the full P1 content audit.
- No canonical JSON changed in this screen.

#### Direct source passage checks

- **Shelter — current canonical sources**
  - Ready.gov Source URI is the general homepage: https://www.ready.gov/
  - American Red Cross Source URI is a shelter locator: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html
  - Neither current URL provides a pinpoint passage for Claims B/C on weather exposure, water, ventilation, site safety or hazard-dependent suitability.
  - Direct authoritative replacement candidates found but not linked in the current records:
    - UNHCR, “Emergency Shelter Solutions and Standards” (21 Jan 2026): shelter choices depend on geographical context, climate, culture, local resources, materials, hazard risks, privacy, thermal comfort, safety and protection from weather; warm/cold climate ventilation and space criteria are differentiated. https://emergency.unhcr.org/emergency-assistance/settlement-and-shelter/guidance-shelter/emergency-shelter-solutions-and-standards
    - Sphere Handbook, “Location and settlement planning”: safe/secure location, access to essential services, site selection and hazard minimization; shelter standards include ventilation, drainage and climate-specific design. https://disasterlaw.ifrc.org/sites/default/files/media/disaster_law/2021-01/Sphere-Handbook-2018-EN.pdf
- **Fire safety — current canonical sources**
  - U.S. Fire Administration Source URI is a prevention hub: https://www.usfa.fema.gov/prevention/
  - NFPA Source URI is an escape-planning page: https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning
  - USFA’s specific Home Fires page provides more direct prevention/smoke-alarm/escape-plan material: https://www.usfa.fema.gov/prevention/home-fires/
  - These sources support prevention, detection and escape planning, but do not directly support the full Claim B list, particularly suppression and compartmentation. Claim C's building/site/occupant/system/code dependency also needs a direct fire-protection source and jurisdictional locator.
- **Wildfire smoke**
  - CDC “Safety Guidelines: Wildfires and Wildfire Smoke” (24 Aug 2026), lines 29–43: monitor local weather and Air Quality Index, follow local emergency-management instructions, stay inside when directed, reduce smoke exposure and account for higher-risk groups. https://www.cdc.gov/wildfires/safety/how-to-safely-stay-safe-during-a-wildfire.html
  - EPA “Create a Clean Room to Protect Indoor Air Quality During a Wildfire”, lines 46–48 onward: a clean room is kept closed to prevent smoke entry and may contain a portable air cleaner. Further sections specify air-cleaner/DIY choices and limitations. https://www.epa.gov/emergencies-iaq/create-clean-room-protect-indoor-air-quality-during-wildfire
- **Extreme heat**
  - CDC “About Heat and Your Health” (20 Jul 2026), lines 27–45: stay cool, stay hydrated, know symptoms, use shade/breaks and air conditioning/cooling centers; fan use is temperature-dependent. https://www.cdc.gov/heat-health/about/index.html
  - The current CDC Source identity also names “During Hot Weather, Watch for Heat Illness”, but its single stored URI is only the general About Heat page. The separate CDC PSA (26 Aug 2026) directly lists heavy sweating, nausea and fainting and advises moving to a cool place, water and cool wet cloths; worsening symptoms require medical help. https://www.cdc.gov/natural-disasters/psa-toolkit/during-hot-weather.html
  - NWS Burlington “Excessive Heat Awareness and Safety”, lines 266–275: heat exhaustion symptoms and first aid; heat stroke is a severe medical emergency, call 911, move to a cooler place and cool rapidly; do not give fluids in heat stroke. https://www.weather.gov/btv/heat
  - The NWS page is maintained by a regional office (BTV); its symptom guidance is useful, but its U.S./regional context should remain visible.
- **Cold weather / hypothermia**
  - CDC “Safety Guidelines: During & After a Winter Storm” (25 Aug 2026), lines 29–39: limit outdoor time, take precautions, and know hypothermia signs; lines 200–217 list adult signs and state below 95°F is an emergency requiring immediate medical attention. https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html
  - CDC “Stay Alert for Hypothermia” (26 Aug 2026), lines 24–27 and 43–47: below 95°F plus confusion/slurred speech requires immediate emergency care. https://www.cdc.gov/natural-disasters/psa-toolkit/stay-alert-for-hypothermia.html
  - NWS “During Extremely Cold Weather”, lines 65–69: dress in layers, cover exposed skin, seek wind shelter, change wet clothing immediately and watch for hypothermia/frostbite. https://www.weather.gov/safety/cold-during
- **Carbon monoxide**
  - CDC “Carbon Monoxide (CO) Poisoning Basics” (26 Oct 2026), lines 47–68 and 79–98: detectors near sleeping areas, annual professional servicing of fuel-burning appliances, never heat a home with a gas oven, never burn charcoal or use portable gas camp stoves indoors, and generators outdoors more than 20 feet from openings. https://www.cdc.gov/carbon-monoxide/about/index.html
  - CPSC “Carbon-Monoxide-Questions-and-Answers”, lines 41–50 and 68–77: alarms on every home level and outside sleeping areas; annual appliance service; move outside immediately, call emergency services/911, do not re-enter until responders give permission, and do not use fuel-burning appliances/camping equipment indoors. https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Carbon-Monoxide-Questions-and-Answers
  - CPSC “Carbon Monoxide Fact Sheet”, lines 48–59 and 75–84, independently repeats alarm placement, annual servicing, indoor-use prohibitions and re-entry instructions. https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet

#### Claim-level fit, boundaries and record issues

1. **shelter-basics**
   - Claims: A — shelter is a basic need under environmental exposure/emergency; B — selection/setup must consider weather, water, ventilation and site safety; C — suitability depends on hazard and context; no universal safe shelter.
   - The two current EUs to Ready.gov support all three Claims with generic descriptions, but the Source URI is only the Ready.gov homepage. The Red Cross shelter locator independently supports the existence/location of shelters, not the selection criteria in Claims B/C.
   - UNHCR and Sphere passages directly support the missing criteria, but are candidate sources only. They must be added through controlled Source/EU records with exact locators; do not silently borrow them.
   - Context/Scope target Claim A only. Claim B/C are materially context-dependent and cannot inherit A's boundary.
   - README topology was stale (claimed 1 Source/3 Evidence Use and omitted the Relation). It was corrected to 12 records / 2 Sources / 3 Claims / 4 EU / Context / Scope / Relation in commit `20a725812ec2b3ca21e2fc62b4ec4b373d5940f6`.
2. **fire-safety-basics**
   - Claims A–C cover prevention/limiting consequences, the full measure set (prevention, detection, suppression, compartmentation, evacuation and response), and dependencies on hazards/building/site/occupants/systems/requirements.
   - The USFA hub and NFPA escape-planning page do not directly support the full Claim B list, particularly suppression and compartmentation. The USFA Home Fires page is a better locator for prevention/smoke alarms/escape plans, but it still does not close all of B/C.
   - Context/Scope target Claim A only; B/C contain building-, system- and jurisdiction-dependent statements.
   - README incorrectly described a nine-record profile and omitted the second Source, fourth EU and Relation. It was corrected to the actual 12-record topology in commit `dc91267e325983acccabcf9a5da7d9985ca13df4`. The stale “nine_record_shape” test function name was corrected to “twelve_record_shape” without changing assertions in commit `8d651687d206f3fa746560bf8be8d6486cea63dd`.
3. **wildfire-smoke-safety**
   - CDC directly supports air-quality monitoring, local instructions, exposure reduction and higher-risk groups; EPA directly supports a closable clean room and portable air cleaner.
   - Claim C's “temporary DIY alternative, not permanent replacement” should be kept aligned to EPA's exact wording and limitations. Do not imply that a box-fan filter is equivalent to a certified portable air cleaner.
   - Claim D contains a health-escalation proposition. Context/Scope target Claim A only; the README's broad “not medical advice” line does not automatically replace a Claim-D Scope record.
   - EUs are generic, but direct current source passages exist.
4. **extreme-heat-safety**
   - CDC and NWS directly support the high-level claims and emergency escalation. The current CDC Source identity names two pages while storing only one URI; the symptom/first-aid PSA is a separate URL and should be represented by an exact Source/EU locator.
   - NWS Burlington page is regionally hosted; its heatstroke first-aid content is useful but should be explicitly bounded to U.S. public guidance or supported by a national CDC source.
   - Context/Scope target only Claim C. The heat-exhaustion and heatstroke Claims are medical-emergency guidance and need their own explicit applicability/safety boundary.
   - The CDC PSA supports a narrow set of heat-exhaustion signs (heavy sweating, nausea, fainting); broader symptom lists need the precise CDC/NWS source passage.
5. **cold-weather-hypothermia**
   - CDC directly supports adult warning signs and the below-95°F emergency threshold; NWS supports wet-clothing exposure and wind protection; CDC winter guidance supports limiting outdoor time.
   - Context/Scope target only `CLM-COLD-HYPOTHERMIA-SIGNS@1` (the dedicated test asserts this exact target). The below-95°F emergency Claim, wetness/exposure Claim and outdoor-time Claim do not automatically inherit it.
   - README correctly states no universal safe exposure duration or treatment, but the formal record-level Scope must cover the emergency threshold and outdoor exposure Claims too.
6. **carbon-monoxide-heating-safety**
   - CPSC directly supports every-level/outside-sleeping-area alarm placement, annual servicing, immediate exit/911 and no re-entry until responders permit. CDC supports annual maintenance and indoor-use prohibitions.
   - The current evidence graph is substantively strong and independently sourced. The formal Scope targets only Claim D, although Claims A–C contain detector installation, emergency response and maintenance guidance. The reader-facing scope must explicitly state U.S. CPSC/CDC public guidance and that local building codes/manufacturer instructions govern.
   - Claim D overlaps the generator-specific “no indoor use” Claim in generator-carbon-monoxide-safety. Preserve the distinction: this slice covers the broad prohibition across fuel-burning appliances/camping equipment; the generator slice adds the 20-foot separation/exhaust-opening condition. Do not duplicate the same sentence as two independent facts.
   - No new Relation is added; any cross-slice linkage should be justified by the generator-specific distance/ventilation distinction.

#### Decisions

- **shelter-basics: HOLD — all three Claims and dependency closures.** M3 substantive/Human View and exact 3/3 checkpoint are reused. Current Source URLs do not support the selection criteria in Claims B/C; UNHCR/Sphere are replacement candidates but not linked.
- **fire-safety-basics: HOLD — all three Claims and dependency closures.** M3 substantive/Human View and exact 3/3 checkpoint are reused. Current sources do not support the full measure set in Claim B or the system/jurisdiction dependencies in Claim C.
- **wildfire-smoke-safety: HOLD — all four Claims and dependency closures.** P1 substantive/evidence/Human View and exact 3/3 checkpoint are reused; CDC/EPA direct support is strong. Remaining blockers are exact EU locators and Claim-D medical Scope coverage.
- **extreme-heat-safety: HOLD — all three Claims and dependency closures.** P1 substantive/evidence/Human View and exact 3/3 checkpoint are reused. Remaining blockers are the CDC multi-page URI mismatch, exact symptom locators, regional NWS boundary and missing medical Scope for Claims A/B.
- **cold-weather-hypothermia: HOLD — all four Claims and dependency closures.** P1 substantive/evidence/Human View and exact 3/3 checkpoint are reused. Source support is direct; the Scope record currently targets only the signs Claim and must cover the emergency threshold/exposure Claims without implicit inheritance.
- **carbon-monoxide-heating-safety: HOLD — all four Claims and dependency closures.** P1 substantive/evidence/Human View and exact 3/3 checkpoint are reused; CDC/CPSC directly support the claims. Remaining blocker is Claim-specific U.S./local-code Scope coverage for Claims A–C and explicit differentiation from generator-carbon-monoxide-safety.

No canonical JSON changed in this screen.


### 33. Food science, nutrition science, public health, environmental health, anatomy, physiology, microbiology, epidemiology and sleep — nine-slice health/biology block (2026-11-19)

All nine slices are Part I candidates. Exact record directories, current Claims, Sources, Evidence Use links, Context/Scope targets, README files and dedicated regression tests were inspected. All records are version `@1`, type version `1.0`.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| food-science-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| nutrition-science-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| public-health-basics | 12 | 2 | 4 | 4 | 1 | 1 |
| environmental-health-basics | 12 | 2 | 4 | 4 | 1 | 1 |
| anatomy-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| physiology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| microbiology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| epidemiology-basics | 12 | 2 | 4 | 4 | 1 | 1 |
| sleep-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **92** | **13** | **30** | **31** | **9** | **9** |

The dedicated regression tests establish the record profile, schema/semantic validity and Claim→Evidence Use→Source links. They do not establish that a Claim is substantive rather than a placeholder, that the source passage supports its full scope, or that one Claim's Context/Scope automatically applies to another.

#### Reused audits and exact checkpoint verification

- **P6 / public-health-basics, environmental-health-basics and epidemiology-basics**
  - `RELEASE/P6-PUBLIC-HEALTH-SUBSTANTIVE-RE-AUDIT-2026-10-06.md` and `RELEASE/P6-PUBLIC-HEALTH-UNIFIED-DEBT-MAP-2026-10-06.md`: prior P6 content/evidence findings and dispositions reused.
  - `RELEASE/P9-LIFE-HEALTH-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`, `RELEASE/P9-UNIFIED-DEBT-MAP-2026-10-06.md` and P13 no-change review: environmental-health findings reused; no new P9/P13 substantive finding is asserted here.
  - Exact P6 checkpoint commit `737b4bcc9fba40db240a7f2abdac16f32657e7b8` has exact-head Reference #1655, Release Gate #1948 and Offline #1124 all successful.
  - Important limitation: the P6 checkpoint says technical integrity is not factual truth or publication approval. The current epidemiology Claims A–C below are placeholder-level, despite P6's historical PASS. Reopen only that content/dependency closure; do not repeat the full P6 audit.
- **M2 / anatomy-basics**
  - `RELEASE/M2-SUBSTANTIVE-RE-AUDIT-2026-10-08.md` and `RELEASE/M2-UNIFIED-DEBT-MAP-2026-10-08.md`: anatomy content, evidence and Human View findings reused.
  - Exact M2 checkpoint commit `bfd0578ca6f8dae9093a96de4f2bf6139589a40f` has exact-head Reference #2153, Release Gate #2440 and Offline #1622 all successful.
- No dedicated substantive audit was located for food-science-basics, nutrition-science-basics, physiology-basics, microbiology-basics or sleep-basics in the inspected release artifacts.

#### Direct source and record checks

- **food-science-basics**
  - Claims A–C are meta-level statements about what the slice intends to describe, not substantive food-science knowledge.
  - Its only Source is labelled “OpenStax — Food Science” but points to `https://openstax.org/books/biology-2e/pages/34-1-nutrition-and-energy-production`, which does not resolve as the claimed section.
  - The valid OpenStax section is **34.2 Nutrition and Energy Production**, a Biology 2e nutrition chapter, not a general food-science reference. It covers balanced diet, food components, essential nutrients, energy production and nutrient storage. https://openstax.org/books/biology-2e/pages/34-2-nutrition-and-energy-production
  - README now marks the slice HOLD and documents the placeholder Claims and source identity/URI mismatch. No canonical JSON was changed.
- **nutrition-science-basics**
  - Claims A–C are substantive at a high level: nutrition science relates food/nutrients to health and function; nutrients support energy, growth/repair and regulation; requirements vary by life stage and context.
  - The sole current Source is the NIH Office of Dietary Supplements homepage (`https://ods.od.nih.gov/`). This is too broad to support all three Claims without exact fact-sheet locators; ODS is also supplement-focused rather than a general nutrition-science source.
  - Candidate direct sources, not linked in canonical records:
    - WHO, “Healthy Diet” (26 Jan 2026): supports healthy dietary patterns, varied food groups and dietary needs across individual characteristics/life stages. https://www.who.int/news-room/fact-sheets/detail/healthy-diet
    - OpenStax Biology 2e, §34.2: supports food components, nutrient functions, energy production and cellular/tissue maintenance. https://openstax.org/books/biology-2e/pages/34-2-nutrition-and-energy-production
  - Context/Scope target Claim A only; Claim C's life-stage and health-context dependency requires an explicit scope boundary. README now records the source-fit HOLD.
- **public-health-basics**
  - Four Claims are substantive and use CDC Public Health 101 plus WHO public-health material; current topology and source independence are covered by the P6 audit/test.
  - Claim D remains in English in the Russian-first edition. All EUs need exact section/paragraph locators rather than generic descriptions.
  - Context/Scope target only one Claim; no inheritance to Claims B–D. README now records the translation and locator HOLD.
- **environmental-health-basics**
  - Claims A–C use WHO environmental-health framing; Claim D uses the US EPA human-exposure pathway material. The WHO topic page describes environmental determinants such as air, water, sanitation, chemicals and climate; EPA explains release/source → environmental media → exposure/contact → health outcome.
  - Claim D remains in English; EUs need exact WHO/EPA locators. Context/Scope target only one Claim and must not be treated as applying automatically to the others.
  - P9/P13 no-change disposition is reused, not represented as a new exact-head CI pass. README now makes the Claim-D translation and per-Claim scope boundary explicit.
- **anatomy-basics**
  - Three Claims cover the distinction between anatomy and physiology, levels of biological organization and tissue types.
  - NIGMS material supports cells/tissues/organs/systems; OpenStax Anatomy & Physiology 2e §4.1 supports tissue classification and characteristics. Two independent source tracks exist.
  - M2 content/evidence/Human View and exact 3/3 checkpoint are reused. EUs still need exact paragraph/section locators; Context/Scope target only Claim A, but the Claims are descriptive rather than individual diagnosis.
- **physiology-basics**
  - Three Claims cover the study of function, homeostasis and coordinated organ-system activity.
  - The single Source is OpenStax Anatomy & Physiology 2e §1.1, “Overview of Anatomy and Physiology”. It supports the general distinction and homeostasis; Claim C's detailed organ-system coordination may need a direct structural-organization section locator or a second Source.
  - EUs are generic, there is no independent second Source, and Context/Scope target only Claim A. No dedicated substantive audit was located.
- **microbiology-basics**
  - Three Claims cover the microscopic scale of microorganisms, their distribution/ecological roles and the fact that microbes can be beneficial, neutral or pathogenic.
  - The single Source URI is OpenStax Microbiology §1 Introduction and supports the basic concepts. However, the canonical Source identity text is generic (“Authoritative reference source for microbiology-basics”), not a proper bibliographic identity; the README now identifies the actual OpenStax source and flags the metadata correction.
  - EUs need exact section locators; no second independent Source or dedicated substantive audit was located.
- **epidemiology-basics**
  - Claims A–C currently describe what the slice is intended to cover (“this slice defines/describes/distinguishes…”). These are meta-level placeholders, not substantive epidemiology Claims.
  - Claim D contains a definition in English. The CDC Source is “Principles of Epidemiology”; the WHO Source is a participatory-surveillance publication, not a dedicated general epidemiology definition. A current CDC Introduction to Epidemiology page directly sets learning objectives around defining epidemiology, basic terms, time/place/person and outbreak investigation: https://www.cdc.gov/training-publichealth101/php/training/introduction-to-epidemiology.html
  - WHO Basic Epidemiology, 2nd edition is a stronger general reference candidate: https://iris.who.int/bitstream/handle/10665/43541/9241547073_eng.pdf
  - The P6 PASS and exact 3/3 checkpoint are historical and do not override the current placeholder text. README was corrected to HOLD; rebuild substantive Claims and translate Claim D before re-auditing.
- **sleep-basics**
  - Three Claims cover sleep stages, the sleep/wake cycle and health/cognitive effects.
  - NHLBI “How Sleep Works” directly supports all three: internal body clocks run on approximately 24-hour cycles and are regulated by light/dark and schedules; sleep cycles through stages; inadequate sleep affects cardiovascular/respiratory health, metabolism and attention/focus. https://www.nhlbi.nih.gov/health/sleep
  - The current source is direct and readable, but it is the only Source; EUs need exact locators. Context/Scope target only Claim A, while Claim C makes health-effect claims. No dedicated substantive audit was located.

#### Decisions

- **food-science-basics: HOLD — all three Claims and dependency closures.** Claims A–C are meta placeholders; the only Source URI is incorrect/misidentified and the correct OpenStax section is nutrition, not food science.
- **nutrition-science-basics: HOLD — all three Claims and dependency closures.** Claims are substantive, but the sole NIH ODS homepage does not support the full scope; exact locators, an independent general nutrition source and Claim-C scope are required.
- **public-health-basics: HOLD — all four Claims and dependency closures.** P6 substantive/evidence/Human View and exact 3/3 checkpoint are reused; Claim D translation, exact EU locators and per-Claim scope coverage remain.
- **environmental-health-basics: HOLD — all four Claims and dependency closures.** P6/P9/P13 substantive results are reused; Claim D translation, exact WHO/EPA locators and per-Claim scope coverage remain.
- **anatomy-basics: HOLD — all three Claims and dependency closures.** M2 substantive/evidence/Human View and exact 3/3 checkpoint are reused; exact EU locators remain.
- **physiology-basics: HOLD — all three Claims and dependency closures.** One broad OpenStax source, generic EUs, Claim-C locator and absence of a dedicated substantive audit remain.
- **microbiology-basics: HOLD — all three Claims and dependency closures.** OpenStax content is relevant, but the Source identity is generic, EUs lack locators and only one Source is linked.
- **epidemiology-basics: HOLD — all four Claims and dependency closures; narrowly reopen P6 content/evidence closure for Claims A–C.** Three Claims are placeholders; Claim D is English; the WHO Source is not a strong general definition source.
- **sleep-basics: HOLD — all three Claims and dependency closures.** NHLBI directly supports the claims; exact EU locators, a second independent Source and Claim-C Scope coverage remain.

Documentation-only updates in this block:
- food-science README marks placeholder content and corrects the OpenStax section identity/URL.
- nutrition-science README records the NIH ODS source-fit gap and unlinked WHO/OpenStax candidates.
- epidemiology README corrects the unsupported “matured P6” interpretation and records the placeholder Claims.
- microbiology README identifies the actual OpenStax source and generic Source-identity defect.
- public-health and environmental-health READMEs make Claim-D translation and per-Claim scope boundaries explicit.

No canonical JSON changed in this screen.

### 34. Construction, housing, architecture, civil engineering and human settlements — five-slice record-level screen (2026-11-19)

All five Part I slices were read directly from the exact PR #22 HEAD c4e95cd16aae89c5aca54357d16b285d13eb41aa. The full record directories, README files, current Claims, Sources, Evidence Use links, Context/Scope targets and five dedicated regression tests were inspected. All records are version @1, type version 1.0.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| construction-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| housing-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| architecture-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| civil-engineering-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| human-settlement-systems-basics | 11 | 3 | 3 | 3 | 1 | 1 |
| **Total** | **49** | **8** | **15** | **16** | **5** | **5** |

The five dedicated tests confirm only limited structural profiles and selected link relationships. They do not establish passage-level source fit, claim substance, file-stem/record-ID equality, or per-Claim Context/Scope coverage.

#### Direct record and source findings

1. **construction-basics — HOLD**
   - Claims A–C are substantive general statements about building-science interactions, materials/connections/loads/conditions, and the need for qualified calculations and review of critical structures.
   - The canonical Source URI https://www.nist.gov/building-science currently returns 404. NIST's current Buildings and Construction page is a plausible replacement candidate and describes building materials, structural engineering, building codes, damage/repair and safety research; it is not linked in the canonical record.
   - All three Evidence Use records have generic descriptions and no exact section/paragraph locators. Context and Scope target Claim A only; Claims B/C do not inherit them.
   - The safety boundary in Claim C is directionally appropriate but still needs a precise source or an explicitly editorial/non-empirical classification and per-Claim applicability boundary.

2. **housing-systems-basics — HOLD**
   - Claims A–C are substantive: adequate housing dimensions; relationship of housing to employment, education, healthcare and services; and dependence on institutional, economic, climate and planning context.
   - The only Source is the UN-Habitat housing topic landing page. The current linked EUs say only that the source is used within scope; none identifies a passage, section or data locator.
   - UN/OHCHR material directly describes seven dimensions of adequate housing, including habitability, affordability, accessibility, services and location. UN-Habitat's Housing Data page and the OHCHR adequate-housing guidance are stronger direct locator candidates, but remain unlinked.
   - Context/Scope target Claim A only. Claims B/C require their own exact applicability boundaries, especially where access to services or national/local housing policy is discussed.

3. **architecture-basics — HOLD**
   - Claim A is a substantive high-level definition. Claims B and C are generic evidence-method and professional-review caveats rather than substantive architecture knowledge; they should not be counted as equivalent subject-matter coverage.
   - The Britannica Source URL is plausible but its exact passage could not be independently inspected in this screen. The AIA corroboration Source points to a 2016 PDF that now redirects to the AIA homepage in the available retrieval path; the PDF is not presently a reliable direct locator.
   - All four EUs use generic descriptions without section/page/paragraph locators. The AIA EU is attached only to Claim C and does not independently corroborate Claim A's definition.
   - Context/Scope target Claim A only. Specialized licensing, building-code and engineering conclusions remain outside the safe scope.

4. **civil-engineering-basics — HOLD**
   - Claims A–C are meta-level statements about what the slice introduces, the need for context, and the need for specialized review. They do not state substantive civil-engineering knowledge.
   - The Source is labelled “OpenStax — Engineering mechanics” but points to the general OpenStax Science subject landing page, not a specific engineering-mechanics text or passage.
   - All EUs are generic and contain no locators. Context/Scope target Claim A only. This slice needs substantive Claims and a correctly identified, subject-specific source before it can be considered for publication.

5. **human-settlement-systems-basics — HOLD**
   - Claims A–C are substantive and describe settlements as physical/social/economic/ecological systems, interconnected services/infrastructure, and integrated planning.
   - The UN source directly supports Claim A's general definition. World Bank and OECD sources are relevant to Claims B/C, but their linked pages are broad landing pages; the EUs summarize material without exact locators. The OECD 2025 integrated-urban-policy publication is a stronger direct candidate for Claim C; the current World Bank urban-development page is a more specific candidate for Claim B.
   - The three Sources are institutionally distinct, but the source-to-Claim passage fit still needs precise verification.
   - **Identifier convention defect:** all 11 record filenames use hyphenated stems (for example, CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-A.json), while the internal record_id values and references use underscore forms (for example, CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_A). The dedicated test verifies internal references but does not assert filename stem equals record_id. Do not silently normalize IDs; resolve the repository convention and downstream consumers before any canonical edit.
   - Context/Scope target Claim A only; Claims B/C do not inherit those boundaries.

#### Reused work, tests and decisions

- No dedicated substantive audit was found for these five slices in the inspected release artifacts. No earlier adjudication is claimed as newly completed.
- Dedicated tests inspected:
  - REFERENCE/tests/test_content_construction_basics_vertical_slice.py
  - REFERENCE/tests/test_content_housing_systems_basics_vertical_slice.py
  - REFERENCE/tests/test_content_architecture_basics_vertical_slice.py
  - REFERENCE/tests/test_content_civil_engineering_basics_vertical_slice.py
  - REFERENCE/tests/test_content_human_settlement_systems_basics_vertical_slice.py
- Structural tests are not evidence of substantive validity or publication approval.

#### Decisions

- **construction-basics: HOLD — all three Claims and dependency closures.** NIST URL is broken; locators are generic; Context/Scope cover only Claim A.
- **housing-systems-basics: HOLD — all three Claims and dependency closures.** Broad UN-Habitat landing page; no exact locators; per-Claim scope coverage missing for B/C.
- **architecture-basics: HOLD — all three Claims and dependency closures.** AIA PDF retrieval redirects to the homepage; Britannica passage not confirmed; two Claims are generic meta-level caveats; EU locators and per-Claim boundaries are insufficient.
- **civil-engineering-basics: HOLD — all three Claims and dependency closures.** Claims are meta-level placeholders; Source is a general subject index misidentified as Engineering Mechanics; no exact locators.
- **human-settlement-systems-basics: HOLD — all three Claims and dependency closures.** Sources are relevant but EUs lack exact locators; Context/Scope cover only Claim A; filename/internal-ID convention mismatch requires explicit resolution.

No canonical JSON, Relations, Assessments, or other content records were changed. No new Relation was created. No public INCLUDE decision is made. The five slices remain HOLD pending substantive Claim quality, exact source passages, per-Claim Context/Scope, identifier convention resolution where applicable, and qualified review for structural-safety implications.


### 35. Agriculture, plant biology, forestry, fisheries, livestock, zoology, ecology, ecosystems and fermentation — ten-slice life-support block (2026-11-19)

All ten slices are in the controlling Part I inventory. Each contains nine records: one Source, three Claims, three Evidence Use, one Context and one Scope. The ten dedicated tests verify the 9-record profile, schema/semantic validity and Claim→EU→Source dependency paths. They do not validate that Claims are substantive, that Source identity fields are bibliographic, or that generic EUs locate the supporting passage.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| early-agriculture | 9 | 1 | 3 | 3 | 1 | 1 |
| plant-biology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| plant-physiology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| forestry-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| fisheries-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| livestock-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| zoology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| ecology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| ecosystems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| food-fermentation-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **90** | **10** | **30** | **30** | **10** | **10** |

No dedicated substantive audit was located for these ten slices in the inspected release artifacts. The Domain Expansion Audit and its semantic-rule count are structural/validator evidence, not a substantive Claim/source audit.

#### Direct source passage checks

- **early-agriculture**
  - Current Source is an FAO AGRIS bibliographic record for the ICARDA Harlan Symposium proceedings. Its abstract explicitly describes multiple research approaches to the origins of agriculture, domestication pathways and the Fertile Crescent crops wheat, barley and lentils; the abstract is the direct locator, while the proceedings link is the stronger full-text candidate.
  - URL: https://agris.fao.org/search/en/providers/122535/records/669faf4b4295623862505523
  - This is a historical source (1997 proceedings); keep the Claims historical and do not imply current agronomic recommendations.
- **plant-biology-basics**
  - OpenStax Biology 2e §30.5, “Transport of Water and Solutes in Plants”, directly explains water/mineral movement through xylem, sugar movement through phloem, water potential, transpiration and stomatal control.
  - URL: https://openstax.org/books/biology-2e/pages/30-5-transport-of-water-and-solutes-in-plants
  - Source identity is currently generic (“Authoritative reference source for plant-biology-basics”) and should be corrected to the actual OpenStax title/section.
- **plant-physiology-basics**
  - Current Source points to OpenStax Biology 2e Chapter 30 introduction, which is a broad chapter entry point. It is relevant to plant form and physiology, but Claims about photosynthesis/metabolism, transport and environmental response need exact subchapter locators (including §30.5 and the relevant photosynthesis/response sections).
  - URL: https://openstax.org/books/biology-2e/pages/30-introduction
  - Source identity is a descriptive statement about plant physiology, not a bibliographic title.
- **forestry-basics**
  - FAO Sustainable Forest Management overview directly describes ecological, economic and social/cultural forest functions, sustainable management objectives, local context and stakeholder/policy dependencies.
  - URL: https://www.fao.org/sustainable-forest-management/en/
  - Source is relevant; EUs still need exact paragraph locators.
- **fisheries-basics**
  - FAO fisheries chapter describes fisheries/aquaculture food and livelihood roles, resource/stock management and the need to consider biological, social and economic conditions.
  - URL: https://www.fao.org/4/y3427e/y3427e03.htm
  - The publication is old (2003); the current Claims are conceptual and do not use old stock statistics, but the age and regional/species-specific limits must remain visible. Claim C's local regulation/stock boundary is not inherited from the Scope attached to Claim A.
- **livestock-systems-basics**
  - FAO “Livestock Systems” directly frames livestock as systems with production, resources, people, products and environmental/social/economic dimensions; the page is current and relevant to the high-level Claims.
  - URL: https://www.fao.org/livestock-systems
  - One Source only; exact EU locators and a second independent source remain outstanding. The local/species/production-model boundary in Claim C is not covered by Claim A's Scope.
- **zoology-basics**
  - OpenStax Biology 2e Chapter 28 introduction supports animal diversity, evolutionary lineages and classification context.
  - URL: https://openstax.org/books/biology-2e/pages/28-introduction
  - Source identity is currently a descriptive definition of zoology, not the actual OpenStax title. The broad definition Claim needs a precise section locator or a more direct reference.
- **ecology-basics**
  - Claims A–C are meta-level statements about what the slice defines/describes/explains; they are not substantive ecology knowledge.
  - Current Source points to OpenStax Biology 2e Chapter 46 introduction (ecosystems), not a general ecology definition. A more direct OpenStax candidate is §44.1 “The Scope of Ecology”: https://openstax.org/books/biology-2e/pages/44-1-the-scope-of-ecology
  - Rebuild the Claims as actual ecology content before attempting source repair.
- **ecosystems-basics**
  - OpenStax Biology 2e §46.1 “Ecology of Ecosystems” directly supports ecosystem components, biotic/abiotic interaction, energy flow and nutrient cycling.
  - URL: https://openstax.org/books/biology-2e/pages/46-1-ecology-of-ecosystems
  - Source is directly relevant; exact EU locators and a second independent source are still needed.
- **food-fermentation-basics**
  - FAO “Basic Principles of Fermentation” describes fermentation as microbial transformation of food substrates and discusses the roles of microorganisms, raw materials and process conditions.
  - URL: https://www.fao.org/4/x0560e/x0560e07.htm
  - The three Claims are in English in a Russian-first edition and require controlled translation. The source is old (2004), but the current Claims are conceptual and do not prescribe food-safety procedures.

#### Record-level findings and boundaries

1. All ten slices use one Source and three generic Evidence Use descriptions; the test suite checks dependency edges, not source passage fit. Exact paragraph/section locators are required before any INCLUDE.
2. **early-agriculture**, **plant-biology-basics**, **forestry-basics**, **fisheries-basics**, **livestock-systems-basics**, **zoology-basics**, **plant-physiology-basics**, **ecosystems-basics** and **food-fermentation-basics** contain domain-oriented Claims, but one-source dependence and generic EUs remain. Their current Source identities also need correction where they describe a topic instead of naming the actual publication.
3. **ecology-basics** has three meta-placeholder Claims and a Source aimed at an ecosystems chapter. This is a content and source-identity mismatch, not merely a missing locator.
4. **fisheries-basics**, **forestry-basics** and **livestock-systems-basics** include local, species, stock, resource, regulatory or production-model dependencies in Claim C; Context/Scope target Claim A only. Do not infer automatic inheritance.
5. **food-fermentation-basics** requires Russian translation and a visible boundary between descriptive fermentation science and actionable food-safety/process instructions.
6. No cross-slice Relation is present in this ten-slice set. Do not add one merely because the topics are adjacent; only create Relations for a distinct, useful dependency.

#### Decisions

- **early-agriculture: HOLD — all three Claims and dependency closures.** The FAO AGRIS abstract directly supports the historical claims, but the EUs need exact abstract/proceedings locators, a second source is absent and the source is historical.
- **plant-biology-basics: HOLD — all three Claims and dependency closures.** OpenStax §30.5 is relevant; generic Source identity, generic EUs, exact locators and second-source independence remain.
- **plant-physiology-basics: HOLD — all three Claims and dependency closures.** The OpenStax Chapter 30 introduction is too broad as the only locator for the full set; exact subsection locators and source identity correction remain.
- **forestry-basics: HOLD — all three Claims and dependency closures.** FAO supports the broad content; exact EUs, independent evidence and Claim-C local-context Scope remain.
- **fisheries-basics: HOLD — all three Claims and dependency closures.** FAO supports the broad content, but the 2003 source age, generic EUs, one-source dependency and local/species/stock Scope remain.
- **livestock-systems-basics: HOLD — all three Claims and dependency closures.** FAO is directly relevant, but the current homepage-level locator, generic EUs, one-source dependency and Claim-C local context remain.
- **zoology-basics: HOLD — all three Claims and dependency closures.** OpenStax supports animal diversity/classification; source identity, exact locators and second-source independence remain.
- **ecology-basics: HOLD — all three Claims and dependency closures.** Claims A–C are meta placeholders; the current Source points to the ecosystems chapter rather than general ecology.
- **ecosystems-basics: HOLD — all three Claims and dependency closures.** OpenStax §46.1 is directly relevant; exact EUs and a second independent source remain.
- **food-fermentation-basics: HOLD — all three Claims and dependency closures.** FAO supports the descriptive science; Russian translation, exact EUs and a clear non-procedural food-safety boundary remain.

No canonical JSON changed in this screen.

### 36. Wildfire safety, renewable energy, materials, manufacturing and robotics — seven-slice record-level screen (2026-11-19)

All seven Part I slices were read from exact PR #22 HEAD d4ab6a1fa12d8d55cd9b7f52fd7a45268f503b87. Inspected all 63 JSON records, seven README files and seven dedicated regression tests. All records are version @1, type version 1.0.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| fire | 9 | 1 | 3 | 3 | 1 | 1 |
| renewable-energy-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| materials-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| materials-science-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| manufacturing-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| manufacturing-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| robotics-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **63** | **7** | **21** | **21** | **7** | **7** |

The seven tests confirm record counts/types and selected internal dependency edges. They do not establish source passage fit, exact Evidence Use locators, claim substance, per-Claim Context/Scope closure, or release suitability.

#### Direct record and source findings

1. **fire — HOLD (wildfire / evacuation safety, not general combustion science)**
   - Claims A–C cover official warnings and evacuation orders; multiple evacuation routes, shelter locations and needs of pets/people with disabilities; and residual heat hazards after a wildfire.
   - The Ready.gov wildfire landing page currently returns HTTP 403 to the retrieval path, so it was not independently inspected as a live page. The official Ready.gov hazard-information PDF (March 2024) provides direct, readable support: evacuation on official order and monitoring alerts; knowing multiple routes and shelter locations and planning for pets/livestock; and avoiding hot ash, charred trees, smoldering debris and live embers because heat pockets may remain.
   - PDF locator: https://www.ready.gov/sites/default/files/2024-03/ready-gov_full-suite_hazard-info-sheets.pdf
   - Current EUs are generic summaries and do not cite the relevant wildfire “Prepare / Be Safe / After” passages. Context/Scope target Claim A only. Claim C is directly supported by the PDF but its own applicability boundary is not represented.
   - Slice title “fire” is broader than its actual wildfire-only content; README correctly points to Ready.gov wildfires. Do not treat it as a general fire science or structural-fire safety source, and do not duplicate the already screened fire-safety-basics / wildfire-smoke-safety coverage.

2. **renewable-energy-basics — HOLD**
   - Claims A–C are meta-placeholders about what the slice describes, the need to consider source/context, and the need for specialist review. They do not contain renewable-energy subject knowledge.
   - The canonical DOE URL https://www.energy.gov/energysaver/renewable-energy currently returns HTTP 404. DOE's current official pages include a statutory definition and a distributed-energy technologies overview, but the statutory definition is legal/jurisdiction-specific and must not be generalized as a universal scientific definition.
   - Useful candidate locators: DOE Distributed Energy Technologies for Federal Projects; DOE Federal Renewable Energy Use Statutory Requirement; DOE consumer guide to renewable energy. The current EUs do not cite any of these.
   - Context/Scope target Claim A only. Rebuild substantive Claims before source-link repair.

3. **materials-basics — HOLD**
   - Claims A–C are substantive, domain-oriented statements: materials science relates materials, measurements, models, data and performance; materials have physical, chemical and mechanical properties; and behavior depends on composition, structure, processing and operating conditions.
   - NIST Materials Science and Engineering Division page is live and directly supports the broad measurement/model/data/standards and structure-property-processing framing. Its page identifies competence in structure-property-processing relationships and areas including metallurgy, polymers and functional materials.
   - Locator: https://www.nist.gov/mml/materials-science-and-engineering-division
   - Claim B's three-way physical/chemical/mechanical classification is not demonstrated by the inspected NIST overview as currently summarized; it needs a more direct reference. All EUs are generic and have no paragraph/section locators.
   - Claims are in English despite the Russian-first Part I edition. Context/Scope target Claim A only; Claims B/C have no explicit per-Claim applicability boundaries. One source only.

4. **materials-science-basics — HOLD**
   - Claims A–C are meta-placeholders: they describe the purpose of the slice, dependence on source/context, and need for specialist review. They do not teach materials science.
   - The NIST Materials Science and Engineering Division page is live and is a strong subject source. It explicitly identifies structure-property-processing relationships, measurements, models, data, standards, and advanced manufacturing. However, this source does not make the current placeholder Claims into substantive content.
   - Locator: https://www.nist.gov/mml/materials-science-and-engineering-division
   - All EUs are generic. Context/Scope target Claim A only. A second source is not the immediate debt; the Claims must first be replaced through authorized editorial work.

5. **manufacturing-basics — HOLD**
   - Claims A/B are substantially supported by the NIST CSRC “Manufacturing Operations” definition: facility operation, system processes, material inputs/outputs, maintenance, supply/distribution, health/safety, IT and other enterprise functions.
   - Direct locator: https://csrc.nist.gov/glossary/term/Manufacturing_Operations
   - Important source limitation: the CSRC glossary explicitly warns that definitions must be understood in the context of their cited source publications and says to cite the source publication, not the glossary page. It cites NISTIR 8183 and its revisions/volumes. The canonical Source should not treat the glossary as a standalone universal manufacturing standard.
   - Claim C (“enterprise is a system of interacting operational functions rather than a single production step”) is a reasonable synthesis of the listed functions, but it is not a verbatim definition. EU-C should be classified and explained as a synthesis/inference rather than simple direct support.
   - All EUs are generic, with no cited section or source publication locator. Context/Scope target Claim A only. Claims are in English in a Russian-first edition.

6. **manufacturing-systems-basics — HOLD**
   - Claims A–C are substantive: production systems combine processes/equipment/people/information; measurement and process control support reproducibility, quality and efficiency; digital technology/data connect operations, monitoring and analysis.
   - NIST's Smart Manufacturing Systems Design and Analysis Program page directly supports system design, measurement science, standards, information technology, sensor networks, computerized controls, production-management software, real-time control and data analytics.
   - Direct locator: https://www.nist.gov/programs-projects/smart-manufacturing-systems-design-and-analysis-program
   - NIST's general Manufacturing landing page is broad. The dedicated NIST program page is a much stronger pinpoint candidate, but it is not the current canonical Source. The EUs merely say the source is used within available material and lack exact passage locators.
   - Context/Scope target Claim A only; Claims B/C need explicit boundaries. One Source only; claims in Russian, unlike the neighboring English manufacturing-basics slice.

#### Test and dependency observations

- Dedicated tests inspected:
  - REFERENCE/tests/test_content_fire_vertical_slice.py
  - REFERENCE/tests/test_content_renewable_energy_basics_vertical_slice.py
  - REFERENCE/tests/test_content_materials_basics_vertical_slice.py
  - REFERENCE/tests/test_content_materials_science_basics_vertical_slice.py
  - REFERENCE/tests/test_content_manufacturing_basics_vertical_slice.py
  - REFERENCE/tests/test_content_manufacturing_systems_basics_vertical_slice.py
  - REFERENCE/tests/test_content_robotics_basics_vertical_slice.py
- All six tests are structural. The fire and manufacturing-basics tests verify Claim→Source provenance and an Evidence Use edge per Claim; the other tests also verify the expected 9-record type profile and selected links. None asserts precise source locators, language consistency, or Context/Scope coverage for all Claims.
- No new cross-slice Relation is created. Topic adjacency between materials, manufacturing and energy is not by itself a distinct dependency. The fire slice is wildfire-focused and should not be merged with indoor/structural fire safety.

#### Decisions

- **fire: HOLD — all three Claims and dependency closures.** The official Ready.gov PDF supports the wildfire evacuation and post-fire hazard statements, but current EUs lack exact PDF locators; the landing page is not retrievable in this review; Context/Scope cover Claim A only; title is broader than content.
- **renewable-energy-basics: HOLD — all three Claims and dependency closures.** All Claims are meta-placeholders; canonical DOE URL returns 404; current EUs generic; replace with substantive Claims and direct, non-jurisdictionally misleading sources.
- **materials-basics: HOLD — all three Claims and dependency closures.** NIST supports broad materials-science framing, but Claim B needs a more direct locator; all EUs generic; English-language Claims; Context/Scope cover Claim A only.
- **materials-science-basics: HOLD — all three Claims and dependency closures.** All Claims are meta-placeholders despite a relevant NIST Source; EUs generic; Context/Scope cover Claim A only.
- **manufacturing-basics: HOLD — all three Claims and dependency closures.** NIST CSRC supports the broad operations content, but glossary terms require citation to their source publications; Claim C is synthesis rather than direct fact; EUs generic; English-language Claims; Context/Scope cover Claim A only.
- **manufacturing-systems-basics: HOLD — all three Claims and dependency closures.** NIST program page is directly relevant but not linked; EUs generic; one-source dependency; Context/Scope cover Claim A only.

No canonical JSON, Relations, Assessments or other content records were changed. No new Relation was created. No public INCLUDE decision is made. All six slices remain HOLD pending exact source publication/section locators, per-Claim applicability boundaries, language/editing consistency, and the substantive Claim repairs identified above.

### 37. Earthquake protection and aftershocks, floods and cleanup, climate, geology, seismology, volcanology and ocean systems — nine-slice hazard/geoscience screen (2026-11-19)

All nine Part I slices were read from exact PR #22 HEAD 64d4b9047b88502f8f29895c10793b59363bbe5a. Inspected all 88 JSON records, nine README files and nine dedicated regression tests. All records are version @1, type version 1.0.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| earthquake-protective-action | 12 | 2 | 1 | 2 | 1 | 1 |
| earthquake-aftershock-safety | 10 | 2 | 2 | 4 | 1 | 1 |
| flood | 9 | 1 | 3 | 3 | 1 | 1 |
| flood-cleanup-safety | 12 | 2 | 4 | 4 | 1 | 1 |
| climate-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| geology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| seismology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| volcanology-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| ocean-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **88** | **12** | **25** | **28** | **9** | **9** |

The 9 dedicated tests confirm expected counts/types or schema/semantic validity and selected links. Only the earthquake-protective-action test additionally checks Event → Decision → Action → Result references and publication-package citation preservation. None establishes passage-level source fit or full per-Claim Context/Scope coverage.

#### Direct record and source findings

1. **earthquake-protective-action — HOLD (high consequence)**
   - One documented-recommendation Claim: Drop to hands and knees, cover head/neck and hold on to sturdy furniture until shaking stops. FEMA/Ready.gov and American Red Cross provide independent corroboration.
   - FEMA P-2143/August 2024, current linked PDF: https://www.ready.gov/sites/default/files/2025-02/fema_full-suite-hazard-info-sheets.pdf. Exact earthquake section covers Drop/Cover/Hold On and situational exceptions (vehicle, bed, outdoors, doorway); Red Cross gives the same action and mobility-specific adaptations.
   - README says “Всего: 9 Record”, but the actual directory and dedicated regression both establish **12 records**. The README's listed profile omits the additional Red Cross Source/Evidence Use and the Actor record. This is a concrete documentation/test discrepancy; do not change the test or records to match the stale README.
   - EUs identify the action but do not provide PDF page/section or Red Cross subsection locators. Context/Scope appropriately describe the shaking phase, but only one Claim exists; preserve the limited scope and do not generalize to post-shaking evacuation or building inspection.
   - The PDF filename contains 2025 while the embedded FEMA publication is P-2143/August 2024. Keep the source's actual publication date visible; do not treat the URL folder as its publication date.

2. **earthquake-aftershock-safety — HOLD (high consequence)**
   - Claim EXPECT says to account for aftershocks after an earthquake. The USGS forecast source and Red Cross Earthquake Safety page support the existence/expectation of aftershocks; the Red Cross page also says to use Drop, Cover and Hold On whenever shaking occurs.
   - Claim DAMAGE says damaged buildings may present additional danger during subsequent shaking and building safety assessment requires a competent professional. Red Cross supports leaving a home that is no longer safe and professional inspection; USGS Open-File Report 2026-1029 directly studies strong-shaking risk during entry into earthquake-damaged buildings.
   - Direct USGS research candidate: https://pubs.usgs.gov/publication/ofr20261029 (first posted September 3, 2026). It is materially stronger than a generic aftershock forecast landing page for Claim DAMAGE.
   - The two Claims have two independent Sources each, but Evidence Use descriptions are mostly generic and lack exact section/report locators. Context/Scope target EXPECT only; DAMAGE has no explicit Context/Scope target.
   - **Duplicate Source identity across slices:** the American Red Cross Earthquake Safety URL is stored under both SRC-RED-CROSS-EARTHQUAKE and SRC-RED-CROSS-AFTERSHOCK-2026. Preserve both current records; resolve canonical Source reuse/deduplication policy before any authorized edit.

3. **flood — HOLD (high consequence)**
   - Claims A–C cover official warnings and safe locations; avoiding walking/swimming/driving through fast-moving floodwater; and slow/rapid onset plus disruption to transport, buildings and utilities.
   - The official FEMA P-2143 flood sheet directly supports flood definition, slow/fast onset, local alerts/official instructions, evacuation, higher ground, and not walking/swimming/driving through floodwater. It also documents infrastructure/transport disruption. The current FEMA PDF is https://www.ready.gov/sites/default/files/2025-02/fema_full-suite-hazard-info-sheets.pdf.
   - CDC's current flood preparedness page provides stronger direct locator candidates for evacuation routes and shelter locations: https://www.cdc.gov/floods/safety/. The current Claim A's “predefined safe places” is broader than the linked FEMA/Ready.gov Source as recorded.
   - All three EUs use the same generic Ready.gov/FEMA summary. Context/Scope target Claim A only; B/C have no explicit applicability boundaries. One Source only.

4. **flood-cleanup-safety — HOLD (high consequence; important Claim correction)**
   - Four Claims cover cleaning/disinfecting after floodwater, protective equipment, escalation for suspected electrical/gas/structural hazards, and safe re-entry after professional confirmation.
   - Current CDC disaster-cleanup guidance (Aug. 26, 2026) directly covers PPE, floodwater contamination, cleaning/drying and bleach safety: https://www.cdc.gov/natural-disasters/safety/. It says floodwater can contain dangerous bacteria and that skin contact alone does not pose a serious health risk; open cuts/sores need careful washing and infection precautions.
   - **Substantive overstatement in CLM-FLOOD-CLEAN-PROTECT:** the Claim says to avoid contact of contaminated water with skin and eyes without qualification. CDC explicitly distinguishes skin contact alone from ingestion and open-wound exposure. PPE is warranted, but the Claim as written may mislead readers about the risk pathway. This requires authorized editorial correction and precise source language, not a silent rewrite.
   - EPA's current Flooded Home text version directly says wait until professionals confirm re-entry is safe, ensure electricity is off, look for structural/other hazards, and wear N95 respirator, goggles, gloves and protective clothing: https://www.epa.gov/emergencies-iaq/text-version-flooded-home.
   - **Unsupported gas-specific clause:** CLM-FLOOD-REENTRY-HAZARD-ESCALATION includes suspected gas leaks as a reason not to enter. The inspected EPA locator supports electrical and structural hazards, but does not directly establish the gas-leak clause. A precise gas-safety source is required.
   - The current CDC Source URI recorded in JSON could not be verified through the retrieval path; the matching CDC publication title also exists as a 2008 archive record, while CDC now provides a current 2026 cleanup page and a current bleach guidance page. Do not silently substitute a new Source version.
   - Context/Scope target only CLM-FLOOD-CLEAN-DISINFECT; Claims B, C and REENTRY-SAFE have no explicit target boundaries. All four EUs are concise summaries without pinpoint locators.

5. **climate-basics — HOLD**
   - Claims A–C are substantive: climate concerns long-term characteristics/change; climate conclusions rely on observations, measurements and models over long timescales; and a single weather event does not characterize the climate.
   - NASA's “What's the difference between weather and climate?” directly distinguishes short timescales (minutes to days/weeks) from long-term averages over decades. NASA's “What Is Climate Change?” also describes observations from ground/air/space and computer models. Direct candidates: https://science.nasa.gov/climate-change/faq/whats-the-difference-between-weather-and-climate/ and https://science.nasa.gov/climate-change/what-is-climate-change/.
   - The current EUs are generic and do not point to the FAQ definition, observations/model passage or explicit weather-vs-climate contrast. Context/Scope target Claim A only. One Source only; per-Claim applicability boundaries for B/C are absent.

6. **geology-basics — HOLD**
   - All three Claims are meta-placeholders about the purpose of the slice, source/context limitations and the need for specialist review. No substantive geology knowledge is represented.
   - The Source identity is generic (“USGS — Geology”) and the URI points to a USGS water-resources science/geology path, not a well-defined general geology reference. Stronger direct candidates include USGS Geology Education, the USGS rock/mineral definition, and National Park Service Geoscience Concepts.
   - Candidate locators: https://www.usgs.gov/educational-resources/geology-education; https://www.usgs.gov/faqs/what-difference-between-a-rock-and-a-mineral; https://www.nps.gov/subjects/geology/geology-concepts.htm.
   - All EUs are generic. Context/Scope target Claim A only. Rebuild Claims before trying to repair locators.

7. **seismology-basics — HOLD**
   - Claims A/B are substantive: seismology studies earthquakes and seismic-wave propagation; seismographs record ground motion associated with seismic events. Claim C is a broad but underspecified statement that earthquake strength and consequences depend on multiple event and site characteristics.
   - The current Source identity is a sentence describing seismology, not the actual source title; the URI is the broad USGS Earthquake Hazards Program landing page.
   - Direct USGS source for Claim B: “Seismographs — Keeping Track of Earthquakes” explains seismic waves, seismometers and permanent recordings. https://www.usgs.gov/programs/earthquake-hazards/seismographs-keeping-track-earthquakes
   - Claim C needs a specific source and precision: distinguish magnitude, shaking intensity, ground motion and local site effects rather than collapsing them into “strength and consequences”. All three EUs are generic; Context/Scope target Claim A only; one Source only.

8. **volcanology-basics — HOLD**
   - Claims A–C are substantive: volcanology studies volcanism/magma movement; eruptions vary with characteristics, composition and magma-system conditions; volcano monitoring uses geophysical, geochemical and visual data.
   - USGS Volcano Hazards Program is a valid and relevant institutional source, but Source identity is incorrectly a descriptive sentence rather than the actual title “USGS — Volcano Hazards Program”. The page supports the general topic and hazard-monitoring mission; it is not a pinpoint locator for all three Claims.
   - Direct candidate for Claim C: USGS “What We Do — Volcano Hazards Program” and “Comprehensive monitoring provides timely warnings of volcano reawakening”; monitoring combines seismic, geodetic, hydrological and geochemical techniques, gas chemistry, ground movement and satellite/remote-sensing observations.
   - Candidate locators: https://www.usgs.gov/programs/VHP; https://www.usgs.gov/programs/VHP/what-we-do-volcano-hazards-program; https://www.usgs.gov/programs/VHP/comprehensive-monitoring-provides-timely-warnings-volcano-reawakening.
   - EUs are generic and lack claim-specific locator text. Context/Scope target Claim A only. One Source only; Claim B needs a more direct source passage.

9. **ocean-basics — HOLD**
   - Claims A–C are substantive: ocean interaction with atmosphere/land/living systems; temperature, salinity, water movement and depth as marine characteristics; and ocean processes transporting heat, matter and energy across spatial and temporal scales.
   - NOAA's linked Ocean & Coasts collection is live and provides a useful starting point, but is a broad collection rather than a pinpoint source. Its Ocean Currents page says currents occur at surface and depth, move locally and globally, and affect climate/ecosystems; the Gulf Stream transports heat northward. NOAA's current explanation identifies wind, density differences, tides and temperature/salinity-driven circulation.
   - Direct candidates: https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-currents; https://oceanservice.noaa.gov/facts/current.html; https://oceanservice.noaa.gov/facts/coldocean.html.
   - The current EUs all point to the broad collection and contain no exact section locators. Claim A's interaction with atmosphere/land/life is not fully established by the short current EU. Context/Scope target Claim A only; Claims B/C have no explicit applicability boundaries.

#### Reused work, cross-slice dependencies and test observations

- No exact-record substantive screen for these nine slices was located in the controlling Part I register before this section. Existing emergency and hazard work is not treated as a substitute for these exact records.
- Dedicated tests inspected:
  - REFERENCE/tests/test_content_earthquake_protective_action_vertical_slice.py
  - REFERENCE/tests/test_content_earthquake_aftershock_safety_vertical_slice.py
  - REFERENCE/tests/test_content_flood_vertical_slice.py
  - REFERENCE/tests/test_content_flood_cleanup_safety_vertical_slice.py
  - REFERENCE/tests/test_content_climate_basics_vertical_slice.py
  - REFERENCE/tests/test_content_geology_basics_vertical_slice.py
  - REFERENCE/tests/test_content_seismology_basics_vertical_slice.py
  - REFERENCE/tests/test_content_volcanology_basics_vertical_slice.py
  - REFERENCE/tests/test_content_ocean_basics_vertical_slice.py
- The earthquake-protective-action test checks 12 records, schema/semantic validity, Event/Decision/Action/Result linkage, non-attributed causality, and package citation preservation. Its README's 9-record statement is stale.
- The earthquake-aftershock and flood-cleanup tests check 10/12 records, schema and semantic validity. The other tests check record profiles and some Claim→Evidence Use→Source paths. These tests do not establish publication-grade source support or full Context/Scope closure.
- No new Relation was created. Existing domain adjacency (earthquake ↔ seismology, flood ↔ climate, ocean ↔ climate) is not by itself enough to create a Relation. Preserve any existing Relations and only add a distinct, useful dependency after exact endpoint/version verification.

#### Decisions

- **earthquake-protective-action: HOLD — exact 12-record closure.** FEMA and Red Cross independently support the single protective-action Claim; EU pinpoint locators are missing; README says 9 while directory/test say 12.
- **earthquake-aftershock-safety: HOLD — both Claims and dependency closures.** Red Cross and USGS are relevant; the 2026 USGS report is a stronger Claim-DAMAGE locator; EU locators are weak; Context/Scope target EXPECT only; duplicate Red Cross Source identity across two slices needs policy review.
- **flood: HOLD — all three Claims and dependency closures.** FEMA supports flood behavior and avoiding floodwater; Claim A's “predefined safe places” needs a direct locator; generic EUs; Context/Scope target A only.
- **flood-cleanup-safety: HOLD — all four Claims and dependency closures.** CDC supports cleanup and PPE, but CLM-FLOOD-CLEAN-PROTECT overstates skin-contact risk; EPA supports electrical/structural re-entry precautions but not the gas-leak clause; current CDC Source locator is not verified; Context/Scope target only one of four Claims.
- **climate-basics: HOLD — all three Claims and dependency closures.** NASA directly supports long/short time-scale distinction and observation/model methods; EUs generic; one source; Context/Scope target A only.
- **geology-basics: HOLD — all three Claims and dependency closures.** Claims are meta-placeholders; Source identity/locator weak; EUs generic.
- **seismology-basics: HOLD — all three Claims and dependency closures.** A/B are substantive but need direct USGS locators; Claim C requires magnitude/intensity/site-effect precision; Source identity is not bibliographic; EUs generic.
- **volcanology-basics: HOLD — all three Claims and dependency closures.** Claims are substantive and USGS is relevant; source identity is a description, not title; EUs generic; Claim B locator insufficient.
- **ocean-basics: HOLD — all three Claims and dependency closures.** NOAA material supports ocean currents and heat transport, but EUs point only to a broad collection; Claim A's Earth-system scope and per-Claim Context/Scope remain incomplete.

No canonical JSON, Relations, Assessments or other content records were changed. No public INCLUDE decision is made. All nine slices remain HOLD. High-consequence flood and earthquake Claims require qualified safety review; scientific/educational geoscience Claims require exact source passages, correct terminology and per-Claim applicability boundaries.


> Superseded by Section 36, which consolidates the more detailed six-slice review and adds the robotics slice. Use Section 36 for current decisions and progress counts; this block is retained as a working audit trail and must not be counted separately.

### 38. Superseded working screen — fire, renewable energy, materials, manufacturing and robotics (2026-11-19)

All seven slices are in the controlling Part I inventory. Each has nine records: one Source, three Claims, three Evidence Use, one Context and one Scope. Dedicated tests validate the 9-record profile and dependency graph; they do not validate substantive Claims or exact source locators.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| fire | 9 | 1 | 3 | 3 | 1 | 1 |
| renewable-energy-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| materials-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| materials-science-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| manufacturing-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| manufacturing-systems-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| robotics-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **63** | **7** | **21** | **21** | **7** | **7** |

#### Reused audit and checkpoint

- `manufacturing-systems-basics` is the only slice in this block with a dedicated substantive audit located:
  - `RELEASE/WAVE-22-SUBSTANTIVE-AUDIT-2026-10-05.md` and `RELEASE/R22-CLEAN-CHECKPOINT-2026-10-05.md` declare R22 CLEAN with zero outstanding acceptance debt.
  - Corrected content commit `a1a187648014e1bd6af39edfbb76d96b6a99b310` has exact-head Release Gate #37289735579, Reference #37289735585 and Offline Edition #37289735864 all successful.
  - All nine current canonical JSON files in `manufacturing-systems-basics/records/` have byte-identical Git blob SHAs to the R22 corrected content commit. The R22 substantive and CI evidence is therefore reusable for the current record graph.
- The M3 fire-safety audit applies to `fire-safety-basics`, not to the separate `fire` wildfire-emergency slice in this block.
- No dedicated substantive audit was located for the other six slices. The Domain Expansion Audit is structural/validator evidence, not a substitute for source-fit review.

#### Direct source passage checks

- **fire**
  - Current Source is Ready.gov Wildfires: https://www.ready.gov/wildfires
  - The page returned 403 to direct inspection in this pass, so its current passage fit could not be independently confirmed.
  - Better direct USFA candidates found:
    - Wildfire Evacuation Checklist: https://www.usfa.fema.gov/downloads/pdf/publications/wildfire-evacuation-checklist.pdf
    - Wildfire Evacuation Outreach Materials: https://www.usfa.fema.gov/wui/outreach/wildfire-evacuation.html
    - National Wildfire Evacuation Guidance (2026): https://www.usfa.fema.gov/downloads/pdf/publications/national-wildfire-evacuation-guidance-1st-edition.pdf
  - These sources address warnings/evacuation, route planning, pets and people with access/support needs, and post-fire hot ash/embers. They are candidates only until controlled Source/EU records are created.
- **renewable-energy-basics**
  - Claims A–C are meta-level statements about the purpose/structure of the slice, not substantive renewable-energy facts.
  - Current DOE Source URI `https://www.energy.gov/energysaver/renewable-energy` returns 404.
  - Current DOE candidate: “Renewable Energy Resource Assessment Information for the United States” (23 Jul 2026): https://www.energy.gov/cmei/renewable-energy-resource-assessment-information-united-states
  - The candidate is U.S.-specific and must not be generalized as a universal global resource assessment.
- **materials-basics**
  - NIST Materials Science and Engineering Division page is live: https://www.metallurgy.nist.gov/
  - The page describes materials measurement, models, data, standards and structure/property/processing relationships; it is relevant to the three substantive Claims.
  - The three Claims are in English in a Russian-first edition. EUs are generic and lack exact page/paragraph locators; only one Source is linked.
- **materials-science-basics**
  - Claims A–C are meta-level placeholders, not substantive materials-science knowledge.
  - Current Source URI `https://www.nist.gov/materials-science-and-engineering` returns 404.
  - Current NIST Materials Science and Engineering Division candidate: https://www.nist.gov/mml/materials-science-and-engineering-division
  - This candidate describes measurement, models, data, standards and structure-property-processing relationships, but it cannot support placeholder Claims as currently written.
- **manufacturing-basics**
  - NIST CSRC “Manufacturing Operations” glossary page directly defines manufacturing operations and enumerates facility operations, system processes, material inputs/outputs, maintenance, supply/distribution, health and safety, emergency response, human resources, security and IT.
  - URL: https://csrc.nist.gov/glossary/term/manufacturing_operations
  - The current page is direct and relevant to the three Claims, but the Claims are in English and the EUs do not point to exact lines or the underlying NISTIR source document.
- **manufacturing-systems-basics**
  - NIST Manufacturing page directly describes manufacturing innovation, measurement, production monitoring, quality and resilience, including measurement/data capabilities and production monitoring.
  - URL: https://www.nist.gov/manufacturing
  - The R22-audited record graph is unchanged. Remaining record-level issue is that EUs are generic and the one Source is a broad NIST hub; add exact section locators before publication.
- **robotics-basics**
  - Claims A–C are meta-level statements about what the slice intends to cover, not substantive robotics knowledge.
  - Current NASA Robotics page is a broad program/topic landing page: https://www.nasa.gov/technology/robotics/
  - It does not turn the placeholder Claims into domain knowledge. Rebuild the Claims and select direct NASA/academic sources.

#### Record-level findings and boundaries

1. All seven slices have a single Source and three generic EUs. A valid dependency graph does not establish source diversity or passage-level fit.
2. **fire** has three substantive wildfire emergency Claims (warnings/evacuation, multiple routes and support needs, post-fire hot ash/embers). Its source was inaccessible in this pass; the USFA materials are suitable replacement candidates. Context/Scope target Claim A only, so B/C do not inherit the boundary.
3. **renewable-energy-basics**, **materials-science-basics** and **robotics-basics** contain meta-placeholder Claims and must be rebuilt before source repair.
4. **materials-basics** and **manufacturing-basics** contain substantive English Claims and require controlled Russian translation for the Russian-first edition.
5. **manufacturing-systems-basics** is the R22 exception: all nine current record JSON blobs are identical to the audited corrected content commit. Do not repeat R22. Preserve the R22 decision; only exact EU locators remain for record-level publication screening.
6. No cross-slice Relation is present. The fire slice is related in subject matter to wildfire-smoke-safety and fire-safety-basics, but it has a distinct evacuation/post-fire hazard scope; do not add a Relation unless a concrete dependency is documented.

#### Decisions

- **fire: HOLD — all three Claims and dependency closures.** Claims are substantive, but the current Ready.gov page was inaccessible for verification, EUs are generic and USFA replacement sources are not linked.
- **renewable-energy-basics: HOLD — all three Claims and dependency closures.** Claims A–C are placeholders and the DOE Source URI returns 404.
- **materials-basics: HOLD — all three Claims and dependency closures.** NIST source is relevant; Russian translation, exact EUs and a second independent source remain.
- **materials-science-basics: HOLD — all three Claims and dependency closures.** Claims A–C are placeholders and the current NIST Source URI returns 404.
- **manufacturing-basics: HOLD — all three Claims and dependency closures.** NIST CSRC directly supports the concepts, but the Claims need Russian translation, exact locators and independent evidence.
- **manufacturing-systems-basics: HOLD — all three Claims and dependency closures.** R22 substantive audit and exact 3/3 checkpoint are reused; all current record blobs match the audited commit. Exact EU locators remain before first-edition INCLUDE.
- **robotics-basics: HOLD — all three Claims and dependency closures.** Claims A–C are placeholders; the NASA landing page is not evidence for them.

Documentation-only README updates in this block record the broken source URLs, placeholder Claims, direct source candidates and translation requirements. No canonical JSON changed.

### 39. Maps and navigation, geographic coordinates, telecommunications and networks, public risk communication, transportation and infrastructure — final eight-slice Part I screen (2026-11-19)

The eight remaining Part I slices were read from exact PR #22 HEAD 5d15f0d70d7b6b9ef061b47c47229d088adaad90. Inspected all 80 JSON records, eight README files and eight dedicated regression tests. Robotics-basics is not repeated here: its exact-record screen and HOLD decision are already recorded in the superseded working screen §38 and the controlling slice index under §36.

| Slice | Records | Sources | Claims | Evidence Use | Context | Scope |
|---|---:|---:|---:|---:|---:|---:|
| maps-and-navigation-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| geographic-coordinates-basics | 11 | 2 | 3 | 4 | 1 | 1 |
| telecommunications-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| networks-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| public-risk-communication-basics | 15 | 2 | 4 | 7 | 1 | 1 |
| transportation-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| public-transport-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| infrastructure-basics | 9 | 1 | 3 | 3 | 1 | 1 |
| **Total** | **80** | **10** | **25** | **29** | **8** | **8** |

The tests establish record profiles and selected internal dependency paths. The public-risk-communication test requires at least one Evidence Use path per Claim; the public-transport test additionally validates schema and semantic-dataset cleanliness. They do not establish pinpoint source support or complete per-Claim Context/Scope closure.

#### Direct record and source findings

1. **maps-and-navigation-basics — HOLD**
   - Claims A/B are directly supported by the USGS “Finding Your Way With Map and Compass” fact sheet: topographic maps show natural/man-made features, terrain, distance and direction; map scale relates map distance to ground distance.
   - Direct publication record: https://pubs.usgs.gov/publication/fs03501. Current educational locator: https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass.
   - The underlying fact sheet is from 2001 and its publication record labels it archived. Foundational map-reading concepts remain useful, but the old fact sheet cannot establish that a particular map, route, road, bridge or local feature is current or safe.
   - Claim C says navigation depends on map quality, scale, currency and ground conditions. Scale and map features are supported; currency and current ground conditions require current map/field data and an explicit boundary, not the old fact sheet alone.
   - All EUs only say the source is used within its material. Context/Scope target Claim A only; Claims B/C have no individual applicability boundaries.

2. **geographic-coordinates-basics — HOLD**
   - Claims A/B are supported by the USGS “27 Ideas for Teaching with Topographic Maps” resource, which directly discusses latitude/longitude, UTM, coordinate systems, datums and determining position from topographic maps. Claim C is supported in principle by USGS precision/datum discussion and OGC's coordinate-reference-system specification.
   - OGC Topic 2 is an official public standard consistent with ISO 19111; it describes coordinate reference systems, coordinate tuples, datums/reference frames, coordinate metadata and coordinate operations. Direct locator: https://docs.ogc.org/as/18-005r4/18-005r4.html.
   - The USGS Source record's source_identity is generic (“Authoritative reference source for geographic-coordinates-basics”) rather than the actual title “27 Ideas for Teaching with Topographic Maps”. Its URI is live and relevant, but bibliographic identity is defective.
   - EU-OGC is the only EU with an explicit distinct corroboration description; the three primary EUs are generic. OGC is used only for CRS/applicability, not as an end-user navigation instruction. Context/Scope target Claim A only; Claims B/C need explicit boundaries.

3. **telecommunications-basics — HOLD**
   - Claims A–C are substantive general statements about transmitting information between distant points, telecommunications infrastructure, and the role of international standards in network compatibility.
   - The canonical ITU source URI is live. The actual page title is “ITU-D Delegate Guide: What is ITU?”, not the Source identity's “Telecommunication networks and services”. It says ITU coordinates telecommunication networks and services and that ITU-T develops interoperable international standards.
   - ITU's dedicated Recommendations page more directly states that ITU-T Recommendations define how telecommunications networks operate and interwork and support worldwide network interconnectivity: https://www.itu.int/en/ITU-T/publications/Pages/recs.aspx.
   - Claim C has strong official corroboration available, but the dedicated standards page is not the canonical Source. Claims A/B are only broadly supported by the delegate guide; their EUs contain no exact section locators. Context/Scope target Claim A only.

4. **networks-basics — HOLD**
   - Claims A–C are substantive technical statements about network components, communication protocols, and Internet Protocol in packet-switched networks.
   - The only canonical Source is NIST CSRC Glossary “network” (https://csrc.nist.gov/glossary/term/network). The README says “network/protocol/IP”, but there is no separate Source record for protocol or Internet Protocol.
   - Exact NIST CSRC entries exist for “protocol” and “internet protocol”. The protocol definition is a set of rules/formats/procedures controlling communication between systems; the Internet Protocol entry describes transmission from source to destination in packet-switched communications networks. Candidate locators: https://csrc.nist.gov/glossary/term/protocol and https://csrc.nist.gov/glossary/term/internet_protocol.
   - NIST CSRC Glossary pages direct readers to the identified source publications for context; the glossary term alone is not a substitute for citing the underlying RFC/NIST/CNSSI source document.
   - All three EUs point to the network glossary page and use generic descriptions. Claims are in English while the first-edition corpus is Russian-first. Context/Scope target Claim A only. Split the source dependency by Claim and cite the actual source publications before reconsidering.

5. **public-risk-communication-basics — HOLD**
   - Four Claims A–D are substantive and cover shared understanding/action; audience/context/accessibility/trust; misinformation and protective action; and clear explanation of uncertainty/numbers with updates as threats or knowledge change.
   - UNDRR's current “Risk communication” page directly says effective risk communication builds shared understanding and supports behaviour change; ineffective communication can fuel rumours, erode trust, hamper solutions and increase risk. It also highlights last-mile reach and the effect of damaged/weak communications infrastructure. Direct page: https://www.undrr.org/risk-communication.
   - CDC's current “Understanding Risk Communication” page (September 3, 2026) directly defines public-health risk communication, explains audience/context/channel differences, changing risks, inaccurate information and trust. Its companion “Understanding and Applying Risk Communication Principles” page (September 17, 2026) addresses uncertainty, explaining numbers, audience relevance, inaccurate information and trusted messengers. Direct locators: https://www.cdc.gov/public-health-risk-communication/php/about/understanding-risk-communication.html and https://www.cdc.gov/public-health-risk-communication/php/about/understanding-and-applying-risk-communication-principles.html.
   - The seven EUs form a sensible profile: primary UNDRR links for A/B/C, additional CDC corroboration for A/B/C, and CDC support for D. The additional A-2/B-2/C-2 EUs are distinct source tracks, not accidental duplicate claim IDs. However, all descriptions remain broad and do not cite exact sections/paragraphs.
   - Context/Scope target Claim A only despite four Claims. Claim D's audience/uncertainty/numbers/update requirements need explicit per-Claim context and scope. This slice is substantively stronger than most in this batch, but is not publication-ready until the EUs are made pinpoint and all Claims receive applicable boundaries.

6. **transportation-basics — HOLD**
   - Claims A–C describe moving people/goods, system components and the dependence of safety/efficiency on infrastructure, rules, operating conditions and participant behaviour.
   - The canonical USDOT “About DOT” page supports the high-level mission to move people and goods and build infrastructure. Direct locator: https://www.transportation.gov/mission/about-dot.
   - The page is a mission/about page, not a technical description of transportation systems. It does not directly establish the full component list in Claim B or the causal factors in Claim C. A current DOT annual report or modal system/transport safety reference is a stronger candidate for those statements.
   - All EUs simply say the source is used within the stated material. Context/Scope target Claim A only. One Source only.

7. **public-transport-basics — HOLD**
   - Claims A–C describe shared mobility, common public-transport modes, and planning dependencies such as demand, network design, accessibility, capacity and resources.
   - The canonical World Bank URL https://www.worldbank.org/en/topic/transport/brief/urban-transport currently redirects to the generic Development Topics page rather than an urban-transport reference. The current World Bank Transport topic page is a possible replacement candidate and discusses transport's role linking people to opportunities and gaps in public-transport access, but it does not automatically support every mode/planning detail in the three Claims.
   - All EUs use generic “Source supports the claim within scope” text without section or data locators. Claims are in English in a Russian-first Part I edition.
   - **Identifier convention defect:** filenames use hyphenated stems (for example, CLM-PUBLIC_TRANSPORT_BASICS-A.json), while internal record_id values and references use underscore forms (for example, CLM_PUBLIC_TRANSPORT_BASICS_A). The test validates IDs and semantics but does not assert filename stem equals record_id. Do not silently normalize; resolve naming convention and downstream consumers before any canonical edit.
   - Context/Scope target Claim A only. Claims B/C lack explicit applicability boundaries. One Source only.

8. **infrastructure-basics — HOLD**
   - Claims A/B are substantively supported by the NIST Infrastructure page: it defines infrastructure as physical and organizational structures needed for society or enterprise and lists roads, bridges, dams, rail/ports, hospitals, power, food/farming, communications, manufacturing supply chains and the Internet. Direct locator: https://www.nist.gov/infrastructure.
   - Claim C states that reliability depends on interdependencies between systems. A strong current NIST candidate is the September 29, 2026 publication “Advancing Resilience Across Lifeline Infrastructure Systems: The Need for Consistent Guidance”, which explicitly describes water, wastewater, electric power, gas/liquid fuel, communications and transportation as interconnected/interdependent. Direct locator: https://www.nist.gov/publications/advancing-resilience-across-lifeline-infrastructure-systems-need-consistent-guidance.
   - The current Source is the general NIST Infrastructure page, not the interdependency research paper. EUs are generic and lack pinpoint references. Context/Scope target Claim A only; Claims B/C need per-Claim applicability boundaries. One Source only.

#### Test, language and cross-slice observations

- Dedicated tests inspected:
  - REFERENCE/tests/test_content_maps_and_navigation_basics_vertical_slice.py
  - REFERENCE/tests/test_content_geographic_coordinates_basics_vertical_slice.py
  - REFERENCE/tests/test_content_telecommunications_basics_vertical_slice.py
  - REFERENCE/tests/test_content_networks_basics_vertical_slice.py
  - REFERENCE/tests/test_content_public_risk_communication_basics_vertical_slice.py
  - REFERENCE/tests/test_content_transportation_basics_vertical_slice.py
  - REFERENCE/tests/test_content_public_transport_basics_vertical_slice.py
  - REFERENCE/tests/test_content_infrastructure_basics_vertical_slice.py
- Tests primarily verify record counts/types and Claim→Evidence Use→Source paths. The public-risk-communication test requires one Evidence Use path per Claim; the public-transport test additionally verifies schema and semantic-dataset cleanliness. None establishes pinpoint source locators or complete per-Claim Context/Scope coverage.
- **English-language inconsistency:** networks-basics and public-transport-basics use English Claims in the Russian-first Part I corpus. The other seven slices use Russian Claims. Do not translate or rewrite without authorized editorial change.
- The adjacent transportation and public-transport slices overlap by subject but are not duplicates: one is the broad transportation-system concept; the other focuses on shared passenger mobility. No new Relation is justified solely by adjacency. Telecommunications and computer networks are related but should remain distinct until a specific versioned dependency is demonstrated.
- Robotics-basics is reused from the exact-record review documented in superseded working screen §38 and remains HOLD for three meta-placeholder Claims. It is counted only once in the Part I denominator under §36.

#### Decisions

- **maps-and-navigation-basics: HOLD — all three Claims and dependency closures.** USGS supports topographic map, scale and direction fundamentals; source is a 2001 archived fact sheet; Claim C's currency/current-ground-condition assertions require current data; EUs generic; Context/Scope target A only.
- **geographic-coordinates-basics: HOLD — all three Claims and dependency closures.** USGS and OGC are relevant; USGS Source identity is generic instead of the true title; EUs lack pinpoint locators; Context/Scope target A only.
- **telecommunications-basics: HOLD — all three Claims and dependency closures.** ITU page supports network coordination and standards, but the dedicated ITU-T standards page is not linked; Source identity does not match page title; Claims A/B need exact support; EUs generic; Context/Scope target A only.
- **networks-basics: HOLD — all three Claims and dependency closures.** Source record links only NIST “network” term, not the protocol and Internet Protocol entries needed for B/C; glossary needs underlying source publications; EUs generic; Claims English; Context/Scope target A only.
- **public-risk-communication-basics: HOLD — all four Claims and dependency closures.** Strong current UNDRR and CDC support exists; seven EUs cover four Claims but lack exact section locators; Context/Scope target A only.
- **transportation-basics: HOLD — all three Claims and dependency closures.** USDOT mission supports people/goods movement but not the full component/factor claims; EUs generic; Context/Scope target A only.
- **public-transport-basics: HOLD — all three Claims and dependency closures.** World Bank Source URL redirects to a generic topic page; EUs generic; English Claims; filename/internal-ID mismatch; Context/Scope target A only.
- **infrastructure-basics: HOLD — all three Claims and dependency closures.** NIST directly supports broad definition and component list; a 2026 NIST interdependency paper is a stronger source for Claim C but is not linked; EUs generic; Context/Scope target A only.

No canonical JSON, Relations, Assessments or other content records were changed. No public INCLUDE decision is made. All eight slices remain HOLD. Technical standards, navigation, public-safety communications, transport and infrastructure-resilience claims require exact source versions and appropriate expert review before publication.

### 40. Nutrition science and food science — focused second-pass source-to-Claim audit and README rollback reconciliation (2026-11-19)

This is a follow-up to §33, not a new Part I slice or a new denominator. The exact nine canonical JSON records in `nutrition-science-basics` and nine in `food-science-basics` were re-read at PR #22 HEAD `74752548b671003b2f3b91abc8b128118083248a`. External source pages were checked against the actual Claim wording. No canonical JSON, Claim, Source, Evidence Use, Context, Scope, Relation or Assessment was changed.

#### 1. nutrition-science-basics — HOLD

**Canonical record topology:** one Source, three Claims, three Evidence Use, one Context and one Scope. All three Claims are in English; all three EUs link to the same NIH Office of Dietary Supplements (ODS) homepage. Context and Scope each target Claim A only.

| Claim | Current statement, summarized | Direct support found | Remaining gap |
|---|---|---|---|
| A | Nutrition science studies how nutrients and other food components relate to human health and physiological function | WHO Healthy diet describes diet's role in individual/population health; OpenStax Biology 2e §34.2 explains food components, nutrient functions and cellular function | No pinpoint EUs; current ODS homepage is supplement-focused, not a general nutrition-science source |
| B | Nutrients participate in energy metabolism, tissue maintenance and regulation of physiological functions | OpenStax Biology 2e §34.2 directly discusses nutrients for cellular function, biosynthesis/growth/maintenance, ATP production and vitamins/minerals in structure/regulation | OpenStax §34.2 is not linked in canonical Source/EU records; EU description is generic and does not identify a passage |
| C | Nutrition guidance depends on dietary patterns, individual characteristics, life stage, health status and evidence quality | WHO Healthy diet (26 Jan 2026) directly says dietary composition varies with age, gender, lifestyle, activity, cultural context, locally available foods and dietary customs; ODPHP's Dietary Reference Intakes development page describes systematic evidence reviews, relevant health outcomes, knowledge gaps and independent peer review | WHO page does not by itself establish every listed modifier (notably health status and evidence-quality method); ODPHP DRI methodology is US/DRI-specific and not a universal rule for every nutrition recommendation. Neither candidate is linked in the current records |

**Source findings and exact locators**

- Current canonical Source: NIH Office of Dietary Supplements, `https://ods.od.nih.gov/`. This is a real and authoritative NIH office, but its declared remit is dietary-supplement research and information. Its “For Health Professionals” page explicitly describes evidence-based information for discussing dietary supplements and fact sheets about vitamins, minerals, herbs and other ingredients. It is therefore too narrow as the sole general source for the three Claims.
- WHO, “Healthy diet”, dated 26 January 2026: `https://www.who.int/news-room/fact-sheets/detail/healthy-diet`. Relevant passages are the Overview (life-course diet and health), the four principles of adequacy/balance/moderation/diversity, and the paragraph explaining variation by individual characteristics, cultural context, locally available foods and dietary customs. This is the strongest general public-health source for Claim A and the context-dependence portion of Claim C.
- OpenStax, Biology 2e, §34.2 “Nutrition and Energy Production”: `https://openstax.org/books/biology-2e/pages/34-2-nutrition-and-energy-production`. Relevant subheadings are “Food Requirements”, “Organic Precursors”, “Essential Nutrients” and “Food Energy and ATP”. These support the functions and biological roles in Claims A/B. This source is an educational biology text and should not be used to derive individualized nutrient prescriptions or treatment recommendations.
- U.S. Office of Disease Prevention and Health Promotion, “Dietary Reference Intakes Development”: `https://odphp.health.gov/our-work/nutrition-physical-activity/dietary-guidelines/dietary-reference-intakes/dietary-reference-intakes-development`. It describes NASEM committee use of systematic reviews, health outcomes selected on strength/relevance of evidence, independent peer review, special considerations and knowledge gaps. It can support a carefully bounded description of the US DRI process, not the proposition that all nutrition guidance everywhere follows one identical process.
- ODPHP, “Maintaining Dietary Reference Intakes”: `https://odphp.health.gov/our-work/nutrition-physical-activity/dietary-guidelines/dietary-reference-intakes/maintaining-dietary-reference-intakes`. It explains evidence scanning and systematic reviews of adequacy, potential toxicity and chronic-disease risk. This is a useful second locator for the evidence-quality component of Claim C, subject to the same US DRI boundary.

**Evidence Use defects**

- EU A, EU B and EU C all use the same Source ref (ODS homepage) and the same generic description: “Source supports the claim within the stated scope.”
- The current EU records do not identify a chapter, heading, section, paragraph, table or other pinpoint locator.
- ODS is not irrelevant: it is a credible source for supplement-specific evidence, safety, and nutrient fact sheets. The defect is the mismatch between its narrow remit and the broad nutrition-science Claims, not institutional authority.
- Do not silently replace the ODS Source or repoint EUs. A controlled, versioned editorial decision should decide whether to retain ODS as a supplement-specific supporting Source, add WHO/OpenStax/ODPHP Sources, or narrow the Claims.

**Context, Scope and language**

- Context and Scope both target Claim A only. Claims B and C have no explicit record-level applicability boundary. The README or a general educational label cannot silently extend formal Context/Scope to them.
- All three Claims are English in a Russian-first Part I edition. They require controlled translation and review, not ad hoc machine translation.
- Health boundary: these are foundational educational statements, not personal dietary prescriptions, diagnosis, treatment, supplement recommendations or clinical nutrition advice. Any applied guidance must state population, age/life stage, health status, relevant conditions/medications, geography, food availability and the specific guideline/evidence framework.

**Decision: HOLD — all three Claims and dependency closures.** The claims are broadly plausible and can be supported with better-matched sources, but current linked evidence does not establish the stated scope. Required before reconsideration: controlled Russian translation; source records for the WHO/OpenStax/ODPHP materials selected by editorial review; pinpoint EU descriptions per Claim; explicit Context/Scope coverage for Claims B/C; and a clear boundary between general nutrition science, public-health dietary guidance and individualized clinical advice.

#### 2. food-science-basics — HOLD

**Canonical record topology:** one Source, three Claims, three Evidence Use, one Context and one Scope.

- Claims A–C are not food-science facts. They describe the slice's intended content, the need to consider source/context/scope, and the fact that general information does not replace specialist assessment. These are documentation/editorial meta-statements and cannot serve as the substantive knowledge Claims of a food-science vertical slice.
- The sole Source is identified as “OpenStax — Food Science” and points to `https://openstax.org/books/biology-2e/pages/34-1-nutrition-and-energy-production`. The locator does not identify the actual relevant section.
- The actual OpenStax Biology 2e §34.2 is titled “Nutrition and Energy Production”: `https://openstax.org/books/biology-2e/pages/34-2-nutrition-and-energy-production`. It concerns animal nutrition, nutrients and energy production; it is not a general food-science source covering food chemistry, processing, preservation, safety, sensory properties or food systems.
- All three EUs point to the same misidentified Source and use the generic text “Указанный источник используется в пределах заявленного материала.” No exact passage is supplied.
- Context and Scope target Claim A only. That does not cure the fact that all three Claims are meta-level placeholders.

**Decision: HOLD — all three Claims and dependency closures.** Do not merely change the Source URL to §34.2 and treat the slice as repaired. First define the intended food-science domain and replace the placeholder Claims with substantive, bounded knowledge claims; then select sources that directly support those claims, add exact locators and per-Claim Context/Scope, and run the slice's regression and semantic checks. No translation is the primary blocker here; content validity and source fit are.

#### 3. README rollback reconciliation for §33

The earlier §33 screen described several README changes as “now” present. The subsequent exact-head preflight on the PR branch rejected modifications to 13 existing vertical-slice directories because they lacked explicit editorial-correction authorization. To restore the repository's wave-safety rule, the following README files were returned to their parent-commit contents: `environmental-health-basics`, `fire`, `food-science-basics`, `hydrology-basics`, `manufacturing-basics`, `materials-basics`, `materials-science-basics`, `microbiology-basics`, `nutrition-science-basics`, `public-health-basics`, `renewable-energy-basics`, `robotics-basics`, and `water-filter-assessment`.

Consequently, statements in §33 that those README files “now” contain the audit boundary/HOLD note describe the attempted documentation-only pass, not the current file contents. Treat the audit findings and dispositions in §33 as retained findings in this register; do not assume the corresponding README edits remain. The epidemiology README was not part of the 13-file rollback list. No canonical JSON was changed by the rollback.

This rollback is intentional and preserves the preflight authorization model. Any future README correction to an existing slice must be covered by the repository's explicit editorial-correction process before it is made. Do not add slice slugs to the authorization manifest merely to silence CI: authorization must be grounded in an actual approved correction scope.

#### 4. Follow-up priority

1. Nutrition: prepare a bounded source proposal and exact EU locator matrix for editorial approval; preserve the current ODS Source unless a versioned decision changes its role.
2. Food science: define substantive scope and replacement Claim set before source selection; the current three meta-Claims are not salvageable by locator repair alone.
3. Do not modify canonical JSON or existing slice READMEs in this pass. Both slices remain HOLD and no public INCLUDE is granted.

### 41. Physiology, microbiology and sleep — focused second-pass Claim-to-source and rights audit (2026-11-19)

This follow-up deepens the three-slice portion of §33. Exact current records were re-read at PR #22 HEAD `f56f3084459c6a813f0123a1c5b7c6e3766c4a69`: 27 JSON records in total (three slices × nine records). Official source pages and section-level locators were checked. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. physiology-basics — HOLD

**Topology:** one Source, three substantive Russian Claims, three Evidence Use, one Context and one Scope.

- **Claim A:** “Физиология изучает функции организма и то, как его структуры работают совместно.” Directly supported by OpenStax Anatomy and Physiology 2e §1.1, “Overview of Anatomy and Physiology”, which defines physiology as the scientific study of the chemistry and physics of body structures and how they work together to support life. Locator: `https://openstax.org/books/anatomy-and-physiology-2e/pages/1-1-overview-of-anatomy-and-physiology`.
- **Claim B:** “Гомеостаз описывает поддержание относительно устойчивых внутренних условий организма.” §1.1 directly defines homeostasis as steady internal conditions maintained by living things. The more detailed Chapter Review and §1.5 “Homeostasis” describe narrow compatible ranges and feedback mechanisms. Candidate pinpoint: `https://openstax.org/books/anatomy-and-physiology-2e/pages/1-5-homeostasis`.
- **Claim C:** “Органные системы выполняют различные функции и взаимодействуют для поддержания жизнедеятельности.” §1.1 supports the broad relationship of structures and functions; §1.2 “Structural Organization of the Human Body” directly describes organ systems as groups of organs working together to perform major functions and meet physiological needs. Candidate pinpoint: `https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body`.

**Evidence Use / Source fit**

- The current Source URL is a valid exact section 1.1, but the Source identity “OpenStax Anatomy and Physiology 2e — overview” is an abbreviated title rather than the exact bibliographic title.
- All three EUs name the overview generally but do not identify the specific sentence, subsection or heading. Claim B is better pinned to §1.5; Claim C needs §1.2 as well as §1.1.
- A single textbook is adequate for an introductory educational claim set only if the limits are explicit; the absence of a second institution is not by itself proof that the claims are false. A second independent source would improve triangulation but is not the primary blocker here.

**Context / Scope / boundaries**

- Context correctly states that the material is not an individual medical assessment, diagnosis or recommendation. Scope says the slice is foundational and not exhaustive.
- Both formal records target Claim A only. Claims B/C have no formal record-level Context/Scope target. Claim C's “maintaining life” language should remain a broad physiology description, not a clinical interpretation of organ function or disease.
- Claims are Russian; no translation issue identified.

**Decision: HOLD — all three Claims and dependency closures.** The claims are supportable, and precise OpenStax sections are identified. Before reconsideration, correct the bibliographic Source identity through a controlled metadata version, add the section-level source dependency for Claims B/C, write pinpoint EU descriptions, and provide explicit Context/Scope coverage for B/C. Do not alter the current @1 records without approved versioned editorial authorization.

#### 2. microbiology-basics — HOLD; additional source-rights gate

**Topology:** one Source, three substantive Russian Claims, three Evidence Use, one Context and one Scope.

- **Claim A:** microorganisms are organisms, most too small to be observed without a microscope. OpenStax Microbiology Chapter 1 Introduction states that microorganisms are small organisms and most cannot be seen without a microscope. Section 1.3 “Types of Microorganisms” adds useful nuance: some unicellular microbes are visible and some multicellular organisms are microscopic. Direct locators: `https://openstax.org/books/microbiology/pages/1-introduction` and `https://openstax.org/books/microbiology/pages/1-3-types-of-microorganisms`.
- **Claim B:** microorganisms are widespread and perform important ecological functions. Chapter 1 Introduction directly describes their presence across environments and fundamental ecosystem roles; Chapter 4 Introduction describes prokaryotes as important to shaping and sustaining the biosphere. Chapter 8 Introduction provides a further direct treatment of microbial metabolism and biogeochemical roles. Locators: `https://openstax.org/books/microbiology/pages/1-introduction`, `https://openstax.org/books/microbiology/pages/4-introduction`, `https://openstax.org/books/microbiology/pages/8-introduction`.
- **Claim C:** microorganisms may be beneficial, neutral or pathogenic depending on organism/context. Chapter 1 Introduction supports the main contrast: most are harmless, many helpful, and some cause disease. However, “neutral” is not the exact classification used in that introductory passage. The American Society for Microbiology curriculum statements reproduced in the OpenStax Preface explicitly classify interactions of cellular and viral microorganisms with hosts as beneficial, neutral or detrimental; the same preface says these are ASM recommended curriculum guidelines. This is a supporting conceptual locator, but a dedicated independent ASM source is preferable for the final Source chain.

**Evidence Use / Source identity**

- All three EUs point to the same OpenStax Chapter 1 Introduction and use generic descriptions; none identifies a section or passage.
- The Source identity “Authoritative reference source for microbiology-basics” is not bibliographic identification. The URI resolves to “Ch. 1 Introduction — Microbiology” by OpenStax.
- The current Source alone does not adequately pinpoint ecological roles in Claim B or the three-part beneficial/neutral/detrimental distinction in Claim C. Chapter 4/8 and a separate ASM source are stronger candidate dependencies.

**Material rights finding — do not overlook**

- The OpenStax Microbiology Preface states that the book is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0), requiring attribution and ShareAlike for derivatives and limiting reuse/remixing to noncommercial purposes.
- The same Preface expressly says the book may not be used for training large language models or otherwise ingested into LLM offerings without OpenStax's prior written permission. It also directs users intending to incorporate material into LLMs, AI offerings or commercial uses to request permission.
- This is a distinct rights/operations gate, not a factual-source-quality issue. A public URL or the ability to read the page is not blanket permission to reproduce, adapt, ingest or commercially print its content. Before using this text in an AI-assisted editorial workflow or reproducing/adapting it in a release, obtain and record the required permission or choose an independently verified source whose terms permit the intended use. Do not assume the book's CC BY-NC-SA label overrides the separate LLM restriction.
- The canonical records store only bibliographic metadata and short paraphrased Claims, not textbook passages or images. This audit does not grant any reuse permission and is not a legal determination.

**Context / Scope / biosafety**

- Context and Scope target Claim A only. Claims B/C do not inherit those formal boundaries.
- The current claims are introductory and not laboratory instructions. Keep this slice descriptive. Do not expand it into pathogen handling, culturing, enrichment, growth optimization, virulence enhancement or operational pathogen work without a separate biosafety and expert-review gate.
- Claims are Russian; no translation issue identified.

**Decision: HOLD — all three Claims and dependency closures.** Factual support is promising, but exact EU locators, proper Source identity, a direct source for Claim C's exact three-part classification, per-Claim Context/Scope, and the OpenStax rights/AI-ingestion restriction must be resolved. The rights restriction is independently sufficient to prevent treating OpenStax Microbiology as an unrestricted source for the project's AI-assisted content workflow.

#### 3. sleep-basics — HOLD

**Topology:** one Source, three substantive Russian Claims, three Evidence Use, one Context and one Scope.

- **Claim A:** sleep includes repeating REM and non-REM stages. The current Source page “How Sleep Works” says sleep cycles through stages but does not name the phases in the page's summary. NHLBI's dedicated “Sleep Phases and Stages” page directly identifies REM and non-REM and says the cycle repeats every 80–100 minutes, usually four to six times a night. Pinpoint: `https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep`.
- **Claim B:** internal circadian clocks have an approximately 24-hour rhythm and respond to light/dark. The current Source page directly supports this. NHLBI's dedicated “What Makes You Sleep?” and “Your Sleep/Wake Cycle” pages further explain light, darkness and other environmental cues. Pinpoints: `https://www.nhlbi.nih.gov/health/sleep-deprivation/body-clock` and `https://www.nhlbi.nih.gov/health/sleep/sleep-wake-cycle`.
- **Claim C:** insufficient quality sleep can affect health, attention and other functions. The current page directly supports heart/respiratory health, metabolism and focus; the dedicated NHLBI “Why Is Sleep Important?” page supports effects on physical health, thinking, learning, reaction and memory. Pinpoint: `https://www.nhlbi.nih.gov/health/sleep/why-sleep-important`.

**Evidence Use / Source fit**

- The current NHLBI Source page is real and authoritative, and its “How Sleep Works” identity is substantially accurate.
- All three EUs point to the same broad page and have no exact subsection locator. Claim A should point to the dedicated REM/non-REM stages page, not rely only on the general summary; Claim C should point to the dedicated health-effects page.
- The current Source record can remain as an overview source if the editorial design permits; the dedicated NHLBI pages should be added as distinct Source records or otherwise represented by the approved source-version model. Do not insert unrecorded URLs into EU prose and call that a completed source chain.

**Context / Scope / health boundary**

- Context appropriately says general physiological patterns do not diagnose an individual sleep disorder; Scope says the slice is foundational and not exhaustive.
- Both target Claim A only. Claim C explicitly concerns health effects, so its own Context/Scope boundary is particularly important: population-level associations and general effects are not a diagnosis of an individual's fatigue, concentration problems, sleep disorder or other condition.
- Claims are Russian; no translation issue identified.
- NHLBI pages are official U.S. public-health education materials. Their general sleep-health statements should not be converted into personalized treatment instructions or universal recommendations without population and age context.

**Decision: HOLD — all three Claims and dependency closures.** The claims have direct, high-quality NIH/NHLBI support. The remaining blockers are exact section-level EUs, explicit Context/Scope for Claims B/C, and a source-chain update to the dedicated NHLBI pages. This is a narrower repair than placeholder-content slices; no public INCLUDE is granted.

#### 4. Cross-slice outcome and next work

| Slice | Claim substance | Source fit | EU precision | Context/Scope closure | Additional gate |
|---|---|---|---|---|---|
| physiology-basics | Substantive | Good, one OpenStax textbook | Missing exact §1.1/§1.2/§1.5 mapping | A only | Correct bibliographic identity |
| microbiology-basics | Substantive | Relevant OpenStax, but single-source and metadata defect | Missing; Claims B/C need further locators | A only | CC BY-NC-SA and explicit no-LLM-ingestion-without-permission restriction |
| sleep-basics | Substantive | Strong official NHLBI/NIH source | Dedicated stages/body-clock/health-effects pages needed | A only | Maintain non-diagnostic boundary for Claim C |

The three slices contain **27 records** in total. No canonical records were changed. All three remain HOLD. Next remediation should prioritize microbiology's rights decision before any additional AI-assisted source use, then prepare a versioned locator proposal for sleep and physiology. Existing @1 records must remain immutable; any approved correction must create the appropriate new versions and update references without rewriting historical evidence.

### 42. Epidemiology-basics — placeholder-Claim replacement design and source-dependency audit (2026-11-19)

This is a focused follow-up to §33's narrowly reopened epidemiology closure. Exact current Claim A–D, both Source records, Context/Scope and available A–C Evidence Use records were inspected at PR #22 HEAD `98c6d90fc8a5e9bfaf4935b0cce0c7bd82d915bc`. Official CDC and WHO source pages were checked. No canonical record was edited and no replacement wording is approved by this screen.

#### Current record defects

- Claim A: “Срез epidemiology-basics описывает базовые понятия предметной области и их взаимосвязи.” This is a description of the document, not epidemiological knowledge.
- Claim B: “Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.” This is an editorial rule, not an epidemiology fact.
- Claim C: “Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.” This is a general disclaimer, not an epidemiology fact.
- Claim D is a substantive definition but remains in English: “WHO describes epidemiology as the study of the distribution and determinants of health and disease in populations and its application to prevention and control.”
- Current CDC Source: “CDC — Principles of Epidemiology”, URI `https://www.cdc.gov/training-publichealth101/php/lessons/principles-of-epidemiology.html`. This source identity/locator does not match the current CDC “Introduction to Epidemiology” course locator discovered during this pass.
- Current WHO Source: “WHO — Putting participatory surveillance into practice”, URI `https://www.who.int/news/item/16-10-2024-putting-participatory-surveillance-into-practice--new-who-publication-released`. This is a publication about participatory surveillance practice, not the strongest general source for the foundational definition in Claim D.
- Context and Scope both target Claim A only, which is itself a meta-placeholder. Neither supplies usable formal boundaries for a replacement substantive Claim set.

#### Stronger authoritative sources and exact support

1. **WHO, Basic Epidemiology, 2nd edition (2006), Chapter 1, Box 1.2 “Definition of epidemiology”.**
   - Official publication record: `https://www.who.int/publications/b/31231`.
   - Official WHO IRIS PDF: `https://iris.who.int/bitstream/handle/10665/43541/9241547073_eng.pdf`.
   - The definition explicitly covers study; distribution; determinants; health-related states/events; specified populations; and application to prevention/control. Box 1.2 explains distribution through time, persons, places and affected classes; determinants through biological, chemical, physical, social, cultural, economic, genetic and behavioural factors.
   - This is a strong general reference for the core definition and terminology. Confirm publication reuse rights before reproducing or adapting any substantial text; storing a citation and writing an independently phrased Claim is not the same as receiving permission to reproduce the book.

2. **CDC, Introduction to Epidemiology, Public Health 101 Series (10 January 2025).**
   - Direct course page: `https://www.cdc.gov/training-publichealth101/php/training/introduction-to-epidemiology.html`.
   - Learning objectives directly identify defining epidemiology, basic terms, data sources, collection/interpretation methods, describing public-health problems by time/place/person and descriptive outbreak investigation components.
   - The course's slide presentation is explicitly described by CDC as public domain and may be downloaded/customized for informational or educational use with citation. This makes the CDC slide material a stronger rights-cleared candidate for an educational corpus than assuming all third-party textbooks are freely reusable.
   - The page is a course overview, so pinpoint Claims to the relevant slide/lesson, not merely the course landing page.

3. **CDC, archived Principles of Epidemiology, Lesson 1 Section 1 — Definition of Epidemiology.**
   - Direct locator: `https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html`.
   - Directly explains the distribution/determinants/population/control components and elaborates frequency, pattern, time, place, person and determinants. This is a useful exact locator for foundational concepts, but it is an archived course. Prefer the current CDC course for current training context and use the archived lesson only when its exact methodological definition is required and its archived status is made explicit.
   - CDC's Lesson 1 Section 5 “The Epidemiologic Approach” explains case definition, counting, time/place/person description, denominators, rates and comparison groups: `https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section5.html`.

#### Proposed replacement Claim architecture — editorial proposal only

The following are candidate concepts for a controlled Russian rewrite, not canonical changes and not permission to edit @1 records:

| Candidate | Proposed substantive statement | Source dependency |
|---|---|---|
| A | Эпидемиология изучает распределение и детерминанты связанных со здоровьем состояний и событий в определённых популяциях и применяет это знание для профилактики и контроля проблем здоровья. | WHO Basic Epidemiology, Ch. 1 Box 1.2; CDC Introduction to Epidemiology |
| B | Описательная эпидемиология характеризует частоту и распределение событий, в том числе по времени, месту и характеристикам людей или групп. | CDC Principles of Epidemiology, Lesson 1 §§1 and 5; WHO Basic Epidemiology, Ch. 1 |
| C | Аналитическая эпидемиология сравнивает группы и исследует факторы, связанные с различиями в частоте событий и состояниях здоровья. | CDC Principles of Epidemiology, Lesson 1 §§1 and 5; WHO Basic Epidemiology, Ch. 1 |
| D | Эпидемиологические выводы относятся к определённым популяциям, периодам, определениям случаев и источникам данных; сами по себе наблюдаемые связи не доказывают причинность. | WHO Basic Epidemiology, Ch. 1 and methods chapters; CDC Principles of Epidemiology, Lesson 1 §§1 and 5 |

The D candidate deliberately adds a boundary that prevents readers from treating population-level associations as an individual diagnosis or as proof of causation. Before approval, verify the exact supporting chapter/section for the causation limitation and avoid broadening the Claim beyond the cited methodology.

#### Evidence Use and dependency defects

- EU A–C each links only to the CDC Source and repeats the current meta-Claim wording in its description. The description may accurately identify what the current Claim says, but it cannot turn a meta-Claim into epidemiological knowledge.
- Claim D links to the WHO participatory-surveillance Source. That Source is not a suitable sole locator for the general definition; the WHO Basic Epidemiology publication or the CDC course should replace/supplement it only through versioned Source and EU records.
- The three A–C EU descriptions have no section/slide pinpoint. They should be retired by versioned replacement when Claims are substantively rewritten; do not simply change their descriptions while leaving the meta-Claims intact.
- No EU should imply that surveillance data automatically establish causation, that rates are comparable without appropriate denominators/definitions, or that population findings diagnose individuals.

#### Context, Scope, and public-health boundary

- Replace the current Context/Scope target on placeholder Claim A only after the new Claim set is approved.
- At minimum, define the population, health event/state, time period, geography, case definition, data source and method where those variables are material.
- Distinguish descriptive epidemiology (frequency/pattern) from analytic epidemiology (hypothesis testing/comparison and determinants). A descriptive pattern alone is not a causal conclusion.
- Epidemiological statistics and surveillance summaries describe populations and must not be presented as individualized diagnosis or treatment advice. Outbreak thresholds, reportability and public-health action depend on jurisdiction, current surveillance definitions and responsible authorities.
- All four Claims should be in Russian for the Russian-first edition. Preserve recognized technical terms with concise definitions where useful.

**Decision: HOLD — all four Claims and dependency closures.** Claims A–C must be replaced as substantive knowledge statements; Claim D needs controlled translation and a better-aligned source dependency. The two current Source records do not yet form a coherent, pinpointed source chain for the intended slice. Rebuild this slice under a new, authorized versioned editorial correction; preserve the historical @1 records and their original EUs. No public INCLUDE is granted.

#### Next execution order

1. Obtain editorial authorization for a new substantive Claim set and controlled Russian wording.
2. Select WHO Basic Epidemiology and/or the current CDC Public Health 101 course as canonical Sources; record exact edition, date, chapter/slide locators and reuse-rights status.
3. Version the new Claims, Sources and EUs; do not mutate historical @1 records.
4. Create explicit Context/Scope coverage for every new Claim.
5. Add regression checks that reject meta-placeholder Claim wording and verify each Claim's source/version and locator.
6. Re-run exact-head preflight, Reference Tests, Release Gate and Offline Edition. Keep HOLD until factual review and release gates are complete.

### 43. Anatomy-basics — M2 closure reuse versus current source-locator integrity (2026-11-19)

This is a narrow exact-record and current-source recheck of anatomy-basics, not a repeat of the completed M2 substantive/Human View audit. The 11-record slice was inspected at PR #22 HEAD `c6b41ad224bb2c209c82fd8ff5adf49d7fae2781`; the historical M2 audit and debt map were read in full; the current external source URLs and relevant OpenStax sections were checked. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. Reuse of historical M2 work — retained, not repeated

- `RELEASE/M2-SUBSTANTIVE-RE-AUDIT-2026-10-08.md` records PASS for 10/10 scoped slices, including anatomy-basics. It says the anatomy single-source debt was closed by adding an independent OpenStax evidence track and a descriptive-versus-clinical boundary.
- `RELEASE/M2-UNIFIED-DEBT-MAP-2026-10-08.md` marks M2-03 closed and records the evidence-independence, Human View/adversarial and substantive closure commits. Its closure rule requires agreement between canonical content, Evidence Use provenance, regression, documentation and audit evidence.
- The current anatomy slice has 11 records: two Sources, three Claims, four Evidence Use, one Context and one Scope. This matches the M2 target topology. The current README retains the descriptive-anatomy versus individual clinical diagnosis/treatment boundary.
- M2's historical exact-checkpoint PASS is not re-labelled as a current exact-HEAD CI PASS. Nor is the historical semantic review discarded. This pass checks whether the current source URLs and EU mapping still substantiate the existing records.

#### 2. Current Claim-to-source mapping

| Claim | Canonical statement | Direct evidence observed | Current EU coverage |
|---|---|---|---|
| A | Ткани состоят из клеток, организованных для выполнения определённых функций. | OpenStax A&P 2e §4.1 directly defines tissue as cells found together and arranged to achieve tissue functions; NIGMS glossary defines tissue as cells acting together for a specific function. | NIGMS EU A plus OpenStax corroboration EU A |
| B | Органы состоят из нескольких типов тканей, работающих совместно. | OpenStax A&P 2e §1.2 directly defines an organ as an anatomically distinct structure composed of two or more tissue types; §4.1 says several tissue types form a working unit at the organ level. | NIGMS EU B; no dedicated OpenStax EU for B |
| C | Системы органов объединяют органы, взаимодействующие для выполнения связанных функций. | OpenStax A&P 2e §1.2 directly defines an organ system as a group of organs working together to perform major functions or meet physiological needs. | NIGMS EU C; no dedicated OpenStax EU for C |

Relevant OpenStax locators:
- §4.1 Types of Tissues: `https://openstax.org/books/anatomy-and-physiology-2e/pages/4-1-types-of-tissues`.
- §1.2 Structural Organization of the Human Body: `https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body`.

The exact §1.2 passage is particularly strong for Claims B and C: it defines organs as structures composed of two or more tissue types and organ systems as groups of organs working together. The existing OpenStax Source record, however, points only to §4.1. A page cited in an audit narrative does not become part of the canonical source chain automatically.

#### 3. Source availability and identity defect — new current finding

- Current NIGMS Source record `SRC-ANATOMY_BASICS@1` identifies “NIGMS — Cells, tissues, organs and systems” and points to `https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx`.
- The exact URL could not be retrieved in the current web check (open returned an internal access error); a targeted search did not surface the titled fact sheet. The current NIGMS education glossary is available at `https://www.nigms.nih.gov/education/glossary` and contains direct entries for “Tissue” and “Organ”, but it is a different resource and does not reproduce the old page's complete title or URL. Do not silently treat the glossary as the same Source version.
- The NIGMS glossary confirms that a tissue is a group of cells acting together for a specific function and that organs are made up of tissues. It therefore offers a candidate replacement/updated Source for A/B, but its available entries do not independently establish the complete Claim C wording about organ systems.
- OpenStax §4.1 is directly suitable for Claim A and provides an additional tissue-to-organ transition. OpenStax §1.2 is directly suitable for Claims B and C. These are two distinct section locators and should be represented as such in a controlled source-version model.
- The current OpenStax corroboration EU `EU-ANATOMY-OPENSTAX-CORROBORATION@1` targets Claim A only. It must not be counted as canonical direct evidence for B/C merely because §1.2 is cited in this audit.

#### 4. Context, Scope and clinical boundary

- Current Context and Scope both target Claim A only. Claims B and C have no formal Context/Scope target; the README's general boundary is not a substitute for explicit record-level targets.
- Preserve the existing descriptive-versus-clinical boundary: the hierarchy of cells, tissues, organs and organ systems is an educational anatomical model, not an individual diagnosis, prognosis or treatment recommendation.
- Keep anatomical variation explicit where later claims become more detailed. “Typical human anatomy” should not be treated as a universal description of every individual, developmental stage, congenital variation or surgical state.
- The current three Claims are Russian and are not placeholder statements. No semantic rewrite is indicated by this pass.

#### 5. Decision

**HOLD — all three Claims and dependency closures, with historical M2 substantive PASS retained as a historical result.** This is not a reversal of M2's completed semantic audit. It is a current source-availability and exact dependency-coverage issue: the NIGMS URL is not currently retrievable, and the existing OpenStax canonical corroboration only targets Claim A even though §1.2 directly supports B/C.

Required before reconsideration:
1. Verify whether the original NIGMS page moved or was retired. If the current NIGMS glossary is selected, add it as a distinct versioned Source with accurate identity and locator; do not rewrite `SRC-ANATOMY_BASICS@1`.
2. Add/authorize a distinct OpenStax §1.2 Source dependency for Claims B/C (or another source with equivalent direct support), with Claim-specific Evidence Use records and pinpoint locators.
3. Decide whether Context/Scope should explicitly target B and C, or whether the schema supports a justified shared boundary record; do not infer inheritance.
4. Re-run current exact-HEAD regression and source-chain checks after any authorized correction. Do not re-run the entire M2 substantive audit unless content itself changes.

No public INCLUDE is granted. No canonical JSON or other content record was edited in this screen.

### 44. Public health and environmental health — exact Claim/EU source mapping and population-risk boundaries (2026-11-19)

This is a focused second-pass source-to-Claim audit of the 24 canonical records in `public-health-basics` and `environmental-health-basics`. The current four Claims, Source identities/URIs, Evidence Use descriptions and Context/Scope targets were inspected at PR #22 HEAD `2dfdacc4366e01e519c5f67b6348c7109a38c2d0`; current WHO, CDC and EPA pages were checked. Historical P6/P9/P13 substantive findings are reused rather than repeated. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. public-health-basics — HOLD

**Current claims and source fit**

- **A:** “Общественное здравоохранение направлено на улучшение здоровья популяций и профилактику заболеваний.” The WHO European Observatory page “Public health” directly says public health aims to improve population health and prevent disease. The source is an appropriate WHO European Observatory policy overview, but its institutional identity should be represented accurately as the European Observatory on Health Systems and Policies, rather than implying this is a WHO global technical fact sheet. Locator: `https://eurohealthobservatory.who.int/themes/health-system-functions/public-health`.
- **B:** “К общественному здравоохранению относятся наблюдение за здоровьем населения, профилактика, защита здоровья и реагирование на угрозы.” The same Observatory page directly lists surveillance, response to health hazards/emergencies, health protection, health promotion and disease prevention. This is a strong direct match.
- **C:** “Популяционные меры общественного здравоохранения применяются на уровне групп и сообществ, а не только отдельных людей.” The source is population-focused and describes population health and public-health action. The statement is directionally consistent, but its contrast “not only individuals” is stronger than the page's wording. It would be more precise to say that public health focuses on population-level health and coordinated action while also including services delivered to individuals (e.g., early detection, vaccination or preventive services). Avoid a false dichotomy between public health and individual services.
- **D:** “CDC describes public health as including core functions, essential services and attention to determinants that affect population health.” This is an English meta-attributed statement, not a Russian-first Claim. CDC's “Introduction to Public Health” (10 January 2025) directly identifies mission, core functions, essential services, determinants and their effects on population health. Locator: `https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health.html`. The source is directly aligned.

**Evidence Use precision**

- EU A, B and C all point to the WHO European Observatory page and repeat only “Источник WHO — Public health используется в пределах указанного материала.” These descriptions do not identify the specific paragraph or activity list.
- EU D points to the CDC course and has a better claim-specific description, but still lacks a lesson/slide locator. The CDC course page links a slide presentation and references; the page's course objectives support the high-level Claim.
- CDC explicitly says its slide sets are public domain and may be downloaded/customized for informational or educational use with citation. This is a clear reuse route for the slide material, subject to accurate citation and the scope of that public-domain statement. It should not be generalized to every third-party resource linked from the course.

**Context/Scope and language**

- Current Context and Scope both target Claim A only. The population-level versus individual-clinical boundary is relevant to all four Claims and is not formally attached to B–D.
- Claim D remains English. Translate it into a direct substantive Russian statement (for example, the core public-health functions and essential services are commonly organized around assessment, policy development and assurance) only after the exact CDC slide/lesson is selected. Do not retain “CDC describes…” as the Claim's main proposition if the objective is to state domain knowledge.
- Avoid presenting the U.S. CDC's service framework as a universal legal or administrative structure applying identically in every country. Label it as a recognized U.S. public-health framework if retained.

**Decision: HOLD — all four Claims and dependency closures.** Claims A/B have a direct WHO European Observatory match; D has a direct CDC match; C needs tighter wording to avoid an artificial public-health-versus-individual-services dichotomy. Required: accurate source identity, pinpoint EU locators, controlled translation and substantive framing of D, and explicit Context/Scope coverage for B–D.

#### 2. environmental-health-basics — HOLD

**Current claims and source fit**

- **A:** “Здоровье зависит от условий окружающей среды, включая качество воздуха, воды и санитарии, воздействие химических факторов и климатические условия.” WHO's current “Environmental health” page directly lists clean air, stable climate, adequate water, sanitation and hygiene, harmful radiation, chemical management and unhealthy working conditions. Locator: `https://www.who.int/health-topics/environmental-health`.
- **B:** “Оценка экологических рисков для здоровья использует сведения об экспозиции и связи между воздействием и последствиями для здоровья.” WHO's overview supports the broad environmental-determinants framing, but EPA's “Human Exposure and Health” is the much more direct source for the exposure pathway and its relationship to possible health outcomes. EPA explains source/release → environmental media (air, water, land) → human contact/entry routes → sufficient dose → possible biological change/adverse outcome. It also warns that contamination or exposure alone does not mean disease will occur. Locator: `https://www.epa.gov/report-environment/human-exposure-and-health`.
- **C:** “Экологическое здоровье требует межсекторного рассмотрения, поскольку факторы риска связаны с транспортом, энергетикой, сельским хозяйством, городами и другими системами.” WHO directly says cross-sectoral collaboration is crucial and names health, energy, industry, agriculture and transport. Its overview also discusses climate, biodiversity, pollution, food production, migration, economic instability and social inequalities. Direct locator: the WHO Environmental health overview above.
- **D:** English statement on the EPA exposure pathway and multiple contributors to health outcomes. EPA directly supports the conceptual point and explicitly states that the relationship between contamination, exposure and disease is complex; exposure is only one factor among potentially multiple contributors. The current Claim is appropriately cautious but remains in English.

**Evidence Use precision**

- EU A/B/C all point to the WHO overview and use the same generic description, without identifying the WHO overview paragraphs or specific determinants.
- The EPA Source and EU D directly support Claim D, but the same EPA material is also a stronger fit for Claim B. The current canonical source chain does not link EPA to B. Do not silently count a source mentioned in this audit as an existing canonical dependency.
- EU D's description is better than the generic WHO EUs, but still should identify the exact EPA “Environmental Public Health Paradigm” and the source → media → receptor/contact → dose → possible effect sequence.
- WHO's page gives a broad and current overview, but it does not supply a single quantitative risk estimate applicable to every location or population. Avoid implying that all listed environmental factors have equal risk or that a generic global statement establishes local exposure.

**Context/Scope and health-risk boundary**

- Context and Scope both target Claim A only. Claims B–D have no formal per-Claim boundary.
- Claim B requires explicit distinctions among hazard, exposure, dose, vulnerability and risk; presence of a contaminant does not by itself establish an individual's exposure or disease.
- Claim D already includes a useful multifactorial caveat. Preserve it during translation and do not turn the pathway into a deterministic sequence in which every exposure necessarily produces illness.
- Claim C is a systems-level statement, not a claim that every transport, energy, agricultural or urban activity has the same health effect. Actual effects depend on pollutant, route, dose, population, geography and time.
- Claim D remains English and needs controlled Russian translation before inclusion in a Russian-first edition.

**Decision: HOLD — all four Claims and dependency closures.** WHO directly supports A/C; EPA directly supports B/D, but the current EUs only attach EPA to D. Required: accurate Claim-specific EU locators, an authorized EPA dependency for B, controlled translation of D, and explicit Context/Scope boundaries for B–D. No public INCLUDE is granted.

#### 3. Cross-slice dependency implications

- **Environmental health → public health:** WHO explicitly describes environmental determinants and the need for cross-sectoral action. The public-health slice should not duplicate detailed environmental risk assessment; it should reference environmental health as one domain contributing to population health and prevention.
- **Environmental health → water/sanitation, air quality, food safety, heat/climate and occupational health:** these are distinct exposure or determinant domains. A broad environmental-health Claim must not be treated as direct evidence for the technical thresholds, local advisories or operational controls in those slices.
- **Public health → epidemiology/surveillance:** surveillance and population-level analysis are public-health functions, but the public-health overview does not itself validate epidemiological methods, denominators, causal inference or outbreak thresholds. Keep those as separate Claims with their own sources.
- **Clinical boundary:** population-level determinants, exposure pathways and public-health frameworks do not diagnose an individual, estimate an individual's dose without data, or prescribe treatment.

No new Relation record is justified by this audit alone. The cross-slice links are conceptual dependencies; they should be represented only if the Relation standard's typed semantics and source/version references are satisfied, not by adding an artificial generic relation.

#### 4. Reused audit boundaries

- The P6 public-health substantive/evidence audit and exact historical checkpoint are reused for previously closed findings; this pass does not claim a new P6 checkpoint.
- P9/P13 environmental-health prior findings are reused; this pass adds current source-to-EU mapping and the explicit observation that EPA directly supports Claim B but is not linked to it.
- Existing historical evaluations remain historical evidence. No new Claim evaluation or publication authorization is created by this documentation pass.

### 45. Antimicrobial resistance and biostatistics — current source-chain and medical interpretation audit (2026-11-19)

This focused pass inspected 20 canonical records across `antimicrobial-resistance-basics` (11 records) and `biostatistics-basics` (9 records) at PR #22 HEAD `a974b4af95ed4167b2b8ca58cb844ca119dd81cb`. WHO, CDC, NCBI MeSH and NCBI Bookshelf source pages were checked. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. antimicrobial-resistance-basics — HOLD

**Claim support**

- **A:** “Антимикробная устойчивость возникает, когда микроорганизмы перестают отвечать на соответствующие антимикробные препараты.” WHO's current fact sheet (16 July 2026) directly defines AMR as bacteria, viruses, fungi and parasites not responding to antimicrobial medicines. CDC's current “About Antimicrobial Resistance” page (updated 25 October 2026) directly explains that germs develop the ability to defeat the drugs designed to kill them. Both support the basic definition.
- **B:** “Антимикробные препараты включают антибактериальные, противовирусные, противогрибковые и противопаразитарные средства.” WHO explicitly lists antibiotics/antibacterials, antivirals, antifungals and antiparasitics. This is a direct match.
- **C:** “Устойчивость затрагивает людей, животных, растения, пищевые системы и окружающую среду и поэтому требует межсекторного подхода.” WHO explicitly says AMR requires coordinated action across human, animal, plant and environmental sectors through a One Health approach. The broad cross-sectoral direction is directly supported; “food systems” is not an independent sector in that exact WHO sentence and should be understood as an application context, not silently substituted for the stated One Health sectors.

**Source identity and Evidence Use**

- Current WHO Source `SRC-ANTIMICROBIAL_RESISTANCE_BASICS@1` points to the WHO AMR fact sheet. The live page now shows a 16 July 2026 update. If the Source record is intended to identify a frozen edition, its metadata must record the accessed/revision date through the repository's approved versioning model; do not overwrite @1 to make it appear newly issued.
- Current CDC Source `SRC-CDC-AMR-BASICS-2025@1` points to the CDC “About Antimicrobial Resistance” page. Its live content now carries an October 2026 update and new U.S.-specific burden figures. Those changing statistics must not be imported into a timeless foundational Claim without date, geography and metric context.
- The three WHO EUs A/B/C use the same generic description. They do not identify the exact definition, antimicrobial classes or One Health passage. EU A's CDC corroboration identifies the microbe-versus-human-body distinction, but it targets Claim A only. This is a useful safety boundary and should remain attached to the definition.
- WHO's current page supports A/B/C; CDC's page supports A and provides a useful patient-facing distinction. Do not count CDC's A-only EU as independent canonical evidence for B/C.

**Medical and public-health boundary**

- Context and Scope both target Claim A only. Claims B and C have no formal record-level Context/Scope target.
- The most important misconception boundary is explicit: antimicrobial resistance is a property of microorganisms; it does not mean a person's body becomes resistant to antibiotics or antifungals. CDC states this directly.
- The slice is descriptive. It must not imply that a particular person has a resistant infection, identify an effective medicine for a patient, or recommend starting/stopping/changing antimicrobials. Treatment depends on infection site, organism, susceptibility testing, patient factors and clinician/veterinarian judgment.
- Keep the One Health boundary: AMR involves human, animal, plant and environmental sectors. A general statement does not itself establish a local prevalence, exposure route, transmission event or jurisdictional treatment protocol.

**Decision: HOLD — all three Claims and dependency closures.** The substantive Claims are well supported by WHO; CDC provides valuable independent corroboration for A and the critical host-versus-microbe boundary. The blockers are generic EU descriptions, missing formal Context/Scope for B/C, and source-version date control for pages updated in 2026. The M2 historical closure is retained; this pass does not repeat its full substantive audit.

#### 2. biostatistics-basics — HOLD; current source does not support the Claim set

**Current canonical claims**

- **A:** “Biostatistics applies statistical methods to questions involving biological, medical, and public-health data.”
- **B:** “Biostatistical analysis can describe populations, quantify uncertainty, compare groups, and evaluate associations or effects under stated assumptions.”
- **C:** “Interpretation of statistical results depends on study design, measurement quality, sampling, model assumptions, and the population to which the analysis applies.”

All three Claims are English in a Russian-first Part I edition.

**Current source and exact support**

- The only Source is “NCBI MeSH — Biostatistics”, currently pointing to the MeSH search URL `https://www.ncbi.nlm.nih.gov/mesh/?term=Biostatistics`.
- The specific MeSH record “Biostatistics” defines the term as application of statistics to biological systems and organisms, involving retrieval/collection, analysis, reduction and interpretation of qualitative and quantitative data. Direct record: `https://www.ncbi.nlm.nih.gov/mesh/68056808`.
- This definition supports Claim A at a high level. It does not establish the full method list and inferential scope in Claim B, nor the study-design, measurement, sampling, assumptions and target-population limitations in Claim C.
- All three EUs use the generic description “Источник используется в пределах заявленного материала.” No exact MeSH descriptor or subheading is identified. MeSH is a controlled-vocabulary/indexing resource, not a comprehensive teaching text for all methods asserted in B/C.

**Candidate additional sources — not yet canonical**

1. **NCBI Bookshelf, “Understanding Biostatistics Interpretation” (StatPearls; last updated 15 February 2026).** `https://www.ncbi.nlm.nih.gov/books/NBK431056/`
   - Directly discusses selection of statistical methods based on study design, variable types, distributional assumptions and research question; confidence intervals, effect sizes, power, Type I/II error, bias, confounding, generalizability and the fact that statistical association does not establish causation.
   - The article is distributed under CC BY-NC-ND 4.0. That license permits redistribution with attribution but does not permit altered/derivative versions or commercial use. Do not assume it is an unrestricted source for reproducing or adapting text in a commercial edition or AI workflow. A bibliographic citation and independently authored factual paraphrase are not blanket permission to reproduce the article.
   - It is a clinical interpretation resource, not a universal introduction to all biostatistics; use only for the methods and medical interpretation it actually covers.

2. **CDC Field Epidemiology Manual, “Analyzing and Interpreting Data”.** `https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html`
   - Directly explains confidence intervals for measures of association, the uncertainty/precision of point estimates, and interpretation of population-sample estimates. This can support a carefully bounded portion of Claim B.
   - It is field epidemiology guidance, not a general source for every biostatistical method.

3. **NCBI Bookshelf, “Reference Guide on Statistics and Research Methods”.** `https://www.ncbi.nlm.nih.gov/books/NBK621595/`
   - The accessible search extract discusses study design, population/sample, representative sampling, sampling error, bias, standard errors and confidence intervals. It is a candidate for Claim C and parts of B, but the exact publisher/edition and reuse terms must be confirmed before adding it to canonical records.

**Evidence Use / Context / Scope**

- The current three EUs link the same MeSH Source. Their descriptions are generic and do not map the claims to the descriptor's actual scope.
- Context and Scope target Claim A only. Claims B/C require explicit boundaries: inferential results depend on design, sampling, measurement, missingness, assumptions, multiplicity and target population; statistical significance is not equivalent to effect size, practical importance or causality.
- Statistical analysis does not repair a biased sample, invalid measurement, confounding or a poorly designed study. Increasing sample size may reduce random error but does not eliminate systematic bias.
- The slice should remain educational. It must not be treated as a substitute for a qualified biostatistician, statistical analysis plan, clinical-trial protocol or domain-specific review.

**Decision: HOLD — all three Claims and dependency closures.** The MeSH Source is a valid definitional locator for Claim A, but it is not a sufficient sole source for B/C. Required: controlled Russian translation; additional method-specific Sources; Claim-specific EUs with exact section locators; and explicit Context/Scope coverage for B/C. Keep the MeSH Source as a terminology source if editorially approved, rather than stretching it to cover methods it does not describe.

#### 3. Cross-slice implications

- **AMR ↔ microbiology:** microbiology explains organisms and their properties; AMR describes the response of microorganisms to antimicrobial medicines. Neither should be used as a shortcut for pathogen-specific diagnosis, susceptibility interpretation or laboratory procedures.
- **AMR ↔ public/environmental health:** WHO's One Health framing links human, animal, plant and environmental sectors. Environmental pathways and surveillance require their own evidence and local scope.
- **Biostatistics ↔ epidemiology/public health:** statistical uncertainty, sampling, study design and interpretation underpin epidemiological claims. A descriptive surveillance count is not automatically a population rate, a causal estimate or a treatment effect.
- No new Relation record is justified solely by these conceptual overlaps. Any Relation must use the repository's typed semantics and exact version references; do not manufacture a generic link to simulate evidence coverage.

### 46. Cell basics and cell biology — duplicate-scope and placeholder-Claim audit (2026-11-19)

This pass inspected 18 canonical JSON records across `cell-basics` and `cell-biology-basics` at PR #22 HEAD `360384a35dc05d3f2f5f4ce024fcc6b922202cae`. Current OpenStax Biology 2e sections were checked against the exact Claim wording. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. cell-basics — substantive Claims, but source precision HOLD

**Current Claims**

- **A:** “Клетка является основной структурной и функциональной единицей живых организмов.”
- **B:** “Прокариотические клетки не имеют мембранного ядра, тогда как эукариотические клетки имеют ядро.”
- **C:** “Клеточные структуры выполняют различные функции внутри клетки.”

All three are substantive, introductory and in Russian.

**Direct OpenStax Biology 2e locators**

- **A:** §4.1 “Studying Cells” directly says a cell is the smallest unit of a living thing and the basic building block of organisms. `https://openstax.org/books/biology-2e/pages/4-1-studying-cells`.
- **B:** §4.2 “Prokaryotic Cells” says prokaryotes do not have a nucleus and distinguishes Bacteria/Archaea from eukaryotes; §4.3 “Eukaryotic Cells” directly says eukaryotic cells have a membrane-bound nucleus. `https://openstax.org/books/biology-2e/pages/4-2-prokaryotic-cells`; `https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells`.
- **C:** §4.3 directly describes specialized functions of the plasma membrane, ribosomes, mitochondria, chloroplasts, lysosomes, peroxisomes and other organelles. `https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells`.

**Current canonical source-chain issue**

- The sole Source is “OpenStax Biology 2e — cell structure and function” and points only to the broad Chapter 4 Introduction: `https://openstax.org/books/biology-2e/pages/4-introduction`.
- All three EUs point to that same chapter introduction and use the same generic description. The chapter introduction provides orientation but is not the best pinpoint for the specific cell-theory, prokaryotic/eukaryotic and organelle-function Claims.
- The precise sections identified above are candidate locators, not canonical dependencies yet. Do not assume that an audit citation creates a Source/EU link.
- The source chain should distinguish the cell-theory statement (4.1), nuclear distinction (4.2 + 4.3) and organelle functions (4.3).

**Context/Scope**

- Context and Scope both target Claim A only. Claim B has an important taxonomy boundary: prokaryotes are Bacteria and Archaea; eukaryotes include animals, plants, fungi and protists. Avoid equating “prokaryote” with bacteria alone.
- Claim C should not imply that every cell has every organelle. The presence of chloroplasts, cell walls, lysosomes, centrioles and other structures differs among cell types and lineages. The OpenStax section explicitly describes plant/animal differences.
- This is basic cell biology, not a medical diagnostic description of an individual cell sample or a laboratory protocol.

**Decision: HOLD — all three Claims and dependency closures.** Claim substance is acceptable at introductory level, but exact section-level Sources/EUs and formal Context/Scope coverage for B/C remain. The current broad Chapter 4 Introduction is insufficiently precise for the full Claim set.

#### 2. cell-biology-basics — HOLD; all three Claims are meta-placeholders

**Current Claims**

- **A:** “Срез cell-biology-basics вводит базовые понятия и отношения, необходимые для ориентации в предметной области.”
- **B:** “Интерпретация сведений по cell-biology-basics зависит от источника, контекста и границ применимости утверждения.”
- **C:** “Базовое знание по cell-biology-basics не заменяет специализированную проверку, когда вывод зависит от условий, измерений или профессиональной оценки.”

These are descriptions of the slice, evidence rules and generic disclaimers. They do not state cell-biology knowledge. Their classification as `documented_fact` is semantically inappropriate.

- The only Source is “OpenStax Biology 2e — Cell Structure” and points to the Chapter 4 Introduction. The three EUs use generic descriptions and merely link the Source to the meta-Claims.
- Context and Scope target Claim A only. They do not repair the absence of domain knowledge.
- No new domain-specific content is established by the current record set. Do not copy the three `cell-basics` Claims into this slice without an editorial scope decision; that would create a duplicate slice rather than solve the gap.

**Required editorial choice before a new version is authorized**

Choose one coherent path:

1. **Merge/retire as a duplicate scope:** if `cell-biology-basics` was intended to be an alias or broad duplicate of `cell-basics`, preserve its historical @1 records and use an approved deprecation/redirect mechanism, with exact references to the canonical `cell-basics` slice.
2. **Define a genuinely distinct cell-biology scope:** for example, cell theory and evolution of cell concepts; membrane structure and transport; cellular metabolism and energy conversion; cell signalling; cell cycle and division; gene expression and protein synthesis. Select a bounded subset and write substantive Claims that do not duplicate the current `cell-basics` set.

The second path would require distinct, direct Sources and claim-specific Evidence Use; a general Chapter 4 landing page is not enough. Avoid expanding into operational wet-lab instructions, genetic manipulation or pathogen handling without separate safety and rights review.

**Decision: HOLD — all three Claims and dependency closures.** Rebuild or formally retire this slice through a versioned editorial decision. Do not merely relabel the existing statements or change their source links.

#### 3. Cross-slice architecture

- `cell-basics` is the natural foundational dependency for `cell-biology-basics`, anatomy, physiology and microbiology.
- Anatomy describes higher organization (cells → tissues → organs → organ systems); cell basics describes the cell-level building blocks and their structures.
- Microbiology requires a broader scope than human cell biology: bacterial and archaeal prokaryotes, microbial eukaryotes and viruses must not be collapsed into one cellular model. Viruses are acellular and should not be described as cells.
- A typed Relation may be useful if the existing Relation vocabulary supports prerequisite/part-of/overlap/dependency semantics. No Relation is added here: conceptual overlap alone is not enough, and no artificial edge should be created to compensate for weak Evidence Use.

No public INCLUDE is granted. No canonical JSON was modified.


### 47. Immunology, microbiology and epidemiology — exact-record dependency audit (2026-11-19)

This pass inspected the current canonical record chains for three connected slices at PR #22 HEAD `fe7f5b36ff7c20435363698c4e395c89a0a49759`: `immunology-basics` (9 record files), `microbiology-basics` (9 record files), and `epidemiology-basics` (12 record files). The existing `public-health-surveillance-basics` P6 closure is retained and not re-run. Current source pages were checked against the exact Claim wording. No canonical JSON, README, Relation, Assessment or other content record was changed.

#### 1. immunology-basics — HOLD; all three Claims are meta-placeholders

**Current Claims**

- **A:** “Срез immunology-basics описывает базовые понятия предметной области и их взаимосвязи.”
- **B:** “Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.”
- **C:** “Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.”

These statements describe the slice, evidence rules and a generic disclaimer. They do not state immunological knowledge. Their classification as `documented_fact` is semantically inappropriate. Replacing the Source locator alone cannot repair the absence of substantive Claims.

**Current Source and locator defect**

- `SRC-IMMUNOLOGY_BASICS@1` identifies “OpenStax Microbiology — Innate and Adaptive Immunity” but points to `https://openstax.org/books/microbiology/pages/18-1-how-pathogens-cause-disease`.
- The exact OpenStax section for adaptive immunity is Chapter 18, §18.1 “Overview of Specific Adaptive Immunity”: `https://openstax.org/books/microbiology/pages/18-1-overview-of-specific-adaptive-immunity`.
- The innate-immunity foundation is Chapter 17, especially the introduction and sections 17.1–17.5: `https://openstax.org/books/microbiology/pages/17-introduction`.
- OpenStax §18.1 directly describes specificity and memory and distinguishes humoral (B-cell/antibody) from cellular (T-cell) immunity. Chapter 17 describes innate defenses as a distinct, rapid, nonspecific set of defenses. These are separate, directly locatable concepts; they must not be collapsed into one broad “immune system” statement.

**Evidence Use and boundaries**

- All three EUs use generic descriptions. Context and Scope both target Claim A only.
- The existing EU chain mechanically links the Source to meta-Claims; it does not create evidence for innate/adaptive immunity, immune memory, antibodies, lymphocytes or immune response.
- A future substantive slice must distinguish innate from adaptive immunity; humoral from cellular adaptive responses; and immune protection from immunopathology. Do not imply that every exposure produces protective immunity, that immune response is always beneficial, or that a general mechanism predicts an individual's clinical response.
- Keep the educational boundary: no diagnosis of immune deficiency, allergy, autoimmune disease or infection; no individual vaccine/treatment advice; no laboratory or immunomodulatory protocol.

**Decision: HOLD — all three Claims and dependency closures.** Rebuild with substantive, bounded Claims and exact section-level Sources/EUs. Preserve the historical @1 records; do not silently rewrite or reclassify them.

#### 2. microbiology-basics — HOLD; substantive Claims, but incomplete support and boundaries

**Current Claims**

- **A:** “Микроорганизмы — это организмы, большинство которых слишком малы для наблюдения без микроскопа.”
- **B:** “Микроорганизмы широко распространены и выполняют важные экологические функции.”
- **C:** “Микроорганизмы могут быть полезными, нейтральными или патогенными для человека в зависимости от конкретного организма и контекста.”

**Direct source mapping**

- The current Source is OpenStax Microbiology, Chapter 1 Introduction: `https://openstax.org/books/microbiology/pages/1-introduction`. The introduction directly says microorganisms are small and most cannot be seen without a microscope; it also says they occur almost everywhere, many are harmless/helpful, and some cause disease.
- §1.3 “Types of Microorganisms” is a better direct locator for the range of microbial groups, including Bacteria, Archaea, microbial Eukarya and acellular viruses: `https://openstax.org/books/microbiology/pages/1-3-types-of-microorganisms`.
- The Chapter 1 summary reinforces the domain distinctions and states that viruses are acellular: `https://openstax.org/books/microbiology/pages/1-summary`.
- **A:** directly supported by Chapter 1 Introduction.
- **B:** broadly supported by the Introduction, which states that microbes are widespread and play fundamental roles in ecosystems/food webs. A future EU should identify this passage, not simply point to the chapter landing page.
- **C:** the source supports helpful/harmless microbes and disease-causing microbes. It does not establish “neutral” as a distinct, exhaustive or stable category. “Neutral” is context-dependent and should not be presented as a source-defined third class without a specific definition and evidence.

**Evidence Use and boundaries**

- All three EUs use the same generic description and the same broad Chapter 1 Introduction locator. They do not identify the exact supporting passages or distinguish taxonomy from ecological function and host effects.
- Context and Scope both target Claim A only. Claims B/C lack formal claim-specific Context/Scope.
- Taxonomic boundary: Bacteria and Archaea are distinct prokaryotic domains; microbial eukaryotes include fungi and protozoa; viruses are acellular and are not cells or cellular organisms. Do not imply that all microbes are prokaryotes or that all microorganisms are infectious.
- Host-effect boundary: pathogenicity depends on the organism, host, route, dose and context. “Helpful/harmless/pathogenic” is not a universal immutable classification for every interaction.
- Keep descriptive microbiology separate from clinical microbiology, diagnosis, pathogen identification, susceptibility testing, culturing, genetic manipulation and pathogen-handling protocols.

**Decision: HOLD — all three Claims and dependency closures.** A/B have direct support candidates, but the EU locators are not sufficiently precise; C overstates the source by adding “neutral”; and formal Context/Scope coverage is incomplete. No public INCLUDE is granted.

#### 3. epidemiology-basics — HOLD; three placeholders and one source-mismatched English Claim

**Current Claims**

- **A:** “Срез epidemiology-basics описывает базовые понятия предметной области и их взаимосвязи.”
- **B:** “Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.”
- **C:** “Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.”
- **D:** “WHO describes epidemiology as the study of the distribution and determinants of health and disease in populations and its application to prevention and control.”

A–C are slice descriptions and generic evidence disclaimers, not epidemiology Claims. D is substantive but English, and its current attribution needs correction.

**Source-chain findings**

- `SRC-EPIDEMIOLOGY_BASICS@1` points to CDC “Principles of Epidemiology”: `https://www.cdc.gov/training-publichealth101/php/lessons/principles-of-epidemiology.html`.
- `SRC-WHO-EPIDEMIOLOGY-2024@1` points to WHO “Putting participatory surveillance into practice” (2024). That page concerns participatory surveillance; it is not the best direct support for the broad textbook definition stated in Claim D. The current WHO EU description is generic and does not supply a pinpoint passage.
- CDC's official archived Lesson 1, Section 1 gives the standard definition: distribution and determinants of health-related states/events in specified populations and application to control health problems. It also explains frequency, population denominators, time/place/person, and the distinction between population-level epidemiology and individual clinical care: `https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html`.
- CDC's current Introduction to Epidemiology course (10 January 2025) is a useful modern teaching locator for core terms, data sources, study design and time/place/person: `https://www.cdc.gov/training-publichealth101/php/training/introduction-to-epidemiology.html`.
- WHO's *Basic Epidemiology*, 2nd edition, is an appropriate broader teaching reference, but any proposed locator and reuse rights must be checked at the relevant chapter/page level: `https://www.who.int/publications/b/31231`.
- The current Claim D is close to the standard epidemiological definition, but “WHO describes” is not established by the currently linked WHO participatory-surveillance article. A CDC source candidate is more directly matched to the wording. Do not silently substitute the attribution or count the candidate as an existing canonical dependency.

**Evidence Use and boundaries**

- EUs A–C point to the CDC Source but describe evidence for meta-Claims; they do not establish epidemiological knowledge. EU D points to the WHO participatory-surveillance Source but gives only a generic summary.
- Context and Scope target Claim A only. The substantive D has no formal claim-specific Context/Scope.
- A rebuilt slice should distinguish descriptive epidemiology (frequency/pattern by time, place and person) from analytic epidemiology (determinants, risk factors and causal hypotheses); distinguish counts from rates and identify the population denominator; and separate population-level inference from individual diagnosis or treatment.
- Association is not automatically causation. Surveillance signals, case definitions, study design, ascertainment, missingness and changing denominators affect interpretation. Local outbreak thresholds and public-health orders require current jurisdictional authorities, not generic textbook Claims.
- Claim D needs controlled Russian translation before inclusion in a Russian-first edition.

**Decision: HOLD — all four Claims and dependency closures.** Rebuild A–C as substantive epidemiology knowledge or retire them through an approved versioned editorial process; re-source and translate D with an exact locator; add claim-specific Context/Scope and EUs. The historical P6 substantive audit and exact-head technical checkpoint remain historical records, not evidence that the current placeholder text is valid.

#### 4. Public-health surveillance, infection prevention and biosafety — dependency boundary only; no repeat of closed audit

- The existing `public-health-surveillance-basics` slice is marked as matured P6, has four substantive Claims, and has a dedicated regression test. Its prior substantive closure is retained; this section does not repeat P6 or claim a new surveillance adjudication.
- Current surveillance documentation correctly requires time, population, geography and methodology where relevant, and prohibits converting a surveillance signal into an individual diagnosis or live public-health directive. CDC's current “Introduction to Public Health Surveillance” (10 January 2025) describes system types, data sources, uses and the surveillance process: `https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health-surveillance.html`.
- The conceptual chain is microbiology (organisms and their properties) → immunology (host defenses) → infectious disease/clinical assessment (individual disease) → epidemiology (population distribution/determinants) → surveillance (systematic population data and public-health action). These are related but non-interchangeable scopes.
- WHO's IPC programme and core components provide authoritative health-care infection-prevention context: `https://www.who.int/teams/integrated-health-services/infection-prevention-control` and `https://www.who.int/teams/integrated-health-services/infection-prevention-control/core-components`. CDC Standard Precautions are explicitly for patient care and use risk assessment, hand hygiene, PPE when exposure is expected, respiratory hygiene, safe equipment handling and environmental cleaning: `https://www.cdc.gov/infection-control/hcp/basics/standard-precautions.html`.
- These health-care IPC sources must not be generalized into a universal home/community biosafety protocol. Facility-level IPC, community infection prevention, laboratory biosafety and biosecurity are distinct domains with different settings, controls and competent authorities. No dedicated infectious-disease or biosafety Claim set is established by the three slices audited above; absence of a dedicated slice is a coverage gap, not permission to invent Claims or relations.
- Existing emergency hand-hygiene, emergency-waste/sanitation and public-health surveillance material may be used as dependency candidates only after exact Claim/EU/Source and setting checks. Do not re-open their closed audits merely because a conceptual link exists.

#### 5. Cross-slice dependency conclusions

- **Cell basics → microbiology:** the distinction between cellular organisms and acellular viruses is foundational. Viruses must not be described as cells.
- **Microbiology → AMR:** organism classification and microbial biology support the conceptual foundation for AMR, but do not establish local resistance prevalence, susceptibility results or treatment choice.
- **Immunology ↔ infectious disease:** host defenses and pathogen properties are complementary explanations; neither alone establishes an individual diagnosis, prognosis or treatment.
- **Epidemiology ↔ surveillance:** surveillance supplies systematic data for population-level analysis; raw counts are not automatically comparable rates, causal effects or representative estimates.
- **Public/environmental health ↔ One Health/AMR:** human, animal, plant and environmental sectors are connected, but each pathway and local exposure claim needs its own evidence.
- No Relation record is added. A conceptual dependency is not itself a typed, versioned Relation, and no generic edge may be used to simulate evidence coverage.

**Overall decision: HOLD for immunology, microbiology and epidemiology.** Preserve historical versions and closed surveillance/P6 work. No canonical JSON, Assessment, Relation or publication status was changed. No public INCLUDE is granted by this audit.


### 48. Virology, parasitology, vaccination, IPC and biosafety dependency audit (2026-11-19)

This pass inspected current canonical chains at PR #22 HEAD `bf2923687ea4af7a3f938632b2cbc925267e7326`: `virology-basics` (9 records), `parasitology-basics` (9 records), `vaccination-information-basics` (9 records), and the already matured `public-health-basics` (12 records) as a boundary/dependency check. It also checked the existing `emergency-hand-hygiene` and `emergency-waste-sanitation` chains against their prior P3/P6 findings and current WHO/CDC guidance. No canonical JSON, README, Relation, Assessment or publication status was changed.

#### 1. virology-basics — HOLD; Claims are substantive, Evidence Use is not pinpointed

**Current Claims**
- **A:** Viruses do not have all the characteristics of cellular organisms and depend on host cells for replication.
- **B:** Viral particles contain genetic material and protein structures that support their life cycle.
- **C:** Different viruses vary in genomes, structures and mechanisms of interaction with hosts.

**Source fit**
- `SRC-VIROLOGY_BASICS@1` points to OpenStax Biology 2e §21.1, “Viral Evolution, Morphology, and Classification”: `https://openstax.org/books/biology-2e/pages/21-1-viral-evolution-morphology-and-classification`.
- This is a directly relevant section. It explicitly describes viruses as noncellular, describes nucleic-acid genomes and protein capsids (with or without envelopes), and compares genome types, capsid morphologies, host attachment and Baltimore classification.
- Claim A is supported by the section's “Viral Morphology” discussion and the Chapter 21 introduction; Claim B by the description of nucleic-acid core/capsid/envelope; Claim C by the variation in host range, morphology, genome and replication/classification.
- The source is materially better matched than a generic microbiology chapter introduction. No need to replace the source solely because it is one section.

**Remaining defects**
- All three EUs use the same generic “source is used without going beyond material” description. They do not name the specific passages (noncellular/host dependence; genome/capsid/envelope; genome and morphology diversity/classification).
- Context and Scope both target Claim A only. Claims B/C lack formal claim-specific boundaries.
- Claim A's “не имеют всех признаков клеточных организмов” is imprecise: viruses are acellular/noncellular, not incomplete cells. Consider a versioned editorial correction to say “Вирусы — неклеточные биологические агенты; для репликации они используют клетку-хозяина.” This is a proposal only; canonical text remains untouched.
- Do not imply that all viruses infect humans, that morphology alone predicts disease/severity, or that all viruses have lipid envelopes. Viral genomes may be DNA or RNA; not all share the same structure or host range.
- Keep this as descriptive educational virology. Do not expand it into virus propagation, isolation, culture, engineering, host-range alteration or experimental procedures.

**Decision: HOLD — Claims A–C and dependency closure.** The underlying source is relevant and supports the subject matter, but exact EU passage mapping, per-Claim Context/Scope coverage and a precise definition for Claim A are still required. No public INCLUDE.

#### 2. parasitology-basics — HOLD; the current source is too narrow for the three general Claims

**Current Claims**
- **A:** Parasitism is a biological interaction in which a parasite obtains resources from a host.
- **B:** Parasitic organisms have diverse life cycles and transmission strategies.
- **C:** Describing a parasite requires distinguishing host, life-cycle stage and transmission route.

**Source fit**
- `SRC-PARASITOLOGY_BASICS@1` points to OpenStax Biology 2e §28.6 “Flatworms”: `https://openstax.org/books/biology-2e/pages/28-6-flatworms`.
- Flatworms are one taxonomic group, not a general reference for all parasites or parasitism. A single flatworm chapter cannot by itself establish the full breadth of Claims B/C or the broad definition in A.
- A more suitable general introductory source candidate is CDC “About Parasites” (14 November 2024): `https://www.cdc.gov/parasites/about/index.html`. It defines parasites as organisms living on or in a host and obtaining food from or at the host's expense; it distinguishes protozoa, helminths and ectoparasites, and describes differing transmission routes.
- CDC's “What Causes Parasitic Diseases” is a further source candidate for animals, food, insects and water as transmission pathways: `https://www.cdc.gov/parasites/causes/index.html`.
- These are source candidates for a future version, not current canonical dependencies. The current Source record remains unchanged.

**Evidence Use and boundaries**
- All three EUs repeat generic language and cite only the flatworm page. They do not identify exact passages for host relationship, life-cycle diversity or transmission.
- Context and Scope target Claim A only; B/C have no formal per-Claim applicability boundary.
- Parasitic organisms are diverse. The three CDC groupings (protozoa, helminths, ectoparasites) are a human-disease framing, not an exhaustive taxonomy of every parasitic interaction across biology.
- Transmission depends on the organism and life-cycle stage; examples include fecal–oral routes, food/water, direct contact and arthropod vectors. Do not imply one route applies to all parasites.
- Do not infer diagnosis, treatment, medication, deworming schedule or individual risk from general taxonomy. Keep this slice descriptive and refer clinical questions to qualified health services.

**Decision: HOLD — Claims A–C and dependency closure.** The existing OpenStax source is too narrow for the broad claim set; add direct general sources and pinpoint Evidence Use in a versioned proposal, and add Claim-specific Context/Scope. No canonical change.

#### 3. vaccination-information-basics — substantive Claims; direct WHO source, but generic EU and boundary coverage remain

**Current Claims**
- **A:** Vaccine safety is evaluated before introduction through successive trial phases and assessment of results.
- **B:** After introduction, vaccines remain under safety monitoring by health authorities and specialists.
- **C:** Vaccine safety and effectiveness information must be interpreted in the context of the specific vaccine, population and available data.

**Source fit**
- `SRC-VACCINATION_INFORMATION_BASICS@1` points to WHO “Vaccines and immunization: Vaccine safety”: `https://www.who.int/news-room/questions-and-answers/item/vaccines-and-immunization-vaccine-safety` (WHO page updated 23 September 2025).
- The current WHO page directly describes pre-introduction clinical testing (phases I–III), regulatory assessment, post-introduction safety monitoring, adverse-event reporting and expert causality assessment.
- Claim A is directly supported by the “How are vaccines tested?” and approval sections; B by the “How is vaccine safety monitored?” section; C is supported in part by the vaccine-specific evaluation and monitoring discussion, but its broad “available data” wording needs a precise passage or a narrower formulation.
- The WHO page also makes an important distinction: an adverse event following immunization (AEFI) is a health event after vaccination and does not by itself establish that the vaccine caused it. Causality requires assessment.

**Evidence Use and boundaries**
- All three EUs use the same generic summary; none names the exact WHO section or passage.
- Context and Scope both target Claim A only. Claims B/C need claim-specific context and scope.
- Do not turn population-level safety monitoring into a guarantee of zero risk, a claim that every reported event is caused by a vaccine, or individual medical advice.
- Vaccine-specific indications, contraindications, schedules and individual risk require current national guidance and clinical context. This audit does not evaluate any specific vaccine or recommend an individual vaccination decision.

**Decision: HOLD pending EU precision and formal Claim B/C boundaries.** The current WHO Source is well matched and current; the blocker is the record-level evidence mapping and incomplete boundary coverage, not a demonstrated contradiction in the Claims. No canonical change.

#### 4. public-health-basics and public-health-surveillance-basics — preserve historical P6

- `public-health-basics` README identifies a matured P6 slice with four Claims, four EUs and dedicated regression. Its prior closure is retained; no repeat adjudication is performed here.
- `public-health-surveillance-basics` likewise remains a previously matured P6 slice. Do not reopen its substantive audit merely because it is connected to the infection-prevention chain.
- These slices are population-level public-health foundations. They do not substitute for individual diagnosis, clinical infection management, facility IPC policy or laboratory biosafety.

#### 5. Infection prevention and control — setting distinction and current evidence candidates

The repository already contains `emergency-hand-hygiene` and `emergency-waste-sanitation`. Their earlier P3 substantive/technical closures are preserved; this pass does not rerun those completed audits.

**Emergency hand hygiene**
- Existing Claim `CLM-HANDWASH-20SEC@1` is supported by CDC emergency personal-hygiene guidance and WHO emergency hygiene guidance; the prior register records direct support from both sources.
- Existing EUs remain generic and should identify the exact CDC passage and WHO Technical Note 10 text/figure. The previous HOLD remains an evidence-locator debt, not a new contradiction.
- A newer WHO community-setting source is now available: *Guidelines on hand hygiene in community settings* (15 October 2025), `https://www.who.int/publications/i/item/9789240116559`. It explicitly addresses non-health-care settings (households, public and institutional settings) and reducing diarrhoeal disease and acute respiratory infections. Its recommendations distinguish community settings from settings where health care is routinely delivered.
- This 2025 guideline is a useful candidate for a future version or supplemental Evidence Use, but it does not silently replace the existing emergency-context WHO/CDC evidence or retroactively close the exact-locator debt.

**Emergency waste and sanitation**
- Prior P3 review is already explicit: `emergency-waste-sanitation` remains HOLD for all four Claims and dependency closures, with a narrow reopen of P3-EVIDENCE-002/Claim C and Claim D source fit. The historical P3 exact 3/3 CI checkpoint remains historical evidence only.
- The existing register records that WHO Technical Note 7 explicitly excludes specialist medical/toxic waste from its ordinary emergency solid-waste guidance; Claim C therefore cannot be treated as fully supported by its current WHO EU. Claim D also lacks the required WHO disposal Evidence Use, and the current Scope does not cover Claim C's applicability. These are existing open findings, not newly discovered or closed by this pass.
- Do not generalize household/community sanitation guidance to medical, chemical, toxic, radioactive or other specialist waste. Unknown hazardous materials require competent local authorities/specialist services and applicable law.

**Healthcare IPC**
- CDC Standard Precautions apply to all patient care and are based on risk assessment; elements include hand hygiene, PPE when exposure is expected, respiratory hygiene/cough etiquette, safe handling of equipment and environmental cleaning/disinfection: `https://www.cdc.gov/infection-control/hcp/basics/standard-precautions.html`.
- CDC Core Infection Prevention and Control Practices provide the broader facility-level implementation context: `https://www.cdc.gov/infection-control/hcp/core-practices/`.
- WHO IPC core components provide national and acute health-care facility programme context: `https://www.who.int/teams/integrated-health-services/infection-prevention-control/core-components`.
- These are healthcare IPC sources. They must not be represented as a universal community, household, farm, food-production or laboratory biosafety procedure. Community hand hygiene is separately covered by WHO's 2025 guideline above.

#### 6. Biosafety and biosecurity — substantive coverage gap; define scope before creating Claims

No dedicated `biosafety-basics`, `laboratory-biosafety-basics` or `biosecurity-basics` vertical slice exists in the current vertical-slices inventory. This is a coverage gap, not permission to create generic placeholder Claims or Relations.

**Authoritative source candidates**
- WHO *Laboratory biosafety manual, fourth edition* (21 December 2020): `https://www.who.int/publications/i/item/9789240011311`. It uses a risk- and evidence-based approach and requires risk assessment before laboratory activities; controls are selected in relation to the agent, procedures, equipment, exposure routes, host range, local susceptibility and personnel competence.
- WHO *Laboratory biosafety manual, fourth edition: Risk Assessment* (20 December 2020): `https://www.who.int/publications/i/item/9789240011458`. It defines biological risk through likelihood and consequences and treats the risk assessment as a systematic process informing control selection.
- WHO *Laboratory biosecurity guidance* (21 June 2024): `https://www.who.int/publications/i/item/9789240095113`. This complements LBM4 and addresses preventing lapses/incidents across the value chain for high-consequence biological material, technology and information.
- WHO *A guide for the practical implementation of the WHO Laboratory Biosafety Manual fourth edition* (29 February 2024): `https://www.who.int/publications/i/item/9789290211051`.

**Required scope separation**
1. Community infection prevention: everyday hygiene, respiratory etiquette, safe water/sanitation and risk communication.
2. Healthcare IPC: precautions and facility programmes for patient-care environments.
3. Laboratory biosafety: risk assessment and controls for laboratory activities.
4. Laboratory biosecurity: prevention of loss, theft, misuse, diversion or deliberate release of high-consequence biological material, technology or information.
5. Waste management: routine municipal, emergency, healthcare and hazardous/specialist waste are not interchangeable.

Any new biosafety/biosecurity slice must remain high-level, prevention-focused and governance-oriented. It may describe risk assessment, roles, training, reporting, incident response and competent oversight. It must not provide operational pathogen handling, propagation, culturing, concentration, genetic modification, virulence enhancement, evasion or release instructions. Specific laboratory procedures belong to approved institutional protocols and competent biosafety oversight, not a general survival encyclopedia.

**Decision: coverage gap — do not create canonical records in this pass.** First approve a distinct, bounded scope and identify the intended audience and setting. Build direct Source → substantive Claim → exact Evidence Use → Context/Scope only after that scope is approved.

#### 7. Cross-slice dependencies and final disposition

- **Cell basics → microbiology → virology:** viruses are acellular and depend on host-cell machinery; do not place viruses inside a cellular-organism taxonomy.
- **Microbiology/virology/parasitology → infectious disease:** pathogen class, host range, life-cycle stage and transmission route are distinct explanatory dimensions.
- **Immunology → infection:** host defenses interact with pathogens, but this does not establish diagnosis or treatment.
- **Vaccination → immunology/public health:** immunization is a prevention strategy; vaccine safety monitoring is distinct from disease surveillance and from individual clinical assessment.
- **IPC/community hygiene → public health:** household/community hand hygiene and healthcare IPC share goals but have different settings and recommendations.
- **Biosafety/biosecurity → laboratory governance:** laboratory risk control is a separate domain from community infection prevention and healthcare IPC.
- **AMR:** retain the prior §45 HOLD and its specific findings; this pass uses AMR only as a dependency and does not repeat the adjudication.
- No new Relation record is added. No relation is inferred solely from adjacent subject labels.

**Overall decisions:** virology-basics — HOLD; parasitology-basics — HOLD; vaccination-information-basics — HOLD pending EU/Context/Scope refinement; public-health-basics and public-health-surveillance-basics — historical P6 preserved; emergency-hand-hygiene — prior HOLD preserved, no rerun; emergency-waste-sanitation — prior HOLD and specific open findings preserved; biosafety/biosecurity — coverage gap, scope decision required.

No canonical JSON, README, Relation, Assessment, publication status or historical evaluation was modified. No public INCLUDE is granted by this pass.


### 49. Pathology, plant pathology and ecophysiology — three-slice record-level source-chain audit (2026-11-19)

This pass examines the current canonical Claim/Evidence Use/Source/Context/Scope chains for `pathology-basics`, `plant-pathology-basics` and `ecophysiology-basics`. It is a new focused review of these three slices; it does not repeat the earlier physiology, environmental-health, plant-biology, microbiology, epidemiology or life-support audits. The three slices contain nine Claims in total. The review distinguishes source relevance from record-level evidence precision and from the sufficiency of Context/Scope. No canonical JSON, README, Relation, Assessment or publication status is changed.

#### 1. pathology-basics — HOLD; Claim A has direct definitional support, B/C are broader than the mapped evidence

**Current Claims**
- **A — `CLM_PATHOLOGY_BASICS_A@1`:** Pathology studies the nature and causes of diseases through changes in the structure and function of cells and tissues.
- **B — `CLM_PATHOLOGY_BASICS_B@1`:** Pathological disciplines differ by object and method, including cellular, tissue and clinical-laboratory approaches.
- **C — `CLM_PATHOLOGY_BASICS_C@1`:** Interpretation of a pathological finding depends on the material, method of examination and clinical or research context.

**Source-chain inspection**
- `SRC_PATHOLOGY_BASICS@1` points to NCBI MeSH “Pathology”: `https://ncbi.nlm.nih.gov/mesh/68010336`.
- This source is directly relevant to Claim A. The MeSH scope note defines pathology as a specialty concerned with the nature and cause of disease as expressed through changes in cellular or tissue structure and function caused by the disease process. The exact definition is visible in the source's Pathology entry.
- The source is a controlled-vocabulary definition, not a textbook survey of all pathology subdisciplines, methods or interpretation conditions. It does not establish Claim B's taxonomy of cellular, tissue and clinical-laboratory approaches, nor Claim C's material/method/context proposition.
- The additional source `SRC_NCBI_HISTOLOGY_PATHOLOGY@1` points to NCBI Bookshelf, “Histology: The Lives and Deaths of Cells in Tissues”: `https://www.ncbi.nlm.nih.gov/books/NBK21066/`. The three additional records `EU_P9_PATHOLOGY_BASICS_A/B/C@1` link that source to all three Claims, but each EU only says that an independent source corroborates the claim within an educational/reference scope. The current source identity and generic EU descriptions do not provide an auditable, claim-specific passage locator. A broad histology source cannot be assumed to support clinical laboratory pathology or all diagnostic methods merely because it concerns cells and tissues.
- A more directly matched NCBI MeSH/NLM reference, “Pathology” (updated 25 September 2025), gives the same concise definition: `https://www.ncbi.nlm.nih.gov/sites/books/NBK518792/`. It is useful corroboration for A, not a replacement for evidence needed by B/C.
- For B, a future version would need a source explicitly distinguishing anatomic pathology (cell/tissue examination) from clinical pathology/laboratory medicine (analysis of blood and other body fluids) and identifying the limits of that classification. NCBI Bookshelf's “Overview of Selected Techniques for Diagnosing and Evaluating Patients” is a candidate for a carefully bounded explanation: `https://www.ncbi.nlm.nih.gov/books/NBK593686/`. It describes anatomic and clinical pathology and their diagnostic roles, but the exact passages must be mapped before use.
- For C, NCBI Bookshelf “Histology, Staining” explains that specimen preparation, staining, microscopy, the investigational question and clinical history matter to interpretation: `https://www.ncbi.nlm.nih.gov/books/NBK557663/`. This is a candidate for a narrowed histopathology-specific claim, not proof that every pathological finding has the same dependencies.

**Evidence Use and boundary defects**
- The three primary EUs `EU_PATHOLOGY_BASICS_A/B/C@1` simply repeat the target Claim and assert that relevant source material supports it. They provide no section, heading, definition text, page or other pinpoint locator.
- The three additional P9 EUs also lack pinpoint locators and do not specify what distinct evidence the NCBI Bookshelf source contributes. They must not be counted as independent corroboration without inspecting the source and recording exact support.
- Both `CTX_PATHOLOGY_BASICS@1` and `SCP_PATHOLOGY_BASICS@1` target Claim A only. Claims B/C have no formal per-Claim Context and Scope.
- Claim B combines different classification dimensions: object of study (cell/tissue) and service/discipline (clinical laboratory). It should not present these as a complete or mutually exclusive taxonomy. Consider a versioned, evidence-backed reformulation separating anatomic pathology from clinical pathology/laboratory medicine.
- Claim C is a plausible interpretive boundary, but currently too general. It should be narrowed to a named type of finding (for example, histological tissue findings) and state which material, preparation/staining method and clinical context affect interpretation.
- This is descriptive educational content, not diagnostic guidance. No Claim or source in this slice authorizes self-diagnosis, interpretation of an individual's biopsy/laboratory report, or treatment decisions. Individual findings require qualified professional interpretation in context.

**Decision: HOLD — all three Claims for first-edition inclusion.** Claim A has a strong direct definition in MeSH, but its EU still needs a precise locator. Claims B/C need better-matched sources, narrower wording and claim-specific Context/Scope. The P9 EUs are preserved as historical records; their presence is not treated as proof of independent evidentiary closure.

#### 2. plant-pathology-basics — HOLD pending pinpoint Evidence Use and claim-specific boundaries; source is substantively well matched

**Current Claims**
- **A — `CLM-PLANT_PATHOLOGY_BASICS-A@1`:** Phytopathology studies plant diseases and disorders.
- **B — `CLM-PLANT_PATHOLOGY_BASICS-B@1`:** Causes of plant diseases may include living pathogens and non-living environmental factors.
- **C — `CLM-PLANT_PATHOLOGY_BASICS-C@1`:** Phytopathology integrates knowledge from botany, microbiology, ecology, genetics, biochemistry and physiology.

**Source-chain inspection**
- `SRC-PLANT_PATHOLOGY_BASICS@1` points to the American Phytopathological Society (APS), “What Is Phytopathology?”: `https://www.apsnet.org/careers/Pages/WhatisPhytopathology.aspx`.
- The source is live and directly relevant. Its “The Study of Plant Disease” section identifies plant pathology as an interdisciplinary science including botany, microbiology, crop science, soil science, ecology, genetics, biochemistry, molecular biology and physiology. This directly supports Claim A's field definition and Claim C's interdisciplinary character.
- The source's “Understanding and Managing Plant Diseases” section states that plant diseases may be caused by living organisms (including fungi, bacteria, viruses, nematodes, phytoplasmas, protozoa and parasitic plants) and nonliving agents (including air pollutants, nutrient imbalances and environmental factors). This directly supports Claim B.
- The APS page therefore has adequate substantive breadth for all three Claims at the level of introductory definitions. The problem is not an obvious source mismatch; it is that the current EUs do not identify the exact passages used.
- An independent educational source from the Canadian Phytopathological Society gives a useful cross-check: `https://phytopath.ca/education/what-is-plant-pathology/`. Its “What is Plant Pathology?” section explicitly distinguishes biotic causes (fungi, bacteria, viruses and nematodes) from abiotic causes (winter damage, drought stress), and describes the field's links to botany, mycology, microbiology, genetics, chemistry, horticulture, agronomy and soil science. This is a candidate corroborating source, not a canonical dependency.
- APS's “Overview of Plant Defenses” also distinguishes living agents from abiotic factors such as nutrient deficiency, drought, lack of oxygen, temperature extremes, ultraviolet radiation and pollution: `https://www.apsnet.org/edcenter/Pages/OverviewOfPlantDiseases.aspx`. It can support a more detailed future treatment of biotic/abiotic disease distinctions, but is not needed to establish the broad introductory claims.

**Evidence Use and boundary defects**
- `EU-PLANT_PATHOLOGY_BASICS-A/B/C@1` all point to the correct APS Source but repeat the same generic description. None identifies the exact source section or text for its Claim.
- `CTX-PLANT_PATHOLOGY_BASICS@1` and `SCP-PLANT_PATHOLOGY_BASICS@1` both target Claim A only. Claims B/C have no formal claim-specific Context/Scope.
- Claim B's distinction should remain broad and educational. It must not imply that every abiotic stress is a disease in every classification system, or that all plant disorders are infectious. Mechanical injury, nutrient imbalance, drought and other abiotic stresses are not automatically transmissible plant infections.
- Claim C's list is illustrative, not exhaustive. The APS source includes additional fields such as crop science, soil science and molecular biology; the Claim should either say “включает, в частности” or keep its list explicitly non-exhaustive. The word “объединяет” should not imply that every phytopathological investigation uses every listed discipline.
- The current material supports an introductory science description, not operational diagnosis, pesticide selection, pathogen culture, inoculation or field-release procedures. Disease management recommendations require crop-, pathogen-, jurisdiction- and product-specific evidence and applicable safety/regulatory controls.

**Decision: HOLD pending record-level completion.** The APS Source is directly matched to all three Claims, and no substantive contradiction was found. However, the three EUs need exact section-level locators, and Context/Scope must be extended to Claims B/C. A versioned clarification that Claim C's discipline list is illustrative/non-exhaustive is recommended. No canonical changes are made.

#### 3. ecophysiology-basics — HOLD; the linked source is materially mismatched to the slice and Claims

**Current Claims**
- **A — `CLM-ECOPHYSIOLOGY_BASICS-A@1`:** Physiological processes of an organism depend on external conditions.
- **B — `CLM-ECOPHYSIOLOGY_BASICS-B@1`:** Organisms have ranges of conditions in which their physiological functions are maintained.
- **C — `CLM-ECOPHYSIOLOGY_BASICS-C@1`:** Comparing physiological responses requires comparable measurement conditions.

**Source-chain inspection**
- `SRC-ECOPHYSIOLOGY_BASICS@1` identifies itself as “Экологическая физиология изучает связь функций организма с условиями окружающей среды” but links to OpenStax Biology 2e, “Animal Sensory Systems and Movement”: `https://openstax.org/books/biology-2e/pages/44-animal-sensory-systems-and-movement`.
- The linked URL is not an ecophysiology overview and does not match the source identity stated in the record. The record therefore has a source identity/locator mismatch. It must not be treated as a verified textbook source for general organism-environment physiology.
- The EUs `EU-ECOPHYSIOLOGY_BASICS-A/B/C@1` are generic and do not name any exact relevant passage. Even if the linked chapter contains an example of an animal response, that would not establish the general claims about all organisms, tolerance ranges or comparable measurement conditions.
- A potentially relevant conceptual source for Claim B is Nature Education, “Physiological Optima and Critical Limits”: `https://www.nature.com/scitable/knowledge/library/physiological-optima-and-critical-limits-45749376/`. Its abstract explains that organismal distribution limits and responses to climate change depend on physiological performance across optimal and extreme conditions, and discusses critical tolerance limits. Access to the page was blocked during this check, so this remains a candidate, not verified canonical evidence.
- A further accessible teaching candidate is Georgia Tech's Organismal Biology material on plant and animal responses to the environment: `https://organismalbio.biosci.gatech.edu/materials-balance-and-homeostasis/plant-and-animal-responses-to-the-environment/`. It gives examples of thermoregulation in animals and water/heat stress in plants. It may support specific examples, but it is not sufficient by itself for all three broad Claims.
- Claim C needs a separate methods source addressing controlled/comparable measurement conditions, experimental design, temperature/acclimation, life stage, species, measurement protocol and uncertainty. Neither the current OpenStax URL nor the two candidates above has been shown to support that full proposition.

**Evidence Use and boundary defects**
- All three EUs lack claim-specific locators and cite a Source whose identity does not match its URL.
- `CTX-ECOPHYSIOLOGY_BASICS@1` and `SCP-ECOPHYSIOLOGY_BASICS@1` target Claim A only; Claims B/C lack formal per-Claim boundaries.
- Claim A is too broad unless the domain is bounded by organism, physiological process and environmental factor. Claim B should specify that tolerance ranges vary by species, life stage, acclimation and the physiological function being measured; survival, growth and reproduction do not necessarily share the same limits. Claim C is a methodological proposition and needs its own methods evidence rather than a general ecology reference.
- Do not convert laboratory tolerance ranges into universal safe operating limits for people, animals, crops or ecosystems. Do not infer that a species' distribution boundary is determined by one physiological variable alone; biotic interactions, resource availability and multiple interacting environmental factors can matter.
- The slice is basic ecological/organismal science, not human medical advice, veterinary diagnosis or agricultural treatment instructions.

**Decision: HOLD — all three Claims and the Source chain.** First reconcile the Source identity with a genuinely relevant external reference; then map each Claim to a precise passage and add claim-specific Context/Scope. Claim C likely needs a separate experimental-methods source. No canonical change.

#### 4. Cross-slice and first-edition conclusions

- **Pathology ↔ histology/cell biology:** pathology interprets disease-related changes in cells and tissues; histology supplies structural observations. Histological morphology alone does not establish etiology, full pathogenesis or individual diagnosis.
- **Pathology ↔ clinical laboratory medicine:** anatomic pathology and clinical pathology/laboratory medicine are related but distinct diagnostic domains. The current pathology slice should not collapse them into one method or imply that a MeSH definition substantiates every clinical laboratory discipline.
- **Plant pathology ↔ plant biology/ecology/soil science/microbiology:** the APS source directly supports the interdisciplinary nature of phytopathology. Biotic pathogens and abiotic disorders must remain distinct; plant disease does not automatically mean transmissible infection.
- **Ecophysiology ↔ physiology/ecology/climate:** organismal responses depend on environmental conditions, but tolerance limits are function-, species- and context-dependent. A broad ecological concept cannot be used as a universal threshold or operational safety rule.
- No typed Relation is created. These are conceptual dependencies, not evidence-backed versioned Relation records.
- No prior closed audit is reopened. The earlier physiology and plant/life-support work is retained; this section adds only the new pathology/plant-pathology/ecophysiology source-chain findings.

**Overall decision: HOLD for all three slices.** Plant pathology is the strongest candidate: the APS page is substantively aligned, with locator and boundary work remaining. Pathology has direct support for Claim A only; B/C require additional sources and narrowing. Ecophysiology has a demonstrable Source identity/URL mismatch and requires a corrected source chain before any inclusion decision. No public INCLUDE is granted by this audit.


### 50. Zoology, livestock systems, ecology and ecosystems — unresolved-debt follow-up; One Health and animal-health coverage gap (2026-11-19)

This section is a targeted follow-up to the unresolved findings already recorded in §35, not a repetition of its full ten-slice screen and not a claim that any prior HOLD has been closed. It rechecks the exact live source pages for four relevant slices and adds a bounded coverage review for zoonoses, veterinary/public animal health and One Health. Historical §35 findings remain intact. No canonical JSON, README, Relation, Assessment or publication status is changed.

#### 1. zoology-basics — prior HOLD confirmed; current Source URL is narrower than the Claim set

**Current Claims (all version 1)**
- **A — `CLM-ZOOLOGY_BASICS-A@1`:** Zoology is a branch of biology that studies animals.
- **B — `CLM-ZOOLOGY_BASICS-B@1`:** Animals form diverse evolutionary lineages with different body plans.
- **C — `CLM-ZOOLOGY_BASICS-C@1`:** Animal classification is based on observable and evolutionarily significant characteristics.

**Live source check**
- `SRC-ZOOLOGY_BASICS@1` currently identifies itself as a general definition of zoology but points to OpenStax Biology 2e Chapter 28 Introduction: `https://openstax.org/books/biology-2e/pages/28-introduction`.
- The live page is explicitly the introduction to **Invertebrates**, not a general zoology introduction. It describes the diversity and structural adaptations of invertebrate phyla and notes that their phylogenetic relationships are updated as new information is collected. It does not define zoology as a discipline, and its taxonomic scope is narrower than the all-animal wording of Claims A–C.
- Better topical candidates inside the same textbook are §27.2 “Features Used to Classify Animals” (`https://openstax.org/books/biology-2e/pages/27-2-features-used-to-classify-animals`) and §27.3 “Animal Phylogeny” (`https://openstax.org/books/biology-2e/pages/27-3-animal-phylogeny`). The Chapter 27 summary explicitly says animal classification uses morphology, developmental pathways and genetic affinities, and that phylogenetic trees use morphological/developmental, fossil and molecular evidence: `https://openstax.org/books/biology-2e/pages/27-chapter-summary`.
- These are candidates for Claim B/C, not existing canonical Source records and not evidence for Claim A's definition of zoology. A direct general reference defining zoology as the study of animals is still needed for A.
- **Material rights restriction:** OpenStax pages state that the textbook must not be used to train or otherwise be ingested into large language models or generative-AI offerings without prior written permission. The same page states CC BY-NC-SA for ordinary reuse, but that licence statement does not override the separate LLM-ingestion restriction. This applies to the current Chapter 28 page and the proposed Chapter 27 candidates. Do not treat a public URL or CC BY-NC-SA label alone as permission to feed the material into AI-based workflows, create AI-derived extracts, or include copied textbook text in the corpus. Obtain written permission for the intended AI use or select a source whose terms permit it.
- The current three EUs remain generic and have no exact section or passage locators. Context and Scope target Claim A only; B/C have no formal claim-specific boundaries.

**Decision: HOLD — all three Claims.** Correct the Source identity and scope; locate a direct definition for A and separate animal-diversity/phylogeny evidence for B/C; add exact EU locators and Claim-specific Context/Scope. OpenStax is a useful scholarly teaching reference for content, but its explicit AI-ingestion restriction is a material source-use blocker for AI-mediated processing unless written permission is obtained.

#### 2. livestock-systems-basics — source is directly aligned; record-level and independent-evidence debt remains

**Current Claims**
- **A — `CLM-LIVESTOCK_SYSTEMS_BASICS-A@1`:** Livestock systems cover keeping domesticated terrestrial animals to obtain products and services.
- **B — `CLM-LIVESTOCK_SYSTEMS_BASICS-B@1`:** Livestock systems include not only production but also the distribution of resources, people, products, impacts and benefits.
- **C — `CLM-LIVESTOCK_SYSTEMS_BASICS-C@1`:** System characteristics depend on animal species, production model, geography, resources and farm objectives.

**Live source check**
- `SRC-LIVESTOCK_SYSTEMS_BASICS@1` points to FAO “Livestock Systems”: `https://www.fao.org/livestock-systems/en/`.
- The live FAO page directly defines livestock as domesticated terrestrial animals raised for goods and services (including traction, meat, milk, eggs, hides, fibres and feathers). This directly supports the core of Claim A.
- The immediately following definition says livestock systems embrace the supply and use of livestock commodities, distribution and abundance, production systems, consumption/production estimates, people engaged in production, and the benefits and impacts of keeping livestock. This is a close direct match for Claim B. Exact locator: FAO “Livestock Systems”, opening definition paragraphs.
- FAO “Production systems” further explains that the scale, purpose and nature of the enterprise define its production system, and that ruminant systems depend strongly on agro-ecology and land use, while pig/poultry systems depend more on consumer demand and capital investment: `https://www.fao.org/livestock-systems/production-systems/en/`. This supports part of Claim C, but not necessarily every listed factor or every production model.
- FAO “Animal health” states that animal health systems include prevention/control, surveillance/early warning, emergency preparedness/response, veterinary services and laboratories, and One Health: `https://www.fao.org/animal-health/en/`. This is useful as a separate animal-health dependency, not evidence that the current livestock-system Claims cover veterinary medicine or animal disease diagnosis.
- The three EUs still contain only generic statements and do not identify the exact FAO paragraphs. The current Context and Scope target Claim A only; Claim C's local/species/production-model variability is not formally bounded. The Source set still contains one FAO source record; independent source diversity remains an open requirement from §35.

**Boundaries**
- Do not universalize production-system descriptions across species, agroecological zones, economies or production scales.
- Do not treat livestock as synonymous with all animals: livestock is a domesticated terrestrial-animal category, while wildlife, companion animals, aquatic animals and free-living species have different scopes.
- Do not infer animal welfare compliance, veterinary diagnosis, disease freedom, food safety, environmental sustainability or productivity from the broad system definition alone. Each requires its own evidence and local context.
- Claim B's phrase “distribution of resources” is broader than the FAO wording about distribution/abundance of livestock and supply/use of commodities. Clarify whether it means livestock distribution, commodity flows, production inputs or all three; do not leave “resources” as an unbounded paraphrase.

**Decision: HOLD — all three Claims.** The FAO page directly supports A/B and partly supports C, so the previous broad source-fit concern can be narrowed: the source is relevant, but the EU records still need exact paragraph locators, C needs more precise factor-level support and Context/Scope, and a genuinely independent evidence track is still absent. The animal-health FAO page is a candidate for a distinct future veterinary/animal-health slice, not a retroactive dependency for the current three Claims.

#### 3. ecology-basics — prior content-level HOLD confirmed; do not mistake editorial disclaimers for ecology knowledge

The current Claims A–C remain meta-statements about the slice itself: it introduces concepts, requires attention to source/context, and does not replace specialist verification. They are not substantive Claims about ecological relationships, populations, communities, energy, matter, habitats or ecological processes. The current Source points to OpenStax Biology 2e Chapter 46 Introduction (ecosystems), not a general ecology definition or claim-specific ecological passages.

This is the same content-level gap already recorded in §35, not a new substantive audit or closure. A possible source candidate for a rebuilt, genuinely educational ecology slice is OpenStax Biology 2e §44.1 “The Scope of Ecology”: `https://openstax.org/books/biology-2e/pages/44-1-the-scope-of-ecology`. However, OpenStax's explicit restriction on LLM/generative-AI ingestion without prior written permission must be addressed before that source is used in AI-mediated content processing. The claims should be rebuilt as actual ecology knowledge through an authorized editorial process; do not simply reword the three meta-claims and retain the same evidence chain.

**Decision: HOLD — all three Claims.** Preserve §35; this follow-up confirms no substantive replacement has occurred. No canonical rewrite authorized.

#### 4. ecosystems-basics — source is directly aligned; exact EU locators and rights review remain

**Current Claims**
- **A — `CLM-ECOSYSTEMS_BASICS-A@1`:** An ecosystem includes a community of living organisms and their interactions with the abiotic environment.
- **B — `CLM-ECOSYSTEMS_BASICS-B@1`:** Energy flows and matter cycles are important components of ecosystem functioning.
- **C — `CLM-ECOSYSTEMS_BASICS-C@1`:** Ecosystems can differ substantially in scale and environment type.

**Live source check**
- `SRC-ECOSYSTEMS_BASICS@1` points to OpenStax Biology 2e §46.1 “Ecology of Ecosystems”: `https://openstax.org/books/biology-2e/pages/46-1-ecology-of-ecosystems`.
- The page directly defines an ecosystem as a community of living organisms and their interactions with the abiotic environment (§46.1 opening discussion; live page lines 31–34). This directly supports Claim A.
- The same section describes the three broad environment categories (freshwater, ocean water and terrestrial) and variation within them (lines 35–41), directly supporting Claim C at an introductory level.
- The “Food Chains and Food Webs” section describes energy and nutrient transfer through trophic levels (lines 47–57), and the conceptual-model discussion describes energy and nutrient flows among ecosystem compartments (lines 97–103). This supports the energy-flow and nutrient-cycling core of Claim B. Keep “matter cycling” conceptually distinct from energy flow: matter is recycled through biological and geochemical processes, while energy passes through trophic levels and is dissipated as heat.
- All three EUs are still generic; none points to these exact section headings or passages. Context and Scope target Claim A only; B/C need explicit applicability boundaries.
- **Material rights restriction:** §46.1 states that OpenStax content must not be used for LLM training or otherwise ingested into LLM/generative-AI offerings without prior written permission, despite its ordinary CC BY-NC-SA reuse terms. This is a blocker for AI-mediated processing unless permission is obtained. Do not infer permission from the fact that the Source record stores only a URL.
- The prior §35 second-source requirement remains open. A second independent source must be assessed for actual Claim-level support and compatible reuse/AI-processing terms; a second URL to the same OpenStax textbook is not independent evidence.

**Decision: HOLD — all three Claims and dependency closure.** The scientific source is well matched and exact passages have now been identified, but current EU records remain non-pinpointed, B/C lack formal Context/Scope, independent evidence is missing, and the OpenStax AI-ingestion restriction must be resolved before AI-mediated reuse. No canonical changes.

#### 5. Zoonoses, veterinary/public animal health and One Health — confirmed Part I coverage gap

The current `CONTENT/vertical-slices` inventory contains zoology, livestock systems, ecology and ecosystems, but no dedicated `zoonoses-basics`, `one-health-basics`, `veterinary-public-health-basics` or equivalent animal-health/zoonoses slice. This is a real coverage gap. The livestock-system slice does not substitute for animal health; zoology does not substitute for veterinary/public health; and existing human microbiology, epidemiology, AMR and public-health-surveillance slices do not by themselves establish animal-to-human transmission pathways or animal-health surveillance.

**Verified authoritative source candidates**
- FAO “Zoonoses” defines zoonotic diseases as diseases shared between animals (including livestock, wildlife and pets) and people. It lists foodborne, waterborne, vector-borne, direct-contact and indirect fomite/environmental-contamination routes and describes the human–animal–environment interface: `https://www.fao.org/one-health/areas-of-work/zoonoses/`. The live page explicitly defines a zoonosis as a disease or infection naturally transmissible from vertebrate animals to humans. This supports a future descriptive Claim set, not a universal claim that every pathogen or every animal species transmits infection to humans.
- WHO “One Health” (fact sheet, 8 May 2026) describes an integrated approach across human, animal, plant and ecosystem health; identifies zoonotic, vector-borne, food-safety, AMR and environmental concerns; and stresses cross-sector collaboration, prevention, detection and response: `https://www.who.int/news-room/fact-sheets/detail/one-health/`.
- FAO “Animal health” identifies prevention/control, surveillance and early warning, preparedness/response, veterinary services and laboratories as components of animal-health systems: `https://www.fao.org/animal-health/en/`.
- FAO “Biosecurity in terrestrial animal value chains” describes biosecurity as an integrated risk-management approach protecting agriculture, food and the environment from biological risks, including risks across livestock and wildlife sectors: `https://www.fao.org/animal-health/areas-of-work/biosecurity/en`.
- WOAH Terrestrial Animal Health Code, Chapter 1.4, “Animal health surveillance”, explains that surveillance objectives include demonstrating absence, determining presence/distribution and early detection of exotic or emerging disease; the design depends on objectives, data sources and decision needs: `https://www.woah.org/fileadmin/Home/eng/Health_standards/tahc/current/en_chapitre_surveillance_general.htm`.

**Proposed bounded coverage architecture (design proposal only; no canonical records created)**
1. **Zoonoses basics:** definition and boundaries; animal reservoirs/hosts/vectors as distinct concepts; transmission routes; human–animal–environment interface; uncertainty and species/pathogen specificity.
2. **Veterinary and animal-health systems basics:** animal health, veterinary services, prevention, welfare, surveillance, early warning and emergency response at a high level. Keep clinical diagnosis and treatment outside the introductory slice.
3. **One Health basics:** integrated governance and collaboration across human, animal, plant and environmental health; shared surveillance and risk communication; AMR, food safety and ecosystem context.
4. **Animal biosecurity basics:** prevention and risk governance in farms/value chains and interfaces with wildlife; keep separate from laboratory biosafety/biosecurity already identified in §48.
5. Maintain separate layers for **human public health**, **animal health**, **food safety**, **environmental/ecosystem health** and **laboratory biosafety**. Their relations must be typed, versioned and justified by a real shared concept or evidence dependency, not generic topic similarity.

**Safety and scope boundaries**
- No diagnosis of animal or human illness, drug/vaccine regimen, treatment protocol, pathogen isolation/culture, propagation, genetic manipulation, deliberate infection, vector breeding or operational pathogen-handling procedures.
- Do not treat every zoonosis as transmitted by direct animal contact; food, water, vectors, fomites and environmental contamination are distinct possible pathways and depend on the disease.
- Do not equate One Health with a single agency, a single surveillance database or a universal response protocol. Roles, reporting obligations and veterinary/public-health authority are jurisdiction-specific.
- Wildlife, livestock, companion animals and aquatic animals require distinct ecological, legal and epidemiological boundaries. A statement about terrestrial livestock must not be generalized to wildlife or aquaculture.

**Decision: COVERAGE GAP — no new vertical slice or Relation is created in this audit.** The authoritative sources are suitable candidates for a future Russian-first, prevention/governance-oriented content design. A new slice set requires its own scoped Claims, direct Evidence Use, exact locators, independent sources, Context/Scope and human-view review before any publication decision.

#### 6. Cross-slice dependency and decision summary

- Zoology supplies animal diversity and classification foundations; it does not establish animal disease or veterinary practice.
- Livestock systems describe domesticated terrestrial animal production and associated supply/use/impact systems; they do not cover all animal populations or all animal-health services.
- Ecology and ecosystems provide population/community/environment foundations; they do not alone establish zoonotic causation or outbreak risk.
- Zoonoses require explicit animal–human transmission evidence and disease-specific routes; One Health provides the cross-sector governance framework, not a substitute for those mechanisms.
- Animal-health surveillance and human public-health surveillance are related but distinct systems with different target populations, case definitions, authorities and outputs.
- No Relations are added. A future relation between livestock, animal health, zoonoses, food safety, AMR, human epidemiology and ecosystem health must identify the exact Claim versions and a specific evidentiary or operational dependency.

**Overall disposition:** preserve all prior §35 HOLD decisions. The FAO livestock source has now been verified as directly supporting the broad A/B definitions, while exact EUs, Claim-C boundaries and independent evidence remain. Zoology's existing OpenStax URL is narrower than the all-animal Claims, and OpenStax's explicit AI-ingestion restriction is material. Ecology remains a meta-Claim coverage defect. Ecosystems has strong direct §46.1 support but unresolved EU, boundary, independent-source and AI-rights debts. Zoonoses/One Health/animal health is a confirmed coverage gap requiring a separately designed and audited content set. No public INCLUDE is granted.


---

## §51 — Agricultural, food-system, biodiversity, forestry, fisheries and marine-life record-level follow-up (2026-11-19)

**Audit scope:** targeted current-record review of ten adjacent vertical slices after §50, selected from the live PR #22 tree. This is a new record-level follow-up, not a blanket rerun of earlier closed work. It checks current Claim/Source/Evidence Use/Context/Scope versions, source identity and live source fit. Historical records and prior maturity work are preserved.

**Repository boundary:** PR #22 branch `mvp-public-contribution-design-2026-10-11`, HEAD `4faea3252af24c71855d52ed4bac6b14448fc31f`. No canonical JSON, README, Relations, Assessments, publication status or `main` changes are authorized or made by this audit.

### 1. agriculture-basics — FAO portal is not a claim-level source; USDA corroboration is narrow

**Current Claims**
- A — `CLM-AGRICULTURE_BASICS-A@1`: agriculture includes activities producing plant and animal products and managing related resources.
- B — `CLM-AGRICULTURE_BASICS-B@1`: agricultural productivity depends on interactions among soil, water, biological factors, climate and management.
- C — `CLM-AGRICULTURE_BASICS-C@1`: agricultural practices must account for local natural conditions; results are not guaranteed to transfer to another location.

**Source and evidence chain**
- `SRC-AGRICULTURE_BASICS@1` points to the broad FAO Agriculture landing page (`https://www.fao.org/agriculture/`). Its identity is an institutional portal, not a pinpointed definition or technical passage for all three Claims.
- `EU-AGRICULTURE_BASICS-A/B/C@1` each link the relevant Claim to that same broad FAO landing page. Their descriptions are generic and contain no section, paragraph, table, figure or other exact locator.
- The additional `SRC-USDA-AGRICULTURE-CONTEXT@1` points to USDA Climate Hubs “Manage crops to cope with warmer and drier conditions” (`https://www.climatehubs.usda.gov/approach/manage-crops-cope-warmer-drier-conditions`). `EU-AGRICULTURE-USDA-CORROBORATION@1` links it only to Claim B. This is a useful independent corroboration for the interaction of soil, water and climate with management, but it does not independently establish Claim A's broad definition or all of Claim C's transferability language.
- FAO materials on sustainable land management and agriculture–nature interactions are plausible candidates for a rebuilt evidence chain, but they are not the current Source record and must not be treated as if already linked.

**Record-level findings**
- Claim A is plausible as a high-level description but the current FAO portal URL does not establish the complete definition as recorded.
- Claim B has the strongest support: USDA's page gives context-specific evidence about crop management under warmer/drier conditions, but the EU description should identify the actual passage and narrow the supported factors. It is not a universal proof of all agricultural productivity drivers.
- Claim C is a sound applicability boundary, but its current FAO EU does not point to evidence that supports it. The USDA source is contextual corroboration, not a universal statement that all agricultural practices fail to transfer.
- Context and Scope target Claim A only; B/C have no claim-specific formal boundaries.

**Decision: HOLD — A/B/C.** Preserve the USDA corroboration as an existing additional evidence record. Do not infer that it closes A or C. Replace broad portal-level evidence with exact, compatible, claim-specific passages and extend Context/Scope coverage before reconsideration.

### 2. agricultural-engineering-basics — material source-to-Claim scope mismatch

**Current Claims**
- A — `CLM_AGRICULTURAL_ENGINEERING_BASICS_A@1`: agricultural engineering applies engineering principles to agricultural production and resource management.
- B — `CLM_AGRICULTURAL_ENGINEERING_BASICS_B@1`: it includes machinery, irrigation, drainage, storage, processing and other farm-operation systems.
- C — `CLM_AGRICULTURAL_ENGINEERING_BASICS_C@1`: choices depend on crops, soils, water, climate, energy, labour and operating conditions.

**Source and evidence chain**
- `SRC_AGRICULTURAL_ENGINEERING_BASICS@1` identifies “FAO — Land and water management” and points to `https://www.fao.org/land-water/land/soil-water-management/en/`.
- The live FAO land/soil/water material is relevant to agricultural water management, irrigation, water harvesting, soil and water conservation, and associated governance. It does not, as a single source, define the whole discipline of agricultural engineering or establish the full list in Claim B.
- The current EUs A/B/C use generic “source supports the claim within the stated scope” descriptions, without exact locators.
- Context and Scope target Claim A only.

**Record-level findings**
- A is broader than the current land-and-water source identity; an engineering-discipline source is required.
- B combines several engineering subdomains. The current source can support only a subset, especially irrigation/water management; machinery, drainage engineering, storage, processing and farm systems need distinct evidence.
- C's factors are plausible but are not mapped individually to the current source. Crop/soil/water/climate factors cannot silently stand in for energy, labour and operating constraints.
- The FAO irrigation-management page (`https://www.fao.org/land-water/water/agricultural-water-management/irrigation/en`) is a useful candidate for an irrigation subclaim, not a replacement source for the whole engineering discipline. FAO water-harvesting/storage and drainage references are similarly narrow candidates.

**Decision: HOLD — A/B/C.** The source is topically adjacent but materially narrower than the slice. Either narrow the slice to land/water engineering or add appropriately scoped engineering sources for machinery, drainage, storage, processing and farm systems. No canonical rewrite is authorized.

### 3. agrifood-systems-basics — strong FAO definition; remaining EU precision and Claim-C boundaries

**Current Claims**
- A — `CLM-AGRIFOOD_SYSTEMS_BASICS-A@1`: an agrifood system includes people, activities, investments and decisions involved in producing and delivering food and agricultural goods.
- B — `CLM-AGRIFOOD_SYSTEMS_BASICS-B@1`: the chain can include growing, harvesting, processing, packaging, transport, distribution, trade, purchase, preparation, consumption and disposal.
- C — `CLM-AGRIFOOD_SYSTEMS_BASICS-C@1`: analysis must consider production, economic, social and environmental connections.

**Source and evidence chain**
- `SRC-AGRIFOOD_SYSTEMS_BASICS@1` points to FAO Agrifood Systems (`https://www.fao.org/food-systems/en`). The live FAO definition directly identifies people, activities, investments and choices; the journey from production through consumption and disposal; and non-food agricultural products such as forestry, feedstock, biomass and fibres.
- The FAO FAQ (`https://www.fao.org/food-systems/faq/en`) explicitly includes growing, raising, culturing, fishing, harvesting, processing, packaging, transport, distribution, trade, purchase, preparation, eating, disposal/reuse and non-food agricultural, forest and fisheries products. This directly supports the breadth of A/B.
- `SRC-WORLDBANK-FOODSYSTEMS-2030@1` points to World Bank FoodSystems 2030. `EU-AGRIFOOD-WORLDBANK-CORROBORATION@1` links this source only to Claim C. The live World Bank programme describes connected human health, planetary health and economic prosperity, and the incentives, institutions, investments and behaviours shaping outcomes. This is useful corroboration for systems-level C, but is a programme overview rather than a precise empirical proof of every possible systems relationship.
- The three primary EUs remain generic and do not point to exact FAO passages. The World Bank EU also gives a broad summary rather than a pinpoint locator.
- Context and Scope target Claim A only.

**Record-level findings**
- A/B are closely aligned with the FAO definition. B is a “can include” list and should retain the distinction between food and non-food agricultural products; FAO's agrifood concept is wider than food-only systems.
- C is directionally supported by FAO and the World Bank programme, but its broad list of production/economic/social/environmental connections needs exact passages and boundaries. A programme's stated transformation goals should not be mistaken for measured causal findings.
- The slice needs claim-specific Context/Scope for B/C, and exact locators for both FAO and World Bank evidence.

**Decision: HOLD — A/B/C pending EU locator and boundary completion.** This is not a source-fit failure: FAO is directly relevant. Preserve the existing World Bank corroboration for C; do not claim it independently validates A/B.

### 4. food-systems-basics — valid two-source architecture, but incomplete Claim-level distribution and duplication risk with agrifood

**Current Claims**
- A — `CLM-FOOD_SYSTEMS-A@1`: food systems cover interconnected production, processing, distribution, consumption and disposal.
- B — `CLM-FOOD_SYSTEMS-B@1`: they include people, activities, investments and decisions connected with producing and delivering food.
- C — `CLM-FOOD_SYSTEMS-C@1`: analysis considers links among natural resources, technologies, trade, food access and other chain stages.
- D — `CLM-FOOD_SYSTEMS-D@1`: the system includes storage, processing, distribution, transport, logistics and retail beyond production.

**Source and evidence chain**
- `SRC-FOOD_SYSTEMS@1` points to the same FAO Agrifood Systems page used by agrifood-systems-basics.
- `SRC-FOOD_SYSTEMS_WB@1` points to World Bank “The Future of Food” (`https://www.worldbank.org/en/topic/agriculture/publication/the-future-of-food-shaping-the-global-food-system-to-deliver-improved-nutrition-and-health`). `EU-FOOD_SYSTEMS-D@1` links it to D. The live World Bank page supports the production-to-consumption continuum and identifies producers, post-harvest handlers, processors, distributors and consumers; it also emphasizes that interventions must be tailored to country circumstances.
- EUs A/B/C link only to FAO and use generic descriptions. EU D identifies World Bank but supplies no exact locator.
- Context and Scope target Claim A only. README describes a two-source/four-Claim profile, but the current Evidence Use graph distributes World Bank to D only.

**Record-level findings**
- A/B are directly aligned with FAO's system definition.
- C is a broad analytical proposition. FAO's systems material discusses interconnected components and trade-offs; World Bank sources discuss economic, social, nutrition and health outcomes. Exact passages must be identified for each component rather than using a broad source label.
- D is supported at a high level by the World Bank production-to-consumption continuum. The exact terms “transport”, “logistics” and “retail” need locator-level confirmation.
- **Taxonomic boundary:** food systems and agrifood systems are related but not identical. FAO's 2021 definition distinguishes the wider agrifood system (including non-food agricultural outputs) from the food system (products intended for human consumption). The two current slices substantially overlap in A/B and need an explicit editorial distinction so they do not become duplicate concept records. Do not collapse the two slices without an authorized canonical decision.

**Decision: HOLD — A/B/C/D pending pinpoint EU and boundary work.** Preserve the existing two-source structure and historical maturity state. This follow-up identifies a record-level debt, not authorization to rewrite or merge either slice.

### 5. biodiversity-basics — one OpenStax section does not cover the full three-Claim chain; material AI-use restriction

**Current Claims**
- A — `CLM-BIODIVERSITY_BASICS-A@1`: biodiversity includes species diversity, genetic variants and ecosystem diversity.
- B — `CLM-BIODIVERSITY_BASICS-B@1`: species counts can change with the balance between speciation and extinction.
- C — `CLM-BIODIVERSITY_BASICS-C@1`: biodiversity assessment depends on spatial scale, time and observation method.

**Source and evidence chain**
- `SRC-BIODIVERSITY_BASICS@1` points to OpenStax Biology 2e §47.4 “Preserving Biodiversity” (`https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity`).
- §47.4 covers methods for describing biodiversity, DNA barcoding, species cataloguing, conservation strategies, preserve design and restoration. The Chapter 47 key terms and §47.1 “The Biodiversity Crisis” are more directly relevant to the definition, speciation/extinction balance and measurement concepts, but are not the current Source record.
- All three EUs are generic; no exact passage locators are supplied. Context and Scope target Claim A only.
- **Material rights restriction:** OpenStax pages explicitly state that textbook material must not be used for training or otherwise ingested into LLMs or generative-AI offerings without prior written permission. The ordinary CC BY licence statement does not override that separate restriction. This is a blocker for AI-mediated processing unless permission is obtained or a compatible alternative source is selected.

**Record-level findings**
- A's three-level definition is supported more directly by the Chapter 47 key terms/§47.1 than by the selected §47.4 page alone.
- B is directly explained in §47.1 through the relationship between speciation and extinction, but the current URL and EU do not locate that passage.
- C is only partly supported by the selected section's treatment of DNA barcoding, cataloguing and species-area relationships; a precise methods/scale/time passage is needed.
- No independent compatible source is linked.

**Decision: HOLD — A/B/C.** Preserve the existing records. Resolve the OpenStax AI-ingestion restriction before AI-mediated use; then provide claim-specific source passages, exact EUs and Context/Scope for B/C. Do not treat the presence of a public URL as permission.

### 6. conservation-biology-basics — substantial overlap with biodiversity; no discipline definition or independent source

**Current Claims**
- A — `CLM-CONSERVATION_BIOLOGY_BASICS-A@1`: biodiversity is associated with species diversity and changes in organism abundance over time.
- B — `CLM-CONSERVATION_BIOLOGY_BASICS-B@1`: conservation considers population, habitat and ecosystem condition.
- C — `CLM-CONSERVATION_BIOLOGY_BASICS-C@1`: habitat restoration is one tool for conserving biodiversity.

**Source and evidence chain**
- `SRC-CONSERVATION_BIOLOGY_BASICS@1` points to the same OpenStax Biology 2e §47.4 “Preserving Biodiversity” URL as biodiversity-basics.
- The section discusses preserve design, habitat restoration, species/population considerations, and conservation approaches, so it is topically aligned with B/C. It does not by itself define conservation biology as a discipline, and Claim A substantially repeats a biodiversity concept rather than stating a distinct conservation-biology proposition.
- EUs A/B/C remain generic and have no exact locators. Context and Scope target Claim A only. A second independent source is absent.
- The same OpenStax restriction on LLM/generative-AI ingestion without prior written permission applies.

**Record-level findings**
- B/C have a plausible direct thematic fit to §47.4 but need precise locators and claim-specific boundaries.
- A overlaps with biodiversity-basics and should not be treated as a distinct conservation-biology foundation without an editorially meaningful conservation-specific claim.
- Restoration is one conservation tool; it is not equivalent to ecosystem recovery, biodiversity recovery, or proof of restoration success in a particular site.
- The source's AI-ingestion restriction remains material.

**Decision: HOLD — A/B/C.** Preserve the slice and its existing records; no duplicate-Claim rewrite is authorized. A future authorized revision should distinguish conservation science and intervention evaluation from general biodiversity definitions, add independent compatible evidence, and define success/uncertainty boundaries.

### 7. fisheries-basics — FAO management source strongly supports B, but A/C and capture-fishery boundaries remain

**Current Claims**
- A — `CLM-FISHERIES_BASICS-A@1`: fisheries have economic and social significance and provide diverse products.
- B — `CLM-FISHERIES_BASICS-B@1`: fisheries management is needed to align resource use with resource condition and ecological conditions.
- C — `CLM-FISHERIES_BASICS-C@1`: assessment and management depend on species, area, stock data, fishing methods and applicable rules.

**Source and evidence chain**
- `SRC-FISHERIES_BASICS@1` points to FAO “Chapter 1: Fisheries Management” (`https://www.fao.org/4/y3427e/y3427e03.htm`).
- The FAO chapter gives a working definition of fisheries management as an integrated process of information gathering, analysis, planning, consultation, decisions, resource allocation, rules and enforcement to maintain resource productivity and meet other objectives. This is a direct conceptual fit for B.
- The source discusses sustained benefits and ecosystem-oriented management, but it does not, from the current locator alone, establish all of A's social/economic/product assertions or each factor enumerated in C.
- EUs A/B/C contain generic descriptions and no exact locator. One FAO source is linked. Context and Scope target A only.

**Record-level findings**
- B is the strongest Claim and has a close direct source match.
- A needs a source explicitly supporting the social/economic contribution and product range of fisheries; management guidance alone is not enough.
- C needs exact support for stock information, species/area differences, gear/methods and applicable rules. These are not interchangeable dimensions and may vary by fishery.
- **Boundary:** the current slice is fisheries/capture-fishery management; do not silently generalize it to aquaculture, fish farming, aquatic animal health or all marine resource use.

**Decision: HOLD — A/B/C.** Preserve the FAO source as relevant to B and parts of C. Add independent, claim-specific evidence and exact locators; make the capture-fisheries versus aquaculture distinction explicit.

### 8. forestry-basics — strong FAO source fit; pinpoint evidence and context coverage remain incomplete

**Current Claims**
- A — `CLM-FORESTRY_BASICS-A@1`: forest management treats forests as resources with ecological, economic, social and cultural functions.
- B — `CLM-FORESTRY_BASICS-B@1`: sustainable forest management links conservation and use with long-term objectives.
- C — `CLM-FORESTRY_BASICS-C@1`: objectives and measures depend on forest type, local conditions, law and stakeholder interests.

**Source and evidence chain**
- `SRC-FORESTRY_BASICS@1` points to FAO Sustainable Forest Management overview (`https://www.fao.org/forestry/sfm/overview/`).
- The live FAO overview directly defines forest management as planning and implementing stewardship/use practices for environmental, economic, social and cultural objectives. It describes SFM as sustainable use and conservation maintaining multiple forest values, and notes the diversity of forest types, conditions and socioeconomic contexts.
- FAO's forest-management-planning module (`https://www.fao.org/sustainable-forest-management-toolbox/modules/forest-management-planning/en`) is a strong candidate for C: it discusses legal, biophysical, socioeconomic and market assessments, stakeholder participation, objectives, forest inventories, approval and periodic revision.
- Current EUs A/B/C are generic and do not point to exact paragraphs. Context and Scope target A only. Only one Source record is linked.

**Record-level findings**
- A/B have strong direct alignment with the current FAO overview.
- C is substantially supported by the FAO planning module, but that module is a candidate source, not a current canonical evidence link. Local law and approval requirements are jurisdiction-specific; stakeholder interests can conflict.
- The source itself notes that a single precise global definition of SFM is impractical given forest and socioeconomic diversity. This is a necessary boundary, not a defect in the FAO source.
- Claim-specific Context/Scope for B/C and a second independent source remain open.

**Decision: HOLD — A/B/C pending EU precision and independent corroboration.** This is a strong source-fit case, not a substantive source mismatch. Do not turn global principles into site-specific harvesting prescriptions or legal advice.

### 9. entomology-basics — unusually good single-source coverage; locator and independent-source debt

**Current Claims**
- A — `CLM-ENTOMOLOGY_BASICS-A@1`: entomology studies insects and, in broad professional usage, related arthropods.
- B — `CLM-ENTOMOLOGY_BASICS-B@1`: insects contribute to pollination, nutrient recycling and other ecological processes; some harm agriculture, health or buildings.
- C — `CLM-ENTOMOLOGY_BASICS-C@1`: entomology is applied in agriculture, ecology, human health, forestry and invasive-species research.

**Source and evidence chain**
- `SRC-ENTOMOLOGY_BASICS@1` points to the Entomological Society of America “What Is Entomology?” (`https://entsoc.org/about/what-is-entomology`).
- The live ESA page directly states that entomology studies insects and related animals; it explains that the term often includes spiders, ticks, centipedes and millipedes. It also describes pollination, predation, nutrient recycling, crop damage, disease transmission and damage to homes.
- The same page explicitly lists agriculture/food security, human health, household pests, invasive species, ecology, forest health and animal health as areas of study. It therefore has unusually good topical coverage for A/B/C.
- EUs A/B/C all point to this one source but use generic descriptions without exact passage locators. Context and Scope target A only. A second independent source is absent.

**Record-level findings**
- A is directly supported; the qualifier “in broad professional usage” is important and correctly prevents the false claim that all arthropods are insects.
- B is broadly supported, but the effects are heterogeneous: not all insects pollinate crops, recycle nutrients or harm people; ecological roles depend on species and context.
- C is directly supported by the ESA list of applied areas. It should not imply that introductory entomology provides clinical/vector-control or pest-control protocols.
- The ESA page is a professional-society source, suitable for introductory discipline scope, but the corpus still needs an independent source and precise EUs for robust evidence diversity.

**Decision: HOLD — A/B/C pending exact EUs, independent corroboration and Context/Scope coverage.** This is a strong candidate for targeted maturation; no canonical changes are made.

### 10. marine-biology-basics — existing P9 second-source records preserved; same-agency triangulation and exact locator debt

**Current Claims**
- A — `CLM_MARINE_BIOLOGY_BASICS_A@1`: marine biology studies organisms in marine environments, life cycles, habitats and interactions.
- B — `CLM_MARINE_BIOLOGY_BASICS_B@1`: marine food webs connect organisms through feeding relationships and energy transfer.
- C — `CLM_MARINE_BIOLOGY_BASICS_C@1`: marine organisms are affected by physical/biological conditions including temperature, oxygen, habitat and human impacts.

**Source and evidence chain**
- `SRC_MARINE_BIOLOGY_BASICS@1` points to NOAA “Marine life” (`https://www.noaa.gov/education/resource-collections/marine-life`). The live page describes marine organisms, life cycles, habits, habitats, interrelationships, changing environmental conditions and threats such as oxygen-depleted zones, debris, warming and overfishing.
- `SRC_NOAA_ECOSYSTEM_SCIENCE_2026@1` points to NOAA “What is ecosystem science?” (`https://oceanservice.noaa.gov/facts/ecosci.html`). Existing `EU_P9_MARINE_BIOLOGY_BASICS_A/B/C@1` records link this second source to all three Claims.
- The NOAA aquatic-food-webs resource (`https://www.noaa.gov/education/resource-collections/marine-life/aquatic-food-webs`) directly explains feeding relationships and energy flow and is a more pinpointed candidate for B.
- The current EUs A/B/C contain claim-specific summaries, but they still do not cite exact page sections or passages. The three P9 EUs are additional evidence records and are preserved.
- Both Source records are NOAA publications. They are distinct source documents, but not institutionally independent evidence providers. The second source is general ecosystem science and does not independently establish every marine-specific element of A/B/C.
- Context and Scope target A only. README records the existing P9 two-source/three-Claim/six-EU maturation profile; this follow-up does not erase that historical work.

**Record-level findings**
- A is directly supported by the NOAA Marine Life page.
- B has a clear exact candidate in NOAA's aquatic food-webs resource; the current marine-life landing page alone is not a pinpoint citation.
- C is supported at a broad descriptive level by NOAA's Marine Life page; the claim's specific list should be mapped to exact passages and kept distinct from site-specific exposure, environmental safety or intervention advice.
- P9 adds a second document, but both sources are NOAA. If the project's evidence-diversity rule requires independent institutions or independent research lineages, the present pair does not meet that stronger test.

**Decision: HOLD for first-edition candidate closure — A/B/C pending exact locators, claim-specific Context/Scope and institutionally independent corroboration if required by the applicable evidence-diversity standard.** Preserve the historical P9 maturation and all six EU records; no reassessment is silently substituted for prior closure.

### 11. Cross-slice architecture, duplication and coverage gaps

**A. Food systems versus agrifood systems**
- FAO distinguishes the wider agrifood system, which includes food and non-food agricultural/forestry/fisheries products and all related activities, from the food system focused on products intended for human consumption.
- The current slices share near-parallel claims about people, activities, investment/decisions and production-to-consumption chains. They should remain separate only if the editorial distinction is made explicit and each Claim is unique to its intended scope. No merge or canonical rewrite is authorized here.
- The same FAO landing page is used in both Source records. Reusing a URL under two Source IDs does not create independent evidence.

**B. Fisheries versus aquaculture**
- The current vertical-slice inventory has `fisheries-basics` and `marine-biology-basics`, but no dedicated `aquaculture-basics` slice.
- FAO agrifood sources include cultured aquatic products in the broader food chain, but that does not provide an introductory treatment of aquaculture systems, farmed aquatic organisms, production environments, water quality, biosecurity, animal health, welfare, or environmental interactions.
- **Coverage gap:** aquaculture is a distinct potential content domain. Do not silently fold aquaculture into capture fisheries or livestock systems.

**C. Animal welfare**
- The inventory has livestock systems and zoology, but no dedicated animal-welfare slice was identified in the live vertical-slice directory list. Neither general zoology nor production-system definitions establish welfare principles, assessment domains or jurisdiction-specific requirements.
- This is a candidate coverage gap for a future bounded slice, not permission to create records in this audit. Keep animal welfare distinct from animal health, veterinary diagnosis/treatment and productivity.

**D. Biodiversity and conservation**
- Biodiversity-basics and conservation-biology-basics currently share the same OpenStax §47.4 source URL and overlap in core statements. Their distinct purposes should be explicit: biodiversity concepts/measurement versus conservation objectives, threats, interventions and evaluation.
- The OpenStax AI-ingestion restriction applies to both. Do not use the textbook as input to AI-mediated content work without written permission, even though the source is publicly readable and carries an ordinary reuse licence.

**E. Forestry, fisheries and local operating rules**
- FAO global principles do not override local forest tenure, harvest authorization, fishery licensing, quotas, seasons, protected areas, gear restrictions or other jurisdictional requirements.
- These are not universal operational instructions. Site-, stock-, species- and jurisdiction-specific decisions require current official local data and competent authority.

**F. Cross-slice relations**
- No Relations are created. Potential conceptual links among agriculture, agrifood/food systems, soil, water, biodiversity, conservation, entomology, forestry, fisheries, marine biology, livestock and One Health are not self-proving.
- Any future Relation must identify exact versioned Claims and a specific evidentiary, causal, definitional or operational dependency. Topic adjacency alone is insufficient.

### 12. Consolidated dispositions

| Slice | Current disposition | Main unresolved item |
|---|---|---|
| agriculture-basics | HOLD A/B/C | Broad FAO portal; USDA corroboration only for B; generic EUs |
| agricultural-engineering-basics | HOLD A/B/C | Source too narrow for engineering discipline and full system list |
| agrifood-systems-basics | HOLD A/B/C | Strong FAO fit; exact locators and B/C boundaries |
| food-systems-basics | HOLD A/B/C/D | Existing two-source profile preserved; exact locators and distinction from agrifood |
| biodiversity-basics | HOLD A/B/C | Claim-to-section mismatch; OpenStax AI-use restriction |
| conservation-biology-basics | HOLD A/B/C | Overlap with biodiversity; one source; OpenStax AI-use restriction |
| fisheries-basics | HOLD A/B/C | B strongly supported; A/C and capture/aquaculture boundary |
| forestry-basics | HOLD A/B/C | Strong FAO fit; exact locators, independent evidence, B/C boundaries |
| entomology-basics | HOLD A/B/C | Strong ESA source; exact locators and independent evidence |
| marine-biology-basics | HOLD A/B/C for candidate closure | P9 preserved; NOAA-only source pair and exact locators |

**Overall result:** no public INCLUDE is granted by this follow-up. The strongest source-fit candidates are agrifood systems, food systems, forestry, entomology and marine biology; fisheries has a strong direct management source for Claim B; agriculture has narrow USDA corroboration for Claim B; agricultural engineering has a material source-scope mismatch; biodiversity and conservation have a material OpenStax AI-ingestion restriction and claim/locator debt. The newly identified aquaculture and animal-welfare gaps are recorded as coverage findings only.

**Change control:** no canonical records, README files, Relations, Assessments or publication states changed. Only this controlling audit register is extended.


---

## §52 — Soil, plant science, seed storage, ecotoxicology and food-chain safety follow-up (2026-11-19)

**Audit scope:** twelve adjacent vertical slices were inspected at current Claim, Source, Evidence Use, Context and Scope record level. The audit follows §51 and expands the review into the soil–plant–seed–food continuum. It does not repeat earlier closed work or rewrite canonical records.

**Repository boundary:** PR #22 branch `mvp-public-contribution-design-2026-10-11`, starting HEAD `d51b0102558a728cca0e903e06a35380ad7f0479`. No canonical JSON, README, Relation, Assessment, publication status or `main` changes are made by this audit.

### 1. soil-basics — official source is relevant, but evidence is not pinpointed

**Current Claims**
- A — `CLM-SOIL_BASICS-A@1`: soil is a natural system consisting of mineral and organic components, water, air and living organisms.
- B — `CLM-SOIL_BASICS-B@1`: soil properties affect water movement, nutrient availability and plant-growth conditions.
- C — `CLM-SOIL_BASICS-C@1`: soil properties vary by place and depth; one soil description cannot automatically be transferred to another.

**Evidence chain**
- `SRC-SOIL_BASICS@1` points to USDA NRCS “Soils” (`https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/soils`).
- `EU-SOIL_BASICS-A/B/C@1` link each Claim to that source but provide only generic descriptions, without a section, paragraph, table, figure or other exact locator.
- USDA NRCS “What is Soil?” (`https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil`) gives a direct soil definition as a natural body composed of mineral/organic solids, liquid and gases, and describes the role of climate, relief, organisms and time. This is a better direct locator candidate for A.
- USDA NRCS Soil Health Assessment (`https://www.nrcs.usda.gov/conservation-basics/soil/soil-health/soil-health-assessment`) identifies physical, chemical and biological indicators and explains links to water movement, nutrients, soil microbes and productivity. It is a useful candidate for B and for the local/field variability boundary in C.
- FAO Soils Portal describes soil's functions in plant growth, water regulation, biodiversity, carbon and nutrient cycles (`https://www.fao.org/soils-portal/about/en/`).

**Findings**
- A is scientifically sound and has direct USDA definition candidates, but the current Source/EU chain is broad and non-pinpointed.
- B has direct NRCS/FAO support candidates, but the current EU does not identify which soil properties support which mechanisms.
- C is an essential transfer boundary; soil profiles, horizons, texture, drainage and biological/chemical conditions are spatially variable. A general portal is not evidence for a specific field or depth.
- Context and Scope target A only. B/C require claim-specific applicability boundaries.
- Soil classification, sampling and site-specific agronomic decisions must not be inferred from a general introductory definition.

**Decision: HOLD — A/B/C.** Strong authoritative source candidates exist; complete exact EUs and Claim-specific Context/Scope. Do not turn the general slice into a field-specific diagnosis or fertilizer prescription.

### 2. soil-science-basics — FAO source closely matches all three Claims; independent evidence and locators remain

**Current Claims**
- A — `CLM_SOIL_SCIENCE_BASICS_A@1`: soil properties include physical, chemical and biological characteristics that vary among soils and under management.
- B — `CLM_SOIL_SCIENCE_BASICS_B@1`: soil quality has inherent and dynamic characteristics.
- C — `CLM_SOIL_SCIENCE_BASICS_C@1`: soil functions connect soil properties with productivity, water regulation, nutrient cycling, biodiversity and ecosystem services.

**Evidence chain**
- `SRC_SOIL_SCIENCE_BASICS@1` points to FAO “Soil properties” (`https://www.fao.org/soils-portal/data-hub/soil-properties/en/`).
- FAO explicitly states that soil quality varies and responds differently to management inputs; it identifies physical, chemical and biological properties and distinguishes inherent from dynamic characteristics. This is a direct match for A/B.
- FAO Soils Portal “Why soils matter” (`https://www.fao.org/soils-portal/about/en/`) describes soil functions supporting plant growth, water supply/regulation, biodiversity, carbon and nutrient cycles. This is a relevant companion source for C, but it is not currently linked as a second Source record in this slice.
- `EU_SOIL_SCIENCE_BASICS_A/B/C@1` descriptions are generic and do not provide exact locators.
- Context and Scope target A only.

**Findings**
- A/B have unusually strong direct alignment with the current FAO page.
- C is supported by related FAO soil-function material, but the present single Source record is the properties page. The function list should be mapped to exact source sections, not treated as fully proven by the source identity alone.
- “Soil quality” and “soil health” are related but not interchangeable without defining the framework and measurement context. A single indicator or crop yield cannot stand in for all soil functions.
- Independent source diversity is not yet represented in the current slice.

**Decision: HOLD — A/B/C pending exact EU locators, claim-specific boundaries and independent corroboration.** This is a strong source-fit slice, not a substantive content failure.

### 3. soil-microbiology-basics — source is promising but generic EUs obscure which biological mechanisms are established

**Current Claims**
- A — `CLM-SOIL_MICROBIOLOGY_BASICS-A@1`: soil contains a complex community of microorganisms and other organisms.
- B — `CLM-SOIL_MICROBIOLOGY_BASICS-B@1`: soil microorganisms participate in decomposition of organic matter and nutrient cycling.
- C — `CLM-SOIL_MICROBIOLOGY_BASICS-C@1`: soil biodiversity is part of soil-ecosystem functioning.

**Evidence chain**
- `SRC-SOIL_MICROBIOLOGY_BASICS@1` points to USDA NRCS “Soil Health Starter Kit” (`https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil-Health-Starter-Kit-reduced.pdf`).
- `EU-SOIL_MICROBIOLOGY_BASICS-A/B/C@1` all point to the same PDF and contain only generic descriptions.
- USDA NRCS “Soil Health” (`https://www.nrcs.usda.gov/conservation-basics/soil/soil-health`) describes soil as a living ecosystem containing billions of microorganisms.
- USDA NRCS “Rangeland Soil Health — Soil Biota” (`https://www.nrcs.usda.gov/sites/default/files/2024-05/Rangeland%20Soil%20Health%20Soil%20Biota%20SD-FS-85b%205-9-24.pdf`) identifies bacteria, fungi, algae and soil animals and describes the soil food web.
- FAO “Why soils matter” describes soil organisms' roles in decomposition and carbon, nutrient and hydrological cycles.

**Findings**
- A is supported at a broad level by USDA's living-soil and soil-biota materials.
- B is plausible and well supported by the FAO/NRCS candidate materials, but the current EU does not identify the decomposition or nutrient-cycling passage.
- C is broader than microbial diversity alone: soil biodiversity includes bacteria, fungi, archaea, protists and soil fauna; the ecological role differs by organism, soil and conditions.
- The current Source is a starter kit, not a pinpointed specialist review of soil microbiology. A/B/C need exact pages/figures/sections and an independent scientific source.
- Context and Scope target A only.

**Decision: HOLD — A/B/C.** Preserve the USDA source; add exact locators and boundaries, and distinguish microbial communities from the wider soil-biota community. Do not infer that a general soil-health claim establishes the presence or safety of any particular organism.

### 4. plant-biology-basics — exact topical fit, but OpenStax AI-use restriction is material

**Current Claims**
- A — `CLM-PLANT_BIOLOGY_BASICS-A@1`: plants move water, dissolved substances and photosynthetic products between organs.
- B — `CLM-PLANT_BIOLOGY_BASICS-B@1`: xylem and phloem are the main transport tissues in plants.
- C — `CLM-PLANT_BIOLOGY_BASICS-C@1`: transpiration, water potential and stomatal regulation affect water transport.

**Evidence chain**
- `SRC-PLANT_BIOLOGY_BASICS@1` points to OpenStax Biology 2e §30.5 “Transport of Water and Solutes in Plants” (`https://openstax.org/books/biology-2e/pages/30-5-transport-of-water-and-solutes-in-plants`).
- The live section directly explains xylem and phloem transport, water potential, transpiration, stomatal regulation and photosynthate movement. The content is a strong topical match for A/B/C.
- `EU-PLANT_BIOLOGY_BASICS-A/B/C@1` use generic descriptions and do not identify the relevant paragraphs/figures.
- Context and Scope target A only.
- **Material rights restriction:** OpenStax Biology 2e pages state that textbook material must not be used for training or otherwise ingested into LLMs or generative-AI offerings without prior written permission. The textbook's ordinary Creative Commons reuse statement does not override that explicit AI-use restriction. This is a blocker for AI-mediated processing unless written permission is obtained or a source with compatible terms is selected.

**Findings**
- The source is well matched scientifically, but its terms restrict AI ingestion. Do not treat the public URL as permission for AI-based extraction, analysis, summarization or corpus generation.
- EUs must be pinpointed if the source is used in an authorized workflow.
- Claim A's “dissolved substances” is broad; the record should distinguish xylem water/mineral transport from phloem transport of photosynthates.
- Claim C's mechanisms depend on species, environment and plant condition; it is an introductory mechanism, not a crop-watering prescription.

**Decision: HOLD — A/B/C.** Resolve the OpenStax AI-use restriction first; then add exact locators, independent compatible corroboration and Claim-specific boundaries. No public INCLUDE.

### 5. plant-physiology-basics — current chapter introduction does not substantiate the detailed physiology Claims

**Current Claims**
- A — `CLM-PLANT_PHYSIOLOGY_BASICS-A@1`: plants carry out photosynthesis and other metabolic processes.
- B — `CLM-PLANT_PHYSIOLOGY_BASICS-B@1`: water and dissolved-substance transport is associated with plant vascular tissues.
- C — `CLM-PLANT_PHYSIOLOGY_BASICS-C@1`: physiological processes depend on environmental conditions including light, water and temperature.

**Evidence chain**
- `SRC-PLANT_PHYSIOLOGY_BASICS@1` points to OpenStax Biology 2e Chapter 30 Introduction (`https://openstax.org/books/biology-2e/pages/30-introduction`).
- The live chapter introduction is a chapter overview. It notes that plants use photosynthesis and that vascular systems supply water/minerals and export photosynthetic products, but it is not a direct source for the full scope of all three physiology Claims.
- §30.5 “Transport of Water and Solutes in Plants” is a more direct candidate for B and parts of C; it does not alone cover the full range of plant physiology or all environmental factors in C.
- `EU-PLANT_PHYSIOLOGY_BASICS-A/B/C@1` are generic. Context and Scope target A only.
- The same OpenStax LLM/generative-AI ingestion restriction described in §52.4 applies to Chapter 30 and §30.5.

**Findings**
- A is too broad for a chapter introduction as its only evidence; photosynthesis and metabolism require direct sections.
- B has a stronger candidate in §30.5, but the existing Source record is the chapter introduction.
- C lists light, water and temperature without a claim-specific mapping to plant response mechanisms.
- The source identity (“plant physiology”) is more comprehensive than the specific chapter URL supports.

**Decision: HOLD — A/B/C.** Source identity/scope mismatch and AI-use restriction must be resolved. Do not create substitute Evidence Use from a candidate section without an authorized source-use path.

### 6. plant-pathology-basics — APS source directly supports the three introductory Claims; exact locators and independent evidence remain

**Current Claims**
- A — `CLM-PLANT_PATHOLOGY_BASICS-A@1`: plant pathology studies plant diseases and disorders.
- B — `CLM-PLANT_PATHOLOGY_BASICS-B@1`: causes may include living pathogens and nonliving environmental factors.
- C — `CLM-PLANT_PATHOLOGY_BASICS-C@1`: plant pathology combines botany, microbiology, ecology, genetics, biochemistry and physiology.

**Evidence chain**
- `SRC-PLANT_PATHOLOGY_BASICS@1` points to American Phytopathological Society “What Is Phytopathology?” (`https://www.apsnet.org/careers/Pages/WhatisPhytopathology.aspx`).
- The live APS page explicitly describes plant pathology as the study of plant disease; identifies living pathogens and nonliving agents such as pollutants, nutrient imbalances and environmental factors; and lists the interdisciplinary fields used by plant pathologists.
- `EU-PLANT_PATHOLOGY_BASICS-A/B/C@1` point to the APS source but have generic descriptions without precise locators.
- Context and Scope target A only. A second independent source is not linked.

**Findings**
- A/B/C have a strong direct source fit. B correctly distinguishes biotic pathogens from abiotic disorders; do not imply every plant disorder is infectious.
- Claim C is supported by the APS interdisciplinary list, but the exact list should be preserved and not expanded into an unrestricted set of specialties.
- The slice is introductory and must not be interpreted as plant diagnosis, pesticide selection, pathogen culturing, or operational plant-disease treatment advice.
- Independent evidence and Context/Scope for B/C remain open.

**Decision: HOLD — A/B/C pending exact EUs, independent corroboration and Claim-specific boundaries.** This is a strong candidate for targeted maturation.

### 7. seed-storage-basics — useful two-source architecture, but one Source URL is unresolved and the current claims are crop-specific

**Current Claims**
- `CLM-SEED-APPLICABILITY@1`: storage conditions and expected viability depend on seed type and condition; generic cool/dry advice does not replace crop-specific requirements.
- `CLM-SEED-DRY-STORAGE@1`: suitable storage conditions, including humidity control, matter for seed viability.
- `CLM-SEED-LABEL@1`: saved seeds should be identified and labelled to preserve crop and lot information.

**Evidence chain**
- `SRC-UMN-SEED-STORAGE@1` points to University of Minnesota Extension “Saving vegetable seeds” (`https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/saving-vegetable-seeds`). It directly recommends dry/cool storage and labelling by name, variety and collection date; it also notes that seed longevity and handling differ by crop.
- `SRC-USDA-SEED-STORAGE-2026@1` points to `https://www.nrcs.usda.gov/plant-materials/using-seed-to-save-seeds`. The URL was not accessible during this live check and did not yield a matching indexed page. Its identity “USDA — Seed Saving” therefore remains unverified at the stated locator.
- `EU-SEED-DRY-STORAGE@1` and `EU-SEED-LABEL@1` point to the unverified USDA URL. `EU-SEED-APPLICABILITY@1` points to UMN Extension.
- Context and Scope target the dry-storage Claim and explicitly exclude breeding, phytosanitary certification and crop-specific advice outside the source.

**Findings**
- UMN Extension directly supports the core of all three Claims for the vegetable-seed context, including cool/dry storage and labelling.
- The exact temperature and viability advice is crop- and seed-condition-specific; it must not be generalized to all crop, tree, wild, orthodox or recalcitrant seeds.
- The USDA Source URL is a material provenance/availability problem. Do not treat the Source identity as verified until the URL resolves to the intended USDA material or is replaced by an exact stable source.
- The two-source structure is not yet proven to be genuinely independent for the two Claims linked to the unresolved USDA URL.

**Decision: HOLD — all three Claims.** Preserve the UMN Extension evidence. Verify or replace the USDA URL and relink only after exact source identity, locator and claim fit are confirmed. No universal seed-storage temperature or longevity rule is established by this slice.

### 8. ecotoxicology-basics — EPA source fits the subject but EUs are generic and Claim C needs methodological boundaries

**Current Claims**
- A — `CLM-ECOTOXICOLOGY_BASICS-A@1`: ecotoxicology examines effects of chemical substances and other stressors on organisms, populations and ecosystems.
- B — `CLM-ECOTOXICOLOGY_BASICS-B@1`: effects depend on exposure, organism characteristics, environmental conditions and stressor properties.
- C — `CLM-ECOTOXICOLOGY_BASICS-C@1`: evidence is bounded by species, endpoints, exposure conditions and study design.

**Evidence chain**
- `SRC-ECOTOXICOLOGY_BASICS@1` points to US EPA “Ecological effects” (`https://www.epa.gov/chemical-research/ecological-effects`).
- EPA ecological-risk-assessment materials (`https://www.epa.gov/risk/conducting-ecological-risk-assessment`) explain exposure profiles, stressor-response relationships, receptors, assessment endpoints and uncertainty; they are strong candidates for B/C.
- `EU-ECOTOXICOLOGY_BASICS-A/B/C@1` use generic descriptions without exact locators.
- Context and Scope target A only. A second independent source is not linked.

**Findings**
- A is broadly aligned with ecotoxicology, but the current EPA page identity should be checked against the intended breadth “chemical substances and other stressors”; ecological risk assessment can include chemical, physical and biological stressors, while the named ecological-effects page may be narrower.
- B/C have strong EPA methodological support candidates, but no claim-level locator or formal boundary exists in the current EUs.
- Species, life stage, endpoint, exposure route/duration, environmental matrix and study design can change conclusions. Results from one test species or laboratory endpoint must not be silently generalized to all ecosystems or human health.
- The slice is educational; it does not establish safe concentrations, remediation thresholds or site-specific regulatory decisions.

**Decision: HOLD — A/B/C.** Add precise EPA passages, a compatible independent source and claim-specific Context/Scope. Keep ecotoxicological effects distinct from human toxicology and regulatory risk thresholds.

### 9. food-safety-basics — FDA track is direct; CDC track is correctly kept separate

**Current Claims**
- A — `CLM-FOOD_SAFETY_BASICS-A@1`: basic food-safety measures include cleaning, separation, adequate cooking and proper chilling.
- B — `CLM-FOOD_SAFETY_BASICS-B@1`: separating raw food from ready-to-eat food reduces cross-contamination risk.
- C — `CLM-FOOD_SAFETY_BASICS-C@1`: specific temperature, storage and control requirements depend on product, process and applicable rules.

**Evidence chain**
- `SRC-FOOD_SAFETY_BASICS@1` points to FDA “Food Safety at Home” (`https://www.fda.gov/consumers/womens-health-topics/food-safety-home`). The live FDA page directly describes the four steps: Clean, Separate, Cook and Chill; it gives handling examples, cooking temperatures and prompt refrigeration guidance.
- `EU-FOOD_SAFETY_BASICS-A/B/C@1` link to FDA but are generic and do not identify exact sections.
- A separate CDC track exists: `CLM_FOOD_SAFETY_CDC_A@1` and `EU_FOOD_SAFETY_CDC_A@1` link CDC’s prevention page (`https://www.cdc.gov/food-safety/prevention/index.html`) to a distinct Claim about internal cooking temperatures and thermometers.
- README explicitly states that CDC evidence is not represented as independent corroboration of FDA Claims A/B/C. This separation is correct and must be preserved.

**Findings**
- FDA directly supports A/B and provides useful context for C.
- The CDC record is a separate, bounded Claim; it must not be counted as a second evidence source for A/B/C.
- US temperature recommendations and regulatory references must not be presented as universal legal requirements. The relevant jurisdiction, food type and current official guidance matter.
- Context and Scope target A only; B/C need claim-specific boundaries and exact locators.
- No food-safety advice should imply that smell, appearance or taste can reliably establish safety.

**Decision: HOLD — A/B/C pending EU precision and Claim-specific Context/Scope.** Preserve the explicitly separate CDC Claim and README boundary. Do not merge the two evidence tracks or inflate evidence diversity.

### 10. food-preservation-basics — evidence is mostly food-handling safety, not preservation technologies

**Current Claims**
- A — `CLM-FOOD_PRESERVATION_BASICS-A@1`: food safety requires controlling factors that support growth or transfer of hazardous microorganisms.
- B — `CLM-FOOD_PRESERVATION_BASICS-B@1`: safety depends on handling, storage, time, temperature and product characteristics.
- C — `CLM-FOOD_PRESERVATION_BASICS-C@1`: general preservation information does not replace product- and method-specific authoritative safety requirements.

**Evidence chain**
- `SRC-FOOD_PRESERVATION_BASICS@1` points to USDA FSIS “Food Safety Basics” (`https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics`).
- `SRC_FDA_FOOD_STORAGE_SAFETY@1` points to FDA “Are You Storing Food Safely?” (`https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely`).
- EUs A/B/C point to USDA FSIS; an additional FDA EU corroborates B. Both sources are relevant to food handling and storage safety, but the EUs have no exact locators.
- Context and Scope target A only. Existing `REL_M3_FOOD_PRESERVATION_SAFETY@1` links Claim B to `CLM-FOOD_SAFETY_BASICS-A@1`; preserve the historical relation.

**Findings**
- The current Claims are principally about safe handling and storage, not the broader set of preservation technologies implied by “food preservation” (e.g. drying, freezing, heat processing, fermentation, curing and packaging).
- USDA FSIS/FDA directly support safe handling and storage, especially B; they do not establish a comprehensive taxonomy or validated procedures for every preservation method.
- Claim C is a valid boundary statement, but it should not be mistaken for a substantive description of preservation science.
- **Safety boundary:** do not infer safe home-canning, low-acid food processing, fermentation recipes, shelf stability, toxin prevention or storage duration from general “Food Safety Basics” pages. Method-, acidity-, product-, container- and process-specific validated guidance is required.

**Decision: HOLD — A/B/C.** This is a scope/identity mismatch between the slice title and its current Claims. Keep the existing FDA corroboration and M3 relation; do not add preservation procedures or infer safe methods from generic handling sources.

### 11. food-fermentation-basics — FAO source directly covers the descriptive Claims; no independent evidence and no validated process guidance

**Current Claims**
- A — `CLM-FOOD_FERMENTATION_BASICS-A@1`: food fermentation uses microorganisms and their metabolic activity to transform food materials under suitable conditions.
- B — `CLM-FOOD_FERMENTATION_BASICS-B@1`: fermented foods include diverse products produced in different regions from different raw materials and processes.
- C — `CLM-FOOD_FERMENTATION_BASICS-C@1`: different microorganism groups participate in food fermentations, and dominant organisms depend on product and fermentation conditions.

**Evidence chain**
- `SRC-FOOD_FERMENTATION_BASICS@1` points to FAO “Basic Principles of Fermentation” (`https://www.fao.org/4/x0560e/x0560e07.htm`).
- The FAO chapter explicitly describes diversity of fermented foods across regions and raw materials and lists common microorganism groups involved in food fermentations. It is a direct source candidate for A/B/C.
- `EU-FOOD_FERMENTATION_BASICS-A/B/C@1` all point to this one source with generic descriptions and no precise section locator.
- Context and Scope target A only; README describes a single-source, three-Claim slice.

**Findings**
- A/B/C have good topical alignment with the FAO chapter; exact section 2.1 (“The diversity of fermented foods”) and section 2.2 (“Organisms responsible for food fermentations”) should be used as candidate locators.
- The source is older and descriptive; it should not be treated as current validation of every modern process or safety control.
- The Claims are descriptive, not operational. Presence of fermentation microorganisms does not establish that a particular batch is safe, shelf-stable, pathogen-free or toxin-free.
- Independent current food-science/food-safety evidence remains absent.
- **Safety boundary:** no improvised fermentation parameters, pathogen culture, inoculum propagation or unsafe preservation instructions should be inferred from this introductory slice. Use validated product-specific authoritative processes for practical food production.

**Decision: HOLD — A/B/C pending exact locators, independent current corroboration and explicit safety boundaries.** The FAO source is a strong historical descriptive reference, not a universal process-validation standard.

### 12. food-distribution-basics — two sources exist, but FAO is broad and WFP source does not yet establish the full humanitarian chain

**Current Claims**
- A — `CLM-FOOD_DISTRIBUTION_BASICS-A@1`: food distribution links production and other food-system stages with consumers.
- B — `CLM-FOOD_DISTRIBUTION_BASICS-B@1`: transport, storage, infrastructure, markets, rules and food losses influence distribution.
- C — `CLM-FOOD_DISTRIBUTION_BASICS-C@1`: local food availability is not determined only by production volume.
- D — `CLM-FOOD_DISTRIBUTION_BASICS-D@1`: a humanitarian food chain may include procurement, storage, transport and delivery to final points.

**Evidence chain**
- `SRC-FOOD_DISTRIBUTION_BASICS@1` points to FAO Food Systems (`https://www.fao.org/food-systems/en/`), a broad systems-level source.
- `SRC-FOOD_DISTRIBUTION_WFP@1` points to WFP “2024 Procurement Infographics” (`https://www.wfp.org/publications/2024-procurement-infographics`).
- `EU-FOOD_DISTRIBUTION_BASICS-A/B/C@1` point to FAO with generic descriptions. `EU-FOOD_DISTRIBUTION_BASICS-D@1` points to WFP with a generic description.
- WFP's procurement infographic page describes what WFP purchases, where supplies come from and how procurement supports humanitarian operations. The current page may be found under “Supply chain and delivery procurement infographics” (`https://friends.wfp.org/publications/supply-chain-and-delivery-procurement-infographics`). The current record's URL and “Supply Chain” source identity should be reconciled; procurement graphics alone do not necessarily substantiate the complete storage–transport–delivery sequence.
- Context and Scope target A only. README correctly warns that live routing, procurement, storage, safety, regulation and emergency decisions require current operational data.

**Findings**
- A is broadly consistent with the FAO food-systems concept but the current source is not a claim-specific distribution reference.
- B requires distinct evidence for infrastructure, cold/storage, transport, market rules and food losses. A broad food-system portal does not substantiate every item.
- C is a systems-level insight that requires evidence about access, affordability, distribution and market/infrastructure constraints; production volume alone is not a sufficient proxy for availability or access.
- D is only partly corroborated by the WFP procurement source as currently identified. Verify the exact current WFP source, and add sources specifically covering warehousing, transport, last-mile delivery and humanitarian logistics.
- Humanitarian supply-chain descriptions are not live operational plans; do not infer routes, stock levels, procurement suitability or safe storage without current field data.

**Decision: HOLD — A/B/C/D.** Preserve the two-source structure, but resolve WFP source identity/URL, provide exact locators and strengthen Claim-level evidence. No operational logistics instructions are authorized.

### 13. Cross-slice boundaries and relation audit

**A. Soil / soil science / soil microbiology**
- These three slices overlap but have distinct potential roles: introductory soil composition and variability; soil properties/quality/functions; soil microbial and broader soil-biota communities.
- Avoid duplicate Claims that simply restate “soil contains organisms” or “soil properties vary”. Each slice should maintain its own unique explanatory level.
- A relation from soil properties to soil microbiology should name the exact versioned Claims and the specific property/process link (e.g. biological indicators or nutrient cycling); topical adjacency alone is not sufficient.

**B. Plant biology / plant physiology**
- Plant-biology-basics currently concentrates on vascular transport and water movement; plant-physiology-basics covers photosynthesis, metabolism, transport and environmental response.
- Their Claims B overlap on water/solute transport. The distinction should be explicit: plant anatomy/transport tissues versus integrated physiological mechanisms. No merge or rewrite is authorized.
- Both current Source records point to OpenStax Biology 2e and are subject to the same explicit LLM/generative-AI ingestion restriction without prior written permission.

**C. Plant pathology / soil microbiology / food safety**
- Plant pathology includes biotic pathogens and abiotic disorders. Soil microbiology is not equivalent to plant pathology; not every soil microorganism is a pathogen.
- Plant disease evidence must not be converted into human foodborne disease claims. Crop contamination, post-harvest pathogens and mycotoxins require distinct food-safety evidence.

**D. Seed storage / food preservation**
- Seed viability and food safety are different preservation domains. A storage recommendation for viable planting seed is not a food-storage safety recommendation; food preservation methods cannot be transferred to seed storage.
- Seed storage's current USDA URL requires verification. UMN Extension evidence is crop-specific, not a universal seed-bank standard.

**E. Food safety / food preservation / fermentation**
- Food-safety basics describes handling safeguards; food-preservation-basics currently focuses on handling/storage rather than preservation technologies; food-fermentation-basics describes microbial transformation.
- Fermentation is one food-processing/preservation domain, but the existence of fermentation does not establish safety. Validated process requirements are distinct from introductory microbial descriptions.
- Preserve the existing M3 relation between food-preservation and food-safety Claims; do not broaden it into a general equivalence.

**F. Food distribution / food systems / humanitarian logistics**
- Food distribution is a component of food systems, not the whole food system.
- Humanitarian procurement is not equivalent to the complete supply chain, and global institutional infographics do not substitute for live operational logistics data.
- No new Relations are created. Any future link must be typed, versioned and supported by a precise dependency.

### 14. Consolidated dispositions

| Slice | Disposition | Main open issue |
|---|---|---|
| soil-basics | HOLD A/B/C | Generic USDA portal EUs; exact locators and B/C boundaries |
| soil-science-basics | HOLD A/B/C | Strong FAO fit; exact locators, independent source, B/C boundaries |
| soil-microbiology-basics | HOLD A/B/C | USDA starter-kit PDF needs pinpoint locators and independent evidence |
| plant-biology-basics | HOLD A/B/C | Strong OpenStax topical fit; explicit AI-ingestion restriction |
| plant-physiology-basics | HOLD A/B/C | Chapter-introduction/source mismatch; OpenStax AI-ingestion restriction |
| plant-pathology-basics | HOLD A/B/C | Strong APS fit; exact locators and independent source |
| seed-storage-basics | HOLD all three | USDA source URL unresolved; UMN evidence is crop-specific |
| ecotoxicology-basics | HOLD A/B/C | EPA EUs generic; methodological boundaries and second source |
| food-safety-basics | HOLD A/B/C | FDA EUs generic; CDC separate Claim correctly not a second source for A/B/C |
| food-preservation-basics | HOLD A/B/C | Current scope is handling/storage safety, not preservation technologies |
| food-fermentation-basics | HOLD A/B/C | Good FAO descriptive fit; no independent evidence or process validation |
| food-distribution-basics | HOLD A/B/C/D | WFP source identity/URL and full-chain support unresolved |

**Overall result:** all twelve slices remain HOLD for first-edition candidate closure; no public INCLUDE is granted. Strongest source-fit candidates are soil-science-basics, plant-pathology-basics, food-safety-basics and food-fermentation-basics. Plant-biology-basics is also scientifically well matched but blocked for AI-mediated use by the OpenStax terms. The most material source-identity defects are plant-physiology-basics, seed-storage-basics and food-distribution-basics. Food-preservation-basics has a title/content scope mismatch. Existing CDC separation in food-safety-basics and existing M3 food-preservation relation are preserved.

**Change control:** no canonical JSON, README files, Relations, Assessments or publication states changed. Only this controlling audit register is extended.


---

## §53 — Food security, food science and nutrition evidence-chain follow-up (2026-11-19)

**Audit scope:** four adjacent Part I slices were inspected at exact record level: all 42 JSON records in `food-security-basics` (12), `food-science-basics` (9), `nutrition-basics` (12) and `nutrition-science-basics` (9). This is a targeted deepening of existing filename/exact-record screens, not a new M13 batch. Claims, Evidence Use, Source, Context and Scope records were read from the PR branch. No canonical record was changed.

**Repository boundary:** PR #22 branch `mvp-public-contribution-design-2026-10-11`, starting HEAD `257a3b25e0f0c3822b3bddd428f34ff28c81ddc9`. Only this controlling register is extended. No main, canonical JSON, README, Relation, Assessment, publication state or allowlist change is authorized.

### 1. food-security-basics — two authoritative sources fit the subject, but all four Evidence Use records lack pinpoint locators

**Current Claims**
- A — `CLM-FOOD_SECURITY_BASICS-A@1`: food security includes physical and economic access to sufficient, safe and nutritious food.
- B — `CLM-FOOD_SECURITY_BASICS-B@1`: assessment considers availability and stability of food supplies alongside access.
- C — `CLM-FOOD_SECURITY_BASICS-C@1`: information systems and early warning support understanding food-security conditions and decision-making.
- D — `CLM-FOOD_SECURITY_BASICS-D@1`: household food security means all members have access at all times to enough food for an active and healthy life.

**Evidence chain**
- `SRC-FOOD_SECURITY_BASICS@1` identifies the FAO *Handbook for Defining and Setting up a Food Security Information and Early Warning System* at `https://www.fao.org/4/x8622e/x8622e04.htm`.
- `EU-FOOD_SECURITY_BASICS-A/B/C@1` correctly point to the FAO Source and to the corresponding Claims, but each description is generic. No section, paragraph or exact passage is recorded.
- The FAO page section 1.4 defines food security in terms of physical/economic access for all people at all times to sufficient, safe and nutritious food, and identifies availability, stability, access and biological utilization. The handbook's forecasting/steering and FSIEWS framework sections are direct candidates for Claim C.
- `SRC-FOOD_SECURITY_USDA@1` identifies USDA ERS *Food Security in the U.S. — Measurement* at `https://ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/measurement`.
- `EU-FOOD_SECURITY_BASICS-D@1` links the USDA Source to Claim D. USDA ERS directly defines household food security as access by all members at all times to enough food for an active, healthy life.
- `CTX-FOOD_SECURITY_BASICS@1` and `SCP-FOOD_SECURITY_BASICS@1` both target Claim A only; B/C/D have no corresponding claim-specific Context/Scope pair in this slice.

**Findings**
- A has direct FAO support. Preserve the distinction between the four food-security dimensions; do not reduce food security to aggregate food production or supply.
- B is consistent with the FAO framework, but its Evidence Use needs an exact locator for availability/stability and access. The FAO text also includes biological utilization; the current Claim's wording should not be read as an exhaustive four-dimension definition.
- C has a particularly good source fit: the source is explicitly a handbook for food-security information and early-warning systems. Identify the exact forecasting/steering and FSIEWS passages in the EU rather than relying on the handbook title.
- D has a direct USDA definition match. Its operational measurement context is the United States; do not present the USDA survey method or classification thresholds as universal global standards.
- The current two-source architecture is meaningful but not independent corroboration of every Claim: FAO supports A/B/C, USDA supports D. Do not count source quantity as cross-support where no EU link exists.
- Claim-level applicability boundaries are incomplete because Context/Scope target A only. Specific territory, time period, household survey, market conditions and emergency decisions require current local data.

**Decision: HOLD — A/B/C/D.** Strong source fit, especially A/C/D. Add pinpoint locators to all four EUs, retain the FAO four-dimension distinction, and add Claim-specific Context/Scope for B/C/D. No live food-security assessment or policy recommendation is authorized.

### 2. nutrition-basics — NIH/NIEHS and WHO directly fit the Claims; generic Evidence Use and single-target Context/Scope remain

**Current Claims**
- A — `CLM-NUTRITION_BASICS-A@1`: nutrition includes consumption, absorption and use of nutrients from food.
- B — `CLM-NUTRITION_BASICS-B@1`: macronutrients include proteins, carbohydrates and fats; micronutrients include vitamins and minerals.
- C — `CLM-NUTRITION_BASICS-C@1`: excess or deficiency of some nutrients can affect health.
- D — `CLM-NUTRITION_BASICS-D@1`: WHO describes healthy-diet principles as adequacy, balance, moderation and diversity, with diets depending on individual and cultural conditions.

**Evidence chain**
- `SRC-NUTRITION_BASICS@1` identifies NIH/NIEHS *Nutrition, Health, and Your Environment* at `https://www.niehs.nih.gov/health/topics/nutrition`.
- `EU-NUTRITION_BASICS-A/B/C@1` point to the NIH/NIEHS Source and their matching Claims. Their material descriptions are generic and do not identify the definition, nutrient classification or health-effects passages.
- The current NIEHS page defines nutrition as consuming, absorbing and using nutrients; identifies proteins, carbohydrates and fats as macronutrients; and describes nutrient deficiency/excess as capable of affecting health. It is a strong direct source fit for A/B/C.
- `SRC-NUTRITION_WHO@1` identifies WHO *Healthy diet* at `https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet`.
- `EU-NUTRITION_BASICS-D@1` links WHO to Claim D. The WHO page describes adequacy, balance, moderation and diversity as four core principles.
- `CTX-NUTRITION_BASICS@1` and `SCP-NUTRITION_BASICS@1` target Claim A only. B/C/D have no claim-specific Context/Scope pair.

**Findings**
- A/B/C are closely matched to the NIEHS page. The source supports general educational definitions, not individualized nutrient requirements, deficiency diagnosis or supplement dosing.
- D has a direct WHO fit. Keep the four principles together and preserve WHO's framing as population-level healthy-diet guidance; do not convert the page into a personalized diet prescription.
- No exact locators are present in any of the four EUs. Add the NIEHS definition, nutrient-classification and deficiency/excess passages separately, and the WHO principles passage for D.
- Context and Scope are only attached to A. Claim-specific applicability should cover life stage, health status, dietary pattern, cultural context and the limits of general-population guidance.
- The NIH/NIEHS and WHO tracks support different Claims. They are not automatically two-source triangulation for all four Claims.

**Decision: HOLD — A/B/C/D.** Source identity and claim fit are strong; close the locator debt and add per-Claim Context/Scope for B/C/D. No individual medical, therapeutic or supplement advice is established.

### 3. food-science-basics — source title overstates the locator; OpenStax AI-ingestion restriction is a release blocker

**Current Claims**
- A — `CLM-FOOD_SCIENCE_BASICS-A@1`: the slice describes basic concepts of the subject area and their relationships.
- B — `CLM-FOOD_SCIENCE_BASICS-B@1`: interpretation requires attention to source, context and applicability limits.
- C — `CLM-FOOD_SCIENCE_BASICS-C@1`: generalized information does not replace specialist review where conclusions depend on conditions, measurements or professional judgment.

**Evidence chain**
- `SRC-FOOD_SCIENCE_BASICS@1` identifies “OpenStax — Food Science” but points only to Biology 2e §34.1, *Nutrition and Energy Production*: `https://openstax.org/books/biology-2e/pages/34-1-nutrition-and-energy-production`.
- `EU-FOOD_SCIENCE_BASICS-A/B/C@1` all link the same Source and use only generic descriptions; no passage or subsection is identified.
- `CTX-FOOD_SCIENCE_BASICS@1` and `SCP-FOOD_SCIENCE_BASICS@1` target Claim A only.
- OpenStax Biology 2e reuse terms explicitly prohibit use for training or ingestion into LLMs/generative-AI offerings without prior written permission. The ordinary CC BY-NC-SA reuse notice does not override that separate AI-use restriction.

**Findings**
- The Source identity “Food Science” is materially broader than the linked §34.1 nutrition/energy-production page.
- Claim A is self-referential to the slice rather than a substantive food-science proposition. Claims B/C are general editorial caveats; the current source/EU chain does not demonstrate that §34.1 supports those propositions.
- The AI-ingestion restriction prevents treating this publicly accessible textbook section as freely available for AI-mediated extraction or corpus processing. No additional OpenStax content was ingested for this screen.
- The slice needs a compatible, properly scoped food-science source and substantive Claims before it can serve as a useful first-edition subject entry.

**Decision: HOLD — A/B/C.** Do not ingest or reuse OpenStax content in an AI-mediated workflow without prior written permission. Resolve Source identity/scope, replace or authorize the source, and substantively review the Claims/EUs through an authorized process. No new source or rewritten Claim is added here.

### 4. nutrition-science-basics — NIH ODS portal is not a pinpoint source for the broad discipline-level Claims

**Current Claims**
- A — `CLM_NUTRITION_SCIENCE_BASICS_A@1`: nutrition science studies relationships between nutrients/food components, human health and physiological function.
- B — `CLM_NUTRITION_SCIENCE_BASICS_B@1`: nutrients participate in energy metabolism, tissue maintenance and regulation of physiological functions.
- C — `CLM_NUTRITION_SCIENCE_BASICS_C@1`: nutrition guidance depends on dietary patterns, individual characteristics, life stage, health status and evidence quality.

**Evidence chain**
- `SRC_NUTRITION_SCIENCE_BASICS@1` identifies the NIH Office of Dietary Supplements and points to its general homepage: `https://ods.od.nih.gov/`.
- `EU_NUTRITION_SCIENCE_BASICS_A/B/C@1` correctly link each Claim to that Source but provide only generic descriptions (“Source supports the claim within the stated scope”). No fact sheet, section, table or passage is identified.
- `CTX_NUTRITION_SCIENCE_BASICS@1` and `SCP_NUTRITION_SCIENCE_BASICS@1` target Claim A only.
- The ODS homepage is a portal to dietary-supplement information and fact sheets; its identity alone does not substantiate the broad scope of nutrition science, the full set of physiological roles in B, or all the evidence/applicability factors in C.

**Findings**
- A is a plausible discipline-level description, but a general ODS portal is not a direct, claim-specific source for the breadth of nutrition science.
- B requires specific evidence for energy metabolism, tissue maintenance and physiological regulation; one general supplement portal cannot be assumed to establish all three mechanisms.
- C combines evidence quality, dietary patterns, life stage and health status. These require distinct, precise sources or a clearly bounded claim; the current single Source/EU structure does not demonstrate them.
- The slice is conceptually adjacent to nutrition-basics but should not duplicate its basic definitions. Its role should be the scientific mechanisms and evidence framework, not individualized dietary advice.
- The filename-to-record-ID underscore convention is internally consistent across the three Claims, EUs, Context and Scope; it is not treated as a broken reference. Exact IDs and version 1 references resolve within the slice.

**Decision: HOLD — A/B/C.** Replace or supplement the generic ODS homepage with exact, compatible sources and pinpoint passages; add Claim-specific Context/Scope for B/C. Do not infer clinical recommendations or supplement efficacy from the portal.

### 5. Cross-slice boundaries and relation audit

- **Food security vs. nutrition:** food security concerns availability, access, stability and utilization at population/household levels; nutrition concerns the intake, absorption and use of nutrients and their relation to health. Neither concept substitutes for the other.
- **Food security vs. food distribution:** aggregate production or availability is not equivalent to household economic/physical access. The USDA household definition is a US measurement context; the FAO handbook provides the broader international framework.
- **Nutrition basics vs. nutrition science:** the former provides introductory nutrient definitions and broad healthy-diet principles; the latter should explain scientific mechanisms and evidence quality. Avoid duplicate generic Claims.
- **Food science vs. food safety/preservation/fermentation:** a general food-science subject entry cannot be established by one narrow nutrition/energy page, and it cannot replace method-specific food-safety evidence. Preserve §52 boundaries for preservation and fermentation.
- No new Relations are created. Existing Relations and prior review decisions remain untouched.

### 6. Consolidated dispositions

| Slice | Records screened | Decision | Main unresolved issue |
|---|---:|---|---|
| food-security-basics | 12 | HOLD A/B/C/D | Four generic EUs; missing per-Claim Context/Scope for B/C/D |
| nutrition-basics | 12 | HOLD A/B/C/D | Four generic EUs; missing per-Claim Context/Scope for B/C/D |
| food-science-basics | 9 | HOLD A/B/C | Source-title/locator mismatch; OpenStax AI-ingestion restriction; Claims are largely meta-level |
| nutrition-science-basics | 9 | HOLD A/B/C | Generic NIH ODS homepage; no pinpoint evidence; missing per-Claim Context/Scope for B/C |

**Overall result:** all 42 inspected records retain their existing canonical content and publication fields. Fourteen Claims remain HOLD for first-edition candidate closure. Strongest source-fit candidates are food-security-basics and nutrition-basics, where FAO/USDA and NIH/NIEHS/WHO respectively match the stated educational Claims but require precise Evidence Use locators and complete applicability boundaries. Food-science-basics has both a material source-scope mismatch and an AI-use rights blocker. Nutrition-science-basics has a source-specificity problem rather than a demonstrated factual contradiction.

**Change control:** this section is an audit finding only. No canonical JSON, README, Relation, Assessment, public allowlist, or publication state is changed. No new M13 batch is started. No public INCLUDE is assigned.


---

## §54 — Human biology and epidemiology evidence-chain follow-up (2026-11-19)

**Audit scope:** exact record-level follow-up of four adjacent Part I slices: `anatomy-basics` (11 JSON records), `physiology-basics` (9), `microbiology-basics` (9), and `epidemiology-basics` (12). All 41 listed records were read at version 1, including Claims, Evidence Use, Sources, Context and Scope. External source pages and reuse notices were checked separately. This deepens the prior §33 screens; it does not claim that all 94 Part I slices have been audited or re-adjudicate unrelated prior work.

**Repository boundary:** PR #22 branch `mvp-public-contribution-design-2026-10-11`, starting HEAD `724a5df5a5db0c7be4ebba35fe9bc0b20509f6fc`. This section records findings only. No canonical JSON, README, Relation, Assessment, public allowlist or publication state is changed.

### 1. anatomy-basics — NIGMS source locator not verified; OpenStax corroboration is narrow and AI-use restricted

**Claims**
- A — `CLM-ANATOMY_BASICS-A@1`: tissues consist of cells organized to perform particular functions.
- B — `CLM-ANATOMY_BASICS-B@1`: organs consist of several tissue types working together.
- C — `CLM-ANATOMY_BASICS-C@1`: organ systems combine organs that interact to perform related functions.

**Evidence chain**
- `SRC-ANATOMY_BASICS@1` identifies NIGMS — *Cells, tissues, organs and systems*, URL `https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx`.
- `EU-ANATOMY_BASICS-A/B/C@1` all link this source to their respective Claims, but each description is generic and contains no section, paragraph or other pinpoint locator.
- The exact NIGMS URL could not be retrieved during this audit. Treat the source as **not verified at the recorded locator**, not as proven nonexistent; the identity/URL needs confirmation or replacement.
- `SRC-OPENSTAX-ANATOMY-2E@1` identifies OpenStax *Anatomy and Physiology 2e — Types of Tissues*, §4.1, URL `https://openstax.org/books/anatomy-and-physiology-2e/pages/4-1-types-of-tissues`.
- `EU-ANATOMY-OPENSTAX-CORROBORATION@1` links that second source only to Claim A. The OpenStax section directly describes tissues as groups of cells, the four broad tissue categories, and the formation of organs from several tissue types. It is a relevant direct source for A and B, but the current EU does not link B and does not establish C's organ-system statement.
- OpenStax's current reuse notice for *Anatomy and Physiology 2e* expressly prohibits use for LLM training or ingestion into generative-AI offerings without prior written permission.

**Findings**
- A and B have clear conceptual fit with OpenStax §4.1, but the recorded EU chain captures only A. Do not silently extend the current corroboration to B/C.
- C needs a source passage that explicitly treats organ systems as interacting organs performing related functions.
- The NIGMS source may be a suitable independent educational reference, but its exact recorded URL was not verified and the EU has no pinpoint locators.
- The OpenStax source is not an unrestricted fallback for AI-mediated ingestion or extraction. The publicly readable page and its CC BY-NC-SA notice do not cancel the separate AI-use permission requirement.
- Context and Scope both target Claim A only; B/C have no claim-specific applicability boundary. This is an educational anatomy slice, not a clinical anatomy or diagnostic reference.

**Decision: HOLD — A/B/C.** Verify or replace the NIGMS locator; add claim-specific pinpoint EU locators; establish independent support for B/C without assuming OpenStax can be ingested absent written permission; add Context/Scope coverage for B/C. No anatomy Claim is promoted.

### 2. physiology-basics — the overview is conceptually relevant but EU locators are generic and the textbook has an AI-use restriction

**Claims**
- A — `CLM-PHYSIOLOGY_BASICS-A@1`: physiology studies organism functions and how structures work together.
- B — `CLM-PHYSIOLOGY_BASICS-B@1`: homeostasis describes maintenance of relatively stable internal conditions.
- C — `CLM-PHYSIOLOGY_BASICS-C@1`: organ systems perform different functions and interact to sustain life.

**Evidence chain**
- `SRC-PHYSIOLOGY_BASICS@1` points to OpenStax *Anatomy and Physiology 2e — 1.1 Overview of Anatomy and Physiology*: `https://openstax.org/books/anatomy-and-physiology-2e/pages/1-1-overview-of-anatomy-and-physiology`.
- `EU-PHYSIOLOGY_BASICS-A/B/C@1` link the matching Claims to this Source but describe only the “overview” generically; none gives a pinpoint paragraph or subsection.
- The linked §1.1 does in fact distinguish anatomy (structure) from physiology (function), describes physiology as the study of body structures and how they work together, and defines homeostasis as steady internal conditions. It is therefore a good subject fit for A and B.
- The same section discusses form/function and systems but is an introductory overview; Claim C's broad statement about all organ systems and sustaining life would benefit from a more exact locator or a more specific source.
- The OpenStax reuse notice explicitly prohibits LLM training or ingestion into generative-AI offerings without prior written permission.
- `CTX-PHYSIOLOGY_BASICS@1` and `SCP-PHYSIOLOGY_BASICS@1` both target Claim A only.

**Findings**
- Unlike a source-title mismatch, the recorded OpenStax overview is genuinely about anatomy and physiology and directly supports the central definitions in A/B.
- The Evidence Use records do not expose the actual passages that support the Claims; the source fit must not be mistaken for completed Evidence Use.
- Claim B is directly supported by the homeostasis definition in §1.1, but a dedicated §1.5 *Homeostasis* passage is a better locator for the mechanism, set points and feedback processes if those details are later claimed.
- Claim C needs precise evidence for organ-system interactions; do not infer every system's functions from a broad introductory description.
- AI-use permission is a release blocker for ingestion/reuse of OpenStax content. No permission is assumed.
- Context/Scope only target A, leaving B/C without explicit boundaries. The slice cannot be used as a clinical assessment, diagnostic tool or individualized treatment guide.

**Decision: HOLD — A/B/C.** The source has good educational relevance, but add pinpoint locators, strengthen C's support, close Context/Scope coverage, and resolve the OpenStax AI-use permission issue before any AI-mediated use.

### 3. microbiology-basics — source supports the introductory concepts, but source identity is generic and AI ingestion is expressly restricted

**Claims**
- A — `CLM-MICROBIOLOGY_BASICS-A@1`: microorganisms are organisms most of which are too small to be observed without a microscope.
- B — `CLM-MICROBIOLOGY_BASICS-B@1`: microorganisms are widespread and perform important ecological functions.
- C — `CLM-MICROBIOLOGY_BASICS-C@1`: microorganisms can be beneficial, neutral or pathogenic to humans depending on the organism and context.

**Evidence chain**
- `SRC-MICROBIOLOGY_BASICS@1` uses the generic identity “Authoritative reference source for microbiology-basics” and points to OpenStax *Microbiology*, Chapter 1 Introduction: `https://openstax.org/books/microbiology/pages/1-introduction`.
- `EU-MICROBIOLOGY_BASICS-A/B/C@1` link the correct Claim and Source IDs, but all three descriptions are the same generic sentence and provide no pinpoint locators.
- The OpenStax Chapter 1 introduction directly states that microorganisms are small and most cannot be seen without a microscope; it describes their global distribution, their role in food webs and ecosystems, and the fact that many are helpful while others cause disease.
- The OpenStax *Microbiology* reuse notice explicitly prohibits use for LLM training or ingestion into generative-AI offerings without prior written permission.
- `CTX-MICROBIOLOGY_BASICS@1` and `SCP-MICROBIOLOGY_BASICS@1` target Claim A only.

**Findings**
- A is directly supported by the opening definition in Chapter 1.
- B is directly supported in broad terms by the chapter's description of microbes as ubiquitous and foundational to food webs. “Important ecological functions” is a reasonable summary, but an EU should point to the exact ecosystem/food-web passage and not imply all microbes have the same ecological role.
- C needs a wording refinement before it can be considered precise: the source says many microbes are helpful, many harmless, and some disease-causing. “Neutral” is not necessarily synonymous with “harmless” in every ecological or host context. Keep human pathogenicity separate from an organism's ecological role and avoid classifying a species as universally beneficial or harmful.
- The Source identity is not a real bibliographic identity; it should identify the actual OpenStax book, authors/publisher and exact section rather than “Authoritative reference source”.
- No independent second source is present. More importantly, the only source is OpenStax and the explicit AI-ingestion restriction blocks treating the page as freely reusable for AI-mediated corpus ingestion.
- Context/Scope target A only; B/C lack claim-specific scope and should distinguish general ecology, human commensalism, opportunistic infection and pathogenicity.

**Decision: HOLD — A/B/C.** Correct the Source identity, add exact EU locators, refine the “neutral” wording, establish independent/permission-compatible support, and add Context/Scope for B/C. Do not ingest OpenStax material into an AI workflow without prior written permission.

### 4. epidemiology-basics — WHO source is mismatched to the definition; three Claims are editorial placeholders

**Claims**
- A — `CLM-EPIDEMIOLOGY_BASICS-A@1`: “the slice describes basic concepts of the subject area and their relationships.”
- B — `CLM-EPIDEMIOLOGY_BASICS-B@1`: interpretation should consider source, context and applicability limits.
- C — `CLM-EPIDEMIOLOGY_BASICS-C@1`: general information does not replace specialist review where conclusions depend on conditions, measurements or professional judgment.
- D — `CLM-EPIDEMIOLOGY_BASICS-D@1`: a substantive English-language definition attributed to WHO: study of distribution and determinants of health/disease in populations and application to prevention/control.

**Evidence chain**
- `SRC-EPIDEMIOLOGY_BASICS@1` identifies CDC *Principles of Epidemiology* at `https://www.cdc.gov/training-publichealth101/php/lessons/principles-of-epidemiology.html`.
- `EU-EPIDEMIOLOGY_BASICS-A/B/C@1` correctly reference the respective Claims and the CDC Source, but their descriptions merely repeat the editorial placeholder statements. They do not identify a substantive epidemiological passage.
- `SRC-WHO-EPIDEMIOLOGY-2024@1` identifies WHO *Putting participatory surveillance into practice* at `https://www.who.int/news/item/16-10-2024-putting-participatory-surveillance-into-practice--new-who-publication-released`.
- `EU-EPIDEMIOLOGY_BASICS-D-WHO@1` links that WHO item to the definition in Claim D. The linked WHO item concerns participatory surveillance practice; its title and purpose do not establish the classic definition of epidemiology recorded in D. This is a source/claim mismatch, not independent confirmation.
- The CDC's archived *Principles of Epidemiology*, Lesson 1, Section 1 directly states the distribution/determinants/population definition and explains frequency, pattern (time/place/person), determinants and application. CDC's current *Introduction to Epidemiology* course (Jan. 10, 2025) also identifies core terms, data sources, study design and outbreak investigation learning objectives.
- `CTX-EPIDEMIOLOGY_BASICS@1` and `SCP-EPIDEMIOLOGY_BASICS@1` target Claim A only.

**Findings**
- A/B/C are not epidemiology facts. They are generic editorial statements about the slice and should not occupy the substantive Claim set for an introductory epidemiology topic.
- D is the only substantive epidemiology Claim in this slice. Its definition closely matches the established CDC definition, but the currently linked WHO participatory-surveillance publication is not the source for that definition.
- The archived CDC Lesson 1 Section 1 is a much better direct source for D; it explicitly covers distribution, determinants, specified populations and application to control health problems. The CDC source already in the record may be a current course landing page rather than the exact lesson text; the EU must point to the exact lesson/section or a verified current equivalent.
- The definition in D is population-level and does not authorize clinical diagnosis or treatment of individuals. Epidemiological association, determinant and risk factor must not be casually equated with proven individual causation.
- A/B/C currently have matching IDs and EU references, but syntactically valid links do not turn editorial placeholders into documented facts.
- Context/Scope target A only; D needs a boundary explicitly stating population-level analysis, specified populations/time/place and the distinction from individual clinical care.

**Decision: HOLD — A/B/C/D.** Rebuild A/B/C as substantive epidemiology Claims through a separately authorized content pass; replace or correct the WHO Source/EU for D with a direct CDC epidemiology definition locator; add exact EU locators and claim-specific Context/Scope. No new Claim text or Source record is written in this audit.

### 5. Cross-slice boundaries and release implications

- **Anatomy vs. physiology:** anatomy describes structure; physiology describes function and mechanisms. The two can cross-reference conceptually but should not duplicate the same introductory Claim.
- **Microbiology vs. epidemiology:** microbiology describes microorganisms and their biology; epidemiology studies distribution/determinants of health events in populations and applies findings to control health problems. A microbial cause is not, by itself, a complete population-level explanation.
- **Microbiology vs. environmental/soil microbiology:** general claims about microorganisms do not establish the role of a particular microbial community in soil, water, food or a host. Preserve the narrower boundaries established in earlier audits.
- **Epidemiology vs. public health:** epidemiology supplies population-level evidence and methods; public-health practice also includes policy, systems, services and implementation. Neither generic editorial caveats nor a surveillance case study is a full definition of epidemiology.
- **OpenStax rights:** the Anatomy and Physiology 2e and Microbiology pages both carry explicit prior-written-permission requirements for LLM training/ingestion. Public accessibility and ordinary Creative Commons reuse language do not waive this separate restriction. These sources may be recorded as references, but AI-mediated extraction/ingestion must not proceed absent permission.
- No new Relations are created. Existing Relations, historical records and prior decisions remain untouched.

### 6. Consolidated dispositions

| Slice | Records screened | Claims | Decision | Principal blocker |
|---|---:|---:|---|---|
| anatomy-basics | 11 | 3 | HOLD A/B/C | NIGMS locator unverified; OpenStax support narrow and AI-use restricted |
| physiology-basics | 9 | 3 | HOLD A/B/C | Generic EU locators; OpenStax AI-use restriction; Context/Scope only target A |
| microbiology-basics | 9 | 3 | HOLD A/B/C | Generic Source identity/EUs; “neutral” ambiguity; OpenStax AI-use restriction |
| epidemiology-basics | 12 | 4 | HOLD A/B/C/D | A/B/C editorial placeholders; WHO source mismatch for D; incomplete Context/Scope |

**Overall result:** 41 records screened; 13 Claims remain HOLD. No canonical JSON, README, Relation, Assessment, public allowlist or publication state was changed. The strongest direct conceptual matches are the anatomy tissue Claims, physiology A/B, microbiology A/B/C (subject to precision and rights), and epidemiology D with CDC's archived definition. None is release-ready under the current evidence/use and applicability records. The most serious defects are the OpenStax AI-ingestion restrictions, the unverified NIGMS locator, and the WHO-to-epidemiology-definition mismatch.

**Change control:** audit finding only. No new M13 batch is started. No public INCLUDE is assigned.
