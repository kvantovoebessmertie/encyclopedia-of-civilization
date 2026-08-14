# 008 — ACTION
## Стандарт представления действий

**Проект:** Энциклопедия цивилизации  
**Статус:** рабочий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются действия — человеческие, коллективные, институциональные, технические, автоматизированные и иные случаи, в которых определённое осуществление представлено как действие или операция в рамках применимой модели.

Цель стандарта — позволить сохранять:

- что было сделано;
- кем или чем это было осуществлено, если это известно;
- когда и где;
- над чем или в отношении чего;
- каким способом;
- в каком контексте;
- с каким фактическим охватом;
- было ли действие начато, продолжено, завершено, прервано или предпринято как попытка;
- являлось ли оно исполнением Decision, Plan, Procedure, Instruction или другого объекта;
- какие результаты наблюдались;
- какие причинные связи установлены, предполагаются или неизвестны;
- что известно, неизвестно, реконструировано или оспаривается.

Стандарт не предназначен для автоматического определения того, является ли Action:

- намеренным;
- правильным;
- разумным;
- законным;
- легитимным;
- этичным;
- безопасным;
- соответствующим Decision;
- соответствующим Plan;
- соответствующим Procedure;
- эффективным;
- успешным;
- причиной последующего Result.

Сохранить Action означает сохранить максимально честное представление о том, **что было сделано или представлено как фактически осуществлённое действие**, не подменяя действие намерением, Decision, Plan, Procedure, Result или последующей интерпретацией.

---

# 1. Основное понятие

## 1.1. Action

**Action (Действие)** — специализированный Record, представляющий определённое осуществление, представленное как произошедшая операция, поведение или иное enactment, атрибутируемое acting или operational role в рамках применимой модели.

Action отвечает на основной вопрос:

> **Что было сделано?**

Action представляет осуществление, а не:

- намерение осуществить;
- Decision осуществить;
- Recommendation осуществить;
- Plan осуществить;
- описание того, как следует осуществлять;
- автоматически любой Event;
- автоматически любой Result.

Action не требует человеческого сознания или намерения.

Но:

    mere occurrence
    ≠ Action automatically

    natural change
    ≠ Action automatically

    causal activity
    ≠ Action automatically

Action требует достаточной семантической атрибуции occurrence как enactment или operation, а не просто как произошедшего изменения.

---

## 1.2. Функциональная нейтральность

Action не является исключительно человеческой категорией.

Action MAY быть атрибутирован:

- человеку;
- группе;
- организации;
- механизму;
- программной системе;
- автоматизированной системе;
- распределённой системе;
- иному actor/process, которому в применимой модели приписывается acting или operational role.

Наличие сознания, намерения, моральной ответственности или свободы воли не является универсальным Core requirement для существования Action.

---

# 2. Минимальная структура Action

Для представления завершённого Action необходимо как минимум:

1. определённое enactment, представленное как произошедшее;
2. определённый Action Content;
3. достаточная enactment attribution.

Минимальная формула:

    defined enactment represented as having occurred
    +
    defined Action Content
    +
    sufficient enactment attribution

**Enactment attribution** — достаточная семантическая атрибуция occurrence как Action/enactment, позволяющая отличить его от mere Event, natural change или иной не-action semantics.

Конкретная identity Actor MAY быть:

- известна;
- частично известна;
- неизвестна;
- оспариваема.

Следовательно:

    specific Actor unknown
    ≠ no Action automatically

Не обязательно, чтобы для существования Action были известны:

- конкретный Actor;
- intention;
- Decision;
- Plan;
- Procedure;
- Motivation;
- Method;
- точное время;
- точное место;
- полный Context;
- Result;
- Effect;
- Objective;
- успешность.

Неизвестные элементы MUST NOT изобретаться для заполнения модели.

---

# 3. Action Content

**Action Content** — содержание, представляющее то, что было осуществлено в рамках конкретного Action.

Например:

    оператор закрыл клапан

Action Content:

    закрытие клапана

Action Content является semantic role/content construct и не требует отдельной Core Entity.

Он MAY включать:

- operation;
- transformation;
- movement;
- transfer;
- communication;
- activation;
- deactivation;
- application;
- removal;
- construction;
- destruction;
- withholding;
- другие формы осуществления.

Action Content MAY быть простым или структурированным.

В отличие от `007-DECISION`, `008-ACTION` не вводит универсальное требование `exactly one Outcome construct`.

---

# 4. Action ≠ Decision

Decision отвечает:

> Что было решено?

Action отвечает:

> Что было сделано?

Следовательно:

    Decision
    ≠ Action

Decision может существовать без Action.

Action может существовать без известного Decision.

Например:

    Decision:
    evacuate Sector A

не означает:

    Sector A was evacuated

И:

    Sector A was evacuated

не доказывает автоматически:

    a Decision to evacuate existed

Связь между Decision и Action должна быть представлена отдельно, когда она установлена.

---

# 5. Execution

**Execution (Исполнение)** — relation или semantic role, в которой Action представлен как осуществляющий, реализующий или предпринимаемый в исполнение определённого Decision, Plan, Procedure, Instruction или другого релевантного объекта.

Следовательно:

    Action
    ≠ Execution intrinsically

