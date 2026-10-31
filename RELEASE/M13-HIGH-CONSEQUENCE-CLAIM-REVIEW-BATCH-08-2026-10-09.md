# M13 High-Consequence Claim Review — Batch 08
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: four cold-weather / hypothermia claims and their linked Evidence Use records.
Review type: targeted high-consequence review. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits, uncertainty and safety boundaries.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-COLD-HYPOTHERMIA-EMERGENCY` — D2 / E2 / B2
**Statement:** Hypothermia is an emergency; suspected signs require medical help as soon as possible, and a body temperature below 35 °C / 95 °F requires immediate medical help.

**Linked records:** `EU-COLD-HYPOTHERMIA-EMERGENCY` → `SRC-CDC-HYPOTHERMIA-EMERGENCY-2026`; also `EU-COLD-HYPOTHERMIA-EMERGENCY-NWS` → `SRC-NWS-COLD-HYPOTHERMIA-2026`.

**External check:** CDC's [Stay Alert for Hypothermia](https://www.cdc.gov/natural-disasters/psa-toolkit/stay-alert-for-hypothermia.html) says to seek emergency care when body temperature is below 95 °F and the person is confused or slurring words. The CDC's [winter-storm safety guidance](https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html) identifies hypothermia as a medical emergency and recommends immediate medical attention for a reading below 95 °F.

**Assessment:** The threshold and escalation are supported. The claim appropriately prioritizes urgent care, but the sentence could make clearer that serious signs of hypothermia warrant urgent action even when a reliable temperature measurement is unavailable; not everyone has a thermometer. The claim's first clause already helps with this, but a Human View check should verify readers do not treat 35 °C as a prerequisite to seeking help.

**Disposition:** No clear factual defect found. Human View check recommended for the “do not wait for a thermometer” interpretation.

### 2. `CLM-COLD-HYPOTHERMIA-SIGNS` — D2 / E2 / B2
**Statement:** Adult warning signs include shivering, exhaustion, confusion, fumbling hands, memory loss, slurred speech and drowsiness.

**Linked record:** `EU-COLD-HYPOTHERMIA-SIGNS` → `SRC-CDC-COLD-HYPOTHERMIA-2026`.

**External check:** CDC's [winter-storm safety guidance](https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html) lists these adult warning signs. It separately notes different signs in infants: bright red, cold skin and very low energy.

**Assessment:** Strong claim-specific Evidence Use and a close match to the source. The statement explicitly limits itself to adults, avoiding the error of applying adult symptoms to infants. The slice should ensure infant signs and first-aid steps are readily findable elsewhere in the same user-facing flow; this individual claim does not establish their absence.

**Disposition:** No immediate content change indicated. Include infant/vulnerable-person navigation in Human View review.

### 3. `CLM-COLD-HYPOTHERMIA-WETNESS` — D2 / E1 / B3
**Statement:** Hypothermia can occur without severe frost; risk increases with prolonged exposure to cold or water, particularly when a person is wet or inadequately protected.

**Linked record:** `EU-COLD-HYPOTHERMIA-WETNESS` → `SRC-NWS-COLD-HYPOTHERMIA-2026`.

**External check:** The National Weather Service's [During Extremely Cold Weather](https://www.weather.gov/safety/cold-during) says hypothermia can occur at temperatures as warm as 60 °F, particularly in water or after prolonged outdoor exposure without suitable clothing, and advises changing into dry clothing immediately when wet. CDC's [Preventing Hypothermia](https://www.cdc.gov/winter-weather/prevention/index.html) states that hypothermia can occur above 40 °F when a person becomes chilled by rain, sweat or cold water.

**Assessment:** The core risk-boundary message is well supported and useful. However, the linked Evidence Use is vague (“the source supports extending the risk boundary beyond severe frost”) rather than identifying the source's concrete evidence about wetness, exposure duration and temperatures. E is therefore low despite the source itself being relevant.

**Disposition:** Confirmed Evidence Use specificity weakness. Correct only in an authorized correction pass; preserve the source-supported message that wetness and prolonged exposure can cause hypothermia even when air temperature is not extreme.

### 4. `CLM-COLD-LIMIT-OUTDOOR` — D1 / E2 / B1
**Statement:** During winter severe weather, time spent outdoors should be limited.

**Linked record:** `EU-COLD-LIMIT-OUTDOOR` → `SRC-CDC-COLD-HYPOTHERMIA-2026`.

**External check:** CDC's winter-storm safety guidance recommends limiting outdoor time during winter storms, and National Weather Service guidance describes layered clothing, covering exposed skin and sheltering from wind.

**Assessment:** The evidence fit is reasonable, and the linked Evidence Use describes the recommendation directly. The claim is too broad to guide action on its own: it does not identify the conditions that make outdoor exposure unsafe, or the importance of shelter, dry layers, exposed-skin protection and local warnings. It should not be read as an absolute rule to remain indoors regardless of circumstances; emergency access and evacuation can change the decision.

**Disposition:** Human View / scope finding. Consider linking this general recommendation to operational guidance for severe weather and emergency travel rather than expanding it into an unconditional command.

## Batch findings
1. The source records point to relevant official CDC and National Weather Service pages, and the reviewed statements are generally directionally supported.
2. `EU-COLD-HYPOTHERMIA-WETNESS` is a confirmed evidence-description weakness: the linked source's concrete basis is not recorded.
3. The emergency claim should be tested for the dangerous misinterpretation that a person must obtain a temperature reading before seeking help.
4. The general “limit outdoor time” claim is not sufficiently operational in isolation. A user-facing sequence should connect it to shelter, dry clothing, warning signs, local conditions and what to do if exposure cannot be avoided.
5. This is a four-claim purposive sample, not a full audit of the slice or the corpus.

## Required follow-up
- Add the wetness claim to the finding-specific Evidence Use correction queue and test it with a dedicated regression.
- Test the hypothermia emergency path in Human View, including absence of a thermometer and signs in infants.
- Check whether the slice provides immediate, safe warming and escalation guidance in a clearly discoverable path; do not infer missing coverage from this sample alone.
- Continue full Claim D/E/B census, high-consequence overlay, Relation review and independent review.

## Audit boundary
Review artifact only. No corpus records were edited. M13 remains open; this batch does not close any audit phase.
