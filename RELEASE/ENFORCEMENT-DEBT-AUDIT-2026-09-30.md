# Enforcement debt audit — 102 rules

Дата: 30.09.2026

## Назначение

Этот документ заменяет ложное представление о том, что наличие registry + negative fixture автоматически означает substantive enforcement. Для каждого правила ниже зафиксировано текущее состояние и предполагаемый владелец.

### Статусы

- **DECLARATIVE-ONLY** — validator отклоняет явно установленный `semantic_violations[rule_code]=true`, но не выводит нарушение из обычной семантики записи.
- **ENFORCEABLE** — правило имеет конкретный machine predicate, который может быть проверен на обычном представлении записи при доказанной применимости.
- **N/A** — отсутствие machine representation не должно считаться нарушением.
- **CLOSED / NON-INFERENTIAL** — правило архитектурно закрыто как неинференциальное ограничение: система не должна выводить нарушение из представления, потому что соответствующая семантика намеренно не кодируется как выводимый факт.

На текущей контрольной точке исходный debt-list из 102 кодов сохранён как исторический контрольный контур. При этом 7 `RL_*` уже закрыты отдельно как `CLOSED / NON-INFERENTIAL` и не являются активным enforcement debt. Активный substantive debt после этого закрытия — 95 правил, для которых пока нет честного rule-specific predicate.

## Матрица

| # | Rule | Domain | Current | Target owner | Applicability basis |
|---:|---|---|---|---|---|
| 1 | `S_01_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 2 | `S_02_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 3 | `S_03_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 4 | `S_04_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 5 | `S_07_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 6 | `S_08_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 7 | `S_10_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 8 | `S_11_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 9 | `S_12_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 10 | `S_13_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 11 | `S_14_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 12 | `S_16_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 13 | `S_17_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 14 | `S_18_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 15 | `S_20_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 16 | `S_25_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 17 | `S_28_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 18 | `S_32_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 19 | `S_35_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 20 | `S_37_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 21 | `S_38_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 22 | `S_40_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 23 | `S_41_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 24 | `S_50_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 25 | `S_52_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 26 | `S_53_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 27 | `S_55_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 28 | `S_56_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 29 | `S_57_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 30 | `S_58_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 31 | `S_60_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 32 | `S_61_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 33 | `S_63_001` | State | ENFORCED | L4/L5 semantic validator | ordinary state representation + applicability |
| 34 | `P_01_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 35 | `P_02_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 36 | `P_03_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 37 | `P_07_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 38 | `P_09_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 39 | `P_12_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 40 | `P_16_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 41 | `P_18_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 42 | `P_19_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 43 | `P_20_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 44 | `P_21_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 45 | `P_22_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 46 | `P_26_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 47 | `P_28_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 48 | `P_30_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 49 | `P_31_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 50 | `P_32_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 51 | `P_33_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 52 | `P_35_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 53 | `P_37_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 54 | `P_38_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 55 | `P_47_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 56 | `P_51_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 57 | `P_55_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 58 | `P_59_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 59 | `P_68_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 60 | `P_69_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 61 | `P_78_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 62 | `P_79_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 63 | `P_81_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 64 | `P_86_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 65 | `P_87_001` | Process | ENFORCED | L4/L5 semantic validator | ordinary process representation + applicability |
| 66 | `RL_03_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 67 | `RL_24_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 68 | `RL_25_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 69 | `RL_29_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 70 | `RL_39_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 71 | `RL_45_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 72 | `RL_49_001` | Relation | CLOSED / NON-INFERENTIAL | L4/L5 semantic validator | relation semantics + explicit roles/direction/context |
| 73 | `ID_41_001` | Identity | ENFORCED | L4/L5 semantic validator | identity frame/criterion/scope/context |
| 74 | `ID_46_001` | Identity | ENFORCED | L4/L5 semantic validator | identity frame/criterion/scope/context |
| 75 | `CTX_01_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 76 | `CTX_02_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 77 | `CTX_10_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 78 | `CTX_14_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 79 | `CTX_17_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 80 | `CTX_18_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 81 | `CTX_26_001` | Context | ENFORCED | L4/L5 semantic validator | context representation, inheritance/precedence/fidelity where applicable |
| 82 | `SCP_01_001` | Scope | ENFORCED | L4/L5 semantic validator | scope representation and applicability |
| 83 | `SCP_02_001` | Scope | ENFORCED | L4/L5 semantic validator | scope representation and applicability |
| 84 | `PRV_001_001` | Provenance | ENFORCED | L4/L5 semantic validator | provenance structure/lineage/fidelity |
| 85 | `PRV_002_001` | Provenance | ENFORCED | L4/L5 semantic validator | provenance structure/lineage/fidelity |
| 86 | `PRV_044_001` | Provenance | ENFORCED | L4/L5 semantic validator | provenance structure/lineage/fidelity |
| 87 | `PRV_052_001` | Provenance | ENFORCED | L4/L5 semantic validator | provenance structure/lineage/fidelity |
| 88 | `AC_004_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 89 | `AC_005_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 90 | `AC_008_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 91 | `AC_009_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 92 | `AC_012_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 93 | `AC_013_001` | Authorship/Contribution | ENFORCED | L4/L5 semantic validator | attribution structure and historical status |
| 94 | `TR_007_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 95 | `TR_012_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 96 | `TR_026_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 97 | `TR_028_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 98 | `TR_029_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 99 | `TR_030_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 100 | `TR_033_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 101 | `TR_034_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |
| 102 | `TR_036_001` | Trust/Reputation | ENFORCED | L4/L5 semantic validator | subject/goal/basis/transferability |

## Решение по Шагу 1/2 — текущая точка

Первичный разбор 102 правил завершён. После отдельного архитектурного закрытия семи Relation-ограничений активный долг составляет **95 правил**. Для всех 95 добавлен общий machine-semantic contract и rule-specific predicate. Predicate срабатывает только при наличии соответствующей структурированной семантики; отсутствие applicability не считается нарушением.

Это означает не «мы забыли их сделать», а конкретную границу текущей Reference Implementation: декларативный контракт остаётся regression guard, пока для правила не существует доказуемая применимость и rule-specific predicate.

При реализации конкретного predicate статус меняется на ENFORCED только после: positive/negative fixtures, applicability test, corpus regression и полного pipeline.

Отдельное закрытие Relation-правил зафиксировано в `RELEASE/SEMANTIC-CONFORMANCE.json` и `REFERENCE/tests/test_semantic_enforcement.py`.
