# 007 — DECISION
## Стандарт представления решений

**Проект:** Энциклопедия цивилизации  
**Статус:** рабочий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются решения — человеческие, коллективные, институциональные, автоматизированные и иные акты разрешения decision question или Decision Space.

Цель стандарта — позволить сохранять:

- что именно было решено;
- кем или чем решение было принято, если это известно;
- относительно какого пространства возможностей происходило решение;
- на каком основании решение принималось;
- каким процессом оно было получено;
- в каком контексте оно существовало;
- на какую область распространялось;
- как оно связано с другими решениями;
- было ли оно реализовано;
- какие результаты наблюдались;
- что известно, неизвестно, реконструировано или оспаривается.

Стандарт не предназначен для автоматического определения того, является ли решение:

- истинным;
- правильным;
- разумным;
- законным;
- легитимным;
- этичным;
- безопасным;
- выполненным;
- успешным;
- рекомендуемым сейчас.

Сохранить решение означает сохранить максимально честное представление о том, **что было решено и какой исторический смысл может быть обоснованно приписан этому акту**.

---

# 1. Основное понятие

## 1.1. Decision

**Decision (Решение)** — специализированный Record, представляющий определённый акт разрешения *decision question* или *Decision Space*, в котором один определённый **Decision Outcome construct** представлен как выбранный, принятый, отклонённый, установленный, отложенный либо иным образом определённый посредством определённой семантики разрешения решения (*decision-resolution semantics*).

Decision является представлением акта решения, а не утверждением о правильности этого решения.

Decision act является функционально-семантическим понятием.

Он не требует обязательного наличия:

- человеческого сознания;
- психологического размышления;
- формального голосования;
- явно перечисленных альтернатив;
- рациональной оптимизации.

Decision может быть:

- индивидуальным;
- коллективным;
- институциональным;
- автоматизированным;
- распределённым;
- основанным на определённой случайной процедуре.

Однако любой вычислительный результат, рекомендация, прогноз, команда или действие не становятся Decision только потому, что были произведены человеком или системой.

---

# 2. Минимальная структура завершённого Decision

Для представления завершённого Decision необходимо как минимум:

1. определённый decision act;
2. ровно один определённый Decision Outcome construct;
3. разрешимая атрибуция того, что данный Outcome действительно был решён.

Формально:

    defined decision act
    +
    exactly one defined Decision Outcome construct
    +
    resolvable attribution that the Outcome was decided

Это минимальное требование Core.

Для существования исторического Decision не обязательно, чтобы были известны:

- Decision-maker;
- полный Decision Space;
- Alternatives;
- Decision Basis;
- Decision Process;
- Decision Context;
- Execution;
- Result.

Неизвестность этих элементов не уничтожает Decision, если сам акт решения и его Outcome достаточно установлены.

Если известно только содержание `A`, но неизвестно, было ли `A` решено, рекомендовано, предложено, спрогнозировано или просто произошло, этого недостаточно для завершённого Decision.

---

# 3. Decision Outcome

## 3.1. Определение

**Decision Outcome** — содержание, представленное как разрешение конкретного decision-resolution act.

Outcome отвечает на вопрос:

> **Что было решено?**

Decision Outcome является семантической ролью или конструкцией содержания.

Он не является обязательной отдельной Core Entity.

## 3.2. Кардинальность

Завершённый Decision MUST иметь:

    exactly one defined Decision Outcome construct

Outcome может быть:

- атомарным;
- структурированным;
- условным;
- составным в пределах одного интегрированного resolution act.

Например:

    эвакуировать сектор A;
    закрыть дорогу B;
    открыть убежище C;
    провести повторную оценку в 18:00.

может являться одним структурированным Outcome, если исторически это было одним интегрированным актом решения.

Но структурированный Outcome MUST NOT использоваться для искусственного объединения независимых decision acts.

Если компоненты независимо:

- принимались;
- отменялись;
- изменялись;
- вступали в силу;
- имели собственный lifecycle,

это является сильным основанием рассматривать их как отдельные Decisions.

## 3.3. Outcome и тип содержания

Роль Decision Outcome не заменяет онтологию содержания.

Например:

    Decision adopts Policy P

не превращает Policy P в Decision Outcome Entity.

Policy остаётся Policy и занимает роль Outcome в конкретном Decision.

Аналогично Decision может:

- принять Claim как рабочее допущение;
- установить правило;
- назначить лицо;
- определить приоритет;
- распределить ресурс.

---

# 4. Decision Space

## 4.1. Определение

**Decision Space (Пространство решения)** — пространство возможностей, относительно которого происходит или представляется resolution.

Decision Space отвечает на вопрос:

> Между чем, относительно чего или в каком пространстве возможностей происходило решение?

Decision Space может быть:

- дискретным;
- непрерывным;
- структурированным;
- частично известным;
- не полностью перечислимым.

