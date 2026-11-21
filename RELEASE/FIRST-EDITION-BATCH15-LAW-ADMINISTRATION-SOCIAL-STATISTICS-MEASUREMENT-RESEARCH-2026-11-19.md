# First Edition — Batch 15 Law, Public Administration, Social Statistics and Measurement Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `b788772bf0a073896e7c57c1927341327d9f6ad0`  
Status: **15 CANDIDATE CLAIMS / 15 EUS RESEARCHED ACROSS FIVE SLICES; DIRECT LOCATOR CANDIDATES FOUND; SOCIOLOGY HAS THREE EDITORIAL PLACEHOLDERS; SOURCE-GRAPH EXPANSION IDENTIFIED; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Batch 15 selects 15 candidate Claims from five slices present in the exact-version master and not covered by Batches 1–14 or active bounded authorizations:

- law-basics — Claims A–C;
- public-administration-basics — Claims A–C;
- social-statistics-basics — Claims A–C;
- sociology-basics — Claims A–C;
- units-and-measurement — Claims A–C.

All 15 Claims, 15 EUs and five current Sources were re-fetched from the PR branch and confirmed present in the exact-version master. All 15 EUs currently use generic descriptions and lack claim-specific `material.locator` values.

Sociology A–C are editorial scaffolding, not substantive subject Claims. They require substantive replacement proposals. The other four slices have substantive propositions, with source-fit or graph-precision work required.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All five slices remain HOLD.

## 2. Aggregate findings

| Slice | Claims / EUs | Main result |
|---|---:|---|
| law-basics | 3 / 3 | Cornell LII Wex directly supports jurisdiction definition and types; preserve explicit U.S.-law boundary |
| public-administration-basics | 3 / 3 | UN report A/HRC/25/27 provides direct definition and legal/administrative framework passages; current OECD portal Source is too broad |
| social-statistics-basics | 3 / 3 | UN Demographic/Social Statistics supports scope; UN FPOS Principle 9 supports comparability; Statistics Canada and UN FPOS Principle 4 support non-causal interpretation boundary |
| sociology-basics | 3 / 3 | Three current Claims are placeholders; ASA supplies direct substantive propositions and methods |
| units-and-measurement | 3 / 3 | BIPM VIM §§2.1/2.26 and SI Brochure §1.1 provide direct measurement/unit/uncertainty definitions; current NIST Source directly supports SI only |

**Total:** 15 Claims / 15 EUs / five current Sources. Additional Source/EU records are proposed for social statistics, measurement and public administration; no canonical IDs are assigned here.

## 3. Law Basics — Claims A–C

Current records:
- `CLM-LAW_BASICS-A/B/C@1`
- `EU-LAW_BASICS-A/B/C@1`
- `SRC-LAW_BASICS@1`

Current Source: Cornell Legal Information Institute, Wex “Jurisdiction”. This is an appropriate direct source for the three Claims, provided the U.S.-law boundary is explicit.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Jurisdiction concerns the authority of a court or government agency to exercise legal power | Wex “Jurisdiction”, opening definition: power of a court to adjudicate cases and issue orders; territory within which a court/agency may exercise power |
| B | Jurisdiction can depend on the person/parties, subject matter and territory | Wex “Jurisdiction: An Overview”, the three components: personal jurisdiction, subject-matter jurisdiction and territorial jurisdiction; cross-reference “Personal Jurisdiction” and “Subject Matter Jurisdiction” |
| C | Legal rules and procedures are jurisdiction-specific; U.S. examples must not be presented as universal law | Wex “Jurisdiction”, examples tied to the U.S. Constitution, federal statutes, state courts and state law; Wex landing page identifies the collection as a U.S.-law legal dictionary/encyclopedia |

