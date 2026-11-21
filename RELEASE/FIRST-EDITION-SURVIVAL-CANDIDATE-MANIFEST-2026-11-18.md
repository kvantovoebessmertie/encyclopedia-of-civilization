# First Edition — Survival Opening Candidate Manifest (Record-Level)

Date: 2026-11-18  
Branch: `mvp-public-contribution-design-2026-10-11`  
Technical validation baseline: `19ff17a31e3e5433d7077ce67d7534c0238ef4df`  
Status: **SCREENED CANDIDATES — ALL HOLD; NOT A PUBLICATION ALLOWLIST**

## Purpose and interpretation

This manifest turns nine previously reviewed survival-opening slices into an exact, version-pinned candidate inventory. It reuses the P1/P2/M3 substantive and Human View work already present in the repository. It does not repeat those audits and does not convert slice completion, published metadata, or green CI into editorial acceptance.

Every ID below was read from the canonical JSON files on the working branch. Every listed record is currently version `@1`. The complete record inventory is 112 records across nine slices, including 33 Claims. This is an inventory and dependency map, not an assertion that all 112 records belong in the first public edition.

Decision vocabulary:
- **HOLD** — keep outside the public bundle until every listed and general release condition is closed.
- **INCLUDE** — may be assigned only after exact-version evidence, dependency closure, rights, editorial/Human View, consequence review and owner approval pass.
- **EXCLUDE** — not assigned in this screening; do not delete canonical history.

## A. Exact candidate inventory

### A1. Emergency alerts and public warning — HOLD

Slice: `emergency-alert-warning` (10 records; 3 Claims)

Claims and exact evidence chain:
- `CLM-IPAWS-ALERT-CONTENT@1` → `EU-IPAWS-ALERT-CONTENT@1` → `SRC-PUBLIC-ALERT-GUIDANCE@1`
- `CLM-IPAWS-ALERT-ELEMENTS@1` → `EU-IPAWS-ALERT-ELEMENTS@1` → `SRC-PUBLIC-ALERT-GUIDANCE@1`
- `CLM-ALERTS-ENABLE-RESPOND@1` → `EU-ALERTS-ENABLE-RESPOND@1` → `SRC-RED-CROSS-ALERTS-2026@1`

Additional records:
- Context: `CTX-IPAWS-ALERTS@1` — target is only `CLM-IPAWS-ALERT-CONTENT@1`.
- Scope: `SCP-IPAWS-ALERTS@1` — target is only `CLM-IPAWS-ALERT-CONTENT@1`.
- Sources: `SRC-PUBLIC-ALERT-GUIDANCE@1`, `SRC-RED-CROSS-ALERTS-2026@1`.

Specific HOLD reason: the three Evidence Use records do not yet provide the required exact inspected passage/page/section locators in the reviewed inventory. Context/Scope must not be silently extended to the separate Red Cross Claim. Existing P1 review is reused; no new audit is claimed.

### A2. Hand-tool safety — HOLD

Slice: `hand-tool-safety` (10 records; 3 Claims)

Claims and exact evidence chain:
- `CLM-TOOL-DEFECTIVE@1` → `EU-TOOL-DEFECTIVE@1` → `SRC-CCOHS-HAND-TOOLS-2026@1`
- `CLM-TOOL-INSPECT@1` → `EU-TOOL-INSPECT@1` → `SRC-OSHA-HAND-TOOLS-2026@1`
- `CLM-TOOL-PPE@1` → `EU-TOOL-PPE@1` → `SRC-OSHA-HAND-TOOLS-2026@1`

Additional records:
- Context: `CTX-HAND-TOOLS@1` — target is only `CLM-TOOL-INSPECT@1`.
- Scope: `SCP-HAND-TOOLS@1` — target is only `CLM-TOOL-INSPECT@1`.
- Sources: `SRC-CCOHS-HAND-TOOLS-2026@1`, `SRC-OSHA-HAND-TOOLS-2026@1`.

Specific HOLD reason: do not infer that Context/Scope for inspection automatically applies to the defective-tool and PPE Claims. The P1 substantive/Human View review is reused. Final exact record-to-passage, rights and reader approval remain release conditions.

### A3. Home fire and smoke safety — HOLD

