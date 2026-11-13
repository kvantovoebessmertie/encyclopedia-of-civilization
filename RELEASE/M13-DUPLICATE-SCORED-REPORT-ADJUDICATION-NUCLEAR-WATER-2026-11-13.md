# M13 duplicate scored-report adjudication review — nuclear physics and water treatment

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Review basis: historical Batch 12/17/21/27 reports; current canonical Claim, Evidence Use and Source records at the branch HEAD before this report; current M13 D/E/B rubric; official WHO/EPA source pages checked on 2026-11-13.
Status: **desk-review reconciliation proposal; not independent adjudication, not a canonical score update, and not release approval.**

## 1. Purpose and limits

This review examines six of the seven duplicate scored-report groups: three nuclear-physics Claims scored in Batches 12 and 17, and three water-treatment Claims scored in Batches 21 and 27. The seventh group, `CLM-M5-WATER-EMERGENCY-DISINFECTION-D`, is also assessed below because its duplicate rows have identical scores.

The review compares the original rationales with the current Claim/Evidence Use/Source chain. Historical rows are preserved. No canonical JSON, score ledger, or prior report is changed by this document. Proposed score reconciliation remains provisional pending independent review against the rubric.

## 2. Nuclear-physics Claims — Batches 12 and 17

All three current Evidence Use records still contain the same generic description: “Источник используется в пределах заявленного материала.” Each points to the same Source record, whose identity is “Nuclear science — IAEA” and whose URI is a broad IAEA topic page. The current evidence chain therefore does not identify a claim-specific passage for any of the three propositions.

| Claim | Batch 12 | Batch 17 | Current record-level observation | Provisional reconciliation |
|---|---:|---:|---|---|
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A` | D1/E1/B2 | D2/E1/B2 | The statement is a concise subject definition; it names the field and its objects but does not explain a mechanism or distinguish subdomains. | Prefer D1 over D2 under the current D rubric; retain E1; B2 remains defensible. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B` | D2/E1/B3 | D2/E1/B2 | The statement identifies a possible emission and explicitly limits process character by nucleus and transition. The wording is bounded but does not enumerate exceptions or explain the transition mechanism. | Retain D2/E1; prefer B2 over B3 because the stated qualifications are meaningful but do not meet the rubric's strongest boundary level. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C` | D1/E1/B3 | D2/E1/B2 | The statement makes a useful distinction among mechanism, measured quantity and experimental conditions, but gives no worked example or source-grounded explanation. | D2 is more consistent with the explicit distinction/limitation in the statement; retain E1; prefer B2 over B3. |

### Nuclear-physics disposition

- The E1 findings are stable across both historical reviews and are confirmed by inspection of the current canonical Evidence Use text.
- The broad IAEA topic page may serve as background, but it is not mapped to a precise passage for these three claims. It cannot, by itself, justify raising E.
- Proposed reconciliation of D/B is a reasoned desk-review recommendation, not an independently approved replacement score. The historical rows must remain intact and linked to this adjudication decision once an independent reviewer confirms or rejects it.
- All three Claims remain **HOLD** for evidence remediation. No content rewrite is proposed here.

## 3. Water-treatment Claims — Batches 21 and 27

The current canonical Claim statements are unchanged at version 1. The current Evidence Use records are more specific than the nuclear records, but none contains an exact section, paragraph, table, figure or page locator.

| Claim | Batch 21 | Batch 27 | Current chain finding | Provisional reconciliation |
|---|---:|---:|---|---|
| `CLM-WATER_TREATMENT_BASICS-A` | D2/E2/B3 | D2/E3/B3 | EU-A describes WHO's public-health/water-quality context, but links only to the WHO programme landing page and supplies no pinpoint. | D2/B3 stable. E3 is not established by the current trace; retain at most provisional E2 pending a pinpointed source passage. |
| `CLM-WATER_TREATMENT_BASICS-B` | D2/E3/B3 | D3/E3/B3 | EU-B says WHO is primary and EPA supports the narrower point, but its only `source_ref` is `SRC-WATER_TREATMENT_BASICS` (WHO). The EPA source is not registered in this Evidence Use chain. | D3 is not yet justified by the short Claim statement alone; D2 is the safer current-rubric reading. E3 is unsupported until the EPA source is separately registered/linked and pinpoints are verified; provisional E2 at most. |
| `CLM-WATER_TREATMENT_BASICS-C` | D2/E2/B3 | D2/E3/B3 | EU-C describes the water-quality/use-dependent boundary and links to WHO's programme page, but has no exact locator or independent corroboration in the linked chain. | D2/B3 stable. E3 is not established; provisional E2 at most, pending pinpoint verification. |

