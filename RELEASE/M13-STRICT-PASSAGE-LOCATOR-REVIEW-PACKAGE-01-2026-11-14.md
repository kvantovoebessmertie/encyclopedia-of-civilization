# M13 — strict passage/locator review package 01

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input queue: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`  
Queue baseline: 47 Claim/Evidence Use/Source triples  
Scope: 7 exact triples selected from the safety / emergency / water / energy end of the 47-item queue.  
State: **desk-level source-passage and risk-routing review only; no canonical edits, no D/E/B changes, no specialist sign-off, no release clearance.**

## 1. Selection and boundary

The seven reviewed Claims are exact entries in the 47-item strict passage/locator gap queue:
- `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1`
- `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1`
- `CLM-SHELTER_BASICS-A@1`
- `CLM-SHELTER_BASICS-B@1`
- `CLM-SHELTER_BASICS-C@1`
- `CLM-WATER_SECURITY-B@1`
- `CLM-HYDROPOWER_BASICS-A@1`

The exact v1 Claim, linked v1 Evidence Use and linked v1 Source records were retrieved from the branch. Claim/EU/Source reference identities resolve and match. All seven EUs have broad descriptions rather than reproducible Claim-specific locators. This package does not treat a successful URL or institution match as a passage-level locator correction.

## 2. Claim-by-Claim findings

### 2.1 Emergency management — roles across sectors

**Claim:** `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1`  
**Chain:** `EU-EMERGENCY_MANAGEMENT_BASICS-B@1` → `SRC-EMERGENCY_MANAGEMENT_BASICS@1`  
**Claim text:** “Эффективное управление ЧС требует распределения ролей между государственными, частными и общественными участниками.”

**Source inspected:** FEMA, *Fundamentals of Emergency Management*, IS-230.E, course overview:  
https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-230.e&lang=en

**Passage result:** Partial / conceptually aligned. The FEMA overview says the course covers emergency-management principles and authorities, how different partners contribute in a community, and the roles of each partner. It does not, in the overview itself, enumerate the exact government / private / community triad stated in the Claim. FEMA's *Preparedness: The Whole Community* handout separately states that private-sector and nongovernmental/voluntary organizations are key partners and describes their roles:  
https://training.fema.gov/emiweb/is/is909/preparedness_facilitatorguide.pdf

**Risk route:** MODERATE. The statement is organizational and descriptive, but may influence emergency-planning governance. Require emergency-management / public-administration review before turning it into operational role allocation. The institutional model is U.S.-specific and should not be generalized as a universal governance structure.

**Finding:** Existing registered Source is relevant but the Evidence Use is generic and the exact triad is not directly demonstrated by its course-overview page. A separate, versioned source/EU proposal may be needed for the FEMA Whole Community handout. Do not silently add or substitute it.

### 2.2 Emergency management — jurisdictional and event-specific authority

**Claim:** `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1`  
**Chain:** `EU-EMERGENCY_MANAGEMENT_BASICS-C@1` → `SRC-EMERGENCY_MANAGEMENT_BASICS@1`  
**Claim text:** “Конкретные полномочия, планы и процедуры определяются юрисдикцией, типом события и действующими системами управления.”

**Source inspected:** FEMA IS-230.E, same course overview above; additionally FEMA, *Comprehensive Preparedness Guide 101* (official planning guidance):  
https://www.ready.gov/sites/default/files/2019-06/comprehensive_preparedness_guide_developing_and_maintaining_emergency_operations_plans.pdf

**Passage result:** Partial. FEMA IS-230.E confirms that authorities and emergency-management roles are foundational topics. CPG 101 requires plans to identify who has authority to initiate protective actions and to coordinate with local/community and State plans. This supports jurisdictional and plan-specific variation in the U.S. planning context. The current Source is a broad course landing page and does not itself provide a pinpoint for all three elements in the Claim.

**Risk route:** MODERATE. The Claim is a useful boundary statement that discourages universalizing emergency powers. It must not be used as a substitute for checking current local law, agency authority or event-specific plans.

**Finding:** Keep the jurisdictional boundary. Add exact, versioned passage locators only after source registration and review. The present EU is not a sufficient pinpoint.

### 2.3 Shelter — basic need under environmental exposure and emergencies

**Claim:** `CLM-SHELTER_BASICS-A@1`  
**Chain:** `EU-SHELTER_BASICS-A@1` → `SRC-SHELTER_BASICS@1`  
**Claim text:** “Укрытие является базовой потребностью при воздействии внешней среды и чрезвычайных ситуациях.”

**Source registered:** Ready.gov — Emergency Preparedness, root page: https://www.ready.gov/

**Passage result:** Not established by the registered root-page locator. The Ready.gov home page is a portal, not a stable Claim-specific passage. FEMA shelter-in-place guidance confirms that sheltering may be the safer protective action for some hazards and conditions, while its hazard-specific instructions differ:  
https://www.fema.gov/sites/default/files/documents/fema_shelter-in-place_guidance.pdf

**Risk route:** MODERATE. This is a foundational human-needs statement, not a directive for selecting a particular shelter. Avoid turning it into an absolute statement that staying indoors is always safer.

**Finding:** Claim is broadly plausible, but the current registered Source/EU does not provide a reproducible pinpoint. A direct human-needs / humanitarian shelter standard would be preferable for the broad Claim; FEMA's hazard-specific shelter guide is contextual corroboration, not a universal source for the general proposition.

### 2.4 Shelter — weather, water, ventilation and location safety

**Claim:** `CLM-SHELTER_BASICS-B@1`  
**Chain:** `EU-SHELTER_BASICS-B@1` → `SRC-SHELTER_BASICS@1`  
**Claim text:** “При выборе или обустройстве временного укрытия необходимо учитывать воздействие погоды, доступность воды, вентиляцию и безопасность места.”

**Source registered:** Ready.gov root page: https://www.ready.gov/

**Passage result:** Not established by the registered root-page locator. FEMA's shelter-in-place guidance is hazard-specific and shows why ventilation cannot be treated as a universal instruction: for chemical hazards, guidance may require reducing outside air flow and turning off fans/HVAC, while other conditions call for different protective actions. The guidance also states that tap water may be unsafe in the specified chemical-hazard scenario.  
https://www.fema.gov/sites/default/files/documents/fema_shelter-in-place_guidance.pdf

**Risk route:** HIGH CONSEQUENCE. The Claim could be interpreted as operational advice for selecting or preparing a shelter. Incorrect choices about location, ventilation or water can increase exposure or create life-safety risks.

**Finding:** Keep HOLD. The list of considerations is reasonable at a high level, but “ventilation” is materially ambiguous and may be unsafe if read as “increase ventilation” during an airborne chemical release. Add an explicit statement that protective actions depend on the hazard and competent local authority guidance, or narrow the Claim to non-operational assessment factors. Require emergency-management / environmental-health review. No universal shelter checklist should be inferred from this Claim.

### 2.5 Shelter — no universally safe shelter

**Claim:** `CLM-SHELTER_BASICS-C@1`  
**Chain:** `EU-SHELTER_BASICS-C@1` → `SRC-SHELTER_BASICS@1`  
**Claim text:** “При чрезвычайной ситуации пригодность укрытия зависит от конкретной угрозы и условий среды; универсального безопасного укрытия для всех сценариев нет.”

**Source registered:** Ready.gov root page: https://www.ready.gov/

**Passage result:** The principle is directly consistent with FEMA's hazard-specific shelter-in-place guidance, which differentiates protective actions by hazard and building/location type and repeatedly directs users to follow current local emergency information. The registered root-page locator remains non-specific; the FEMA document is not the current canonical Source in the record chain.

**Risk route:** HIGH CONSEQUENCE. This is a safety-critical boundary claim and can help prevent unsafe generalization, but its wording must not be used to make individual shelter decisions without hazard-specific authority guidance.

**Finding:** Conceptual support located, but canonical passage chain remains incomplete. Keep HOLD pending a versioned, directly registered source/EU locator and qualified emergency-management review.

### 2.6 Water security — pollution, water-related disasters and ecosystems

**Claim:** `CLM-WATER_SECURITY-B@1`  
**Chain:** `EU-WATER_SECURITY-B@1` → `SRC-WATER_SECURITY@1`  
**Claim text:** “Водная безопасность включает защиту от загрязнения и связанных с водой бедствий, а также сохранение экосистем.”

**Source inspected:** UN-Water, *Water Security and the Global Water Agenda*, analytical brief (2013):  
https://www.unwater.org/publications/water-security-and-global-water-agenda  
PDF: https://www.unwater.org/sites/default/files/app/uploads/2017/05/analytical_brief_oct2013_web.pdf

**Passage result:** Direct conceptual support. UN-Water's working definition explicitly includes protection against water-borne pollution and water-related disasters, alongside preserving ecosystems. This is a working analytical definition from 2013, not a current legal standard or a complete technical water-safety framework.

**Risk route:** ELEVATED. Water security is connected to public health, disaster resilience and ecosystem protection. The Claim is descriptive and does not provide operational water-treatment or drinking-water-safety advice. Any such downstream use requires jurisdiction-specific standards and technical review.

**Finding:** Strong direct source fit at the level of a working definition. The EU description remains generic and lacks a section/page locator. Add a stable pinpoint to the definition and preserve the “UN-Water working definition” attribution and date/context. Independent corroboration is not established by this single Source.

### 2.7 Hydropower — generation from moving water

**Claim:** `CLM-HYDROPOWER_BASICS-A@1`  
**Chain:** `EU-HYDROPOWER_BASICS-A@1` → `SRC-HYDROPOWER_BASICS@1`  
**Claim text:** “Hydropower generates electricity by using the natural flow of moving water.”

**Source inspected:** U.S. Department of Energy, *Hydropower Basics*:  
https://www.energy.gov/cmei/water/hydropower-basics  
Supplementary DOE explanation:  
https://www.energy.gov/cmei/water/how-hydropower-works

**Passage result:** Direct support. DOE defines hydropower as using the natural flow of moving water to generate electricity and explains the conversion through turbines and generators. The Claim is appropriately concise. It does not cover pumped-storage operation, environmental effects, dam safety or project suitability; none should be inferred.

**Risk route:** LOW DIRECT CONSEQUENCE for the exact educational statement. Hydropower infrastructure itself is consequential, but this Claim is a basic descriptive definition, not operational design or safety guidance.

**Finding:** Source fit is direct. The EU remains generic; add a Claim-specific locator to the DOE “What is Hydropower?” section through a bounded versioned correction. Preserve U.S. DOE source identity and avoid using the general definition to imply that all hydropower systems rely only on natural river flow (pumped storage has a distinct operating mode).

## 3. Consolidated disposition

| Claim | Passage support at desk review | Risk route | Canonical pinpoint present | Disposition |
|---|---|---|---|---|
| Emergency management B | Partial; registered overview broad; supplementary FEMA Whole Community handout directly names private and voluntary partners | Moderate | No | HOLD |
| Emergency management C | Partial; FEMA planning guidance supports jurisdictional and plan-specific authority | Moderate | No | HOLD |
| Shelter A | General principle plausible; registered portal is not a passage | Moderate | No | HOLD |
| Shelter B | Registered portal not a passage; FEMA hazard-specific guidance exposes ventilation ambiguity | High consequence | No | HOLD |
| Shelter C | Principle directly consistent with hazard-specific FEMA guidance; registered locator remains generic | High consequence | No | HOLD |
| Water security B | Direct conceptual support from UN-Water working definition | Elevated | No | HOLD |
| Hydropower A | Direct support from DOE Hydropower Basics | Low direct consequence | No | HOLD |

## 4. Exact change and completion boundary

- Claims reviewed: 7.
- Evidence Use records reviewed: 7.
- Source records reviewed: 4.
- Claim/EU/Source identity and version links: 7/7 resolve and match.
- EUs with generic/non-pinpoint descriptions: 7/7.
- Direct or partial passage support found: 5; not established from the registered locator: 2.
- High-consequence routes: 2.
- Elevated routes: 1.
- Moderate routes: 3.
- Low-direct-consequence routes: 1.
- Canonical Claim/Evidence Use/Source records changed: 0.
- Canonical passage locators added: 0.
- D/E/B scores assigned or overwritten: 0.
- Risk metadata assigned or changed: 0.
- Independent specialist reviews completed: 0.
- Human View / release approval: 0.

## 5. Required next actions

1. Prepare a narrowly scoped correction proposal for Shelter B/C first. Resolve the ventilation ambiguity and register hazard-specific passages; require qualified emergency-management review.
2. Prepare a source/EU correction proposal for Emergency Management B/C. Separate the FEMA IS-230.E course overview from the Whole Community and CPG 101 passages; preserve U.S. jurisdictional boundaries.
3. Add a stable pinpoint for the UN-Water working definition in Water Security B; preserve its date and non-regulatory status.
4. Add a stable DOE “What is Hydropower?” locator for Hydropower A; do not expand the Claim into design, environmental or safety guidance.
5. Keep all seven Claims HOLD until versioned changes are authorized, regression-tested and independently reviewed. Run exact-head Reference Tests, Release Conformance Gate and Offline Edition after any canonical edit.

This package is a desk review and routing artifact. It is not a complete risk assessment, legal/engineering advice, independent certification, or M13 closure.