Action становится Execution только относительно чего-либо.

Например:

    Action A
    executes
    Decision D

Но:

    Action A exists

само по себе не означает:

    Action A executes Decision D

Execution relation MAY существовать при:

- частичном исполнении;
- отклоняющемся исполнении;
- ошибочном исполнении;
- несанкционированном исполнении;
- неполном исполнении.

Следовательно:

    executes
    ≠ perfectly conforms

    executes
    ≠ authorized automatically

    executes
    ≠ successful

`008` не требует отдельной фундаментальной Execution Entity.

---

# 6. Action ≠ Plan ≠ Procedure ≠ Instruction

Необходимо различать:

    Plan
    → что предполагается сделать

    Procedure
    → как действие должно выполняться

    Instruction
    → что кому-либо предписывается сделать

    Action
    → что было осуществлено

Следовательно:

    planned
    ≠ performed

    prescribed
    ≠ performed

    instructed
    ≠ performed

    scheduled
    ≠ performed

Procedure MAY быть реализована через один или несколько Actions.

Но Procedure как template MUST NOT автоматически отождествляться с фактически выполненной последовательностью Actions.

---

# 7. Action ≠ Event

Не всякое Event является Action.

Event MAY представлять произошедшее изменение или событие независимо от actor/enactment attribution.

Например:

    землетрясение произошло

может быть Event, но не Action в смысле этого стандарта.

Напротив:

    оператор закрыл клапан

может быть Action.

Action classification зависит от represented enactment attribution, а не от:

- человеческого намерения;
- движения;
- физического изменения;
- грамматической формы предложения.

Один и тот же real-world occurrence MAY поддерживать разные representations.

Например:

    Event:
    клапан открылся

и:

    Action:
    автоматическая система открыла клапан

могут описывать один occurrence с разными semantic roles.

Эти representations MUST NOT автоматически смешиваться.

Следовательно:

    occurrence
    ≠ Action automatically

    natural change
    ≠ Action automatically

---

# 8. Action ≠ Process

Action и Process могут относиться к одной и той же реальности, но не должны автоматически отождествляться.

Process обычно представляет:

- разворачивающуюся последовательность;
- механизм;
- устойчивое течение;
- повторяющуюся или продолжительную деятельность;
- совокупность взаимосвязанных изменений.

Action представляет определённое осуществление.

Один Process MAY включать множество Actions.

Один Action MAY сам иметь внутреннюю процессуальную структуру.

Action/Process distinction определяется semantic purpose и granularity, а не продолжительностью.

Core MUST NOT устанавливать универсальный временной порог, после которого Action автоматически становится Process.

Duration, continuity или repetition сами по себе не определяют, является ли representation Action, Process, одним Action или множеством Actions.

---

# 9. Action ≠ Result

Action представляет осуществление.

Result представляет наблюдаемое состояние, событие или изменение, относимое к downstream-состоянию после Action или Process.

Следовательно:

    Action
    ≠ Result

Например:

    Action:
    administered substance X

    Result:
    temperature decreased

Первое не доказывает второе.

Второе не доказывает автоматически причинность первого.

---

# 10. Actor

## 10.1. Определение

**Actor** в контексте Action — субъект, система, collective или process, которому атрибутируется осуществление Action.

Actor является semantic role.

Он не требует отдельной ActionActor Core Entity.

Конкретный Actor MAY быть неизвестен, если actionality самого occurrence достаточно установлена.

Например:

    ворота были намеренно открыты ночью
    Actor unknown

MAY сохраняться как Action, если имеются достаточные основания считать открытие действием, а не самопроизвольным Event.

---

## 10.2. Actor ≠ Decision-maker

Исполнитель Action не становится автоматически Decision-maker.

    Actor
    ≠ Decision-maker

Например:

    Committee decided D
    Operator performed A

Committee может быть Decision-maker.

Operator может быть Actor.

Они не обязаны совпадать.

---

## 10.3. Actor ≠ responsibility / authority

Факт осуществления Action не доказывает автоматически:

- authority;
- responsibility;
- accountability;
- ownership;
- intention;
- legitimacy;
- moral blame.

Следовательно:

    performed by P
    ≠ authorized by P

    performed by P
    ≠ decided by P

    performed by P
    ≠ morally responsible automatically

---

# 11. Multiple actors

Action MAY иметь:

- одного Actor;
- нескольких Actors;
- коллективную attribution;
- институциональную attribution;
- системную attribution;
- распределённую attribution.

Необходимо различать, когда materially relevant:

- direct performer;
- controller;
- operator;
- supervisor;
- authorizer;
- coordinator;
- supporting participant;
- automated subsystem.

Участие в Action не означает одинаковую роль всех участников.

Разные Actors сами по себе также не доказывают существование нескольких Actions.

Один коллективный Action MAY включать множество участников.

---

# 12. Automated Action

Автоматизированная система MAY быть Actor, если в применимой модели именно системе или её части атрибутируется осуществление Action.

Необходимо различать:

    system recommended A
    ≠ system performed A

    system triggered A
    ≠ system necessarily performed entire A

    human initiated system
    ≠ human manually performed every downstream Action

    automated Action
    ≠ autonomous Decision automatically

