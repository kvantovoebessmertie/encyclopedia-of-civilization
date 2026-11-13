# M13 thematic source-passage review — public-health-basics
Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: source-passage desk review of Claims A–D, their linked Evidence Uses, and the current WHO/CDC Sources. Noncanonical audit material only.

## Result
- Claims reviewed: 4/4.
- A: direct support from the WHO European Observatory definition and activity list.
- B: direct support from the WHO list of essential public-health functions.
- C: direct support from the population/community scope of WHO public-health functions; wording is appropriately population-level.
- D: CDC's Introduction to Public Health course explicitly covers core functions, essential services and determinants; WHO's current functions list provides a stronger substantive cross-check.
- Final D/E/B scores assigned: 0.
- Canonical records changed: 0.
- All four Claims remain **HOLD** because the current Evidence Uses A–C are generic and non-reproducible, and D lacks a pinpoint to the CDC page's exact course-description passage. This is a source-passage desk review, not independent reviewer scoring.

## Records examined
- Claims: `CLM-PUBLIC_HEALTH_BASICS-A/B/C/D@1`.
- Evidence Uses: `EU-PUBLIC_HEALTH_BASICS-A/B/C@1`, `EU-PUBLIC_HEALTH_BASICS-D-CDC@1`.
- Sources:
  - `SRC-PUBLIC_HEALTH_BASICS@1`: WHO European Observatory on Health Systems and Policies, “Public health”, https://eurohealthobservatory.who.int/themes/health-system-functions/public-health
  - `SRC-CDC-PUBLIC_HEALTH-2026@1`: CDC, “Introduction to Public Health”, https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health.html
- Context/scope: `CTX-PUBLIC_HEALTH_BASICS@1`, `SCP-PUBLIC_HEALTH_BASICS@1`.

## Passage-level findings

### Claim A
Claim: “Общественное здравоохранение направлено на улучшение здоровья популяций и профилактику заболеваний.”

**Direct support**
- WHO European Observatory, “Public health”, opening paragraph: “Public health aims to improve the health of populations” and prevent disease.
- Same page, immediately following paragraph: repeats the population-health objective and enumerates surveillance, response to health hazards/emergencies, health protection, health promotion and disease prevention.

**Assessment**
Direct, near-verbatim conceptual support. The Claim is appropriately general and does not imply that public health is limited to clinical care.

**Required Evidence Use repair**
Replace the generic description in `EU-PUBLIC_HEALTH_BASICS-A@1` with a pinpoint to the WHO European Observatory page, opening paragraph and the following paragraph listing typical activities (page paragraphs 1–2; rendered lines 66–68 in the 2026-11-13 review).

**Disposition: HOLD.** Strong direct support; EU locator defect remains.

### Claim B
Claim: “К общественному здравоохранению относятся наблюдение за здоровьем населения, профилактика, защита здоровья и реагирование на угрозы.”

**Direct support**
- WHO, “Essential public health functions”, section “The unified list of essential public health functions”, items:
  - public health surveillance and monitoring;
  - public health emergency management;
  - health protection;
  - disease prevention and early detection;
  - health promotion.
- WHO European Observatory, “Public health”, paragraph 2: surveillance of population health, response to hazards and emergencies, health protection and disease prevention.
- CDC, “Introduction to Public Health”, “At a glance” and “Learning Objectives”: the course covers core public-health functions and essential services.

**Assessment**
All four elements of the Claim are explicitly represented in WHO's unified list. The wording is a reasonable high-level summary, not an exhaustive list of public-health functions. Note that the WHO unified list contains 12 functions, including stewardship, multisectoral planning, workforce development, research and access to health products; the Claim should not be read as a complete taxonomy.

**Required Evidence Use repair**
For `EU-PUBLIC_HEALTH_BASICS-B@1`, cite WHO “Essential public health functions”, the section “The unified list of essential public health functions”, especially items 1, 2, 5 and 6 (surveillance, emergency management, health protection, disease prevention/early detection). Add the WHO Observatory paragraph 2 as a concise corroborating passage. Current EU description identifies no passages.

**Disposition: HOLD.** Direct support; exact locator absent.

### Claim C
Claim: “Популяционные меры общественного здравоохранения применяются на уровне групп и сообществ, а не только отдельных людей.”