Slice: `home-fire-smoke-safety` (12 records; 4 Claims)

Claims and exact evidence chain:
- `CLM-HOME-FIRE-ESCAPE-PLAN@1` → `EU-HOME-FIRE-ESCAPE-PLAN@1` → `SRC-USFA-HOME-FIRE-2026@1`
- `CLM-HOME-FIRE-LEAVE-STAY-OUT@1` → `EU-HOME-FIRE-LEAVE-STAY-OUT@1` → `SRC-NFPA-HOME-FIRE-2026@1`
- `CLM-HOME-FIRE-SMOKE-ALARMS@1` → `EU-HOME-FIRE-SMOKE-ALARMS@1` → `SRC-USFA-HOME-FIRE-2026@1`
- `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` → `EU-HOME-FIRE-TWO-WAYS-NFPA@1` → `SRC-NFPA-HOME-FIRE-2026@1`

Additional records:
- Context: `CTX-HOME-FIRE-SAFETY@1` — target is only `CLM-HOME-FIRE-SMOKE-ALARMS@1`.
- Scope: `SCP-HOME-FIRE-SAFETY@1` — target is only `CLM-HOME-FIRE-SMOKE-ALARMS@1`.
- Sources: `SRC-NFPA-HOME-FIRE-2026@1`, `SRC-USFA-HOME-FIRE-2026@1`.

Specific HOLD reason: Context/Scope are targeted at the smoke-alarm Claim only. Do not extend them to escape-plan or evacuation Claims. Existing P1 substantive/Human View work is reused; fire-safety consequence and exact record rights/editorial review still apply.

### A4. Emergency lighting and candle safety — HOLD

Slice: `emergency-lighting-safety` (12 records; 4 Claims)

Claims and exact evidence chain:
- `CLM-LIGHTING-CANDLE-CHILDREN@1` → `EU-LIGHTING-CANDLE-CHILDREN@1` → `SRC-USFA-CANDLE-SAFETY-2026@1`
- `CLM-LIGHTING-CANDLE-UNATTENDED@1` → `EU-LIGHTING-CANDLE-UNATTENDED@1` → `SRC-USFA-CANDLE-SAFETY-2026@1`
- `CLM-LIGHTING-EXTINGUISH@1` → `EU-LIGHTING-EXTINGUISH@1` → `SRC-USFA-CANDLE-SAFETY-2026@1`
- `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1` → `EU-LIGHTING-FLASHLIGHT-OUTAGE@1` → `SRC-NFPA-CANDLE-SAFETY-2026@1`

Additional records:
- Context: `CTX-EMERGENCY-LIGHTING@1` — target is only `CLM-LIGHTING-CANDLE-UNATTENDED@1`.
- Scope: `SCP-EMERGENCY-LIGHTING@1` — target is only `CLM-LIGHTING-CANDLE-UNATTENDED@1`.
- Sources: `SRC-NFPA-CANDLE-SAFETY-2026@1`, `SRC-USFA-CANDLE-SAFETY-2026@1`.

Specific HOLD reason: Context/Scope are explicitly targeted at the unattended-candle Claim only; they do not automatically govern the child-safety, extinguishing or flashlight Claims. Existing P1 review is reused; fire consequence, exact evidence and rights review remain.

### A5. Septic-system emergency — HOLD (high consequence)

Slice: `septic-system-emergency` (12 records; 4 Claims)

Claims and exact evidence chain:
- `CLM-SEPTIC-FLOOD-NO-PUMP@1` → `EU-SEPTIC-FLOOD-NO-PUMP@1` → `SRC-EPA-SEPTIC-EMERGENCY-2026@1`
- `CLM-SEPTIC-PROFESSIONAL-INSPECTION@1` → `EU-SEPTIC-PROFESSIONAL-INSPECTION@1` → `SRC-EPA-SEPTIC-EMERGENCY-2026@1`
- `CLM-SEPTIC-REDUCE-WATER@1` → `EU-SEPTIC-REDUCE-WATER@1` → `SRC-CDC-SEPTIC-EMERGENCY-2026@1`
- `CLM-SEPTIC-SEWAGE-CONTACT@1` → `EU-SEPTIC-SEWAGE-CONTACT@1` → `SRC-CDC-SEPTIC-EMERGENCY-2026@1`

