# shelter-basics

Предметный вертикальный срез: shelter-basics.

## Точная структура

13 Records:
- 2 Source;
- 3 Claim;
- 4 Evidence Use;
- 2 Context records (slice Claim context plus target-specific Relation context);
- 1 Scope;
- 1 Relation.

Связки Claim→Evidence Use→Source проверяются отдельным regression test. Relation связывает срез с human-settlement-systems; он не заменяет доказательства для отдельных Claims.

## Текущие источники в canonical records

- Ready.gov — Emergency Preparedness: https://www.ready.gov/
- American Red Cross — Disaster Shelters: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html

Эти два URL требуют точных предметных локаторов; общий портал и shelter finder сами по себе не подтверждают критерии выбора безопасного временного укрытия.

Definition of Done: exact source locators, Context/Scope per applicable Claim, dedicated regression, Human View, package/recovery evidence, full Reference CI and Release Gate.

Граница: базовое справочное покрытие без перехода к индивидуальной рекомендации или опасным строительным процедурам.
