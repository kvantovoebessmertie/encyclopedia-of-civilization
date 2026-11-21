# M13 Batch 44 — Lane 1 source-passage and D/E/B review

Date: 2026-11-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Selection revision: `e55dbfcefb4811d9aa4819032109591c22c3401e`  
Queue artifact: workflow run `43077545154`, artifact `13883590011`  
Scope: first frozen lane, 20 Claims. This report does not modify canonical Claim, Evidence Use, or Source records.

## Method and limits

- Read the exact Claim, Evidence Use and Source JSON records for all 20 candidates from the selection revision.
- Checked available public source passages/pages where retrievable. A source identity or URI alone is not treated as passage support.
- The current Evidence Use descriptions are generic and do not preserve claim-specific section, paragraph, table, figure, or page locators. Under the M13 rubric this limits E to 1 even where the public source page contains relevant material.
- No source text was fetched by the queue generator; source checking in this report is a separate human review step.
- Scores below are provisional first-pass desk assessments. They are not specialist certification, independent review, or publication clearance. Where source passage could not be retrieved or the locator is broad/misaligned, retain HOLD.

## Batch accounting

- Frozen lane capacity: 20.
- Claims reviewed: 20/20.
- Exact Claim → Evidence Use references: 20/20 resolve in the checked records.
- Evidence Use → Source references: 20/20 resolve in the checked records.
- Claim-specific Evidence Use pinpoint: 0/20 present.
- Canonical records modified: 0.
- D/E/B generated automatically: no; all scores below are reviewer assessments.
- High-consequence flags and structural flags remain routing signals only. The lane includes clear false-positive/overbroad risk routing (for example, ecology and kinematics Claims assigned legal/financial risk; ecophysiology Claims assigned communications-continuity risk). These flags must not be represented as actual risk findings.

## Scored review

