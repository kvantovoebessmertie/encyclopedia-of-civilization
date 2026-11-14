# M13 Batch 45 — Lane 5 source-passage and D/E/B review

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Selection revision: `ef4dce0f7130028a2a3fd4e9171bea0138e40386`  
Queue workflow: `43166873642`; artifact: `13919774068`  
Scope: fifth frozen lane, 20 Claims. Append-only audit documentation; no canonical records modified.

## Method and limits

- Reviewed all 20 Claim statements and Evidence Use descriptions/source identities in the exact-revision queue packets.
- Checked the named source passages where the evidence packet supplied section locators and checked relevant public source material where retrievable.
- Evidence Use contains explicit section-level locators for Claims 82–84. Other entries do not preserve a sufficiently precise claim-specific locator in this pass. E=2 is assigned only to the three exact Newton-law section references.
- Exact record-level Claim → Evidence Use → Source JSON linkage remains a human verification task; this report does not certify those edges.
- Scores are provisional desk assessments, not specialist certification, independent review, or publication clearance.

## Batch accounting

- Claims reviewed: 20/20.
- Evidence packet entries reviewed: 20/20.
- Explicit section locator in Evidence Use: 3/20 (Claims 82–84).
- Canonical JSON modified: 0.
- Automated D/E/B scoring: none.
- Disposition: all 20 HOLD pending linkage verification and any remaining source/scope work.

## Scored review