## 4.2. Alternatives

Alternative не является обязательной Core Entity.

Явный список Alternatives не требуется для каждого Decision.

Необходимо различать:

    physically possible
    ≠ available
    ≠ known
    ≠ considered
    ≠ feasible
    ≠ admissible
    ≠ selected

Decision Space MUST NOT незаметно объединять объективно возможные, воспринимаемые Decision-maker, известные ему, процедурно допустимые и фактически рассматривавшиеся возможности, когда это различие materially relevant.

Следовательно:

    objective possibility space
    ≠ perceived space
    ≠ known space
    ≠ procedurally admissible space
    ≠ actually considered space

Эти различия являются semantic dimensions, а не обязательной universal status schema для каждой Alternative.

Decision Space не означает совокупность всех физически возможных действий.

Он может отражать только пространство, которое:

- было известно;
- рассматривалось;
- допускалось процедурой;
- было доступно;
- исторически реконструируется.

Неизвестные Alternatives MUST NOT изобретаться для заполнения модели.

## 4.3. Decision Space ≠ Decision Scope

Decision Space и Decision Scope являются разными понятиями.

    Decision Space
    → относительно каких возможностей происходит resolution

    Decision Scope
    → к какой области применяется выбранный Outcome

Например:

    Space:
    evacuate / remain

    Outcome:
    evacuate

    Scope:
    Sector A

---

# 5. Decision Basis

## 5.1. Определение

**Decision Basis (Основание решения)** — представленная или атрибутированная materially relevant semantics, которой приписывается участие в разрешении конкретного Decision Space и определении Outcome.

Basis может включать, где применимо:

- Claims;
- Evidence;
- Inferences;
- Assessments;
- Objectives;
- Criteria;
- Constraints;
- Values;
- Preferences;
- Policies;
- Rules;
- другую релевантную информацию.

Но Decision Basis не означает «всё, что относилось к ситуации».

## 5.2. Различия

Необходимо различать:

    known
    ≠ mentioned
    ≠ available
    ≠ considered
    ≠ used
    ≠ causally influential

Наличие материала в документе, архиве или информационном пакете не доказывает его использование в Decision Basis.

Basis membership также не доказывает психологическую причинность.

Следует различать, когда это существенно:

- contemporaneous recorded Basis;
- stated reason;
- attributed Basis;
- later justification;
- reconstruction;
- inferred motivation;
- causal explanation.

Позднейшее объяснение MUST NOT автоматически становиться историческим Basis.

Recorded или attributed Decision Basis MUST NOT автоматически считаться полной или исключительной Basis, если её completeness или exclusivity не установлены отдельно.

Следовательно:

    recorded Basis
    ≠ complete Basis

    listed reasons
    ≠ only reasons

Отсутствующий factor также MUST NOT автоматически считаться не участвовавшим в Decision.

## 5.3. Семантические роли

Objective, Criterion, Constraint, Value, Preference, Weight и сходные понятия являются в рамках этого стандарта семантическими ролями или концептами.

`007` не требует создавать для них отдельные Core Entities.

Одно и то же содержание MAY занимать несколько ролей, если materially relevant различия между этими ролями остаются разрешимыми.

---

# 6. Decision Process

## 6.1. Определение

**Decision Process (Процесс решения)** — представление того, каким процессом или механизмом происходил decision-resolution act.

Он может включать:

- deliberation;
- proposal;
- voting;
- review;
- approval;
- consultation;
- certification;
- algorithmic resolution;
- randomized procedure;
- иные стадии.

Decision Process не является обязательной отдельной Core Entity.

## 6.2. Procedure ≠ Process

Необходимо различать:

    Procedure
    → как процесс должен был происходить

    Decision Process
    → как представлено, что он происходил фактически

Знание официальной процедуры не позволяет автоматически реконструировать фактическую историю.

## 6.3. Голосование и коллективные решения

Само голосование не является автоматически Decision.

    vote
    ≠ Decision

    vote result
    ≠ Decision Outcome automatically

    majority
    ≠ consensus

    approval stage
    ≠ final Decision automatically

То, каким образом голосование, согласование или иная процедура преобразуется в Decision, определяется применимой процедурной или governance semantics.

---

# 7. Decision-maker

## 7.1. Определение

**Decision-maker** — actor, collective, institution, system или определённый process, которому в представленной procedural/governance semantics атрибутируется конкретный decision act.

Decision-maker является ролью атрибуции.

Он не обязан быть отдельным человеком.

## 7.2. Запрещённые автоматические отождествления

Не следует автоматически считать Decision-maker того, кто:

- участвовал;
- голосовал;
- предложил вариант;
- рекомендовал;
- записал решение;
- объявил его;
- исполнил;
- технически подтвердил;
- несёт ответственность.

