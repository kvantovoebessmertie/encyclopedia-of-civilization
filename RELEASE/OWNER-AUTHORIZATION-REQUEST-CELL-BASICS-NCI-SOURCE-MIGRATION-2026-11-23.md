# Запрос владельцу — bounded Source migration для Cell Basics Claim A

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: REQUEST ONLY — canonical changes не разрешены до явного approval.

## 1. Причина запроса

Текущий Claim:

- CLM-CELL_BASICS-A@1
- statement: «Клетка является основной структурной и функциональной единицей живых организмов.»
- текущая provenance.created_from → SRC-CELL_BASICS@1 (OpenStax Biology 2e)
- EU-CELL_BASICS-A@1 → SRC-CELL_BASICS@1
- CTX-CELL_BASICS@1 и SCP-CELL_BASICS@1 target Claim A@1

OpenStax Biology 2e имеет CC BY-NC-SA 4.0 и отдельное ограничение на LLM/generative-AI ingestion без предварительного письменного разрешения. Поэтому его нельзя считать совместимым с потенциальной CC BY-only или коммерческой моделью первой редакции.

## 2. Проверенная альтернатива — National Cancer Institute

NCI Dictionary of Cancer Terms, entry “cell”:
https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cell

Вводное определение описывает клетку как наименьшую единицу, способную самостоятельно жить и составляющую все живые организмы; далее названы основные части клетки и функции мембраны, ядра и цитоплазмы. Это поддерживает структурный и функциональный смысл Claim A.

Дополнительные NCI SEER Training locators:
- Cell Structure: https://training.seer.cancer.gov/anatomy/cells_tissues_membranes/cells/structure.html
- Cell Function: https://training.seer.cancer.gov/anatomy/cells_tissues_membranes/cells/function.html

NCI Reuse of Information policy:
https://www.cancer.gov/policies/copyright-reuse

Политика NCI указывает, что, если не отмечено иное, текст в NCI products не защищён copyright и может повторно использоваться без разрешения при указании NCI как источника и ссылке на оригинальный продукт. Графика может быть third-party copyrighted; NCI logo и PDQ trademark имеют отдельные ограничения. NCI допускает переводы при соблюдении требований, включая disclaimer об отсутствии endorsement NCI.

Для этой Энциклопедии предлагается использовать только независимо сформулированный factual paraphrase и ссылки. Не копировать изображения, аудио, логотипы, макет или другие assets. Если редакция будет переводить текст NCI напрямую, выполнить все условия NCI для перевода; предпочтителен самостоятельный русский factual paraphrase.

## 3. Предлагаемая bounded authorization

Если владелец одобрит точный scope, разрешить только:

### A. Новый Source

Создать:
- SRC-NCI-CELL-DICTIONARY@1

Source identity: National Cancer Institute, NCI Dictionary of Cancer Terms, entry “cell”.  
External ref: точный URL entry “cell”.  
Preservation: сохранять title, page identity, retrieval date и NCI reuse policy reference.  
Не включать текст статьи, изображения, audio, logo или page layout.

### B. Новая версия Claim A

Создать CLM-CELL_BASICS-A@2:
- statement сохранить побуквенно;
- claim_type сохранить;
- record_type, type_version, schema сохранить;
- изменить только provenance.created_from на SRC-NCI-CELL-DICTIONARY@1;
- сохранить Claim A@1 как историческую версию без перезаписи.

Смысл: Claim A@2 — новая source-grounded версия той же формулировки; прежнее происхождение и OpenStax dependency остаются в исторической версии @1.

### C. Новый Evidence Use

Создать EU-CELL_BASICS-A-NCI@1:
- claim_ref → CLM-CELL_BASICS-A@2;
- source_ref → SRC-NCI-CELL-DICTIONARY@1;
- evidence_role = supports;
- material.locator → NCI Dictionary entry “cell” и точные подразделы определения/частей клетки;
- material.description → краткая независимая формулировка границы поддержки: базовая единица, состав клетки, функции мембраны/ядра/цитоплазмы;
- не копировать текст NCI.

### D. Context and Scope

Создать:
- CTX-CELL_BASICS@2, target_ref → Claim A@2;
- SCP-CELL_BASICS@2, target_ref → Claim A@2.

Сохранить смысл существующих Context/Scope без расширения. Версии @1 остаются историческими и по-прежнему target Claim A@1.

### E. Tests and registers

Разрешить:
- обновить только cell-basics slice README и targeted tests для Claim A@2 / EU-NCI@1 / Source@1 / Context@2 / Scope@2;
- update Part II exact-version master с новыми exact-version rows, все HOLD;
- update RELEASE/EDITORIAL-CORRECTION.json для фиксации этого конкретного разрешения;
- подготовить bounded remediation report с diff, hashes, exact locators, NCI reuse-policy citation и test results.

Не менять CONTENT-COVERAGE.json: физическое число canonical files увеличивается только на два новых ID (Source и EU), а Claim/Context/Scope versions сохраняются в тех же record files. Проверить текущий manifest semantics перед изменением coverage; не менять counts по предположению.

## 4. Явно запрещено

- Не менять statement Claim A.
- Не менять Claims B/C и их Evidence Use.
- Не удалять и не переписывать OpenStax Source/EU@1.
- Не изменять D/E/B, publication_status, completion_status, HOLD/INCLUDE/EXCLUDE.
- Не создавать production allowlist и не публиковать Claim A автоматически.
- Не копировать NCI graphics, audio, logos, trademarks или third-party assets.
- Не заявлять, что вся cell-basics slice прошла rights clearance: запрос касается только Claim A и нового NCI text/source track.
- Не менять другие slices, main, PR base, merge, deployment или publication state.

## 5. Ожидаемая dependency closure после approval

Если Claim A@2 будет отдельно допущен к рассмотрению, минимальная цепочка:

| Record | Version | Роль |
|---|---:|---|
| CLM-CELL_BASICS-A | 2 | Claim |
| EU-CELL_BASICS-A-NCI | 1 | Evidence Use |
| SRC-NCI-CELL-DICTIONARY | 1 | NCI Source |
| CTX-CELL_BASICS | 2 | Context |
| SCP-CELL_BASICS | 2 | Scope |

В этой новой цепочке OpenStax Source@1 не является provenance dependency. Исторические Claim A@1 / EU A@1 / OpenStax Source@1 остаются сохранены и не включаются в новую цепочку, если selection manifest выберет только версии @2 и EU-NCI@1.

## 6. Условия после выполнения

- Exact current HEAD и все входные записи re-fetch перед изменением.
- Старые версии сохраняются.
- Новая dependency closure проверена.
- Targeted tests проходят, затем все обязательные release workflows проходят на одном immutable HEAD.
- Rights review фиксирует NCI reuse terms и отсутствие third-party assets.
- Все новые записи остаются HOLD; независимая редакционная/Human View проверка и owner release approval остаются отдельными gates.

## 7. Решение владельца

- **APPROVE** — разрешить только операции A–E в указанных границах.
- **REJECT / DEFER** — ничего не менять; существующие версии и HOLD остаются как есть.

Это решение не означает INCLUDE, publication, merge или deployment.
