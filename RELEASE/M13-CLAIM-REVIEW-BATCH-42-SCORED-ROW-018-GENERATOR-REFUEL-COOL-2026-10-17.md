# M13 Batch 42 — Scored row 018: refuelling a generator

Date: 2026-10-17  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-GENERATOR-REFUEL-COOL@1`  
Evidence Use version: `EU-GENERATOR-REFUEL-COOL@1`  
Source version: `SRC-CPSC-GENERATOR-2026@1`

## Claim under review

> Генератор нельзя заправлять во время работы; перед заправкой его следует выключить и дать двигателю остыть.

## Current record linkage

The Claim and Evidence Use point to the U.S. Consumer Product Safety Commission (CPSC) page **CPSC Warns of Generator, Carbon Monoxide and Fire Hazards Ahead of Hurricane Season** (release dated May 27, 2026):

https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Warns-of-Generator-Carbon-Monoxide-and-Fire-Hazards-Ahead-of-Hurricane-Season

The canonical Evidence Use says the source supports the need to switch off and cool a generator before refuelling. However, the inspected canonical page covers outdoor placement, carbon-monoxide hazards, alarms, wet appliances after flooding, and gas leaks; it does **not** contain the generator-refuelling/cooling instruction. No passage-level locator is recorded.

## Passage-level assessment

The exact canonical CPSC page was inspected. It contains no refuelling/cooling instruction, so the current source-to-Claim link does not substantiate this Claim as recorded.

A separate CPSC release dated January 23, 2026, **Keep Warm and Safe This Winter: Tips for Using Generators, Furnaces and Space Heaters**, does directly state: “Never refuel a generator while it is running. Turn off generators and let them cool before refueling.”  
https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters

This is strong official corroboration for the proposition, but it is a different Source record/URL and is not the source currently linked by the canonical Evidence Use. Review must score the actual chain, not silently substitute a better source. A versioned Evidence Use correction to the appropriate exact CPSC source could be proposed separately, with authorization; no canonical change is made here.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-GENERATOR-REFUEL-COOL` | 2 | 1 | 1 | **D=2:** refuelling a running or hot generator can create a serious fire hazard. **E=1:** the linked CPSC page does not contain the claimed refuelling/cooling passage, and the Evidence Use has no locator. **B=1:** an authoritative CPSC page directly supports the Claim, but it is a different source from the canonical Source reference, so the current evidence chain remains mismatched. |

## Disposition

**HOLD pending corrected, pinpointed evidence and independent Human View / M13 high-consequence review.** Propose a separately authorized versioned Evidence Use update to the CPSC source that directly contains the instruction, then re-run the relevant reference tests. Do not alter canonical Claim, Evidence Use, or Source records as part of this score report.

The score is provisional, not a safety clearance or publication decision.
