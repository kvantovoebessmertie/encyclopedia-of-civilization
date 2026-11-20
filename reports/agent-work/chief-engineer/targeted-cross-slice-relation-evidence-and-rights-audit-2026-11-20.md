# Targeted Cross-Slice Relation Evidence and Rights Audit — AMR / Plant Health, Research / Statistics, Migration / Labour

Date: 2026-11-20  
Inspection PR HEAD: `c177cbf0def595b4d478d0eddb512db5b33c18d4`  
Scope: three priority Relations in the existing 15-item semantic-HOLD queue  
Status: **NEW PRIMARY-SOURCE EVIDENCE FOUND FOR ALL THREE LINKS; MIGRATION / LABOUR HAS THE STRONGEST DIRECT BRIDGE; NO CANONICAL CHANGES; ALL THREE REMAIN HOLD**

## 1. Method and boundaries

Re-fetched the current Relation, Relation-specific Context, participant Claims and Evidence Use records at the exact inspection HEAD. Conducted a targeted external source search for authoritative material that directly connects the concepts represented by each endpoint pair, then separately checked source-specific rights terms.

This report is a research and adjudication aid only. It does not create a new canonical Source/Evidence Use record, add a provenance reference, change a Relation, amend a Claim, change a rights decision, or authorize a release disposition. All three Relations remain HOLD. No endpoint substitution or scope expansion is proposed.

## 2. REL-CROSS-AMR-PLANT-HEALTH@2 — direct FAO bridge identified; canonical evidence chain remains incomplete

### Current canonical endpoints

- Relation: `REL-CROSS-AMR-PLANT-HEALTH@2`, type `one_health_plant_health_link`; Context @1 points back to Relation @2.
- `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`: “Устойчивость затрагивает людей, животных, растения, пищевые системы и окружающую среду и поэтому требует межсекторного подхода.”
- Its Evidence Use C@1 points to WHO *Antimicrobial resistance* but has only a generic material description and no pinpoint locator.
- `CLM-PLANT_PATHOLOGY_BASICS-A@1`: “Фитопатология изучает болезни и расстройства растений.”
- Its Evidence Use A@1 points to the American Phytopathological Society's “What Is Phytopathology?” and also has only a generic material description.

### New direct evidence

FAO's official “Antimicrobial resistance” page in its plant-health / pesticide-risk-reduction section states that AMR in plant health includes:
1. resistance of plant pathogens against antimicrobials used as pesticides;
2. contributions of pesticide use in plant production to AMR in human and animal pathogens;
3. examples of antibiotics used to control bacterial crop diseases; and
4. the importance of plant health within AMR programmes.

Locator: https://www.fao.org/pest-and-pesticide-management/pesticide-risk-reduction/amr/en/

The current WHO fact sheet (16 July 2026) independently states that drug-resistant infections affect plant health and reduce farm productivity, threatening food security, and describes the 2026–2036 GAP-AMR as a One Health approach.

Locator: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance

### Assessment

This materially improves the case for the cross-slice relation: it is not merely topic adjacency. FAO directly describes AMR in plant health and the reciprocal plant-production / human-animal AMR pathway.

However, the existing two canonical Evidence Use records do not currently contain these specific FAO/WHO locators, and the Plant Pathology endpoint remains a general discipline definition. The Relation's current provenance lists only the WHO AMR Source and APS Plant Pathology Source. The external FAO page is not currently represented by a canonical Source/Evidence Use or Relation-level evidence path in the inspected records.

**Recommended disposition:** move from “no direct mechanism found” to **“direct external bridge identified; canonical evidence-linkage and independent endpoint-fit review required.”** Keep HOLD. Do not broaden either Claim or silently treat the FAO page as part of the current canonical evidence chain.

### Rights screen

FAO's general website terms state that non-expressly-exempt web content may be copied for private study, research, teaching and non-commercial products/services with attribution; translation/adaptation and resale/commercial use rights require a permission request. Third-party components require separate clearance. Hyperlinking is encouraged without prior permission.

- Terms: https://www.fao.org/contact-us/terms/
- No FAO photograph, graphic, table or logo is proposed for reuse.
- Safe research path for now: link to the page and independently word factual paraphrase only; do not reproduce or translate FAO expression or assets.
- The Encyclopedia's intended distribution/commercial model remains undecided, so this does not close rights review.

WHO's copyright policy states that WHO publications are generally CC BY-NC-SA 3.0 IGO, while third-party credited materials may require separate permission; commercial uses require permission. Verify the specific fact-sheet copyright status and third-party components before any expressive reuse.