То есть:

    participant
    voter
    recommender
    recorder
    announcer
    executor
    accountable actor

    ≠ Decision-maker automatically

## 7.3. Неизвестный Decision-maker

Если надёжно установлено, что Decision произошёл, но Decision-maker неизвестен, Decision может быть сохранён как частично известный.

    Decision occurred
    + maker unknown
    → valid partial historical representation

Но:

    unknown whether Decision occurred
    ≠ known Decision

---

# 8. Human, collective и automated Decisions

Decision не является исключительно человеческой категорией.

Автоматизированная система MAY быть представлена как Decision-maker или часть decision-resolution process, если применимая системная семантика действительно назначает ей функцию разрешения решения.

Необходимо различать:

    prediction
    ≠ recommendation
    ≠ ranking
    ≠ Decision
    ≠ Execution

AI output не является Decision автоматически.

Human click также не является человеческим Decision автоматически.

Система может:

- рекомендовать, а человек решать;
- решать, а человек подтверждать получение;
- решать и исполнять;
- участвовать только в Assessment;
- участвовать только в Execution.

Decision attribution определяется фактической процедурной и governance semantics, а не интерфейсом.

---

# 9. Decision Context

## 9.1. Определение

**Decision Context (Контекст решения)** — внешние условия, состояния или обстоятельства, materially необходимые для интерпретации, применимости или исторического понимания Decision.

Context может включать:

- время;
- место;
- состояние среды;
- emergency conditions;
- применимые правила;
- версии систем;
- институциональное состояние;
- другие условия.

## 9.2. Context ≠ Basis ≠ Scope ≠ Authority

Необходимо различать:

    Context
    → внешние условия интерпретации/applicability

    Basis
    → semantics, использованная или атрибутированная в resolution

    Scope
    → область действия Outcome

    Authority
    → semantics полномочий в соответствующей governance system

Одно содержание MAY участвовать в нескольких ролях, но роли не должны незаметно схлопываться.

---

# 10. Decision Scope

**Decision Scope (Область действия решения)** — область, к которой относится decision force выбранного Outcome.

Scope может ограничиваться:

- территорией;
- населением;
- объектами;
- организациями;
- временем;
- условиями;
- системой;
- версией;
- другими параметрами.

Неизвестная граница MUST NOT автоматически становиться универсальной.

    territory unknown
    ≠ global

    duration unknown
    ≠ permanent

    population unknown
    ≠ everyone

    Context unknown
    ≠ current/default Context

## 10.1. Три разных Scope

Необходимо различать:

    Decision Scope
    → на что было направлено решение

    Execution Scope
    → что фактически охватило исполнение

    Affected Result Scope
    → что фактически оказалось затронуто

Они не наследуют друг друга автоматически.

---

# 11. Семантическая граница Decision

**Decision Semantic Boundary (Семантическая граница решения)** — совокупность materially relevant semantics, необходимых для сохранения identity, interpretation, applicability и historical attribution конкретного Decision.

В зависимости от случая она MAY включать:

- Decision-maker attribution;
- Decision Space;
- Decision Basis;
- Decision Process;
- Decision Context;
- Decision Outcome;
- decision force;
- Decision Scope;
- time;
- authority/procedural semantics;
- historical States.

Decision Semantic Boundary:

- не является отдельной Core Entity;
- не является обязательным фиксированным payload;
- не является универсальным checklist.

Состав границы определяется тем, какие semantics materially необходимы для конкретного Decision.

---

# 12. Materiality

**Materially relevant / materially required** — semantics, отсутствие, изменение или искажение которой способно изменить:

- Decision identity;
- decision force;
- historical attribution;
- applicability;
- current interpretation;
- либо существенно повлиять на downstream use.

Materiality зависит от конкретного случая и цели использования.

---

# 13. Resolvability

**Resolvable (разрешимый)** — semantic role, content, relation, State или historical meaning которого может быть восстановлен из сохранённой структуры, references или provenance без изобретения отсутствующего смысла.

Resolvable не означает:

- обязательно встроенный локально;
- обязательно доступный через интернет;
- обязательно содержащий все детали.

Offline-представление MAY использовать ссылки и структуры при условии, что необходимые semantics могут быть восстановлены из сохраняемой системы.

---

# 14. Unknown, partial и disputed semantics

Unknown, partial или disputed Decision semantics MUST NOT заменяться:

- invented semantics;
- default semantics;
- current semantics;
- merely plausible semantics.

Если исторически неизвестно:

    unknown
    MUST remain unresolved

если только inference или reconstruction не представлены отдельно с собственной provenance.

Следовательно:

    unknown Basis
    ≠ plausible rationale

    unknown Process
    ≠ expected Procedure

    unknown Scope
    ≠ universal Scope

    unknown duration
    ≠ permanent

Неопределённость является допустимым состоянием знания и не должна устраняться выдумыванием.

