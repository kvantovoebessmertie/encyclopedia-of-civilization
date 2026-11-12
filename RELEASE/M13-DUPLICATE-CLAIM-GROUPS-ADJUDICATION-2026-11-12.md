# M13 — adjudication of seven duplicate scored-report groups

Date: 2026-11-12
Branch: m13-system-wide-depth-audit-2026-10-09
Inventory baseline: 1,494 Claims
Scope: seven duplicate report groups (14 historical rows) identified by the scored-report ledger. This document resolves the meaning and handling of duplicate rows; it does not silently delete historical assessments or certify the underlying Claims.

## 1. Decision rule

1. Preserve every historical review row and its original report. Do not rewrite or delete a prior assessment.
2. A later report is not automatically authoritative merely because its date is later.
3. Where scores differ, keep the group in the unresolved adjudication queue until an independent reviewer compares the exact Claim version, linked Evidence Use/Source set, review rubric and source passages.
4. Where scores are identical, classify the repeated row as a repeated assessment of the same Claim, not as a second independent reviewer or independent corroboration.
5. For current M13 scoring, apply the current locator rule consistently: if the canonical Evidence Use has no reproducible claim-specific page/section/table/figure locator, E remains 1. Do not retroactively overwrite historical E scores; flag them as legacy rubric assessments requiring recalibration.

## 2. Nuclear-physics group — 3 Claims

Canonical records inspected:
- CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A/B/C, version 1.
- EU_NUCLEAR_PHYSICS_INFORMATION_BASICS_A/B/C, version 1.
- SRC_NUCLEAR_PHYSICS_INFORMATION_BASICS, version 1 (IAEA Nuclear Science topic page).

The three Evidence Use records contain only the generic description “Источник используется в пределах заявленного материала.” None identifies a section, passage or specific technical reference. The linked IAEA topic page is a broad entry point, not a sufficiently precise basis for all three claims.

Current public-source check:
- OECD Nuclear Energy Agency describes nuclear science as study of atomic nuclei and applications.
- IAEA Basic Professional Training Course Module I covers atomic/nuclear structure, radioactivity and nuclear reactions.
- U.S. Department of Energy explains nuclear structure and examples of alpha, beta and gamma decay, including emission of particles and photons.
- IAEA reference material distinguishes radioactive decay types and explains how unstable nuclei emit particles/energy.

### Historical rows and decision

| Claim ID | Earlier review | Later review | Decision |
|---|---|---|---|
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A | Batch 12: D1/E1/B2 | Batch 17: D2/E1/B2 | Conflict on D. Keep both rows; no winner selected. Definition is concise and introductory; independent scoring adjudication needed. |
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B | Batch 12: D2/E1/B3 | Batch 17: D2/E1/B2 | Conflict on B. The “may” and nucleus/transition qualifications are meaningful boundaries; retain disagreement for independent review. |
| CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C | Batch 12: D1/E1/B3 | Batch 17: D2/E1/B2 | Conflict on D and B. The statement is a methodological boundary rather than a sourced physical mechanism; the broad IAEA page does not establish this methodological proposition. |

### Nuclear group disposition

- Duplicate rows retained: 6.
- Score conflicts: 3 Claims.
- Current Evidence Use locator status: 0/3 have reproducible pinpoint locators.
- Current M13 E recalibration: E=1 remains appropriate pending evidence-use remediation; historical E=1 already agrees.
- Source remediation: replace the broad IAEA topic-page-only evidence chain with a specific nuclear-structure/decay reference for A/B; identify an appropriate methodological/measurement source for C.
- No canonical record changed. No score was overwritten.

## 3. Water-treatment and emergency-disinfection group — 4 Claims

Canonical records inspected:
- CLM-WATER_TREATMENT_BASICS-A/B/C, version 1.
- CLM-M5-WATER-EMERGENCY-DISINFECTION-D, version 1.
- Linked WHO and EPA Evidence Use records, including EU-EPA-WATER-TREATMENT-B and EU-M5-EPA-DRINKING-WATER-A/B/C.
- Source records for WHO Water, EPA Emergency Disinfection, and EPA Overview of Drinking Water Treatment Technologies.

