# M13 High-Consequence Claim Review — Batch 05
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: generator carbon-monoxide and refuelling safety; four claim records and their linked Evidence Use records.
Review type: purposive high-consequence sample, not a substitute for the full claim census. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** how far the claim explains the hazard and actionable response.
- **E — evidence fit (0–3):** how specifically the linked source and Evidence Use material support the exact statement.
- **B — boundaries / epistemic discipline (0–3):** whether scope and limits are clear and the wording avoids unsupported certainty.
- Scores are reviewer judgments for triage, not automated facts or a population-wide quality estimate.

## Claim-level review

### 1. `CLM-GENERATOR-NO-INDOOR` — D2 / E3 / B3
**Statement:** Do not use a generator inside a home, basement, or garage because combustion products can cause CO to accumulate.
**Evidence Use:** `EU-GENERATOR-NO-INDOOR` says CDC explicitly prohibits use in those spaces and explains accumulation in enclosed or partly enclosed areas.
**External check:** CDC guidance says never use a generator inside a home or garage, even with doors/windows open, and identifies CO accumulation in enclosed or partly enclosed spaces. See [CDC — power-outage safety](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html) and [CDC — CO poisoning basics](https://www.cdc.gov/carbon-monoxide/about/).
**Assessment:** Strong claim-to-source fit and practical wording. The statement is concise and does not imply that opening doors/windows makes indoor use safe.
**Disposition:** No content change indicated by this sample.

### 2. `CLM-GENERATOR-OUTSIDE-20FT` — D2 / E3 / B2
**Statement:** Operate outdoors, at least 20 feet from windows, doors, and vents.
**Evidence Use:** `EU-GENERATOR-OUTSIDE-20FT` names CDC and directly describes the same distance and openings.
**External check:** CDC states that generators should be outdoors more than 20 feet from windows, doors, and vents. The linked CDC source also warns against indoor use. See [CDC — power-outage safety](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html).
**Assessment:** Evidence fit is strong. Boundary score is 2 rather than 3 because the claim is a short rule and does not itself surface related practical controls (exhaust directed away from buildings, CO alarms, local product instructions). Those may exist elsewhere in the corpus and must be checked in the Human View audit before concluding that coverage is missing.
**Disposition:** Check cross-record usability and redundancy; do not treat related controls as absent based on this claim alone.

### 3. `CLM-GENERATOR-CO-ALARM-EMERGENCY` — D2 / E2 / B1
**Statement:** If a CO alarm sounds or symptoms suggest CO poisoning while using a generator, immediately get to fresh air and seek emergency medical help; do not return until the space has been checked for safety.
**Evidence Use:** `EU-GENERATOR-CO-ALARM-EMERGENCY` says CDC supports leaving the space and seeking emergency assistance.
**External check:** CDC describes common symptoms and says to call 911 or a poison-control center / obtain prompt medical help if CO poisoning is suspected. CDC materials also say to leave immediately when an alarm sounds. See [CDC — power-outage safety](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html) and [CDC — CO poisoning basics](https://www.cdc.gov/carbon-monoxide/about/).
**Assessment:** The escape and medical-escalation elements have support. However, the final instruction, “do not return until the space has been checked for safety,” is not explicitly substantiated by the linked Evidence Use description or the checked CDC passage. It is prudent safety advice, but the audit must distinguish sound advice from source-backed representation. The phrase “while using a generator” could also be read too narrowly: symptoms or an alarm require action even if the generator has already been switched off.
**Disposition:** Flag for a targeted content/evidence pass. Either add a reliable source that explicitly supports re-entry only after the area is determined safe, or revise Evidence Use and wording so the source-backed scope is transparent. Preserve the clear immediate-evacuation and medical-help instruction. Consider phrasing symptoms broadly enough to cover suspected exposure, not only symptoms noticed during active generator use.

### 4. `CLM-GENERATOR-REFUEL-COOL` — D2 / E2 / B2
**Statement:** Never refuel while the generator is running; switch it off and allow the engine to cool before refuelling.
**Evidence Use:** `EU-GENERATOR-REFUEL-COOL` says the source supports the separate fire risk and the need to switch off and cool before refuelling.
**External check:** CPSC generator guidance states not to refuel a generator while running and to turn it off and let it cool before refuelling. See [CPSC — generator, furnace and space-heater safety](https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters).
**Assessment:** The claim is well aligned with official guidance. The linked local source record points to a differently titled 2026 CPSC hurricane-season release; the safety rule was independently corroborated on the current CPSC page, but the precise locator stored in `SRC-CPSC-GENERATOR-2026` should be verified against the source identity before a full evidence-diversity / lifecycle pass.
**Disposition:** No immediate claim rewrite indicated; verify source-record identity/locator and retain claim-specific Evidence Use.

## Batch findings
1. Three claims have clear claim-specific evidence descriptions, a positive contrast to boilerplate Evidence Use patterns seen in earlier batches.
2. The emergency-response claim contains a potentially unsupported re-entry condition. This is the only concrete claim-level correction candidate from this batch; it is not yet changed.
3. Source identity and source locator are separate audit dimensions: a claim can be independently corroborated while its local source record still needs canonical-URL verification.
4. Generator safety should be assessed as a connected Human View path: placement, CO alarms, symptoms, evacuation, emergency response, refuelling, and safe re-entry must be findable as one practical sequence. This batch does not establish whether the complete path is present elsewhere.

## Required follow-up
- Verify the canonical identity and URL for `SRC-CPSC-GENERATOR-2026`.
- Reconcile the unsupported re-entry clause in `CLM-GENERATOR-CO-ALARM-EMERGENCY` with a source-specific Evidence Use record or a narrowed claim.
- In the Human View pass, test whether a person encountering a CO alarm or symptoms can quickly find evacuation and medical escalation steps without navigating the architecture.
- Continue the full D/E/B census; this batch is only four purposively selected claims.

## Audit boundary
This is a review artifact on the M13 branch. It does not modify the corpus, does not close M13, and does not authorize merge or a protected checkpoint.
