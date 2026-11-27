# First Edition — Emergency Alerts, Hand Hygiene and Food Security: 33-Record Evidence Audit

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `f1f2f6cde68a1f149a94dc230cb469dc1835c5`  
PR #22: OPEN / DRAFT / NOT MERGED  
Status: bounded source/record audit; no canonical writes; no release inclusion decision.

## 1. Scope and method

Re-fetched 33 records at the exact inspection HEAD across three first-edition candidate slices:

- Emergency Alert Warning: 10 records.
- Emergency Hand Hygiene: 11 records.
- Food Security Basics: 12 records.

Checked exact record identities and blob SHAs, Claim→Evidence Use→Source targets, locators, Context/Scope boundaries, procedural dependencies and current official source content. This package is not a full safety validation, legal opinion, clinical guideline, or release approval. No canonical JSON was changed. All Claims remain HOLD.

## 2. Emergency Alert Warning — 10 records

### 2.1 Exact records

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-ALERTS-ENABLE-RESPOND | 2 | Claim | `11d1ad98d8eb0c90eb5248612e5c9fc3625a1ed3` |
| EU-ALERTS-ENABLE-RESPOND | 2 | Evidence Use | `1a6441cd36d53e887741507f329e47da1276ec18` |
| SRC-RED-CROSS-ALERTS-2026 | 2 | Source | `8c16c6da1a0cf95e03b525f57e43c4234ff1fa93` |
| SRC-PUBLIC-ALERT-GUIDANCE | 1 | Source | `4fc85e5202f5c4c3eb62f83e5e4709c15a0843d6` |
| CLM-IPAWS-ALERT-CONTENT | 1 | Claim | `84fa206cdd0216f2378eb2ced66c6a3ba9edbd18` |
| EU-IPAWS-ALERT-CONTENT | 1 | Evidence Use | `0035bf472a61581b69592ec9159f1a2bba2f4d62` |
| CLM-IPAWS-ALERT-ELEMENTS | 1 | Claim | `a6734418b8b807a3b63781dfce80b65e22b9348e` |
| EU-IPAWS-ALERT-ELEMENTS | 1 | Evidence Use | `444ac87d3a9e78eabe81d3e20dedbc3b3ea86268` |
| CTX-IPAWS-ALERTS | 1 | Context | `42ea1b8bdb815fb6f364e918127d29c4636c48de` |
| SCP-IPAWS-ALERTS | 1 | Scope | `d96cd10da34664b7312667192ad8ab8e21378f22` |

### 2.2 Findings

**Red Cross preparedness Claim v2**

The canonical Claim is explicitly limited to American Red Cross disaster-preparedness guidance in the United States. Its v2 EU now describes the relevant content precisely: identify how local authorities will notify residents, where to obtain information (local radio, television, NOAA Weather Radio), distinguish watches from warnings, and know protective actions.

The current Red Cross page confirms all of these points. This is a good bounded explanatory/preparedness Claim. It does not say to enable mobile-phone alerts, and the source should not be represented as saying that. The geographic and institutional boundary must remain visible.

**FEMA IPAWS message-content Claims**

The current FEMA TIP 44 PDF is the source recorded by SRC-PUBLIC-ALERT-GUIDANCE. The two EUs give exact pinpoints:

- §II.A–B, printed p. 1: effective Wireless Emergency Alerts contain enough information to validate the incident/risk and take protective action.
- §II.B, printed p. 1: trusted sender, event, incident location, protective action, guidance/expiration time or duration, and a URL or phone number for more information.

These locators and the two Claim statements align. However, the FEMA guidance concerns public warning message design and WEA message content. It is not a general guarantee that every alert channel or message contains every element, nor does it replace local instructions.

**Graph boundary**

CTX-IPAWS-ALERTS and SCP-IPAWS-ALERTS target CLM-IPAWS-ALERT-CONTENT@1 only. They must not be silently displayed as applying to CLM-IPAWS-ALERT-ELEMENTS@1. The two Claims have their own EUs but only one explicitly targeted Context/Scope pair.

### 2.3 Rights and publication boundary

This audit checked factual content and locators, not every asset or legal term. Red Cross and FEMA pages/PDFs may contain logos, graphics or other credited elements. No copied prose, graphics, diagrams or logos are proposed for the Encyclopedia. A public release should use independently written factual paraphrases with attribution and links, subject to item-specific rights review.

**Disposition:** the Red Cross Claim and both FEMA Claims have promising source fit and precise locators. All three remain HOLD pending Human View, exact reader rendering, rights/attribution review, and owner/release gates.

## 3. Emergency Hand Hygiene — 11 records