| # | Claim | D | E | B | Source/passage finding and disposition |
|---:|---|---:|---:|---:|---|
| 81 | `CLM-MECHANICAL_ENGINEERING_BASICS-C@1` | 2 | 1 | 2 | The American University of Sharjah Mechanical Engineering page is a departmental overview, not a technical source establishing safety/reliability as design principles or the need for specialist calculations in every mechanical system. HOLD; use engineering safety/design standards and define the calculation boundary. |
| 82 | `CLM-MECHANICS_BASICS-A@1` | 3 | 2 | 3 | Evidence Use identifies OpenStax University Physics Vol. 1 §5.2 “Newton's First Law” and states the inertial-frame/net-force-zero condition. This is a precise, direct locator. HOLD pending exact record-link verification and preservation of the stated inertial-frame condition. |
| 83 | `CLM-MECHANICS_BASICS-B@1` | 3 | 2 | 3 | Evidence Use identifies OpenStax §5.3 “Newton's Second Law” and explicitly limits F_net = m·a to the classical constant-mass case. Direct support with appropriate boundary. HOLD pending exact record-link verification and confirmation that the source edition retains the cited formula/context. |
| 84 | `CLM-MECHANICS_BASICS-C@1` | 3 | 2 | 3 | Evidence Use identifies OpenStax §5.5 “Newton's Third Law” and explains that action-reaction forces act on different bodies, so they do not cancel on one body's free-body diagram. Direct support with a useful explanatory boundary. HOLD pending exact record-link verification. |
| 85 | `CLM-MIGRATION_AND_MOBILITY_BASICS-B@1` | 2 | 1 | 3 | IOM and World Bank sources are relevant to internal/international migration, but neither Evidence Use description supplies a section/page pinpoint. The Claim is a sound demographic distinction and appropriately excludes individual immigration rights. HOLD pending independent-source and locator verification. |
| 86 | `CLM-MIGRATION_AND_MOBILITY_BASICS-C@1` | 2 | 1 | 3 | IOM and World Bank material may support comparability requirements, but the Claim's definition, time, territory, and flow/stock measurement dimensions are not individually pinpointed. HOLD; map each dimension to a methodological passage. |
| 87 | `CLM-MIGRATION_BASICS-A@1` | 2 | 1 | 2 | IOM World Migration Report is relevant background, but the broad report landing page does not identify a precise migration definition passage. HOLD pending exact definition locator and review of “place of residence” boundary. |
| 88 | `CLM-MIGRATION_BASICS-C@1` | 2 | 1 | 3 | The distinction between migrant, refugee, and other displaced persons is legally and factually important. IOM's broad World Migration Report page does not by itself establish the precise legal definitions and criteria. HOLD; use the Refugee Convention/UNHCR and applicable migration-law sources with explicit boundaries. |
| 89 | `CLM-MIXTURES_AND_SOLUTIONS-A@1` | 2 | 1 | 2 | OpenStax Chemistry 2e §11.1 is relevant to dissolution, but the Evidence Use does not pinpoint the definition of a solution as a homogeneous mixture of two or more substances. HOLD pending exact definition locator and chemistry terminology review. |
| 90 | `CLM-MIXTURES_AND_SOLUTIONS-B@1` | 2 | 1 | 2 | The solvent definition and the “usually greater concentration” qualification require a specific passage; the registered §11.1 page is not pinpointed in Evidence Use. The physical-state clause also needs careful handling for nonstandard mixtures. HOLD pending exact source locator. |
| 91 | `CLM-MIXTURES_AND_SOLUTIONS-C@1` | 2 | 1 | 2 | OpenStax §11.1 is relevant to dissolution, but no exact passage is preserved for molecular/ionic dispersion. The statement should avoid implying that every solute is molecular or ionic in all solution types. HOLD pending pinpoint and scope review. |
| 92 | `CLM-MONEY_AND_BANKING_BASICS-A@1` | 2 | 1 | 2 | The Federal Reserve note on new forms of money and U.S. monetary aggregates is relevant, but the Evidence Use does not pinpoint the standard functions of money (medium of exchange/payment and store of value). HOLD pending exact passage and clarification of “means of payment” versus “medium of exchange.” |
| 93 | `CLM-MONEY_AND_BANKING_BASICS-C@1` | 2 | 1 | 3 | The Federal Reserve note is relevant to differences among money forms and monetary aggregates, but liquidity and uses require exact passages and careful separation of money from broader financial assets. HOLD pending locator and terminology review. |
| 94 | `CLM-NEGOTIATION_BASICS-C@1` | 2 | 1 | 3 | Harvard Program on Negotiation's “What Is Negotiation?” is a general overview; the Claim's list of alternatives, options, criteria, and commitments needs specific support (including a source for BATNA if intended). HOLD pending precise negotiation-preparation material and a pinpoint. |
| 95 | `CLM-OPEN_SCIENCE_BASICS-A@1` | 3 | 1 | 3 | UNESCO's Open Science material supports making scientific knowledge more accessible and reusable, and includes inclusiveness in its principles. The registered broad page does not preserve the exact definition passage. HOLD pending definition/Recommendation locator. |
| 96 | `CLM-OPTICS_BASICS-A@1` | 2 | 1 | 2 | OpenStax Physics Chapter 16 is relevant to optics and light, but the broad chapter introduction does not clearly establish the inclusion of all other electromagnetic waves and their interactions with matter. HOLD pending exact definition and scope locator. |
| 97 | `CLM-OPTICS_BASICS-B@1` | 2 | 1 | 2 | The ray-model boundary for geometric optics requires a passage explaining when wave effects can be neglected. The registered OpenStax chapter introduction is too broad to support this full regime statement without a pinpoint. HOLD pending a geometrical-optics section locator. |
| 98 | `CLM-OPTICS_BASICS-C@1` | 2 | 1 | 2 | The Claim about lenses/mirrors and image properties is plausible, but the registered OpenStax chapter landing page does not pinpoint the relevant image-formation rules or distinguish real/virtual images. HOLD pending exact sections and a narrower statement. |
| 99 | `CLM-PARTICLE_PHYSICS_BASICS-B@1` | 3 | 1 | 3 | CERN's Standard Model overview is directly relevant to quarks, leptons, fermions, and bosons/force carriers. The Evidence Use lacks the exact Standard Model section locator and should distinguish fundamental fermions from composite hadrons. HOLD pending pinpoint and terminology review. |
| 100 | `CLM-PAYMENT_SYSTEMS_BASICS-B@1` | 2 | 1 | 2 | BIS CPMI material is a relevant source for payment systems, but the PDF reference lacks a claim-specific page/paragraph locator for participants, instruments, infrastructure, and rules. HOLD pending exact passages and a clear system-boundary definition. |

## Structural findings

1. **Three strong exact locators:** Claims 82–84 cite OpenStax §§5.2, 5.3, and 5.5, with propositions and limitations matching Newton's three laws. These receive E=2 provisionally, not full acceptance.
2. **Source-specific legal definitions:** Migration status and IP/labour-law claims require explicit separation of general concepts from treaty definitions, national statutes, and individual legal advice.
3. **Terminology boundaries:** Distinguish medium of exchange from means of payment; money from broader financial assets; solution from all possible mixtures; and fundamental quarks/leptons from composite particles.
4. **No canonical edits:** No Claim, Evidence Use, or Source JSON was modified. No source substitution, ID rewrite, or publication clearance is authorized.

## Disposition

- Lane 5 first-pass review: **20/20 recorded**.
- All 20 Claims: **HOLD**.
- Explicit section locators: **3/20**.
- Canonical JSON changes: **0**.
- Specialist, independent, Human View, rights, editorial, and publication gates cleared: **0**.