- WHO terms: https://www.who.int/about/policies/publishing/copyright

## 3. REL-CROSS-RESEARCH-STATISTICS@3 — strong conceptual fit; current endpoint/evidence chain is materially improved

### Current canonical endpoints

- Relation: `REL-CROSS-RESEARCH-STATISTICS@3`, type `research_and_statistical_inference_link`; Context @2 points back to Relation @3.
- `CLM-RESEARCH_METHODS_BASICS-A@1`: scientific methods include systematic formulation of questions, obtaining data and evaluating evidence in accordance with the research task.
- Evidence Use A@2: National Academies (2019), *Reproducibility and Replicability in Science*, Chapter 2, “Scientific Methods and Knowledge”, pp. 27–29. It expressly limits the proposition to a general overview and does not assert one mandatory linear sequence.
- `CLM-STATISTICS_INFERENCE_BASICS-A@1`: statistical inference uses sample data to obtain information about characteristics of a wider population or model.
- Evidence Use A@2: NIST/SEMATECH e-Handbook, Chapter 3, §3.1.3.4, “Populations and Sampling”; the support boundary covers sample-to-population inference and its design/representativeness/precision constraints.

### New direct evidence confirmation

National Academies Chapter 2 (pp. 27–29) explicitly presents statistical inference as part of how scientific knowledge is gained, questioned and modified. It also describes scientific inquiry, systematic observation/experimentation, measurement, evidence collection and characterization, data analysis and critical review.

Locator: https://www.nationalacademies.org/read/25303/chapter/5

NIST's current locator remains directly relevant to population and sampling inference:
https://www.itl.nist.gov/div898/handbook/ppc/section1/ppc134.htm

### Assessment

The current endpoint pair supports a defensible broad research-methods / statistical-inference navigation link. The link is conceptual and methodological, not an assertion that all research is statistical, that every research design requires inferential statistics, or that statistical inference alone validates a study.

**Recommended disposition:** retain as a **high-confidence contextual-navigation candidate**, pending independent editorial confirmation of the stated boundary. Do not confuse this with the separate `REL-CROSS-M2-STATISTICS-RESEARCH@3`, whose Research Methods B endpoint concerns reproducibility/replicability and does not establish its declared research-design relation.

### Rights screen

National Academies Press states that its books are copyrighted with all rights reserved; PDFs may not be distributed, posted or copied without written permission. Reuse of portions in other publications/media requires a rights request/licence.

- Rights: https://www.nationalacademies.org/request-rights-and-permissions
- Current canonical Evidence Use should remain a pinpoint citation/link, not a copied chapter, PDF, table, figure or extended passage.
- Any reproduction, translation or adaptation requires item-specific rights review/permission.
- The NIST e-Handbook is a separate source and must be screened on its own terms.

This rights flag does not negate the scientific relevance of the National Academies locator; it constrains reuse of protected expression and the release bundle.

## 4. REL-CROSS-MIGRATION-LABOR-ECONOMICS@4 — strongest direct cross-domain bridge identified; exact locator and provenance work still required

### Current canonical endpoints

- Relation: `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`, type `migration_and_labor_measurement_link`; Context @1 points back to Relation @4.
- `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2`: comparison of migration processes requires clarification of definition, time period, territory and measurement of flows or stocks.
- Evidence Use C@2: UNSD *Recommendations on Statistics of International Migration and Temporary Mobility* (2025, rev. 2), Executive Summary recommendations 1–3, Chapter 3 and §3(a), pp. 17–22; Chapter 2 §2(a), pp. 7–10.
- `CLM-LABOR_ECONOMICS_BASICS-C@2`: labour-market analysis uses employment, earnings, working time, productivity and labour-underutilization indicators.
- Evidence Use C@2: ILOSTAT descriptions for labour-force status, wages/working time, labour productivity and labour underutilization; definitions and series differ and are not interchangeable without methodological checks.

### New direct cross-domain source

ILO's June 2026 *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility: ILO practical guide* explicitly integrates international migration concepts with labour-force and employment statistics.

Verified primary PDF: https://www.ilo.org/sites/default/files/2026-07/ILO_Guide_Mapping_ILMS_2026_FINAL.pdf

