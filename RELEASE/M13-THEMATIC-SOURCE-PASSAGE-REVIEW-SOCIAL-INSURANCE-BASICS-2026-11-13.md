# M13 thematic source-passage review — social-insurance-basics
Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: source-passage desk review of Claims A–C, their existing Evidence Uses, and the current ILO Source. Noncanonical audit material only.

## Result
- Claims reviewed: 3/3.
- Claim A: direct conceptual support.
- Claim B: direct support from ILO Convention No. 102 guidance and comparative OECD/ILO material.
- Claim C: direct support as a general rule, with a clear distinction between system rules and individual eligibility.
- Final D/E/B scores assigned: 0.
- Canonical records changed: 0.
- All three Claims remain **HOLD** pending exact Evidence Use pinpoints, Source metadata remediation under bounded authorization, and separate independent/editorial review.

## Records examined
- Claims: `CLM-SOCIAL_INSURANCE_BASICS-A/B/C@1`.
- Evidence Uses: `EU-SOCIAL_INSURANCE_BASICS-A/B/C@1`.
- Source: `SRC-SOCIAL_INSURANCE_BASICS@1`, identity “ILO — Social protection”, URI `https://www.ilo.org/topics/social-protection`.
- Context and scope: `CTX-SOCIAL_INSURANCE_BASICS@1`, `SCP-SOCIAL_INSURANCE_BASICS@1`.

## Passage-level findings

### Claim A
Claim: “Социальное страхование является одним из механизмов социальной защиты от определённых социальных рисков.”

**Direct support**
- ILO, *Social protection*, opening definition paragraph: social protection/social security schemes can be financed through wage contributions (social insurance) or general taxation (social assistance); benefits address risks across the life cycle.
- ILO, *Frequently asked questions — Social Security (Minimum Standards) Convention, 1952 (No. 102)*, section “What is the difference between contributory schemes and non-contributory schemes?”: social insurance schemes are identified as the most common form of contributory social security schemes.
- ILO, *World Social Protection Report 2024–26*, Chapter 1, Box 1.2: social protection systems operate through social insurance, universal/categorical schemes and social assistance.

**Assessment**
The Claim is directly supported and correctly describes social insurance as one mechanism within broader social protection. It does not overstate social insurance as the only mechanism.

**Required Evidence Use repair**
Use ILO FAQ, “What is the difference between contributory schemes and non-contributory schemes?” (paragraph beginning “Contributory schemes are those…”), plus the ILO *Social protection* opening definition paragraph. The current generic EU description does not identify either passage.

**Disposition: HOLD.** Direct support; pinpoint defect remains.

### Claim B
Claim: “Условия охвата, финансирования и получения социальных страховых выплат различаются между системами.”

**Direct support**
- ILO Convention No. 102 FAQ, introductory section: the Convention sets minimum benchmarks for coverage, adequacy, entitlement conditions and duration, while national law has flexibility to determine many details.
- Same FAQ, “What is the difference between contributory schemes and non-contributory schemes?”: entitlement and benefit amounts in contributory schemes can depend on contribution history and previous earnings; qualifying periods may be required.
- OECD, *Financing of Social Protection*, “A stocktaking of current financing mixes in social protection systems” / section 1.4.1 “Funding mixes vary widely across countries”: financing strategies and funding mixes differ significantly across countries.
- OECD, *Financing of Social Protection*, section 3.4.1: the link between benefits and contributions varies across countries and programmes; even insurance benefits may have incomplete contribution-entitlement links.
- ILO, *World Social Protection Report 2024–26*, Chapter 3: effective coverage through contributory and non-contributory mechanisms varies by region and country-income level.

**Assessment**
The general claim is directly supported. Its three dimensions are all evidenced: coverage by Convention No. 102 and ILO coverage data; financing by ILO/OECD; benefit qualification by Convention No. 102 FAQ and OECD analysis. Avoid implying that every social insurance scheme has a simple one-to-one link between paid contributions and entitlement: the OECD explicitly documents exceptions and mixed arrangements.

**Required Evidence Use repair**
- ILO FAQ: introductory description of Convention No. 102 and its coverage/entitlement/duration benchmarks.
- ILO FAQ: “Contributory schemes” paragraphs on entitlement, contribution history and earnings.
- OECD financing report: section 1.4.1 and section 3.4.1 for cross-country variation and incomplete contribution-benefit links.
These are pinpointable passages; the existing EU record only repeats the generic Source name.