Sources:
- Cornell LII Wex, “Jurisdiction”: https://www.law.cornell.edu/wex/Jurisdiction
- Cornell LII Wex, “Personal Jurisdiction”: https://www.law.cornell.edu/wex/Personal_Jurisdiction
- Cornell LII Wex, “Subject Matter Jurisdiction”: https://www.law.cornell.edu/wex/subject_matter_jurisdiction
- Cornell LII Wex, “Wex”: https://www.law.cornell.edu/wex/index

The source directly defines jurisdiction and separates personal, subject-matter and territorial dimensions. Its examples and doctrine are U.S.-law focused. Keep Claim C as an explicit scope boundary; do not present the Cornell explanation as a universal account of jurisdiction in every legal system.

No Claim wording change is proposed. Add exact heading-level locators to all three EUs. The Wex landing page also states that its entries are community-built legal reference material and are not legal advice or an official position of Cornell University/Law School. Preserve that source-status limitation.

## 4. Public Administration Basics — Claims A–C

Current records:
- `CLM-PUBLIC_ADMINISTRATION_BASICS-A/B/C@1`
- `EU-PUBLIC_ADMINISTRATION_BASICS-A/B/C@1`
- `SRC-PUBLIC_ADMINISTRATION_BASICS@1`

Current Source: OECD Public Governance portal. It is a broad institutional landing page and is not a sufficiently precise source for all three Claims.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Public administration is connected with implementation of state functions and provision of public services | UN Human Rights Council report A/HRC/25/27, para. 5: UNDP definition of public administration as machinery for management/implementation of government activities, laws, regulations and decisions and provision of public services |
| B | Administrative processes operate within established powers and procedures | A/HRC/25/27, para. 5: public-sector governance as regimes of laws, rules, judicial decisions and administrative practices that constrain, prescribe and enable provision of publicly supported goods/services |
| C | Content and powers of public bodies depend on jurisdiction and applicable rules | A/HRC/25/27, paras. 5–6: no universally recognized definition of public service; definitions vary; public administration and public-sector governance are framed by legal and administrative systems |

Sources:
- UN Human Rights Council, A/HRC/25/27, “Good governance and human rights”: https://digitallibrary.un.org/record/766713/files/A_HRC_25_27-EN.pdf
- OECD Recommendation of the Council on Public Service Leadership and Capability (OECD/LEGAL/0445): https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0445
- OECD Recommendation of the Council on Human-Centred Public Administrative Services (OECD/LEGAL/0503): https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0503

The UN report provides a direct source-fit correction. It states that there is no universally recognized definition of public service, quotes a UNDP definition of public administration, and defines public-sector governance through laws, rules, judicial decisions and administrative practices. It directly supports A–C with the jurisdictional/context boundary intact.

**Recommended Source correction:** version the current OECD portal Source identity/URI to the exact UN report A/HRC/25/27, or retain the OECD portal as a separate contextual Source and add a distinct UN Source/Evidence Use chain. Do not mix UN and OECD material in one Source record. No new ID is assigned here.

## 5. Social Statistics Basics — Claims A–C

Current records:
- `CLM-SOCIAL_STATISTICS_BASICS-A/B/C@1`
- `EU-SOCIAL_STATISTICS_BASICS-A/B/C@1`
- `SRC-SOCIAL_STATISTICS_BASICS@1`

Current Source: UN Statistics Division, “Demographic and Social Statistics”. It is appropriate for Claim A; Claims B/C need additional official methodology sources.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Social statistics cover data about populations, social conditions and related aspects of societal life | UN Statistics Division, “Demographic and Social Statistics” portal and domain pages: population/censuses, migration, education, health, disability, labour and living conditions |
| B | Comparability depends on definitions, classifications and collection methodology | UN Fundamental Principles of Official Statistics, Principle 9 “Use of International Standards”; also Principle 3 on transparent concepts, definitions, classifications, sources, methods and procedures |
| C | A statistical indicator describes an operationally defined set of observations and should not automatically be treated as a causal explanation | Statistics Canada, “Statistics 101: Correlation and causality”, section “Correlation =/= Causality”; UN Fundamental Principles, Principle 4 “Prevention of misuse” |

