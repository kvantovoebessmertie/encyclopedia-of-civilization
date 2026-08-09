004 — Стандарт использования свидетельств (Evidence Use)

Проект: Энциклопедия цивилизации
Статус: рабочий стандарт
Версия: 0.1
Идентификатор: 004-EVIDENCE-USE

────────

1. Назначение

Настоящий стандарт определяет Evidence Use — запись о том, как
определённый материал одного Источника (Source) используется как
свидетельство относительно конкретного Утверждения (Claim).

Evidence Use отделяет сам Источник и его содержание от
зарегистрированной доказательной интерпретации. Прямая связь
Source → Claim недостаточна: она не фиксирует, какая часть Источника
использована, в каком направлении она относится к Claim, к какому
состоянию Source относится и как эта интерпретация может быть отдельно
проверена и оценена.

Evidence Use является самостоятельной сущностью модели. Стандарт не
заменяет будущие стандарты Assessment, Inference, Argument,
Search, Observation и агрегирования свидетельств.

2. Нормативный язык

MUST — обязательно; MUST NOT — запрещено; SHOULD / SHOULD
NOT — сильная рекомендация или запрет, отступление от которых
требует причины; MAY — допустимо, но не обязательно.

Profile MAY усиливать требования стандарта, но MUST NOT ослаблять
Core-инварианты и одновременно заявлять Core-совместимость.

3. Основные понятия

Evidence Use — специализированный Record, фиксирующий
зарегистрированное использование определённого материала одного Source
относительно одного Claim в одном доказательном направлении.

Регистрация Evidence Use означает только существование такой
интерпретации в системе. Она не устанавливает правильность
интерпретации, надёжность Source, силу или независимость evidence,
истинность/ложность Claim либо одобрение проектом.

Evidence Scope — часть Source Context, зарегистрированная как
свидетельственное основание конкретного Evidence Use. Он MAY охватывать
весь Source, одну адресуемую часть либо несколько частей одного
согласованного Source Context. Это обязательный смысловой компонент, но
не отдельная обязательная Core-сущность.

Source Context — согласованный набор ссылок и уровней Source,
необходимых для определения фактически использованного материала. Он
всегда разрешается к ровно одной Source Identity и, когда существенно,
MAY включать Source State / Version, Expression, Representation,
Instance, Component, Anchor, Locator и другие адресуемые
структуры.

Target Claim — единственный Claim, относительно которого
зарегистрирован Evidence Use.

Evidence Role — направление свидетельства относительно Target
Claim. Core 0.1 определяет только supports и contradicts.

Различие является существенно значимым, если способно изменить
идентификацию, интерпретацию, воспроизводимость или доказательный смысл
Evidence Use.

Объект или контекст является resolvable, если его смысловой объект
можно однозначно установить по сохранённой структуре, ссылкам, истории
или контексту. Текущая доступность в интернете не требуется.

Evidence Use атомарен: один EU представляет одну Source Identity, одно
согласованное свидетельственное основание, один Target Claim и одну
Evidence Role. Атомарность не означает одну страницу, предложение,
Locator или физический фрагмент.

4. Core-модель Evidence Use

```text
Evidence Use
├── ровно 1 Source Identity
├── ровно 1 определённый Evidence Scope
├── ровно 1 Target Claim
└── ровно 1 Evidence Role
```

Каждый Evidence Use MUST разрешаться к ровно одной исходной Source
Identity и MUST NOT объединять несколько Source Identities. Несколько
Sources относительно одного Claim представляются несколькими Evidence
Use либо downstream-структурой синтеза.

Каждый EU MUST иметь один определённый Evidence Scope. Отсутствующий
Scope MUST NOT молча означать использование всего Source.

Каждый EU MUST разрешаться к ровно одному Target Claim. Один материал
относительно нескольких Claims требует отдельных Evidence Use.

Каждый Core-совместимый EU MUST иметь ровно одну роль: supports или
contradicts. unknown, neutral и mixed не являются Core Evidence
Roles.

5. Семантика Evidence Role

supports означает, что выбранный Evidence Scope зарегистрирован как
свидетельство в пользу Target Claim. Это не устанавливает истинность
Claim, силу evidence, надёжность Source, независимость или endorsement.