**Disposition: HOLD.** Direct support, but the Claim's Evidence Use is currently non-reproducible.

### Claim C
Claim: “Оценка конкретного права на социальное страхование требует учитывать правила соответствующей системы и индивидуальные обстоятельства.”

**Direct support**
- ILO Convention No. 102 FAQ: national law defines specific eligibility matters; for example, national law should define the degree of permanent disability that gives entitlement to a disability pension.
- Same FAQ: contributory schemes commonly require a qualifying number of contributions; benefit amount may depend on contribution history and previous income.
- Same FAQ: national systems can use different mechanisms (employee schemes, economically active population schemes, or means-tested resident schemes), and national circumstances differ.
- ILO, *Social Security Convention No. 102*, summary: the Convention sets minimum objectives but leaves flexibility to Member States; coverage, benefit levels and entitlement conditions are governed through national arrangements.

**Assessment**
The Claim is a sound general caution and is directly supported. “Индивидуальные обстоятельства” is not an exhaustive legal test; it appropriately signals that general educational material cannot determine an individual entitlement. The scope statement that this is not a professional or jurisdiction-specific consultation is appropriate.

**Required Evidence Use repair**
Pinpoint the ILO FAQ sections on national legal flexibility, contribution qualifying periods, and the example of disability-pension eligibility. Add the Convention No. 102 summary only as an overview, not as a substitute for the applicable national legislation.

**Disposition: HOLD.** Direct support for the general rule; no individual entitlement can be adjudicated from this educational slice.

## Source identity and quality findings
1. The current Source identity “ILO — Social protection” is generic. The current URI `https://www.ilo.org/topics/social-protection` is not the canonical URL surfaced for the ILO topic page in the current review. The current ILO topic page is `https://www.ilo.org/topics-and-sectors/social-protection`. Do not silently replace the URI; version the Source only under explicit authorization and verify redirect/canonical behavior.
2. The single ILO topic page is a high-level overview, not enough to support the detailed claims B and C. The ILO Convention No. 102 FAQ is the strongest direct source for eligibility, contribution periods, coverage and national flexibility.
3. The OECD *Financing of Social Protection* report supplies a distinct institutional perspective on cross-country financing variation and the imperfect relationship between contributions and benefits.
4. Three generic Evidence Uses currently all point to one ILO Source and provide no section/paragraph locators. That is an evidence-reproducibility defect, not a reason to mark the underlying Claims false.

## Recommended bounded remediation
- Under explicit editorial authorization, create a versioned ILO Source for the Convention No. 102 FAQ and version each affected EU with exact section/paragraph locators.
- Consider a separate OECD Source for *Financing of Social Protection* only if source-record policy permits it and rights/availability metadata are captured.
- Correct the existing ILO topic Source URL/identity only through a bounded, versioned correction; preserve provenance.
- Do not change Claim wording on the basis of this review.
- Run schema/reference regression tests and exact-head CI after authorized corrections.
- Keep all Claims HOLD until independent human review and editorial/publication approval are separately documented.

## Source register
- ILO, *Social protection*: https://www.ilo.org/topics-and-sectors/social-protection
- ILO, *Frequently asked questions — Social Security (Minimum Standards) Convention, 1952 (No. 102)*: https://www.ilo.org/frequently-asked-questions-social-security-minimum-standards-convention
- ILO, *Social Security Convention No. 102*: https://www.ilo.org/resource/ilo-social-security-convention-no102
- ILO, *World Social Protection Report 2024–26*, Chapter 3: https://webapps.ilo.org/static/english/reports/flagship/world_social_protection_report_2024-26/Chapter%2003.html
- OECD, *Financing of Social Protection*, financing mixes: https://www.oecd.org/en/publications/financing-of-social-protection_b384fd31-en/full-report/a-stocktaking-of-current-financing-mixes-in-social-protection-systems_edd23fad.html
- OECD, *Financing of Social Protection*, link between benefits and contributions: https://www.oecd.org/en/publications/financing-of-social-protection_b384fd31-en/full-report/securing-the-revenue-base-for-social-protection_fee691c9.html

---
This is a source-passage desk review only. It is not final D/E/B scoring, legal advice, independent human review, or publication authorization.
