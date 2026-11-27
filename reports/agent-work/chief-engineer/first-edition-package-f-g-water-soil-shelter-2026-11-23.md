# Agent task report

- **Agent:** chief-engineer
- **Task:** first-edition-package-f-g-shelter-soil-water-and-release-gate-check
- **Date (UTC):** 2026-11-23
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** 9711fa0ea8e0275c71f358e986f0713ee35658df
- **Final HEAD:** fc5134eb95d1c15058929bc074be858794260ea6 (task documentation HEAD before this mandatory report-only commit)
- **Status:** VERIFIED / BLOCKED / NOT VERIFIED

## 1. Request and acceptance criteria

Continue preparing a bounded, substantive first public incomplete edition without waiting for the full M13 audit or the entire encyclopedia.

Acceptance criteria:
- preserve PR #22 as OPEN / DRAFT / NOT MERGED;
- do not modify `main`, rebase, merge or synchronize the PR base without explicit owner authorization;
- deepen exact-version source/evidence work for the latest 32-record Shelter/Soil/Emergency Water audit;
- do not change canonical records or publication decisions without exact bounded authorization;
- distinguish source research from rights clearance, safety review, Human View and publication approval;
- leave one durable report and link it from the Draft PR.

## 2. Scope

- In scope: inspect PR #22 and current branch/head; re-fetch the water and soil records; inspect the Evidence Use schema; inspect official CDC, EPA, USDA NRCS, FEMA and UK Government source passages; prepare Packages F and G; inspect exact-head checks and main-base drift.
- Out of scope: canonical Claim/Evidence Use/Source writes; INCLUDE/HOLD/EXCLUDE changes; production allowlist; legal permission; specialist safety approval; production build, deployment, public release; main synchronization, rebase or merge.
- Dependencies: existing 32-record audit; `IMPLEMENTATION/005-RECORD-SCHEMA.json`; current PR #22 branch and release-gate policy; explicit owner authorization for any canonical version changes.

## 3. Work performed

1. Re-fetched PR #22 metadata. It is OPEN / DRAFT / NOT MERGED, branch `mvp-public-contribution-design-2026-10-11`, base `main`.
2. Confirmed the starting branch HEAD was `9711fa0ea8e0275c71f358e986f0713ee35658df`.
3. Re-fetched all 10 records in `CONTENT/vertical-slices/water/records/` and all 9 records in `CONTENT/vertical-slices/soil-basics/records/`. Their exact versions and blob SHAs are embedded in Package F.
4. Retained the prior 13-record Shelter audit as a prior inspection; did not claim a second full Shelter re-fetch at the current starting HEAD.
5. Inspected official source passages:
   - CDC emergency water: boiling steps, 1-minute / above-6,500-feet 3-minute instruction, cloudy-water pre-treatment, and the fuel/toxic-chemical/radioactive-material warning.
   - EPA emergency disinfection: microbial treatment and the separate chemical-contaminant limitation; noted its different above-5,000-feet threshold.
   - USDA NRCS “What is Soil?”: soil functions, Soil Taxonomy composition definition and horizons.
   - USDA NRCS Soil Organic Matter educator guide: organic matter, living organisms, nutrient supply, water capacity and infiltration.
   - FEMA chemical-incident KPF 4 §4.1, printed pp. 147–149: hazard-specific evacuation/shelter-in-place decision factors.
   - UK Government chemical-emergency guidance: “Stay in” and “Evacuation” sections.
6. Added Package F: exact locator remediation and safety/editorial boundaries for Shelter, Soil and Emergency Water.
7. Inspected canonical Evidence Use profile in `IMPLEMENTATION/005-RECORD-SCHEMA.json`; prepared Package G as a bounded authorization request for four Water EU version bumps, one Soil Source version bump and one Soil EU version bump. No canonical writes were made.
8. Compared PR #22 with current `main`. Current main is `5b77f81f3d74c4cdc0149f6584b9d153154cedd0`; PR head `fc5134eb95d1c15058929bc074be858794260ea6` is 1,691 commits ahead and 10 behind, with merge base `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`. The main-only delta inspected in the comparison is governance/reporting documentation across seven paths. No synchronization action was taken.
9. Read the current main-branch Copilot governance and mandatory report template. This report and its PR link satisfy the durable reporting handoff; the base drift remains deliberately unresolved.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `RELEASE/FIRST-EDITION-PACKAGE-F-SHELTER-SOIL-EMERGENCY-WATER-LOCATOR-REMEDIATION-2026-11-23.md` | Added, commit `21545ac9476b8d0888c6c665796b5e27969c055d` | Convert the 32-record audit into source-specific locator proposals and safety boundaries |
| `RELEASE/FIRST-EDITION-PACKAGE-G-BOUNDED-WATER-SOIL-EVIDENCE-USE-AUTHORIZATION-REQUEST-2026-11-23.md` | Added, commit `fc5134eb95d1c15058929bc074be858794260ea6` | Specify exact bounded canonical version operations for owner authorization |
| `reports/agent-work/chief-engineer/first-edition-package-f-g-water-soil-shelter-2026-11-23.md` | Added as this report | Mandatory durable task record and handoff |

