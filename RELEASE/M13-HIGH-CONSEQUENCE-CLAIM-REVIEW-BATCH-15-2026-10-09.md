# M13 High-Consequence Claim Review — Batch 15: Emergency Lighting and Candle Safety
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: four emergency-lighting claims and their linked Evidence Use / Source records.
Review type: targeted safety review. No content records changed.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits and safety boundaries.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-LIGHTING-CANDLE-CHILDREN` — D1 / E1 / B2
**Statement:** Burning candles should be kept out of reach of children and pets.

**Linked record:** `EU-LIGHTING-CANDLE-CHILDREN` → U.S. Fire Administration (USFA).

**External check:** USFA's [Candle Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/) recommends keeping candles where they cannot be knocked down easily and considering battery-operated flameless candles. NFPA's [Candle Safety](https://www.nfpa.org/education-and-research/home-fire-safety/candles) specifically says never to leave a child alone in a room with a burning candle and to keep matches/lighters out of children's reach.

**Assessment:** The recommendation is sound, but the linked Evidence Use only says USFA supports the recommendation; it does not identify the specific source guidance. The statement could be more useful by distinguishing placing candles beyond reach from ensuring that children are never left alone with a burning candle. Pet-specific support should be checked against the chosen source rather than inferred from child-safety guidance.

**Disposition:** Evidence-specificity finding; verify pet-specific source fit and improve the Evidence Use description in the authorized correction pass.

### 2. `CLM-LIGHTING-CANDLE-UNATTENDED` — D1 / E1 / B3
**Statement:** Lit candles must not be left unattended.

**Linked record:** `EU-LIGHTING-CANDLE-UNATTENDED` → USFA.

**External check:** USFA explicitly says to blow out candles when leaving a room or home, or when going to bed. NFPA likewise says to blow out all candles before leaving the room or going to bed.

**Assessment:** Clear, high-value safety instruction with strong direct source support. The Evidence Use is generic rather than claim-specific, but the statement itself is unambiguous and well bounded.

**Disposition:** No substantive claim defect. Low-severity Evidence Use specificity candidate.

### 3. `CLM-LIGHTING-EXTINGUISH` — D2 / E3 / B3
**Statement:** If a lit candle is used, extinguish it before leaving the room or home, when drowsy and before sleep.

**Linked record:** `EU-LIGHTING-EXTINGUISH` → USFA.

**External check:** USFA's current Candle Fire Safety guidance directly states to blow out candles when leaving a room or home, or going to bed. The linked Evidence Use describes these exact conditions.

**Assessment:** Clear, actionable and specifically supported. “When drowsy” is a sensible extension of the sleep-related boundary; the source supports the central actions.

**Disposition:** No immediate content change indicated.

### 4. `CLM-LIGHTING-FLASHLIGHT-OUTAGE` — D2 / E3 / B3
**Statement:** During a power outage, flashlights or battery-powered lighting are preferable to candles for temporary lighting.

**Linked record:** `EU-LIGHTING-FLASHLIGHT-OUTAGE` → NFPA.

**External check:** NFPA's [Candle Safety](https://www.nfpa.org/education-and-research/home-fire-safety/candles) says to have flashlights and battery-powered lighting ready for a power outage and never use candles. USFA and CDC also recommend flashlights rather than candles during outages.

**Assessment:** Strong fit and important safety value. The statement uses “preferable” rather than claiming candles are impossible to use; this is slightly softer than NFPA's “never use candles” advice, but CDC allows a contingency in which candles are used only with strict precautions. A user-facing emergency guide should make the safest default prominent and any fallback subordinate.

**Disposition:** No clear factual defect. Human View should ensure the reader sees battery-powered lighting as the default and the risks of open flame during outages.

## Batch findings
1. The central safety sequence is sound: keep candles away from children/pets, never leave a candle unattended, extinguish it before leaving/sleeping, and prefer battery-powered lights during outages.
2. The first two Evidence Use records contain generic descriptions and should be made claim-specific. This is an auditability issue, not evidence that the recommendations are false.
3. The source for child/pet safety should be checked carefully: evidence that supports keeping children away should not automatically be represented as direct pet-specific support.
4. This sample is about lighting/fire prevention, not the entire power-outage safety picture. Generator placement, carbon monoxide, battery safety and evacuation/exit lighting need their own checks.
5. This is a four-claim purposive sample, not a full audit of the slice or corpus.

## Required follow-up
- Add the first two Evidence Use records to the specific-evidence correction queue.
- Verify the child/pet wording against a source that directly covers both audiences or narrow the claim to what the source says.
- Human View test whether a reader can find and act on “use a flashlight, not a candle” immediately during a power outage.
- Continue the full Claim D/E/B census, high-consequence overlay, Human View, Relation audit and independent review.

## Audit boundary
Review artifact only. No content records were edited. M13 remains open; this batch does not close any audit phase.