**Direct support**
- WHO European Observatory, “Public health”, opening paragraph: objective is improvement of the health of populations.
- WHO, “Essential public health functions”, item “Community engagement and social participation”: strengthening community engagement, participation and social mobilization for health and well-being.
- WHO, same section, surveillance and monitoring item: population health status, risk and protective factors, threats to health, health-system performance and service use are monitored at population level.
- CDC, “Introduction to Public Health”, learning objective: recognize how individual determinants of health affect population health.

**Assessment**
The Claim is directly supported as a population-level description. The distinction is not absolute: public-health functions can include interventions or services delivered to individuals, but they are organized and evaluated in relation to population health. The phrase “а не только отдельных людей” correctly avoids saying public health never works with individuals.

**Required Evidence Use repair**
For `EU-PUBLIC_HEALTH_BASICS-C@1`, pinpoint WHO Observatory opening paragraph and WHO EPHF list items “Public health surveillance and monitoring” and “Community engagement and social participation”. The current generic EU description is not reproducible.

**Disposition: HOLD.** Direct support with a necessary scope nuance; locator absent.

### Claim D
Claim: “CDC describes public health as including core functions, essential services and attention to determinants that affect population health.”

**Direct support**
- CDC, “Introduction to Public Health”, “At a glance” paragraph: the course overview explicitly includes core public-health functions and essential services, and determinants of health.
- Same CDC page, “Learning Objectives”, bullets 4, 6 and 7: recognizing core functions and essential services; listing determinants of health; recognizing how individual determinants affect population health.
- CDC page metadata identifies the page as updated January 10, 2025; its “Content Source” is the Public Health Infrastructure Center.
- As a substantive cross-check, WHO's current unified EPHF list covers surveillance, emergency management, protection, prevention, promotion and wider determinants/community participation.

**Assessment**
The Claim is directly supported as a description of what the CDC course covers. It does not claim the CDC page itself provides a full technical definition. The source is correctly identified and its URL is a specific official CDC page.

**Required Evidence Use repair**
For `EU-PUBLIC_HEALTH_BASICS-D-CDC@1`, specify CDC “Introduction to Public Health”, “At a glance” paragraph and “Learning Objectives” bullets 4, 6 and 7. The existing EU has a better scope description than A–C, but still lacks a precise locator.

**Disposition: HOLD.** Direct support; exact locator still required.

## Source identity and quality findings
1. WHO Source @1 has a specific, working institutional identity and a canonical topic URL. It is a thematic page, but the reviewed paragraphs directly support the basic definition and activity list.
2. WHO's “Essential public health functions” page is a separate, more detailed source and should be added as a distinct Source record only under an explicit bounded authorization. Do not silently redirect the existing WHO Source or treat the EPHF page as already linked in the canonical record.
3. CDC Source @1 has a specific title and official URL. The CDC page is a course overview, not a standalone technical definition; the Claim D wording correctly attributes what the CDC course covers rather than asserting that the page is a complete definition.
4. Evidence Uses A–C all repeat the same generic description and do not identify passages. EU D is semantically better but also lacks pinpoint locators. This is an evidence-reproducibility defect, not evidence that the Claims are false.
5. No evidence here establishes individual clinical advice, diagnosis, or a specific national public-health mandate. The existing Context and Scope boundaries remain appropriate.

## Recommended bounded remediation
- Under explicit editorial authorization, version Evidence Uses A–D with the exact passage locators above.
- If the project wishes to cite the WHO unified 12-function framework directly, create a separate versioned Source for the WHO “Essential public health functions” page and link it only through authorized Evidence Use changes.
- Preserve the existing WHO and CDC source provenance; do not silently change their URLs or identities.
- Do not change Claim wording on the basis of this desk review.
- Run schema/reference regression tests and exact-head CI after any authorized correction.
- Keep all Claims HOLD until independent human review and editorial/publication approval are separately documented.

## Source register
- WHO European Observatory on Health Systems and Policies, “Public health”: https://eurohealthobservatory.who.int/themes/health-system-functions/public-health
- WHO, “Essential public health functions”: https://www.who.int/teams/primary-health-care/health-systems-resilience/essential-public-health-functions
- CDC, “Introduction to Public Health”, Public Health 101 Series: https://www.cdc.gov/training-publichealth101/php/training/introduction-to-public-health.html
- CDC, “10 Essential Public Health Services”: https://www.cdc.gov/public-health-gateway/php/about/

---
This is a source-passage desk review only. It is not final D/E/B scoring, medical advice, independent human review, or publication authorization.
