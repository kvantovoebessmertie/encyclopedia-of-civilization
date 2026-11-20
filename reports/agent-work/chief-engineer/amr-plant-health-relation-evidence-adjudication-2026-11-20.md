# AMR / Plant Health — Focused Cross-Slice Evidence Adjudication

- **Agent:** chief-engineer
- **Task:** Focused WP1 adjudication of `REL-CROSS-AMR-PLANT-HEALTH@3`
- **Date (UTC):** 2026-11-20
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** 54071d43bbb3e4b2f7bd071a092a2718d4fc6d10
- **Status:** VERIFIED — exact canonical graph and official FAO sources inspected; report-only

## 1. Request and acceptance criteria

Continue WP1 by testing the existing AMR / Plant Health Relation against exact participant wording and authoritative FAO evidence. Preserve canonical records, versioning and HOLD unless an exact owner authorization exists.

## 2. Scope

- **In scope:** Relation @3, Context @2, both participant Claims, both Evidence Use records, both original Source records, the existing FAO Source record, and official FAO source pages.
- **Out of scope:** canonical Claim/Evidence Use/Source/Relation/Context edits, adding evidence links or locators, candidate promotion, rights clearance, and release/merge actions.
- **Dependencies:** PR #22 current HEAD and the WP1 semantic-HOLD checkpoint.

## 3. Work performed