Sources:
- UN Statistics Division, “Demographic and Social Statistics”: https://unstats.un.org/unsd/demographic-social/
- UN Fundamental Principles of Official Statistics, Principle 9: https://unstats.un.org/unsd/goodprac/bpaboutpr.asp?RecId=9
- UN Fundamental Principles of Official Statistics, Principle 4: https://unstats.un.org/unsd/goodprac/bpaboutpr.asp?RecId=4
- Statistics Canada, “Statistics 101: Correlation and causality”: https://www.statcan.gc.ca/en/wtc/data-literacy/catalogue/892000062021002

Direct support:
- UN Statistics Division's domain portal and subject pages show the breadth of demographic/social statistics, including population, education, health, migration and other social conditions.
- Principle 9 says international concepts, classifications and methods promote consistency and efficiency and facilitate international comparisons.
- Principle 3 requires concepts, definitions, classifications, sources, methods and procedures to be transparent to users.
- Statistics Canada's tutorial distinguishes correlation from causality and explains why a statistical association alone does not establish cause and effect. Principle 4 entitles statistical agencies to address erroneous interpretation and misuse.

**Source graph requirement:** keep the current UN Statistics Division Source for Claim A. Add separate UN FPOS and Statistics Canada Source/EU chains for Claims B/C, or use a separately approved cross-slice source-reuse design. The current Source should not be repointed to a different publisher's standards page.

The current Source record's `provenance.method` is `editorial_context` despite its external official source identity. Treat this as a metadata/source-method review item; do not silently change it under a locator-only authorization.

## 6. Sociology Basics — three editorial placeholders

Current records:
- `CLM-SOCIOLOGY_BASICS-A/B/C@1`
- `EU-SOCIOLOGY_BASICS-A/B/C@1`
- `SRC-SOCIOLOGY_BASICS@1`

Current Claims are generic slice-scaffolding statements:
- A: the slice introduces basic concepts and relationships;
- B: interpretation depends on source, context and claim boundaries;
- C: basic knowledge does not replace specialist verification.

These are not substantive sociology propositions. The American Sociological Association provides direct, falsifiable alternatives.

| Claim | Proposed replacement statement | Direct locator candidate |
|---|---|---|
| A | Социология — научное изучение социальной жизни. | ASA brochure, “What is Sociology?” |
| B | Социологи изучают структуру обществ, их изменения и взаимодействие, а также влияние этих процессов на людей. | ASA brochure, paragraph beginning “Sociologists study the structure of societies…” |
| C | Социологические исследования используют теоретические рамки и научные методы, включая статистический анализ, опросы, этнографию, анализ разговоров и контента. | ASA brochure, paragraph on questions/hypotheses, theoretical frameworks and scientific research methods |

Source:
- American Sociological Association, *Sociology: A 21st Century Major*: https://www.asanet.org/wp-content/uploads/2023/11/Brochure_Sociology_21st_Century_Major.pdf
- Existing ASA page: https://www.asanet.org/about/about-sociology/what-sociology/

The ASA brochure directly describes sociology as the scientific study of social life, identifies the structure and change of societies and their effects on individuals, and lists statistical analysis, survey research, ethnography, conversational analysis and content analysis. It also says sociological questions/hypotheses are examined through theoretical frameworks and scientific methods.

**Recommended implementation:** version Source identity/URI to the exact ASA brochure (or create a separate Source if the current page must remain) and version Claims A–C to v2 with the proposed substantive statements. Version the three EUs to v2 with direct locators and current Claim/Source references. Do not merely add locators to the current placeholder Claims; that would preserve non-substantive statements.

Rights: ASA is a professional association and its brochure is copyright-controlled. Attribute and paraphrase; no permission to reproduce the brochure or graphics is implied.

## 7. Units and Measurement — Claims A–C

Current records:
- `CLM-UNITS_AND_MEASUREMENT-A/B/C@1`
- `EU-UNITS_AND_MEASUREMENT-A/B/C@1`
- `SRC-UNITS_AND_MEASUREMENT@1`