Actor attribution определяется фактической архитектурой системы и сохранённой provenance, а не поверхностной грамматикой или UI.

Sensor, controller, actuator и whole system MUST NOT автоматически считаться одним и тем же Actor role.

---

# 13. Action Object / Target

Action MAY быть направлен на:

- объект;
- человека;
- территорию;
- систему;
- данные;
- ресурс;
- состояние;
- множество объектов;
- другой Action или Process.

Target отвечает на вопрос:

> Над чем или в отношении чего осуществлялось действие?

Target не является обязательной отдельной Core Entity.

Отсутствие известного Target не уничтожает Action, если само осуществление достаточно определено.

---

# 14. Action Context

**Action Context** — внешние условия и состояния, materially необходимые для интерпретации Action.

Context MAY включать:

- время;
- место;
- среду;
- operating state;
- emergency conditions;
- system version;
- jurisdiction;
- доступные ресурсы;
- другие обстоятельства.

Необходимо различать:

    Action Context
    ≠ Action Content
    ≠ Action Scope
    ≠ Action Result

Одно содержание MAY участвовать в нескольких semantic roles, но materially relevant различия должны оставаться resolvable.

---

# 15. Action Scope

**Action Scope** — область фактического осуществления Action.

Scope MAY включать:

- территорию;
- population;
- objects;
- quantity;
- duration;
- system components;
- другие границы.

Неизвестная граница MUST NOT становиться универсальной.

    unknown area
    ≠ everywhere

    unknown quantity
    ≠ all

    unknown duration
    ≠ continuous

---

# 16. Intended Scope ≠ Action Scope ≠ Effect Scope

Необходимо различать:

    Intended Scope
    → что предполагалось охватить

    Action Scope
    → что фактически охватило действие

    Effect Scope
    → что оказалось затронуто последствиями

Например:

    intended:
    treat Field A

    Action:
    substance applied to 70% of Field A

    Effect:
    runoff affected River B

Эти области не должны автоматически наследоваться друг от друга.

---

# 17. Method

**Action Method** — представление того, каким способом Action осуществлялся.

Method MAY включать:

- инструмент;
- технику;
- последовательность;
- материал;
- protocol;
- configuration;
- operational mode.

Но:

    prescribed Method
    ≠ actual Method

    available Method
    ≠ used Method

    reported Method
    ≠ verified Method

Method не является обязательной отдельной Core Entity.

---

# 18. Intention и Motivation

Action MAY быть намеренным или ненамеренным.

Но Core не требует известного intention для существования Action.

Необходимо различать:

    Action
    ≠ Intention

    Intention
    ≠ Decision

    stated Motivation
    ≠ actual Motivation automatically

    inferred Motivation
    ≠ recorded Motivation

Неизвестная Motivation MUST NOT изобретаться.

Наличие намеренного Action не означает автоматически намерение всех downstream effects.

---

# 19. Omission / deliberate non-action

Сознательное воздержание MAY представляться как Action только когда non-performance itself materially выделено и достаточно атрибутировано в сохраняемой semantics через один или несколько sufficiently grounded frames, например:

- expectation;
- duty;
- Decision;
- Instruction;
- Plan;
- Procedure;
- explicit materially relevant opportunity;
- actor stance;
- определённый available course of action;
- другую обоснованную контекстную рамку.

Например:

    operator deliberately withheld activation

может быть Action.

Но:

    no recorded action

не означает автоматически:

    deliberate omission

И:

    P did not administer drug

само по себе не позволяет установить:

- deliberate withholding;
- забывание;
- отсутствие препарата;
- отсутствие показаний;
- невозможность действия.

Следовательно:

    absence of Action evidence
    ≠ evidence of deliberate non-action

Omission требует собственной attribution и materially relevant Context.

Core MUST NOT превращать любую логически возможную неосуществлённую альтернативу в Omission Action.

---

# 20. Attempt

**Attempt** — Action, представленный как направленный на осуществление определённого изменения, состояния или Objective независимо от того, было ли желаемое достигнуто.

Следовательно:

    attempted
    ≠ completed

    attempted
    ≠ succeeded

Например:

    person pulled trigger

может быть завершённым Action относительно:

    pull trigger

и одновременно failed Attempt относительно:

    fire weapon

Completion и Attempt semantics являются относительными к тому Action Content, intended change или reference target, относительно которого они утверждаются.

Отдельная Attempt Entity не требуется.

---

# 21. Completion

Необходимо различать:

    started
    ≠ continued
    ≠ completed
    ≠ interrupted
    ≠ aborted

Но `008` не вводит универсальный закрытый `Action.status` enum.

Completion/failure semantics MUST быть привязаны к определённому reference/semantic target, например:

- Action Content;
- intended change;
- Decision;
- Plan;
- Procedure;
- Objective;
- другому reference object,

если без этого смысл неясен.

Например:

    valve opened to 50%

может быть:

- completed относительно `open to 50%`;
- partial относительно `fully open`;
- failed Attempt относительно `fully open`;
- fully conformant относительно Decision, требовавшего 50%.

Следовательно completion и failure не являются универсальными свойствами occurrence самих по себе.

---

# 22. Partial Action

Partial completion MUST NOT автоматически превращаться:

