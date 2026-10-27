# M13 Unscored Claim Source-Fit Triage — Batch 08

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: exactly 30 Claims: inventory rows 375–390, 395–397, and 403–413.
Mode: source-fit / record-classification triage only; no D/E/B scores.

## Coverage and limits

- Opened the 30 Claim records and corresponding primary Evidence Use (EU) records.
- Inspected source metadata for the covered slices and, where referenced, the additional OECD Education at a Glance 2026 EU/Source pair.
- Primary EUs generally resolve to the intended Claim and Source IDs and use `supports`; this is a structural result, not proof of passage-level support.
- Assigned **0 D/E/B scores** and made **0 canonical Claim, Evidence Use, Source, or Relation JSON edits**.
- These 30 Claims remain within the frozen 1,494-Claim denominator. The count of 1,242 Claims without scored rows remains unchanged.
- This pass does not independently verify each proposition against the cited passage or establish independent corroboration.

## Claim-level triage

| Inventory row | Claim(s) | Source-fit / classification finding | Follow-up |
|---:|---|---|---|
| 375 | `CLM-ECOPHYSIOLOGY_BASICS-C` | Claim says physiological responses require comparable measurement conditions. The Source identity is a descriptive definition, while the URI is an OpenStax page on animal sensory systems and movement. This is a source identity/scope mismatch for a general comparative-method claim. EU is generic. | Identify a fit-for-purpose ecophysiology/experimental-comparability source and exact passage; retain the source identity/URI defect already noted in Batch 07. |
| 376–378 | `CLM-ECOSYSTEMS_BASICS-A/B/C` | OpenStax Biology 2e, “Ecology of Ecosystems,” is a plausible and relatively specific source for the community/abiotic environment, energy/material cycles, and ecosystem-scale statements. EUs repeat the same title-level description without chapter subsection or passage locators. | Locate the relevant subsections for each distinct Claim. Do not treat the same broad chapter link as three completed evidence checks. |
| 379–381 | `CLM-ECOTOXICOLOGY_BASICS-A/B/C` | US EPA “Ecological effects” is a credible topical source. The three propositions concern field scope, factors affecting effects, and limits of generalization across species/endpoints/exposure/study design. EUs are nearly identical generic descriptions and do not identify the relevant EPA passage or distinguish which proposition it supports. | Add specific locators and verify all parts separately. Claim C’s methodological caution needs a source passage that directly establishes the listed boundary factors. |
| 382–384 | `CLM-EDUCATION_SCIENCE_BASICS-A/B/C` | The Source identity is a descriptive sentence rather than a stable named publication, and the URI points to the Institute of Education Sciences homepage. EUs are generic. A/B are broad field/method statements; C is primarily a research-transfer and comparability principle. | Replace the descriptive identity with the actual IES resource and a specific locator, or identify a better methodological source. Review C’s claim type as a cross-slice methodology candidate. |
| 385–387 | `CLM-EDUCATION_SYSTEMS-A/B/C` | A/B are attributed to UNESCO’s right-to-education framework. Their EUs explain the relevant human-rights framing and the 4-A framework, but the Source URI is a broad landing page without a pinpoint locator. C explicitly states that UNESCO is not the comparative source for education finance/organisation and links a separate OECD Education at a Glance 2026 EU/Source; that separation is sound in principle, though a report/table locator is still needed. | Preserve attribution and the distinction between the rights framework and cross-country comparison. Add exact UNESCO and OECD section/table locators and retain country coverage/reference period for C. |
| 388–390 | `CLM-ELECTORAL_SYSTEMS_BASICS-A/B/C` | International IDEA’s Electoral System Design handbook is a concrete, relevant source. The EUs use identical title-level language without chapter/section locators. A/B are broad descriptive statements; C is a comparative-method caution about rules, electoral environment, and institutions, which may need classification review alongside other methodology Claims. | Locate the handbook chapters/sections for A/B and verify the full scope. For C, determine whether the record belongs as a domain fact or methodology guidance before scoring. |
| 395–397 | `CLM-ELECTRICAL_MACHINES_BASICS-A/B/C` | DOE “Electric Motors” is plausible for the basic motor-conversion proposition in A. B concerns technical requirements and test procedures varying by category/jurisdiction; C specifically invokes applicable DOE energy-efficiency/testing rules. The same general DOE page is used for all three, without exact regulatory, category, or test-procedure locators. | A requires a specific passage on motor conversion. B/C require the applicable regulation/test-procedure source and scope (product category, effective date and jurisdiction), not only a general motors page. |
| 403–405 | `CLM-ELECTRICITY_BASICS-A/B/C` | U.S. DOE “Electricity” is a broad landing page; EUs are identical generic descriptions. A is a general importance statement, B names generation/transmission/substations/distribution, and C describes continuous balancing. The broad pointer does not by itself establish each system-level detail. | Add claim-specific DOE or grid-operator/authoritative technical locators. C needs a source explaining real-time balancing and the intended grid/system scope. |
| 406–408 | `CLM-ELECTROMAGNETISM_BASICS-A/B/C` | All three Claims describe the purpose of the slice, dependence on source/context, or the need for specialist review; they are editorial/methodological rather than core electromagnetism facts. The Source is “OpenStax University Physics — Electromagnetic Induction” with a chapter-introduction URI, too narrow for the broad slice-level statements. | Route as a methodology/record-type family. Identify whether these are governance/readiness statements that belong outside the subject Claim set; do not rewrite or delete them automatically. |
| 409–411 | `CLM-ELECTRONICS_BASICS-A/B/C` | NIST “Electronics” is named as a source, but the URI is a broad NIST page and the EUs are title-level. A defines the field very broadly; B’s semiconductor/integrated-circuit statement needs a specific technical passage; C is a general dependency/measurement-boundary statement. | Identify the actual NIST resource/page behind the link, or choose better-matched sources. Add separate locators for the definition, semiconductor statement, and measurement/dependence proposition. |
| 412–413 | `CLM-EMBEDDED_SYSTEMS_BASICS-A/B` | The Source is NIST IoT Cybersecurity, which may cover a subset of embedded/IoT systems but does not by its identity alone support the broad definition of an embedded system or the general influence of resource/environment constraints. EUs are generic. | Source-scope mismatch: find a source for the general embedded-systems definition and a separate technical source for resource/environment constraints; state any IoT-specific limitation explicitly. |