Additional records:
- Context: `CTX-SEPTIC-EMERGENCY@1` — target is only `CLM-SEPTIC-REDUCE-WATER@1`.
- Scope: `SCP-SEPTIC-EMERGENCY@1` — target is only `CLM-SEPTIC-REDUCE-WATER@1`.
- Sources: `SRC-CDC-SEPTIC-EMERGENCY-2026@1`, `SRC-EPA-SEPTIC-EMERGENCY-2026@1`.

Specific HOLD reason: Context/Scope target only the reduce-water Claim. Sewage contact, flood/no-pump and professional-inspection Claims must retain their own boundaries. Require exact passage and qualified safety review before publication of operational advice. P1 work is reused.

### A6. Food safety basics — HOLD

Slice: `food-safety-basics` (12 records; 4 Claims)

Claims and exact evidence chain:
- `CLM-FOOD_SAFETY_BASICS-A@1` → `EU-FOOD_SAFETY_BASICS-A@1` → `SRC-FOOD_SAFETY_BASICS@1`
- `CLM-FOOD_SAFETY_BASICS-B@1` → `EU-FOOD_SAFETY_BASICS-B@1` → `SRC-FOOD_SAFETY_BASICS@1`
- `CLM-FOOD_SAFETY_BASICS-C@1` → `EU-FOOD_SAFETY_BASICS-C@1` → `SRC-FOOD_SAFETY_BASICS@1`
- `CLM_FOOD_SAFETY_CDC_A@1` → `EU_FOOD_SAFETY_CDC_A@1` → `SRC_FOOD_SAFETY_CDC@1`

Additional records:
- Context: `CTX-FOOD_SAFETY_BASICS@1` — target is only `CLM-FOOD_SAFETY_BASICS-A@1`.
- Scope: `SCP-FOOD_SAFETY_BASICS@1` — target is only `CLM-FOOD_SAFETY_BASICS-A@1`.
- Sources: `SRC-FOOD_SAFETY_BASICS@1`, `SRC_FOOD_SAFETY_CDC@1`.

Specific HOLD reason: preserve the separation between the original source track and CDC Claim. Context/Scope currently target only Claim A. Existing P2 substantive/Human View work is reused; exact rights, source passage and per-Claim boundaries still need release signoff.

### A7. Food preservation basics — HOLD

Slice: `food-preservation-basics` (12 records; 3 Claims, 1 Relation)

Claims and exact evidence chain:
- `CLM-FOOD_PRESERVATION_BASICS-A@1` → `EU-FOOD_PRESERVATION_BASICS-A@1` → `SRC-FOOD_PRESERVATION_BASICS@1`
- `CLM-FOOD_PRESERVATION_BASICS-B@1` → `EU-FOOD_PRESERVATION_BASICS-B@1` → `SRC-FOOD_PRESERVATION_BASICS@1`
- `CLM-FOOD_PRESERVATION_BASICS-C@1` → `EU-FOOD_PRESERVATION_BASICS-C@1` → `SRC-FOOD_PRESERVATION_BASICS@1`
- Additional evidence: `EU_FOOD_PRESERVATION_BASICS_FDA@1` supports Claim B via `SRC_FDA_FOOD_STORAGE_SAFETY@1`.

Additional records:
- Context: `CTX-FOOD_PRESERVATION_BASICS@1` — target is only Claim A.
- Scope: `SCP-FOOD_PRESERVATION_BASICS@1` — target is only Claim A.
- Relation: `REL_M3_FOOD_PRESERVATION_SAFETY@1` — preserve the existing cross-slice relation; do not create a duplicate.
- Sources: `SRC-FOOD_PRESERVATION_BASICS@1`, `SRC_FDA_FOOD_STORAGE_SAFETY@1`.

Specific HOLD reason: Context/Scope target only Claim A; FDA's additional evidence use is attached to Claim B. Do not infer it applies to Claims A/C. P2 and M3 audit work is reused; do not reopen the substantive review or duplicate the existing Relation.

### A8. Flood food safety — HOLD

Slice: `flood-food-safety` (10 records; 3 Claims)

