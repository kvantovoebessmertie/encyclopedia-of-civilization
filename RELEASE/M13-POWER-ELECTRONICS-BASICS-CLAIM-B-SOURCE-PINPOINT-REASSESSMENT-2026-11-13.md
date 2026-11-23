# M13 — power-electronics Claim B source and pinpoint reassessment

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Target records: `CLM_POWER_ELECTRONICS_BASICS_B@1`, `EU_POWER_ELECTRONICS_BASICS_B@1`, `SRC_POWER_ELECTRONICS_BASICS@1`
Status: **source-passage desk review and correction proposal only; no canonical record, source registration, Evidence Use, or D/E/B score changed.**

## 1. Exact current record chain

The Batch 44 queue spelling was `CLM-POWER_ELECTRONICS_BASICS-B@1`. The actual file is `CLM-POWER_ELECTRONICS_BASICS-B.json`; its internal ID is `CLM_POWER_ELECTRONICS_BASICS_B`, version `1`. The corresponding EU and Source internal IDs use the same underscore form and exact version-1 references.

The Claim states: “Power-electronic converters can change electrical quantities such as voltage, current, frequency, or the form of AC and DC power.”

The current EU description is generic: “Источник используется в пределах заявленного материала.” It has no section, paragraph, page, table, figure, or other reproducible pinpoint.

The current Source identifies the U.S. Department of Energy page “Power Electronics and Balance of System Hardware Technologies”:
https://www.energy.gov/cmei/systems/power-electronics-and-balance-system-hardware-technologies

## 2. Current linked source: what it does and does not establish

The DOE page was last updated **4 February 2014**. Its content is specifically framed around solar photovoltaic systems and inverters:
- the “Power Electronics” subsection says PV inverters convert DC from PV modules/arrays to AC for the grid;
- the same passage lists setting current and voltage to maximize output power and matching converted AC to the utility network;
- later text describes voltage and frequency ride-through capabilities as an advanced inverter function.

These passages provide relevant examples for DC-to-AC conversion, current/voltage control in PV inverters, and grid-support functionality. They do **not**, by themselves, establish the Claim's full generalization across power-electronic converters, all AC/DC conversion directions, DC/DC voltage conversion, or all applications. The existing EU also fails to identify which passage supports which clause.

Source review performed 2026-11-13. The old source remains relevant background but is too narrow and dated to carry the complete present Claim unaided.

## 3. Additional official DOE passages located

The following official DOE material is more directly aligned. These are **candidate sources only**; none is currently registered in the canonical vertical slice.

### A. DOE Office of Electricity, “Unlocking the Potential of Power Electronics for the Grid” (10 September 2026)
https://www.energy.gov/oe/articles/unlocking-potential-power-electronics-grid

Exact relevant passages:
- paragraph beginning “Power electronics control and transform electricity…”: describes conversion of 120 V AC wall power to low-voltage DC for a phone/laptop battery;
- following paragraph: explicitly states that grid power electronics can regulate voltage and frequency or convert between AC and DC.

This is the strongest concise support for the general AC/DC conversion and voltage/frequency regulation concepts in the Claim. Its grid statement is expressly about the U.S. electricity grid; the Claim should not silently turn that example into a universal regulatory or jurisdictional statement.

### B. DOE Solar Energy Technologies Office, “Solar Power Electronic Devices” (last updated 12 December 2025)
https://www.energy.gov/cmei/systems/solar-power-electronic-devices

Exact relevant passages under “What are Power Electronic Devices?”:
- paragraph 1: defines power-electronic devices as converting electricity from one form to another and gives the DC-to-AC inverter example;
- paragraph 2: gives a bidirectional converter example that converts battery DC to AC during discharge and AC to DC during charging.

This supports AC/DC conversion and bidirectional operation, but is limited to solar/storage context.

### C. DOE Transportation Technologies Office, “Power Electronics Research and Development” (last updated 29 May 2026)
https://www.energy.gov/cmei/vehicles/power-electronics-research-and-development

Exact relevant passages:
- opening paragraph: vehicle power electronics process/control electrical energy and lists inverters, DC/DC converters and chargers;
- “DC/DC Converters”: explains boost converters increase battery voltage and buck converters decrease it to meet system voltage requirements;
- “On-Board Chargers”: says chargers convert AC from the grid to DC for battery charging.

This directly supports voltage increase/decrease and AC-to-DC conversion in vehicle applications. It does not, by itself, establish the full range of converter topologies or general current/frequency behavior.

## 4. Claim-level support matrix

| Claim clause | Existing linked DOE 2014 page | Candidate DOE 2026/2025 sources | Finding |
|---|---|---|---|
| Convert between AC and DC | Direct for PV inverter DC-to-AC | Direct for AC-to-DC, DC-to-AC and bidirectional conversion | Supported with broader source coverage |
| Change/adjust voltage | Direct in PV inverter output-control context | Direct for DC/DC boost and buck converters | Supported, but application/topology must be stated |
| Change current | Lists setting current in PV inverter context | Current-control details are not fully established by the reviewed short passages | Do not generalize without a technical source/passage |
| Change frequency | Mentions frequency ride-through in advanced PV inverter context | DOE grid article says grid power electronics can regulate frequency | Supported in grid-control context; distinguish regulation from arbitrary frequency conversion |

## 5. Recommended editorial treatment

Do not silently preserve the broad wording as fully established by the current one-source chain. Consider a more precise Claim formulation, subject to editorial approval:

“Power-electronic converters process electrical power by converting between AC and DC and, depending on converter topology and control, adjusting voltage and regulating power flow or grid-related frequency.”

This is a proposal, not a replacement Claim. If “current” remains a separate asserted capability, add a technical source that directly describes current regulation/control and record the exact passage. Do not equate switching current on/off with general current regulation without explanation.

## 6. Evidence Use remediation proposal

If a separate bounded authorization is granted:
1. retain the existing DOE Source and EU as historical provenance; do not overwrite the old source identity or erase the earlier chain;
2. register the three additional DOE publications as distinct Source records with correct titles, issuing offices, dates and canonical URIs;
3. create versioned Evidence Use records for the exact passages above, each linked to the intended Claim version and exact Source version;
4. explain which clause each passage supports, including application scope (grid, solar/storage, vehicle systems);
5. add a separate technical reference for current regulation if that clause remains;
6. run record schema, Claim/EU/Source linkage, duplicate-source identity, offline edition and release-conformance regressions;
7. reassess E under the current rubric only after the canonical pinpoints exist and the passages are rechecked. Do not retroactively edit Batch 44's historical D/E/B row.

## 7. Disposition

- Batch 44 first-pass D/E/B desk row remains historical and unchanged.
- Current canonical EU remains generic and has no pinpoint.
- Current linked Source is relevant but insufficient on its own for the entire Claim.
- Candidate official passages improve coverage but are not yet canonical evidence links.
- No D/E/B score upgrade is proposed on this report alone.
- Claim remains **HOLD** for canonical locator remediation and editorial scope decision.
- No independent specialist review, rights clearance, Human View or publication clearance is claimed.
- Canonical Claim/EU/Source records changed: **0**.