---

# 15. Identity

Decision identity следует историческому decision act, а не текстовому совпадению.

    same Outcome
    ≠ same Decision

Два Decision могут иметь:

- одинаковый Outcome;
- одного Decision-maker;
- одинаковый Basis;
- одинаковый Space;

и всё равно быть разными Decisions, если существовали разные decision acts.

Обратное также верно:

разные архивные представления одного исторического act не должны автоматически становиться несколькими Decisions.

---

# 16. Correction и новое Decision

**Correction** исправляет представление того же исторического decision act.

**New Decision / Re-decision** представляет новый resolution act.

Изменение Outcome, Scope, force или conditions MAY считаться Correction только если имеется основание считать, что исправленная semantics принадлежала исходному историческому акту.

Если новая semantics появилась в результате нового resolution act, требуется новый Decision.

    correction
    ≠ re-decision

---

# 17. Lifecycle

Decision может участвовать в lifecycle semantics, включая, где применимо:

- activation;
- suspension;
- expiration;
- revocation;
- supersession;
- reinstatement;
- amendment;
- другие Profile-defined states или relations.

Но Core не требует закрытого универсального lifecycle enum.

Необходимо сохранять:

    revoked
    ≠ never existed

    superseded
    ≠ false

    not executed
    ≠ revoked

    latest
    ≠ currently effective automatically

Lifecycle может быть графом, а не линейной последовательностью.

Lifecycle relations MAY сами быть:

- directly recorded;
- inferred;
- computed;
- reconstructed;
- disputed.

Их provenance, Scope и uncertainty MUST оставаться различимыми, когда это materially relevant.

Следовательно:

    recorded revocation
    ≠ inferred revocation

    computed supersession
    ≠ explicitly declared supersession

    disputed lifecycle relation
    ≠ undisputed historical fact

---

# 18. Decision State

Стандарт не вводит универсальное свойство:

    Decision.state

поскольку необходимо различать как минимум:

- lifecycle state самого Record;
- decision force/effect state;
- Execution state;
- Result/achievement state.

Эти измерения не должны схлопываться в один универсальный статус.

---

# 19. Current force и applicability

Текущая сила или применимость Decision может зависеть от:

- времени;
- Scope;
- Context;
- jurisdiction;
- условий;
- authority rules;
- последующих Decisions;
- Profile;
- других факторов.

Поэтому:

    Decision.active = true

или:

    Decision.applicable = true

не должны использоваться как универсальные контекстно-независимые утверждения.

Current force и applicability являются relational/contextual semantics.

---

# 20. Historical State preservation

Исторический Decision MUST NOT незаметно изменяться вслед за текущим состоянием связанных объектов.

Например:

    Assessment A.Result@T1
    ≠ A.Result@current

    Region X@T1
    ≠ Region X@current

    Procedure P@T1
    ≠ P@current

    Model M@v1
    ≠ M@v5

Если историческое состояние materially важно, оно должно оставаться разрешимым.

Позднейшая информация MUST NOT незаметно добавляться в исторический Basis, Process, Context или Outcome.

---

# 21. Transfer и reuse

Использование Decision за пределами исходной Semantic Boundary не расширяет исходный Decision автоматически.

Необходимо различать:

    application inside original Scope
    → original applicability / Execution

    reuse outside original boundary
    → transfer/applicability question

    new resolution in new context
    → new Decision

`007` не вводит обязательную отдельную DecisionTransfer Entity.

---

# 22. Relations между Decisions

Decisions MAY быть связаны различными отношениями, например:

- supersedes;
- depends on;
- conflicts with;
- authorizes;
- triggers;
- coordinates with;
- modifies;
- implements;
- другими отношениями.

По возможности следует использовать общую relation infrastructure проекта, а не создавать параллельную ontology только для Decisions.

## 22.1. Provenance отношений

Relation между Decisions сама является знанием и MAY быть:

- directly recorded;
- computed;
- inferred;
- assessed;
- reconstructed;
- disputed.

Если provenance отношения materially важна, она должна сохраняться.

    inferred dependency
    ≠ recorded dependency

    computed supersession
    ≠ historical statement of supersession

## 22.2. Distinct ≠ independent

Два разных Decision не являются автоматически независимыми.

    distinct
    ≠ independent

И:

    no known dependency
    ≠ proven independence

Положительное утверждение независимости требует основания, если оно materially важно.

---

# 23. Conflict

Противоположные формулировки сами по себе не доказывают актуальный конфликт.

Conflict обычно требует:

    materially aligned Semantic Boundaries
    +
    incompatible decision forces
    +
    applicable system semantics

Следовательно:

    opposite text
    ≠ conflict automatically

    conflict
    ≠ supersession

    precedence
    ≠ supersession

    higher authority
    ≠ correctness

