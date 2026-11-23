# Первая редакция — Package E: точная карта глав и fail-closed validation

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: реализованный валидатор редакционного размещения Claims; не approval engine и не production reader.

## 1. Реализация

Добавлен модуль:
`REFERENCE/src/encyclopedia_reference/first_edition.py`

Добавлены тесты:
`REFERENCE/tests/test_first_edition_chapter_map.py`

Добавлен шаблон:
`REFERENCE/first_edition_shell/chapter-map-template.json`

Валидатор `validate_first_edition_chapter_map(selected_records, chapter_map)` проверяет:
- schema_version карты глав ровно 1.0;
- ровно 19 глав;
- стабильный порядок chapter-1 … chapter-19;
- корректные exact record_id + record_version ссылки;
- все ссылки ведут на выбранные записи;
- размещать можно только записи с record_type=claim;
- один Claim нельзя разместить более одного раза;
- каждый выбранный Claim обязан попасть ровно в одну главу;
- Evidence Use, Source, Context, Scope и Relation нельзя ошибочно выдавать за самостоятельные статьи глав.

Функция возвращает точную карту `(record_id, version) → chapter_id` и не меняет сами записи.

## 2. Почему это важно

Existing selection-aware builder уже проверяет schema 1.1, INCLUDE decision, explicit APPROVED attestation, type/profile/schema pins и полную declared dependency closure. Новый chapter-map validator добавляет независимый редакционный контроль: approved Claim должен быть помещён в одну и только одну главу.

Так разделяются две разные операции:
- selection manifest решает, какие exact-version records вообще могут попасть в сборку;
- chapter map решает, где показывать уже выбранные Claims.

Chapter map не может:
- одобрить запись;
- заменить INCLUDE;
- добавить незаявленную зависимость;
- показать невыбранный Claim;
- обойти HOLD/EXCLUDE;
- превратить Relation или Evidence Use в самостоятельную статью.

## 3. Шаблон карты

`REFERENCE/first_edition_shell/chapter-map-template.json` содержит 19 глав и пустые `claim_refs`. Его статус явно задан как `template_not_approved`. Он намеренно не содержит Claims, не является selection manifest и не может создать содержательный выпуск.

Когда будут одобрены exact-version Claims, в соответствующую главу добавляются только ссылки на эти выбранные версии. Если хотя бы один выбранный Claim не назначен или назначен дважды, валидация завершается ошибкой.

## 4. Тестовое покрытие

Добавлены тесты:
1. успешное точное назначение двух synthetic Claims в разные главы;
2. отказ при числе глав, отличном от 19;
3. отказ при неправильном порядке/ID глав;
4. отказ для unselected или stale Claim;
5. отказ при попытке назначить Evidence Use вместо Claim;
6. отказ при двойном назначении Claim;
7. отказ, если выбранный Claim не имеет главы;
8. отказ при неподдерживаемой версии схемы;
9. проверка checked-in template: 19 глав, пустые списки Claims, статус unapproved.

Тестовый набор закоммичен, но пока не подтверждён CI на последнем HEAD. Наличие тестов не равно PASS.

## 5. Следующий интеграционный шаг

После появления одобренного schema-1.1 selection manifest production build должен:
1. вызвать существующий fail-closed selection builder;
2. получить exact selected record set;
3. проверить chapter map именно против selected Claims;
4. отрендерить только назначенные Claims и связанные выбранные Evidence Use/Source/Context/Scope;
5. сформировать reader navigation и cross-links;
6. сохранить manifest digest, source commit и hashes в offline artifact.

Пока selection manifest пуст, production build должен оставаться закрытым. Нельзя подменять отсутствие INCLUDE отображением всего корпуса или исторически проверенных записей.

## 6. Статус

Package E усиливает точность и безопасность будущего production reader. Он не создаёт release artifact и не меняет publication state. Все кандидаты остаются HOLD; R-01–R-10 остаются OPEN; PR #22 Draft; main не менялся.

## 7. Production-reader integration — implementation checkpoint 2026-11-23

Added:
- `REFERENCE/src/encyclopedia_reference/first_edition_reader.py`
- `REFERENCE/build_first_edition_reader.py`
- `REFERENCE/tests/test_first_edition_reader.py`

The integration calls the existing schema-1.1 selection builder first. That builder remains authoritative for exact record versions, INCLUDE decisions, explicit approval attestations, profile/schema pins and complete dependency closure. The reader then validates the chapter map against only that selected record set.

Fail-closed behavior:
- the production reader requires chapter-map status `approved` and a separate explicit approval attestation;
- the 19 chapter IDs and order remain fixed;
- every selected Claim must appear exactly once;
- only selected Claims render as articles;
- selected Evidence Use and Source records can render only as evidence notes attached to their Claim;
- unselected Claims and non-Claim records cannot become articles;
- HOLD/EXCLUDE, missing dependencies, stale versions, profile drift and incomplete closure are rejected by the selection builder;
- output must be absent or empty and cannot be a symbolic link;
- output is static, local and network-independent; its manifest records source revision, selection/chapter-map digests and output hash.

CLI:
```bash
python REFERENCE/build_first_edition_reader.py \
  --selection-manifest RELEASE/FIRST-EDITION-INCLUDE.json \
  --chapter-map RELEASE/FIRST-EDITION-CHAPTER-MAP.json \
  --source-commit <full-40-character-git-sha> \
  --output /tmp/first-edition-reader
```

The CLI verifies that the requested commit equals the clean checked-out Git HEAD before reading or building. The paths above describe the future production inputs; no production INCLUDE manifest or approved chapter map has been created by this package.

Six additional synthetic integration tests cover successful rendering, evidence/source attachment, exclusion of unselected Claims, rejection of the unapproved template, missing chapter-map approval, HOLD selection, non-Claim article assignment and stale output isolation.

## 8. Owner-provided chapter titles

The first ten chapter titles in `REFERENCE/first_edition_shell/chapter-map-template.json` have been aligned verbatim with the owner-provided list shown in the project conversation. Chapters 11–19 remain unchanged. The template still has 19 empty Claim lists and `template_not_approved`; this title alignment does not approve any content or chapter map.

## 9. Current implementation boundary

This is a completed technical integration package, not a public edition. No production selection, chapter-map approval, INCLUDE decision, rights clearance, publication, deployment, merge or main-branch change is created or inferred. The chapter map and selection manifest remain independent gates. All canonical candidate dispositions remain HOLD.

