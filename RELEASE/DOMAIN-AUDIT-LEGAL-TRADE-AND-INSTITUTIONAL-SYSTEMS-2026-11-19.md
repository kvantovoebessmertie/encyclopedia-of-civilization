# Domain Audit — Legal, Trade and Institutional Systems (Part II / Gap Map R7) — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR workstream: #22, Work Package 1 — first-edition candidate selection  
Scope: ten non-duplicate Gap Map R7 slices  
Disposition: **0 INCLUDE / 10 HOLD / 0 EXCLUDE**

## Scope and duplicate control

The Part II work order calls for the remaining legal, trade and institutional domains after screening the society/public-institutions core. This package follows the ten-slice Gap Map R7 registry:

1. `political-economy-basics`
2. `comparative-law-basics`
3. `administrative-law-basics`
4. `international-law-basics`
5. `civil-society-basics`
6. `social-policy-basics`
7. `taxation-basics`
8. `labor-economics-basics`
9. `migration-and-mobility-basics`
10. `comparative-civilizations-basics`

Duplicate control:
- `law-basics` and `migration-basics` were screened in the preceding Society and Public Institutions package; they are distinct from the comparative-law/administrative-law/international-law and migration-and-mobility slices screened here.
- The earlier economic-systems package covered accounting, macroeconomics, microeconomics, money and banking, and organizational behaviour. None of those five slices is repeated here.
- The earlier engineering/computing, human-sciences and Part I audits are not repeated.

Each slice was screened at its current canonical 9-record structure: one Source, three Claims, three Evidence Use records, one Context and one Scope. Total: **90 records** (10 Sources, 30 Claims, 30 Evidence Use, 10 Context, 10 Scope).

This is a record-level candidate screen, not legal advice, rights clearance, full subject-matter peer review or release approval. No canonical JSON, publication state, allowlist or decision was changed.

## Inventory and decisions

| Slice | Records | Source | Claims | Evidence Use | Context | Scope | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| political-economy-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| comparative-law-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| administrative-law-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| international-law-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| civil-society-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| social-policy-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| taxation-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| labor-economics-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| migration-and-mobility-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| comparative-civilizations-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| **Total** | **90** | **10** | **30** | **30** | **10** | **10** | **0 INCLUDE / 10 HOLD / 0 EXCLUDE** |

All inspected records currently carry `record_version=1`, `publication_status=published` and `completion_status=complete`. Those stored states are not first-edition approval.

## Slice findings

### 1. political-economy-basics — HOLD

- Claims A–C are substantive and generally fit Jeffry Frieden's IMF Finance & Development article, “The Political Economy of Economic Policy” (June 2020).
- The article explicitly describes the two-way relationship between politics and the economy, the role of voters, interest groups and institutions, and how economic conditions can influence political behaviour and policy choices.
- Claim B is closely supported by the article's discussion of concentrated/diffuse interests and institutional channels. Claim C is supported at a high level, but it must remain contextual and non-deterministic.
- The Source identity is only “Political economy — public reference” despite linking to a specific named article. Evidence Use B/C include some useful boundaries but no exact paragraph/section/page locators; EU A is generic.
- Context and Scope are useful and correctly reject universal prediction or political recommendation.

Required work: normalize the Source identity to the full author/title/publication/date; add exact article/paragraph pinpoints for A–C; preserve the non-deterministic institutional and historical boundary.

### 2. comparative-law-basics — HOLD

- Claims A–C are substantive and substantially aligned with Cornell LII's Wex “Legal systems” entry: legal systems include rules, procedures and institutions; jurisdictions differ; legal-system differences affect sources of law, judicial roles, evidence standards and authority.
- The Source identity is generic rather than the named Wex entry. The page is a U.S.-authored educational summary and its examples should not be treated as a comprehensive comparative-law taxonomy.
- Evidence Use A is generic; B/C give useful summaries but no exact section or page locators.
- Context and Scope appropriately require jurisdiction, period and branch of law.

Required work: identify the exact Wex entry and its subheadings as locators; add a comparative-law scholarly or institutional source if the Claims intend to cover more than the illustrative legal-system categories on that page. Retain explicit limits and avoid treating civil/common/religious/customary categories as exhaustive or mutually exclusive.

### 3. administrative-law-basics — HOLD

- Claims A–C are substantive and directly align with Cornell LII Wex “Administrative law”: agency creation and operation; delegated powers and constitutional/statutory limits; rulemaking, enforcement and adjudication.
- The current Source identity is generic and does not name Cornell LII/Wex. The article is U.S.-specific (federal and state agencies, Congress, state legislatures and the U.S. Administrative Procedure Act); it cannot establish a universal administrative-law model.
- Evidence Use A is generic; B/C contain useful boundaries but no precise locators.
- Context and Scope correctly require jurisdiction-specific law and exclude individual-case advice.

