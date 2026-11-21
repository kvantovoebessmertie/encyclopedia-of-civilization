# M13 — 200-report cohort structural closure checkpoint

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Source tree head immediately before this checkpoint artifact: `034cc1b1540b0b8f28818e1aa5680e5dfa8f068a`

## Final result for this cohort

**The Batch 42–43 200-report cohort is closed for report-body inspection, normalized Claim-ID reconciliation and primary current Claim → EU → Source graph identity.**

| Control | Result |
|---|---:|
| Batch 42 report rows individually inspected | 100/100 |
| Batch 43 report rows individually inspected | 100/100 |
| Total report rows | 200/200 |
| Batch 42 current primary graph chains | 100/100 |
| Batch 43 current primary graph chains | 100/100 |
| Total primary graph chains | 200/200 |
| Unique normalized Claim IDs | 200 |
| Duplicate normalized Claim-ID groups in this cohort | 0 |
| Primary chain version/linkage mismatches | 0 |
| Current accepted D/E/B assessments from this structural work | 0 |
| Canonical record mutations in this closure | 0 |

The only Claim@2 in the 200 report headers is Batch 43 row 098 (hydrology). The other 199 Claim report references are @1. Multi-EU/multi-Source branches remain separate and are not collapsed.

## Durable artifacts

1. `M13-BATCH-42-68-CHAIN-RECONCILIATION-AND-STRUCTURAL-CLOSURE-2026-11-21.md` — direct JSON and graph audit for the remaining 68 Batch 42 rows. 68 Claims, 69 Evidence Use records and 54 distinct Source records were read; 191 distinct record IDs resolved; all ID/version/provenance links matched.
2. `M13-BATCH-42-43-MASTER-NORMALIZED-CROSSWALK-200-REPORTS-2026-11-21.md` — full 200-row normalized Claim crosswalk, unique-ID accounting and multi-edge preservation.
3. `M13-BATCH-42-43-TARGETED-SOURCE-FIT-ADJUDICATION-2026-11-21.md` — direct official-source rechecks for CPSC, USFA, NFPA, EPA, FDA and WHO, including confirmed source-fit defects, direct alternate source candidates and one positive source-fit verification.
4. `M13-BATCH-43-CURRENT-CANONICAL-GRAPH-RECONCILIATION-ROWS-001-100-2026-11-21.md` — corrected row 012 WHO URI interpretation and row 081 FDA partial-support finding.
5. `M13-BATCH-42-CURRENT-CANONICAL-GRAPH-RECONCILIATION-ROWS-069-100-2026-11-21.md` — previously verified final 32 Batch 42 graph rows.

The earlier checkpoint `M13-200-REPORTS-INSPECTED-132-CANONICAL-GRAPH-CHAINS-VERIFIED-CHECKPOINT-2026-11-21.md` remains a valid historical snapshot as of 132/200; this checkpoint supersedes it for current cohort status.

## Material source-fit adjudications

- Batch 42 row 018: current CPSC Source does not contain generator refuelling/cooling instruction; a separate January 23, 2026 CPSC page directly does.
- Batch 42 row 021: current USFA Source URI is smoke alarms; a dedicated USFA home-fire-escape page directly supports the Claim.
- Batch 42 row 022: current NFPA URI is broad; a dedicated NFPA escape-planning page is available.
- Batch 42 row 025: EPA's Primer for Municipal Wastewater Treatment Systems, printed page 10, directly describes physical, biological and chemical processes.
- Batch 42 row 030: January 23, 2026 CPSC page directly recommends flashlights/lanterns instead of candles during outages.
- Batch 42 row 059: current WHO Clinical Trials page directly supports the core definition; the EU should gain an explicit “Overview” locator.
- Batch 42 row 068: current WHO participatory-surveillance Source is not a direct epidemiology definition; WHO Basic Epidemiology, Chapter 1, Box 1.2 is a direct candidate.
- Batch 43 row 012: the row report's quoted WHO URL omits a path segment and returns 404; the canonical Source URI is correct and identical at its 2026-10-05 introduction commit and current head. No unversioned Source mutation was observed; EU locator remains open.
- Batch 43 row 081: current FDA secondary EU's Source URL states refrigerator 40°F but not freezer 0°F; a different FDA page states both, but is not the current canonical Source.

These findings do not authorize canonical changes. Any new Source/EU edge or versioned correction requires bounded authorization, preflight, regression coverage and exact-head CI.

## Remaining M13 work — not closed by this checkpoint

- Full 1,494-Claim inventory and historical ledger reconciliation beyond this 200-report cohort.
- The 496 generic-EU cohort and 356 residual rows.
- Semantic duplicate adjudication across different Claim IDs and broader historical batches.
- Full passage-level source-fit and locator review for the remaining report rows.
- Evidence diversity and source independence.
- High-consequence risk review and specialist review.
- Rights, attribution and licensing decisions.
- Independent Human View and adversarial review.
- Exact-head CI and final release gates.

## Integrity controls

- `main` remains `d58289f319993ede5294a46f4741a506fd2fd710`.
- PR #21 remains Open / Draft / Unmerged.
- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was changed by the 200-report closure.
- No historical D/E/B value was transferred into current accepted assessments.
- No Claim received publication or release clearance.
- M13 remains OPEN and is not CLEAN.