contradicts означает, что Evidence Scope зарегистрирован как
свидетельство против Target Claim. Это не устанавливает ложность
Claim, истинность его логического отрицания или окончательное
опровержение.

Evidence Role кодирует направление, а не силу. Core MUST NOT вводить
strongly_supports, weakly_supports и подобные роли; сила относится к
Assessment.

contradicts C MUST NOT автоматически превращаться в supports not-C.
Role MUST NOT автоматически распространяться через отношения Claims.
Если требуется рассуждение, оно относится к Inference или Argument.

Profile MAY вводить специализированные роли, но при Core-совместимости
каждая такая relation MUST сохранять ровно одно Core-направление —
supports или contradicts.

Ограничение или уточнение Claim не создаёт третью Core Role. Если
ограничение само является самостоятельным проверяемым утверждением, оно
SHOULD быть отдельным Claim; его отношение к исходному Claim относится к
Claim relations, Assessment или Inference.

6. Source Context и Evidence Scope

Source Identity MUST быть однозначной. Отдельное поле source_id не
обязательно, если Identity уже однозначно выводится из более
специфической ссылки.

Используемые уровни Source Context MUST быть взаимно согласованы.
Representation должен относиться к выбранному Source/Expression context,
а Instance — к соответствующему Representation, если эти уровни
используются.

Evidence Scope определяет материал конкретного Evidence Use и MUST NOT
смешиваться с общим временным, географическим, коллекционным или
предметным охватом Source.

Whole-Source use MAY применяться, если весь Source является
свидетельственным основанием, но это MUST быть намеренно или однозначно
представлено и MUST NOT выводиться лишь из отсутствия Locator.

Multi-Part Scope MAY включать несколько адресуемых частей одного Source
Context. Части MUST разделяться при разных Evidence Roles и SHOULD
разделяться при существенно различном provenance, interpretation,
dependency treatment или независимом Assessment. Самостоятельно
оспоримая предпосылка или inference, связывающие части с Claim, SHOULD
быть представлены явно.

Scope MUST позволять определить использованный материал, но
точность Scope ≠ эпистемическая достаточность: даже точная цитата
может быть вырвана из контекста; это вопрос Assessment.

Locator MUST быть интерпретируем внутри Source Context. page 37,
00:14:32 или row 27 недостаточны без разрешимого контекста.

Source State / Version, Expression, Representation, Instance,
Component, Anchor, Locator и контекст носителя становятся
обязательными только когда они существенно значимы.

7. Состояние Source и Claim

Если Source изменяем и изменение способно изменить evidence,
соответствующий Source State MUST оставаться resolvable. Существующий
Evidence Use MUST NOT молча следовать за более поздним, текущим или иным
существенно отличающимся State.

Если изменение Claim способно изменить смысл EU, соответствующий Claim
State MUST оставаться resolvable. EU MUST NOT молча следовать за
семантически изменившимся Claim.

Если EU зависит от конкретного перевода или Expression, он MUST быть
resolvable. Evidence из перевода MUST NOT представляться как обязательно
полученное непосредственно из исходного Expression.

Если доказательный смысл зависит от Representation — например, OCR,
layout, scan, transcription или rendering — оно MUST быть resolvable.
Если смысл зависит от конкретного физического или цифрового Instance,
этот Instance MUST быть resolvable.

Текущая недоступность Source, Representation или Instance сама по себе
не ломает conformance исторического EU, если Identity, Evidence Scope и
существенно необходимый исторический контекст остаются resolvable.

8. Identity и жизненный цикл

Evidence Use имеет собственную Record Identity. Она MUST NOT
автоматически вычисляться из Source + Claim или
Source + Evidence Scope + Claim + Role. Такие комбинации MAY
использоваться для обнаружения возможных duplicates, но не заменяют
persistent Identity.

Identity MAY сохраняться при исправлении или обогащении, если
сохраняются Target Claim, Evidence Role, предполагаемое
свидетельственное основание и его доказательный смысл.

Изменение Scope MAY сохранить Identity, если исправляет адрес или точнее
описывает тот же материал. Существенно другое основание обычно требует
нового EU.