### 3.1 Exact records

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-HANDWASH-20SEC | 1 | Claim | `f5bf1ee347c9fd0befbbc49e2ced1f2ca58d8d75` |
| EU-HANDWASH-20SEC | 1 | Evidence Use | `f0e9443f32c539105d6a9f8ff950a78563b16dea` |
| EU-HANDWASH-20SEC-WHO | 1 | Evidence Use | `9735038b0a5c91c45d3a3cfc099d831d586cb147` |
| SRC-CDC-HAND-HYGIENE-EMERGENCY-2024 | 1 | Source | `1ed6c5b8a82cba02b27039391e0f1bdecf26c5d0` |
| SRC-WHO-HYGIENE-EMERGENCY-2013 | 1 | Source | `db6b724ec0315b478c0374834d02bede5f7e4123` |
| CTX-HANDWASH-EMERGENCY | 1 | Context | `0e06b06c3dde2107159c8d1c30e66f82d2d51829` |
| SCP-HANDWASH-EMERGENCY | 1 | Scope | `c542acea7c1387a25c341c9227ca4d1e9451c3da` |
| PRC-HANDWASH-SOAP-WATER | 1 | Process | `64fd540007645c156d7c941ce47ec758de9c6a74` |
| ACT-HANDWASH-WET-SOAP | 1 | Action | `2905655c328ac7a0ecee0bcb80c56528586125df` |
| ACT-HANDWASH-SCRUB-20SEC | 1 | Action | `843f84f98c4b239afe77cb6a14aacc00ab3ed18b` |
| RES-HANDWASH-CLEANING | 1 | Result | `db8f521f047a9a61eb05c5db4b04d0380e596edb` |

### 3.2 Claim and evidence

The CDC page, dated 2024-08-05 and still available, explicitly recommends washing hands with soap and water for at least 20 seconds during emergencies. It also provides emergency-specific qualifications:

- if authorities or a clinician recommend extra caution, use water that has been boiled or disinfected;
- during a boil-water or do-not-drink advisory, tap water may still be safe for handwashing;
- if clean tap water is unavailable, a temporary handwashing station can be made using a large water jug;
- if soap and water are unavailable, use alcohol-based sanitizer with at least 60% alcohol, while recognizing its limitations.

The canonical Claim is accurately narrow: it states the CDC recommendation of soap and water for at least 20 seconds. It should not be expanded into “always use any available water” or into a claim that sanitizer is equivalent.

EU-HANDWASH-20SEC currently has no formal locator field; its description names the relevant CDC section. EU-HANDWASH-20SEC-WHO is also generic and has no section/page locator. The 2013 WHO PDF is useful corroboration but CDC 2024 is the stronger current emergency-specific source for this Claim.

### 3.3 Process and action review

The local process chain is explicit:

`PRC-HANDWASH-SOAP-WATER@1` → `ACT-HANDWASH-WET-SOAP@1` → `ACT-HANDWASH-SCRUB-20SEC@1`

The actions say to wet hands with clean running water, apply soap, and rub all hand surfaces for at least 20 seconds, including backs of hands, between fingers and under nails. The result record describes removal of dirt, microbes and chemicals, but marks causal attribution as not attributed and status preliminary.

The process/action records are not all fully evidenced by the Claim's 20-second sentence alone. They need their own step-level source mapping, and the result record must not be interpreted as guaranteeing removal of all harmful chemicals or pathogens in every condition. CDC itself cautions that sanitizer may not remove harmful chemicals and that handwashing guidance depends on water safety.

### 3.4 Context, scope and disposition

Context and Scope target CLM-HANDWASH-20SEC@1 only. Scope explicitly excludes specialized healthcare hand-hygiene requirements, which is a useful boundary.

**Disposition:** Claim has direct current CDC support; versioned EU locator correction and step-level process/action evidence are still needed. Keep all records HOLD until source mapping and safety Human View are complete.

## 4. Food Security Basics — 12 records

