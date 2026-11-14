# M13 Batch 51 — Lane 4 source-passage and D/E/B review

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Frozen selection revision: `3f4af7b8da0064b4c611fdbe6decff232efdf702`  
Queue workflow: `43190842072`; artifact: `13929979132`  
Scope: Lane 4, 20 Claims. Append-only audit documentation; no canonical Claim, Evidence Use, or Source records are modified.

## Method and limits

- Reviewed all 20 Claim records and all 21 associated Evidence Use records in the frozen Batch 51 evidence packets against repository JSON at the frozen revision.
- Checked public source pages and authoritative indexed source content where retrievable. Broad topic hubs, bibliographic catalogues and standard previews are not treated as full technical passage review.
- No Evidence Use entry in this lane preserves a sufficiently precise claim-specific section/page/table/figure locator. E is therefore 1 throughout this first pass.
- The textile-fibre Claim has two distinct Evidence Use links (The Met and FAO AGRIS); both Claim links and source references were checked. Their scope is explicitly limited: the FAO bibliographic record is about long vegetable fibres (flax, hemp, jute, tow and ramie), and the Met exhibition compares selected plant fibres and regional processing.
- The ISO/IEC 31010 public preview confirms the standard's purpose and broad application, but the full standard is not available in the public preview. The EPA septic source is directly accessible and explicitly warns against pumping a tank during flooded/saturated drainfield conditions.
- Two cited pages could not be retrieved directly in this pass (SEP Philosophy of Language and DOE renewable-energy page). Their fit is not certified.
- Scores are provisional desk assessments, not specialist certification, independent review, or publication clearance.

## Batch accounting

- Claims reviewed: 20/20.
- Evidence Use records reviewed: 21/21.
- Claim → Evidence Use → Source references verified against repository JSON: 20/20, including both textile-fibre links.
- Source pages or authoritative source content checked: 12 of 14 distinct source identities; 2 pages not retrievable directly.
- Evidence Use entries with explicit claim-specific locator: 0/21.
- Canonical Claim/Evidence Use/Source JSON modified: 0.
- Automated D/E/B scoring: none.
- Disposition: all 20 HOLD pending pinpoint remediation and any required specialist/editorial review.

## Scored review