- в полный Action;
- в отсутствие Action;
- в failure;
- в новый Action.

Например:

    Decision:
    evacuate 100 people

    Action:
    60 people transported

    Outcome Realization:
    partial

Decision Scope, Action Scope и Outcome Realization должны оставаться различимыми.

---

# 23. Identity

Action identity следует конкретному осуществлению, а не совпадению текста или Action Content.

    same Action Content
    ≠ same Action

Например:

    Valve A closed at T1
    Valve A closed at T2

MAY быть двумя Actions.

Но:

    different wording
    ≠ different Action automatically

Например:

    closed valve 7

и:

    isolated coolant line

MAY описывать одно и то же historical enactment на разных уровнях abstraction.

Разные архивные representations одного осуществления MUST NOT автоматически создавать несколько Action identities.

---

# 24. Granularity

Action может быть представлен на разных уровнях:

    build shelter

или:

    cut timber
    transport timber
    assemble frame
    install roof

Ни один уровень не является универсально правильным.

Granularity должна определяться:

- целью представления;
- provenance;
- materially relevant distinctions;
- Profile.

Признаками возможной самостоятельности Actions могут быть:

- разные Actors;
- разные времена;
- независимое начало/прекращение;
- разные Targets;
- разные Execution relations;
- independent provenance;
- materially different causal roles.

Но каждый такой признак является analytical/evidential signal, а не достаточным identity criterion сам по себе.

Разные Actors, времена или Targets MAY всё равно входить в один коллективный, длительный или структурированный Action.

---

# 25. Composite Action

Один Action MAY иметь структурированный Action Content.

Но Composite Action MUST NOT использоваться для искусственного объединения исторически независимых осуществлений, если это materially искажает:

- identity;
- Actor attribution;
- timing;
- Scope;
- provenance;
- Execution relations;
- causal interpretation;
- safety-critical meaning.

Отдельная CompositeAction Entity не требуется.

---

# 26. Repeated Action

Повторяющиеся одинаковые действия не становятся автоматически одним Action.

    same operation repeated
    ≠ one Action automatically

Но Profile MAY представлять повторяющуюся деятельность агрегированно, если individual identities не materially важны.

Например:

    pump operated continuously from T1 to T2

может быть представлено:

- как один aggregated Action;
- как Process;
- как множество cycles;

в зависимости от цели.

Если segmentation исторически неизвестна:

    unknown segmentation
    ≠ one Action automatically

    unknown segmentation
    ≠ many Actions automatically

---

# 27. Continuous Action

Action MAY быть непрерывным или иметь нечёткие естественные границы.

Core не требует универсального способа деления continuous activity на отдельные Actions.

Identity/granularity MAY определяться Profile.

Неопределённость границы MUST NOT заменяться искусственно точной segmentation без основания.

Продолжительность сама по себе не определяет, является ли representation Action или Process.

---

# 28. Temporal semantics

Когда materially relevant, Action MAY сохранять:

- start time;
- end time;
- duration;
- ordering;
- temporal uncertainty;
- relative timing.

Необходимо различать:

    occurred before
    ≠ caused

    occurred during
    ≠ participated in automatically

    started
    ≠ completed

Точная дата или время MUST NOT изобретаться из приблизительного исторического свидетельства.

---

# 29. Spatial semantics

Action MAY иметь несколько materially distinct spatial roles.

Например:

    Actor location
    Target location
    operational locus
    Effect location

могут различаться.

Дистанционное Action может иметь:

    Actor location: A
    Target location: B
    Effect location: C

Поэтому Core не вводит один универсальный:

    Action.location

без определения spatial role.

Location roles должны оставаться distinguishable when material.

---

# 30. Action lifecycle и historical state

Action как историческое осуществление MUST NOT переписываться позднейшими состояниями связанных объектов.

Например:

    Machine M@T1
    ≠ Machine M@current

    Procedure P@T1
    ≠ Procedure P@current

    Region R@T1
    ≠ Region R@current

Если historical State materially важен для интерпретации Action, он должен оставаться resolvable.

Позднейшая информация MUST NOT незаметно добавляться в historical Method, Context, Scope или Actor attribution.

---

# 31. Correction ≠ new Action

Correction исправляет representation того же historical enactment.

New Action представляет другое фактическое осуществление.

Например:

    recorded time:
    14:00

    corrected time:
    14:10

MAY быть Correction, если evidence показывает, что это тот же Action и исходное время было записано ошибочно.

Но:

    Action repeated at 14:10

является новым Action.

Само изменение field не определяет identity.

---

# 32. Relations между Actions

Actions MAY иметь отношения:

- precedes;
- follows;
- enables;
- inhibits;
- interrupts;
- resumes;
- repeats;
- coordinates with;
- executes;
- triggers;
- affects;
- part of;
- другие отношения.

`008` определяет Action-specific relation semantics, но SHOULD использовать generic project relation infrastructure, а не создавать отдельный Action-only relation framework.

Relations не должны автоматически означать:

- identity;
- causality;
- intention;
- responsibility;
- common Actor.

Relation labels, такие как:

- affects;
- triggers;
- enables;
- inhibits;