Correction исправляет представление уже предполагавшегося
использования и MAY сохранять Identity. Reinterpretation меняет
аналитическое понимание; существенная переинтерпретация SHOULD сохранять
прежнюю историю и обычно требует нового EU либо другого
history-preserving механизма.

Существенное supports ↔ contradicts обычно требует нового EU.
Настоящая ошибка ввода MAY исправляться с сохранением Identity.
Существенная смена Target Claim также обычно требует нового EU.

Evidence Use MUST использовать общие механизмы проекта для Record
lifecycle, versioning, history и relations; отдельная параллельная
система статусов не вводится.

9. Provenance Evidence Use

Provenance Source отвечает: «Откуда появился этот Source?» Provenance
Evidence Use отвечает: «Как эта доказательная интерпретация появилась в
системе?» Эти цепочки MAY пересекаться, но MUST NOT смешиваться.

EU MUST использовать общую модель Record provenance/history. Отдельная
Core Entity EvidenceUseProvenance не создаётся.

Когда это известно и существенно, provenance SHOULD позволять различать
формирование интерпретации, техническую регистрацию, review/approval,
automated generation, import, migration и derivation.

Human, automated и imported Evidence Use используют одну Core ontology.
Тип происхождения не определяет качество evidence.

Import не означает независимую проверку, endorsement, принятие Role или
силу. Внешний объект SHOULD импортироваться как EU только при
достоверном отображении на один Source, один Scope, один Claim и одно
Core-направление.

Известная lineage копирования, импорта, derivation или adaptation SHOULD
оставаться traceable и MUST NOT намеренно стираться так, чтобы зависимые
интерпретации выглядели независимыми.

Авторитет, статус и экспертность интерпретатора MUST NOT автоматически
становиться Evidence Strength; это MAY учитываться Assessment.

EU MAY содержать rationale. Если Role без объяснения существенно
непрозрачна, rationale SHOULD быть доступно. Самостоятельно оспоримое
proposition, необходимое для связи Source и Claim, SHOULD быть отдельным
Claim и/или Inference.

10. Граница Assessment

Evidence Use фиксирует:

```text
какой материал используется
из какого Source
в каком Evidence Scope
относительно какого Claim
в каком направлении
```

Assessment оценивает:

```text
релевантность
силу
надёжность Source
независимость
достаточность контекста
качество метода
```

Создание EU регистрирует заявленную evidential relevance, но не
доказывает её. Assessment MAY признать EU высоко релевантным, слабым,
нерелевантным или ошибочно интерпретированным.

strength, reliability, independence, assessed relevance,
directness, methodological quality, confidence, probative value
и общий trust/quality не являются универсальными intrinsic Core
properties EU.

Несколько несовместимых Assessments одного EU MUST иметь возможность
сосуществовать. Assessment MUST NOT автоматически переписывать Role или
lifecycle EU.

Core-совместимый EU MAY иметь ноль Assessments. Profile MAY требовать
Assessment перед публикацией или high-risk use.

Cached Assessment summary MAY храниться, но MUST оставаться traceable к
конкретному Assessment и соответствующим состояниям и MUST NOT
трактоваться как вечное внутреннее свойство EU.

11. Несколько свидетельств

Claim MAY иметь 0..N Evidence Use. Supporting и contradicting EU MAY
сосуществовать.

Core не вводит обязательную Entity Evidence Bundle или Evidence Set;
downstream-процесс MAY определять конкретный набор EU как inputs.

Количество EU, Sources, URL, copies, Representations или access
locations не определяет силу или независимость evidence.

Independence относится к downstream Assessment и может быть pairwise,
set-level, Claim-relative, multidimensional или uncertain. Отсутствие
известной зависимости не доказывает independence.

corroborates не является Core Evidence Role.

Известные существенно значимые provenance dependencies MUST оставаться
представимыми. Система MUST NOT скрывать зависимость ради видимости
независимой поддержки. Искусственное дробление одного evidential basis
MUST NOT считаться множеством независимых evidence lines.

Dependence оценивается относительно Target Claim: производные Sources
могут быть зависимыми для Claim о событии, но независимо полезными для
Claim о распространении информации.

