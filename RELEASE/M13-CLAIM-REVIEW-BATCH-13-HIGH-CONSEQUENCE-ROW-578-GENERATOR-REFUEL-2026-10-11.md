# M13 Batch 13 — high-consequence source-fit review (row 578)

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **partial review; high-consequence source mismatch; Batch 13 not complete**

## `CLM-GENERATOR-REFUEL-COOL` — **D1 / E0 / B3** (provisional)

**Claim:** “Генератор нельзя заправлять во время работы; перед заправкой его следует выключить и дать двигателю остыть.”

**Record chain:** Claim provenance → `SRC-CPSC-GENERATOR-2026`; `EU-GENERATOR-REFUEL-COOL` links to the same Source. The EU description says the source supports the fire risk and shutdown/cooling before refuelling.

**External source check:** The linked U.S. Consumer Product Safety Commission release, dated 27 May 2026, covers carbon-monoxide and fire hazards and gives safe generator-use instructions (https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Warns-of-Generator-Carbon-Monoxide-and-Fire-Hazards-Ahead-of-Hurricane-Season). The visible release does **not** contain the specific instruction to shut down and allow the engine to cool before refuelling. Thus the local Evidence Use overstates what this locator shows; the exact proposition is not supported by the linked page (E0), even though the guidance may be correct and is important for safety.

**Assessment:** The Claim is a basic actionable safety instruction, not a mechanism explanation (D1). It is precise and does not suggest refuelling while running is acceptable (B3). Because this is high-consequence safety guidance, source mismatch cannot be treated as a cosmetic issue.

**Required disposition:** Keep out of any public pilot until a directly relevant authoritative source—such as the applicable generator manufacturer’s manual or an official fire-safety agency page—explicitly says to shut the generator off and allow it to cool before refuelling. Then update the EU with the exact section/passage and ensure the source applies to the relevant generator class. Do not alter canonical records in this audit pass.

## Checkpoint totals

- New Claim reviewed in this checkpoint: **1**.
- Batch 13 total with provisional D/E/B review recorded: **28 of 100**.
- Remaining candidates without individual D/E/B review: **72**.
- High-consequence source-fit blocker found: **1**.
- Canonical records changed: **0**.
- Batch 13 complete: **NO**.