### 4.1 Exact records

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-FOOD_SECURITY_BASICS-A | 1 | Claim | `96f8b4e63f8abc27452eb998e36b9491ba6d3308` |
| CLM-FOOD_SECURITY_BASICS-B | 1 | Claim | `9e61c713ac545f7dc5345b35170f0a7393d825b9` |
| CLM-FOOD_SECURITY_BASICS-C | 1 | Claim | `976fdb4ca9cb49207d4679cba59bff4f60a36ac5` |
| CLM-FOOD_SECURITY_BASICS-D | 1 | Claim | `45224107bed11976a70511cf978de327e603b60b` |
| EU-FOOD_SECURITY_BASICS-A | 1 | Evidence Use | `39f93d33a4fef420ba52992c4afdf59948de02b3` |
| EU-FOOD_SECURITY_BASICS-B | 1 | Evidence Use | `7853d992f272af1343febda84198cf2230117fcf` |
| EU-FOOD_SECURITY_BASICS-C | 1 | Evidence Use | `7e8e6280ba57c06968681c69ce7f22defac06c4d` |
| EU-FOOD_SECURITY_BASICS-D | 1 | Evidence Use | `be4f1357df82b027eb2465c1b714bf4065786716` |
| SRC-FOOD_SECURITY_BASICS | 1 | Source | `22f161d7a3eb110768825cdb8d2eca430a023bd1` |
| SRC-FOOD_SECURITY_USDA | 1 | Source | `a166708bafe4d8a235b6213d397947f41bd79b86` |
| CTX-FOOD_SECURITY_BASICS | 1 | Context | `629386933c65f47b430a23f9acda684b5b67aa49` |
| SCP-FOOD_SECURITY_BASICS | 1 | Scope | `31f045004f2eba60b07ec42d06b7e9a82698ae0d` |

### 4.2 Claim-level findings

**Claim A — physical/economic access to sufficient, safe and nutritious food**

FAO's handbook §1.4 contains the World Food Summit 1996 definition: physical and economic access to sufficient, safe and nutritious food for all people, at all times, for an active and healthy life. It also identifies availability, stability, access and biological utilization. This is a direct conceptual match.

The current EU-A only names the FAO handbook and has no locator. A future versioned EU should point to §1.4 and identify the 1996 definition and its historical provenance. Do not present the quote as an original FAO definition without attribution to the World Food Summit.

**Claim B — availability, stability and access**

FAO §1.4 explicitly identifies the three classic aspects: availability of staple foods, stability of supplies, and access for all. The statement is directly supported. The EU-B needs the same pinpoint. For broader modern framing, other FAO materials use four or more dimensions, including utilization and, in newer resilience frameworks, sustainability and agency. The Claim should be presented as the three classic aspects in the cited handbook, not as an exhaustive universal taxonomy.

**Claim C — information systems and early warning**

The source itself is a handbook for defining and setting up a Food Security Information and Early Warning System. The next chapters discuss analysing information on availability, collecting and processing information, and dissemination mechanisms. The current EU-C does not identify the relevant sections. The claim is supported at a high level, but a locator should identify the system-design/monitoring passages and not imply that every information system automatically produces sound decisions.

**Claim D — household food security**

USDA ERS's current Measurement page, updated 2026-03-30, defines household food security as access by all members at all times to enough food for an active, healthy life. It adds ready availability of nutritionally adequate and safe food and assured ability to acquire acceptable foods in socially acceptable ways. This is a direct match to the canonical Claim. EU-D needs a precise “What Is Food Security?” locator. The definition is U.S. household measurement context; do not universalize its survey method or infer current household status from the definition alone.

### 4.3 Source rights and scope

FAO and USDA pages are public institutional sources, but this audit does not establish a blanket reproduction licence for every document, figure, data set or third-party asset. Use independently written paraphrases, exact attribution and stable links; verify specific terms before copying any tables, graphics or extended text.

CTX and SCP target Claim A only. They do not automatically govern B, C or D. Claim D uses a separate USDA Source/EU path and should retain its U.S. household measurement context.

**Disposition:** all four Claims have credible source fit; all four EUs need exact locators. Claim B's “three classic aspects” qualification should be retained. All remain HOLD pending rights review, reader review and approval.

## 5. Consolidated remediation decisions

1. **Alerts:** keep Red Cross Claim v2 and FEMA Claims as separate source tracks. Their locators are already exact; perform Human View and rights/attribution review. Do not merge Red Cross preparedness advice with FEMA message-design guidance.
2. **Hand hygiene:** add exact CDC section locator and WHO page locator in versioned EUs; create step-level evidence mapping for process/actions; bound the Result so it does not promise universal removal of contaminants.
3. **Food security:** version EU-A/B/C to FAO §1.4 and relevant information-system chapters; version EU-D to USDA ERS “What Is Food Security?”; preserve the three-classic-aspects qualification and U.S. boundary for Claim D.
4. Do not change canonical records or promote Claims without explicit bounded authorization.
5. Keep safety claims separate from operational procedures. Alert comprehension is not evacuation instruction; handwashing is not a substitute for local water-safety directions.
6. Complete independent Human View, reader rendering, source rights and project owner gates before selection.

**Final disposition: 33 records inspected; 8 Claims remain HOLD; zero canonical writes; zero INCLUDE decisions.**