No canonical records, tests, schemas, production manifests, allowlists or release states were changed.

## 5. Findings and evidence

### VERIFIED — Emergency Water locator evidence

- Canonical records: 10/10 re-fetched at starting HEAD 9711fa0; exact IDs, versions and blob SHAs are in Package F §2.1.
- CDC source URI: https://www.cdc.gov/water-emergency/about/
  - “Water with fuel or toxic chemicals in it” explicitly includes radioactive materials and says boiling/disinfection cannot make that water safe.
  - “Steps for boiling water” step 1 specifies 1 minute and above 6,500 feet 3 minutes.
  - Cloudy-water settling/filtering appears immediately before the boiling steps.
- EPA source URI: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water
  - Opening warning says boiling/disinfection do not destroy heavy metals, salts and most other chemicals.
  - EPA uses a different high-altitude threshold (>5,000 feet). Package F prohibits merging it into the CDC-specific Claim.
- Proposed version operations are limited to four existing EUs and are listed in Package G §3.1. All four Claims remain HOLD.

### VERIFIED — Soil locator evidence

- Canonical records: 9/9 re-fetched at starting HEAD 9711fa0; exact IDs, versions and blob SHAs are in Package F §3.1.
- Current Source@1 URI points to a broad NRCS soils landing page. The inspected exact definitional/functional passages are on https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil.
- NRCS “What is Soil?” distinguishes solids (minerals and organic matter), liquid and gases, and describes horizons/layers. Its opening functional summary covers water-flow regulation and nutrient cycling.
- NRCS Soil Organic Matter guide: https://www.nrcs.usda.gov/sites/default/files/2022-10/Soil%20Organic%20Matter.pdf; page 1 and page 3 support organic matter's relation to living organisms, nutrients, water capacity and infiltration. Its figure/map includes third-party credit and is excluded from reuse in this proposal.
- Soil Claim A's organisms wording needs additional evidence and careful phase/constituent distinction. Soil Claim C's “place and depth” wording is not fully supported by a locator-only patch. Package G therefore requests only Soil Claim B EU remediation. All three Soil Claims remain HOLD.

### VERIFIED — Shelter safety boundary

- Prior 13-record Shelter audit is in `RELEASE/SHELTER-SOIL-EMERGENCY-WATER-32-RECORD-AUDIT-2026-11-23.md`; this task did not re-fetch those 13 blobs again at starting HEAD 9711fa0.
- FEMA source: https://www.fema.gov/sites/default/files/documents/fema_chemical-incident-kpf-2022.pdf, KPF 4 §4.1 “Evacuation/Sheltering”, printed pp. 147–149. It identifies chemical identity/amount, movement, time, building sealing, traffic and weather as factors; says no simple technical decision method applies across scenarios.
- UK Government source: https://www.gov.uk/government/publications/chemical-emergencies-information-for-the-public/what-to-do-in-a-chemical-emergency, “Stay in (sheltering-in-place)” and “Evacuation”. These sections distinguish sheltering from evacuation and defer duration/action to emergency services.
- These sources are chemical-incident-specific. They do not support a universal shelter checklist for all hazards. Shelter Claims remain HOLD.

### VERIFIED — schema and authorization boundary

- `IMPLEMENTATION/005-RECORD-SCHEMA.json` permits `content.material.locator` in the Evidence Use profile and `content.external_ref.uri` in the Source profile.
- Package G requests four Water EU v1→v2 updates, Soil Source v1→v2 and Soil EU-B v1→v2 only. It expressly excludes Claim rewrites, Shelter canonical changes, disposition changes, allowlist and publication.
- The broad user request to continue the first-edition packages was not treated as authorization for these exact canonical operations. Owner authorization remains required.

