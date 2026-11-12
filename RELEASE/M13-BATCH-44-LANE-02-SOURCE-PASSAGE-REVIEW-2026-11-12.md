# M13 Batch 44 — Lane 2 source-passage and D/E/B review

Date: 2026-11-12
Branch: `m13-system-wide-depth-audit-2026-10-09`
Selection revision: `f20c7c0e2a078d2a423471a19869c99ef267d93c`
Queue artifact: workflow run `43079898711`, artifact `13884370584`
Scope: second frozen lane, 20 Claims. No canonical Claim, Evidence Use, or Source records are modified by this report.

## Method and limits

- Reviewed the frozen Lane 2 queue and the exact Claim/Evidence Use/Source records referenced by its evidence packets.
- Checked public source passages where retrievable. A source identity or general landing-page URI is not treated as passage-level support.
- The Evidence Use records do not preserve claim-specific section, paragraph, table, figure, or page locators. This limits E to 1 under the M13 rubric even when a suitable public passage exists.
- The ACRL secondary Evidence Use records for critical-thinking Claims A–C describe additional independent support but contain no pinpoint; their existence alone does not establish independence or claim-specific fit.
- Scores are provisional first-pass desk assessments, not specialist certification, independent review, or publication clearance. All HOLD dispositions remain in force pending exact Evidence Use locators and any required subject-matter review.

## Batch accounting

- Frozen lane capacity: 20.
- First-pass Claim reviews recorded: 20/20.
- Claim → Evidence Use → Source references: 20 candidates routed with linked records in the frozen evidence packets; no canonical linkage repair is authorized by this report.
- Claim-specific Evidence Use pinpoints: 0 recorded in the linked Evidence Use descriptions.
- Canonical records modified: 0.
- Automated D/E/B scoring: none; scores below are reviewer-assigned.
- Risk/structural flags are routing signals, not substantive findings.

## Scored review

