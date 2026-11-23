# M13 — strict passage/locator review package 02

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input queue: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`  
Scope: 6 exact triples from the strict 47-item generic-EU passage/locator gap queue.  
State: **desk-level passage/source-fit and risk-routing review only; no canonical edits, no D/E/B changes, no specialist sign-off, no release clearance.**

## 1. Exact records inspected

For each Claim below, the exact v1 Claim, linked v1 Evidence Use and linked v1 Source records were retrieved from the active branch. All six Claim → EU → Source links resolve and the endpoint IDs match. All six EUs use generic descriptions and contain no reproducible Claim-specific passage locator.

- `CLM-DIGITAL_COMMUNICATIONS_BASICS-A@1` → `EU-DIGITAL_COMMUNICATIONS_BASICS-A@1` → `SRC-DIGITAL_COMMUNICATIONS_BASICS@1`
- `CLM-DIGITAL_COMMUNICATIONS_BASICS-B@1` → `EU-DIGITAL_COMMUNICATIONS_BASICS-B@1` → `SRC-DIGITAL_COMMUNICATIONS_BASICS@1`
- `CLM-DIGITAL_COMMUNICATIONS_BASICS-C@1` → `EU-DIGITAL_COMMUNICATIONS_BASICS-C@1` → `SRC-DIGITAL_COMMUNICATIONS_BASICS@1`
- `CLM-ELECTRONICS_BASICS-B@1` → `EU-ELECTRONICS_BASICS-B@1` → `SRC-ELECTRONICS_BASICS@1`
- `CLM-ELECTRONICS_BASICS-C@1` → `EU-ELECTRONICS_BASICS-C@1` → `SRC-ELECTRONICS_BASICS@1`
- `CLM-CALIBRATION_BASICS-A@1` → `EU-CALIBRATION_BASICS-A@1` → `SRC-CALIBRATION_BASICS@1`

## 2. Claim-by-Claim findings

### 2.1 Digital communications — standards-based transmission and processing

**Claim:** `CLM-DIGITAL_COMMUNICATIONS_BASICS-A@1`  
**Claim text:** “Цифровые коммуникационные системы используют стандартизованные методы передачи и обработки информации по телекоммуникационным сетям.”

**Registered Source:** ITU-T Recommendations catalogue: https://www.itu.int/rec/T-REC/en/  
**Supplementary ITU-T overview:** https://www.itu.int/en/ITU-T/publications/Pages/recs.aspx

**Passage result:** Partial / broad conceptual fit. ITU-T describes its Recommendations as standards defining how telecommunication networks operate and interwork. The catalogue groups recommendations across transmission systems, digital systems and networks, multimedia, data networks, security and related topics. The registered catalogue does not establish that all digital communication systems necessarily use a particular standard or method.

**Risk route:** MODERATE. The Claim is descriptive, but readers may infer universal standardization or interoperability. Keep the wording bounded to standards-based systems and do not imply that standardization alone guarantees compatibility or secure operation.

**Finding:** Source identity is relevant, but the EU needs a direct locator to the ITU-T description of Recommendations and relevant series. Avoid changing the Claim into an absolute statement about all systems.

### 2.2 Digital communications — scope of ITU-T Recommendations

**Claim:** `CLM-DIGITAL_COMMUNICATIONS_BASICS-B@1`  
**Claim text:** “Рекомендации ITU-T охватывают, в частности, системы передачи, цифровые системы и сети, мультимедийные системы и сети передачи данных.”

**Registered Source:** ITU-T Recommendations catalogue: https://www.itu.int/rec/T-REC/en/

**Passage result:** Direct support. The ITU-T catalogue explicitly lists:
- G-series: transmission systems and media, digital systems and networks;
- H-series: audiovisual and multimedia systems;
- X-series: data networks, open system communications and security;
- Y-series: global information infrastructure, Internet protocol aspects and next-generation networks.

**Risk route:** MODERATE. This is a descriptive statement about the scope of an international standards catalogue. The main risk is overgeneralizing categories or confusing ITU-T recommendations with all telecommunications standards or with mandatory law.

**Finding:** Direct support is present. Add a stable locator to the catalogue's series list and retain the explicit ITU-T boundary. ITU-T Recommendations are not automatically mandatory in every jurisdiction; their adoption status must not be misrepresented.

### 2.3 Digital communications — compatibility conditions

**Claim:** `CLM-DIGITAL_COMMUNICATIONS_BASICS-C@1`  
**Claim text:** “Совместимость коммуникационных систем зависит от применяемых стандартов, архитектуры сети, интерфейсов и условий передачи.”

**Registered Source:** ITU-T Recommendations catalogue: https://www.itu.int/rec/T-REC/en/

**Passage result:** Partial. ITU-T states that its Recommendations define how networks operate and interwork and its catalogue covers network architecture, digital transmission and data networks. That supports the standards/interworking component. The current broad catalogue does not directly demonstrate the full four-part dependency stated in the Claim, especially the role of physical transmission conditions.

**Risk route:** MODERATE. The Claim is a general engineering principle, not an implementation instruction. Do not use it as a compatibility test or assurance that two systems will interoperate.

**Finding:** Keep HOLD pending direct passages for interfaces and transmission conditions, or narrow the Claim to the aspect actually supported by the ITU-T source. A catalogue-level source is not sufficient proof of a general engineering rule.

### 2.4 Electronics — semiconductors and integrated circuits

**Claim:** `CLM-ELECTRONICS_BASICS-B@1`  
**Claim text:** “Полупроводники являются базовыми материалами для многих современных электронных компонентов и интегральных схем.”

**Registered Source:** NIST Electronics: https://www.nist.gov/electronics  
**Direct supplementary NIST page:** NIST, *Semiconductors*: https://www.nist.gov/semiconductors

**Passage result:** Direct support from the supplementary NIST Semiconductors page. NIST states that semiconductors such as silicon are the base for most electronics and enable construction of complex integrated circuits. The registered NIST Electronics landing page lists semiconductors as one of its topics but is not itself the clearest pinpoint for this Claim.

**Risk route:** LOW DIRECT CONSEQUENCE for this exact foundational statement. The semiconductor supply chain and specific component design can be consequential, but the Claim does not prescribe fabrication, selection or repair.

**Finding:** The statement is supported at the general level. The registered Source should point to the direct NIST Semiconductors page through a bounded, versioned Source/EU proposal; do not silently replace the canonical URI. Preserve the qualifier “many” rather than implying every electronic component is semiconductor-based.

### 2.5 Electronics — component characteristics

**Claim:** `CLM-ELECTRONICS_BASICS-C@1`  
**Claim text:** “Характеристики электронных компонентов зависят от конструкции, материалов, условий эксплуатации и методов измерения.”

**Registered Source:** NIST Electronics: https://www.nist.gov/electronics

**Passage result:** Partial / not established at the full stated scope. The NIST Electronics page describes NIST's work on standards, instruments and calibrations for electronic components and power systems; NIST semiconductor materials pages describe material properties, measurement capabilities and device performance. These pages are relevant, but the current registered page does not directly establish the complete four-factor generalization for electronic components as a class.

**Risk route:** MODERATE. The statement may influence component characterization or selection. It must not be used to infer a component's safe operating limits or reliability without the specific datasheet, conditions, measurement method and applicable standards.

**Finding:** Keep HOLD. Either register distinct primary references for the relevant factors and bound the Claim to the covered component classes, or reclassify it as a high-level editorial summary with an explicit scope note. Do not treat a broad NIST topic page as direct evidence.

### 2.6 Calibration — relation between indications and quantity values

**Claim:** `CLM-CALIBRATION_BASICS-A@1`  
**Claim text:** “Калибровка устанавливает связь между показаниями измерительного средства и соответствующими значениями измеряемой величины.”

**Registered Source:** NIST Calibration Services: https://www.nist.gov/calibrations  
**Direct normative/metrology definition:** JCGM VIM 2.39, *Calibration*: https://jcgm.bipm.org/vim/en/2.39.html

**Passage result:** Direct support from JCGM VIM 2.39, not from a pinpoint in the registered NIST Source. VIM defines calibration under specified conditions as a first step relating quantity values with uncertainties provided by measurement standards to corresponding indications with associated uncertainties, and a second step using this information to establish a relation for obtaining a measurement result from an indication.

**Scope finding:** The Claim is a simplified description of the first part of the definition. It omits the specified conditions, measurement standards, uncertainty, and second operational step. That may be acceptable as an introductory summary only if the linked Scope/context makes the simplification explicit. Calibration must not be confused with adjustment or verification.

**Risk route:** ELEVATED. Calibration underpins measurement reliability in regulated, clinical, industrial and safety-critical decisions. The statement is conceptual, but downstream use requires metrology expertise and fit-for-purpose uncertainty evaluation.

**Finding:** Keep HOLD pending a bounded Source/EU proposal using the exact VIM 2.39 locator and a decision whether to expand the Claim or explicitly mark it as a simplified first-step description. The existing NIST Calibration Services Source is relevant institutionally but does not supply the direct definition pinpoint. Preserve the distinction between calibration, adjustment and verification.

## 3. Consolidated disposition

| Claim | Passage support | Risk route | Canonical pinpoint present | Disposition |
|---|---|---|---|---|
| Digital communications A | Partial; ITU-T network standards/interworking concept | Moderate | No | HOLD |
| Digital communications B | Direct; ITU-T G/H/X/Y series list | Moderate | No | HOLD |
| Digital communications C | Partial; standards/interworking only, remaining factors not fully pinned | Moderate | No | HOLD |
| Electronics B | Direct supplementary NIST Semiconductors page; registered NIST landing page broad | Low direct consequence | No | HOLD |
| Electronics C | Partial; full four-factor statement not demonstrated | Moderate | No | HOLD |
| Calibration A | Direct JCGM VIM 2.39 definition; current NIST Source lacks pinpoint | Elevated | No | HOLD |

## 4. Exact change and completion boundary

- Claims reviewed: 6.
- Evidence Use records reviewed: 6.
- Source records reviewed: 3.
- Claim/EU/Source identity and version links: 6/6 resolve and match.
- EUs with generic/non-pinpoint descriptions: 6/6.
- Direct or partial support found from official/standards sources: 6.
- Claims requiring source identity or locator proposal: 6.
- Canonical Claim/Evidence Use/Source records changed: 0.
- Canonical passage locators added: 0.
- D/E/B scores assigned or overwritten: 0.
- Risk metadata assigned or changed: 0.
- Independent specialist reviews completed: 0.
- Human View / release approval: 0.

## 5. Required next actions

1. Prepare an ITU-T Source/EU locator proposal for A/B/C. B can use the exact series catalogue; A needs the ITU-T explanation of Recommendations; C needs separate evidence for interfaces and transmission conditions or narrower wording.
2. Prepare a bounded NIST Source/EU locator proposal for Electronics B using the NIST Semiconductors page. For C, obtain more specific technical references or narrow the claim.
3. Prepare a metrology correction proposal for Calibration A using JCGM VIM 2.39, preserving uncertainty and the distinction between calibration, adjustment and verification.
4. Keep all six Claims HOLD until exact source passages, rights/attribution, versioned authorization, regression tests and appropriate specialist review are complete.
5. Run exact-head Reference Tests, Release Conformance Gate and Offline Edition after any later canonical correction.

This package is a desk review and routing artifact. It is not an independent technical certification, a full risk assessment, or M13 closure.
