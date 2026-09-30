# 018 — Authorship & Contribution

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: CLOSED — SEMANTIC ENFORCEMENT ESTABLISHED FOR REFERENCE CONTOUR  
Дата: 29 сентября 2026 года

## 1. Назначение

Определяет реализацию Авторства и Вклада без смешения с Provenance, Identity, Agent, Source или фактическим происхождением реальности.

## 2. Structural contract

Schema уже требует для `authorship_contribution`:

- `target_ref`;
- `contributor_ref`;
- `contribution`.

Дополнительно допускаются:

- `role`;
- `credit`;
- `responsibility`;
- `rights_ref`.

Это structural conformance.

## 3. Core distinctions

Implementation обязана различать:

- Author ≠ contributor;
- contributor ≠ participant;
- identity ≠ account;
- authorship ≠ provenance;
- authorship of representation ≠ authorship of reality;
- credit ≠ responsibility;
- responsibility ≠ legal liability;
- contribution ≠ ownership;
- editorial contribution ≠ substantive authorship automatically;
- absence of recorded contribution ≠ proof of no contribution.

## 4. Target granularity

Contribution относится к конкретному target.

Target может быть:

- Record;
- Claim;
- Source representation;
- translation;
- revision;
- dataset;
- method;
- software artifact;
- composite work.

Нельзя автоматически переносить contribution одного компонента на весь контейнер.

## 5. Contribution semantics

`contribution` — обязательное значение, но его семантика должна оставаться recoverable.

При необходимости различаются:

- conception;
- data collection;
- analysis;
- writing;
- translation;
- editing;
- review;
- implementation;
- verification;
- curation;
- reconstruction.

Не следует превращать список ролей в универсальный ontology без необходимости.

## 6. Collective / anonymous / pseudonymous

System должна поддерживать:

- collective contributor;
- anonymous attribution;
- pseudonymous attribution;
- disputed attribution;
- unknown attribution.

Нельзя выводить конкретного человека из псевдонима без Identity resolution.

## 7. AI contribution

ИИ может быть contributor/tool/agent в зависимости от конкретной семантики.

Нельзя автоматически делать:

```text
AI tool used
→
AI author
```

или:

```text
AI author
→
human responsibility
```

Они требуют отдельных relations/attributions.

## 8. Rights and responsibility

`rights_ref`, responsibility и credit не являются доказательством друг друга.

Legal rights/lability могут существовать вне epistemic authorship model и не должны выводиться автоматически.

## 9. Historical attribution

Атрибуция может изменяться.

System должна сохранять:

- historical attribution;
- current attribution;
- evidence/basis;
- uncertainty;
- dispute status;
- attribution time.

Позднейшее решение не должно стирать историческое состояние.

## 10. Validator levels

### L1 Schema
Required refs и strings.

### L2 Profile
Role/contribution vocabulary where defined.

### L3 Reference
Contributor/target resolution.

### L4 Semantic
Role distinctions, attribution conflicts, collective/pseudonymous semantics.

### L5 History
Preservation through migration/publication/recovery.

## 11. Negative tests

- отсутствующий contributor_ref → fail;
- отсутствующий target_ref → fail;
- contribution без target не принимается;
- pseudonym не становится person автоматически;
- tool use не становится authorship автоматически;
- credit не становится responsibility;
- authorship не становится provenance;
- отсутствующий contribution не становится доказательством отсутствия вклада;
- disputed attribution не становится confirmed;
- historical attribution не переписывается current attribution.

## 12. Stress tests

A01–A20:

- many contributors;
- collective authorship;
- anonymous/pseudonymous;
- disputed attribution;
- AI-assisted production;
- translation/editing chains;
- shared contribution;
- overlapping roles;
- contribution inheritance;
- component-level attribution;
- migration;
- merge;
- split;
- redaction;
- deleted identity;
- offline recovery;
- historical reassessment;
- conflicting credits;
- rights references;
- deterministic replay.

## 13. Enforcement matrix

| Rule | Owner | Status |
|---|---|---|
| target/contributor/contribution | Schema | ENFORCED |
| reference resolution | L3 | PARTIAL |
| role semantics | L2/L4 | MAPPED |
| collective/pseudonymous attribution | L4 | DEFERRED |
| AI attribution | L4 | DEFERRED |
| historical attribution | L5 | PARTIAL |
| rights/responsibility distinction | L4 | DEFERRED |
| component-level attribution | L4 | DEFERRED |
| attribution conflict | L4 | DEFERRED |

## 14. Conformance

Structural: **PASS**  
Reference/history: **PARTIAL**  
Semantic: **LIMITED**  
Transformation/history: **LIMITED**

## 15. Enforcement debt

1. role vocabulary registry;
2. attribution conflict resolver;
3. collective/pseudonymous model;
4. AI contribution fixtures;
5. component-level attribution;
6. rights/responsibility boundary tests;
7. historical attribution integration;
8. migration/publication preservation.

## 16. Invariants

1. Contribution is not automatically authorship.
2. Authorship is not provenance.
3. Credit is not responsibility.
4. Tool use is not authorship.
5. Pseudonym is not resolved identity.
6. Missing contribution is not no contribution.
7. Historical attribution is not current attribution.
8. Legal rights are not inferred from epistemic attribution.
9. Resolver does not invent contributors.
10. Attribution does not prove truth.

## 17. Статус

**018 — CLOSED — SEMANTIC ENFORCEMENT ESTABLISHED FOR REFERENCE CONTOUR.**


### Semantic closure

Role, pseudonymous attribution, conflict and historical attribution boundaries are enforced when represented. Tool use, credit and provenance are not inferred into authorship semantics.
