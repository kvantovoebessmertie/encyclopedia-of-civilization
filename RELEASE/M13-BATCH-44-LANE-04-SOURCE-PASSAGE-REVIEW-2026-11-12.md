# M13 Batch 44 — Lane 4 source-passage and D/E/B review

Date: 2026-11-12
Branch: `m13-system-wide-depth-audit-2026-10-09`
Selection revision: `d3a0d14b1be7873ee73dcdff435fe0684fb40170`
Queue artifact: workflow run `43156665644`, artifact `13915369047`
Scope: fourth frozen lane, 20 Claims. No canonical Claim, Evidence Use, or Source records are modified by this report.

## Method and limits

- Read the frozen Lane 4 queue and the exact Claim, Evidence Use and Source records for all selected Claims, including additional Evidence Use/Source records where the queue lists more than one.
- Checked public source passages for the substantive propositions. General landing pages, source labels and additional source counts are not treated as proof of claim-specific support.
- The lane contains generic Evidence Use descriptions and some more detailed descriptions, but none of the 20 preserves a complete, exact claim-specific section/paragraph/page locator. E is therefore capped at 1 under the M13 rubric.
- Provisional D/E/B scores are reviewer-assigned first-pass desk assessments, not automated scores, specialist certification, independent review or publication clearance.
- All queue risk flags remain routing signals only.

## Batch accounting

- Frozen lane capacity: 20.
- First-pass reviews recorded: 20/20.
- Claim/Evidence Use/Source links: checked against exact stored IDs and the evidence packet. Separator differences are retained; no ID rewrite is performed.
- Complete claim-specific pinpoint locators: 0/20.
- Canonical records modified: 0.
- All 20 Claims remain HOLD.

## Scored review

