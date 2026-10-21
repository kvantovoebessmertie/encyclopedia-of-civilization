# M13 Claim Review Batch 23 — Construction Safety Foundations
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **4 additional Claims reviewed. This is a bounded review batch, not domain closure or corpus completion.**

## Method
Reviewed four Claim statements and all seven linked Evidence Use records in `construction-safety-basics`. Inspected the two source identities and canonical locators: U.S. OSHA construction guidance and the UK Construction (Design and Management) Regulations 2015. D (explanatory depth), E (claim-specific evidence fit) and B (boundary discipline) are scored independently from 0–3. This desk review does not replace a jurisdiction-specific compliance assessment.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-CONSTRUCTION_SAFETY_BASICS-A` | 1 | 2 | 2 | Correct but very broad statement that construction has diverse occupational hazards. OSHA is directly relevant to U.S. construction, and UK CDM is an independent regulatory source for its own jurisdiction. The Evidence Use records are better than generic “supports” wording, but their descriptions still do not identify the specific passages or hazard examples. Keep both jurisdictions explicit. |
| `CLM-CONSTRUCTION_SAFETY_BASICS-B` | 2 | 2 | 2 | Falls, electrical hazards, dust and equipment are credible examples of construction hazards. The two institutional sources are relevant, but the Evidence Use descriptions do not map each listed hazard to the supporting source material. OSHA and UK CDM are not interchangeable legal regimes; avoid implying identical duties or thresholds. |
| `CLM-CONSTRUCTION_SAFETY_BASICS-C` | 2 | 2 | 3 | Strong boundary statement: controls depend on the task, equipment, site and applicable rules. Both sources are relevant to risk-specific controls, and the wording correctly avoids a universal checklist. The record would be more auditable if Evidence Use named the concrete source material; jurisdiction boundary is sound. |
| `CLM-CONSTRUCTION_SAFETY_BASICS-D` | 2 | 2 | 2 | Planning, role allocation, coordination, risk information and review are consistent with a construction-safety management approach. The linked UK CDM source is specifically a UK regulatory framework; the claim itself is phrased generally and could be read as universally legally required. Label this as a general management pattern and distinguish jurisdiction-specific statutory duties. |

## Findings
1. **Evidence fit is relevant but not passage-level:** all four Claims have institutional source coverage; the seven Evidence Use records make primary/additional-source roles visible, but still lack a precise passage, section or specific supported subclaim.
2. **Independent sources have different jurisdictional force:** OSHA guidance is U.S.-specific; the CDM Regulations are UK law. Their conceptual overlap can corroborate general safety principles but cannot establish equivalent legal obligations across countries.
3. **No clear falsity found in these four statements.** The main deficits are explanatory depth, source traceability and explicit jurisdiction boundaries.
4. No content Records were changed. These four Claims remain within the frozen 1,494-Claim denominator. This batch does not close construction safety, the high-consequence pass, or M13.

## Records inspected
- `CONTENT/vertical-slices/construction-safety-basics/records/CLM-CONSTRUCTION_SAFETY_BASICS-A.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/CLM-CONSTRUCTION_SAFETY_BASICS-B.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/CLM-CONSTRUCTION_SAFETY_BASICS-C.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/CLM-CONSTRUCTION_SAFETY_BASICS-D.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-A.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-A-2.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-B.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-B-2.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-C.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-C-2.json`
- `CONTENT/vertical-slices/construction-safety-basics/records/EU-CONSTRUCTION_SAFETY_BASICS-D.json`

## Sources
- U.S. Occupational Safety and Health Administration, Construction: https://www.osha.gov/construction
- UK Government, Construction (Design and Management) Regulations 2015: https://www.legislation.gov.uk/uksi/2015/51

## Acceptance status
Four additional Claim rows have explicit D/E/B scores and rationales. Follow-up actions: improve source-to-subclaim traceability and preserve jurisdiction-specific legal boundaries. Full 1,494-Claim scoring, high-consequence recall, Human View, Relation endpoint review, independent scoring review, authorized corrections with regression tests, and final same-HEAD 3/3 CI remain open.
