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