General rule и specific exception MAY сосуществовать без противоречия, если применимая semantics это допускает.

---

# 24. Coordination и joint Decisions

Несколько согласованных Decisions не становятся автоматически одним Decision.

    coordination
    ≠ joint Decision

Joint Decision возможен, когда имеется один decision act со структурированной или коллективной maker attribution.

Joint Decision является конфигурацией provenance, а не обязательным отдельным subtype.

---

# 25. Decision, Execution и Result

Необходимо строго различать:

    Decision Outcome
    → что было решено

    Execution
    → что было сделано или предпринято для реализации

    Result
    → что наблюдалось после

    Consequence
    → Result/event с атрибутированной consequential relation

    Outcome Realization
    → реализовалось ли то, что было решено

    Objective Achievement
    → была ли достигнута цель

    Effectiveness
    → способствовало ли Decision/Execution достижению цели

Следовательно:

    Outcome
    ≠ Execution
    ≠ Result
    ≠ Objective Achievement
    ≠ Effectiveness

---

# 26. Execution

Decision может:

- быть исполнен полностью;
- быть исполнен частично;
- не быть исполнен;
- быть исполнен после утраты силы;
- быть исполнен за пределами Scope;
- иметь множество execution acts.

Execution не изменяет исторический Outcome автоматически.

Совпадение действия с Decision не доказывает, что действие являлось Execution этого Decision.

    matching action
    ≠ Execution automatically

---

# 27. Result и causality

Событие, произошедшее после Decision, не становится автоматически его следствием.

    D at T1
    R at T2

не означает:

    D caused R

Causal attribution требует соответствующей Evidence, Inference, Assessment, модели или другой допустимой semantics.

Temporal succession MUST NOT автоматически интерпретироваться как causation.

---

# 28. Outcome Realization, Objective Achievement и Effectiveness

Необходимо различать:

    Outcome realized
    ≠ Objective achieved

и:

    Objective achieved
    ≠ Decision effective

Цель может быть достигнута по причинам, не связанным с Decision.

Outcome может быть полностью реализован, но Objective — не достигнут.

Decision может способствовать Result вместе с множеством других причин.

Стандарт не вводит универсальный `Decision.success` boolean.

---

# 29. Ex ante и ex post evaluation

Необходимо различать:

    Was the Decision reasonable
    given information available at T1?

и:

    Did the Decision produce
    a good Result at T2?

Хороший Result не доказывает хорошее ex ante Decision.

Плохой Result не доказывает плохое ex ante Decision.

Позднейшие Results MUST NOT незаметно переписываться в исторический Decision Basis.

---

# 30. Constitutive Decisions

Некоторые Decisions могут непосредственно конституировать institutional или normative state, если применимая governance semantics определяет такой эффект.

Например:

- назначить лицо на должность;
- принять Policy;
- установить институциональное правило;
- объявить определённый нормативный статус.

Это не нарушает различие между Decision и Result.

Decision MAY непосредственно создавать определённое institutional/normative состояние, но не становится автоматически unrelated empirical или physical Result.

Например:

    Decision:
    demolish building

не означает:

    building was demolished

---

# 31. Decision quality

`007` не вводит intrinsic universal Decision Quality.

Такие вопросы, как:

- rationality;
- safety;
- legality;
- legitimacy;
- ethical acceptability;
- robustness;
- reversibility;
- effectiveness;
- другие quality aspects,

при необходимости представляются через Assessment или другую соответствующую semantics.

Набор quality aspects является открытым и может определяться Profile или предметной областью.

---

# 32. Existence, validity, legitimacy и authority

Необходимо различать:

    historical Decision existence
    ≠ legal validity
    ≠ procedural validity
    ≠ legitimacy
    ≠ authority
    ≠ correctness

Unauthorized, illegal, procedurally flawed, irrational или harmful Decision всё равно может быть исторически существовавшим Decision.

Поэтому Core не вводит универсальное свойство:

    Decision.valid

без указания того, что именно означает `valid`.

---

# 33. Conformance

Необходимо различать:

    Core structural/semantic conformance
    ≠ historical/provenance integrity
    ≠ Decision quality
    ≠ governance/legal status
    ≠ current force
    ≠ Representation Fidelity

**Core Conformance** отвечает на вопрос, соответствует ли Decision структурным и семантическим требованиям данного стандарта.

**Historical/Provenance Integrity** отвечает на вопрос, насколько честно сохранены происхождение, исторические States, attribution, uncertainty и известная история Decision.

Следовательно:

    Core PASS
    ≠ historically true automatically
    ≠ good Decision
    ≠ legitimate Decision
    ≠ successful Decision

## 33.1. Core и Profiles

Profile MAY вводить дополнительные требования.

Например high-risk Profile MAY требовать:

- явный Basis;
- authority provenance;
- uncertainty;
- Scope;
- Process;
- дополнительные проверки.