Current Source: NIST “SI Units”. This is direct for the SI system in Claim B but not sufficient for the metrological definition of measurement in A or uncertainty in C.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Measurement expresses a quantity quantitatively relative to an accepted unit and procedure | JCGM 200:2012, International Vocabulary of Metrology (VIM), §2.1 “measurement”; §2.9 “measurement result”; §2.12 “measurement procedure” |
| B | The SI defines a coherent set of units for expressing physical quantities | BIPM SI Brochure, §1.1 “The SI” and Table 1 “The seven base units of the SI”; NIST “SI Units” base-unit table |
| C | A measurement result should not be treated as exact without accounting for unit, method and measurement uncertainty | VIM §2.26 “measurement uncertainty”; NIST Technical Note 1297, §2.2.1 and guidance on reporting measurement results with uncertainty |

Sources:
- JCGM 200:2012 VIM, §2.1: https://jcgm.bipm.org/vim/en/2.1.html
- JCGM 200:2012 VIM, §2.26: https://jcgm.bipm.org/vim/en/2.26.html
- BIPM, *The International System of Units (SI Brochure)*: https://www.bipm.org/en/publications/si-brochure
- NIST, “SI Units”: https://www.nist.gov/pml/owm/metric-si/si-units
- NIST Technical Note 1297: https://www.nist.gov/pml/nist-technical-note-1297

Direct support:
- VIM §2.1 defines measurement as an experimental process of obtaining one or more quantity values attributable to a quantity.
- VIM §2.9 and §2.12 define measurement results and procedures.
- The SI Brochure §1.1 describes the SI as a coherent system of units; Table 1 lists the seven base units.
- VIM §2.26 defines measurement uncertainty as a non-negative parameter characterizing the dispersion of quantity values attributed to a measurand based on the information used.
- NIST TN 1297 provides guidance for evaluating and reporting uncertainty.

**Source graph requirement:** retain the existing NIST Source for Claim B. Add a distinct VIM Source/EU chain for Claim A and a VIM/NIST uncertainty chain for Claim C. Do not point the existing NIST SI Source to the BIPM VIM document or merge publishers in one Source record.

Support boundary: measurement uncertainty does not mean every measurement is unusable or that all results have identical uncertainty. The result must be reported with the relevant unit, method and uncertainty statement appropriate to the measurement.

## 8. Rights, source and editorial gates

- Cornell LII Wex is a U.S.-law legal reference, not a universal legal code or legal advice.
- UN and OECD public-administration sources have separate institutional status and rights terms; keep them distinct.
- UN Statistics Division and Statistics Canada sources are official statistical-method references; preserve the distinction between correlation, causation and indicator definitions.
- ASA brochure is copyright-controlled; paraphrase and attribute.
- BIPM VIM/SI Brochure are official metrology references; check BIPM reuse terms and do not copy tables/figures without permission.
- NIST TN 1297 is a U.S. Government technical note; check third-party figures/components.
- All five slices remain HOLD pending canonical locator implementation, source rights, independent editorial review and Human View.

## 9. Recommended execution order after owner authorization

1. Locator-only: Law A–C; Social Statistics A; Units and Measurement B.
2. Source graph: Public Administration A–C using the UN report; Social Statistics B/C using UN FPOS and Statistics Canada; Units and Measurement A/C using VIM and NIST TN 1297.
3. Sociology: approve three substantive Claim replacements; version Claims A–C and their EUs; align Source identity/URI to ASA.
4. Re-fetch all authorized records at one frozen HEAD; apply only approved versioned changes, validate exact Claim→EU→Source references, run affected-slice tests and then full release gates on the final immutable HEAD.

## 10. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change any Claim statement or version;
- create new canonical Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve or amend the 15 locator/source proposals; separately approve Sociology's three substantive Claim replacements and the additional UN/Statistics Canada/VIM source/EU dependency chains.
