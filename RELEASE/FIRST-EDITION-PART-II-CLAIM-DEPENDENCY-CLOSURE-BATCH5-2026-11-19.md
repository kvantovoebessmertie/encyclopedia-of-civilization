# First Edition — Part II Claim Dependency Closure Batch 5

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `4ec5d55690ad2c6c17e8f046834eb8b88de2d3f6`  
Status: **15/15 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; 6/15 EUS HAVE PINPOINTS; ALL HOLD**

## 1. Scope and result

This batch closes the exact dependency graph for calculus, chemical reactions, climate science, computer networks and computer-science algorithms.

| Check | Result |
|---|---:|
| Claims fetched and parsed | 15/15 |
| Evidence Use records fetched and parsed | 15/15 |
| Source records fetched and parsed | 5/5 |
| Claim ID/version/type matches | 15/15 |
| Evidence Use `claim_ref` matches exact Claim | 15/15 |
| Evidence Use `source_ref` matches exact Source | 15/15 |
| Claim provenance source identity matches EU source target | 15/15 |
| Evidence Use records with claim-specific locator | 6/15 |
| Source records with direct locator/section | 2/5 |

Version differences were preserved. Chemical-reaction Claims are v2 and their Evidence Use records are v4, correctly referencing Claim v2 and Source v2. No version was downgraded.

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Graph result |
|---|---|---|---|---|
| calculus-basics | `CLM-CALCULUS_BASICS-A@1` | `EU-CALCULUS_BASICS-A@1` | `SRC-CALCULUS_BASICS@1` | MATCH |
| calculus-basics | `CLM-CALCULUS_BASICS-B@1` | `EU-CALCULUS_BASICS-B@1` | `SRC-CALCULUS_BASICS@1` | MATCH |
| calculus-basics | `CLM-CALCULUS_BASICS-C@1` | `EU-CALCULUS_BASICS-C@1` | `SRC-CALCULUS_BASICS@1` | MATCH |
| chemical-reactions-basics | `CLM-CHEMICAL_REACTIONS_BASICS-A@2` | `EU-CHEMICAL_REACTIONS_BASICS-A@4` | `SRC-CHEMICAL_REACTIONS_BASICS@2` | MATCH |
| chemical-reactions-basics | `CLM-CHEMICAL_REACTIONS_BASICS-B@2` | `EU-CHEMICAL_REACTIONS_BASICS-B@4` | `SRC-CHEMICAL_REACTIONS_BASICS@2` | MATCH |
| chemical-reactions-basics | `CLM-CHEMICAL_REACTIONS_BASICS-C@2` | `EU-CHEMICAL_REACTIONS_BASICS-C@4` | `SRC-CHEMICAL_REACTIONS_BASICS@2` | MATCH |
| climate-science-basics | `CLM-CLIMATE_SCIENCE_BASICS-A@1` | `EU-CLIMATE_SCIENCE_BASICS-A@1` | `SRC-CLIMATE_SCIENCE_BASICS@1` | MATCH |
| climate-science-basics | `CLM-CLIMATE_SCIENCE_BASICS-B@1` | `EU-CLIMATE_SCIENCE_BASICS-B@1` | `SRC-CLIMATE_SCIENCE_BASICS@1` | MATCH |
| climate-science-basics | `CLM-CLIMATE_SCIENCE_BASICS-C@1` | `EU-CLIMATE_SCIENCE_BASICS-C@1` | `SRC-CLIMATE_SCIENCE_BASICS@1` | MATCH |
| computer-networks-basics | `CLM-COMPUTER_NETWORKS_BASICS-A@1` | `EU-COMPUTER_NETWORKS_BASICS-A@1` | `SRC-COMPUTER_NETWORKS_BASICS@1` | MATCH |
| computer-networks-basics | `CLM-COMPUTER_NETWORKS_BASICS-B@1` | `EU-COMPUTER_NETWORKS_BASICS-B@1` | `SRC-COMPUTER_NETWORKS_BASICS@1` | MATCH |
| computer-networks-basics | `CLM-COMPUTER_NETWORKS_BASICS-C@1` | `EU-COMPUTER_NETWORKS_BASICS-C@1` | `SRC-COMPUTER_NETWORKS_BASICS@1` | MATCH |
| computer-science-algorithms-basics | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A@2` | `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A@2` | `SRC-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | MATCH |
| computer-science-algorithms-basics | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B@2` | `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B@2` | `SRC-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | MATCH |
| computer-science-algorithms-basics | `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C@2` | `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C@2` | `SRC-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | MATCH |

## 3. Substantive findings

- **Calculus:** all three Claims are substantive (limit, derivative, definite integral), but their Evidence Use records have no locators. The Source is the broad OpenStax Calculus Volume 1 landing page. Add direct sections for the relevant definitions/theorems and their conditions.
- **Chemical reactions:** all three Claims are substantive and have direct OpenStax Chemistry 2e §4.3 locators. The A/B locators point to reaction equations and coefficients; C points to worked stoichiometric examples. This is the strongest evidence-complete group in this batch, subject to rights and edition checks.
- **Climate science:** the three Claims are generic editorial scaffolding rather than climate-science propositions: “the slice introduces basic concepts”, “interpretation depends on source/context/boundaries”, and “basic knowledge does not replace specialist verification”. The NASA Climate Change: Evidence page does not substantiate these generic statements. Rewrite into falsifiable climate-science Claims or remove the placeholders; do not promote.
- **Computer networks:** the three Claims are also generic scaffolding (topic introduction, source/context caveat, and specialist-verification caveat). The NIST CSRC network glossary source is not a sufficient evidence source for those statements. Replace the placeholder Claims with actual networking propositions and add direct sources/locators.
- **Computer-science algorithms:** all three Claims are substantive and have Runestone Academy §1.2 locators for algorithm definition, pseudocode/precision, and the algorithm/program distinction. Verify the applicable open licence and attribution obligations before reuse.

## 4. Decision

- All 15 Claim → Evidence Use → Source chains have exact ID/version/type matches.
- Six EUs have claim-specific locators; the remaining nine do not.
- Six climate-science and computer-network Claims are editorial placeholders and cannot be considered substantive content.
- All 15 Claims remain **HOLD**. No INCLUDE/EXCLUDE decision or release allowlist was created.
- No canonical JSON changed.