Поэтому возможно:

    Core PASS
    +
    Profile FAIL

Profile MAY усиливать Core.

Profile MUST NOT ослаблять Core, продолжая заявлять совместимость с ним.

---

# 34. Draft и partial historical knowledge

Необходимо различать:

    Draft
    → lifecycle/work state representation

    Partial historical Decision
    → неполнота сохранившегося знания

Они могут пересекаться, но не являются одним понятием.

Неполный исторический Record не должен автоматически считаться Draft.

---

# 35. Integrity и provenance

Decision может быть плохим, но точно сохранённым.

И наоборот, хорошее решение может быть представлено с повреждённой provenance.

    bad Decision
    + accurate record
    → Integrity MAY be intact

    good Decision
    + fabricated history
    → Integrity failure

Известная provenance должна сохраняться настолько, насколько это materially необходимо.

Отсутствующая provenance MUST NOT изобретаться.

---

# 36. Attribution integrity

Необходимо избегать необоснованного приписывания:

- Decision-maker;
- Basis;
- Objectives;
- Values;
- Process;
- Context;
- authority;
- motives;
- relations.

Например:

    P announced A
    ≠ P decided A

    P decided A
    ≠ P legitimately decided A

    P voted for A
    ≠ P was institutional Decision-maker

---

# 37. Representation Fidelity

Canonical data может быть корректной, а её представление — вводящим в заблуждение.

Поэтому Representation Fidelity является отдельным измерением.

Представление MUST NOT materially искажать:

- Outcome;
- decision force;
- Scope;
- Context;
- time;
- maker attribution;
- lifecycle;
- provenance;
- relation semantics.

## 37.1. Lossy representation

Сокращённое или lossy representation не является ошибкой автоматически.

Оно допустимо, если опущенная semantics не изменяет materially интерпретацию для заявленной или разумно подразумеваемой цели представления.

## 37.2. Translation Fidelity

Перевод MUST сохранять materially significant decision semantics.

Особенно необходимо различать:

    may
    ≠ must

    recommend
    ≠ decide

    defer
    ≠ reject

    temporary
    ≠ permanent

    local
    ≠ universal

Неоднозначность оригинала не должна превращаться в ложную точность перевода.

## 37.3. Логическая точность

Представление SHOULD сохранять materially significant:

- negation;
- quantifiers;
- exceptions;
- conjunction/disjunction;
- conditional scope.

Например:

    all except C
    ≠ all including C

    at least 3
    ≠ exactly 3

    A or B
    ≠ A and B

---

# 38. Historical Decision ≠ current Recommendation

Исторический Decision не является автоматически современной рекомендацией или инструкцией.

    Historical Decision:
    someone decided A

    ≠

    Recommendation:
    A should be done now

При представлении исторических Decisions система MUST NOT превращать их в текущие указания без отдельного основания.

---

# 39. Decision adopting Claim ≠ Claim truth

Decision может принять Claim как:

- working assumption;
- official position;
- planning premise;
- institutional position.

Но:

    Decision adopts Claim C
    ≠ C is true

Истина Claim определяется соответствующей epistemic semantics, а не фактом его принятия Decision.

---

# 40. Import и архивы

При импорте Decision из внешних систем необходимо сохранять различия между:

- explicitly recorded;
- inferred;
- reconstructed;
- unknown.

Конкретный Profile MAY использовать собственный vocabulary для этих distinctions.

## 40.1. External labels

Внешние названия вроде:

- resolution;
- directive;
- order;
- approval;
- determination;
- command;

не должны автоматически отображаться в canonical Decision только по названию.

Необходимо анализировать их фактическую семантическую функцию.

## 40.2. Conflicting imports

Конфликтующие источники MUST NOT принудительно сливаться в одно якобы достоверное представление.

Допустимо сохранять:

- competing Claims;
- competing reconstructions;
- disputed Decision semantics;
- unresolved uncertainty.

## 40.3. Damaged records

Повреждённый или частичный архивный материал MAY сохраняться даже если он не удовлетворяет требованиям completed Decision.

Необходимо различать:

    raw / imported / quarantined material
    ≠ completed canonical Decision

Частичное знание предпочтительнее выдуманного заполнения пробелов.

---

# 41. Offline preservation

Представление Decision SHOULD, насколько позволяют сохранившиеся данные, позволять будущему читателю восстановить materially relevant semantics без зависимости от конкретной современной платформы.

Offline preservation не требует:

- работающего исходного программного обеспечения;
- доступа к облаку;
- исполняемого AI model;
- исходной базы данных;
- полного воспроизведения proprietary system.

Если Decision был создан автоматизированной системой, достаточно сохранять доступную materially relevant information о:

- системе;
- версии;
- inputs;
- Context;
- Outcome;
- Process/Basis, если известны;
- uncertainty/unknowns.

