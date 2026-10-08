# M1 Substantive Audit — 2026-10-08

Baseline: `f5cdf0e8c951c9455c42078459323b63b613a57c` (M1 scope commit; audit performed against P1 CLEAN content at `3209950f23ffce503ab6e5a448be40364e656b24`).

## Result

**SUBSTANTIVE AUDIT: FINDINGS CONFIRMED — M1 NOT YET CLEAN.**

All six target slices were inspected at record level.

| Slice | Depth | Evidence independence | Applicability / Human View | Linkage |
|---|---|---|---|---|
| probability-basics | finding | finding | finding | candidate |
| ratios-and-percentages | finding | finding | finding | candidate |
| seed-storage-basics | finding | finding | finding | candidate |
| si-units-basics | finding | finding | finding | candidate |
| time-standard-basics | finding | finding | finding | candidate |
| water | finding | **high priority finding** | **high priority finding** | candidate |

## Confirmed findings

### M1-01 — probability-basics
Current slice has two Claims and one source/evidence track. The Context correctly states that probability depends on a model, outcome space and assumptions, but the Claims do not yet expose that dependency sufficiently for standalone reuse.

**Required:** add only materially useful depth and an independent corroborating source if it supports the existing claims without duplicating NIST's evidence.

### M1-02 — ratios-and-percentages
Current slice has two Claims and one NIST evidence track. It lacks a standalone boundary explaining that ratios/percentages are interpreted relative to the quantities and units being compared.

**Required:** strengthen applicability/interpretation boundary and independently corroborate the core representation claim where warranted.

### M1-03 — seed-storage-basics
Two broad guidance Claims are supported only by USDA. The current wording is appropriately cautious but does not identify that storage conditions and viability are crop/seed-specific.

**Required:** independent agricultural/scientific corroboration and an explicit applicability boundary; do not add crop-specific prescriptions unless directly sourced.

### M1-04 — si-units-basics
Two Claims are supported only by NIST. The slice should distinguish the SI base-unit framework from practical measurement interpretation and avoid implying that the existence of a unit alone establishes measurement accuracy.

**Required:** independent metrology corroboration and an applicability/measurement-interpretation boundary.

### M1-05 — time-standard-basics
Two Claims are supported only by NIST. The slice correctly distinguishes UTC from UTC(NIST), but does not sufficiently state that UTC is a reference time scale and that local civil time/offset conventions are a separate layer.

**Required:** independent authoritative corroboration and a concise boundary on UTC versus local civil time.

### M1-06 — water
The slice contains three Claims, but all are supported by one CDC source. This is the highest-priority M1 finding because one claim contains an operational emergency threshold and another contains a high-consequence exclusion.

**Required:** independent corroboration of the applicable water-safety guidance, explicit conditions/limits, and Human View review preserving the chemical/radioactive contamination boundary. Existing water-related independent sources in the corpus must be used only if they actually support the exact Claim; otherwise create a new source record.

## Cross-domain audit

Existing Relations already cover several water dependencies, including water ↔ chemical contamination and water ↔ treatment/filter/infrastructure contexts. No new Relation is justified merely because the six slices are in M1.

For the other five:
- probability ↔ statistics/measurement: candidate, requires semantic evidence;
- ratios/percentages ↔ units/measurement: candidate;
- SI ↔ measurement/uncertainty: candidate;
- UTC ↔ astronomy/geospatial/computing: candidate;
- seed storage ↔ agriculture/food systems: candidate.

No Relation is added at this audit stage without exact source/semantic justification.

## Human View preliminary result

No immediate unsafe wording defect was found, but all six need a second adversarial pass after corrections. The water slice is explicitly blocking until its emergency limits and source role remain visible after maturation.

## Decision

Create one unified M1 Debt Map. Corrections must be made in one controlled pass, followed by re-audit.
