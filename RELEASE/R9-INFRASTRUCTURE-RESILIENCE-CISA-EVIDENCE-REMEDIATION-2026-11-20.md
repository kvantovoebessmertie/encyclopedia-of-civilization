# R9 — Infrastructure Resilience CISA source and evidence remediation

Date: 2026-11-20

## Decision and bounded scope

Implemented under explicit project-owner approval recorded in the project conversation and bounded authorization `R9-INFRASTRUCTURE-RESILIENCE-CISA-SOURCE-AND-EVIDENCE-REMEDIATION-2026-11-20` in `RELEASE/EDITORIAL-CORRECTION.json`.

Only three canonical records in `infrastructure-resilience-basics` were changed:

- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1 → @2`
- `CLM-INFRASTRUCTURE_RESILIENCE-D@1 → @2`
- `EU-INFRASTRUCTURE_RESILIENCE-D@1 → @2`

The historical Source record ID is preserved for stable identity, but its source identity and URI now correctly identify the Cybersecurity and Infrastructure Security Agency (CISA) and the official CISA-hosted *The Infrastructure Dependency Primer* PDF (as of June 2, 2023). The record ID's legacy FEMA label is not an assertion of FEMA authorship.

## Claim correction

Claim D now states:

> Зависимости между инфраструктурными системами могут влиять на риски для сообщества и должны учитываться при планировании устойчивости.

The claim remains `documented_fact`. Its provenance points to Source @2.

This is deliberately narrower than the former wording about a failure or recovery of one service changing the risk and recovery of other community functions. The first-page overview supports the relevance of infrastructure dependencies to community risk and resilience planning; it does not by itself establish quantified effects or universal causal pathways.

## Evidence Use

Evidence Use D @2 points to Claim D @2 and Source @2 and records this locator:

- CISA, *The Infrastructure Dependency Primer* (as of June 2, 2023), p. 1, “Overview” and “Learn” module.

The support description is qualitative and explicitly preserves the limits above.

## Boundaries preserved

- `publication_status` and `completion_status` were not changed.
- No other Claim, Source, Evidence Use, Context, Scope, Relation, README, validator, test or release-gate semantics were changed under this authorization.
- No licence, copyright permission or project-distribution rights clearance is inferred from public availability.
- Infrastructure Resilience remains HOLD. No INCLUDE/EXCLUDE decision, allowlist, publication, deployment or merge was made.
- Independent infrastructure-resilience editorial review, rights/project-distribution review, Human View and exact-head CI remain required.

## Official source

CISA, *The Infrastructure Dependency Primer*, as of June 2, 2023:
https://www.cisa.gov/sites/default/files/2023-06/InfrastructureDependencyPrimerFS_June23_508c.pdf

## Implementation commits

- Authorization: `42d4569e3343250088be041edead404bd4067d26`
- Source @2: `ff37fd869b9a37f8130bee4a80a9fbbb33d48f2a`
- Claim D @2: `41b98e3a3864ff26313defb34c16ec09933b4a70`
- Evidence Use D @2: `9dba17356f2f7032e4868749a76824923c8fbe5f`


## Follow-on exact-version Relation alignment — 2026-11-20

Under separate explicit project-owner approval and bounded authorization `R9-P11-INFRASTRUCTURE-SYSTEMS-THINKING-SOURCE-REFERENCE-ALIGNMENT-2026-11-20`, the single dependent Relation was aligned:

- `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@2 → @3`
- Only `provenance.created_from[0].version` changed from Source @1 to Source @2 for the preserved Source identity `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025` (now identified as CISA).
- `SRC-WHO-SYSTEMS-THINKING-2026@1`, both participants and their exact versions, participant order, `relation_type`, roles, undirected direction, `frame_ref`, method and all semantic fields were preserved.
- The Relation's publication/completion statuses were preserved. It remains HOLD for release use; no allowlist, INCLUDE/EXCLUDE, publication, deployment or merge decision was made.

Authorization commit: `24a8dc08b7ce7f26dc88a02fedb47fe661ac4c2e`  
Relation commit: `c1d487ac0b7cd433f56e4a2420aafd708f36bf73`


## Explicitly preserved Context boundary

A follow-up inspection of `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@1` found that its `target_ref` still points to Relation @2 and its `provenance.created_from` still contains the legacy infrastructure Source @1. This Context was expressly excluded from the Relation-only authorization, so it was not modified. The Relation @3 / Context @1 pair therefore has a remaining exact-version target/provenance alignment issue. A separate bounded owner authorization is required before versioning Context to @2 (targeting Relation @3 and aligning its infrastructure Source provenance to @2). The Relation remains HOLD; no Context mutation is implied by the completed Relation-only approval.

## Follow-on exact-version Context alignment — 2026-11-20

Under separate explicit project-owner approval and bounded authorization `R9-P11-INFRASTRUCTURE-SYSTEMS-THINKING-CONTEXT-ALIGNMENT-2026-11-20`, the dependent Context was aligned:

- `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@1 → @2`
- `content.target_ref` now points to `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@3`.
- Only the first `provenance.created_from` Source version advanced from @1 to @2 for the preserved infrastructure Source identity `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025`, now identified as the official CISA Infrastructure Dependency Primer.
- The second provenance reference `SRC-WHO-SYSTEMS-THINKING-2026@1` was preserved.
- The Context condition, epistemic status, provenance method, record identity, type version, publication/completion statuses and all other fields were preserved.
- No Claim, Source, Evidence Use, Scope, Relation or other Context was changed under this authorization.
- Context @2 and Relation @3 now form a mutually aligned exact-version pair; both remain HOLD for release use. No allowlist, INCLUDE/EXCLUDE decision, publication, deployment or merge was made.

Authorization commit: `e0a3d32cd2b54f0db873f4cd9afc88cfe6007a8d`  
Context @2 commit: `f0adc4376b587f79bac2e16ff039b70d99a23437`

The remaining release conditions are unchanged: independent editorial review, rights/project-distribution review, Human View and exact-head CI are still required.

## Precision note — remaining Relation frame reference

A post-implementation graph check found one additional dependency that was not included in the Context-only authorization above: `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@3` still has `frame_ref` pointing to `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@1`. The Context @2 target now correctly points to Relation @3, but the reverse Relation-to-Context frame reference is still stale.

No Relation change has been made. The existing Relation-only authorization explicitly prohibited Context changes, and the Context-only authorization above does not authorize a Relation mutation. A separate owner authorization is required before advancing the Relation from @3 to @4 solely to update `frame_ref.version` from 1 to 2. All participants, participant order, roles, direction, relation type, provenance, method and semantic fields must remain unchanged. Until that separate alignment is authorized and implemented, the Relation/Context pair is not fully mutually aligned and remains HOLD.

## Final exact-version Relation / Context reconciliation — 2026-11-20

Following separate explicit project-owner approval and bounded authorization `R9-P11-INFRASTRUCTURE-SYSTEMS-THINKING-FRAME-ALIGNMENT-2026-11-20`, the reciprocal Relation frame reference was aligned:

- `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@3 → @4`
- Only `content.frame_ref.version` changed from 1 to 2 for the preserved Context identity `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING`.
- The Context @2 already targets Relation @3. Relation @4 now frames Context @2, completing the reciprocal exact-version references.
- Both Relation provenance references, both participant identities/order/versions, relation type, roles, undirected direction, provenance method, publication/completion statuses and all other fields were preserved.
- No Claim, Source, Evidence Use, Context, Scope or other Relation was changed under this authorization.
- The Relation and Context remain HOLD for release use. No allowlist, INCLUDE/EXCLUDE decision, publication, deployment or merge was made.

Authorization commit: `07130ff9be2df698bb7100e8121e28bef54ff4e3`  
Relation @4 commit: `50650ffd9934b025504ce9c25067e5d7ef68bf83`

The P11 Relation/Context exact-version cycle is now internally aligned: Relation @4 → Context @2 → Relation @3 as the Context target. This is an exact-version reference reconciliation, not a semantic re-adjudication or release approval. Independent editorial review, rights/project-distribution review, Human View and exact-head CI remain required.

## Correction to the exact-version status above

A final graph-level verification after Relation @4 shows that the reciprocal pair is **not yet fully aligned**: Relation @4 now points to Context @2, but Context @2 still targets Relation @3. The previous paragraph's statement that the pair was now internally aligned was premature and is superseded by this correction.

The remaining coordinated versioning sequence is:
1. Version Relation @4 → @5, changing only `frame_ref.version` to the planned Context @3.
2. Version Context @2 → @3, changing only `target_ref.version` to Relation @5.

This order produces the mutually exact final pair Relation @5 ↔ Context @3. The just-completed authorization covered only Relation @3 → @4; it does not authorize either additional step. No further canonical mutation will be made until a separate bounded owner approval is recorded. Both records and both slices remain HOLD.

## Completed coordinated exact-version reconciliation — 2026-11-20

The project owner explicitly approved the coordinated two-step alignment under bounded authorization `R9-P11-INFRASTRUCTURE-SYSTEMS-THINKING-FINAL-CYCLE-ALIGNMENT-2026-11-20`.

1. Relation `REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@4 → @5`: only `content.frame_ref.version` advanced from Context @2 to Context @3.
2. Context `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@2 → @3`: only `content.target_ref.version` advanced from Relation @3 to Relation @5.

Final exact-version references verified from the committed files:

- Relation @5 `frame_ref` → Context @3.
- Context @3 `target_ref` → Relation @5.
- Both records' infrastructure Source provenance references resolve to Source @2.
- Both records' WHO Source provenance references remain at @1.

Preserved without change: Relation type, participants and order, roles, direction, both provenance arrays and methods, Context condition and epistemic status, record identities, type versions, publication/completion statuses and all other semantic fields.

Authorization commit: `6c1850e71e606fbe5797380fe04cedde55a51dbb`  
Relation @5 commit: `c072a8d489eb412ba61452cc973b4099abf4be37`  
Context @3 commit: `9e3eaee0d45a69d6f9426a71e2e3bde15389921c`

The earlier interim statements in this report that the pair was already aligned at Relation @4 / Context @2 are superseded by the subsequent correction and this final verified pair. The Relation and both subject slices remain HOLD; no allowlist, INCLUDE/EXCLUDE decision, publication, deployment or merge was made. Independent editorial review, rights/project-distribution review, Human View and exact-head CI remain required.

## Source schema correction and remaining exact-version preflight finding — 2026-11-20

The first exact-head preflight rejected Source @2 because `publisher`, `title` and `as_of_date` were added as unsupported properties inside the Source content profile. The Source record was corrected within the existing bounded source-identity authorization: those extra properties were removed, with publisher/identity, title and as-of date retained in the schema-supported `source_identity` field and the `representation` field. The official CISA URI, availability and preservation fields remain unchanged.

Source schema correction commit: `694a629ff96a16e9d7bf45945f30d132447d9470`

The subsequent exact-head Reference and Offline Edition preflights no longer report a Source schema error. They now report only unresolved references to the historical Source @1 (`STORAGE-VERSION-NOT-FOUND`). The remaining edges are confined to three Infrastructure Resilience Evidence Use records (A-2, B-2, C-2), plus the emergency-management Relation `REL_M3_EMERGENCY_INFRASTRUCTURE@2` and its Context `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@1`. These records retain exact historical references to the pre-correction Source @1; the current corpus file contains Source @2 only.

No dependent Evidence Use, Relation or Context has been changed. Repointing these historical records to Source @2 without a claim-specific support review would risk implying new evidentiary support. The minimal history-preserving option is to restore the exact Source @1 snapshot as a second versioned JSON record in the same slice (separate filename, same record_id, record_version "1"), leaving all historical edges intact, and update only the corpus coverage manifest from 4,741 to 4,742 total records and from 589 to 590 Source records. This requires separate owner authorization because it adds a canonical historical version and changes the coverage manifest. Until authorized, the exact-head content preflight remains blocked by the missing historical Source @1; no CI PASS is claimed.


## Historical Source @1 restoration — 2026-11-20

The project owner explicitly authorized restoration of the exact historical Source @1 snapshot under bounded authorization `R9-INFRASTRUCTURE-HISTORICAL-SOURCE-RESTORATION-2026-11-20`, recorded in `RELEASE/EDITORIAL-CORRECTION.json`.

The historical snapshot was recovered from commit `d490c1a6c2a370bda037b2dba8c6e45ecc7a8ace` (blob `1079759df3a44483db63fca65c279e06fe519a3b`) and restored without changing its JSON content as:

- `CONTENT/vertical-slices/infrastructure-resilience-basics/records/SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025-v1.json`
- Logical identity: `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1`
- Historical identity and URI remain FEMA — Infrastructure Dependency Primer and the original FEMA public reference.
- Current `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@2` remains the corrected CISA source record; neither version replaces the other.

This restores the exact historical version needed by the three existing Infrastructure Resilience Evidence Use records and the emergency-management Relation/Context provenance edges. No dependent Evidence Use, Relation, Context, Claim or Source @2 record was modified or repointed.

The restored @1 snapshot conforms to the existing Source schema. Therefore **no schema exception or schema relaxation was necessary**; Source @2 remains strictly validated under the same profile.

The coverage manifest was updated only for the added versioned record:

- `total_records`: 4,741 → 4,742
- `types.source.count`: 589 → 590
- Slice count remains unchanged.

A focused regression test now verifies that Source @1 and Source @2 coexist, that the historical FEMA identity/URI are preserved, and that version-pinned historical references remain represented.

Implementation commits on the PR branch:

- Historical Source @1 restoration: `294002ea130c003eeb1741cc127f70fd2845539c`
- Regression test: `07122764eb8467caa6fa6d7055276538787b42fe`
- Coverage manifest: `16c03b9a126b9ea404210e29ea95cde7f7fb3252`
- Bounded authorization manifest: `1a72e0eff1d7bb495ece08fab80ef2cd6f21f938`

The Infrastructure Resilience slice remains HOLD. No INCLUDE/EXCLUDE decision, allowlist, publication, deployment, merge or `main`-branch change was made. Exact-head validation and CI must still be run against the resulting PR head; no PASS is claimed here.