The canonical water-treatment slice contains multiple evidence-use links. The EPA technology overview explains that different technologies target different contaminants and have different efficiencies, capacities and limitations. CDC and EPA emergency guidance explicitly warn that boiling/disinfection does not destroy heavy metals, salts and most chemical contaminants (and CDC separately names fuel, toxic chemicals and radioactive materials).

### Historical rows and decision

| Claim ID | Earlier review | Later review | Decision |
|---|---|---|---|
| CLM-M5-WATER-EMERGENCY-DISINFECTION-D | Batch 21: D3/E3/B3 | Batch 27: D3/E3/B3 | Same score repeated. Retain both rows as repeated desk assessments; not independent corroboration. Claim is directly supported by EPA emergency-disinfection guidance. |
| CLM-WATER_TREATMENT_BASICS-A | Batch 21: D2/E2/B3 | Batch 27: D2/E3/B3 | Conflict on E. The canonical slice has WHO and EPA technology links, but no exact passage locator in the Evidence Use records. Preserve historical scores; current M13 E=1 until pinpoint locators are recorded. |
| CLM-WATER_TREATMENT_BASICS-B | Batch 21: D2/E3/B3 | Batch 27: D3/E3/B3 | Conflict on D. The claim is supported by multiple EPA/WHO descriptions, but current EU descriptions still lack pinpoint locators. Preserve historical scores; current M13 E=1 until locators are added. |
| CLM-WATER_TREATMENT_BASICS-C | Batch 21: D2/E2/B3 | Batch 27: D2/E3/B3 | Conflict on E. The source set supports the no-universal-method boundary; current EU records lack pinpoint locators. Preserve historical scores; current M13 E=1 until locators are added. |

### Water group disposition

- Duplicate rows retained: 8.
- Identical-score repeated row: 1 Claim.
- Score conflicts: 3 Claims.
- Current Evidence Use pinpoint locator status: 0/4 fully locator-complete.
- Current M13 E recalibration: E=1 for all four until reproducible source locators are entered and independently checked. This is a prospective consistent application of the current rule, not deletion of the historical E=2/3 rows.
- The emergency-disinfection Claim remains a high-value safety boundary; do not weaken or bury it.
- No canonical record changed. No score was overwritten.

## 4. Reconciliation totals and unresolved work

- Duplicate groups: 7.
- Historical rows preserved: 14.
- Claims in duplicate groups: 7.
- Claims with differing historical scores: 6 (three nuclear and three water-treatment Claims).
- Claim with identical repeated scores: 1 (emergency-disinfection Claim).
- Claims with complete current pinpoint Evidence Use locators: 0/7.
- Canonical Claim/Evidence Use/Source edits: 0.
- Independent reviewer adjudications completed: 0.
- Claims accepted or release-cleared by this note: 0.

The six conflicting groups remain open for independent score adjudication. The single identical-score group is classified as a repeated assessment, not a separate independent vote. All seven remain within the 1,494-Claim denominator and retain their full historical review trail.

## 5. Sources checked

- OECD Nuclear Energy Agency, Nuclear Science: https://oecd-nea.org/jcms/c_12767/nuclear-science
- IAEA, Basic Professional Training Course Module I — Nuclear Physics and Nuclear Reactor Principles: https://gnssn-qa.iaea.org/main/BPTC/Pages/module1.aspx
- U.S. Department of Energy, DOE Explains...Nuclei: https://www.energy.gov/science/doe-explainsnuclei
- IAEA Nuclear Energy Series, radiation and radioactive decay reference: https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1558_web.pdf
- U.S. EPA, Overview of Drinking Water Treatment Technologies: https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies
- U.S. EPA, Emergency Disinfection of Drinking Water: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water
- CDC, How to Make Water Safe in an Emergency: https://www.cdc.gov/water-emergency/about/

## 6. Acceptance boundary

This note resolves duplicate-row handling and makes the score conflicts explicit. It does not produce independent scoring adjudication, does not modify canonical content, and does not close M13. Required next work is exact Evidence Use locator remediation under bounded authorization, independent review of the six conflicting groups, and separate source-independence, Human View, high-consequence and final release-gate checks.
