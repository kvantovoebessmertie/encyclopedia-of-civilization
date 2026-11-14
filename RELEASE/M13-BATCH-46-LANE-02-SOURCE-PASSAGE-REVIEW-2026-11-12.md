# M13 Batch 46 — Lane 2 source-passage and D/E/B review

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Frozen selection revision: `e5be4cb9093b4adf07825e21b45e98ce5c7e1d45`  
Queue workflow: `43188564179`; artifact: `13928863496`  
Scope: Lane 2, 20 Claims. Append-only audit documentation; no canonical Claim, Evidence Use, or Source records are modified.

## Method and limits

- Reviewed all 20 Claim statements and Evidence Use descriptions/source identities in the frozen Batch 46 evidence packets.
- Checked public source pages where retrievable. A source identity, URI, or general topic page is not treated as claim-specific passage support.
- Only three entries in this batch (Lane 3 Claims 50–52) contain named MDN sections in Evidence Use; they receive E=2 provisionally. The other 97 entries lack sufficiently precise claim-specific pinpoints and receive E=1.
- The packet linkage fields require exact Claim → Evidence Use → Source record verification; this report does not certify those JSON edges as independently resolved.
- Scores are provisional desk assessments, not specialist certification, independent review, or publication clearance.

## Batch accounting

- Claims reviewed: 20/20.
- Evidence packet entries reviewed: 20/20.
- Canonical JSON modified: 0.
- Automated D/E/B scoring: none.
- Disposition: all 20 HOLD pending linkage verification, pinpoint remediation, and any required specialist/editorial review.

## Scored review