| # | Claim | D | E | B | Source-passage finding and disposition |
|---:|---|---:|---:|---:|---|
| 1 | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C@1` | 3 | 1 | 3 | OECD Sustainable Urban Development page identifies water, housing, transport, infrastructure and climate policy as local-government domains and supports place-based priorities, vertical coordination, synergies and overcoming policy silos. The Claim itself is well-bounded: coordination helps, but does not guarantee equal outcomes. Evidence Use describes the OECD support but does not identify the exact page section/report or passage. HOLD pending locator and verification of the “fragmentation” wording against the cited OECD page. |
| 2 | `CLM-INDUSTRIAL_SAFETY_BASICS-C@1` | 2 | 1 | 2 | OSHA's Process Safety Management standards page distinguishes general-industry and construction standards and identifies the applicable U.S. regulatory framework. This supports that safety requirements are process/industry/standard dependent, but the Claim generalizes across jurisdictions while the registered source is U.S.-specific and focused on process safety. HOLD; bound jurisdiction or add a cross-jurisdictional authoritative source and pinpoint. |
| 3 | `CLM-INTERNATIONAL_LAW_BASICS-A@1` | 2 | 1 | 2 | Cornell LII defines international law as rules/principles governing relations and conduct of sovereign states and also international organizations and individuals; its subjects-of-international-law page discusses the evolving recognition of legal subjects. This directly supports the general proposition. The canonical Source set includes the UN Charter and Britannica, but the Evidence Use descriptions are generic and do not point to the Cornell/other exact definitions; source records do not fully preserve the source passage used. HOLD pending source identity/URI reconciliation and precise locator. |
| 4 | `CLM-INTERNATIONAL_RELATIONS_BASICS-A@1` | 3 | 1 | 3 | The UN Charter page directly identifies the Charter as the founding document of the UN and states it entered into force on 24 October 1945. This is a precise historical/legal proposition. Evidence Use names the Charter page but does not pinpoint the official historical note or entry-into-force date. HOLD pending locator; substantive proposition strongly supported. |
| 5 | `CLM-LABOR_ECONOMICS_BASICS-A@1` | 1 | 1 | 1 | ILOSTAT identifies labour-market topics including labour force, employment, unemployment, earnings, working time, social dialogue and productivity. This supports parts of the field description but the registered URI points only to an ILO wages topic page and the source identity is a generic label. The claim is a broad field definition and does not explain how markets, wages and institutions interact. HOLD; select a direct labour-economics source and pinpoint. |
| 6 | `CLM-LABOR_RELATIONS_BASICS-A@1` | 2 | 1 | 2 | ILO collective-bargaining and labour-relations material is relevant to employer/union negotiation; GOV.UK's official guidance explicitly describes collective bargaining as employers and unions discussing workers' terms and conditions. This supports the claim, but the canonical ILO Evidence Use does not identify the relevant ILO passage or a jurisdictional boundary; the GOV.UK material is UK-specific. HOLD pending exact ILO locator and scope statement. |
| 7 | `CLM-LAND_USE_PLANNING_BASICS-B@1` | 1 | 1 | 1 | The claim that planning decisions influence access to infrastructure, services and transport is plausible, and UN-Habitat's land-use topic is relevant. However, the registered page is a broad topic landing page and no exact passage was established in this pass linking land-use planning choices to those three access outcomes. HOLD pending a precise UN-Habitat/UN SDG urban-planning source and locator. |
| 8 | `CLM-MATTER_BASICS-A@1` | 1 | 1 | 1 | OpenStax Chemistry 2e §1.2 classifies matter as pure substances or mixtures and divides pure substances into elements and compounds. This supports the element/compound/mixture distinction, but the Claim is a compressed inventory without explaining composition/properties. Evidence Use points to the chapter introduction rather than §1.2. HOLD pending pinpoint and depth review. |
| 9 | `CLM-MATTER_BASICS-B@1` | 2 | 1 | 2 | The proposition that an element is defined by atoms with the same number of protons is a standard atomic-number definition. The registered OpenStax URI points to the Chemistry 2e chapter 1 introduction and the generic EU does not identify the atomic-structure section; the directly relevant passage was not established from the linked locator in this pass. HOLD; add exact atomic-structure/atomic-number locator. |
| 10 | `CLM-MATTER_BASICS-C@1` | 1 | 1 | 1 | OpenStax Chemistry 2e §1.2 directly distinguishes mixtures from pure substances and explains that pure substances have constant composition. The claim that mixtures contain more than one chemical substance and may have variable composition is broadly supported, but EU only points to the chapter introduction and offers no pinpoint. HOLD pending locator and explanatory depth. |
| 11 | `CLM-MICROECONOMICS_BASICS-A@1` | 2 | 1 | 2 | OpenStax Principles of Economics §3.2 directly explains that demand and supply curves relate quantity and price under the ceteris paribus assumption; other relevant factors are held constant. The Claim's phrase “при заданных условиях” is a useful boundary but does not identify the other factors or distinguish movement along a curve from a shift. Registered Source is a book landing page and EU is generic. HOLD pending §3.2 pinpoint and depth refinement. |
| 12 | `CLM-MOTION_BASICS-B@1` | 1 | 1 | 0 | OpenStax University Physics §3.1 defines average velocity as displacement divided by elapsed time. The Claim uses the Russian term “средняя скорость” with “изменение положения” (displacement), which may conflate scalar average speed (distance/time) with vector average velocity (displacement/time). The registered Source URI is a broad kinematics introduction and EU has no section locator. HOLD; resolve terminology and add the exact §3.1 passage. |
| 13 | `CLM-NETWORKS_BASICS-A@1` | 1 | 1 | 2 | NIST CSRC defines a network as a system implemented with interconnected components, including routers, hubs and cabling. This directly supports the component-interconnection concept. The Claim narrows the generic NIST definition to a computer network; Evidence Use does not identify the NIST glossary definition or its exact scope. HOLD pending pinpoint and terminology check. |
| 14 | `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_A@1` | 1 | 1 | 1 | The Claim defines physiology as study of functions of living systems and how structures support those functions. OpenStax Anatomy & Physiology is a relevant textbook, but the linked Homeostasis §1.5 passage directly covers regulation/feedback, not the full general definition of physiology. The other EU paraphrases the Claim without a precise locator. HOLD; find an introductory physiology definition and section locator. |
| 15 | `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_B@1` | 2 | 1 | 2 | OpenStax Anatomy & Physiology §1.5 directly describes sensors, control centres, effectors and negative feedback maintaining physiological variables within normal ranges. This supports regulatory feedback, but the Claim's broader phrase “organ systems” and interacting processes needs a passage showing system-level coordination. Both Evidence Use records lack exact locators. HOLD pending pinpoint and mechanism scope. |
| 16 | `CLM_PHYSIOLOGY_OF_SYSTEMS_BASICS_C@1` | 2 | 1 | 3 | OpenStax §1.5 explains set points and normal ranges, supporting that physiological values fluctuate and must be interpreted against a range. It does not directly establish the Claim's additional measurement-condition/clinical-normality warning. The wording is a useful boundary, but a measurement-method/clinical reference is needed. HOLD. |
| 17 | `CLM-PLANT_PHYSIOLOGY_BASICS-B@1` | 1 | 1 | 1 | OpenStax Biology 2e §30.5 directly states that xylem and phloem are the main tissues responsible for movement of water, nutrients and photosynthates. This supports the claim, but the registered Source URI is the chapter 30 introduction and Evidence Use does not pinpoint §30.5. The claim is an introductory assertion without the transport mechanisms. HOLD pending locator and depth. |
| 18 | `CLM-POLITICAL_SCIENCE_BASICS-A@1` | 2 | 1 | 2 | OpenStax Introduction to Political Science §1.3 defines political science as systematic study of political phenomena and describes actions of individuals, groups, institutions and countries. This directly supports the Claim. Registered Source points to chapter 1 introduction rather than §1.3 and EU is generic. HOLD pending locator. |
| 19 | `CLM-POLITICAL_SCIENCE_BASICS-B@1` | 2 | 1 | 2 | OpenStax §1.5 defines empirical political science in terms of verifiable facts/evidence and testable hypotheses. This supports the Claim's observable-data and checkable-evidence elements. No §1.5 locator is preserved in Evidence Use. HOLD pending pinpoint and distinction between observation and interpretation. |
| 20 | `CLM-POLITICAL_SCIENCE_BASICS-C@1` | 2 | 1 | 2 | OpenStax §§1.4–1.5 distinguish normative political science (what should be) from empirical political science (what is). This directly supports the descriptive/normative distinction. The generic Evidence Use does not identify either section. HOLD pending pinpoint and note that real political analysis may combine descriptive and normative questions. |

## Cross-cutting findings

1. **No complete claim-specific pinpoint:** the EUs are generic or contain broad paraphrases but do not preserve exact section/paragraph/page locators. E=1 is therefore consistent even when a public passage is directly relevant.
2. **International law source traceability:** the canonical Source set points to the UN Charter and Britannica, while the exact definition and subject-scope passage checked here is from Cornell LII. Do not silently substitute that source; source identity/URI and the independent EU need an authorized reconciliation.
3. **Labour economics source fit:** ILO wage-topic URI is too narrow for the field-level claim. ILOSTAT supports topic coverage, but a direct labour-economics disciplinary source and clear scope are needed.
4. **Industrial safety jurisdiction:** OSHA PSM standards are U.S.-specific and process-safety-focused; the general Claim must not imply one universal regulatory framework.
5. **Motion terminology:** “average speed” and “average velocity” are not interchangeable in physics. Displacement/time defines average velocity; distance/time defines average speed. The Russian wording needs an explicit terminology decision.
6. **Matter source locators:** §1.2 supports classification into mixtures/elements/compounds, while the atomic-number proposition requires a different, precise atomic-structure passage.
7. **Physiology:** homeostasis §1.5 supports feedback and normal ranges, but not all three Claims equally. The broad definition and measurement-condition proposition need better-matched passages.
8. **Human-settlement integration:** OECD supports policy coordination across water, housing, transport, infrastructure and energy, but no universal outcome is guaranteed; the Claim appropriately retains this limit.
9. **Risk labels:** queue flags are triage signals and should not be represented as substantive findings.

## Disposition

- Lane 4: **20/20 first-pass reviews recorded.**
- All 20 remain **HOLD** pending exact pinpoints, source identity/scope alignment, terminology resolution and the specific depth/boundary follow-ups above.
- No canonical Claim, Evidence Use or Source JSON was modified.
- No specialist, independent, Human View, rights, editorial or publication gate is cleared.
- Next: complete Lane 5, reconcile all 100 selected Claim IDs against historical worklists, then prepare the Batch 44 reconciliation package and run exact-head CI once after the full package is committed.
