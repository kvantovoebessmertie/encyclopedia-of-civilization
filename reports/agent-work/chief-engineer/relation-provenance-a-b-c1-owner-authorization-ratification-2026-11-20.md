# Relation Provenance A/B/C1 — Owner Authorization and Exact-Head Ratification

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — `mvp-public-contribution-design-2026-10-11`  
Authorization request: `RELEASE/OWNER-AUTHORIZATION-REQUEST-RELATION-EVIDENCE-PROVENANCE-2026-11-20.md`

## Owner decision

The project owner explicitly confirmed **A + B + C1 exactly as written** in the authorization request in the conversation on 2026-11-20.

This approval is limited to the three Relation-level provenance additions below. It does not authorize Claim/Evidence Use edits, semantic rewrites, endpoint changes, release eligibility changes, INCLUDE/EXCLUDE, allowlists, publication, deployment, merge, or changes to `main`.

## Authorization chronology and reconciliation

The canonical implementation already existed on the PR branch before the explicit confirmation recorded above:

- Authorization packet commit: `9002364559663b25c28d5e0ecbff235b6270c1ad`, 2026-11-20 13:35:28Z.
- Canonical implementation commit: `77af9d506c9726151cd2cef28ebcb6afeee1720f`, 2026-11-20 13:41:11Z.
- Implementation parent: `11ded56e4f0b1ddb43fc8aa9bde746a8a3a5fac7`.

The implementation commit therefore predates the explicit owner confirmation recorded in this conversation. This report preserves that chronology and records the owner's subsequent exact-scope ratification; it does not misrepresent the implementation as having followed that confirmation.

The commit diff contains exactly nine files: six Relation/Context records and three new Source records. No Claims, Evidence Uses, Scopes, schemas, workflow files, allowlists, or release decisions were changed by that commit.

## Exact scope reconciled

| Scope | Source @1 | Relation | Context | Result |
|---|---|---|---|---|
| A — Groundwater / Soil Microbiology | `SRC-USGS-GROUNDWATER-SOIL-MICROBIAL-INTERACTIONS@1` | `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2 → @3` | `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1 → @2` | Implemented as specified |
| B — Food Security / Public Health | `SRC-WHO-FOOD-SAFETY-2026@1` | `REL-CROSS-FOOD-PUBLIC-HEALTH@2 → @3` | `CTX-REL-CROSS-FOOD-PUBLIC-HEALTH@1 → @2` | Implemented as specified |
| C1 — Settlement / Public Health | `SRC-WHO-URBAN-HEALTH-CROSS-SECTOR@1` plus existing `SRC_OECD_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1` | `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@2 → @3` | `CTX-REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1 → @2` | Implemented as C1 |

For C1, the existing UN Human Settlements provenance entry was retained. The existing OECD Source @1 and new WHO urban-health Source @1 were appended to both the Relation and its target-specific Context. No provenance entry was deleted or replaced.

## Exact-head record verification

At branch HEAD `c8c7694808886657432ab56653225a9682b710c1`, all nine canonical records were re-fetched.

The six Relation/Context records have the exact reciprocal references:

- A: Relation @3 → Context @2 → Relation @3.
- B: Relation @3 → Context @2 → Relation @3.
- C1: Relation @3 → Context @2 → Relation @3.

The record diffs preserve:
- Relation type, participant Claim IDs and versions, participant order, roles and direction;
- Context content and epistemic status;
- existing provenance entries and provenance method;
- Relation/Context `publication_status` and `completion_status`.

Only the authorized version increments, additive `provenance.created_from` entries and reciprocal reference versions changed. The three new Source records are identity-and-locator metadata for external official sources; no source prose, tables, images or other expressive content was copied into the corpus.

## Rights and editorial boundary

This is provenance metadata, not rights clearance. In particular:
- WHO website terms are not automatically interchangeable with the CC BY-NC-SA 3.0 IGO policy for WHO publications.
- No item-level open licence or commercial-use permission is inferred for either WHO web page.
- The USGS and OECD source identities/locators do not resolve project-wide distribution compatibility.
- Independent hydrogeology/microbial ecology, food-safety/public-health, and urban-planning/public-health review remains outstanding.
- Human View and project-wide owner decisions R-01–R-10 remain separate and open.

All three Relations and affected slices retain their existing HOLD disposition. No release allowlist, INCLUDE/EXCLUDE decision, publication, deployment or merge was made.

## CI on the canonical implementation HEAD

All four required workflows completed successfully on the same immutable code/content HEAD `c8c7694808886657432ab56653225a9682b710c1`:

| Workflow | Run ID | Result |
|---|---:|---|
| Offline Edition | 44771792010 | PASS |
| MVP Contribution Form Browser Tests | 44771792109 | PASS |
| Release Conformance Gate | 44771792016 | PASS |
| Reference implementation tests | 44771792026 | PASS |

Reference implementation tests: **1,027 passed** in 444.67 seconds. Content preflight: **4,749 records, 479 slices, 4,749 unique record identities, 19 record types**.

These results establish only the named technical gates on this exact HEAD. They do not establish editorial/scientific acceptance, rights clearance, independent review, release eligibility or permission to publish.

## Repository controls

At the time of this report, PR #22 is OPEN / DRAFT / NOT MERGED. The implementation and this ratification remain on the PR branch. `main` is unchanged. No merge, deployment, publication or release allowlist was created.

The authorization request remains preserved as the historical request document; this report supersedes its then-current NOT AUTHORIZED status for the exact A + B + C1 scope only.
