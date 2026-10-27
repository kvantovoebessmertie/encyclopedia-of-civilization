# M13 Batch 42 — Scored row 070: signs of heat illness and escalation

Date: 2026-10-18  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-HEAT-EXHAUSTION-SIGNS@1`  
Evidence Use version: `EU-HEAT-EXHAUSTION-SIGNS@1`  
Source version: `SRC-CDC-EXTREME-HEAT-2026@1`

## Claim under review

> Признаки теплового заболевания могут включать сильное потоотделение, тошноту, головокружение и обморок; при ухудшении симптомов следует незамедлительно получить медицинскую помощь.

## Evidence fit

The canonical Source identifies CDC heat-health guidance:
https://www.cdc.gov/heat-health/about/index.html

The Evidence Use states that CDC lists heavy sweating, nausea and fainting among heat-illness signs and recommends medical care if symptoms worsen. This directly supports much of the Claim. Dizziness is not named in the Evidence Use summary, and no exact CDC section is pinpointed; the full symptom list and escalation language need direct verification.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-HEAT-EXHAUSTION-SIGNS` | 2 | 2 | 1 | **D=2:** symptom recognition and escalation are safety-critical. **E=2:** CDC guidance supports the core warning and escalation, but dizziness and exact wording need pinpoint confirmation. **B=1:** the symptom list and “worsening” threshold are not fully mapped to a specific passage. |

## Disposition

**HOLD pending exact CDC passage verification, symptom-list reconciliation and independent Human View.** Do not treat this as a complete heat-illness diagnostic guide. No canonical record changed.
