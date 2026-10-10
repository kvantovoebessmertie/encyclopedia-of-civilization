# M13 Claim Review Batch 18 — Emergency Water Treatment
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed; not a full water-domain or full-corpus acceptance.**

## Scope
This batch reviews three Claims in the `water` slice using their worksheet-linked Evidence Use descriptions and current CDC/EPA guidance. Scores follow the M13 D/E/B rubric (0–3 independently). The earlier batch 17 reviewed `CLM-WATER-CHEMICAL-LIMIT`; it is not duplicated here.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-WATER-BOILING-EFFECTIVE` | 2 | 3 | 2 | The statement gives a useful emergency rule but does not explain the full limits of boiling. The Evidence Use points to the CDC section specifically about boiling; CDC guidance says boiling is the best method to kill germs in water. The claim is bounded by “болезнетворных микроорганизмов”; preserve nearby warnings that boiling does not remove chemical/radioactive contaminants and follow local advisories. |
| `CLM-WATER-BOILING-TIME` | 2 | 3 | 2 | The statement includes a concrete procedure and elevation exception. The linked Evidence Use identifies the exact CDC section on duration; CDC specifies a rolling boil for 1 minute and 3 minutes above 6,500 feet. EPA guidance is broadly corroborative but uses a different elevation threshold (above 5,000 feet / 1,000 metres), so the content should preserve the exact named authority and avoid blending jurisdictions or thresholds. Review local applicability before presenting this as universal guidance. |
| `CLM-WATER-INDEPENDENT-CORROBORATION` | 2 | 3 | 3 | The statement explicitly distinguishes microbial disinfection from chemical contamination and conditions use on contamination type and official advice. Its linked Evidence Use names EPA’s emergency-disinfection guidance; EPA explicitly says boiling/disinfection does not destroy heavy metals, salts, and most other chemicals, while boiling kills disease-causing microorganisms. This is genuine corroboration from a second authority for the broader water-treatment principle, though exact operational thresholds differ by authority. |

## Findings and follow-up
1. The reviewed Evidence Use descriptions are materially more claim-specific than the generic descriptions found in the nuclear-foundation batch.
2. **Jurisdiction/threshold distinction needs explicit preservation.** CDC's current page uses 6,500 feet for a 3-minute boil; EPA's page uses above 5,000 feet / 1,000 metres. This is not automatically a contradiction: the encyclopedia should cite the chosen authority, state the applicable jurisdiction, and avoid presenting different instructions as one universal rule.
3. The water slice still needs integration review across storage, treatment, chemical contamination, radiological contamination, local advisories, and the uses of water beyond drinking.
4. No content record was changed. Any wording or source edits require separate correction scope and regression.

## Sources checked on 2026-10-10
- CDC, “How to Make Water Safe in an Emergency”: https://www.cdc.gov/water-emergency/about/
- US EPA, “Emergency Disinfection of Drinking Water” (current page): https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

## Acceptance status
Three Claim rows have explicit D/E/B scores and rationales. The full denominator remains 1,494. This batch does not close the complete water-domain review, high-consequence overlay, Human View, Relation review, independent scoring audit, or M13.