## Cross-cutting findings

1. **Source identity/scope defects:** Ecophysiology’s descriptive identity and animal-sensory-systems URI; Education Science’s descriptive identity and IES homepage URI; Electromagnetism’s induction chapter intro for slice-purpose/methodology Claims; Embedded Systems’ IoT cybersecurity program URI for general embedded-systems Claims.
2. **Generic EU descriptions:** prominent in ecosystems, ecotoxicology, education science, electoral systems, electrical machines, electricity, electromagnetism, electronics and embedded systems. The existence of an authoritative publisher or a plausible title does not demonstrate claim-specific passage fit.
3. **Potential methodology/record-type family:** Electromagnetism A/B/C are explicitly about slice purpose, context and specialist review; Education Science C and Electoral Systems C also state cross-cutting comparison/research principles. These should be adjudicated consistently, not edited in isolation.
4. **Regulatory specificity:** Electrical Machines B/C need applicable regulation/test-procedure locators and scope boundaries. A general DOE motors page is not enough to substantiate every regulatory detail.
5. **Good source separation worth preserving:** Education Systems C uses a separate OECD comparative-report EU rather than treating the UNESCO rights page as evidence for comparative financing/organisation. The OECD source is identified as Education at a Glance 2026, but the exact report/table and coverage still need verification.

## Disposition

- Claims reviewed: **30**.
- D/E/B scores: **0**.
- Canonical content JSON changes: **0**.
- Remaining Claims without scored rows: **1,242** (unchanged).
- Batch remains source-fit triage only. Source/Claim/EU corrections require a reviewable authorized correction plan and regression checks.
