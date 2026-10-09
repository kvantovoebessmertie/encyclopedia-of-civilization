# M13 High-Consequence Claim Review — Batch 04

**Date:** 2026-10-09  
**Branch:** `m13-system-wide-depth-audit-2026-10-09`  
**Scope:** Water-treatment fundamentals and emergency disinfection.  
**Status:** Content/evidence review only. No claim records were changed.

## Scoring

D = explanatory depth; E = claim-specific evidence fit; B = boundaries/epistemic discipline. Each score is 0–3. A higher score means the recorded claim and Evidence Use are more complete and auditable, not that the source has been externally peer-reviewed by this audit.

## Batch results

| Claim ID | Slice | D | E | B | Assessment |
|---|---|---:|---:|---:|---|
| `CLM-WATER_TREATMENT_BASICS-A` | water-treatment-basics | 2 | 2 | 2 | Gives a purpose and a use-dependent target rather than promising absolute purity. Evidence Use explains the public-health context, though it remains broad and does not identify a particular treatment process or contaminant class. Appropriate as an introductory definition. |
| `CLM-WATER_TREATMENT_BASICS-B` | water-treatment-basics | 2 | 2 | 2 | Identifies three meaningful selection factors: raw-water quality, target contaminants, and required quality. Evidence Use explicitly points to WHO for the general context and EPA for the narrower emergency-disinfection limitation. Stronger than generic boilerplate; should be connected to the contaminant-specific decision guidance. |
| `CLM-WATER_TREATMENT_BASICS-C` | water-treatment-basics | 2 | 3 | 3 | Clear boundary against treating one method as universally suitable for untested water. Evidence Use explicitly acknowledges what the WHO domain source does and does not establish. Strong epistemic discipline; keep this boundary visible near practical treatment instructions. |
| `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | water-treatment-basics | 3 | 3 | 3 | Explains the purpose of emergency disinfection and explicitly limits it: boiling/disinfection does not automatically remove heavy metals, salts, and most chemical contaminants. EPA Evidence Use identifies the exact distinction. This is a strong safety-critical pattern: action domain plus explicit non-effect. |

## Findings

1. **Positive contrast to boilerplate:** This slice has Evidence Use descriptions that state what the source supports and, in claim C, explicitly state the source's limits. That is the standard to prefer in other high-consequence slices.
2. **Important cross-slice dependency:** The generic “method depends on water quality and target contaminant” claims should lead the reader to the emergency-advisory distinction. A reader must not infer that boiling is a universal remedy for unknown contamination.
3. **No confirmed factual defect in this batch.** The main opportunity is findability/integration: make the non-universality boundary prominent in the Human View, not only in a separate claim record.
4. **Priority for later Human View audit:** test whether a reader who searches for “make water safe” can find the chemical-contamination exception before acting. This audit has not yet run a live novice usability test.

## Status

**Batch 04 reviewed; M13 remains OPEN.** This is a purposive safety-critical sample, not a representative sample and not the full 1,494-claim D/E/B census. No claim records, schema definitions, relation types, or tests were changed.
