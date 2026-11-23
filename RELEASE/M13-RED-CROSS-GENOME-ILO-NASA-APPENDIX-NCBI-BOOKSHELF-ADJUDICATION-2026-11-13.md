# M13 duplicate-source adjudication: Red Cross earthquake, Genome.gov, ILO social protection, NASA appendix, and NCBI Bookshelf

Date: 2026-11-13  
Branch: m13-system-wide-depth-audit-2026-10-09  
Reviewed baseline: 975227edb65ac394e69c5f3ec051673f6a669167  
Scope: five shared-URI groups, ten Source records and 27 linked Claims. Source, Evidence Use and Claim records were inspected directly; official Red Cross, Genome.gov, ILO, NASA and NCBI pages were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Claims | Adjudication |
|---|---:|---:|---|
| American Red Cross Earthquake | 2 | 3 | One Red Cross guidance page. It directly supports aftershock and protective-action Claims. Independent USGS and FEMA sources are also linked, so corroboration is real across institutions; the duplicate Red Cross IDs do not add another source. |
| Genome.gov Genetics Glossary | 2 | 6 | One glossary page. The six linked Claims are generic editorial/methodology statements, not genetics/genomics facts. The glossary could support actual term Claims, but the current EUs do not identify terms. |
| ILO Social Protection | 2 | 6 | One ILO topic page. It directly supports the general social-protection/social-insurance framework; detailed eligibility and country-specific rights Claims need more precise standards or national law. |
| NASA Systems Engineering Handbook Appendix | 2 | 6 | One appendix page containing glossary and requirements guidance. It directly supports the requirements-writing Claims and the reliability definition; some reliability-engineering process claims are only partial. |
| NCBI Bookshelf | 2 | 6 | One library/search root, not a specific publication. It cannot directly substantiate the linked bioinformatics or systems-biology Claims. Specific NLM/NCBI and peer-reviewed sources were identified as candidates. |

Totals: 10 Source records, 27 linked Claims, five shared-URI groups. Repeated Source IDs do not create independent corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed.

## 2. American Red Cross Earthquake — two IDs, one safety page

### Source identity

Both records point to https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/earthquake.html:

- SRC-RED-CROSS-AFTERSHOCK-2026
- SRC-RED-CROSS-EARTHQUAKE

Both identify American Red Cross earthquake safety guidance. They are two Source IDs for one page, not two independent Red Cross sources. The page has distinct sections on aftershocks, damaged buildings and protective actions.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-AFTERSHOCK-DAMAGE — damaged buildings may remain unsafe after shaking and should be assessed before re-entry | Direct. The Red Cross page says to leave a damaged building if unsafe and have it inspected by a qualified professional. A separate USGS aftershock source is also linked, providing independent institutional corroboration. |
| CLM-AFTERSHOCK-EXPECT — aftershocks may follow the main earthquake and create additional risk | Direct. The page explicitly discusses aftershocks and the need to remain prepared. A separate USGS aftershock source is also linked. |
| CLM-EARTHQUAKE-DROP-COVER-HOLD — Drop, Cover and Hold On is the recommended protective action during shaking | Direct. The Red Cross page gives this instruction; a separate FEMA/Ready.gov source is also linked. |

### Disposition

- Two Red Cross Source IDs = one page; no independent corroboration between them.
- Independent corroboration is nevertheless present through the linked USGS source for aftershock Claims and FEMA/Ready.gov for Drop, Cover and Hold On.
- The EUs are generic; add the page’s Aftershocks and During an Earthquake/Drop, Cover and Hold On section locators.
- Preserve the cross-institution evidence links; do not collapse them with the duplicate Red Cross IDs.

## 3. Genome.gov Genetics Glossary — two IDs, one glossary page

### Source identity

Both records point to https://www.genome.gov/genetics-glossary:

- SRC-GENETICS_BASICS
- SRC-GENOMICS_BASICS

Both identify the NHGRI/Genome.gov Talking Glossary of Genetic and Genomic Terms. It is one glossary page with many individual term entries, not two independent sources.

### Claim/Evidence Use adjudication

The six linked Claims are generic rather than term-level science statements:

| Claim | Source fit |
|---|---|
| CLM-GENETICS_BASICS-A — the slice introduces foundational concepts and relationships for orientation in genetics | This describes the Encyclopedia slice, not an external genetics fact. Reclassify as editorial/structural metadata or replace with a substantive Claim. |
| CLM-GENETICS_BASICS-B — interpretation depends on source, context and applicability limits | General evidence-method principle, not a genetics fact. Move to a methodology standard or replace with a domain Claim. |
| CLM-GENETICS_BASICS-C — basic knowledge does not replace specialist verification when conditions, measurements or professional judgment matter | General scope/safety boundary, not a genetics fact. Move to an appropriate policy/decision record. |
| CLM-GENOMICS_BASICS-A — the slice introduces foundational concepts and relationships for orientation in genomics | Project-structure statement, not an external genomics fact. |
| CLM-GENOMICS_BASICS-B — interpretation depends on source, context and applicability limits | General evidence-method principle, not a genomics fact. |
| CLM-GENOMICS_BASICS-C — basic knowledge does not replace specialist verification when conditions, measurements or professional judgment matter | General scope/safety boundary, not a genomics fact. |

