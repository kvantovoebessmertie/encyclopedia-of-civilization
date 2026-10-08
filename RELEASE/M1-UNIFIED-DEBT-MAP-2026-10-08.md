# M1 Unified Debt Map — 2026-10-08

Status: **CLOSED — all substantive M1 findings re-audited PASS**

Audit source: `RELEASE/M1-SUBSTANTIVE-AUDIT-2026-10-08.md`.

## Confirmed debt

| ID | Slice | Debt | Priority | Closure evidence |
|---|---|---|---|---|
| M1-01 | probability-basics | insufficient standalone model/assumption boundary and single-source evidence track | P1 | claim/context + independent Evidence Use |
| M1-02 | ratios-and-percentages | insufficient interpretation/applicability boundary and single-source evidence track | P1 | claim/context + independent Evidence Use |
| M1-03 | seed-storage-basics | insufficient crop/seed applicability boundary and single-source evidence track | P1 | boundary + independent agricultural evidence |
| M1-04 | si-units-basics | insufficient measurement-accuracy/applicability boundary and single-source evidence track | P1 | boundary + independent metrology evidence |
| M1-05 | time-standard-basics | insufficient UTC/reference-time versus local-civil-time boundary and single-source evidence track | P1 | boundary + independent authoritative evidence |
| M1-06 | water | single-source support for high-consequence emergency guidance; requires independent claim-specific corroboration and adversarial verification | P0 | independent source/Evidence Use + Human View PASS |

## Relation debt

No confirmed Relation defect. Candidate links remain under semantic review and must not be added for metric reasons.

## Documentation / regression debt

After content corrections, synchronize affected READMEs, coverage counts, regression contracts and any cross-slice audit metadata. These are closure tasks, not pre-existing defects.

## Closure rule

All six substantive debts were corrected and re-audited PASS. Evidence Independence and Human View audits are PASS. Technical closure remains conditional on the final exact-head 3/3 CI and dedicated CLEAN checkpoint.
