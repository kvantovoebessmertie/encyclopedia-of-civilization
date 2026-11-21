# M13 Batch 13 — source-fit review checkpoint (rows 555–562)

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **partial review; Batch 13 not complete**

Scores use the M13 protocol: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline. They are reviewer judgments for triage. No canonical JSON changed.

## Food security basics

### 1. `CLM-FOOD_SECURITY_BASICS-A` — **D1 / E1 / B3**

**Claim:** Food security includes physical and economic access to sufficient, safe, nutritious food. (The record appends the slice slug in parentheses.)

**Source check:** The referenced FAO handbook defines food security as all people, at all times, having physical and economic access to sufficient, safe, nutritious food for an active and healthy life (section 1.4, paragraph 56 on the official page: https://www.fao.org/4/x8622e/x8622e04.htm). The core proposition is directly supported. The Evidence Use says only that the handbook is used to represent the statement “without going beyond” the material; it does not identify section 1.4 or quote the definition, so E remains 1 rather than 2.

**Assessment/disposition:** A precise definition but no explanatory mechanism (D1); the definition itself is appropriately bounded (B3). Source fit is strong, traceability in the stored EU is weak. Add a section-level locator and remove the trailing editorial slice slug from the user-facing Claim text after authorized editorial review.

### 2. `CLM-FOOD_SECURITY_BASICS-B` — **D2 / E1 / B2**

**Claim:** Food-security assessment considers availability and stability of food supplies alongside access.

**Source check:** The FAO handbook explicitly connects its definition to availability of staple foods, stability of supplies, access for all, and biological utilization (section 1.4, paragraph 57). It also discusses forecasting across four areas (section 2, paragraphs 59–75). This supports the core proposition. The linked EU remains generic and lacks a pinpoint (E1).

**Assessment/disposition:** This adds useful conceptual distinctions among dimensions of food security (D2). It presents three dimensions without implying the list is complete, but does not mention biological utilization (B2). Consider naming it as a non-exhaustive triad or include the fourth dimension when that is the intended framework.

### 3. `CLM-FOOD_SECURITY_BASICS-C` — **D2 / E1 / B2**

**Claim:** Information systems and early warning help understand food-security conditions and support decision-making.

**Source check:** The FAO handbook explains that cross-analysis of information from different food-security areas supports evaluation, forecasting, and crisis prevention (section 1.3, paragraphs 44–49); it describes forecasts, warning signals, and an updated dashboard intended to steer efforts and inform decision-makers (section 2, paragraphs 59–68). The source fits the statement, but the stored EU does not identify these passages (E1).

**Assessment/disposition:** The statement links monitoring and early warning to decision support, which gives it some explanatory value (D2). It does not state that forecasts are uncertain or that information systems support rather than replace decisions; boundaries are moderate (B2). Add section-level pinpoints and retain the distinction between information and decision-making.

### 4. `CLM-FOOD_SECURITY_BASICS-D` — **D1 / E2 / B3**

**Claim:** Household food security means all members have access at all times to enough food for an active, healthy life.

**Source check:** The linked USDA Economic Research Service page states essentially this definition verbatim and adds minimum elements: ready availability of nutritionally adequate and safe foods, and assured ability to acquire acceptable foods in socially acceptable ways (https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-us/measurement, “What Is Food Security?”). The stored EU specifically identifies USDA ERS and the stated definition, which is claim-specific enough for E2, although it would still benefit from a section locator.

**Assessment/disposition:** A concise definition rather than an explanation (D1), with clear household-level and all-members/all-times boundaries (B3). If the intended scope is U.S. measurement, explicitly label it as the USDA/ERS definition rather than presenting it as the only global definition.

## Food systems basics

### 5. `CLM-FOOD_SYSTEMS-A` — **D2 / E1 / B2**

**Claim:** A food system spans connected processes of production, processing, distribution, consumption, and disposal.

**Source check:** FAO’s Agrifood Systems page states that systems tie together people, activities, investments, and choices involved in producing and delivering food, and enumerates growing, harvesting, processing, packaging, transport, distribution, trade, purchase, preparation, eating, and disposal (https://www.fao.org/food-systems/en, “Agrifood Systems”). The proposition is well aligned, but the stored EU only names the source and gives no passage locator (E1).

**Assessment/disposition:** The lifecycle framing conveys meaningful breadth (D2). “Distribution” and “disposal” are clear, but “food system” can include non-food agricultural products and institutional choices as well; the claim is a simplified introductory scope (B2). Add a pinpoint and make the intended simplification explicit if needed.

### 6. `CLM-FOOD_SYSTEMS-B` — **D1 / E1 / B2**

**Claim:** Food systems include people, activities, investments, and decisions associated with producing and delivering food.

**Source check:** This closely follows the FAO page’s opening definition (same URL, “Agrifood Systems”). The EU still lacks a precise locator and is boilerplate in effect (E1).

**Assessment/disposition:** The sentence names system components but does little to explain their interactions (D1). It is appropriately broad but does not make the difference between a food system and an agrifood system explicit (B2). Consider merging with or distinguishing it from Claim A after semantic-duplicate review; both use the same FAO source and overlap substantially.

### 7. `CLM-FOOD_SYSTEMS-C` — **D2 / E1 / B2**

**Claim:** Food-system analysis needs to consider connections among natural resources, technology, trade, food access, and other links in the chain.

**Source check:** FAO’s page supports a systems view linking people, activities, investments, and choices across the lifecycle, but the exact set “natural resources, technologies, trade, access to food” is not explicitly enumerated on the page’s visible introductory section. The EU is generic (E1).

**Assessment/disposition:** The relational framing is more explanatory than a simple list of stages (D2), and “other links” indicates non-exhaustiveness (B2). Source-fit is partial: add specific evidence for natural resources and access, or narrow the proposition to what the FAO page directly says. Review semantic overlap with A/B.

### 8. `CLM-FOOD_SYSTEMS-D` — **D2 / E1 / B2**

**Claim:** Food systems include not only production but storage, processing, distribution, transport, logistics, and retail.

**Source check:** The linked Source identifies a World Bank publication, *The Future of Food: Shaping the Global Food System to Deliver Improved Nutrition and Health* (https://www.worldbank.org/en/topic/agriculture/publication/the-future-of-food-shaping-the-global-food-system-to-deliver-improved-nutrition-and-health). The broad topic is relevant, but the stored EU only states that the World Bank is being used and does not identify the passage supporting each listed stage (E1).

**Assessment/disposition:** The statement broadens the reader’s view beyond production and includes several supply-chain stages (D2). It may still omit other relevant system components and has no explicit boundary beyond the list (B2). Pinpoint the relevant World Bank passage and consider overlap with Claim A.

## Checkpoint totals

- New Claims reviewed in this checkpoint: **8**.
- Batch 13 total with provisional D/E/B review recorded: **15 of 100**.
- Remaining candidates without individual D/E/B review: **85**.
- Semantic overlap candidates: `CLM-FOOD_SYSTEMS-A/B/C` (adjudication still pending; no records merged).
- Canonical records changed: **0**.
- Batch 13 complete: **NO**.
