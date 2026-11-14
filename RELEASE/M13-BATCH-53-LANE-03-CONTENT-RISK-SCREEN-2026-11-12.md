# M13 Batch 53 — Lane 03 content-based risk screen

Date: 2026-11-12  
Queue source revision: `33ef97e7ba6a9e91aebaee198cfead532faa4185`  
Scope: 20 exact Claim statements in lane 03. Routing screen only; not source-fit adjudication, D/E/B scoring, specialist approval, or release clearance.

## Risk routing

| Claim IDs | Route | Rationale |
|---|---|---|
| `CLM-PHYSIOLOGY_OF_EXERCISE_BASICS-A/B/C` | ELEVATED — health/physical activity | Statements concern exercise dose parameters, aerobic fitness and resistance exercise. They may be converted into health or training recommendations. Require exercise-physiology review and ensure no individual prescription is inferred from these general statements. |
| `CLM-PLANT_PATHOLOGY_BASICS-C` | ELEVATED — agriculture/plant health | A disciplinary-scope statement rather than treatment advice, but it sits in a crop-health domain. Keep separate from pesticide, diagnosis or treatment guidance; specialist review is required before operational recommendations are added. |
| `CLM-PAYMENT_SYSTEMS_BASICS-A` | ELEVATED — financial infrastructure | The statement describes mechanisms for transferring funds. It is broad and not itself operational advice, but the domain has financial, legal and resilience implications. Require payments-domain review before extending into settlement, custody, clearing or regulatory claims. |
| `CLM-OPTIMIZATION_BASICS-C` | MODERATE — decision support | The claim warns that optimization results depend on model assumptions and constraints. Misapplication could affect consequential decisions; review examples and avoid universal claims. |
| `CLM-PHILOSOPHY_OF_LANGUAGE_BASICS-A/C` | LOW direct consequence — conceptual | General disciplinary and theory distinctions; check source fit and avoid presenting contested philosophical positions as settled empirical facts. |
| `CLM-PHILOSOPHY_OF_MATHEMATICS_BASICS-A/B/C` | LOW direct consequence — conceptual/epistemic | General philosophical distinctions. Preserve the distinction between mathematical proof, empirical support and philosophical interpretation. |
| `CLM-PHILOSOPHY_OF_MIND_BASICS-A/B` | LOW direct consequence — conceptual/epistemic | General philosophical claims about mental and physical states. Do not imply that the claims settle neuroscience or clinical questions. |
| `CLM-PHILOSOPHY_OF_SCIENCE_BASICS-B/C` | MODERATE — scientific interpretation | These claims frame theory, models, evidence and explanatory scope. Errors can propagate into evidence evaluation; require methodological/editorial review. |
| `CLM-PAPERMAKING_BASICS-B/C` | LOW direct consequence — craft process | Basic fibre preparation and sheet-forming process descriptions. If later converted into chemical, machinery or occupational-safety instructions, those require a separate safety screen. |
| `CLM-PLANETARY_SCIENCE_BASICS-A/B/C` | LOW direct consequence — foundational science | General disciplinary and research-method statements; retain distinctions between observation, mission data, returned samples and inference. |

## Disposition

- Claim statements screened: 20/20.
- Elevated routing: 5 (3 exercise physiology, 1 plant pathology, 1 payment systems).
- Moderate routing: 3 (optimization, 2 philosophy of science).
- Low direct-consequence routing: 12 (2 philosophy of language, 3 philosophy of mathematics, 2 philosophy of mind, 2 papermaking, 3 planetary science).
- D/E/B scores assigned: 0.
- Claims accepted or release-cleared: 0.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- Specialist review completed: 0.
- Lane status: RISK SCREEN COMPLETE FOR ROUTING; SOURCE-PASSAGE REVIEW AND SCORING HOLD.

## Required next work

1. Inspect the Claim → Evidence Use → Source chain and exact passages for all 20.
2. Prioritize exercise physiology, payment systems and plant pathology for domain-specific review.
3. Keep any exercise advice general and evidence-scoped; do not infer individual training prescriptions.
4. Do not infer payment-system legal, settlement or custody rules from a general definition.
5. Keep all Claims HOLD until exact source passages and D/E/B assessment are documented.
