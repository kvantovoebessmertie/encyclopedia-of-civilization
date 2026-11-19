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


### 23. Water resources, quality, treatment, infrastructure, security and management — six-slice record-level block (2026-11-19)

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