Claims and exact evidence chain:
- `CLM-FLOOD-FOOD-CONTACT@1` → `EU-FLOOD-FOOD-CONTACT@1` → `SRC-CDC-FLOOD-FOOD-2025@1`
- `CLM-FLOOD-FOOD-FDA-CONTACT@1` → `EU-FLOOD-FOOD-FDA-CONTACT@1` → `SRC-FDA-FLOOD-FOOD-2024@1`
- `CLM-FLOOD-FOOD-OPEN-PACKAGE@1` → `EU-FLOOD-FOOD-OPEN-PACKAGE@1` → `SRC-CDC-FLOOD-FOOD-2025@1`

Additional records:
- Context: `CTX-FLOOD-FOOD@1` — target is only Claim CONTACT.
- Scope: `SCP-FLOOD-FOOD@1` — target is only Claim CONTACT.
- Sources: `SRC-CDC-FLOOD-FOOD-2025@1`, `SRC-FDA-FLOOD-FOOD-2024@1`.

Specific HOLD reason: Context/Scope are targeted only at Claim CONTACT; the FDA Claim and open-package Claim must not inherit them automatically. Existing P2 substantive/Human View work is reused; maintain conservative contamination boundaries and exact source/rights review.

### A9. Power-outage food safety — HOLD

Slice: `power-outage-food` (22 records; 5 Claims)

Claims and evidence chain:
- `CLM-FOOD-FREEZER-48H@1` → `EU-FOOD-FREEZER-48H@1` → `SRC-USDA-POWER-OUTAGE-2024@1`; additional independent evidence: `EU-FOOD-FREEZER-48H-FDA@1` → `SRC-FDA-POWER-OUTAGE-2026@1`.
- `CLM-FOOD-NO-OUTDOOR-FREEZER@1` → `EU-FOOD-NO-OUTDOOR-FREEZER@1` → `SRC-HEALTH-CANADA-POWER-OUTAGE-2026@1`.
- `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` → `EU-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` → `SRC-FDA-POWER-OUTAGE-2026@1`.
- `CLM-FOOD-REFRIGERATOR-4H@1` → `EU-FOOD-REFRIGERATOR-4H@1` → `SRC-USDA-POWER-OUTAGE-2024@1`; additional FDA evidence: `EU-FOOD-REFRIGERATOR-4H-FDA@1` → `SRC-FDA-POWER-OUTAGE-2026@1`.
- `CLM-FOOD-TARGET-TEMP@1` → `EU-FOOD-TARGET-TEMP@1` → `SRC-USDA-POWER-OUTAGE-2024@1`; additional FDA evidence: `EU-FOOD-TARGET-TEMP-FDA@1` → `SRC-FDA-POWER-OUTAGE-2026@1`.

Additional records:
- Contexts: `CTX-FOOD-FREEZER@1` → Claim FREEZER-48H; `CTX-FOOD-POWER-OUTAGE@1` → Claim REFRIGERATOR-4H; `CTX-FOOD-TEMP@1` → Claim TARGET-TEMP.
- Scopes: `SCP-FOOD-FREEZER@1` → Claim FREEZER-48H; `SCP-FOOD-POWER-OUTAGE@1` → Claim REFRIGERATOR-4H; `SCP-FOOD-TEMP@1` → Claim TARGET-TEMP.
- Sources: `SRC-FDA-POWER-OUTAGE-2026@1`, `SRC-HEALTH-CANADA-POWER-OUTAGE-2026@1`, `SRC-USDA-POWER-OUTAGE-2024@1`.

Specific HOLD reason: preserve three distinct context/scope target pairs; do not generalize any one pair to all five Claims. Keep the threshold and time/temperature boundaries explicit. Existing P2 substantive/Human View work is reused. Rights and final reader-facing safety review remain.

## B. Inventory totals and boundary

| Slice | Records | Claims | Status |
|---|---:|---:|---|
| emergency-alert-warning | 10 | 3 | HOLD |
| hand-tool-safety | 10 | 3 | HOLD |
| home-fire-smoke-safety | 12 | 4 | HOLD |
| emergency-lighting-safety | 12 | 4 | HOLD |
| septic-system-emergency | 12 | 4 | HOLD |
| food-safety-basics | 12 | 4 | HOLD |
| food-preservation-basics | 12 | 3 | HOLD |
| flood-food-safety | 10 | 3 | HOLD |
| power-outage-food | 22 | 5 | HOLD |
| **Total** | **112** | **33** | **0 INCLUDE / 112 HOLD** |