Required work: pin Wex sections “Structure of Agencies” and “Statutory Regulation of Agencies”; make the U.S. federal/state example boundary explicit in the Source and reader-facing presentation. Add non-U.S. comparative sources only if the Claims are generalized beyond the U.S. example.

### 4. international-law-basics — HOLD

- Claims B/C are directly supported by the UN Charter: Article 2(1) establishes sovereign equality of Members; Article 2(3) requires peaceful settlement of international disputes. The UN describes the Charter as an international treaty and a founding instrument of the Organization.
- Claim A is broader than the Charter. The definition and scope of international law, including actors beyond States and international organizations, require separate doctrinal sources and careful terminology about international legal personality.
- Evidence Use B/C describe the right ideas but omit the precise Charter Articles; EU A is generic.
- Context/Scope appropriately state that the Charter is one foundational source, not the whole of international law.

Required work: pin the UN Charter Articles 1–2 and the Charter's status as treaty; add a reliable international-law source for Claim A and for any statement about recognized legal subjects. Do not imply that all individuals or entities have the same international legal personality.

### 5. civil-society-basics — HOLD

- Claims A–C are substantive: voluntary associational space, possible organizational forms, and participation in public discussion/interest representation/service delivery.
- The Source is a large World Bank PDF, but its canonical identity is only “Civil society — public reference”; the exact report title, authorship, date and relevant pages are not recorded. The PDF could not be fully inspected through the available text extraction due to its size.
- Evidence Use A is generic; B/C give some support boundaries but no page/section locators.
- Context and Scope correctly warn that legal status and powers depend on jurisdiction.

Required work: identify the exact World Bank report and pin the relevant definition, organizational forms and participation/service-delivery sections. Confirm whether the report is a World Bank publication or a third-party work hosted by the Bank, and screen its exact rights notice.

### 6. social-policy-basics — HOLD

- Claims A–C are substantive and align with the OECD Social Policy topic page. The OECD describes social policy as protecting individuals/families and identifies social spending on poverty, unemployment, older people, health, family assistance and housing.
- The Source identity “Social policy — public reference” is generic even though the URI is an OECD topic page. The OECD Social Spending indicator offers a more precise definition of cash benefits, in-kind goods/services and tax breaks with a social purpose.
- Evidence Use A is generic; B/C are descriptive but have no exact page or indicator locator.
- Context and Scope correctly distinguish social-policy description from an individual entitlement or causal proof of programme effectiveness.

Required work: normalize the Source identity and pin the OECD Social Policy topic page and Social Spending indicator definition; keep cash benefits, in-kind services and tax expenditure distinct. Avoid implying that an OECD comparative category creates an entitlement under national law.

### 7. taxation-basics — HOLD

- Claims A–C are substantive and align with the OECD Tax Policy topic page: raising revenue, financing public programmes, and possible effects on work, investment and innovation.
- The Source identity is generic; the linked OECD page is a useful direct source candidate and includes clear text for the three propositions.
- Evidence Use B/C contain reasonable boundaries, but none of the three records identifies exact sections or source page headings. Claim C is broad and should not be read as a universal causal law.
- Context and Scope correctly require jurisdiction and time-specific rules and exclude individual tax advice.

Required work: pin the OECD sections “Tax policy seeks to strike a balance”, “Taxes seek to raise revenue” and “Tax policy shapes incentives”; preserve conditional language and add a specific jurisdictional source only if the page is to discuss actual tax obligations.

### 8. labor-economics-basics — HOLD

- Claims A–C are substantive, but the current Source is the ILO Wages topic portal. That portal directly discusses wages, wage policy, wage bargaining and gender pay gaps, but it does not provide a full labour-economics framework or all the listed labour-market indicators.
- Claim A (scope of labour economics) requires a broader ILO/ILOSTAT or labour-economics source.
- Claim B is conceptually sound but needs a precise source defining wages as worker remuneration and employer labour cost.
- Claim C includes employment, earnings, working time, productivity and labour underutilization; the wages portal alone does not establish this full indicator set.
- Evidence Use A is generic; B/C are summaries without exact locator or indicator definitions.
- Context appropriately stresses comparability and indicator definitions.

Required work: add a broader ILOSTAT/labour-statistics source and exact definitions for employment, unemployment/underutilization, wages, hours and productivity. Preserve statistical reference periods and population definitions.

### 9. migration-and-mobility-basics — HOLD

- Claims A–C are substantive and appropriately limited to usual residence, internal/international migration and the need to specify definitions, periods, territories and measurement of flows/stocks.
- The Source is an IOM educator toolkit resource, but the canonical Source identity is generic and the source page was not accessible in the external review. The exact toolkit definition and edition must be verified.
- Evidence Use A is generic; B/C have useful scope boundaries but no precise lesson/page locators.
- Context/Scope correctly avoid determining individual immigration, asylum, residence or work rights.

