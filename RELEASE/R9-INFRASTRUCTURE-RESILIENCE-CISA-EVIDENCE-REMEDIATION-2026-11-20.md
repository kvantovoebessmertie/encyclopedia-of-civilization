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

