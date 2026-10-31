# M13 Prioritized Claim Review Queue — 2026-10-12

Status: **working review queue assembled from Batch 14–21 metadata/source-fit reports; not a score ledger and not a publication decision.**

## Purpose and limits

The first-pass source-fit triage across inventory rows 651–1494 is recorded in Batches 14–21. This queue converts their follow-up notes into an order of operations so reviewers do not repeat inventory discovery. It is deliberately a queue of **review tasks**, not a claim that any item is false, fixed, scored, or cleared.

Before any item is closed, reconcile the literal Claim ID and version against the current corpus and scored-report ledger. Then inspect the linked current Evidence Use and Source versions, the exact cited passage, applicability/scope, rights, and any required independent Human View. Where a report names only a slice or inventory row, resolve exact IDs from the current inventory before editing.

## Queue A — safety-critical or high-consequence claims (first)

| Work packet | Cases surfaced by the triage reports | Required close condition |
|---|---|---|
| Emergency food safety | Power-outage food; preserve the exact food/appliance/door-opening assumptions and jurisdiction-specific discard thresholds. | Current official passages checked individually; conditions preserved; specialist Human View documented. |
| Medical and mental-health boundaries | Medical devices; mental-health information (including the escalatory Claim); medical imaging; pathology; pharmacology and pharmacovigilance; physiology and plant pathology where practical claims occur. | Exact passages and currentness checked; education distinguished from diagnosis/treatment; escalation and intended-use boundaries reviewed by an appropriate specialist. |
| Electricity, energy and power systems | Power electronics; power systems; energy-related claims carrying existing high-consequence flags. | Exact technical sections and system/geographic boundaries recorded; equipment-selection, grid, and electrical-safety inferences not overstated; specialist review recorded where required. |
| Public-health, privacy and public-safety policy | Public-health ethics, surveillance and risk communication; privacy/data protection; public transport; political science and public budgeting where legal/financial flags apply. | Exact provisions/guidance pinpointed; source lineage/independence checked; jurisdiction, privacy and emergency-context boundaries visible; specialist review where required. |
| Emergency water, sanitation and wastewater | Septic-system flood/no-pump; water-filter limitations; wastewater engineering/treatment; water infrastructure and water-quality criteria; vaccine-safety information noted in the Batch 21 high-consequence queue. | Exact current trigger conditions and official wording verified; no generalized safe-water or maintenance guarantee; engineering/regulatory and specialist Human View completed. |
| Engineering and hazardous-material implications | Safety engineering; structural/timber engineering; woodworking; organic and physical chemistry; papermaking hazards; toxicology. | Exact technical sections, material/condition assumptions, and relevant standards or jurisdiction pinned; no design, handling, or compliance advice without qualified review. |
| Other explicitly flagged high-consequence cases | Optics, particle physics, payment systems, quantum physics, railway systems, rehabilitation and reliability. | Determine why the existing risk flag applies to the specific Claim; verify the exact proposition and limitations. A flag is a routing signal, not a verdict. |

**Rule:** these items remain HOLD for public-pilot consideration until the applicable gates pass. Existing scores, if any, must be preserved and reconciled; exclusion from a batch is not clearance.

## Queue B — source identity or source-fit defects (bounded corrections)

| Case named in reports | Action |
|---|---|
| Market design | Keep the three general Claims on HOLD until suitable theory/academic sources and claim-specific pinpoints are identified; a Nobel announcement is not automatically sufficient for broad market-design propositions. |
| Linear algebra | Replace the sentence-like Source identity with the actual MIT OCW course/publication identity only after checking the current Source version; add lecture/section pinpoints for the specific Claims. |
| Macroeconomics | Correct the sentence-like Source identity to the actual IMF page/publication; map each Claim to the relevant article and pinpoint. |
| Microbiology | Replace the placeholder identity with the actual OpenStax publication identity; add relevant chapter/section pinpoints and separately review rights/reuse. |
| Numerical methods | Keep on HOLD until a technical numerical-analysis source directly supports error, convergence and stability Claims; a broad NIST programme page is not a substitute. |
| Plant biology / plant physiology | Correct placeholder or sentence-like identities to the actual OpenStax book/chapter, then verify whether the specific locator supports all stated transport/physiology propositions. |
| Parasitology and seismology | Correct the Source identity and assess whether the current narrow locator supports the broader Claim; add a suitable general reference where needed. |
| Waves and sound | Replace the placeholder identity with the actual OpenStax book/chapter identity and pinpoint the wave-properties section; add further sections if Claims extend beyond it. |

Do not silently change Source identity, URI, or version in isolation where Evidence Use records depend on the existing version. Make a bounded, versioned correction, preserve history, and run targeted link/reference regressions.

## Queue C — evidence independence and relationship integrity

Compare the actual cited passages and underlying source lineage before retaining any “independent corroboration” characterization. The reports specifically route these areas for review:

- pathology and physiology-of-systems;
- political economy, privacy/data protection, public-health surveillance and public risk communication;
- risk analysis and safety engineering;
- rehabilitation and reproductive-health information;
- wastewater and water-resources evidence pairs.

Different record IDs, publishers, or URLs do not by themselves establish independent evidence. Record what is genuinely distinct (data, authorship, method, or analysis), or narrow the claim about independence.

## Queue D — remaining claim-specific passage work

For all other triaged Claims not covered above:

1. Resolve the exact current Claim/Evidence Use/Source IDs and versions from the current inventory.
2. Confirm that each Evidence Use supports the *whole* proposition at a reproducible page/section/table/paragraph pinpoint.
3. Check source identity, URI destination, currentness, scope, context, qualifiers, and relevant Relations.
4. Review generic descriptions and templated/slice-suffix wording; improve only where a source-grounded correction is clear.
5. Reconcile with prior scores and report IDs; never duplicate or overwrite an existing score.
6. Record a disposition with rationale: supported, revise/narrow, insufficient evidence/HOLD, source defect, duplicate/alias review, or specialist review required.

## Execution protocol and exit criteria

- Work in bounded batches of up to 100 **unique, currently unscored** Claims after the exact ID/version join; prioritize Queue A and broken linkages rather than restarting the metadata inventory.
- A metadata flag is not a D/E/B score. A source title or plausible institution is not passage-level support.
- No canonical record changes are authorized by this queue itself. Any substantive correction must use the established bounded authorization and version/history rules.
- A Claim is not “cleared” until the score ledger, evidence/source links, applicable risk review, rights/attribution, independent Human View and exact-head regression checks are reconciled.
- Keep M13 open until the full agreed audit and release gates are complete. Keep all Draft PRs unmerged and `main` unchanged.

## Current state

- Batches 14–21: first-pass metadata/source-fit triage reports exist for 796 selected Claims in rows 651–1494; this does not mean 796 Claims received final D/E/B scores.
- The inventory-to-ledger figures previously recorded (1,494 Claims, 259 historical score rows, 252 normalized Claim IDs represented, 7 repeated report-ID groups, 1,242 without a score row) are a **historical snapshot**. Rebuild the join from the current head before treating them as a current denominator.
- Next machine task: regenerate the inventory/score join and link findings from one pinned revision; resolve aliases by literal IDs first and use normalization only to flag candidates. Attach the resulting exact-ID register to this queue before starting substantive scoring.
