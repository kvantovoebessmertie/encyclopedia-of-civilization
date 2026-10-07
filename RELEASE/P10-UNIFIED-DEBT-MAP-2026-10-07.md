# P10 UNIFIED DEBT MAP — ITERATION 1

**Date:** 2026-10-07
**Base:** c9eacf6b673efdf8c85e435b79c3fe9a955cebe1

| ID | Scope | Debt | Severity | Status | Required closure |
|---|---|---|---|---|---|
| P10-D01 | comparative-law | Independent evidence source was initially same institutional family | HIGH | CLOSED | Replace corroborating source with genuinely different provenance; re-run CI |
| P10-D02 | international-law | Independent evidence source was initially same UN institutional family | HIGH | CLOSED | Replace corroborating source with genuinely different provenance; re-run CI |
| P10-D03 | civil-society | Independent evidence source was initially same World Bank family | HIGH | CLOSED | Replace corroborating source with genuinely different provenance; re-run CI |
| P10-D04 | taxation | Independent evidence source was initially same OECD family | HIGH | CLOSED | Replace corroborating source with genuinely different provenance; re-run CI |
| P10-D05 | labor-economics | Independent evidence source was initially same ILO family | HIGH | CLOSED | Replace corroborating source with genuinely different provenance; re-run CI |
| P10-D06 | all ten | B/C claims require claim-by-claim mechanism/condition/limitation verification | MEDIUM | OPEN | Full substantive re-audit |
| P10-D07 | all ten | Evidence material/locator specificity requires final verification | MEDIUM | OPEN | Verify claim-to-source fit and material boundaries |
| P10-D08 | all ten | Applicability/uncertainty must be checked at claim/evidence level, not only README level | MEDIUM | OPEN | Final applicability/uncertainty audit |
| P10-D09 | all ten | Cross-slice relations require independent high-value linkage validation | MEDIUM | OPEN | Cross-domain audit; add only justified relations |
| P10-D10 | all ten | Human View/adversarial scenarios not yet formally closed for P10 | HIGH | OPEN | HUA-01–HUA-10 audit and debt closure |
| P10-D11 | release | CI must be re-run after source changes | HIGH | OPEN | Exact-HEAD Reference + Release Gate + Offline 3/3 GREEN |
| P10-D12 | release | CLEAN checkpoint must not be created before substantive and Human View closure | HIGH | OPEN | Final re-audit then CLEAN checkpoint |

## Rule
No P10 closure is permitted while any HIGH debt remains open. A green technical CI alone does not close substantive debt.
