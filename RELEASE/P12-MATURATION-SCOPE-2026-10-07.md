# P12 — MATURATION SCOPE: RETROACTIVE P2–P9 MATURITY VERIFICATION

**Дата:** 2026-10-07  
**Protected baseline:** P11 CLEAN — `d612f15847b6adbd3265e2902a840f995a04c8b7`  
**Baseline:** 478 vertical slices / 4565 records / 19 record types

## Цель

Закрыть ретроактивный audit debt, выявленный в `P2-P9-MATURITY-GAP-SCAN-2026-10-07.md`, не переоткрывая исторические волны как содержательные этапы.

P12 проверяет только подтверждаемые зрелостные границы текущего дерева:

1. MG-01 — claim-specific Evidence Use material-boundary verification;
2. MG-02 — Human View/adversarial consistency verification;
3. MG-03 — current global Relation count vs dedicated cross-slice Relation reconciliation.

## Архитектурная граница

P12 не создаёт новые Record types и не требует массовой переписи P2–P9.

Исторические CLEAN checkpoint не отменяются. Исправляются только фактически подтверждённые дефекты текущего дерева.

## Scope

### MG-01 — Evidence Use

Проверить приоритетно высококонцептуальные и ранее исправлявшиеся кластеры P2–P9:

- каждая Evidence Use привязана к конкретному Claim;
- material boundary действительно описывает то, что источник поддерживает;
- источник не используется как доказательство утверждений, которых он не покрывает;
- независимые источники не дублируются искусственно;
- отсутствие locator само по себе не считается дефектом, если семантическая граница достаточна по STANDARD/004.

### MG-02 — Human View / adversarial

Применить единый P10-сценарий:

- не превращается ли общее знание в индивидуальную рекомендацию;
- не превращается ли историческое описание в текущую инструкцию;
- видны ли условия применимости;
- различаются ли известное, неизвестное и непроверенное;
- сохраняются ли предупреждения и границы компетентности;
- не создаёт ли Human View ложного впечатления большей достоверности.

Особое внимание — safety, health, legal, financial, infrastructure и other high-consequence material.

### MG-03 — Relation reconciliation

Единым проходом текущего дерева установить:

- общее количество Relation records;
- количество dedicated cross-slice Relations;
- валидность каждой Relation;
- отсутствие ошибочного смешения domain Relation и cross-slice baseline;
- отсутствие искусственных Relations без материальной зависимости.

## Definition of Done

1. P2–P9 не переоткрыты как исторические волны.
2. Подтверждённые дефекты отделены от audit-only gaps.
3. Все подтверждённые долги исправлены.
4. Повторный P12 audit: 0 blocking, 0 confirmed substantive debt.
5. Human View/adversarial: 0 unresolved findings.
6. Relation reconciliation: 0 unexplained discrepancy.
7. Coverage/README/registry synchronized.
8. Reference + Release Gate + Offline = GREEN на exact checkpoint HEAD.
9. Создан отдельный P12 CLEAN checkpoint.

## Порядок

Protected P11 CLEAN → MG-01 → MG-02 → MG-03 → unified debt map → исправление всех подтверждённых долгов → re-audit → documentation/coverage synchronization → full CI → P12 CLEAN.

## Explicit exclusions

- no new vertical slices solely for P12;
- no new Record types;
- no mass rewrite of historical content;
- no artificial Relations;
- no reopening of closed waves without a verified current-tree defect;
- no declaration of factual truth based only on conformance or CI.

## Success condition

P12 закрыт только после доказанного отсутствия подтверждённого ретроактивного maturity debt и независимого 3/3 GREEN на финальном CLEAN checkpoint.