MUST использоваться только с определённой relation semantics и MUST NOT незаметно усиливать causal claim сверх реально представленного.

---

# 33. Provenance отношений

Relation между Actions сама является знанием.

Она MAY быть:

- directly observed;
- directly recorded;
- inferred;
- computed;
- reconstructed;
- disputed.

Следовательно:

    observed sequence
    ≠ proven causality

    inferred coordination
    ≠ recorded coordination

    computed dependency
    ≠ historically asserted dependency

Materially relevant provenance отношения должна сохраняться.

Relation transitivity или symmetry MUST NOT предполагаться универсально.

---

# 34. Trigger semantics

Action MAY trigger another Action, Event или Process.

Но:

    A triggered B
    ≠ A caused every downstream consequence of B

Trigger relation может описывать initiation semantics, не полную downstream causality.

Её точный meaning должен определяться применимой relation semantics.

---

# 35. Action → Result

Action MAY быть связан с Result.

Но:

    Action A
    before
    Result R

не означает:

    A caused R

Causal attribution требует соответствующей:

- Evidence;
- Inference;
- Assessment;
- causal model;
- другой допустимой semantics.

Temporal succession MUST NOT автоматически интерпретироваться как causation.

---

# 36. Direct effect, Result и Consequence

Иногда полезно аналитически различать:

    attributed direct operational effect
    downstream Result
    later Consequence

Например:

    Action:
    valve opened

    attributed direct operational effect:
    flow began

    Result:
    tank level increased

    later Consequence:
    downstream area flooded

**Attributed Direct Effect** является аналитической causal role, а не отдельной обязательной Core Entity.

Утверждение directness требует соответствующей provenance или causal basis; оно не возникает автоматически из temporal proximity.

`008` не определяет полную ontology Result / Effect / Consequence.

Он определяет только их границы относительно Action.

---

# 37. Success

`008` не вводит универсальный:

    Action.success = true/false

Потому что `success` может означать разные вещи:

- Action completed;
- intended change occurred;
- Decision Outcome realized;
- Objective achieved;
- Procedure followed;
- Result оказался благоприятным.

Они должны оставаться различимыми.

---

# 38. Effectiveness

Action effectiveness не является intrinsic property без определённого Objective, Result model и causal attribution.

    Action completed
    ≠ effective

    Objective achieved
    ≠ Action caused achievement

    good Result
    ≠ good Action automatically

Effectiveness при необходимости представляется через Assessment или другую соответствующую semantics.

---

# 39. Conformance to Decision / Plan / Procedure

Action MAY оцениваться относительно:

- Decision;
- Plan;
- Procedure;
- Instruction;
- Policy;
- safety rule;
- другого normative/reference object.

Но необходимо различать:

    Action exists
    ≠ conforms

    Action executes Decision
    ≠ perfectly conforms to Decision

    Procedure followed
    ≠ Result successful

    Procedure violated
    ≠ Action did not occur

    procedural conformance
    ≠ Action quality

Conformance является отдельной relation/evaluation semantics.

---

# 40. Unauthorized / prohibited Actions

Action может быть:

- unauthorized;
- prohibited;
- illegal;
- procedurally non-conformant;
- harmful;
- mistaken.

Это не отменяет факт его исторического существования как Action.

    Action existence
    ≠ authorization
    ≠ legality
    ≠ legitimacy
    ≠ correctness

Историческое представление MUST сохранять существование Action независимо от его нормативной оценки.

---

# 41. Unknown, partial и disputed Action semantics

Unknown, partial или disputed semantics MUST NOT заменяться invented, default, current или merely plausible semantics.

Следовательно:

    actor unknown
    ≠ nobody acted

    actor unknown
    ≠ occurrence was not Action

    exact time unknown
    ≠ guessed exact time

    method unknown
    ≠ expected Method

    Result unknown
    ≠ no Result

    intention unknown
    ≠ accidental

    Decision relation unknown
    ≠ no Decision existed

Неопределённость является допустимым состоянием знания.

---

# 42. Materiality

**Materially relevant / materially required** — semantics, отсутствие, изменение или искажение которой способно изменить:

- Action identity;
- Action attribution;
- interpretation;
- Scope;
- historical meaning;
- Execution relation;
- causal interpretation;
- safety-critical use;
- либо существенно повлиять на downstream use.

Materiality зависит от цели и контекста representation.

---

# 43. Resolvability

**Resolvable** означает, что materially relevant semantics может быть восстановлена из сохранённой структуры, references или provenance без изобретения отсутствующего смысла.

Resolvable:

    ≠ necessarily embedded
    ≠ necessarily online
    ≠ necessarily complete

---

# 44. Representation Fidelity

Representation Action MUST NOT materially изменять:

- что было сделано;
- кто или что это осуществило;
- время;
- Scope;
- Target;
- Method;
- completion semantics;
- Decision/Execution relation;
- Result relation;
- causal status;
- uncertainty;
- provenance.

Canonical data может быть корректной, а UI, перевод, summary или export — misleading.

Representation Fidelity является отдельным измерением.

---

# 45. Historical Action ≠ current Instruction

Историческое описание Action не является автоматически инструкцией выполнить такое же действие.

    Historical:
    P performed A

    ≠

    Instruction:
    perform A