Required work: pin the exact IOM toolkit module and definition; add UN migration-statistics standards for internal/international migration and stock/flow measurement. Keep migration as a statistical concept distinct from refugee/asylum legal status.

### 10. comparative-civilizations-basics — HOLD

- Claims A–C are methodological and substantive, but the selected UNESCO source is the “History of Civilizations of Central Asia” multimedia/archive collection, not a general comparative-civilization methodology source.
- UNESCO describes this as a six-volume history focused on Central Asian cultures and notes that the full material cannot be posted online and is available for consultation in a reading room or by video on demand. The page identifies UNESCO as rights holder.
- The source cannot establish the broad proposition that comparative study should reject a single universal trajectory, nor does it directly support the method distinction between chronology and causality.
- All three Evidence Use records are generic. Context and Scope are also generic and do not identify a comparative method or geographic/time boundary.
- Context and Scope provenance metadata point to the Source rather than only Claim A; confirm role conventions against the record schema before any authorized change.

Required work: replace or supplement the Source with a genuinely methodological comparative-history/civilization text that is openly accessible for the intended factual use; pin exact methodological passages. Treat the current UNESCO archive as a region-specific case-study resource, not a general methodological authority. Resolve rights and access restrictions before any use of the full work.

## Cross-slice findings

1. **Record shape:** all ten slices contain the expected nine record roles.
2. **Evidence Use:** all 30 records lack precise page/section/article locators. Some descriptions contain useful scope limitations, but none consistently establishes the exact passage supporting each Claim.
3. **Source identity:** seven sources use generic identities despite specific URLs. The civil-society PDF is not bibliographically identified; comparative civilizations points to a region-specific UNESCO archive; labour economics relies on a wage-only topic portal.
4. **Claim substance:** most Claims are substantive. The principal problem is not generic editorial text but source fit, locator precision, broad generalization and legal/statistical scope.
5. **Legal boundaries:** Cornell Wex sources are U.S.-law educational summaries; they must not be presented as universal law. UN Charter propositions must be pinned to exact Articles and not generalized to all international law.
6. **Measurement boundaries:** labour and migration Claims require operational definitions, reference populations, periods, and consistent flow/stock or indicator methodologies.
7. **Rights and editorial:** no rights clearance is asserted. The UNESCO archive is not available for full online posting; World Bank PDF rights ownership/terms need verification; other sources require item-level licence/permission screening.
8. **Selection:** all ten slices remain HOLD. Existing `publication_status=published` values do not constitute first-edition approval.

## Group result

**90/90 records screened; 0 INCLUDE / 10 HOLD / 0 EXCLUDE.**

No canonical JSON was modified. No Source, Claim, Evidence Use, Context or Scope version was changed. No first-edition allowlist, publication state, completion state or release decision was changed. No main-branch change, merge, deployment or release action was performed.

## Next work under the first-edition plan

1. Reconcile this package with the exact-version candidate register; preserve historical decisions.
2. Prepare bounded remediation authorization only after exact source identity, claim-specific locators and rights limits are documented.
3. Prioritize: exact source and pinpoints for political economy; U.S. limits and exact locators for comparative/administrative law; separate international-law sources for Claim A; bibliographic identification of the civil-society report; broader labour-statistics evidence; and replacement of the comparative-civilizations source.
4. Complete source-specific rights/attribution screens and the project-level licence/distribution decision before release.
5. Continue with the next Part II family only after duplicate control against earlier candidate reviews. Do not repeat closed audits or M13 batches.

## Source references consulted

- IMF, Jeffry Frieden, “The Political Economy of Economic Policy,” *Finance & Development* (June 2020): https://www.imf.org/en/publications/fandd/issues/2020/06/political-economy-of-economic-policy-jeffrieden
- Cornell LII, Wex, “Legal systems”: https://www.law.cornell.edu/wex/Legal_systems
- Cornell LII, Wex, “Administrative law”: https://www.law.cornell.edu/wex/administrative_law
- United Nations Charter, full text, Chapter I / Articles 1–2: https://www.un.org/en/about-us/un-charter/full-text
- World Bank-hosted civil society source (exact bibliographic identity and rights still to be confirmed): https://documents1.worldbank.org/curated/en/115751468316166282/pdf/514320WP0WB1CS10Box342028B01PUBLIC1.pdf
- OECD, “Social policy”: https://www.oecd.org/en/topics/policy-issues/social-policy.html
- OECD, “Social spending” indicator definition: https://www.oecd.org/en/data/indicators/social-spending.html
- OECD, “Tax policy”: https://www.oecd.org/en/topics/tax-policy.html
- ILO, “Wages” topic portal: https://www.ilo.org/topics-and-sectors/wages
- IOM, World Migration Report Educators' Toolkit, Module 1: https://www.wmr-educatorstoolkit.iom.int/module-1-what-is-migration-resources
- UNESCO, “History of Civilizations of Central Asia” archive: https://www.unesco.org/archives/multimedia/document-1595