Выбор, исключение, сравнение, взвешивание, синтез, агрегирование и
балансирование нескольких EU находятся вне atomic Core. Воспроизводимый
downstream-процесс SHOULD идентифицировать конкретные EU Records/states.
Набор inputs не означает полного охвата всех evidence в мире.

12. Negative Evidence, отсутствие и Search

Отсутствие supporting EU не противоречит Claim. Отсутствие Records в
repository не означает отсутствие явления в мире.

Negative evidence не требует отдельной Core Role: один non-observation
может support один Claim и contradict другой.

Если non-observation используется как persistent evidence, контекст
того, что и при каких условиях искалось/наблюдалось, MUST быть
достаточно resolvable. Достаточность detection opportunity,
чувствительность метода, completeness и вероятность обнаружения
относятся к Assessment и/или явным premises.

Negative evidence может возникать из адресуемого отсутствия внутри
Source либо из отдельного Search/Observation process, результат которого
должен быть долговременно представлен или реконструируем. Не каждый
технический поиск обязан становиться Source.

Search Scope описывает, что охватывал поиск; Evidence Scope —
какая часть результирующего Source Context используется как evidence.
Search Scope не является универсальной Core Entity.

Для search-derived non-observation существенно необходимый Search
Context MUST быть resolvable и MAY включать corpus, database state,
time, query, filters, observation area, method, access limitations и
detection conditions.

Смыслово разные состояния MUST NOT сливаться, если различие существенно:
zero, missing, not measured, not applicable, not observed,
not detected, below detection limit.

Core MUST NOT применять универсальный closed-world assumption:
отсутствие объекта в системе не означает его отсутствие в мире.

Самостоятельно оспоримые предпосылки — например, «реестр был полным»,
«прибор обязательно обнаружил бы явление», «свидетель обязательно
заметил бы событие» — SHOULD быть представлены явно.

```text
Можно определить, что именно искали?
→ Conformance

Был ли поиск адекватным?
→ Assessment
```

13. Conformance

Core-совместимый Evidence Use:

1. соответствует применимому Record Standard;
2. разрешается к ровно одной Source Identity;
3. имеет один определённый Evidence Scope;
4. разрешается к ровно одному Target Claim;
5. имеет ровно одну Core Evidence Role;
6. имеет согласованный Source Context;
7. сохраняет resolvable все существенно необходимые Source/Claim states
и layers;
8. имеет достаточно идентифицируемый Evidence Scope.

Structural Conformance относится к cardinality, обязательным
relations, Role vocabulary, identifiers, graph consistency и structural
forms.

Referential & Contextual Conformance проверяет, можно ли определить
фактически использованный Source State, Locator context, Representation,
historical state и необходимый Search Context.

Epistemic Assessment отвечает на вопросы правильности Role,
адекватности Scope, надёжности Source, качества Method, силы,
независимости и разумности inference.

```text
Можем ли мы определить, что именно было использовано?
→ Conformance

Было ли разумно использовать это таким образом?
→ Assessment
```

Core Conformance не означает истинность Claim, правильность Role,
evidential strength, independence, project endorsement, publication
eligibility, полную provenance или текущую доступность Source.

Record MAY быть Core-совместимым, но не соответствовать более строгому
Profile. High-risk Profile MAY требовать explicit Source State, exact
Locator, independent review, Assessment, Method provenance или
preservation artifact.

14. Profiles и Extensions

Profile MAY усиливать требования и требовать дополнительные provenance,
reviewer attribution, Source addressing, preservation, Method reference,
Assessment, Search Context и domain-specific specialization.

Profile, заявляющий Core compatibility, MUST NOT отменять инварианты
одного Source, одного Claim, определённого Evidence Scope и Core
evidential direction; MUST NOT смешивать EU с Assessment или трактовать
Record multiplicity как independence.

15. Failure Modes и Anti-Patterns

Invariant Violation: несколько Source Identities или Claims в одном
EU; отсутствие Role; использование EU как Assessment; автоматический
перенос Role через Claim relations; превращение contradicts C в
supports not-C.

Conformance Failure: неразрешимый Source/Claim; неопределённый
Scope; противоречивый Source Context; неразрешимый существенно
необходимый Source State; Locator без интерпретируемого context.