Это особенно важно для:

- опасных процедур;
- медицинских действий;
- аварийных действий;
- исторических практик;
- устаревших технологий.

Representation MUST NOT превращать descriptive historical Action в current Recommendation или Instruction без отдельного основания.

---

# 46. Translation Fidelity

Перевод MUST сохранять materially significant Action semantics.

Особенно необходимо различать:

    attempted
    ≠ completed

    started
    ≠ finished

    partially
    ≠ fully

    intentionally
    ≠ accidentally

    directly
    ≠ indirectly

    may have acted
    ≠ acted

Перевод или summary MUST NOT вводить Actor attribution, отсутствующую в Source.

Например:

    "The valve was opened"

MUST NOT автоматически превращаться в:

    "Operator opened the valve"

если identity Actor не установлена.

Неоднозначность оригинала не должна превращаться в ложную точность.

---

# 47. Logical Fidelity

Representation SHOULD сохранять materially significant:

- negation;
- quantifiers;
- exceptions;
- conditions;
- conjunction/disjunction;
- temporal relations.

Например:

    did not open
    ≠ opened

    opened 3 of 5
    ≠ opened all 5

    A or B
    ≠ A and B

    only after T
    ≠ before T

---

# 48. Import и archival provenance

При импорте необходимо сохранять semantic/provenance distinctions между, например:

- directly recorded Action;
- reported Action;
- observed Action;
- inferred Action;
- reconstructed Action;
- disputed Action;
- unknown.

Эти distinctions не образуют обязательный закрытый Core enum.

Конкретный Profile MAY использовать собственную vocabulary.

External labels вроде:

- execution;
- operation;
- procedure;
- activity;
- intervention;

не становятся canonical Action только из-за названия.

Необходим semantic analysis.

---

# 49. Conflicting records

Конфликтующие свидетельства об Action MUST NOT принудительно сливаться в одно ложнопределённое representation.

Допустимо сохранять:

- competing Claims;
- competing reconstructions;
- disputed Actor attribution;
- disputed timing;
- disputed Scope;
- disputed Method;
- disputed causal relations.

Разрешение конфликта должно следовать соответствующей epistemic architecture проекта.

---

# 50. Damaged / incomplete records

Частичный material MAY сохраняться даже если он недостаточен для completed canonical Action.

Необходимо различать:

    raw / imported / quarantined material
    ≠ completed canonical Action

Частичное знание предпочтительнее выдуманного заполнения.

---

# 51. Offline preservation

Action SHOULD быть представим так, чтобы materially relevant semantics могла быть восстановлена без зависимости от конкретной современной платформы.

Для automated Actions это MAY включать доступную информацию о:

- system;
- version;
- configuration;
- inputs;
- triggering conditions;
- Action Content;
- Actor attribution;
- Scope;
- timing;
- uncertainty.

Offline preservation не требует полного воспроизведения исходной системы, если это невозможно.

---

# 52. Carrier neutrality

Action semantics не зависит от носителя.

Action MAY храниться в:

- базе данных;
- Markdown;
- JSON;
- печатном документе;
- журнале;
- архиве;
- иной долговременно интерпретируемой форме.

Носитель не определяет ontology Action.

---

# 53. Safety-critical Actions

Для Action с высоким потенциальным вредом Profile SHOULD иметь возможность требовать более строгую структуру.

Например:

- Actor;
- qualification/role;
- Decision/authorization relation;
- Procedure version;
- Method;
- timing;
- Scope;
- inputs/materials;
- uncertainty;
- provenance;
- Result monitoring.

Но эти требования не становятся универсальным Core minimum для всех Actions.

---

# 54. Action quality

`008` не вводит intrinsic universal Action Quality.

Такие свойства, как:

- safety;
- legality;
- precision;
- efficiency;
- ethical acceptability;
- procedural conformity;
- effectiveness;
- reversibility;

при необходимости представляются через Assessment или другую соответствующую semantics.

Набор quality aspects открыт и MAY определяться Profile или предметной областью.

---

# 55. Conformance и Integrity

Необходимо различать:

    Core structural/semantic conformance
    ≠ historical/provenance integrity
    ≠ Action quality
    ≠ procedural/legal status
    ≠ causal certainty
    ≠ Representation Fidelity

Core Conformance отвечает на вопрос, соответствует ли Action минимальным структурным и семантическим требованиям `008`.

Historical/Provenance Integrity отвечает на вопрос, насколько честно сохранены:

- происхождение;
- attribution;
- historical States;
- uncertainty;
- известная история Action.

Следовательно:

    Core PASS
    ≠ Action historically certain
    ≠ Action good
    ≠ Action authorized
    ≠ Action successful
    ≠ causal relation proven

---

# 56. Core и Profiles

Profile MAY усиливать требования Core.

Например:

    medical Action Profile
    industrial safety Action Profile
    historical Action Profile
    automated system Action Profile

MAY требовать разные дополнительные semantics и проверки.

Profile MUST NOT ослаблять Core, продолжая заявлять совместимость с `008`.

---

# 57. Диагностические семейства

Diagnostic terminology описывает semantic failure patterns и не создаёт новые Core Entities.

## 57.1. Identity / granularity failures

Примеры:

