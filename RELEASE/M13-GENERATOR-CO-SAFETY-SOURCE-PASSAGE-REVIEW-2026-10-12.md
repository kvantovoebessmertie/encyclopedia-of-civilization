# M13 Generator CO-Safety Source-Passage Review — 2026-10-12

Status: **bounded source-passage review; no D/E/B score change, no canonical record edits, no publication clearance.**

Branch: `m13-system-wide-depth-audit-2026-10-09`

Review scope: four existing Claims in `generator-carbon-monoxide-safety`, their current version-1 Evidence Use records, and the current version-1 CDC/CPSC Source records. Official CDC and CPSC pages were reviewed on 2026-10-12. This is not a specialist Human View.

## Results

| Claim ID/version | Evidence Use ID/version | Source ID/version | Passage-level finding | Disposition |
|---|---|---|---|---|
| `CLM-GENERATOR-NO-INDOOR` v1 | `EU-GENERATOR-NO-INDOOR` v1 | `SRC-CDC-GENERATOR-CO-2026` v1 | Directly supported by CDC's “What to Do to Protect Yourself During a Power Outage,” section “Carbon monoxide poisoning,” subsection “Never use a generator or other gasoline-powered engines inside your home” (paragraph and bullets). CDC expressly prohibits use inside a home, basement or garage, including where doors/windows are open, and explains accumulation in enclosed or partly enclosed spaces. | Substance supported. Add reproducible locator to a versioned Evidence Use correction under the established process. |
| `CLM-GENERATOR-OUTSIDE-20FT` v1 | `EU-GENERATOR-OUTSIDE-20FT` v1 | `SRC-CDC-GENERATOR-CO-2026` v1 | Directly supported by the same CDC subsection, bullet beginning “Never use a generator…”; CDC specifies at least 20 feet from any window, door or vent. CDC's “Use a Generator Safely” page also repeats the 20-foot guidance. | Substance supported. Add reproducible locator to a versioned Evidence Use correction. Preserve the scope as generator use and the stated distances/openings. |
| `CLM-GENERATOR-CO-ALARM-EMERGENCY` v1 | `EU-GENERATOR-CO-ALARM-EMERGENCY` v1 | `SRC-CDC-GENERATOR-CO-2026` v1 | **Partial source-to-Claim mismatch.** CDC's page supports urgent medical/poison-control help for signs of CO poisoning (subsection “Know what to do”), but the reviewed CDC page does not itself say that a sounding CO alarm requires immediate evacuation. CPSC's “Check Carbon Monoxide and Smoke Alarms” section says never ignore an alarm, get outside immediately, then call 911. The present Evidence Use points only to CDC. | Do not mark fully closed. Add/resolve the appropriate alarm-specific source and its exact locator through a versioned, authorized change; preserve separate symptom and alarm triggers. |
| `CLM-GENERATOR-REFUEL-COOL` v1 | `EU-GENERATOR-REFUEL-COOL` v1 | `SRC-CPSC-GENERATOR-2026` v1 | **Current source does not support the whole Claim at the reviewed locator.** The linked 2026 CPSC “Ahead of Hurricane Season” release covers generator CO, placement, alarms and wet-weather shock hazards, but contains no generator refuelling/cooling instruction in its relevant generator-safety section. CPSC's separate “Portable Generator Hazards” safety alert does say to turn the generator off and let it cool before refuelling, explaining that spilled gasoline can ignite on hot engine parts. | Keep HOLD. Identify and version the appropriate CPSC safety-alert Source, then add a precise locator and reconcile Evidence Use under the established correction process. Do not silently repoint the existing Source record. |

## Official passages checked

1. CDC, “What to Do to Protect Yourself During a Power Outage”: https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html  
   - “Carbon monoxide poisoning” and “Never use a generator or other gasoline-powered engines inside your home” — prohibition on indoor use, enclosed-space accumulation and 20-foot separation.
   - “Know what to do” — seek emergency help / poison-control guidance when someone shows signs of CO poisoning.
2. CDC, “Use a Generator Safely”: https://www.cdc.gov/natural-disasters/psa-toolkit/use-a-generator-safely.html  
   - Key points/script: keep the generator outside at least 20 feet from doors, windows or vents.
3. CPSC, “CPSC Warns of Generator, Carbon Monoxide and Fire Hazards Ahead of Hurricane Season” (May 27, 2026): https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Warns-of-Generator-Carbon-Monoxide-and-Fire-Hazards-Ahead-of-Hurricane-Season  
   - “Loss of Power—Using a Generator Safely” and “Check Carbon Monoxide and Smoke Alarms”: generator placement and instruction to get outside immediately when an alarm sounds, then call 911.
4. CPSC, “Safety Alert: Portable Generator Hazards”: https://www.cpsc.gov/s3fs-public/5123_SafetyAlert_PortableGenerators_102021.pdf  
   - “Fire Hazards”: before refuelling, turn the generator off and let it cool; gasoline spilled on hot engine parts could ignite.

## Structural and evidence-quality findings

- The four Claim/Evidence Use links and the referenced Source IDs/versions are structurally resolvable in the reviewed slice.
- The Evidence Use descriptions do not provide reproducible page/section locators.
- Two Claims are substantively supported by the current CDC page, but need exact locators for a reproducible evidence trail.
- The alarm/symptom Claim combines two triggers whose direct support is split across different official guidance. Its current single-source link is incomplete for the alarm trigger.
- The refuelling Claim's present CPSC Source is relevant to generator hazards generally but does not support the specific refuelling instruction. A different official CPSC safety alert does support it; that does not authorize silently changing the canonical Source record.
- CDC and CPSC are distinct publishers, but this review does not automatically characterize their guidance as independent corroboration. They are cited here for specific, different sub-propositions.
- Because CO poisoning and refuelling fire hazards are high-consequence, all four Claims remain **HOLD for public-pilot clearance** until locators/source links are corrected through authorized versioned changes, source history is preserved, and an appropriate independent Human View reviews the emergency-use boundaries.

## Decision

- Source-fit: two Claims provisionally supported; one Claim has an incomplete source link for its alarm trigger; one Claim's current Source does not support its refuelling proposition.
- D/E/B: no scores assigned or changed by this report.
- Canonical Claim/Evidence Use/Source JSON: unchanged.
- Public MVP allowlist: do not add these records on the strength of this review alone.
- Next bounded action: prepare proposed, versioned Evidence Use/Source corrections and regression tests after the established authorization/review step; then rerun exact-head CI and obtain the required Human View.
