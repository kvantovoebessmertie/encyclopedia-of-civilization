# P1 Human View / Adversarial Audit — 2026-10-07

## Baseline

- Corpus: 4601 records / 479 vertical slices / 19 record types
- P1 batch: 8 emergency/high-consequence slices
- Scope: burn-first-aid; cold-weather-hypothermia; extreme-heat-safety; carbon-monoxide-heating-safety; generator-carbon-monoxide-safety; wildfire-smoke-safety; flood-cleanup-safety; emergency-waste-sanitation

## Adversarial checks

| Check | Result |
|---|---|
| Emergency escalation is visible where the topic can become life-threatening | PASS |
| Claims distinguish routine guidance from emergency escalation | PASS |
| No slice presents itself as individualized diagnosis or professional engineering/legal advice | PASS |
| High-risk actions have explicit prohibitions or boundaries where needed | PASS |
| CO guidance separates prevention from alarm/emergency response | PASS |
| Flood guidance blocks unsafe re-entry pending professional safety confirmation | PASS |
| Hazardous-waste guidance does not instruct users to process uncertain hazardous material as ordinary household waste | PASS |
| Wildfire-smoke guidance preserves local-authority / air-quality boundaries | PASS |
| Source traceability remains visible through Claim → Evidence Use → Source | PASS |
| No synthetic cross-domain relation was introduced; only semantically justified links were added | PASS |

## Findings and corrections

1. A source-identity defect was found in the CO heating emergency branch: the initial record cited a CDC page that did not directly support the full alarm-response sequence. It was replaced with a direct CPSC source and the Claim/Evidence Use links were updated.
2. The hypothermia emergency branch initially had only one direct source. Independent National Weather Service Evidence Use was added.
3. Two natural cross-domain Relations were added:
   - shared CO emergency escalation between heating and generator contexts;
   - flood cleanup and hazardous-waste safety boundary.
4. Registry, coverage manifest, and all eight slice READMEs were synchronized with the current corpus.
5. No unresolved Human View findings remain.

## Decision

**HUMAN VIEW PASS — P1 batch.**

This audit does not establish medical, engineering, legal, or other professional correctness by itself. It verifies that the current content is bounded, traceable, escalation-aware, and resistant to the principal usability failure modes identified for this P1 batch.

Final release status remains **OPEN** until exact-head Reference, Release Gate, and Offline CI are all GREEN and a dedicated P1 CLEAN checkpoint is created.