| # | Claim | D | E | B | Source/passage finding and disposition |
|---:|---|---:|---:|---:|---|
| 21 | `CLM-RATIOS_AND_PERCENTAGES-CONTEXT@1` | 3 | 1 | 3 | OpenStax §5.4 describes ratios as comparisons of two numbers and percent as a ratio to 100. Direct topical fit, but Evidence Use does not name the relevant subsection/paragraph or preserve a claim-specific pinpoint. HOLD pending locator and confirmation that unit/baseline wording is retained. |
| 22 | `CLM-RESEARCH_INTEGRITY_BASICS-A@1` | 3 | 1 | 3 | National Academies’ Fostering Integrity in Research is a strong authoritative source for responsible conduct in creating, reporting, and stewarding research. The book-level record lacks a specific chapter/page locator. HOLD pending pinpoint. |
| 23 | `CLM-SCIENCE_POLICY_BASICS-A@1` | 2 | 1 | 2 | OECD Science Policy is relevant to science informing public policy, but a broad topic page does not establish the full proposition about complex societal and environmental challenges. HOLD pending specific OECD section or a policy case study. |
| 24 | `CLM-SIGNAL_PROCESSING_BASICS-A@1` | 2 | 1 | 2 | MIT Signals and Systems course is relevant, but the course landing page does not pinpoint analog/digital representations or time/frequency-domain transformations. HOLD pending exact lecture/notes locator and terminology review. |
| 25 | `CLM-SOCIAL_STATISTICS_BASICS-A@1` | 2 | 1 | 2 | UN Statistics Division’s demographic and social statistics page is relevant to population and social-condition statistics, but the broad page does not establish the full definition. HOLD pending specific statistical domain/metadata locator. |
| 26 | `CLM-STRUCTURAL_ENGINEERING_BASICS-A@1` | 2 | 1 | 2 | NIST Structural Engineering is a broad institutional page; it does not pinpoint the claim's full scope of scientific and engineering methods, structural behaviour, and safety. HOLD pending specific NIST research or standards source. |
| 27 | `CLM-STRUCTURAL_ENGINEERING_BASICS-B@1` | 2 | 1 | 2 | NIST Structural Engineering may be relevant to structural damage, failure, and resilience, but the registered landing page is not a passage-level source for the full list. HOLD pending specific research/standards locators. |
| 28 | `CLM-STRUCTURAL_ENGINEERING_BASICS-C@1` | 2 | 1 | 3 | The claim's dependency on system, materials, loads, conditions, and applicable codes is sound as a boundary statement, but NIST's broad page does not directly support each factor. HOLD pending engineering-code/standard locators. |
| 29 | `CLM-SUPPLY_CHAIN_BASICS-A@1` | 3 | 1 | 3 | CISA and NIST SP 800-161 Rev.1 Update 1 directly address multi-tier ICT supply-chain cybersecurity risk and upstream supplier dependencies. Strong fit within cybersecurity/ICT supply chains; no section/page locator is retained. HOLD pending precise locators and scope boundary. |
| 30 | `CLM-TAXATION_BASICS-B@1` | 3 | 1 | 3 | OECD Tax Policy and IMF Fiscal Affairs are relevant to revenue raising and tax effects on work, investment, and innovation incentives. The sources are broad and no passages are pinpointed; the claim should not be read as individual tax advice. HOLD pending locators and jurisdictional boundary. |
| 31 | `CLM-TAXATION_BASICS-C@1` | 3 | 1 | 3 | OECD and IMF sources are relevant to tax structure, economic environment, and institutional implementation. The full causal formulation requires precise passages and should not imply a universal optimal tax design. HOLD pending pinpoint(s). |
| 32 | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-A@1` | 3 | 1 | 3 | FAO AGRIS describes a guide covering preparation, carding, spinning, and twisting of long vegetable fibres including flax, hemp, and jute; The Met provides comparative plant-fibre context. FAO coir-specific processing cannot be generalized to all fibres. HOLD pending exact FAO guide page/section and fibre-specific boundaries. |
| 33 | `CLM-THERMODYNAMICS_BASICS-A@1` | 3 | 1 | 2 | OpenStax College Physics Chapter 15 is relevant to heat, work, and energy transformations, but the registered chapter introduction does not pinpoint the full definition. HOLD pending exact section locator. |
| 34 | `CLM-THERMODYNAMICS_BASICS-B@1` | 2 | 1 | 2 | The registered OpenStax Chapter 15 introduction does not pinpoint the first-law statement or sign convention for heat and work. HOLD pending the exact first-law section and a consistent convention. |
| 35 | `CLM-THERMODYNAMICS_BASICS-C@1` | 2 | 1 | 2 | The chapter introduction does not directly pinpoint the second law and entropy relation. HOLD pending the exact second-law section and clarification that entropy is not itself a simple direction label. |
| 36 | `CLM-UTC-CIVIL-BOUNDARY@1` | 3 | 1 | 3 | BIPM describes UTC as the international reference time scale and distinguishes its relationship to civil time. The proposition is well bounded, but no exact BIPM passage/section locator is recorded. HOLD pending pinpoint. |
| 37 | `CLM-UTC-INTERNATIONAL@1` | 3 | 1 | 3 | NIST Time Realization describes UTC as the internationally coordinated standard of time. Strong support, but the Evidence Use lacks an exact locator and should distinguish UTC from local civil time. HOLD. |
| 38 | `CLM-TRADE_NETWORKS-A@1` | 2 | 1 | 2 | British Museum's ancient Assyria trade material supports a specific historical example of routes and intermediaries, not a broad generalization about all ancient trade networks. HOLD; narrow the Claim to the example or add comparative historical sources. |
| 39 | `CLM-M5-TRANSPORT-RESILIENCE-D@1` | 3 | 1 | 2 | World Bank Transport connects resilient transport infrastructure and logistics with reliable supply chains and continuity of access. Relevant support, but no exact passage is pinpointed and the claim combines infrastructure resilience with service continuity. HOLD pending locator. |
| 40 | `CLM-TRANSPORTATION_BASICS-A@1` | 3 | 1 | 3 | World Bank transport material supports connections that move people and goods to markets/opportunities; U.S. DOT supplies institutional context. The claim is basic and well scoped, but the source passages are not pinpointed. HOLD. |

## Lane findings

- First-pass review: **20/20 recorded**.
- Disposition: **20 HOLD**; no Claim is accepted for publication by this report.
- Explicit claim-specific Evidence Use locators: **0/20**.
- Canonical JSON changes: **0**.
- Specialist, independent, Human View, rights, editorial, and publication gates cleared: **0**.
