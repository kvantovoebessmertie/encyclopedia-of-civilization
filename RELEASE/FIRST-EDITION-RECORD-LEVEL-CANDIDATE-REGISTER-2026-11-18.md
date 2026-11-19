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
