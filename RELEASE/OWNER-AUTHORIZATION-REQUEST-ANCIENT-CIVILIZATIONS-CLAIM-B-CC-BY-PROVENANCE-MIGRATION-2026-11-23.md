# Запрос владельцу — ограниченная provenance migration для Ancient Civilizations Claim B

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: REQUEST ONLY — никакие canonical changes этим документом не разрешены.

## 1. Зачем требуется отдельное решение

В slice ancient-civilizations-basics уже выполнен owner-approved Package A: добавлены шесть CC BY 4.0 Source records и шесть соответствующих Evidence Use records с точными article locators. Все эти записи остаются HOLD.

Однако текущий Claim B@1 имеет provenance.created_from → SRC-ANCIENT_CIVILIZATIONS_BASICS@1. Этот Source указывает на OpenStax *World History Volume 1, to 1500*, §3.1. Для этого конкретного издания OpenStax указывает:
- CC BY-NC-SA 4.0, а не CC BY 4.0;
- запрет использования книги для обучения LLM или иного ingestion в LLM/generative-AI offerings без предварительного письменного разрешения.

Это ограничение подтверждено на OpenStax book pages:
- https://openstax.org/books/world-history-volume-1/pages/1-introduction
- https://openstax.org/books/world-history-volume-1/pages/preface

Selection-aware builder рекурсивно собирает exact-version references во всех полях выбранной записи, включая provenance.created_from. Поэтому если выбрать Claim B@1, manifest обязан включить старый OpenStax Source@1 как зависимость. Одного наличия трёх новых CC BY 4.0 Evidence Use tracks недостаточно, чтобы исключить эту зависимость.

## 2. Почему Claim B выбран для отдельного узкого решения

Текущая формулировка Claim B:

> В ряде регионов развитие земледелия было связано с изменениями в характере поселений и демографии, но направление и сила этих связей различались по времени и месту.

У Claim B уже есть три owner-approved CC BY 4.0 evidence tracks:

1. Lesure et al. (2021), Mesoamerica and Southwestern North America — сравнительные макрорегиональные данные о длительном и пространственно неоднородном сельскохозяйственно-демографическом переходе.
2. Crema et al. (2024), prehistoric Japan — регионально различающиеся демографические реакции на распространение рисового земледелия, с ограничениями радиоуглеродной/поселенческой выборки.
3. Neil et al. (2016), Early Neolithic Britain — изотопные данные о мобильности фермерских сообществ; это ограничивает упрощённое отождествление земледелия с немедленной и универсальной оседлостью.

Три работы используют разные регионы и исследовательские методы. Вместе они соответствуют осторожной формулировке Claim B, которая прямо ограничивает утверждение несколькими регионами и признаёт различия по времени и месту.

Claim A и Claim C здесь не предлагаются к миграции: их новые case-study источники требуют отдельного решения о достаточности для более широких формулировок. Context/Scope текущего slice таргетируют только Claim A и не должны распространяться на Claim B.

## 3. Предлагаемая bounded authorization

Если владелец одобрит этот точный scope, разрешить только следующие операции.

### A. Version Claim B

Создать CLM-ANCIENT_CIVILIZATIONS_BASICS-B@2:
- сохранить statement побуквенно без изменений;
- сохранить claim_type без изменений;
- сохранить record_type, type_version и schema;
- изменить только provenance.created_from, чтобы текущая версия Claim B была обоснована тремя уже существующими CC BY 4.0 Sources:
  - SRC-LESURE-AGRICULTURAL-DEMOGRAPHIC-TRANSITION@1;
  - SRC-CREMA-RICE-FARMING-JAPAN-DEMOGRAPHY@1;
  - SRC-NEIL-BRITAIN-NEOLITHIC-MOBILITY@1;
- сохранить Claim B@1 как историческую версию; не перезаписывать и не удалять её.

Смысл операции: версия @2 будет новой source-grounded редакцией той же формулировки на основе новых разрешённых evidence tracks. Историческая версия @1 и её происхождение останутся сохранены.

### B. Version three Evidence Use records

Создать:
- EU-ANCIENT_CIVILIZATIONS_BASICS-B-LESURE@2;
- EU-ANCIENT_CIVILIZATIONS_BASICS-B-CREMA@2;
- EU-ANCIENT_CIVILIZATIONS_BASICS-B-NEIL@2.