These 112 records are the full current record files in the nine named slices at the reviewed branch snapshot. The count does not imply that every supporting record must be published; the eventual manifest should include only the exact transitive dependency closure for the selected Claims and the specific Context/Scope/Relation records that actually apply.

## C. Reused audit evidence — no re-adjudication

- P1: `RELEASE/P1-REMAINDER-SUBSTANTIVE-AUDIT-2026-10-06.md` and `RELEASE/P1-HUMAN-VIEW-ADVERSARIAL-AUDIT-2026-10-06.md`; findings were closed in the review reports. The historical P1 checkpoint was marked validation pending. The new current-head technical run is recorded separately in `RELEASE/FIRST-EDITION-CURRENT-HEAD-VALIDATION-2026-11-18.md`; it is not a retroactive revalidation of the historical P1 checkpoint.
- P2: `RELEASE/P2-FOOD-SAFETY-SUBSTANTIVE-RE-AUDIT-2026-10-06.md`; the four food slices above passed substantive/Human View in that report. Historical P2 checkpoint validation is not retroactively inferred from the new current-head run.
- M3: `RELEASE/M3-SUBSTANTIVE-AUDIT-2026-10-08.md`, `RELEASE/M3-DEBT-MAP-2026-10-08.md`, `RELEASE/M3-HUMAN-VIEW-AUDIT-2026-10-08.md`; M3 review is reused, with its historical checkpoint still described as a candidate pending exact-head validation.

## D. Current technical validation (separate from editorial admission)

The exact PR #22 HEAD `19ff17a31e3e5433d7077ce67d7534c0238ef4df` passed all four PR-triggered workflows:
- Release Conformance Gate;
- Reference implementation tests;
- Offline Edition;
- MVP Contribution Form Browser Tests.

The current-head evidence is documented in `RELEASE/FIRST-EDITION-CURRENT-HEAD-VALIDATION-2026-11-18.md`. It validates the current technical snapshot only. It does not independently close each historical checkpoint or any record-level rights, source-locator, editorial or qualified safety gate.

## E. Required closure before any INCLUDE

1. **Exact evidence:** for each selected Claim, record the exact source section/page/table/passage actually inspected and show why it supports that Claim without overreach. Generic source identity is not a pinpoint locator.
2. **Dependency closure:** include only the exact Claim/Evidence Use/Source versions plus only the Context/Scope/Relations whose target references apply to that Claim. Check every referenced ID/version exists in the same edition snapshot.
3. **Rights:** establish a release-specific rights and attribution basis for every included source-derived record. No project-wide license is presumed by this manifest.
4. **Human View:** inspect the actual reader-facing output for every selected Claim, including visible warnings, conditions, limits and source role.
5. **High-consequence review:** water, medical, fire, electrical, structural, chemical, sewage and other safety procedures require qualified review. Unresolved operational instructions remain HOLD; a bounded descriptive record may be considered separately.
6. **Owner decisions:** named accountable editor/release approver, correction/takedown route, rollback operator, publication license and distribution model.
7. **Reproducible bundle:** freeze exact IDs and versions, dependency closure, source commit, manifest hash, build/test evidence, rights decisions and edition date. No record is admitted by slice-level status alone.

## F. Immediate next work

1. Close the easiest exact low-risk reader/evidence candidates first, without reopening completed audits.
2. For P1/P2 slices, use their prior audit findings as evidence and focus only on current-head validation, exact record dependency/locator verification, rights and the actual first-edition reader view.
3. Keep high-consequence operational records out until qualified review is documented.
4. Only after the first bounded set reaches INCLUDE should a machine-readable public allowlist be frozen.
5. Do not start a new M13 batch as a substitute for this work; do not modify canonical Claims or historical adjudications without a controlled, evidence-backed correction.

## Change-control statement

This manifest is a release-planning artifact only. No canonical Claim, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference or Decision record is changed. No M13 adjudication is repeated or overwritten. PR #22 remains Draft and unmerged; `main` is untouched.
