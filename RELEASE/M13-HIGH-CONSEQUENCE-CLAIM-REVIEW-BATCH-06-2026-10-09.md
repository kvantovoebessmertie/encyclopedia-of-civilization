# M13 High-Consequence Claim Review — Batch 06
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: four home-fire escape / smoke-alarm claims and linked Evidence Use records.
Review type: purposive high-consequence sample. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** hazard explanation and actionable usefulness.
- **E — evidence fit (0–3):** support for the exact claim from the linked source and Evidence Use.
- **B — boundaries / epistemic discipline (0–3):** appropriate qualifications and scope.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-HOME-FIRE-ESCAPE-PLAN` — D2 / E2 / B2
**Statement:** A home fire escape plan should account for two exits from every room, be known by everyone in the home, and be practiced regularly.
**Evidence Use:** `EU-HOME-FIRE-ESCAPE-PLAN` says USFA recommends mapping the home, identifying two exits from each room, selecting an outdoor meeting place, and practicing the plan.
**External check:** USFA's specific [Home Fire Escape Plans](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/) page supports mapping doors/windows, two ways out, a meeting place, and practice. NFPA's [escape planning guidance](https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning) also supports planning and practice.
**Assessment:** The substance is supported, but the stored source record `SRC-USFA-HOME-FIRE-2026` currently points to the USFA **Smoke Alarms** page rather than the dedicated escape-plan page. The statement's “должен учитывать два выхода” could also sound like an absolute requirement; source guidance is better represented as identifying two ways out where feasible, with routes that are actually usable by the occupants.
**Disposition:** Flag source locator correction and qualification review; preserve the two-route planning objective.

### 2. `CLM-HOME-FIRE-LEAVE-STAY-OUT` — D3 / E2 / B2
**Statement:** If a smoke alarm sounds or a fire is discovered, exit, stay outside, call the fire service, and do not re-enter.
**Evidence Use:** `EU-HOME-FIRE-LEAVE-STAY-OUT` describes NFPA's matching guidance.
**External check:** NFPA says to get out immediately when the alarm sounds, stay out, and tell dispatchers if someone is missing. See [NFPA escape planning](https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning) and USFA's [home escape-plan guidance](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/).
**Assessment:** Clear, actionable, high-value emergency advice. The claim is supported by the specific NFPA escape-planning content, but the stored source record points only to the generic [NFPA home-fire-safety landing page](https://www.nfpa.org/education-and-research/home-fire-safety). The precise canonical page should be recorded.
**Disposition:** Source locator / source identity maintenance, not a substantive claim defect.

### 3. `CLM-HOME-FIRE-SMOKE-ALARMS` — D2 / E2 / B3
**Statement:** Smoke alarms should be inside and outside each sleeping area and on every level, including the basement.
**Evidence Use:** `EU-HOME-FIRE-SMOKE-ALARMS` gives the same specific placement rule and links it to USFA.
**External check:** USFA's current [Smoke Alarms](https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/) page directly states this placement guidance and recommends interconnected alarms. It also notes local requirements may vary.
**Assessment:** Strong fit and appropriately framed as a recommendation rather than a universal legal code statement. The source URL matches this claim. The corpus could benefit from the associated operational details (monthly testing, replacement, interconnection), but this sample alone cannot establish whether they are missing elsewhere.
**Disposition:** No immediate content change indicated.

### 4. `CLM-HOME-FIRE-TWO-WAYS-NFPA` — D2 / E2 / B2
**Statement:** The escape plan should provide two possible ways out of each room, if possible, and account for exit accessibility.
**Evidence Use:** `EU-HOME-FIRE-TWO-WAYS-NFPA` says NFPA recommends two ways out and considering whether doors/windows are usable.
**External check:** NFPA recommends identifying two ways out of each room if possible, clearing routes, checking doors/windows, and planning for children, older adults, and people with mobility limitations. See [NFPA escape planning](https://www.nfpa.org/education-and-research/home-fire-safety/escape-planning).
**Assessment:** Good qualification (“if possible”) and appropriate accessibility framing. The Evidence Use is specific enough in meaning, but the source record `SRC-NFPA-HOME-FIRE-2026` stores a broad landing-page URL rather than the direct escape-planning page.
**Disposition:** Verify / improve canonical source locator. No substantive rewrite indicated from this sample.

## Batch findings
1. The four claims form a coherent safety sequence: prepare a plan, ensure alarms are placed appropriately, know usable exits, and leave/stay outside during an incident.
2. Two separate source records have locator precision issues: USFA source record points to a smoke-alarm page while supporting escape-plan claims; NFPA source record points to a general landing page while supporting detailed escape-planning claims. The underlying claims are independently corroborated by official pages, but a traceable evidence system should point to the exact page supporting each claim.
3. The broad statement “two exits from every room” should be carefully qualified to avoid presenting guidance as an absolute legal/building requirement or ignoring real accessibility constraints. The parallel NFPA claim already uses “if possible.”
4. A Human View audit should check whether a reader can find an outside meeting point, assistance for occupants with limited mobility, and a “stay outside / tell dispatch if someone is missing” instruction without reading architecture or source records.

## Required follow-up
- Correct or split the source locators so escape-plan claims point to the dedicated USFA / NFPA escape-planning pages and smoke-alarm placement points to the USFA smoke-alarm page.
- Review consistency between `CLM-HOME-FIRE-ESCAPE-PLAN` and `CLM-HOME-FIRE-TWO-WAYS-NFPA`, especially the “if possible” boundary.
- Continue full claim-level D/E/B scoring, cross-record relation review, and Human View testing. This batch does not close any audit phase.

## Audit boundary
Review artifact only. No corpus records were edited. M13 remains open; no merge or protected checkpoint is authorized.
