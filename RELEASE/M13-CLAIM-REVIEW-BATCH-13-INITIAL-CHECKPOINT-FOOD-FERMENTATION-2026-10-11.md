# M13 Batch 13 — Initial Source-Fit Review Checkpoint
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **PARTIAL — 3 of 100 candidate reviews recorded; Batch 13 is not complete.**
Scope: Food fermentation Claims A–C, inventory rows 541–543. This checkpoint is not the final Batch 13 worklist; full 100-Claim eligibility and no-overlap reconciliation remains required before the batch can be called complete.

## Structural identity and linkage
The following records were opened from the M13 branch:
- `CLM-FOOD_FERMENTATION_BASICS-A` → `EU-FOOD_FERMENTATION_BASICS-A` → `SRC-FOOD_FERMENTATION_BASICS`
- `CLM-FOOD_FERMENTATION_BASICS-B` → `EU-FOOD_FERMENTATION_BASICS-B` → `SRC-FOOD_FERMENTATION_BASICS`
- `CLM-FOOD_FERMENTATION_BASICS-C` → `EU-FOOD_FERMENTATION_BASICS-C` → `SRC-FOOD_FERMENTATION_BASICS`

For all three inspected chains, record types, internal IDs, EU `claim_ref`, EU `source_ref`, `supports` role, and Source existence match structurally. Claim provenance names the same Source ID. This is a structural pass, not proof of claim-specific support. The three Evidence Use descriptions are generic and do not identify a pinpoint section.

Source locator opened: FAO, *Fermented fruits and vegetables: A global perspective*, Chapter 2, “Basic Principles of Fermentation”:
https://www.fao.org/4/x0560e/x0560e07.htm

## Provisional D/E/B scoring
D = explanatory depth; E = claim-specific evidence fit; B = boundary discipline. Each is 0–3.

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-FOOD_FERMENTATION_BASICS-A` | 2 | 3 | 3 | The claim says fermentation uses microorganisms and their metabolic activity to transform food materials under suitable conditions. FAO Chapter 2 describes microbial metabolism and growth, the production of by-products, and changes in food texture/flavour (especially lines 60–66); this directly supports the core proposition. The wording is bounded by “under suitable conditions.” Keep provisionally; improve EU description with the exact sections on organisms and microbial activity. |
| `CLM-FOOD_FERMENTATION_BASICS-B` | 2 | 2 | 3 | FAO §2.1 states fermented foods are consumed worldwide and vary by nation, staple diet, and locally available raw ingredients (lines 5–7); Table 2.1 gives regional examples (lines 22–55). This directly supports product and regional diversity. The claim also mentions different processes, which are not comprehensively established by the opening passage alone. Keep provisionally; add a precise locator or narrow the wording to what the source explicitly supports. |
| `CLM-FOOD_FERMENTATION_BASICS-C` | 2 | 3 | 3 | FAO identifies bacteria, yeasts, and moulds as common groups (lines 8–15), discusses organism roles (lines 16–21), and explains that multiple microorganisms may work together or in sequence and that growth conditions affect them (lines 66–68). This directly supports the claim’s core statement. Keep provisionally; update EU description to identify §§2.2–2.4 and the relevant passages. |

## Findings and limits
- 3/3 inspected primary links pass structural identity/linkage checks.
- 3/3 Evidence Use descriptions are generic; source existence alone is not a pinpoint evidence trail.
- No canonical Claim, Evidence Use, Source, or Relation JSON was changed.
- These are initial provisional scores, not independent-review approvals.
- Batch 13 remains open until exactly 100 unique, previously unscored Claims have a no-overlap-checked worklist and all required per-Claim reviews are recorded.