| # | Claim | D | E | B | Source-passage finding and disposition |
|---:|---|---:|---:|---:|---|
| 1 | `CLM-COMPUTING_BASICS-B@1` | 2 | 1 | 2 | Claim defines an algorithm as an ordered sequence of steps for solving a problem or transforming input. OpenStax Introduction to Computer Science §2.1 directly defines an algorithm as ordered steps/instructions; §3.1 further describes precise instructions operating on data. The registered Source URI is only the book landing page and the Evidence Use has no section locator. HOLD pending versioned, claim-specific locator. |
| 2 | `CLM-COMPUTING_BASICS-C@1` | 2 | 1 | 2 | OpenStax §5.1 is relevant to computing systems, hardware/software and data/instruction processing. The claim is a basic proposition but the Evidence Use is generic and points only to the book-level Source. HOLD pending exact section and a concise explanation of what is represented digitally (data and program instructions). |
| 3 | `CLM-CONSERVATION_BIOLOGY_BASICS-C@1` | 2 | 1 | 2 | OpenStax Biology 2e §47.4 explicitly identifies habitat-restoration effects among its learning objectives and discusses conservation strategies. The statement is supportable at introductory level, but the Evidence Use omits §47.4 and any passage locator. HOLD pending pinpoint and scope review. |
| 4 | `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-A@1` | 2 | 1 | 2 | OpenStax Introduction to Political Science §10.1 and its key terms directly state that presidential regimes select the chief executive separately from the legislature and provide separation of powers. The claim is a simplified typology and should retain the democratic-regime context. Evidence Use lacks §10.1 locator. HOLD. |
| 5 | `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B@1` | 2 | 1 | 2 | OpenStax §10.1 directly states that in parliamentary regimes the head of government is selected by the legislature and is responsible to it; the key terms also state that the chief executive is a member of the legislature. The Claim is broadly supported but should avoid implying every constitutional arrangement is identical. No pinpoint in Evidence Use. HOLD. |
| 6 | `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C@1` | 2 | 1 | 1 | OpenStax §10.1 describes a legislature-selected head of government and a popularly elected head of state; §10.5 states that both president and prime minister wield political power. The Claim's phrase “power is divided” is broadly correct but under-specifies substantial country-to-country variation in the allocation of authority. No pinpoint. HOLD; strengthen boundary. |
| 7 | `CLM-CONSTRUCTION_BASICS-A@1` | 1 | 1 | 1 | NIST Building Science is a relevant institutional source area, but the registered URI is a broad landing page and no specific passage was established here that directly supports the full list of materials, structures, environment and building operation. The additional OSHA construction-hazards source is safety context, not evidence for the definition of building science. HOLD; find a precise NIST passage or a better technical source. |
| 8 | `CLM-CONSTRUCTION_BASICS-C@1` | 2 | 1 | 2 | The Claim gives a meaningful safety boundary: general information is not a substitute for engineering calculations, applicable standards and qualified review for load-bearing/critical structures. The linked NIST Building Science landing page and OSHA Construction Hazards landing page do not pinpoint that exact engineering-design rule. HOLD; source with building-code/structural-engineering authority and define “critical structures.” |
| 9 | `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-A@1` | 1 | 1 | 1 | The listed coordination dimensions (goals, participants, schedule, cost, quality and risks) are plausible components of project management, but the registered WBDG source is broad and the Evidence Use contains no pinpoint to a project-management framework or passage. HOLD pending specific authoritative source and explanatory depth. |
| 10 | `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-C@1` | 2 | 1 | 2 | Project scale, contract, participants and jurisdiction are meaningful dependencies for a construction management plan. The linked WBDG material is too broad in the current Evidence Use to establish the full set of dependencies. HOLD pending a specific project-delivery/contract/jurisdiction passage and scope boundary. |
| 11 | `CLM-CRITICAL_THINKING_BASICS-A@1` | 2 | 1 | 2 | OpenStax College Success §7.4 directly describes determining the problem/situation, analyzing perspectives and experimental results, researching, limiting assumptions and weighing options. ACRL is linked as additional support, but its Evidence Use is generic. Neither Evidence Use identifies exact framework frames/section or OpenStax passage. HOLD pending locators. |
| 12 | `CLM-CRITICAL_THINKING_BASICS-B@1` | 2 | 1 | 2 | OpenStax §7.4 directly distinguishes verifiable facts from opinions and discusses checking sources and recognizing bias. ACRL provides a potentially useful additional framework, but the current EU does not identify the relevant frame or demonstrate independent corroboration. HOLD pending pinpoints and a review of the exact wording “assumptions and biases.” |
| 13 | `CLM-CRITICAL_THINKING_BASICS-C@1` | 2 | 1 | 2 | OpenStax §7.4 explicitly says changing information may require revisiting and adapting prior conclusions. ACRL is an additional linked source but no relevant frame/passage is identified. HOLD pending exact locators; avoid treating the presence of two source records as automatic independent corroboration. |
| 14 | `CLM-CRYPTOGRAPHY_BASICS-C@1` | 2 | 1 | 2 | NIST CSRC defines a cryptographic mechanism as providing services such as confidentiality, integrity and source authentication; NIST also distinguishes modes that provide confidentiality with or without authentication. This supports the Claim's conditional wording (“may provide ... depending on construction”). The canonical Source URI is a broad NIST cryptography landing page, not the specific CSRC glossary entry or technical publication. HOLD pending source identity/URI alignment and pinpoint. |
| 15 | `CLM-DATA_ETHICS_BASICS-A@1` | 2 | 1 | 2 | UNESCO Recommendation on the Ethics of AI, paragraphs 32–34, states that privacy must be respected throughout the AI lifecycle and calls for data-protection frameworks and governance mechanisms. This is direct support. The Evidence Use has no paragraph locator and the Claim could better distinguish privacy from the wider data-protection lifecycle. HOLD pending pinpoint. |
| 16 | `CLM-DEVELOPMENT_ECONOMICS_BASICS-A@1` | 2 | 1 | 2 | McKenzie and Paffhausen, “What Is Considered Development Economics?” (World Bank Economic Review, 2017), identifies growth, poverty and inequality, human capital and institutions as a narrow common core while documenting substantial variation across courses. Supports the listed topics but also shows the field is heterogeneous. The generic Evidence Use omits the article title/section and the heterogeneity qualification. HOLD pending precise locator and scope refinement. |
| 17 | `CLM-DIPLOMACY_BASICS-A@1` | 3 | 1 | 2 | UN Treaty Collection confirms the Vienna Convention on Diplomatic Relations was concluded in Vienna on 18 April 1961, adopted on 14 April 1961 and entered into force on 24 April 1964. This is a precise, directly verifiable historical proposition. The Evidence Use does not cite the UNTC treaty-status fields or convention metadata. HOLD pending exact locator. |
| 18 | `CLM-DIPLOMACY_BASICS-B@1` | 2 | 1 | 2 | The Convention's official UNTC record classifies its subject as diplomatic and consular relations and links the treaty text. This supports the Claim at a broad level, but “framework between states” needs a pinpoint to the Convention's scope/preamble and should not imply it exhausts all diplomatic law. HOLD pending treaty-text locator. |
| 19 | `CLM-DISASTER_RISK_REDUCTION_BASICS-A@1` | 2 | 1 | 1 | UNDRR's official definition says DRR aims to prevent new risk, reduce existing risk and manage residual risk. The Claim includes the first two but omits residual-risk management and narrows the idea to action “before a hazardous event,” which is not the full UNDRR definition. HOLD; revise scope or add the omitted component, then pinpoint the definition. |
| 20 | `CLM-ECOPHYSIOLOGY_BASICS-B@1` | 2 | 1 | 1 | The Claim about ranges of environmental conditions within which physiological functions are maintained is plausible, but the registered Source identity/URI mismatch identified in Lane 1 remains unresolved: the identity says ecophysiology while the URI points to an OpenStax page on animal sensory systems and movement. No passage supporting physiological tolerance ranges was established. HOLD; source identity and exact passage must be corrected through a separately authorized process. |