- один Action ошибочно разделён на несколько;
- разные Actions ошибочно объединены;
- Correction представлена как новый Action;
- repeated Actions ошибочно схлопнуты;
- один occurrence искусственно сегментирован без основания.

## 57.2. Attribution / provenance failures

Примеры:

- неверный Actor;
- operator → Decision-maker;
- passive wording → invented Actor;
- expected Method → actual Method;
- inferred Action → observed Action;
- unknown intention → invented intention.

## 57.3. Scope / Context failures

Примеры:

- partial → complete;
- local → universal;
- Intended Scope → Action Scope;
- Action Scope → Effect Scope;
- current Context → historical Context.

## 57.4. Execution / Result / causality failures

Примеры:

- Decision → Action;
- Action → faithful Execution;
- Action → Result;
- sequence → causation;
- trigger → sole causation;
- Objective achieved → Action effective.

## 57.5. Representation / Import failures

Примеры:

- attempted → completed;
- approximate time → exact time;
- reported → observed;
- historical Action → current Instruction;
- uncertainty → false precision;
- duplicate representation → multiple Actions.

Diagnostic label сам по себе не устанавливает:

- intent;
- fraud;
- negligence;
- responsibility;
- moral blame.

---

# 58. Machine validation

Validator MAY проверять:

- обязательную структуру;
- reference integrity;
- Profile requirements;
- определённые semantic constraints.

Но:

    validator PASS
    ≠ Action historically certain
    ≠ Action safe
    ≠ Action legal
    ≠ Action successful
    ≠ causal relation proven

Validator не обладает привилегией истины и сам MAY быть ошибочным.

---

# 59. Cross-standard compatibility

`008-ACTION` должен сохранять границы между соседними Records и semantics.

В компактной форме:

    Claim
    → что утверждается

    Evidence Use
    → что используется как evidence

    Assessment
    → как что-либо оценивается

    Inference
    → что выводится

    Decision
    → что решено

    Action
    → что сделано

    Result
    → что произошло / наблюдалось

Следовательно:

    Claim about Action
    ≠ Action

    Decision to perform A
    ≠ Action A

    Plan for A
    ≠ Action A

    Procedure describing A
    ≠ Action A

    Assessment of A
    ≠ Action A

    Result after A
    ≠ Action A

Action Record также MUST NOT автоматически означать epistemic certainty того, что historical enactment occurred exactly as represented.

`008` не должен поглощать ontology соседних стандартов.

---

# 60. Boundary concepts outside full 008 ontology

`008` использует ряд соседних concepts только для установления границ относительно Action.

К ним относятся, например:

- Event;
- Process;
- Result;
- Effect;
- Consequence;
- Plan;
- Procedure;
- Instruction.

`008` не утверждает, что их полная ontology должна находиться внутри стандарта Action.

Они MAY иметь собственные Records, generic infrastructure или будущие стандарты.

---

# 61. Entity Explosion Test

`008` НЕ требует введения следующих фундаментальных Core Entities только ради представления Action:

- ActionContent;
- ActionActor;
- ActionTarget;
- ActionContext;
- ActionScope;
- IntendedScope;
- EffectScope;
- ActionMethod;
- ActionIntention;
- ActionMotivation;
- Attempt;
- Omission;
- ActionState;
- ActionLifecycle;
- ActionSequence;
- ActionGroup;
- CompositeAction;
- RepeatedAction;
- ContinuousAction;
- AutomatedAction;
- Execution;
- DirectEffect;
- ActionResult;
- ActionEffect;
- ActionSuccess;
- ActionEffectiveness;
- ActionQuality;
- ActionFailure.

Эти понятия MAY быть представлены через:

- semantic roles;
- relations;
- States;
- Profiles;
- существующие Records;
- generic project infrastructure;
- будущие специализированные стандарты.

Отсутствие отдельной Core Entity не означает отсутствия соответствующей semantics.

---

# 62. Core invariants

Следующие положения образуют минимальное нормативное ядро `008-ACTION`.

### A-01
Action является specialized Record, представляющим enactment, представленное как произошедшее.

### A-02
Action MUST иметь defined Action Content.

### A-03
Action MUST сохранять sufficient enactment attribution; identity конкретного Actor MAY быть unknown.

### A-04
Mere occurrence, natural change или causal activity MUST NOT автоматически классифицироваться как Action.

### A-05
Action MUST оставаться различимым от Decision, Event, Process, Plan, Procedure, Instruction и Result.

### A-06
Action existence MUST NOT автоматически означать intention, authorization, legality, legitimacy, correctness, success или effectiveness.

### A-07
Action MUST NOT автоматически считаться Execution какого-либо Decision, Plan, Procedure или Instruction.

### A-08
Execution relation MUST NOT автоматически означать полное соответствие, authorization или success.

### A-09
Actor attribution MUST NOT автоматически означать Decision-maker attribution, authority, responsibility или accountability.

### A-10
Unknown, partial или disputed Action semantics MUST NOT заменяться invented, default, current или merely plausible semantics.

### A-11
Omission MAY представляться как Action только при sufficient attribution non-performance в materially relevant and sufficiently grounded frame.

### A-12
Attempt MUST NOT автоматически представляться как completion или success.