### VERIFIED — PR and current checks

- PR #22 remains OPEN / DRAFT / NOT MERGED.
- Current PR head after Packages F and G: `fc5134eb95d1c15058929bc074be858794260ea6`.
- Exact-head check runs returned:
  - `test-reference`: QUEUED, run/job URL https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45204212399/job/137795423304
  - `build-and-test`: IN_PROGRESS, run/job URL https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45204212397/job/137795415511
- No PASS is claimed for these checks. The earlier 2 PASS / 2 IN_PROGRESS results belonged to the previous HEAD 9711fa0 and are not evidence for fc5134e.

### VERIFIED — base drift

- Current main: `5b77f81f3d74c4cdc0149f6584b9d153154cedd0`.
- PR #22 head: `fc5134eb95d1c15058929bc074be858794260ea6`.
- Merge base: `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.
- Compare reports PR branch 1,691 ahead / 10 behind. Main-only changes inspected are governance/reporting documents. No rebase, merge, update-base or branch synchronization was performed.

## 6. Commands and verification

| Command/check | Result | Exact SHA / run URL | Notes |
|---|---|---|---|
| PR metadata fetch | PASS | PR #22, head `fc5134e...` | OPEN / DRAFT / NOT MERGED |
| Water exact-record re-fetch | PASS | Starting HEAD `9711fa0...` | 10/10 records, versions and blob SHAs captured |
| Soil exact-record re-fetch | PASS | Starting HEAD `9711fa0...` | 9/9 records, versions and blob SHAs captured |
| Shelter exact-record re-fetch at current start | NOT RUN | N/A | Prior audit only; explicitly not represented as current re-fetch |
| Official source inspection | PASS | CDC/EPA/NRCS/FEMA/GOV.UK locators in §5 | Public page/PDF passage inspection; not legal clearance |
| Evidence Use schema inspection | PASS | `IMPLEMENTATION/005-RECORD-SCHEMA.json` | `material.locator` is schema-supported |
| Main/PR comparison | PASS | `5b77f81...` vs `fc5134e...` | Diverged; 1,691 ahead / 10 behind |
| Exact-head Actions checks | PENDING | [Reference](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45204212399/job/137795423304), [Build/Test](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45204212397/job/137795415511) | QUEUED / IN_PROGRESS |
| Local unit tests / local build | NOT RUN | N/A | No local checkout/runtime test performed |
| Independent second-agent review | NOT RUN | N/A | Not available in this task execution |

## 7. Unresolved issues, risks, and blockers

- Owner authorization is required before applying the six requested versioned canonical operations in Package G.
- Shelter Claim B/C need editorial narrowing and hazard-specific safety review; no universal checklist is justified.
- Soil Claim A requires an additional exact evidence path for organisms; Soil Claim C needs a wording/support review; neither is included in Package G.
- Source rights remain preliminary. Public availability is not permission; no rights clearance or project source-reuse policy was adopted.
- R-01–R-10 remain owner decisions, including rights holder, content/code licences, contributor terms, source reuse, editor, release approver, correction/takedown contact, attribution and rights-evidence validation.
- No production INCLUDE exists; no production selection manifest or approved chapter map exists; no public edition can be built from HOLD records.
- PR #22 is 10 commits behind current main. Prior handoff `reports/agent-work/chief-engineer/first-edition-pr22-base-drift-2026-11-22.md` explicitly recommends resolving synchronization separately. No synchronization is authorized here.
- Exact-head checks on fc5134e are pending/in progress. No CI PASS is claimed.
- Independent second-agent review and local tests were not performed.

## 8. Not done / not verified

- No canonical Claim/EU/Source/Context/Scope/Relation write.
- No INCLUDE/HOLD/EXCLUDE change and no production allowlist.
- No rights grant, legal opinion, specialist safety approval, Human View or editorial sign-off.
- No production Reader build, artifact inspection, deployment or public release.
- No main modification, rebase, merge, PR retargeting or branch synchronization.
- No local test execution or independent second-agent review.
- No completion of M13 and no blanket corpus audit.

## 9. Recommendation and acceptance

- **Recommendation:** keep PR #22 Draft; first obtain explicit owner approval for the exact six Package G operations. Then re-fetch at the write-time HEAD, apply only authorized EU/Source version changes, run exact dependency tests and all required checks. In parallel, prepare a separate Shelter editorial decision packet and the missing Soil Claim A/C evidence path. Treat main-base synchronization as a separate owner decision.
- **Acceptance status:** CONDITIONAL / BLOCKED for canonical implementation and public release.
- **Reason:** source-locator research and bounded proposals are complete, but canonical writes require authorization; all candidate Claims remain HOLD; R-01–R-10 and production selection/release gates remain open.

## 10. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/first-edition-package-f-g-water-soil-shelter-2026-11-23.md`
- **Next owner/action:** Project owner — approve or reject the exact bounded Package G changes and separately decide whether/when to synchronize PR #22 with current main. Chief Engineer — after authorization, re-fetch and apply only the approved canonical changes, then verify the exact new HEAD.


