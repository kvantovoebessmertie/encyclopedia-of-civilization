# M13 Batch 41 — Initial Source-Fit Spot Check
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: diagnostic source-fit work only; **not a scored batch and not an accepted unique-Claim count**.

## Scope and guardrail
Inspected five candidate Claim records from the frozen Batch 41 worklist, their linked Evidence Use records, and Source records. The first five checked Claim files have `record_type: claim` and exact filename/internal `record_id` agreement. This sample does not resolve prior-score exclusions or authorize Batch 41 scoring. No content records were modified.

## Findings

### Acid-base basics — three Claims
- `CLM-ACID_BASE_BASICS-A`: Brønsted–Lowry acid/base definition. The linked OpenStax Chemistry 2e chapter 14 summary directly defines acids as proton donors and bases as proton acceptors. The source fit is substantively appropriate. The linked EU description remains generic and does not give the exact section (14.1) or passage.
- `CLM-ACID_BASE_BASICS-B`: pH is defined through hydrogen-ion activity, with concentration as a limited approximation. The linked IUPAC Gold Book record independently supports the activity-based definition; the OpenStax chapter summary also describes pH in terms of hydronium concentration in aqueous solutions. This is a good example of why the IUPAC corroboration must be followed through its own `claim_ref`, rather than assumed from being in the same slice. The OpenStax-linked EU description is generic; the separate IUPAC EU is more specific but could identify the exact Gold Book term/version more explicitly.
- `CLM-ACID_BASE_BASICS-C`: buffer response to small additions of acid/base. OpenStax chapter 14 summary directly supports the weak conjugate acid-base pair and slight pH change after small additions; it also states that sufficiently large additions can exceed buffer capacity. The linked EU description is generic and should identify section 14.6 / the buffer-capacity boundary in a later authorized correction.

### Acoustics basics — two Claims
- `CLM-ACOUSTICS_BASICS-A`: noise as an environmental factor affecting health and well-being. WHO's Environmental Noise Guidelines page identifies noise as a public-health issue and summarizes health impacts, supporting the general proposition. The EU description is generic and has no pinpoint to the guidelines' overview or health-effects sections.
- `CLM-ACOUSTICS_BASICS-B`: noise sources and levels differ by place, time, and activity. The WHO guideline's scope covers multiple source categories (road traffic, railways, aircraft, wind turbines and leisure noise) and recommends source-specific exposure guidance. This supports the source-diversity part; the local EU still does not point to a specific section. The exact wording about variation by place/time/activity is broader than the source title alone and should be tied to the appropriate exposure/recommendation passages before full scoring.

## Cross-cutting result
All five checked records have structurally coherent Claim → Evidence Use → Source pointers. Three acid-base Claims have direct topic-level source support in OpenStax, and the pH activity statement also has an explicit IUPAC definition. Both acoustics Claims have relevant WHO source identity and topic-level support, but claim-specific pinpointing is incomplete. These observations are traceability/source-fit triage, not final D/E/B scores, and do not establish that the full Claims or all linked sources are fully verified.

## Next actions
1. Continue the row-level reconciliation of every prior scored report against the frozen 1,494-file Claim inventory, including duplicate/alias and internal-ID checks.
2. Continue Batch 41 candidate linkage/source checks without marking candidates scored until the prior-score exclusion gate is complete.
3. Correct generic Evidence Use descriptions only in a separately authorized correction scope, with regressions.
4. Keep PR #21 draft/open/unmerged and leave `main` unchanged.

## Public source passages checked
- OpenStax Chemistry 2e, Chapter 14 summary: https://openstax.org/books/chemistry-2e/pages/14-summary
- IUPAC Gold Book, pH (P04524): https://goldbook.iupac.org/terms/view/P04524
- WHO Europe, Environmental Noise Guidelines for the European Region: https://www.who.int/europe/publications/i/item/9789289053563