## Cross-cutting findings

1. **Generic Evidence Use is systemic:** all 20 Evidence Use descriptions lack claim-specific section, paragraph, table, figure or page locators. This makes E=1 under the rubric even where the external passage itself is directly relevant.
2. **Source identity and URI defects:** computing points to a book landing page instead of §§2.1/3.1/5.1; NIST Building Science is a broad landing page; cryptography Source identity is a generic descriptive sentence while its URI is a NIST landing page rather than the specific CSRC definition; ecophysiology's Source identity/URI mismatch remains unresolved.
3. **Critical-thinking extra links:** ACRL EUs are present for Claims A–C but merely say “additional independent support”; no pinpoint or independence analysis is preserved. Do not treat the second link as proof of corroboration until reviewed.
4. **Construction safety:** OSHA's construction-hazards page is relevant safety context but does not, by itself, establish the specific engineering rule about calculations and qualified review of load-bearing structures.
5. **DRR scope omission:** UNDRR includes management of residual risk. The current Claim is narrower than the authoritative definition.
6. **Constitutional-system nuance:** semi-presidential regimes vary considerably in the scope of presidential and prime-ministerial authority; the Claim should not imply a uniform power split.
7. **Automation/risk labels:** queue flags are routing aids only and should not be presented as substantive high-consequence determinations.

## Disposition

- Lane 2: **20/20 first-pass reviews recorded.**
- All 20 Claims remain **HOLD** pending exact Evidence Use pinpoints, source identity/scope follow-up and the specific editorial or specialist actions above.
- No canonical Claim, Evidence Use or Source JSON was changed.
- No specialist, independent, Human View, rights, editorial or publication gate is cleared.
- Next: complete Lanes 3–5, reconcile all 100 IDs against historical worklists, then create the Batch 44 reconciliation package and run exact-head CI once after the full package is committed.
