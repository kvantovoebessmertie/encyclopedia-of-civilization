# First Edition — Current-Head Reconciliation of the 15 Semantic-HOLD Relations

Date: 2026-11-20  
Inspection HEAD: `9a933f272f2124a7748ab0d184de465e84bddee4`  
PR: #22 — `mvp-public-contribution-design-2026-10-11`  
Status: **15/15 CURRENT RELATION RECORDS RE-FETCHED; 14/15 RELATION–CONTEXT TARGET CYCLES EXACT; ALL 15 RELEASE DISPOSITIONS REMAIN HOLD**

## 1. Scope and method

Re-fetched the current canonical JSON for all 15 Relations in the semantic-HOLD remediation queue and the Context referenced by each Relation's `frame_ref`, all at the same immutable inspection HEAD. Verified exact record identity/version, participant IDs/versions, relation type, frame reference and reciprocal Context `target_ref`.

This is a current-version and reference reconciliation, not a fresh substantive re-adjudication of all 30+ participant Claims and their Evidence Use/Source chains. Existing bounded semantic findings remain controlling unless explicitly superseded below. No canonical record, register, allowlist, or publication state was changed by this report.

## 2. Current exact Relation / Context inventory

| # | Current Relation | Current endpoints | Relation frame / Context target | Reference result |
|---:|---|---|---|---|
| 1 | `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@6` | Library Science C@2; Archival Science A@2 | Context @3 → Relation @6 | Exact |
| 2 | `REL-CROSS-CO-EMERGENCY-ESCALATION@2` | CO Heating Emergency@1; Generator CO Alarm Emergency@1 | Context @1 → Relation @2 | Exact |
| 3 | `REL-CROSS-AIR-POWER-SYSTEMS@2` | Air Quality A@1; Power Systems A@1 | Context @1 → Relation @2 | Exact |
| 4 | `REL-CROSS-AMR-PLANT-HEALTH@2` | Antimicrobial Resistance C@1; Plant Pathology A@1 | Context @1 → Relation @2 | Exact |
| 5 | `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2` | Groundwater A@1; Soil Microbiology A@1 | Context @1 → Relation @2 | Exact |
| 6 | `REL-CROSS-FOOD-PUBLIC-HEALTH@2` | Food Security D@1; Public Health A@1 | Context @1 → Relation @2 | Exact |
| 7 | `REL-CROSS-M2-STATISTICS-RESEARCH@3` | Statistics C@1; Research Methods B@2 | Context @2 → Relation @3 | Exact |
| 8 | `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4` | Migration and Mobility C@2; Labor Economics C@2 | Context @1 → Relation @4 | Exact |
| 9 | `REL-CROSS-PLANTPATH-ENTOMOLOGY@2` | Plant Pathology A@1; Entomology A@1 | Context @1 → Relation @2 | Exact |
| 10 | `REL-CROSS-QUANTUM-MEASUREMENT@2` | Quantum Mechanics A@1; Measurement Science B@1 | Context @1 → Relation @2 | Exact |
| 11 | `REL-CROSS-RESEARCH-STATISTICS@3` | Research Methods A@1; Statistical Inference A@1 | Context @2 → Relation @3 | Exact |
| 12 | `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2` | Human Settlement Systems C@1; Public Health A@1 | Context @1 → Relation @2 | Exact |
| 13 | `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2` | Earthquake Event@1; Aftershock Expectation Claim@1 | Context @1 → Relation @2 | Exact |
| 14 | `REL-CONTAINER-WATER-STORAGE@1` | Sanitized Container State@1; Stored Container State@1 | Water Storage Context @1 → Claim `CLM-WATER-STORAGE-CONTAINER@1`, not Relation | **Known model/target exception** |
| 15 | `REL_M3_EMERGENCY_INFRASTRUCTURE@3` | Emergency Management A@1; Infrastructure Resilience D@2 | Context @2 → Relation @3 | Exact |

Result: 14 of 15 Relation-specific Contexts target the exact current Relation version. The one exception is the water-storage model: its Context targets a Claim, consistent with the previously documented mismatch and owner-selected preserve/exclude decision. The earthquake Relation's own Context is correctly reciprocal; the separate Event Context/Scope target issue remains part of the Event-model exclusion decision.

## 3. Current semantic and owner-disposition reconciliation

### Corrected endpoint alignment; still release-HOLD