Для каждого:
- изменить только claim_ref с CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1 на @2;
- сохранить source_ref на соответствующий Source@1;
- сохранить evidence_role, description, locator и provenance;
- не менять смысл или границы доказательной поддержки.

Существующие EU records @1 остаются историческими и неизменными.

### C. Tests and registers

Разрешить только:
- точечные assertions в двух существующих ancient-civilizations slice regression tests для Claim B@2, трёх EU@2 и точных Source@1 references;
- update README slice только для отражения нового exact-version lineage и того, что Claim B@2 опирается на три названные CC BY 4.0 статьи;
- update Part II exact-version master: добавить новые Claim B@2 и три EU@2 как exact-version rows, все HOLD; сохранить все старые версии;
- update RELEASE/EDITORIAL-CORRECTION.json, чтобы записать именно это разрешение;
- remediation report с diff, exact record IDs/versions, hashes, source pinpoints и test results.

Не менять CONTENT-COVERAGE.json: количество физических canonical record files не увеличивается. Не менять Part II slice denominator или candidate membership, кроме точного учёта новых version rows в master согласно его compound key record_id@version.

## 4. Что явно запрещено

- Не менять текст Claim B.
- Не менять Claims A/C, любые Source records, Context, Scope, Relations или другие Evidence Use.
- Не менять generic EU-ANCIENT_CIVILIZATIONS_BASICS-B@1 или исходный SRC-ANCIENT_CIVILIZATIONS_BASICS@1.
- Не менять publication_status, completion_status, D/E/B, HOLD/INCLUDE/EXCLUDE.
- Не создавать first-edition allowlist и не включать Claim B в публичный выпуск автоматически.
- Не объявлять весь ancient-civilizations slice очищенным по правам: разрешение касается только трёх конкретных CC BY 4.0 article tracks и их factual paraphrase/attribution.
- Не копировать текст, таблицы, изображения, карты или другие expressive assets статей.
- Не менять main, PR base, merge, deploy или publish.

## 5. Ожидаемая dependency closure после разрешённой миграции

Для будущего exact-version manifest, если Claim B@2 будет отдельно допущен, его минимальная Claim/Evidence/Source closure будет:

| Record | Version | Роль |
|---|---:|---|
| CLM-ANCIENT_CIVILIZATIONS_BASICS-B | 2 | Claim |
| EU-ANCIENT_CIVILIZATIONS_BASICS-B-LESURE | 2 | Evidence Use |
| EU-ANCIENT_CIVILIZATIONS_BASICS-B-CREMA | 2 | Evidence Use |
| EU-ANCIENT_CIVILIZATIONS_BASICS-B-NEIL | 2 | Evidence Use |
| SRC-LESURE-AGRICULTURAL-DEMOGRAPHIC-TRANSITION | 1 | CC BY 4.0 Source |
| SRC-CREMA-RICE-FARMING-JAPAN-DEMOGRAPHY | 1 | CC BY 4.0 Source |
| SRC-NEIL-BRITAIN-NEOLITHIC-MOBILITY | 1 | CC BY 4.0 Source |

Это только минимальная доказательная closure. Решение INCLUDE, rights review, independent historical/editorial review, Human View и owner release approval остаются отдельными gates.

## 6. Условия принятия

- Exact current HEAD и все семь canonical input records повторно fetched перед записью.
- Существующие @1 versions сохраняются без изменений.
- Все три EU@2 точно указывают на Claim B@2 и исходные CC BY 4.0 Source@1.
- Claim B@2 provenance указывает ровно на три approved Sources.
- Context/Scope Claim A не отображаются как будто они применяются к Claim B.
- Обе targeted tests проходят; затем все четыре required PR workflows должны пройти на одном immutable HEAD.
- Все записи остаются HOLD.

## 7. Решение владельца

Требуется явное подтверждение именно этого ограниченного пакета:

- **APPROVE** — разрешить операции A, B и C строго в описанных границах.
- **REJECT / DEFER** — ничего не менять; все текущие версии и HOLD остаются как есть.

Ни один вариант не означает INCLUDE, публикацию, merge или deployment.
