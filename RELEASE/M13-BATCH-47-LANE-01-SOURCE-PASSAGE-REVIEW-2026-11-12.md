# M13 Batch 47 — Lane 1 source-passage and D/E/B review

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Frozen selection revision: `677dff36c04e8593b74b0b4c6b6323cdadd12fa7`  
Queue workflow: `43189183999`; artifact: `13929592813`  
Scope: Lane 1, 20 Claims. Append-only audit documentation; no canonical Claim, Evidence Use, or Source records are modified.

## Method and limits

- Reviewed all 20 Claim statements and Evidence Use descriptions/source identities in the frozen Batch 47 evidence packets.
- Checked public source pages where retrievable. A source identity, URI, or topic landing page is not treated as claim-specific passage support.
- No Lane 1 entry contains a sufficiently precise claim-specific section/page/table/figure locator in Evidence Use. E is therefore 1 throughout this first pass.
- Exact Claim → Evidence Use → Source JSON linkage remains a human verification task; this report does not certify those record edges.
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
| 1 | `CLM-MEASUREMENT_SCIENCE_BASICS-B@1` | 3 | 1 | 3 | BIPM VIM 2.9 defines a measurement result as quantity values attributed to a measurand together with relevant information, including uncertainty. Strong conceptual fit; Evidence Use does not identify VIM 2.9 or the relevant note. HOLD pending exact locator and distinction between measurement value and full result. |
| 2 | `CLM-MINERALOGY_BASICS-A@1` | 1 | 1 | 2 | USGS defines a mineral as a naturally occurring inorganic element or compound with orderly internal structure and characteristic composition/physical properties. This Claim says mineralogy studies elements and compounds, which is broader and potentially inaccurate; mineralogy studies minerals. HOLD for substantive correction proposal and exact definition locator. |
| 3 | `CLM-MINERALOGY_BASICS-B@1` | 2 | 1 | 2 | USGS Minerals 101 supports composition, internal structure, crystal form, and physical properties, but the registered URI is a general thesaurus rather than the cited definition page. HOLD; resolve source identity/URI and add a pinpoint. |
| 4 | `CLM_PUBLIC_WORKS_BASICS_A@1` | 2 | 1 | 2 | USACE Civil Works is a relevant U.S. federal program source, but its landing page does not establish a technology-neutral definition of public works as infrastructure and related services. HOLD pending a clear definition source and jurisdictional boundary. |
| 5 | `CLM_PUBLIC_WORKS_BASICS_C@1` | 2 | 1 | 2 | USACE Civil Works may cover project planning, asset condition, environment, costs, and risks, but the registered landing page does not pinpoint the complete planning checklist or long-term operation element. HOLD pending source passage and scope review. |
| 6 | `CLM_RAILWAY_SYSTEMS_BASICS_A@1` | 3 | 1 | 3 | FRA Railroad Safety explicitly lists track, operating practices, motive power/equipment, hazardous materials, grade crossings, and signal/train control as technical safety disciplines. Direct support; no exact page/section locator is retained. HOLD pending pinpoint and U.S. scope. |
| 7 | `CLM_RAILWAY_SYSTEMS_BASICS_B@1` | 3 | 1 | 3 | FRA regulates safety and inspection across signal/train-control and other disciplines, but the full lifecycle list (design, installation, maintenance, inspection, testing) needs specific regulatory references such as applicable 49 CFR provisions. HOLD pending pinpoint and jurisdictional boundary. |
| 8 | `CLM_RAILWAY_SYSTEMS_BASICS_C@1` | 3 | 1 | 3 | FRA safety material includes accident/fatality investigations, reporting, safety data, and grade-crossing oversight. The full operational-data list needs exact FRA database/reporting locators. HOLD pending pinpoint. |
| 9 | `CLM-REQUIREMENTS_ENGINEERING_BASICS-A@1` | 3 | 1 | 3 | NASA Appendix C says requirements should state what is needed, not how to provide it, supporting the need-versus-implementation distinction. Evidence Use lacks the exact Appendix C.2 locator. HOLD pending pinpoint. |
| 10 | `CLM-REQUIREMENTS_ENGINEERING_BASICS-B@1` | 3 | 1 | 3 | NASA Appendix C requires consistent terminology, tolerances, and verifiable/testable requirements. The claim's quantitative boundaries and verification criteria are well aligned, but no C.2/C.4 locator is recorded. HOLD pending pinpoint. |
| 11 | `CLM-REQUIREMENTS_ENGINEERING_BASICS-C@1` | 3 | 1 | 3 | NASA Appendix C.1 explicitly distinguishes shall (requirement), will (fact/purpose), and should (goal). Strong direct fit; Evidence Use lacks the C.1 locator. HOLD pending pinpoint and preservation of NASA-specific systems-engineering context. |
| 12 | `CLM-SCIENTIFIC_COMMUNICATION_BASICS-C@1` | 2 | 1 | 2 | National Academies Communicating Science Effectively addresses complexity, audience, and controversy, but the claim's evidence-based selection of form/approach is not pinpointed by the registered chapter 4 URI. HOLD pending precise passage and scope review. |
| 13 | `CLM-SCIENTIFIC_METHOD_BASICS-B@1` | 2 | 1 | 2 | The registered National Academies chapter is broad science-education material; the generic source identity sentence does not establish a testable hypothesis definition. HOLD pending exact definition locator and clarification whether hypothesis is an explanatory proposition or assumption. |
| 14 | `CLM-SEISMOLOGY_BASICS-A@1` | 3 | 1 | 2 | USGS Earthquake Hazards is relevant to earthquakes and seismic waves, but the broad program page is not a precise definition of seismology. HOLD pending a USGS glossary or introductory seismology locator. |
| 15 | `CLM_SEMICONDUCTOR_BASICS_B@1` | 2 | 1 | 2 | NIST Semiconductors is a relevant topic page, but the registered page does not pinpoint switching, amplification, sensing, and computation as functions of semiconductor devices. HOLD pending a device-level source and locator. |
| 16 | `CLM_SEMICONDUCTOR_BASICS_C@1` | 2 | 1 | 2 | NIST Semiconductors is too broad to establish the full integrated-circuit composition/function statement. HOLD pending an authoritative semiconductor/IC source and exact passage. |
| 17 | `CLM-SENSOR_SYSTEMS_BASICS-B@1` | 1 | 1 | 1 | NIST IoT Cybersecurity does not support the general measurement range/accuracy/conditions proposition; it is a source-scope mismatch. HOLD; replace with metrology sources such as VIM/GUM and add exact locators. |
| 18 | `CLM-SOIL_BASICS-C@1` | 3 | 1 | 2 | USDA NRCS soils material is relevant to spatial and depth variability, but the registered landing page lacks a soil-profile/landscape locator. HOLD pending specific NRCS soil-survey passage. |
| 19 | `CLM_SOIL_SCIENCE_BASICS_B@1` | 2 | 1 | 2 | FAO/USDA soil materials distinguish inherent properties from dynamic properties affected by management and conditions, but the registered FAO Soil Properties page lacks the exact definition locator. HOLD pending pinpoint and clear separation of soil quality from soil properties. |
| 20 | `CLM_SOIL_SCIENCE_BASICS_C@1` | 3 | 1 | 2 | FAO describes soil contributions to productivity, water regulation, nutrient cycles, biodiversity, and ecosystem services. The claim's complete function list needs a specific FAO section locator. HOLD pending pinpoint. |

## Lane findings

- First-pass review: **20/20 recorded**.
- Disposition: **20 HOLD**.
- Claim-specific locators explicitly preserved in Evidence Use: **0/20**.
- Canonical JSON changes: **0**.
- Specialist, independent, Human View, rights, editorial, and publication gates cleared: **0**.