---

# 42. Carrier neutrality

Decision semantics не должны зависеть от конкретного носителя.

Decision может быть сохранён в:

- базе данных;
- Markdown;
- JSON;
- печатном документе;
- архиве;
- иной долговременно интерпретируемой форме.

Носитель не определяет ontology Decision.

---

# 43. Диагностические семейства

Diagnostic terminology используется для выявления semantic failure patterns.

Она не создаёт новые Core Entities.

Основные семейства:

## 43.1. Identity / lifecycle failures

Примеры:

- False Decision Multiplicity;
- False Decision Collapse;
- новое Decision, представленное как Correction;
- Correction, представленная как новое Decision;
- silent lifecycle rewrite.

## 43.2. Attribution / provenance failures

Примеры:

- неверная Decision-maker attribution;
- invented Basis;
- invented Objectives/Values;
- post-hoc explanation, представленное как historical Basis;
- required Procedure, представленная как фактически произошедший Process.

## 43.3. Context / Scope / Authority failures

Примеры:

- local → universal;
- temporary → permanent;
- unknown → unrestricted;
- Decision attribution → authority;
- unsupported transfer.

## 43.4. Execution / Result / causality failures

Примеры:

- Outcome → executed state;
- matching action → Execution;
- Outcome Realization → success;
- Result → Objective Achievement;
- chronology → causation.

## 43.5. Representation / Import failures

Примеры:

- ambiguous → falsely precise;
- computed → historically recorded;
- majority → consensus;
- historical Decision → current Recommendation;
- duplicate import → multiple Decisions.

Diagnostic label описывает семантический эффект.

Он сам по себе не устанавливает:

- намерение;
- обман;
- мошенничество;
- халатность;
- моральную вину.

---

# 44. Machine validation

Автоматический validator MAY проверять:

- обязательную структуру;
- cardinality;
- reference integrity;
- Profile requirements;
- определённые semantic constraints.

Но:

    validator PASS
    ≠ historically true
    ≠ good Decision
    ≠ legitimate
    ≠ legal
    ≠ safe

Версия и область применимости validator/Profile должны оставаться разрешимыми, когда это materially важно.

Validator сам не обладает привилегией истины и может быть ошибочным.

---

# 45. Stress-test и validation history

Модель `007-DECISION` была проверена на более чем 200 рабочих случаях, охватывающих:

1. минимальные и неполные Decisions;
2. Decision Space и Outcome granularity;
3. Basis, Process и Authority;
4. human, collective и automated Decisions;
5. Context, Scope и transfer;
6. identity и lifecycle;
7. conflict, dependency и coordination;
8. Execution, Result и effectiveness;
9. damaged, historical и imported records;
10. representation и future-system resilience.

В протестированном пространстве случаев не было выявлено:

- критического архитектурного противоречия;
- необходимости изменить cardinality Outcome;
- необходимости ввести новую фундаментальную Core Entity;
- необходимости сделать модель human-centric;
- необходимости сделать модель зависимой от rational-choice framework;
- необходимости схлопывать соседние типы Records.

Прохождение stress-test не является доказательством полноты, истинности или окончательности модели.

Оно означает только отсутствие выявленного архитектурного противоречия в протестированном наборе случаев.

Новые классы случаев MAY потребовать пересмотра стандарта в соответствии с принципом пересматриваемости проекта.

Stress-test cases сами по себе не создают новые Core requirements.

Если тест выявляет новое обязательное правило, оно должно быть включено в соответствующий нормативный раздел стандарта.

---

# 46. Core invariants

Следующие положения образуют минимальное нормативное ядро `007-DECISION`.

### D-01
Decision является specialized Record, представляющим defined decision-resolution act.

### D-02
Completed Decision MUST иметь exactly one defined Decision Outcome construct.

### D-03
Completed Decision MUST сохранять resolvable attribution того, что данный Outcome был решён.

### D-04
Decision Outcome является semantic role/content construct и не требует отдельной Core Entity.

### D-05
Decision MUST оставаться различимым от Claim, Inference, Assessment, Recommendation, Policy, Plan, Authorization, Execution и Result.

### D-06
Существование или Core Conformance Decision MUST NOT означать автоматически его correctness, rationality, legitimacy, authority, legality, execution, success или endorsement.

### D-07
Unknown, partial или disputed Decision semantics MUST NOT заменяться invented, default, current или merely plausible semantics.

### D-08
Decision Space MUST оставаться различимым от Decision Scope.

### D-09
Decision Basis, Decision Process и Decision Context MUST оставаться различимыми.

### D-10
Одно содержание MAY занимать несколько semantic roles, но materially relevant различия между ролями MUST оставаться resolvable.

### D-11
Same Outcome MUST NOT автоматически означать same Decision.

### D-12
Correction MUST сохранять identity того же исторического decision act; materially new decision-resolution act MUST быть представлен новым Decision.

