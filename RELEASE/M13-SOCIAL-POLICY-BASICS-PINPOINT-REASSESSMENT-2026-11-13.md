# M13 social-policy-basics — pinpoint reassessment
Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: noncanonical supplemental desk review. This supplements, and does not replace, `M13-THEMATIC-SOURCE-PASSAGE-REVIEW-SOCIAL-POLICY-BASICS-2026-11-13.md`.

## Why this reassessment was needed
The first report correctly found that the existing Evidence Uses lacked reproducible passage locators, but it did not fully separate the direct OECD passages from the ILO's more precise social-protection definitions. This reassessment identifies exact section/paragraph targets and narrows what each source can support.

## Exact passage map

| Claim | Strongest exact passage | What it directly supports | What it does not establish alone |
|---|---|---|---|
| A | OECD, *Social policy*, opening paragraph | Social policy protects individuals and families and supports a fulfilling life | A complete taxonomy of every social-policy instrument |
| A | ILO, *Social protection*, opening definition paragraph | Benefits linked to life-cycle risks and poverty/social exclusion | The full disciplinary scope of social policy |
| B | OECD, *Social policy*, “Key messages” | Financial assistance and services in poverty, unemployment, healthcare, family and housing areas | A universal statistical classification applicable to every country |
| B | OECD, *Social spending*, “Definition” | Cash benefits, in-kind goods/services and tax breaks; qualifying programme criteria | That every social programme is included in every national accounting series |
| C | OECD, *Social policy*, “Context” → “Public social spending” | Cross-country differences in welfare-state size and public social-spending levels; historical change | Detailed comparison of individual eligibility or access rules |
| C | ILO, *Social protection*, opening paragraphs | Contribution-financed social insurance versus tax-financed social assistance; coverage gaps | A country-by-country eligibility comparison |
| C | ILO, *World Social Protection Report 2024–26*, Chapter 1, Box 1.2 | Life-course access, adequacy and sustainability concepts; system mechanisms | Specific national entitlement conditions without country-specific law/programme sources |

## Claim dispositions

### A — core wording directly supported; retain HOLD
OECD opening summary is the primary source for the social-policy framing. ILO's definition is a corroborating source for the social-protection and life-cycle-risk portion. The current ILO Source record points to a project page narrowly concerned with forcibly displaced people; that is not the best general-purpose source for this Claim. A versioned source identity/URI correction is recommended, subject to explicit authorization.

### B — direct support; retain HOLD
OECD “Key messages” lists the exact policy areas in the Claim. OECD's dedicated “Social spending” definition provides a more rigorous operational definition. The Claim's “могут включать” correctly signals examples rather than an exhaustive list. The Evidence Use should distinguish the narrative policy-area page from the statistical indicator definition.

### C — direct support for variation, not for every listed dimension equally; retain HOLD
OECD's country and time comparisons directly support variation in system scale and spending. ILO's definition supports different financing mechanisms and notes coverage gaps. The claim's mention of accessibility and eligibility conditions remains a programme-level caveat rather than a comparative finding demonstrated by these topic pages. Do not score those dimensions as directly evidenced until a targeted comparative source or national programme sources are added.

## Existing metadata defects
- `SRC-SOCIAL_POLICY_BASICS@1` has generic identity “Social policy — public reference”; exact identity should be “Social policy” (OECD).
- `SRC-SOCIAL_POLICY_BASICS-INDEPENDENT@1` identifies “ILO — Social protection” but points to a project page on forcibly displaced persons. For general social-protection framing, the ILO topic page is the better match; the World Social Protection Report 2024–26 is a stronger pinpointable report source.
- All six Evidence Uses use descriptions instead of exact passage locators. Three “INDEPENDENT” EU records do not constitute independent human review. The ILO is a distinct institution from OECD, but three EUs linked to one ILO Source remain one institutional source family.
- No canonical records were changed and no formal D/E/B scores were assigned.

## Bounded next steps
1. Obtain explicit editorial authorization before changing either Source identity/URI or any existing EU.
2. Version the OECD EU-A and EU-B with “opening paragraph” and “Key messages” pinpoints respectively.
3. Version OECD EU-C with “Context — Public social spending”; add ILO evidence for financing/coverage and keep the eligibility wording explicitly qualified.
4. If a distinct ILO report Source is added, use *World Social Protection Report 2024–26*, Chapter 1, Box 1.2 and record its publication/rights metadata.
5. Run reference/schema tests and exact-head CI after any authorized canonical correction.
6. Keep all Claims HOLD until separate independent human review and editorial/publication approval.

## Public source locators
- OECD, *Social policy*: https://www.oecd.org/en/topics/policy-issues/social-policy.html
- OECD, *Social spending* — Definition: https://www.oecd.org/en/data/indicators/social-spending.html
- ILO, *Social protection*: https://www.ilo.org/topics-and-sectors/social-protection
- ILO, *World Social Protection Report 2024–26*, Chapter 1, Box 1.2: https://webapps.ilo.org/static/english/reports/flagship/world_social_protection_report_2024-26/Chapter%2001.html

This is source-passage desk review only, not finalized D/E/B scoring, legal advice, independent review, or publication approval.