Pinpoint locator candidates:
- Printed pp. 10–12: migration, labour-market access/participation, working conditions and the need for reliable/comparable labour-dimension data.
- Printed pp. 22–27: migration and mobility statistical concepts, including definitions and stocks/flows.
- Printed pp. 30–33: labour-force status, employment, unemployment and labour underutilization.
- Printed pp. 34–38: international labour migration, labour attachment and related groups.
- Printed p. 43: minimum data items for international labour migration statistics.
- Printed pp. 57–58: core labour-market indicators for international migrants and disaggregation by migrant status.
- Printed pp. 63–66: source-specific capacity/limitations, including labour-force surveys, wages, contractual hours and administrative records.

The guide directly bridges migration statistics and labour-market measurement. It also explicitly warns that source coverage and sample design can bias estimates or make migrant subgroup estimates imprecise. It does not establish that every general labour-economics indicator, especially productivity, is automatically available or comparable for migrant populations.

### Assessment

This is the strongest newly identified direct bridge for the Relation's declared measurement-link type. It supplies an integrated measurement framework that connects the migration endpoint's definitions/time/territory/stocks/flows with the labour endpoint's employment, wages, hours and underutilization measures.

**Recommended disposition:** upgrade to **“strong direct source candidate identified; exact source/provenance linkage and independent semantic review required.”** Keep HOLD until the new source is represented through an authorized canonical evidence path and the Relation's provenance convention is explicitly resolved. The existing Relation provenance currently points directly to the two Claims, not to Source records; prior audit identified this as a consistency/policy question, not an automatically invalid structure. Do not change it autonomously.

### Rights screen

The PDF copyright page (printed p. ii) explicitly licenses the 2026 guide under CC BY 4.0, requires attribution and indication of changes, excludes third-party material from the licence, and prohibits use of the ILO emblem/name/logo in connection with translations, adaptations or derivatives. The ILO's current rights policy confirms that publications from 3 May 2023 are generally CC BY 4.0 unless a work states otherwise.

- Exact work-level licence: printed p. ii in the PDF above.
- General ILO rights policy: https://www.ilo.org/rights-and-permissions
- The 2026 PDF's own copyright page controls over the general default.
- Any reuse must screen third-party figures, photographs and other attributed components separately.
- If the guide itself is translated/adapted, include the disclaimer printed on p. ii. Factual paraphrase and citation do not imply that the guide has been translated or adapted.

This is a materially better rights position than the National Academies source, but it does not clear the project licence or any third-party component. All first-edition release decisions remain owner-controlled.

## 5. Cross-relation disposition summary

| Relation | New evidence result | Remaining blocker | Disposition |
|---|---|---|---|
| AMR / Plant Health @2 | FAO provides a direct plant-AMR mechanism; WHO independently notes plant impacts | FAO not represented in canonical evidence path; current Plant Pathology endpoint is generic; source-rights/distribution review | HOLD |
| Research / Statistics @3 | National Academies directly treats statistical inference as part of scientific inquiry; NIST supports sample/population inference | Independent boundary review; NAP rights restrict expressive reuse | HOLD; high-confidence navigation candidate |
| Migration / Labour @4 | ILO 2026 guide directly integrates migration and labour statistics, with precise locators and CC BY 4.0 | New source not in canonical graph; relation provenance consistency; independent semantic review; third-party asset screen | HOLD; strong direct-source candidate |

## 6. Required next actions

1. Request separate bounded authorizations before adding any Source, Evidence Use, Relation provenance reference, or Context/Relation version.
2. For AMR/Plant, consider FAO page as a relation-specific evidence source; preserve the distinction between plant-pathogen resistance and pesticide-use contributions to human/animal AMR.
3. For Research/Statistics, ask an independent scientific reviewer to confirm the navigation boundary and ensure NAP is linked/cited without unauthorized PDF or expressive reuse.
4. For Migration/Labour, consider a canonical Source record for the ILO 2026 guide and an exact Evidence Use locator for the existing migration/labour measurement claims; keep productivity outside the guide's asserted support unless a separate locator is verified.
5. Resolve the Relation provenance consistency question under the existing Relation Standard; do not invent a new schema or policy rule.
6. Keep all three Relations and affected slices HOLD until independent semantic, rights, editorial and Human View gates close.

## 7. Change-control statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope was changed.
- No candidate membership, INCLUDE/HOLD/EXCLUDE decision, allowlist or publication state changed.
- No owner decision, licence, rights grant, editor, approver or contact was invented.
- PR #22 remains Draft and unmerged; `main` is untouched.

**Acceptance:** accept this report as a bounded external-evidence and source-rights research update for three existing semantic-HOLD Relations. It is not an authorization to modify canonical records or promote any item.
