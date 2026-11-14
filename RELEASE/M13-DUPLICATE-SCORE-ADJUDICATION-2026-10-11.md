# M13 Duplicate Score Adjudication — Batches 12/17 and 21/27

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **audit-report-level adjudication complete; historical rows preserved; independent review still required**.

## Decision rules
- Preserve every original report row and score.
- Choose a canonical audit score only after comparing the actual Claim statement, current Evidence Use description, Source identity/locator and prior rationales.
- Do not change Claim, Evidence Use, Source or Relation JSON.
- A canonical score does not mean the Claim is accepted, the source locator is complete, or M13 is closed.

## A. Nuclear physics — duplicate rows in Batches 12 and 17

Current records were opened directly. The three Claims use one broad IAEA “Nuclear science” Source record, and all three primary Evidence Use descriptions are generic boilerplate (“source used within the stated material”). The current source URI is a broad topic landing page, not a pinpoint locator. Evidence fit therefore remains E=1 for all three.

| Claim ID | Batch 12 score | Batch 17 score | Canonical audit score D/E/B | Adjudication |
|---|---:|---:|---:|---|
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A` | 1/1/2 | 2/1/2 | **1/1/2** | The statement lists the nucleus’s properties, composition, states and interactions, but does not explain a mechanism. D=1 is more proportionate to its introductory list form. E=1 due broad IAEA landing page and generic EU. B=2 is retained because the statement is a general field definition without an explicit boundary clause. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B` | 2/1/3 | 2/1/2 | **2/1/3** | The statement explains that nuclear-state changes may emit particles/radiation and explicitly qualifies the process by nucleus and transition. D=2 and E=1 are stable; B=3 is better calibrated to the explicit “may” and transition-specific boundary. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C` | 1/1/3 | 2/1/2 | **2/1/3** | The statement distinguishes mechanism, measured quantity and experimental conditions and rejects everyday analogy as a substitute for quantitative description; D=2 is more appropriate than D=1. B=3 reflects explicit boundary discipline. E=1 remains because the IAEA topic page does not evidence this general methodological rule. **Record-type mismatch remains open:** the statement is methodological guidance, but is currently `documented_fact`. |

## B. Water treatment — duplicate rows in Batches 21 and 27

The actual Claim statements and current Evidence Use records were checked. Batch 27’s evidence descriptions are more specific than Batch 21’s earlier rationale, but the A/C Claims still rely primarily on a broad WHO water/sanitation/health page without a pinpoint passage. Claim B has a separate EPA Evidence Use record whose source is the EPA emergency-disinfection page; that is a direct, additional source for contaminant-dependent treatment limits. Therefore, the later score is not adopted wholesale: D/E/B is re-adjudicated conservatively claim by claim.

| Claim ID | Batch 21 score | Batch 27 score | Canonical audit score D/E/B | Adjudication |
|---|---:|---:|---:|---|
| `CLM-WATER_TREATMENT_BASICS-A` | 2/2/3 | 2/3/3 | **2/2/3** | The claim correctly ties treatment to contaminant reduction and intended use. However, the current EU links to broad WHO context without a pinpoint passage; the separate EPA EU found in this slice targets Claim B, not A. E=2 is safer until A has a direct locator. |
| `CLM-WATER_TREATMENT_BASICS-B` | 2/3/3 | 3/3/3 | **2/3/3** | The three selection variables—raw-water quality, target contaminants, required output quality—are a useful explanatory rule, but the statement itself is concise and does not explain how to choose among methods. D=2 is more proportionate than D=3. E=3 is supported by the combined WHO context and the distinct EPA evidence link, whose EU description explicitly ties treatment limits to water conditions and contaminant type. |
| `CLM-WATER_TREATMENT_BASICS-C` | 2/2/3 | 2/3/3 | **2/2/3** | The universal-method warning is well bounded, but the WHO domain-level source and EU description do not pinpoint a passage establishing the full analysis-dependent rule. E=2 until a direct locator or an additional technical source is linked to C. |
| `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | 3/3/3 | 3/3/3 | **3/3/3** | Duplicate report row, no score conflict. Both rationales identify the critical EPA-supported boundary between microbial disinfection and removal of chemical contaminants. Preserve the duplicate history but count the Claim once. |

## Ledger disposition
- Seven repeated Claim IDs remain represented by their historical report rows.
- Three nuclear score conflicts are adjudicated above.
- Three water-treatment score conflicts are adjudicated above.
- The water emergency-disinfection Claim has duplicate report rows with identical scores; canonical score remains 3/3/3.
- The detailed consolidated ledger must retain every original score and show these canonical values as adjudicated metadata; do not overwrite the historical D/E/B cells.
- The inventory join should distinguish “score conflict adjudicated” from “semantic duplicate adjudicated.” The former is complete here; the latter is still open.

## Still open
1. Independent reviewer confirmation of these canonical scores.
2. Semantic duplicate review of the repeated Claims and any broader near-duplicates.
3. Claim-specific locator repairs and the nuclear Claim C record-type decision, under a separately authorized correction plan.
4. Regression tests after any authorized content changes.

No content Claim, Evidence Use, Source or Relation record was modified. M13 remains open.
