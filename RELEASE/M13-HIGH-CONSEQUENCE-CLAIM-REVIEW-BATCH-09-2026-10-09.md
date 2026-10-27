# M13 High-Consequence Claim Review — Batch 09
Date: 2026-10-09
Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: four food-safety claims and linked Evidence Use / Source records in `food-safety-basics`.
Review type: targeted high-consequence review. No content records changed in this batch.

## Scoring rubric
- **D — explanatory depth (0–3):** explanatory value and practical meaning.
- **E — claim-specific evidence fit (0–3):** fit of the linked source and Evidence Use to the exact proposition.
- **B — boundaries / epistemic discipline (0–3):** applicability limits and prevention of overgeneralization.
Scores are reviewer judgments for triage, not automated measurements.

## Claim-level review

### 1. `CLM-FOOD_SAFETY_BASICS-A` — D2 / E1 / B2
**Statement:** Basic food-safety measures include cleaning, separation, adequate heat treatment and proper cooling.

**Linked records:** `EU-FOOD_SAFETY_BASICS-A` → `SRC-FOOD_SAFETY_BASICS`.

**External check:** FDA's [Food Safety at Home](https://www.fda.gov/consumers/womens-health-topics/food-safety-home) explicitly presents the four basic steps: clean, separate, cook and chill. CDC's [Preventing Food Poisoning](https://www.cdc.gov/food-safety/prevention/) presents the same framework.

**Assessment:** The claim accurately captures the recognized four-step framework. Its Evidence Use description is generic boilerplate and does not identify the source's four-step list. The wording is concise but “proper cooling” could be interpreted as only cooling after cooking; the broader concept includes prompt refrigeration and safe cold storage.

**Disposition:** Confirmed Evidence Use specificity weakness. Candidate for a narrow, source-specific description and regression.

### 2. `CLM-FOOD_SAFETY_BASICS-B` — D2 / E1 / B2
**Statement:** Separating raw products and ready-to-eat food reduces cross-contamination risk.

**Linked records:** `EU-FOOD_SAFETY_BASICS-B` → `SRC-FOOD_SAFETY_BASICS`.

**External check:** FDA's home food-safety page advises keeping raw foods separate. CDC explains that raw meat, poultry, seafood and eggs can spread germs to ready-to-eat foods and recommends separate cutting boards/plates and sealed storage.

**Assessment:** The claim is directly supported, and the risk mechanism is named. The linked Evidence Use is nevertheless too generic to provide a useful evidence trail. A user-facing instruction should include practical points such as separating during storage and preparation, containing raw juices and not reusing a plate for cooked food without washing.

**Disposition:** Confirmed Evidence Use specificity weakness; verify that detailed practices are discoverable in the slice or adjacent food-handling content.

### 3. `CLM-FOOD_SAFETY_BASICS-C` — D2 / E1 / B3
**Statement:** Specific requirements for temperature, storage and food-risk controls depend on the product, process and applicable rules.

**Linked records:** `EU-FOOD_SAFETY_BASICS-C` → `SRC-FOOD_SAFETY_BASICS`.

**External check:** FDA guidance specifies different safe internal cooking temperatures for different food categories and time limits for refrigeration; regulatory requirements can vary by product, process and jurisdiction.

**Assessment:** This is a well-bounded meta-claim that resists false universalization. The linked Evidence Use remains generic and does not identify the source's concrete examples. Its caution about applicable rules is appropriate, but the source itself is a consumer-facing U.S. page and does not establish the full set of legal requirements in other jurisdictions.

**Disposition:** Confirmed Evidence Use specificity weakness; preserve the scope caveat and avoid representing the FDA consumer page as a complete regulatory source.

### 4. `CLM_FOOD_SAFETY_CDC_A` — D2 / E2 / B2
**Statement:** CDC says safe cooking requires reaching appropriate internal temperatures and recommends using a food thermometer to verify them.

**Linked records:** `EU_FOOD_SAFETY_CDC_A` → `SRC_FOOD_SAFETY_CDC`.

**External check:** CDC's [Preventing Food Poisoning](https://www.cdc.gov/food-safety/prevention/) states that the only way to know whether food is safely cooked is to use a food thermometer (with a stated exception for certain seafood assessments) and provides category-specific internal temperatures. The source record URI points to this CDC prevention page.

**Assessment:** The Evidence Use is unusually clear about its scope: it explicitly says this CDC evidence supports only the separate CDC claim and is not independent corroboration for the FDA-based claims. This is good evidence discipline. The Source identity, however, is only “Independent institutional reference,” which is less informative than identifying CDC and the page title.

**Disposition:** No claim defect found in this sample. Candidate source-metadata improvement (institution/title), subject to the source schema and correction authorization.

## Batch findings
1. Claims A–C are substantively supported by the FDA page, but all three linked Evidence Use records use the same generic boilerplate. This is a confirmed auditability weakness, not evidence that the claims are false.
2. Claim C's jurisdictional boundary is valuable: a U.S. consumer page should not be represented as exhaustive law for every country, business process or food category.
3. The separate CDC Evidence Use record explicitly limits the source's role and avoids falsely presenting it as independent corroboration for the FDA-based claims. This is a positive example of evidence discipline.
4. The CDC source identity is vague even though the URL is traceable. Improve metadata only through a schema-conformant, finding-specific correction.
5. This is a four-claim purposive sample, not a full slice audit or a complete review of food safety during power outages. Refrigeration failure, discard thresholds and contamination after infrastructure outages require separate review.

## Required follow-up
- Add the three FDA-linked generic Evidence Use descriptions to the finding-specific correction queue and give each one claim-specific source support.
- Consider improving the CDC Source identity to identify CDC and the linked page title, if permitted by current schema conventions.
- Include power-outage food safety and cold-chain failure in the broader high-consequence overlay; do not assume this slice covers those scenarios fully.
- Add/confirm regressions for evidence-description specificity and source metadata.
- Continue full Claim D/E/B census, high-consequence overlay, Human View, Relation audit and independent review.

## Audit boundary
Review artifact only. No corpus records were edited. M13 remains open; this batch does not close any audit phase.