Fetched the exact Relation, Context, participant Claims, Evidence Use and Source records at the starting HEAD. Reviewed the FAO page already represented by `SRC-FAO-AMR-PLANT-HEALTH@1` and corroborating official FAO pages on plant production, AMU in plant production/protection, and One Health / plant health.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/amr-plant-health-relation-evidence-adjudication-2026-11-20.md` | Added report-only adjudication | Record endpoint fit, evidence strength, and remaining canonical linkage gap |

## 5. Exact canonical graph

At starting HEAD `54071d43bbb3e4b2f7bd071a092a2718d4fc6d10`:

- `REL-CROSS-AMR-PLANT-HEALTH@3`
  - `relation_type`: `one_health_plant_health_link`
  - participants: `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` and `CLM-PLANT_PATHOLOGY_BASICS-A@1`
  - frame: `CTX-REL-CROSS-AMR-PLANT-HEALTH@2`, correctly targeting Relation @3.
  - provenance already lists the two slice Sources and `SRC-FAO-AMR-PLANT-HEALTH@1`.
- `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`: “Устойчивость затрагивает людей, животных, растения, пищевые системы и окружающую среду и поэтому требует межсекторного подхода.”
  - `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` supports the Claim through WHO's general AMR fact sheet; it does not cite the FAO plant-health bridge.
- `CLM-PLANT_PATHOLOGY_BASICS-A@1`: “Фитопатология изучает болезни и расстройства растений.”
  - `EU-PLANT_PATHOLOGY_BASICS-A@1` supports the Claim through the American Phytopathological Society's introductory definition; it does not cite the FAO AMR/plant-health material.
- `SRC-FAO-AMR-PLANT-HEALTH@1` is already registered and its locator describes FAO's material on plant-pathogen resistance to antimicrobials, antibiotic use against bacterial crop diseases, plant-production pathways contributing to AMR in human/animal pathogens, and plant health in AMR programmes.

**Key graph distinction:** the FAO Source appears in Relation provenance, but there is no canonical Evidence Use record linking that Source to either participant Claim. Relation provenance is not a substitute for Claim-level evidence linkage.

## 6. Official FAO evidence

### 6.1 FAO — AMR in the context of plant health

Locator: https://www.fao.org/pest-and-pesticide-management/pesticide-risk-reduction/amr/en/

FAO explicitly distinguishes two plant-health AMR dimensions:
1. resistance of plant pathogens to antimicrobials used as pesticides; and
2. contributions of pesticide use in plant production to AMR in human and animal pathogens.

It also identifies antibiotics (including streptomycin and oxolinic acid) used against bacterial crop diseases and describes plant health as an indispensable part of AMR programmes.

### 6.2 FAO — Plant production sector

Locator: https://www.fao.org/antimicrobial-resistance/key-sectors/plant-production/en/

FAO states that misuse/overuse of antimicrobial pesticides and antibiotics in plant production can create occupational exposure, consumer and environmental risks. It notes that residues may encourage emergence of resistant fungal and bacterial strains and potentially increase human-resistance risks. It also describes integrated pest management, phytosanitary prevention, and reduction of unnecessary antimicrobial use as risk-reduction approaches.

### 6.3 FAO — Antimicrobial use in plant production and protection

Locator: https://www.fao.org/antimicrobial-resistance/resources/infarm-system/amu-in-plant-production-and-protection/en/

FAO identifies plant pathogenic bacteria as causes of substantial crop losses and describes farmers' use of antibiotics against bacterial plant diseases. It also cautions that global monitoring is incomplete and quantities applied are difficult to assess.

### 6.4 FAO — One Health and plant health

Locator: https://www.fao.org/one-health/highlights/amr-does-it-matter-for-plant-health-too/en

FAO describes plant-pathogen resistance, antimicrobial use in crop protection, possible environmental residues, and food-safety concerns. It explicitly situates plant, animal, human and environmental health within the One Health approach, while noting that some of the evidence and implications remain less explored.

## 7. Adjudication

**Finding:** the official FAO evidence establishes a direct and meaningful AMR ↔ Plant Health connection. The relation is not merely thematic adjacency: antimicrobials are used to control plant pathogens; plant pathogens can develop resistance; and antimicrobial use in plant production can contribute to environmental, food-system and cross-sector AMR concerns.

The endpoint fit is nevertheless uneven:
- The AMR Claim directly includes plants and calls for a cross-sector approach; FAO provides strong support for this broad proposition.
- The Plant Pathology Claim only defines the field as study of plant diseases and disorders. It does not mention plant pathogens, antimicrobial treatment, pathogen resistance, or plant-health management.
- The FAO Source is listed in Relation provenance but not in either participant's Evidence Use. This is a traceability gap, not a source-discovery gap.
- The current Relation type `one_health_plant_health_link` is defensible at a high level, but the current Plant Pathology endpoint is too generic to demonstrate the specific AMR mechanism by itself.
- FAO distinguishes resistance in plant pathogens from the potential contribution of plant-production antimicrobial use to resistance in human/animal pathogens. Those mechanisms should not be collapsed into a single undifferentiated assertion.

**Disposition:** preserve `REL-CROSS-AMR-PLANT-HEALTH@3` and affected slices on **HOLD**. Upgrade the research finding to “direct official FAO bridge confirmed; Relation provenance already records the bridge; Claim-level Evidence Use linkage and participant specificity remain unresolved.” Do not add an EU, change the Claim, replace the participant, or issue a new Relation version without bounded owner authorization and independent plant-health/AMR review.

## 8. Rights and reuse boundary

This review relies on official FAO source identities, links, and independently worded factual summaries. It does not reproduce FAO text, tables, figures, images, photographs, or logos. The existing FAO Source record already flags that certain attributed non-commercial uses may be permitted while translation/adaptation and resale/commercial uses require permission, and third-party components require separate clearance. That source-specific notice is not a project-wide licence and does not resolve the distribution model. No WP2 decision R-01–R-10 is closed.

## 9. Verification

| Check | Result | Notes |
|---|---|---|
| Exact Relation/Context inspection | VERIFIED | Relation @3; Context @2 targets Relation @3 |
| Exact participant Claims | VERIFIED | Both Claim statements checked |
| Exact Evidence Use and Sources | VERIFIED | FAO bridge is in Relation provenance, not participant EU |
| Official FAO cross-check | VERIFIED | Four FAO official pages reviewed |
| Canonical changes | NONE | Report-only |
| CI | NOT RUN | No CI PASS claimed |

## 10. Unresolved issues and risks

- No independent plant pathology / AMR subject-matter reviewer was engaged.
- No canonical Evidence Use record links the FAO Source to the participants.
- The Plant Pathology Claim is broad and does not itself establish the AMR-specific mechanism.
- FAO's stated monitoring limitations mean global usage quantities and prevalence should not be asserted without additional evidence.
- Rights review for any future reuse remains open.
- No candidate disposition, allowlist, licence, permission, or publication state changed.

## 11. Recommendation and acceptance

- **Recommendation:** retain Relation @3 on HOLD. If canonical remediation is authorized, first decide whether to retain the generic Plant Pathology Claim as a broad navigation endpoint or identify a more specific existing plant-pathogen/AMR Claim. Then add only exact, pinpointed Evidence Use permitted by the authorization.
- **Acceptance status:** CONDITIONAL — research bridge established; canonical traceability and endpoint specificity remain open.
- **Reason:** FAO evidence is direct and strong, but current participant evidence linkage is incomplete.

## 12. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/amr-plant-health-relation-evidence-adjudication-2026-11-20.md`
- **Next owner/action:** authorize or decline a tightly bounded canonical Evidence Use / endpoint-alignment remediation; obtain independent plant-health and AMR review.

## 13. Integrity statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