### Disposition

- Two Source IDs = one glossary page; no independent corroboration.
- A glossary can support specific definitions such as gene, genome, genetics, genomics, allele, variant or sequencing, but the current Claims do not identify any such term.
- All six EUs use generic descriptions and no term, entry title or definition passage.
- Reclassify the generic Claims or replace them with actual genetics/genomics propositions; then cite the exact glossary entries and, where needed, primary research/technical standards.

## 4. ILO Social Protection — two IDs, one topic page

### Source identity

Both records point to https://www.ilo.org/topics/social-protection:

- SRC-SOCIAL_INSURANCE_BASICS
- SRC-SOCIAL_PROTECTION_BASICS

Both identify the International Labour Organization’s Social Protection topic page. The current page redirects to the ILO social-protection topic portal. It describes social protection across the life course, social insurance, social assistance, universal health coverage, maternity protection and social protection floors.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-SOCIAL_INSURANCE_BASICS-A — social insurance is one mechanism within the wider social-protection system | Direct. The ILO page distinguishes social insurance financed through contributions from social assistance financed through taxation. |
| CLM-SOCIAL_INSURANCE_BASICS-B — coverage, financing and benefits differ among social-insurance systems | Partial. The page directly distinguishes contribution and tax financing and gives global coverage context, but it does not fully establish detailed country-specific eligibility and benefit conditions. Use ILO Convention No. 102, Recommendation No. 202 and national legislation for those details. |
| CLM-SOCIAL_INSURANCE_BASICS-C — an individual’s entitlement depends on applicable scheme rules and personal circumstances | Partial. The ILO page describes the framework but does not adjudicate an individual entitlement. Add the applicable national law/scheme rules and state the jurisdiction. |
| CLM-SOCIAL_PROTECTION_BASICS-A — social protection covers measures against social risks and needs across the life course | Direct in the ILO framework and page scope. |
| CLM-SOCIAL_PROTECTION_BASICS-B — social-protection programs vary in coverage, financing and access conditions | Partial-to-direct. The page describes different branches, contribution/tax financing and global coverage gaps; exact eligibility and access rules require country-specific evidence. |
| CLM-SOCIAL_PROTECTION_BASICS-C — assessment should consider coverage, adequacy and accessibility of protection | Direct-to-partial. ILO materials address coverage and adequacy, and the social protection floors framework; a precise source such as the World Social Protection Report or Recommendation No. 202 is preferable for the complete three-part formulation. |

### Disposition

- Two Source IDs = one ILO topic page; no independent corroboration.
- The page is suitable for the high-level distinction between social insurance and social assistance.
- Detailed rights, eligibility and benefits require jurisdiction-specific legal sources and the relevant ILO standards.
- All six EUs need exact section/paragraph or publication locators.

## 5. NASA Systems Engineering Handbook Appendix — two IDs, one appendix page

### Source identity

Both records point to https://www.nasa.gov/reference/system-engineering-handbook-appendix/:

- SRC-RELIABILITY_ENGINEERING_BASICS
- SRC-REQUIREMENTS_ENGINEERING_BASICS

Both are Source records for one NASA Systems Engineering Handbook Appendix page. The page contains Appendix B (Glossary) and Appendix C (How to Write a Good Requirement), among other appendices. These are distinct sections within one handbook resource, not independent publications.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| CLM-RELIABILITY_ENGINEERING_BASICS-A — reliability is the ability to perform the required function over the intended life with an acceptably low probability of failure | Direct. Appendix B glossary entry “Reliability” defines mission success through proper functioning over the intended life and a low/acceptable probability of failure. |
| CLM-RELIABILITY_ENGINEERING_BASICS-B — reliability depends on design choices, component quality and operating conditions | Partial. The glossary directly mentions simplicity, proper design, reliable parts/materials, long life, robustness and fault tolerance. The specific operating-condition dependency needs a reliability engineering source or a narrower Claim. |
| CLM-RELIABILITY_ENGINEERING_BASICS-C — failure analysis uses failure modes, consequences and system context to identify improvements | Partial. Appendix C’s Reliability checklist covers measurable/verifiable reliability requirements, error detection/reporting/handling/recovery, undesired events and survivability after faults. It does not set out a failure-analysis method or quantify consequence analysis. Add NASA/IEC/IEEE reliability and FMEA guidance for the broader statement. |
| CLM-REQUIREMENTS_ENGINEERING_BASICS-A — a requirement states what is needed, not how the design will implement it | Direct. Appendix B defines a requirement as a “shall” statement; Appendix C explicitly says requirements should state WHAT is needed, NOT HOW to provide it. |
| CLM-REQUIREMENTS_ENGINEERING_BASICS-B — requirements should be measurable, verifiable, clear and include tolerances where applicable | Direct. Appendix C requires complete tolerances for qualitative/performance values and checks clarity, measurability, verifiability and performance tolerances. |
| CLM-REQUIREMENTS_ENGINEERING_BASICS-C — NASA distinguishes “shall”, “will” and “should” in requirement language | Direct. Appendix C.1 states “Shall = requirement”, “Will = facts or declaration of purpose”, and “Should = goal”. |

