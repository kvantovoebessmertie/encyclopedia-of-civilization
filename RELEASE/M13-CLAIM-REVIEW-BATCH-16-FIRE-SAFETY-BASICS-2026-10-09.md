# M13 High-Consequence / Foundational Claim Review — Batch 16: Fire-Safety Basics
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: three foundational claims in `fire-safety-basics` and linked Evidence Use records.
Review type: targeted depth and evidence-fit review. No content records changed.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits and prevention of overgeneralization.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM_FIRE_SAFETY_BASICS_A` — D1 / E1 / B2
**Statement:** Fire safety uses measures intended to prevent fires, limit their consequences, and support safe response and evacuation.

**Linked record:** `EU_FIRE_SAFETY_BASICS_A` → `SRC_FIRE_SAFETY_BASICS`.

**Assessment:** This is a reasonable high-level framing, but it is an introductory summary rather than an explanation. The linked USFA source is a broad fire-prevention landing page and the Evidence Use only says that the source supports the claim within its scope. It does not identify the source material supporting each of the three purposes.

**Disposition:** Low-severity depth and evidence-traceability finding. The source identity should remain clear that this is a broad public reference, not a complete technical standard.

### 2. `CLM_FIRE_SAFETY_BASICS_B` — D2 / E1 / B2
**Statement:** Fire-safety measures can include prevention, detection, suppression, compartmentation, evacuation planning and emergency response.

**Linked records:** `EU_FIRE_SAFETY_BASICS_B` → USFA; `EU_FIRE_SAFETY_BASICS_NFPA` → NFPA.

**Assessment:** The categories are plausible and useful as a system overview. However, the primary USFA Evidence Use is generic, and the NFPA Source locator points to an escape-planning page that directly supports evacuation planning but is not by itself a precise source for every listed category. The independent Evidence Use says NFPA corroborates the categories, but does not describe the exact support. This is a source-fit issue, not a finding that the listed categories are wrong.

**Disposition:** Evidence-fit finding. Use a more appropriate specific source for the full list or narrow the description of what each source supports; do not treat a broad source count as corroboration for every component.

### 3. `CLM_FIRE_SAFETY_BASICS_C` — D2 / E1 / B3
**Statement:** Fire-safety decisions depend on hazards, building/site characteristics, occupants, detection and suppression systems, and applicable requirements.

**Linked record:** `EU_FIRE_SAFETY_BASICS_C` → USFA.

**Assessment:** The statement has useful boundary discipline: decisions depend on context rather than a universal checklist. But the Evidence Use is generic and the broad USFA landing page does not provide a traceable claim-specific explanation for all listed dependencies. The claim is also too general to serve as an operational decision rule without linked task-specific guidance.

**Disposition:** Evidence-traceability and depth finding. Preserve the context-dependence principle and connect it to more specific fire-prevention, alarm, suppression and evacuation instructions in the user-facing navigation.

## Batch findings
1. All three USFA-linked Evidence Use records use generic “source supports within scope” language. The weakness is evidence auditability, not established factual falsity.
2. The NFPA evidence record is more transparent that it is intended as independent corroboration, but the stored source URL is specifically an escape-planning page. It should not be represented as broad evidence for detection, suppression or compartmentation without further support.
3. These claims are appropriate as an overview, but they should not be mistaken for a complete fire-safety plan, building-code interpretation or technical suppression design.
4. The adjacent emergency-lighting and home-fire slices cover some practical actions, but this sample does not establish full operational coverage of the fire-safety domain.

## Required follow-up
- Add the three claims to the full D/E/B census and the generic Evidence Use correction queue.
- Verify the exact source fit for each enumerated fire-safety category.
- Human View test whether a novice can move from this overview to the appropriate task-specific guidance without treating the overview as a complete checklist.
- Continue the complete Claim census, high-consequence overlay, Relation audit, Human View review and independent review.

## Audit boundary
Review artifact only. No content records were edited. M13 remains open; this batch does not close any audit phase.
