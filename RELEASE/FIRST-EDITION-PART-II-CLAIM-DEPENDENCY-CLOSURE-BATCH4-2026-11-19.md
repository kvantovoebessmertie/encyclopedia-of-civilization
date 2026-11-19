# First Edition — Part II Claim Dependency Closure Batch 4

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `7e47ce9a4bd25d124a0398b4c9b20f1a04c8c52e`  
Status: **15/15 CLAIMS AND 18/18 EVIDENCE USE CHAINS ID/VERSION/TYPE MATCH; ALL HOLD; 15/18 EUS HAVE PINPOINTS**

## 1. Scope and graph result

This batch closes the Claim dependency chains for accounting, administrative law, archival science, artificial intelligence and biochemistry. Administrative-law Claims each have two independent Evidence Use records (Cornell LII and the U.S. Code).

| Check | Result |
|---|---:|
| Claims fetched and parsed | 15/15 |
| Evidence Use records fetched and parsed | 18/18 |
| Source records fetched and parsed | 7/7 |
| Claim ID/version/type matches | 15/15 |
| Evidence Use `claim_ref` matches exact Claim | 18/18 |
| Evidence Use `source_ref` matches exact Source | 18/18 |
| Claim provenance source identity matches EU source target | 15/15 |
| Evidence Use records with claim-specific locators | 15/18 |
| Source records with external locator/pinpoint | 5/7 |

All 40 exact-version records in this batch were already present in the master register. No additional dependency key was discovered. This batch advances their graph verification status only.

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Locator / note |
|---|---|---|---|---|
| accounting-basics | `CLM-ACCOUNTING_BASICS-A@1` | `EU-ACCOUNTING_BASICS-A@1` | `SRC-ACCOUNTING_BASICS@1` | No EU pinpoint |
| accounting-basics | `CLM-ACCOUNTING_BASICS-B@1` | `EU-ACCOUNTING_BASICS-B@1` | `SRC-ACCOUNTING_BASICS@1` | No EU pinpoint |
| accounting-basics | `CLM-ACCOUNTING_BASICS-C@1` | `EU-ACCOUNTING_BASICS-C@1` | `SRC-ACCOUNTING_BASICS@1` | No EU pinpoint |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-A@2` | `EU-ADMINISTRATIVE_LAW_BASICS-A@2` | `SRC-ADMINISTRATIVE_LAW_BASICS@2` | Cornell LII opening definition |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-A@2` | `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-A@2` | `SRC-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT@2` | 5 U.S.C. §551(1), §§551–559 |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-B@2` | `EU-ADMINISTRATIVE_LAW_BASICS-B@2` | `SRC-ADMINISTRATIVE_LAW_BASICS@2` | Cornell agency structure/statutory regulation |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-B@2` | `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-B@2` | `SRC-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT@2` | 5 U.S.C. §551(1), §§553–559 |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-C@2` | `EU-ADMINISTRATIVE_LAW_BASICS-C@2` | `SRC-ADMINISTRATIVE_LAW_BASICS@2` | Cornell rulemaking/adjudication/guidance |
| administrative-law-basics | `CLM-ADMINISTRATIVE_LAW_BASICS-C@2` | `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-C@2` | `SRC-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT@2` | 5 U.S.C. §§553–558 |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-A@2` | `EU-ARCHIVAL_SCIENCE-A@2` | `SRC-ARCHIVAL_SCIENCE@2` | SAA processing: appraisal, arrangement, description, preservation |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-B@3` | `EU-ARCHIVAL_SCIENCE-B@3` | `SRC-ARCHIVAL_SCIENCE@2` | SAA provenance/arrangement; source page marked PRELIMINARY DRAFT |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-C@2` | `EU-ARCHIVAL_SCIENCE-C@2` | `SRC-ARCHIVAL_SCIENCE-ICA@1` | ISAD(G) §§1.1, 2.1, 2.3 |
| artificial-intelligence-basics | `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-A@2` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-A@2` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS@2` | NIST AI RMF 1.0 §5, p. 19 |
| artificial-intelligence-basics | `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-B@2` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-B@2` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS@2` | NIST AI RMF 1.0 §5, p. 20, Fig. 5 |
| artificial-intelligence-basics | `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-C@2` | `EU-ARTIFICIAL_INTELLIGENCE_BASICS-C@2` | `SRC-ARTIFICIAL_INTELLIGENCE_BASICS@2` | NIST AI RMF 1.0 §§2, 5, pp. 9–10, 20 |
| biochemistry-basics | `CLM-BIOCHEMISTRY_BASICS-A@2` | `EU-BIOCHEMISTRY_BASICS-A@2` | `SRC-BIOCHEMISTRY_BASICS@2` | OpenStax Biology 2e §6.1 |
| biochemistry-basics | `CLM-BIOCHEMISTRY_BASICS-B@3` | `EU-BIOCHEMISTRY_BASICS-B@3` | `SRC-BIOCHEMISTRY_BASICS@2` | OpenStax Biology 2e §6.4 |
| biochemistry-basics | `CLM-BIOCHEMISTRY_BASICS-C@2` | `EU-BIOCHEMISTRY_BASICS-C@2` | `SRC-BIOCHEMISTRY_BASICS@2` | OpenStax Biology 2e §6.5 |

## 3. Source-fit, scope and rights findings

- **Accounting:** IFRS Conceptual Framework is a suitable authoritative source, but the EU records have no pinpoint. IFRS material is copyright-controlled; rights/reuse review is mandatory before any republication or derivative text.
- **Administrative law:** Cornell LII and the U.S. Code provide two distinct source paths with locators. The evidence is U.S.-jurisdiction-specific; the Context/Scope records must be checked before the Claims can be treated as general statements about administrative law. The U.S. Code is a primary legal source; Cornell Wex is secondary explanatory material.
- **Archival science:** SAA “Archives 101” is useful professional guidance, but the stored page is marked PRELIMINARY DRAFT and is community-archives guidance, not a final standard. Keep Claims A/B HOLD pending stable version/authority review. Claim C uses the ICA ISAD(G) standard with direct section locators; rights/translation terms still need review.
- **Artificial intelligence:** NIST AI RMF 1.0 provides direct section/page/figure locators for all three Claims. This is the strongest locator-complete chain in this batch. Rights/attribution and applicability to the intended edition still need formal review.
- **Biochemistry:** OpenStax Biology 2e provides direct section locators for metabolic pathways, ATP and enzymes. Confirm the current reuse licence and attribution requirements in the rights register before inclusion.

## 4. Decision

- 15/15 Claims and 18/18 Evidence Use records have exact graph references to canonical versions.
- 15/18 Evidence Use records contain claim-specific locators; accounting's three do not.
- No canonical JSON changed.
- All 15 Claims remain **HOLD** pending the outstanding source-rights, jurisdiction/scope and editorial checks. The presence of a locator does not itself approve a Claim.
- No INCLUDE/EXCLUDE decision or release allowlist was created.