Epistemic/Operational Anti-Pattern: quote mining, слабый Search
design, selection bias, artificial fragmentation, ложная independence,
stale Assessment projection, evidence laundering, unsupported import
mapping.

Citation, mention, retrieval result, semantic similarity или candidate
relevance MUST NOT автоматически становиться Evidence Use.

Evidence Role MUST NOT храниться как абсолютное свойство Source.
strength, reliability, independence, confidence MUST NOT
использоваться для слияния Assessment с EU Core.

External relation MUST NOT превращаться в supports/contradicts, если
её semantics этого не обосновывает; mentions нельзя молча повысить до
supports.

Внешний score MUST NOT переименовываться в evidential
strength/reliability/confidence без совместимой traceable semantics.

Fabricated Source, State, Scope или Locator может быть
referential/conformance integrity failure. Ошибочная интерпретация
реального материала — отдельная эпистемическая проблема.

Locator MUST NOT молча менять исторический semantic target после
изменения Representation/State.

Один evidential basis MUST NOT дробиться ради видимости независимых
подтверждений. Существенно разные bases SHOULD NOT объединяться, если
это скрывает разные Roles, provenance, interpretations или Assessment
requirements.

Source, существенно derived из Target Claim, MUST NOT автоматически
считаться independent support того же Claim.

Downstream presentation SHOULD NOT скрывать существенно релевантные
competing EU, представляя результат как общий баланс evidence.

Cached evaluation MUST NOT представляться как current, если относится к
существенно другому историческому состоянию.

Deduplication MUST NOT уничтожать существенно важные provenance/history,
но duplicate Records MUST NOT автоматически становиться независимыми
evidence lines.

Lossy export MAY существовать, но MUST NOT заявлять full semantic
equivalence, если потеряны Identity, Source Context, Scope, Claim, Role
или существенно необходимое state.

16. Conformance и Stress Tests

1. Один EU содержит две Source Identities? — Нет.
2. Один EU относится к нескольким Claims? — Нет.
3. Core EU существует без supports/contradicts? — Нет.
4. Можно определить фактически использованный материал? — Да.
5. Можно отличить whole-Source use от отсутствующего Scope? — Да.
6. После изменения Source исторический EU остаётся интерпретируемым
относительно использованного State? — Да.
7. Зависимый от перевода EU разрешается к нужному Expression? —
Да.
8. Representation-specific evidence разрешается к нужному
Representation? — Да.
9. Instance-specific evidence разрешается к Instance? — Да.
10. Удаление Assessments не уничтожает смысл EU? — Да.
11. Несовместимые Assessments могут сосуществовать? — Да.
12. Противоположные интерпретации одного Source Scope и Claim могут
сосуществовать как разные EU? — Да.
13. Много EU могут относиться к одному Claim без обязательного Bundle?
— Да.
14. Различие Source/Record Identity доказывает independence? —
Нет.
15. Lineage производных копий сохраняется для предотвращения double
counting? — Да.
16. Fragmentation создаёт независимые evidence lines? — Нет.
17. Circularity остаётся обнаружимой? — Да.
18. Circularity делает Claim автоматически ложным? — Нет.
19. Нулевой Search автоматически доказывает отсутствие? — Нет.
20. Разные виды missingness остаются различимыми? — Да.
21. Repository silence означает отсутствие contradicting evidence в
мире? — Нет.
22. Самостоятельные premises могут быть вынесены из EU? — Да.
23. Reinterpretation может сохранять предыдущую историю? — Да.
24. Genuine correction может сохранить Identity? — Да.
25. Imported EU отличим от внешнего Source, лишь сообщающего о связи?
— Да.
26. Registered/imported EU означает endorsement? — Нет.
27. Historical EU разрешается к достаточно определённому Source/Claim
state? — Да.
28. Locator drift может быть предотвращён или обнаружен? — Да.
29. Deduplication может сохранить существенно важные provenance/history?
— Да.
30. Full-fidelity round-trip восстанавливает EU Identity, Source
Identity, Scope, Claim, Role, необходимые states и Record
provenance/history? — Да.
31. Модель работает с будущим носителем без страниц, файлов и URL? —
Да.
32. Простой immutable Source может дать EU только через
Record + Source + Evidence Scope + Claim + Role? — Да.
33. Та же минимальная структура может быть недостаточной, если случай
существенно требует дополнительного контекста? — Да.