| # | Claim | D | E | B | Passage/source finding and disposition |
|---:|---|---:|---:|---:|---|
| 1 | `CLM-ECOLOGY_BASICS-A@1` | 0 | 1 | 1 | The statement describes what this slice supposedly introduces rather than making a substantive ecology proposition. OpenStax 46.1 defines ecosystems and their components, but the claim does not state those concepts. Recast as a substantive proposition or classify as editorial metadata; HOLD. |
| 2 | `CLM-ECOLOGY_BASICS-B@1` | 1 | 1 | 2 | Source/context/applicability is a generic epistemic caution, not a claim-specific ecology finding. OpenStax 46.1 provides ecological context but does not establish this general evidence-method rule. HOLD; move to a cross-cutting methodology treatment or supply an appropriate methodology source. |
| 3 | `CLM-ECOLOGY_BASICS-C@1` | 1 | 1 | 2 | The specialist-review caveat is prudent but generic and not established by the linked ecology introduction. It needs a clear trigger/boundary and a source or an explicit editorial-policy classification. HOLD. |
| 4 | `CLM-ECOPHYSIOLOGY_BASICS-A@1` | 1 | 1 | 1 | Claim says organismal physiological processes depend on external conditions. The Source identity describes ecological physiology, but its URI points to an OpenStax Biology page titled “Animal Sensory Systems and Movement”; source identity/topic alignment needs correction or a precise passage showing support. HOLD; do not infer from the label. |
| 5 | `CLM-ECOPHYSIOLOGY_BASICS-C@1` | 1 | 1 | 2 | “Comparable measurement conditions” is a reasonable methodological boundary, but the linked animal sensory/movement page and generic Evidence Use do not identify a passage supporting this comparison rule. HOLD; needs a measurement-method source/pinpoint. |
| 6 | `CLM-ENVIRONMENTAL_POLICY_BASICS-C@1` | 2 | 1 | 3 | Claim appropriately distinguishes general principles from jurisdiction-, time- and subject-specific legal requirements. UNEP’s environmental law/governance material confirms the broad legal/governance domain, but the Evidence Use does not identify a passage establishing every stated dependency. HOLD pending claim-specific legal-source pinpoint and jurisdictional review. |
| 7 | `CLM-MOTION_BASICS-A@1` | 2 | 1 | 2 | OpenStax Physics 2.1 directly explains that position/motion is described relative to a selected reference frame. The canonical Evidence Use only names the chapter generally and omits the section locator. HOLD pending exact locator. |
| 8 | `CLM-MOTION_BASICS-C@1` | 1 | 1 | 1 | “Acceleration describes change in velocity over time” is a basic definition. OpenStax Physics chapter 2 includes acceleration and velocity-time material, but the Evidence Use does not pinpoint the definition. HOLD pending section/definition locator. |
| 9 | `CLM-POWER_ELECTRONICS_BASICS_B@1` | 2 | 1 | 1 | DOE’s power-electronics page directly describes PV inverters converting DC to AC and setting current/voltage; it also discusses frequency ride-through. The Claim generalizes to converters and several electrical quantities, while the Evidence Use does not identify the supporting passage or define the converter scope. HOLD; narrow or substantiate the broader wording. |
| 10 | `CLM_PUBLIC_TRANSPORT_BASICS_A@1` | 1 | 1 | 1 | The Claim defines shared mobility services. The registered World Bank Urban Transport URI currently redirects to a broad Development Topics landing page rather than the named urban-transport resource; source identity/URI and passage support need revalidation. HOLD. |
| 11 | `CLM_PUBLIC_TRANSPORT_BASICS_B@1` | 1 | 1 | 1 | Buses, rail and organized shared networks are plausible examples, but the linked World Bank URI currently redirects to a broad landing page. No claim-specific passage is recorded. HOLD; replace/repair source locator and verify examples. |
| 12 | `CLM_PUBLIC_TRANSPORT_BASICS_C@1` | 2 | 1 | 2 | The planning factors are meaningful, but the single broad World Bank source reference and generic Evidence Use do not pinpoint support for demand, accessibility, capacity, operating conditions and resources as a set. HOLD; split or source each material factor. |
| 13 | `CLM_PUBLIC_WORKS_BASICS_B@1` | 1 | 1 | 1 | USACE Civil Works material lists navigation, flood-risk management, hydropower, irrigation and municipal water supply, supporting some examples within a U.S. federal agency remit. It does not by itself establish the general worldwide scope implied by “public works,” and utilities are not pinned. HOLD; bound jurisdiction and identify a suitable general source. |
| 14 | `CLM_SEMICONDUCTOR_BASICS_A@1` | 2 | 1 | 1 | NIST explicitly describes semiconductors as materials with tunable electrical conductivity and as a basis for most electronics. This is direct source-level support, but the Evidence Use lacks the exact locator and the Claim gives little explanation of how conductivity is controlled. HOLD pending locator and depth review. |
| 15 | `CLM_SOIL_SCIENCE_BASICS_A@1` | 1 | 1 | 1 | FAO explicitly lists physical, chemical and biological soil-quality properties and notes variation with management inputs. The Claim is a basic assertion; the Evidence Use is generic and lacks the exact page locator. HOLD pending locator and additional explanatory depth. |
| 16 | `CLM_TOXICOLOGY_BASICS_A@1` | 1 | 1 | 1 | The definition is introductory and very broad. The ATSDR Source record points to a general toxicology resource, but no exact passage was preserved in the Evidence Use or verified in this pass. HOLD pending exact source passage and definition scope. |
| 17 | `CLM_TOXICOLOGY_BASICS_C@1` | 1 | 1 | 1 | The hazard/risk distinction is important but not explained in the Claim. The broad ATSDR source identity alone does not demonstrate the distinction; the Evidence Use has no pinpoint. HOLD pending a specific authoritative passage and a clear distinction. |
| 18 | `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A@1` | 2 | 1 | 2 | The Claim describes comparative study and rejects a single universal trajectory. The linked UNESCO item is a specific multi-volume history of Central Asia, not a method source for comparative civilizations or the stated historiographical boundary. HOLD; source is materially misaligned and needs a methodology source. |
| 19 | `CLM-COMPARATIVE_LAW_BASICS-A@1` | 1 | 1 | 1 | Cornell Wex describes legal systems and jurisdictional variation, which is relevant background, but does not by itself establish the full method/scope of comparative law. Generic Evidence Use lacks a pinpoint. HOLD pending a comparative-law methodology source and locator. |
| 20 | `CLM-COMPUTING_BASICS-A@1` | 1 | 1 | 1 | OpenStax section 5.1 describes hardware, software, data and instruction execution, relevant to the Claim. The registered Source URI is a book landing page, while the relevant passage is in section 5.1; the Evidence Use does not identify it. HOLD pending exact section locator and review of the “by defined rules” wording. |

## Structural and editorial findings

1. **Generic Evidence Use is systematic in this lane.** All 20 Evidence Use records identify a source and Claim link but none provides a claim-specific passage locator. This is an evidence-traceability weakness; it does not mean every source is substantively irrelevant.
2. **Source identity/URI mismatch or drift:** ecophysiology source identity does not clearly match its OpenStax animal sensory/movement URI; public-transport URI redirects to a generic World Bank topics page; comparative-civilizations source is a specific Central Asia history collection rather than a comparative-method source; computing points to a book landing page rather than the relevant section.
3. **Overbroad or likely false-positive risk routing:** ecology and motion Claims are tagged `legal_financial`; ecophysiology Claims are tagged `communications_information_continuity`. The routing flags require risk-frame calibration and must not be read as substantive high-consequence determinations.
4. **Potential editorial taxonomy issue:** ecology Claims B/C and ecophysiology Claim C are cross-cutting evidence/method cautions presented as domain Claims. Their classification and placement should be reviewed before any canonical correction is authorized.
5. **Identifier aliases:** several filenames and internal record IDs differ only by separator conventions. Preserve stored IDs; treat this as a comparison/reconciliation task, not permission to rewrite identifiers.

## Disposition

- Lane 1: **20/20 first-pass reviews recorded.**
- All 20 remain **HOLD** for source pinpoint, source identity/scope and/or editorial-depth follow-up as specified above.
- No canonical JSON record was changed.
- No publication, specialist, Human View, rights, or independent-review gate is cleared.
- Next: continue Lane 2 (20 Claims), preserve the same source-passage and linkage protocol, then reconcile all five lanes before the batch-level audit package and exact-head CI.
