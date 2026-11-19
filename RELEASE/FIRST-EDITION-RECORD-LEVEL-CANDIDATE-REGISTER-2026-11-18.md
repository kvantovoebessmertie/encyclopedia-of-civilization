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