### Water-treatment source check

The current WHO programme landing page is broad. More specific official material is available:
- WHO, *Guidelines for drinking-water quality*, fourth edition incorporating the third addenda (2026), section 4.2.4 “Treatment”, describes treatment processes, hazards that can pass through treatment, and control measures including pretreatment, coagulation, flocculation, sedimentation, filtration and disinfection: https://cdn.who.int/media/docs/default-source/wash-documents/water-safety-and-quality/dwq-guidelines-4/gdwq_4ed_with_third-addenda_water-safety-plans.pdf
- U.S. EPA, “Overview of Drinking Water Treatment Technologies”, describes contaminant-specific technologies and their operating limits, for example granular activated carbon, aeration, ion exchange, biological treatment, reverse osmosis/nanofiltration and adsorptive media: https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies

These pages support the general concepts behind the water-treatment Claims. They do not retroactively fix the current Evidence Use records: the WHO guideline is not the Source currently linked in the canonical records, and the EPA page mentioned in EU-B is not linked by its `source_ref`. Source registration, exact version/locator and any canonical correction require a separate bounded authorization and regression coverage.

### Water-treatment disposition

- Preserve Batch 21 and Batch 27 as separate historical reviews.
- Do not treat the higher Batch 27 E scores as accepted merely because the later report has more detailed prose.
- For A and C, the source descriptions are claim-related but the current linked Source locator is too broad for a reproducible passage-level trail.
- For B, the EU's mention of EPA without a corresponding EPA `source_ref` is a source-lineage inconsistency. Do not count it as linked independent corroboration.
- All three Claims remain **HOLD** pending exact locators and source-chain reconciliation.

## 4. Identical duplicate: emergency-water disinfection

`CLM-M5-WATER-EMERGENCY-DISINFECTION-D` has identical D3/E3/B3 rows in Batches 21 and 27. The current Claim is linked to an EPA Evidence Use whose description explicitly distinguishes microbial disinfection from heavy metals, salts and most chemicals.

Recommended ledger disposition: retain both report rows, mark Batch 27 as a later reaffirmation of the same score rather than independent corroboration, and do not count the repeated row as a second independent assessment. Recheck the exact EPA passage and the basis for E3 under the current rubric before treating the score as current.

## 5. Consolidated proposed ledger decisions

1. Nuclear A: resolve historical D conflict provisionally to D1; E1/B2 unchanged.
2. Nuclear B: retain D2/E1; resolve B conflict provisionally to B2.
3. Nuclear C: resolve D conflict provisionally to D2 and B conflict provisionally to B2; E1 unchanged.
4. Water-treatment A: D2/B3 stable; E3 not substantiated by the current chain; E2 at most pending pinpoint.
5. Water-treatment B: D2 preferred over D3; E3 not substantiated because EPA is described but not linked; E2 at most pending source-chain repair and pinpoint.
6. Water-treatment C: D2/B3 stable; E3 not substantiated by the current chain; E2 at most pending pinpoint.
7. Emergency-water disinfection D: mark duplicate identical score row as repeated historical review, not independent corroboration; revalidate E3 against current rubric.

These are **proposals for independent adjudication**, not final scores. The original rows remain preserved, and the full 1,494-Claim denominator is unchanged.

## 6. Required next actions

- Obtain independent review of the seven proposed dispositions and record reviewer identity, date, rubric version and rationale.
- If confirmed, add a separate adjudication ledger entry; do not delete or overwrite the historical reports.
- For water-treatment B, separately authorize and implement a Source/Evidence Use lineage correction if the EPA source is intended to be part of the evidence chain.
- Add exact source pinpoints only after confirming the exact WHO/EPA edition and passage. Run Claim/Evidence Use/Source linkage and offline export regressions on the correction branch.
- Keep all affected Claims out of any pilot allowlist until their evidence chains and Human View requirements are resolved.

## 7. Audit boundary

This is a desk-review reconciliation of historical scoring conflicts and current record contents. It is not an independent review, specialist certification, live user test, or release decision. No canonical records or scores were changed. M13 remains **IN PROGRESS**.