## 11. Authorized implementation update — 2026-11-23

The project owner explicitly approved the exact six versioned operations listed in Package G. Approval was limited to those six files; it did not authorize any Claim wording changes, disposition changes, rights decisions, production allowlist, publication, merge or main synchronization.

### Writes performed

All six source files were re-fetched at the then-current branch HEAD `e2995d82d4e945b3afd8450959303d25e9c70231`. The branch HEAD matched exactly and all six records were version 1 before writing. The following six updates were then applied sequentially to the existing feature branch:

| Record | New version | Commit | New blob SHA |
|---|---:|---|---|
| EU-WATER-BOILING-EFFECTIVE | 2 | `1061473b7127e617059da52d65d9480ba090b80a` | `128e2555b6203d9143fa0094a3b36742490cb300` |
| EU-WATER-BOILING-TIME | 2 | `ce8e097381bd97e2fcf4eb3de72ab4811431ec07` | `1dec2a102c4d0e8a9e37d6b92e4d5833e94a4bf7` |
| EU-WATER-CHEMICAL-LIMIT | 2 | `9cc38488b0975ccb8723ca8b205211609f62b936` | `e860609dbd9433abb23f729ee5b642bf3f5cef2a` |
| EU-WATER-INDEPENDENT-CORROBORATION | 2 | `afba2e364a17dad916d7bf08fe6967b4ccc73a6b` | `454733db421abdda2ff3316eb550bf6157cd3d77` |
| SRC-SOIL_BASICS | 2 | `d0da87d5e815ed81576dbdd993395fc8c4af47ab` | `d56da42a8aeb693f282dfbf30df139ede21bcac1` |
| EU-SOIL_BASICS-B | 2 | `cc60790351ff76a3eb77ac67353a191802eaa80c` | `ba66c9950e05330e4f47390e14cc4e7cc96f6537` |

### Post-write re-fetch

All six files were re-fetched from the feature branch after writes. Verified:
- every target record is version 2;
- four Water EUs retain their original Claim@1 and Source@1 links;
- Soil Source@2 points to the exact NRCS “What is Soil?” URI;
- Soil EU-B@2 points to both `SRC-SOIL_BASICS@2` in `content.source_ref` and `provenance.created_from`;
- all six locator strings are present in the expected fields.

No record IDs changed. No Claim, assessment, inference, decision, disposition or production selection record was changed. All affected Claims remain HOLD.

### Exact-head checks

Final canonical-write HEAD: `cc60790351ff76a3eb77ac67353a191802eaa80c`.

GitHub check-runs query for this exact SHA returned six jobs, all `in_progress` at the time of inspection:
- `browser-form` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232571805/job/137895753386
- `test-reference` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232571838/job/137895736347
- `release-gate` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232571846/job/137895735754
- `build-and-test` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232571757/job/137895728469
- duplicate `test-reference` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232565111/job/137895707956
- duplicate `build-and-test` — https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/45232565045/job/137895700552

No CI PASS is claimed. The workflow runs must finish on the final report-bearing HEAD before any final technical conformance statement.

### Updated status

- Package G canonical writes: **APPLIED** within exact owner authorization.
- Post-write record identity/locator re-fetch: **PASS**.
- JSON Schema validator and local unit tests: **NOT RUN** in this execution.
- GitHub exact-head CI: **IN PROGRESS** on `cc607903...`.
- PR #22: OPEN / DRAFT / NOT MERGED.
- `main`: unchanged; no base synchronization or merge performed.
- Publication status: **NOT APPROVED**. The six records' changes improve evidence traceability but do not remove HOLD or clear source rights.