| # | Claim | D | E | B | Source/passage finding and disposition |
|---:|---|---:|---:|---:|---|
| 61 | `CLM-MICROBIOLOGY_BASICS-C@1` | 3 | 1 | 3 | OpenStax Microbiology Chapter 1 directly describes microorganisms as often helpful, sometimes harmful, and playing fundamental ecosystem roles; the distinction among beneficial, neutral and pathogenic effects depends on organism and context. Strong fit; add the exact chapter passage locator. HOLD pending pinpoint. |
| 62 | `CLM-PHILOSOPHY_BASICS-A@1` | 1 | 1 | 1 | The cited SEP Philosophy overview could not be retrieved (404) and the source identity alone does not establish the breadth of basic philosophical concepts and relations. HOLD; verify the source URL and add a direct introductory source/locator. |
| 63 | `CLM-PHILOSOPHY_OF_LANGUAGE_BASICS-B@1` | 2 | 1 | 2 | SEP Philosophy of Language is an appropriate subject source by identity, but the cited URL returned 404 in this pass. The claim is plausible and appropriately contextual, but cannot be certified without verifying the exact entry and passage. HOLD; correct/verify the canonical source URL and pinpoint the relevant language-use/context section. |
| 64 | `CLM-PHILOSOPHY_OF_MIND_BASICS-C@1` | 2 | 1 | 2 | SEP The Mind/Brain Identity Theory directly addresses the relation between mental states/processes and brain states/processes. It does not, by identity alone, establish the complete distinction among observable behaviour, physical processes and subjective experience. HOLD; add a passage on phenomenal experience/behavioural evidence and narrow the claim if needed. |
| 65 | `CLM-PLANT_BIOLOGY_BASICS-A@1` | 3 | 1 | 3 | OpenStax Biology 2e §30.5 directly explains transport of water, nutrients/solutes and photosynthates through plant roots, stems and leaves, including xylem and phloem. Strong direct fit; add the §30.5 locator. HOLD pending pinpoint. |
| 66 | `CLM-RENEWABLE_ENERGY_BASICS-A@1` | 1 | 1 | 1 | The cited DOE renewable-energy URL returned 404 in this pass. The source fit and current canonical location are not verified. HOLD; replace/verify the DOE source and add a precise introductory passage. |
| 67 | `CLM-RISK_ANALYSIS_BASICS-D@1` | 3 | 1 | 3 | IEC 31010:2019 is explicitly a standard on risk-assessment techniques and its public preview states that it guides selection/application across situations and supports decisions under uncertainty. Strong fit for matching technique to purpose/context and uncertainty; the full standard's technical clauses still need a precise locator and rights/access review. HOLD. |
| 68 | `CLM-ROBOTICS_BASICS-A@1` | 2 | 1 | 2 | NASA Robotics is an appropriate institutional topic hub, but the page is primarily a portal to programmes and projects rather than a clear foundational definition of robotics concepts/relations. HOLD; add a direct robotics-system definition or textbook/standard locator. |
| 69 | `CLM-SEPTIC-FLOOD-NO-PUMP@1` | 3 | 1 | 3 | U.S. EPA directly states not to pump a septic tank during flooded or saturated drainfield conditions because the tank may float and damage inlet/outlet pipes. This is a strong, high-consequence direct match. Add the exact EPA Q&A locator and preserve the warning without weakening it. HOLD pending pinpoint and independent safety review. |
| 70 | `CLM-SOCIAL_STATISTICS_BASICS-C@1` | 1 | 1 | 1 | UN Statistics Division's Demographic and Social Statistics page is a programme/standards hub. It does not directly establish the distinction between a statistical indicator and a causal explanation. HOLD; cite a statistics/methodology source explicitly discussing descriptive indicators and causal inference. |
| 71 | `CLM-SOLAR_SYSTEM_BASICS-B@1` | 3 | 1 | 3 | NASA Solar System Facts is a direct official reference for the Sun as the star at the centre of the Solar System. Strong fit; add the exact NASA statement locator. HOLD pending pinpoint. |
| 72 | `CLM-SOLAR_SYSTEM_BASICS-C@1` | 3 | 1 | 3 | NASA Solar System Facts is a direct official reference for the Solar System's location in the Milky Way. Strong fit; add the exact NASA statement locator. HOLD pending pinpoint. |
| 73 | `CLM-STATE_FORMATION-C@1` | 2 | 1 | 2 | The World History Encyclopedia review of Scott's *Against the Grain* is relevant to the historical caution against projecting modern state categories onto early societies, but it is a review of a particular work rather than a general primary/academic source. HOLD; cite the book's relevant chapter and an independent historical-method source, preserving chronological and regional limits. |
| 74 | `CLM-TEMPERATURE_BASICS-A@1` | 3 | 1 | 3 | NIST's Kelvin introduction is a direct metrology source for the SI unit kelvin and thermodynamic temperature. Strong fit; add the exact definition/introductory passage locator. HOLD pending pinpoint. |
| 75 | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-D@1` | 2 | 1 | 2 | The Met exhibition discusses selected plant fibres (cotton, flax, hemp, ramie) and regional processing; FAO AGRIS records a 1904 guide limited to long vegetable fibres including flax, hemp, jute, tow and ramie. These sources support the non-interchangeability/context boundary, but not a general comparison of all plant fibres or suitability for every product. HOLD; narrow the Claim to the named fibres and add technical property/process evidence. |
| 76 | `CLM-WAVES_AND_SOUND_BASICS-A@1` | 3 | 1 | 3 | OpenStax Physics §13.2 directly defines wave properties including amplitude, frequency, wavelength and velocity. Strong fit; add the exact definition/section locator. HOLD pending pinpoint. |
| 77 | `CLM-WAVES_AND_SOUND_BASICS-B@1` | 3 | 1 | 3 | OpenStax Physics §13.2 directly relates wave speed, frequency and wavelength and supports the relation v=fλ. Add the equation and surrounding conditions/section locator. HOLD pending pinpoint and notation check. |
| 78 | `CLM-WAVES_AND_SOUND_BASICS-C@1` | 2 | 1 | 2 | OpenStax §13.2 is a general wave-properties section; it does not, by its title or objectives alone, establish that sound is a mechanical wave requiring a material medium. HOLD; add a direct acoustics passage on sound propagation through media. |
| 79 | `CLM-COMPILER_BASICS-A@1` | 3 | 1 | 3 | LLVM's Kaleidoscope tutorial explicitly separates lexer, parser/AST and code-generation stages, supporting the staged compiler representation in the Claim. Strong fit; add the tutorial's exact chapters/sections. HOLD pending pinpoint. |
| 80 | `CLM-COMPILER_BASICS-B@1` | 3 | 1 | 3 | LLVM's parser tutorial constructs an abstract syntax tree from source-language syntax, directly supporting the distinction between program structure and concrete text. Strong fit; add the exact parser/AST section locator. HOLD pending pinpoint. |

## Lane findings

- First-pass review: **20/20 recorded**.
- Disposition: **20 HOLD**.
- D distribution: **3 score 1, 6 score 2, 11 score 3** (mean 2.40).
- E distribution: **20 score 1** (mean 1.00).
- B distribution: **3 score 1, 6 score 2, 11 score 3** (mean 2.40).
- Claim-specific locators explicitly preserved in Evidence Use: **0/21**.
- Exact repository Claim → Evidence Use → Source references verified: **20/20**, including both textile-fibre evidence links.
- Strong direct-fit sources needing pinpoints: OpenStax Microbiology, OpenStax Plant Biology, IEC 31010, U.S. EPA septic flood guidance, NASA Solar System Facts, NIST Kelvin, OpenStax Physics waves, and LLVM compiler tutorial.
- Source-fit follow-ups: SEP Philosophy/Philosophy of Language URLs require correction/verification; DOE renewable-energy URL returned 404; NASA Robotics and UN Statistics Division are broad hubs; World History Encyclopedia review needs a primary/academic corroboration; sound propagation needs an acoustics-specific passage; textile-fibre claims must remain limited to the fibres actually covered by the sources.
- High-consequence item: septic pumping prohibition is directly supported by EPA, but remains HOLD until the exact locator is recorded and an independent safety review is complete.
- Canonical JSON changes: **0**.
- Specialist, independent, Human View, rights, editorial, and publication gates cleared: **0**.

## Required follow-up

1. Add exact, stable passage locators to the Evidence Use records only under bounded editorial authorization.
2. Prioritize EPA septic-flood guidance for pinpoint and independent safety review.
3. Verify/correct the SEP Philosophy and Philosophy of Language source URLs and the DOE renewable-energy URL.
4. Add direct method sources for social-statistics causality and sound propagation through a material medium.
5. Narrow textile-fibre claims to the actual source coverage and corroborate historical state-formation claims with primary/academic material.
6. Keep all 20 Claims on HOLD until locator, source-fit, independent-review and Human View gates are completed.
