# M2 SUBSTANTIVE AUDIT — 2026-10-08

## Baseline

- M1 CLEAN checkpoint: `0019aa2376fd45ecc063f3f6ee680e087ab8d729`
- M2 scope lock: `9277308cd73673492ea4d2674f9b90cb0a7c7633`
- Corpus at audit start: 479 vertical slices / 4619 Records / 19 Record types / 51 Relations.

## Audit result

M2 is **NOT CLEAN**. Confirmed substantive debt exists in all ten scoped slices. The debt is concentrated in evidence independence, applicability boundaries, and a small number of semantic formulations.

No new Record type is required.

### 1. air-quality-basics — DEBT

Findings:
- single EPA evidence track;
- AQI and pollutant-monitoring claims need separation between measurement/reporting and health-guideline interpretation;
- current content does not clearly distinguish U.S. EPA reporting constructs from international health-based guidance.

Required correction:
- add independent WHO evidence track;
- preserve EPA-specific AQI semantics;
- add explicit jurisdiction/source-role boundary.

### 2. agriculture-basics — DEBT

Findings:
- single FAO evidence track;
- productivity claim is context-dependent and should not imply a universal causal ranking;
- local soil, water, climate and management conditions need an explicit applicability boundary.

Required correction:
- add independent agricultural/scientific institutional evidence;
- tighten the applicability wording;
- preserve non-universality of practice claims.

### 3. anatomy-basics — DEBT

Findings:
- single NIGMS evidence track;
- current claims are descriptive but lack an explicit boundary against clinical interpretation;
- independent educational anatomy evidence would improve reuse and reduce source monoculture.

Required correction:
- add independent anatomy source;
- add a descriptive-anatomy versus clinical-interpretation boundary.

### 4. antimicrobial-resistance-basics — DEBT

Findings:
- single WHO evidence track;
- current claims are suitable as public-health basics but need an explicit boundary against individual treatment selection;
- independent public-health evidence is justified because the topic is high-consequence and cross-sector.

Required correction:
- add independent public-health evidence;
- preserve One Health framing;
- add explicit non-individual-treatment boundary.

### 5. acid-base-basics — DEBT / semantic correction required

Findings:
- single OpenStax evidence track;
- Claim C requires bounded interpretation of buffers by solution conditions;
- current Claim B states pH as a logarithmic measure of hydrogen-ion concentration, while the current IUPAC definition is in terms of hydrogen-ion activity. The simplified formulation is acceptable only as an explicitly bounded introductory approximation.

Required correction:
- add independent IUPAC evidence;
- correct or explicitly qualify the pH formulation;
- preserve educational model boundaries and prohibit inference into hazardous procedures.

### 6. analytical-chemistry-basics — DEBT

Findings:
- single NIST evidence track;
- existing Claim B correctly notes that measurement quality depends on method, sample and data processing, but the slice lacks an independent metrological terminology track;
- Claim C already points toward calibration/model/range applicability and should be tied to explicit measurement-procedure and uncertainty boundaries.

Required correction:
- add independent IUPAC evidence;
- strengthen measurement-procedure/uncertainty boundary;
- retain method-specific applicability.

### 7. algebra-basics — DEBT

Findings:
- single OpenStax evidence track;
- claims are structurally sound but source monoculture limits independent verification;
- interpretation of equations/functions should remain mathematical-model content rather than an implicit claim about real systems.

Required correction:
- add an independent educational/mathematical evidence track;
- add explicit model/interpretation boundary where needed.

### 8. agrifood-systems-basics — DEBT

Findings:
- single FAO evidence track;
- current claims are broadly aligned with the systems framing, but independent corroboration is useful because the slice is a high-reuse systems foundation;
- system boundary should distinguish descriptive system mapping from causal policy conclusions.

Required correction:
- add independent systems/food-systems evidence;
- preserve the distinction between system description and causal/policy inference.

### 9. architecture-basics — DEBT / claim-depth correction required

Findings:
- single Britannica evidence track;
- Claim A is effectively self-referential ("the slice describes basic concepts") and provides little substantive domain knowledge;
- architecture content needs a clearer boundary between conceptual/design description and jurisdiction-specific engineering, code or structural requirements.

Required correction:
- replace or narrow the self-referential claim with substantive domain content;
- add independent architectural evidence;
- preserve the engineering/code applicability boundary.

### 10. ancient-civilizations-basics — DEBT / causal-boundary correction required

Findings:
- single OpenStax evidence track;
- Claim B uses causal language about agriculture, settlement and population growth and therefore needs stronger evidence and an explicit regional/temporal boundary;
- current Claim C correctly identifies archaeological and written evidence but does not itself bound evidentiary completeness.

Required correction:
- add independent archaeological/historical evidence;
- qualify causal and regional claims;
- make evidence limits and chronology-versus-causality distinction explicit.

## Cross-slice findings

### Evidence independence

All ten slices currently have one source record. Independent corroboration is materially justified for this package because these are high-reuse foundations and several carry health, environmental, chemistry or systems implications.

### Human View

The most important user-facing boundaries are:
- air quality: measurement/reporting is not a universal health threshold;
- agriculture: practices are condition-dependent;
- anatomy and AMR: general information is not individual clinical advice;
- chemistry: definitions/models do not authorize hazardous procedures;
- architecture: conceptual knowledge is not jurisdiction-specific engineering/code compliance;
- ancient history: evidence and inference must remain distinguishable.

### Relations

No new Relation is required at audit stage. Relations will be added only if the corrected content establishes a material dependency.

## Closure criterion

M2 remains open until all confirmed findings are corrected, dedicated regressions and documentation are synchronized, the substantive re-audit is PASS, evidence-independence and Human View audits are PASS, the unified debt map is CLOSED, and exact-head Reference + Release Gate + Offline verification is GREEN.