### D-13
Historical Decision semantics MUST NOT незаметно смещаться к current States связанных Records, Contexts, rules, procedures или systems.

### D-14
Decision Context и Scope MUST NOT незаметно расширяться посредством reuse, translation или representation.

### D-15
Decision Scope, Execution Scope и affected Result Scope MUST оставаться различимыми.

### D-16
Decision Outcome MUST оставаться различимым от Execution, Result, Objective Achievement и Effectiveness.

### D-17
Temporal succession MUST NOT автоматически интерпретироваться как causal relation.

### D-18
Decision-maker attribution MUST NOT автоматически означать authority, legitimacy, accountability или correctness.

### D-19
Participant, voter, recommender, recorder, announcer или executor MUST NOT автоматически считаться Decision-maker.

### D-20
Decision relations MUST NOT автоматически означать identity и MUST сохранять materially relevant provenance.

### D-21
Distinct Decisions MUST NOT автоматически считаться independent Decisions.

### D-22
Conflict, precedence и supersession MUST NOT автоматически отождествляться.

### D-23
Core structural/semantic conformance MUST оставаться различимым от historical/provenance integrity, Decision quality, governance/legal status и Representation Fidelity.

### D-24
Historical Decision MUST NOT автоматически представляться как current Recommendation или instruction.

### D-25
Profile MAY усиливать требования Core, но MUST NOT ослаблять Core, продолжая заявлять совместимость с ним.

---

# 47. Необязательные Core Entities

Этот стандарт НЕ требует введения следующих фундаментальных Core Entities только ради представления Decision:

- DecisionOutcome;
- DecisionMaker;
- DecisionSpace;
- Alternative;
- DecisionBasis;
- Objective;
- Criterion;
- Constraint;
- Value;
- Preference;
- DecisionProcess;
- Vote;
- Approval;
- DecisionContext;
- DecisionScope;
- DecisionTransfer;
- DecisionSemanticBoundary;
- DecisionState;
- ReDecision;
- Revocation;
- Suspension;
- Supersession;
- DecisionConflict;
- DecisionDependency;
- Coordination;
- DecisionNetwork;
- DecisionResult;
- Consequence;
- OutcomeRealization;
- ObjectiveAchievement;
- Effectiveness;
- DecisionQuality;
- DecisionFailure;
- MetaDecision;
- AutomatedDecision;
- JointDecision;
- ConstitutiveDecision.

Некоторые из этих понятий MAY быть представлены через существующие Records, relations, roles, States, Profiles или будущие стандарты, если это необходимо.

Отсутствие отдельной Core Entity не означает отсутствия соответствующей semantics.

---

# 48. Совместимость с другими стандартами

`007-DECISION` должен сохранять границы между соседними типами знания.

В частности:

    Source
    → происхождение или носитель содержания

    Claim
    → проверяемое утверждение

    Evidence Use
    → использование материала как evidence

    Assessment
    → evaluative semantics

    Inference
    → что было выведено

    Decision
    → что было решено

Следовательно:

    Claim about Decision
    ≠ Decision

    Inference used in Decision Basis
    ≠ Decision

    Assessment of Decision
    ≠ intrinsic Decision property

    Source reporting Decision
    ≠ Decision itself

    Result used as Evidence
    ≠ Result intrinsically Evidence

`007` не должен поглощать ontology других стандартов.

---

# 49. Принцип сохранения

При конфликте между полнотой и честностью представления предпочтение отдаётся честности.

    partial knowledge
    > invented completion

    ambiguity preserved
    > false precision

    unknown
    > unsupported assumption

Цель стандарта — не создать идеально заполненную запись.

Цель — сохранить Decision настолько полно, насколько позволяют данные, **не выдавая неизвестное за известное**.

---

# 50. Итоговая формула

В наиболее компактной форме:

    Decision
    → что было решено

    Inference
    → что было выведено

    Assessment
    → как что-либо было оценено

    Execution
    → что было сделано

    Result
    → что произошло

И центральный принцип `007-DECISION`:

> **Сохранить Decision — значит сохранить максимально честную информацию о том, что именно было решено и как этому акту атрибутируется его исторический смысл.**

Это не означает объявить решение правильным, истинным, разумным, законным, легитимным, выполненным, успешным или рекомендуемым сейчас.

---

## Статус версии

**007-DECISION v0.1**

Архитектура прошла:

- последовательную разработку глав 1–10;
- локальные аудиты;
- сквозную атаку глав 1–9;
- полный stress-test более чем на 200 рабочих случаях;
- системный аудит глав 1–10;
- контрольный аудит собранного стандарта.

**Критических архитектурных противоречий: 0.**  
**Новых обязательных Core Entities: 0.**  
**Невнесённых замечаний контрольного аудита: 0.**

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
