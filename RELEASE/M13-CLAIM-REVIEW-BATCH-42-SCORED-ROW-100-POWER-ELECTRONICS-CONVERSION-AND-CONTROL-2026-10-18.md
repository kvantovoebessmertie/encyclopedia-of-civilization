# M13 Batch 42 — Scored row 100: power-electronics conversion and control

Date: 2026-10-18  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM_POWER_ELECTRONICS_BASICS_A@1`  
Evidence Use version: `EU_POWER_ELECTRONICS_BASICS_A@1`  
Source version: `SRC_POWER_ELECTRONICS_BASICS@1`

## Claim under review

> Power electronics controls and converts electrical energy using solid-state switching and associated components.

## Evidence fit

The canonical Source is the U.S. Department of Energy's “Power Electronics and Balance of System Hardware Technologies” page: https://www.energy.gov/cmei/systems/power-electronics-and-balance-system-hardware-technologies

The DOE page describes inverters converting DC electricity to AC, controlling current and voltage, and using switching to perform conversion. That supports the conversion/control core, but the current page focuses on photovoltaic inverters and does not directly substantiate the full generalization that power electronics as a whole uses “solid-state switching and associated components.” A separate DOE page on solar power electronic devices directly describes power electronics devices as converting electricity between forms, but it is not the canonical Source linked in the current record.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM_POWER_ELECTRONICS_BASICS_A` | 2 | 1 | 1 | **D=2:** electrical-energy conversion and control can affect equipment and grid operation. **E=1:** the linked DOE page supports inverter conversion/control but is narrower than the Claim's full domain and does not directly establish the whole solid-state formulation. **B=1:** the Claim generalizes from a solar-inverter context and adds a broad component/mechanism statement. |

## Disposition

**HOLD pending a directly matched source passage, exact locator and qualified independent technical Human View.** No canonical record changed; this is not design or safety guidance.