### Disposition

- Two Source IDs = one NASA appendix page; no independent corroboration.
- Requirements Claims are well supported by Appendix B and Appendix C; add exact locators: Appendix B “Requirement” and Appendix C.1, C.2 and C.4 as applicable.
- Reliability Claim A is directly supported by Appendix B “Reliability”; B/C need narrower scope or additional reliability-engineering sources.
- Keep the distinction between an appendix glossary definition and a full reliability-engineering method.

## 6. NCBI Bookshelf — two IDs, one library root, no specific publication

### Source identity

Both records point to https://www.ncbi.nlm.nih.gov/books/:

- SRC-BIOINFORMATICS_BASICS
- SRC-SYSTEMS_BIOLOGY_BASICS

The root URL is the NCBI Bookshelf library/search interface, not a specific book, chapter or article. The two Source identities (“NCBI Bookshelf — Bioinformatics” and “NCBI Bookshelf — Systems Biology”) are subject labels, not bibliographic identities. The root page cannot itself substantiate the linked scientific propositions.

### Claim/Evidence Use adjudication and specific source candidates

| Claim | Current source fit and candidate |
|---|---|
| CLM-BIOINFORMATICS_BASICS-A — bioinformatics applies computational methods to biological information | Current Bookshelf root: not direct. A specific NLM Bookshelf entry, “Bioinformatics” in the NLM Collection Development Guidelines (NBK518748; updated 2004-01-07), defines it as organizing and analyzing biological information, usually using computers. This is a direct candidate source. |
| CLM-BIOINFORMATICS_BASICS-B — biological databases organize and retrieve biological information | Current Bookshelf root: not direct. The same NLM definition explicitly mentions developing databases, retrieval mechanisms and data-analysis tools; it can support this Claim with a separate Source record and exact entry locator. |
| CLM-BIOINFORMATICS_BASICS-C — sequence analysis identifies similarities and differences among biological sequences | Current Bookshelf root: not direct. NCBI Bookshelf chapter NBK550342, “Biological Sequence Analysis”, is a specific candidate; page retrieval was blocked by reCAPTCHA during this review, so its exact passage still needs human verification before use. |
| CLM-SYSTEMS_BIOLOGY_BASICS-A — systems biology studies interactions among components of biological systems as a whole | Current Bookshelf root: not direct. Vieira and Laubenbacher, “Computational Models in Systems Biology: Standards, Dissemination, and Best Practices” (Current Opinion in Biotechnology, 2022; PMCID PMC9177621), directly describes models encoding interactions among parts of a biological system. |
| CLM-SYSTEMS_BIOLOGY_BASICS-B — systems biology integrates experimental data with mathematical/computational models | Current Bookshelf root: not direct. The 2022 review discusses experimental approaches, computational models, data-driven and mechanistic models, and systems-biology modeling; use exact sections and narrow wording to what it directly supports. |
| CLM-SYSTEMS_BIOLOGY_BASICS-C — network representations describe relationships among biological components | Current Bookshelf root: not direct. The 2022 review identifies biochemical reaction networks and gene-regulatory networks, and describes SBML/SBGN standards for representing biological models; use a specific standard/review passage. |

### Disposition

- Two Source IDs = one Bookshelf library root; no independent corroboration.
- Replace the root index with bibliographically complete records for the actual NLM entry, sequence-analysis chapter and systems-biology review/standards if authorized.
- Do not treat a search portal or library catalogue as if it were the cited book or article.
- The EUs are generic and contain no book title, chapter, author, publication date, DOI, PMCID or passage locator.

## 7. Consolidated audit decision and next actions

1. Count one source identity per shared URI: Red Cross = 1; Genome.gov glossary = 1; ILO Social Protection = 1; NASA appendix = 1; NCBI Bookshelf root = 1.
2. Keep all 27 Claims in the M13 denominator. Do not merge Source IDs or Evidence Use records solely because their URLs match.
3. Preserve real independence:
   - Red Cross aftershock guidance is independently corroborated by USGS.
   - Red Cross Drop, Cover and Hold On guidance is independently corroborated by FEMA/Ready.gov.
   - The two Red Cross IDs themselves are not independent.
4. Reclassify the six Genome.gov and six other generic slice-description Claims as editorial/methodology metadata or replace them with substantive subject Claims.
5. Use ILO conventions/recommendations and jurisdiction-specific law for individual entitlement and detailed benefit rules.
6. Use NASA Appendix B/C exact locators; supplement reliability engineering methods with a dedicated standard or handbook.
7. Replace the NCBI Bookshelf root with exact publications and chapter/entry locators; verify the sequence-analysis chapter manually because automated retrieval was blocked.
8. After authorized canonical corrections, run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA.

## 8. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; main remains unchanged.

This report records source identity, linkage, source fit and the difference between a library root, glossary, guidance page, handbook appendix and specific publication. It is not a release approval or authorization to edit canonical records.
