# M13 High-Consequence Claim Review — Batch 11
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: two chemical-water advisory claims and their linked evidence records.
Review type: targeted high-consequence review. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits and safety boundaries.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-CHEM-WATER-NO-BOIL` — D2 / E3 / B3
**Statement:** Boiling water contaminated with harmful chemicals or toxins does not make it safe to consume.

**Linked records:** `EU-CHEM-WATER-NO-BOIL` → CDC; `EU-CHEM-WATER-NO-BOIL-EPA` → EPA.

**External check:** CDC's [Drinking Water Advisories: An Overview](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html) states that boiling water containing harmful chemicals or toxins will not make it safe. EPA's [Emergency Disinfection of Drinking Water](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water) says boiling/disinfection can kill disease-causing microorganisms but will not destroy heavy metals, salts and most other chemicals.

**Assessment:** Strong, direct, independently corroborated safety boundary. The claim prevents a common and dangerous overgeneralization from microbial disinfection to chemical contamination. The EPA Evidence Use names the important distinction explicitly. Keep this distinction prominent in any practical water-treatment flow.

**Disposition:** No immediate claim change indicated. Preserve as a high-priority safety boundary in Human View and offline emergency guidance.

### 2. `CLM-CHEM-WATER-NO-DRINK` — D2 / E2 / B1
**Statement:** When a “do not drink” advisory is issued because of possible chemical contamination, use commercially bottled water for drinking and food preparation.

**Linked record:** `EU-CHEM-WATER-NO-DRINK` → CDC.

**External check:** CDC's [Drinking Water Advisories: An Overview](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html) states that “do not drink” advisories call for commercially bottled water for drinking and cooking, and also lists brushing teeth, washing fruits and vegetables, preparing food, mixing infant formula, making ice and giving water to pets. CDC distinguishes this from a “do not use” advisory, under which tap water should not be used for any purpose because even contact may be dangerous.

**Assessment:** The claim's named uses are correct, but its scope is materially incomplete for an emergency instruction. A reader could infer that tap water remains acceptable for brushing teeth, washing produce, preparing infant formula or making ice. The source's Evidence Use says only that CDC distinguishes advisory types and that boiling does not remove chemicals; it does not record the specific uses listed in the claim's subject matter. The statement also needs to preserve the crucial difference between “do not drink” and “do not use.”

**Disposition:** **Confirmed high-consequence completeness finding.** Add to the finding-specific correction queue. The authorized correction should align the list of uses with the official advisory, make clear that “do not drink” and “do not use” are different levels of restriction, and direct readers to follow the exact local advisory. Add a dedicated regression for these distinctions. No content record was edited in this review batch.

## Batch findings
1. The no-boil boundary is strongly supported by both CDC and EPA and should remain prominent.
2. The “do not drink” claim is directionally correct but omits several explicitly listed uses. This is a practical completeness risk, not a claim that its existing wording is false.
3. The user-facing path must distinguish at least three cases: boil-water advisory (microbial hazard instructions), do-not-drink advisory (chemical/toxin concern; bottled water for listed ingestion/food uses), and do-not-use advisory (avoid tap-water contact/use according to official instructions).
4. This is a two-claim purposive review, not a full audit of the water-advisory slice or all water-related claims.

## Required follow-up
- Prioritize the `CLM-CHEM-WATER-NO-DRINK` completeness finding for a narrow authorized correction and regression.
- Expand its Evidence Use description to identify the source's actual list of affected uses and the distinction between advisory categories.
- Human View test whether a reader can identify safe water for brushing teeth, produce, infant formula, ice and pets without confusing “do not drink” with “do not use.”
- Continue full Claim D/E/B census, high-consequence overlay, Human View, Relation audit and independent review.

## Audit boundary
Review artifact only. No corpus records were edited. M13 remains open; this batch does not close any audit phase.
