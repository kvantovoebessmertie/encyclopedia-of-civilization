# P10 SUBSTANTIVE AUDIT — ITERATION 1

**Date:** 2026-10-07
**Candidate:** 28197fc15c134d4106dfe22cd9692566ace46ec5
**Status:** OPEN — substantive audit in progress

## Scope
Ten P10 maturation slices: political-economy-basics, comparative-law-basics, administrative-law-basics, international-law-basics, civil-society-basics, social-policy-basics, taxation-basics, labor-economics-basics, migration-and-mobility-basics, economic-history-basics.

## Checks completed

- All ten selected slices exist and retain their intended single-slice structure.
- Each selected slice has Claims, Evidence Use, Source, Context and Scope records.
- README applicability boundaries are present and appropriately distinguish educational knowledge from individualized legal, tax, migration, political or financial action.
- CI baseline at the start of this audit was 3/3 GREEN.
- Source provenance was inspected rather than inferred from the word INDEPENDENT.
- Five weak source-pair classifications were corrected: comparative law, international law, civil society, taxation, and labor economics now use sources from a different institutional provenance.
- The changes preserve existing Claims and do not create duplicate vertical slices.

## Substantive findings

### S-01 — Independence of corroborating evidence
**Finding:** Several P10 sources originally labelled as independent were from the same institutional family as the primary source.
**Resolution:** Corrected five independent-source records to genuinely different institutional provenance.
**Status:** CLOSED after correction; requires CI re-run and final re-audit.

### S-02 — Claim depth
The selected Claims are concise and non-template in wording, but P10 closure must verify that B/C claims provide mechanisms, conditions and limitations rather than merely restating the A definition.
**Status:** OPEN for full claim-by-claim re-audit.

### S-03 — Locator/material specificity
Evidence Use records currently provide source references and bounded descriptions, but the final audit must verify that the source material is sufficiently specific for each claim and does not rely only on source-level reputation.
**Status:** OPEN.

### S-04 — Applicability and uncertainty
README boundaries are present and generally strong. Final audit must verify that uncertainty is also visible inside claims/evidence where a statement is jurisdiction-, period-, methodology- or definition-sensitive.
**Status:** OPEN.

### S-05 — Cross-slice linkage
Existing corpus linkage baseline remains 34 Relation records. P10 added maturation evidence without adding relations. Final audit must independently verify whether any high-value P10 relations are missing and must not manufacture edges merely to increase the count.
**Status:** OPEN.

## Decision
P10 is not closed. Continue with full substantive claim/evidence re-audit, Human View/adversarial audit, Unified Debt Map, debt closure, re-audit, documentation/coverage synchronization, full regression, CLEAN checkpoint and independent Reference + Release Gate + Offline 3/3.