### A-13
Completion/failure semantics MUST интерпретироваться относительно определённого Action Content или другого reference/semantic target.

### A-14
Same Action Content MUST NOT автоматически означать same Action.

### A-15
Different wording, abstraction или decomposition MUST NOT автоматически создавать разные Action identities.

### A-16
Granularity indicators MUST NOT индивидуально определять Action identity.

### A-17
Intended Scope, Action Scope и Effect Scope MUST оставаться различимыми.

### A-18
Prescribed Method MUST NOT автоматически представляться как actual Method.

### A-19
Historical Action semantics MUST NOT незаметно смещаться к current States связанных Records, systems, Procedures или Contexts.

### A-20
Correction MUST сохранять identity того же historical enactment; новое осуществление MUST быть представлено новым Action.

### A-21
Action relations MUST сохранять materially relevant provenance и MUST NOT автоматически означать identity, causality, intention или responsibility.

### A-22
Temporal succession MUST NOT автоматически интерпретироваться как causation.

### A-23
Action MUST оставаться различимым от Result, Objective Achievement и Effectiveness.

### A-24
Historical Action MUST NOT автоматически представляться как current Recommendation или Instruction.

### A-25
Core structural/semantic conformance MUST оставаться различимым от historical/provenance integrity, Action quality, procedural/legal status, causal certainty и Representation Fidelity.

### A-26
Repeated или continuous activity MUST NOT получать ложную identity/granularity без достаточного основания.

### A-27
Translation или summarization MUST NOT вводить отсутствующую Actor attribution или иную ложную precision.

### A-28
Profile MAY усиливать Core requirements, но MUST NOT ослаблять Core, продолжая заявлять совместимость с `008`.

### A-29
Materially relevant uncertainty и provenance MUST оставаться resolvable.

### A-30
Duration, continuity или repetition MUST NOT сами по себе определять, является ли represented occurrence Action, Process, одним Action или множеством Actions.

---

# 63. Stress-test framework

Архитектура `008-ACTION` должна выдерживать как минимум следующие классы атак:

1. минимальные и частично известные Actions;
2. неизвестный Actor при известной actionality;
3. Decision без Action;
4. Action без известного Decision;
5. Action vs natural Event;
6. Action vs Process;
7. attempted / interrupted / partial Actions;
8. deliberate omission;
9. коллективные и распределённые Actions;
10. automated Actions;
11. sensor / controller / actuator attribution;
12. repeated и continuous Actions;
13. remote Actions;
14. conflicting Actor attribution;
15. prescribed Method ≠ actual Method;
16. Intended Scope ≠ Action Scope;
17. Action Scope ≠ Effect Scope;
18. multiple Actions with identical Content;
19. different descriptions of one Action;
20. one composite Action vs multiple independent Actions;
21. historical-state drift;
22. Execution attribution;
23. partial/deviating Execution;
24. Result without causality;
25. trigger without full downstream causation;
26. causal uncertainty;
27. archival/import corruption;
28. passive wording and missing Actor;
29. translation corruption;
30. future-system Actions;
31. offline reconstruction;
32. safety-critical Profiles;
33. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если тест обнаруживает необходимое фундаментальное правило, оно должно быть внесено в соответствующий нормативный раздел стандарта.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 64. Принцип сохранения

При конфликте между полнотой и честностью представления предпочтение отдаётся честности.

    partial knowledge
    > invented completion

    uncertainty preserved
    > false certainty

    unknown Actor
    > invented Actor

    unknown Method
    > assumed Method

    unknown causality
    > post hoc causality

    partial Action
    > falsely completed Action

    ambiguous granularity
    > invented segmentation

Цель стандарта — не создать идеально заполненную запись.

Цель — сохранить Action настолько полно, насколько позволяют данные, **не выдавая неизвестное за известное и не превращая намерение, Decision, Plan, Event или Result в Action**.

---

# 65. Итоговая формула

В наиболее компактной форме:

    Decision
    → что было решено

    Action
    → что было сделано

    Execution
    → отношение Action к тому,
      что оно реализует или исполняет

    Result
    → что произошло / наблюдалось

    Assessment
    → как это оценивается

    Inference
    → что из этого выводится

Центральный принцип `008-ACTION`:

> **Сохранить Action — значит сохранить максимально честное представление о том, что было осуществлено как действие, какой Action Content ему приписывается и в каких materially relevant границах это произошло.**

Факт Action сам по себе не означает его намеренность, правильность, законность, соответствие Decision, успешность или причинность последующего Result.

---

## Статус версии

**008-ACTION v0.1**

Архитектура прошла:

- первичную полную сборку;
- сквозную атаку всего стандарта;
- контрольный аудит собранного файла;
- проверку границ Action / Decision / Event / Process / Result;
- проверку Actor model;
- проверку Attempt / Completion / Omission;
- проверку granularity;
- проверку repeated / continuous Actions;
- проверку Execution semantics;
- проверку causal boundaries;
- проверку compatibility с `007-DECISION`;
- Entity Explosion Test.

**Критических архитектурных противоречий: 0.**  
**Новых обязательных Core Entities: 0.**  
**Невнесённых замечаний контрольного аудита: 0.**

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