- **Library / Archival @6:** endpoints now directly address library preservation/access and archival preservation. The earlier endpoint-specific mismatch is superseded. Rights/distribution, independent editorial review and Human View remain separate gates.
- **Emergency / Infrastructure @3:** endpoint now uses Infrastructure Resilience D@2 with the CISA-backed evidence chain; the exact Relation/Context cycle is aligned. This is a bounded navigation relation, not a causal or quantified dependency claim. Both slices and the Relation remain HOLD.
- **Migration / Labor @4:** current endpoints and measurement-link type are aligned more closely than the historical pair, but the Claims do not by themselves establish an integrated migration/labor comparison or causal labor-market effect. Retain HOLD pending independent semantic review.
- **Research / Statistics @3:** current pair is Research Methods A@1 and Statistical Inference A@1, a stronger conceptual pair than the prior reproducibility endpoint. Exact EU locator and direct proposition fit still require independent review. Retain HOLD.
- **Statistics / Research Design @3:** the exact-version reference cycle is repaired, but Statistics C concerns experimental design/data analysis while Research Methods B@2 concerns reproducibility/replicability. The current typed relation still requires semantic adjudication; retain HOLD.

### Semantic HOLD findings remain open

- **CO emergency escalation @2:** substantial overlap in the immediate escalation proposition; demonstrate distinct endpoint contribution or treat as navigation without duplicate evidence credit.
- **Air / Power @2:** no interaction, emissions pathway, or monitoring dependency stated by the endpoints.
- **AMR / Plant Health @2:** a plausible One Health/plant-health connection is supported by the current WHO source, but the canonical Evidence Use locators remain generic; retain HOLD pending evidence/version review and independent adjudication.
- **Groundwater / Soil Microbiology @2:** no direct groundwater–microbe mechanism or transport/ecological pathway stated.
- **Food / Public Health @2:** broad conceptual overlap only; the selected public-health Claim does not state a food-security or nutrition-health mechanism.
- **Plant Pathology / Entomology @2:** the endpoint Claims remain generic discipline definitions; no plant–insect/pest mechanism is stated.
- **Quantum / Measurement @2:** broad quantum and generic measurement endpoints do not establish a quantum-specific measurement proposition.
- **Settlement / Public Health @2:** integrated settlement planning does not itself identify a specific health, sanitation, housing, or service-access mechanism.

### Owner-directed exclusions remain unchanged

- **Earthquake / Aftershock @2:** preserve Event @1 and Relation @2 unchanged and HOLD; exclude from first-edition release scope absent a source for a specific occurrence (owner decision E-Q1). Do not reopen or mutate.
- **Container / Water Storage @1:** preserve Object, both State records, Relation and Context unchanged; retain HOLD and exclude from first-edition release scope pending a valid model (owner decision W-Q3). Do not reopen or mutate.

## 4. Important status distinction

The canonical Relation JSON files carry their own `publication_status` and `completion_status` fields (currently `published` / `complete` in the inspected files). Those record metadata fields are not the first-edition eligibility decision. The separate first-edition semantic and owner registers continue to hold all 15 Relations from release use; no Relation is INCLUDE and no allowlist is created by a technically valid record or exact Context reference.

## 5. Work remaining

1. Treat Library/Archival and Emergency/Infrastructure endpoint corrections as implemented, not as pending repair proposals; do not repeat them.
2. Keep Statistics/Research Design, Migration/Labor, Research/Statistics and AMR/Plant in the targeted independent semantic/evidence review lane.
3. Retain the other semantic HOLD findings unless a directly evidenced existing endpoint or an owner-approved narrowing is established.
4. Preserve E-Q1 and W-Q3 exactly; no Event/State/Relation/Context mutation.
5. Complete item-level rights/distribution and Human View gates independently of Relation semantics and CI.
6. Keep all 15 Relations HOLD until explicit release review and owner approval.

## 6. Change-control statement

- No canonical Claim, Evidence Use, Source, Relation, Context, Scope, Event, State or Object was changed.
- No endpoint was substituted by this report.
- No candidate membership, INCLUDE/HOLD/EXCLUDE decision, allowlist, publication, deployment, merge or main-branch state was changed.
- This report supersedes stale Relation/Context version references in earlier 2026-11-19 remediation descriptions only for the exact records and inspection HEAD listed above.

**Acceptance:** accept as a read-only current-head reconciliation of the 15 semantic-HOLD Relations and their Relation-specific Context references. It is not a semantic closure or release approval.