17. Минимальное ядро

```text
EVIDENCE USE
=
Record
+
ровно 1 Source Identity
+
1 определённый Evidence Scope
+
ровно 1 Target Claim
+
ровно 1 Evidence Role
+
только существенно необходимый дополнительный контекст
```

Core Evidence Roles:

```text
supports
contradicts
```

Evidence Use — это не Source, Citation, Claim, Assessment,
Argument, Inference, Evidence Bundle, Truth или
Project Endorsement.

Одна модель должна работать для текста, изображений, аудио, видео,
datasets, measurements, физических артефактов, testimony,
mutable/historical Sources, Search results, non-observations и будущих
носителей.

Свидетельство рассматривается не как абсолютное свойство Source, а как
зарегистрированное, прослеживаемое и отдельно оцениваемое
использование материала Source относительно конкретного Claim.

18. Итоговые Core-инварианты

1. Evidence Use является специализированным Record.
2. Evidence Use фиксирует зарегистрированную доказательную
интерпретацию.
3. Один EU разрешается к ровно одной Source Identity.
4. Один EU имеет один определённый Evidence Scope.
5. Один EU разрешается к ровно одному Target Claim.
6. Один EU имеет ровно одну Core Evidence Role.
7. Core Roles — supports и contradicts.
8. Scope MAY охватывать весь Source или одно согласованное
свидетельственное основание.
9. Отсутствующий Scope MUST NOT молча означать весь Source.
10. Уровни Source Context MUST быть согласованы.
11. Существенно значимые Source и Claim states MUST оставаться
resolvable.
12. Существенно значимые Expression, Representation и Instance MUST
оставаться resolvable.
13. Evidence Role определяет направление, а не силу.
14. supports не означает истинность Claim.
15. contradicts не означает ложность Claim.
16. contradicts C не означает автоматически supports not-C.
17. Role не распространяется автоматически через Claim relations.
18. EU Identity не сводится к semantic endpoint tuple.
19. Correction и Reinterpretation различаются.
20. EU MUST NOT молча следовать за существенно другим Source/Claim
state.
21. EU использует общий Record lifecycle.
22. Provenance EU и provenance Source различаются.
23. Import не означает endorsement.
24. Human/automated/imported origin не определяет качество evidence.
25. EU и Assessment различаются.
26. EU MAY существовать без Assessments.
27. Конкурирующие Assessments MAY сосуществовать.
28. Assessment MUST NOT автоматически изменять EU.
29. Strength, reliability, independence, assessed relevance, directness,
confidence и weight не являются universal intrinsic EU properties.
30. Несколько EU для одного Claim допустимы.
31. Supporting и contradicting EU MAY сосуществовать.
32. Record multiplicity не означает independent evidence.
33. Source multiplicity не означает independent evidence.
34. Unknown dependence не означает independence.
35. Известные materially relevant provenance dependencies MUST NOT
скрываться.
36. Circular provenance не делает Claim автоматически ложным.
37. Negative evidence не требует отдельной Core Role.
38. Absence of evidence не является автоматически evidence of absence.
39. Молчание repository не равно молчанию мира.
40. not detected не означает автоматически absent.
41. Универсальный closed-world assumption запрещён.
42. Search/Observation context обязателен, когда существенно необходим
для интерпретации non-observation.
43. Самостоятельно оспоримые premises SHOULD быть явными.
44. Core Conformance и epistemic quality различаются.
45. Core Conformance и project endorsement различаются.
46. Core Conformance и publication eligibility различаются.
47. Core Conformance и Profile Conformance различаются.
48. Profiles MAY усиливать, но MUST NOT ослаблять Core-инварианты.
49. Core semantics должны быть концептуальными и технологически
независимыми.
50. Full-fidelity representations SHOULD сохранять восстановимость
семантики EU при хранении и экспорте.

────────

Конец документа 004-EVIDENCE-USE.md — версия 0.1
