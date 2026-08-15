# 013 — RELATION
## Стандарт представления отношений

**Проект:** Энциклопедия цивилизации  
**Статус:** действующий базовый стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются Relations — семантические связи между defined semantic positions, participants, records, entities, values или другими referenceable elements.

Relations используются для представления таких семантик, как:

- part-of;
- contains;
- located-in;
- precedes;
- follows;
- overlaps;
- associated-with;
- depends-on;
- supports;
- contradicts;
- derived-from;
- based-on;
- refers-to;
- participates-in;
- affects;
- caused-by;
- enables;
- inhibits;
- corresponds-to;
- same-as;
- similar-to;
- version-of;
- replaces;
- supersedes;
- other domain-specific relations.

Цель стандарта — позволить сохранять:

- какая Relation представлена;
- является ли representation Relation type, Relation model или Relation instance;
- какие semantic positions участвуют в Relation;
- какие participants занимают эти positions;
- каковы participant roles;
- какова arity Relation;
- направлена ли Relation;
- какие formal properties определены для её type/frame;
- в какой applicable frame Relation представлена;
- каков Scope Relation;
- когда Relation применима, если temporal validity materially relevant;
- при каких условиях Relation считается действующей;
- какие qualifiers materially relevant;
- является ли Relation asserted, observed, measured, computed, inferred, modeled или reconstructed;
- насколько Relation определена;
- какие uncertainty и provenance существуют;
- может ли Relation быть contested;
- относится ли Relation к object/domain layer, knowledge layer или meta-model layer.

Стандарт не предназначен для автоматического определения:

- истинности Relation;
- причинности;
- направления causality;
- симметрии;
- транзитивности;
- reflexivity;
- equivalence;
- identity;
- coreference;
- part-whole structure;
- temporal order;
- responsibility;
- authority;
- support strength;
- contradiction;
- dependency;
- ownership;
- similarity;
- quantification;
- того, что Relation сохраняется во времени;
- того, что generic/class-level Relation действует для каждого instance;
- того, что несколько instance-level Relations образуют generic/class-level Relation;
- того, что relation, выраженная естественным языком, имеет одну универсальную canonical semantics.

Сохранить Relation означает сохранить максимально честное представление о semantic linkage между defined semantic positions/participants в resolvable applicable frame, не превращая близость в причинность, association — в dependency, similarity — в identity, coreference — в Record identity, temporal order — в causality, generic Relation — в universal instance-level assertion, несколько instances — в generic rule, а storage edge — в canonical Relation semantics автоматически.

---

# 1. Основное понятие

## 1.1. Relation

**Relation (Отношение)** — semantic construct, представляющий определённую связь между двумя или более semantic positions, которые могут быть заняты participants, values или другими referenceable elements.

Relation отвечает на основной вопрос:

> **Как defined semantic positions/participants связаны между собой в данной applicable frame?**

Relation MAY быть:

- binary;
- ternary;
- n-ary;
- directed;
- undirected;
- symmetric;
- asymmetric;
- temporal;
- spatial;
- causal;
- structural;
- evidential;
- epistemic;
- logical;
- classificatory;
- normative;
- institutional;
- historical;
- statistical;
- domain-specific.

---

# 2. Relation representation ≠ Relation truth

Наличие Relation representation не означает автоматически, что represented Relation objectively holds.

Следовательно:

    Relation representation exists
    ≠ Relation certainly holds

Relation MAY быть:

- asserted;
- observed;
- measured;
- inferred;
- computed;
- modeled;
- reconstructed;
- hypothesized;
- disputed;
- provisional.

Epistemic/provenance status MUST оставаться resolvable when materially relevant.

---

# 3. Relation как semantic construct

Relation не обязана всегда быть отдельной фундаментальной Entity.

Relation MAY быть представлена через:

- graph edge;
- typed reference;
- field;
- embedded structure;
- Record;
- n-ary structure;
- statement;
- relation node;
- other implementation.

Если independent identity, provenance, temporal validity, dispute handling, n-ary role structure, qualifiers или reuse materially важны, Relation MAY быть materialized как отдельный Record.

Следовательно:

    Relation semantics
    ≠ mandatory Relation Entity

Также:

    storage edge
    ≠ canonical Relation semantics automatically

Техническая реализация данных не определяет canonical ontology проекта.

---

# 4. Relation не является универсальным контейнером любого predicate

Не каждое property, attribute или predicate обязано представляться canonical Relation.

Например:

    Person P
    height = 180 cm

MAY технически храниться как edge:

    P → has-height → 180 cm

Но это не означает автоматически, что `has-height` должен становиться canonical Relation type проекта.

Следовательно:

    property
    ≠ Relation automatically

    attribute
    ≠ Relation automatically

    predicate
    ≠ canonical Relation automatically

    storage edge
    ≠ canonical Relation automatically

Relation representation уместна там, где linkage/role semantics между semantic positions materially relevant.

Implementation MAY использовать graph edges без изменения canonical semantic classification.

---

# 5. Co-occurrence ≠ specific Relation

Факт, что два elements:

- появляются рядом в тексте;
- существуют одновременно;
- находятся рядом пространственно;
- часто упоминаются вместе;
- относятся к одной статье;
- имеют похожие properties;

не определяет canonical Relation автоматически.

Следовательно:

    co-occurrence
    ≠ specific Relation automatically

И:

    proximity
    ≠ causality
    ≠ dependency
    ≠ part-of
    ≠ similarity automatically

---

# 6. Relation type ≠ Relation model ≠ Relation instance

Необходимо различать три уровня:

    Relation type
    ≠ Relation model
    ≠ Relation instance

**Relation type** — reusable general semantics Relation.

Например:

    part-of
    causes
    located-in
    supports

**Relation model** — model-level representation структуры, поведения, ограничений, взаимодействий или hypothesized/defined linkages одного или нескольких Relation types.

Например:

    causal graph model
    kinship model
    taxonomic model

Простое перечисление, каталогизация или документация Relation types:

    ≠ Relation model automatically

**Relation instance** — конкретная represented Relation между defined semantic positions/participants в applicable frame.

Например:

    Wheel W part-of Bicycle B

или:

    A owns B during T1–T2

`Relation occurrence` MAY использоваться как более узкое domain term только для Relation instances, которым действительно присущи occurrence-like/temporally instantiated semantics.

Canonical general term в `013`:

    Relation instance

Следовательно:

    Relation type exists
    ≠ Relation instance exists

    Relation model exists
    ≠ Relation instance proven

    model edge
    ≠ represented Relation instance automatically

    Relation model
    ≠ Relation truth

---

# 7. Generic Relation knowledge ≠ specific Relation instance

Generic knowledge:

    metal MAY react with acid

не означает автоматически:

    this historical metal object
    reacted with this acid

Likewise:

    generic Relation type/model
    ≠ specific historical Relation evidence

Transfer from generic/type-level knowledge to specific instance requires:

- Evidence;
- Inference;
- Model application;
- other justified semantics.

---

# 8. Class-level Relation ≠ universal instance-level Relation

Relation between classes/categories MUST NOT automatically become universal Relation among their instances.

Например:

    birds eat insects

MUST NOT automatically mean:

    every bird eats insects

или:

    every bird eats every insect

Generic/class-level Relation MAY encode semantics such as:

- all;
- some;
- most;
- typically;
- often;
- sometimes;
- may;
- can;
- under defined conditions;
- probabilistically;
- other quantified/modal semantics.

Materially relevant quantification MUST remain resolvable.

Следовательно:

    class-level Relation
    ≠ universal instance-level Relation automatically

И:

    generic Relation
    ≠ universal quantified Claim automatically

Full quantified proposition MAY belong primarily to Claim semantics.

`013` requires that Relation representation MUST NOT erase materially relevant quantification.

---

# 9. Instance-level Relations ≠ generic Relation automatically

Наличие нескольких конкретных Relation instances:

    A1 R B
    A2 R B
    A3 R B

не устанавливает автоматически:

    Class A R B

или иной generic/class-level Relation.

Следовательно:

    multiple instance-level Relations
    ≠ class-level/generic Relation automatically

Generalization from instances requires explicit:

- Inference;
- statistical support;
- Model;
- aggregation rule;
- other justified semantics.

Так же как generic Relation не должна автоматически распространяться на каждый instance, набор instances не должен автоматически превращаться в generic rule.

---

# 10. Минимальная структура Relation

Для завершённой Relation semantics необходимо как минимум:

1. defined Relation semantics;
2. resolvable semantic positions;
3. resolvable participants/values where applicable;
4. resolvable participant roles when materially relevant;
5. sufficient Relation attribution;
6. resolvable applicable frame.

Минимальная формула:

    defined Relation semantics
    +
    resolvable semantic positions
    +
    resolvable participants
    +
    resolvable roles when material
    +
    sufficient Relation attribution
    +
    resolvable applicable frame

---

# 11. Applicable frame

Every Relation MUST have a resolvable applicable frame.

**Applicable frame** определяет semantic/reference system, внутри которой Relation имеет определённый смысл и может корректно интерпретироваться.

Applicable frame MAY include:

- semantic/domain frame;
- temporal frame;
- Context;
- jurisdiction;
- spatial/reference frame;
- ontology/taxonomy version;
- system version;
- measurement/reference conventions;
- model;
- Profile;
- other materially relevant interpretive conditions.

Not every component is universally required.

Но:

    Relation without explicit timestamp
    ≠ Relation without frame

Например:

    Dog subclass-of Mammal

MAY require taxonomy/ontology frame.

А:

    A owns B

MAY require temporal + jurisdictional frame.

Frame MAY быть implicit only where it remains unambiguous and resolvable.

---

# 12. Applicable frame ≠ Scope

Applicable frame и Scope являются связанными, но различными понятиями.

**Applicable frame** отвечает прежде всего:

> В какой semantic/reference system Relation имеет смысл и интерпретируется?

**Scope** отвечает прежде всего:

> К какой части domain, participants, population, time range или предметной области данная Relation фактически применяется?

Например:

    Relation:
    Drug A associated-with Outcome B

    Applicable frame:
    clinical-study definitions,
    measurement model,
    relevant domain conventions

    Scope:
    participants age 65+
    in cohort X

Следовательно:

    applicable frame
    ≠ Scope automatically

Некоторые сведения MAY участвовать в обоих аспектах representation, но система MUST preserve distinction where conflation would materially alter meaning.

---

# 13. Relation semantics

**Relation semantics** — смысл связи, которую Relation представляет.

Examples:

    A part-of B

    A precedes B

    A supports Claim C

    Event E associated-with Process P

    Result R derived-from Measurement M

Relation semantics MUST быть sufficiently specific, чтобы materially different relations не collapse into generic edge when distinction важна.

---

# 14. Semantic positions и participants

Relation связывает semantic positions.

Positions MAY быть заняты:

- Entity;
- Record;
- Claim;
- Source;
- State;
- Event;
- Action;
- Process;
- Result;
- Objective;
- Measurement;
- Observation;
- Value;
- Time interval;
- Location;
- other referenceable semantic element.

Core MUST NOT предполагать, что все participants имеют один ontology class.

---

# 15. Relation arity

**Arity** — число semantic positions Relation.

Следовательно:

    Relation arity
    ≠ number of distinct participant identities

Например ternary Relation MAY иметь три semantic positions, даже если один Entity занимает две из них.

Arity belongs to Relation structure, not merely count of unique referenced objects.

---

# 16. Binary Relation

Binary Relation имеет две semantic positions.

Например:

    A located-in B

    Event E precedes Event F

    Source S supports Claim C

Binary Relation MAY иметь distinct roles:

    container / contained

    supporter / supported

    predecessor / successor

Role semantics MUST remain resolvable when material.

---

# 17. N-ary Relation

Не все Relations корректно представляются binary edge.

Example:

    A owes B amount X under Contract C

может требовать:

- debtor;
- creditor;
- amount;
- contract;
- temporal validity.

Likewise:

    Person P administered Substance S
    to Person Q
    at Time T
    by Route R

может быть n-ary structure.

Core MUST NOT force every Relation into pairwise binary edges if materially relevant semantics would be lost.

---

# 18. N-ary decomposition

N-ary Relation MAY быть decomposed into binary relations only if decomposition preserves materially relevant semantics.

Следовательно:

    n-ary Relation
    ≠ arbitrary set of binary edges automatically

Example:

    A owes B $100 under Contract C

cannot safely become only:

    A related-to B
    A related-to $100
    A related-to C

without preserving roles and qualifiers.

---

# 19. Participant roles

Relation positions MAY иметь distinct semantic roles.

Examples:

    parent / child

    source / target

    cause / effect

    owner / owned object

    evidence / supported Claim

    container / contained

Role labels MUST NOT be omitted when omission causes material ambiguity.

---

# 20. Participant role ≠ participant identity

Participant role является semantic role within Relation.

Следовательно:

    participant role
    ≠ participant identity

One Entity MAY occupy different roles in different Relations.

One Entity MAY also occupy multiple semantic positions in one Relation where Relation semantics permits it.

---

# 21. Role ordering ≠ graph directionality

Ordered/asymmetric participant roles and graph directionality are related but not identical concepts.

Например:

    A owes B

имеет roles:

    debtor
    creditor

Но semantic meaning не исчерпывается стрелкой:

    A → B

Следовательно:

    ordered roles
    ≠ graph directionality automatically

Direction MAY encode role ordering in an implementation, but role semantics MUST remain independently resolvable when materially relevant.

---

# 22. Directionality

Relation MAY быть directed.

Например:

    A causes B

    A contains B

    A precedes B

Direction MUST be preserved when materially relevant.

Следовательно:

    A → B
    ≠ B → A automatically

---

# 23. Inverse Relation

Some Relation types MAY have defined inverse.

Например:

    A contains B
    ↔
    B part-of A

Но inverse semantics MUST NOT be invented unless Relation type definition supports it.

Следовательно:

    Relation has direction
    ≠ inverse Relation defined automatically

---

# 24. Formal properties

Formal properties MAY include:

- reflexive;
- irreflexive;
- symmetric;
- asymmetric;
- antisymmetric;
- transitive;
- intransitive;
- functional;
- inverse-functional;
- other defined properties.

Such properties normally characterize:

    Relation type
    within a defined frame/model

rather than one isolated Relation instance.

Следовательно:

    formal property in Frame X
    ≠ same formal property in Frame Y automatically

Core MUST NOT assign universal formal properties to Relation merely from label or intuition.

---

# 25. Symmetry

Some Relation types MAY be symmetric.

Например under a defined semantics:

    A overlaps B
    ↔
    B overlaps A

But symmetry MUST be defined, not assumed.

---

# 26. Asymmetry

Some Relation types MAY be asymmetric.

Например:

    A precedes B

does not imply:

    B precedes A

Asymmetry belongs to defined Relation type/frame semantics.

---

# 27. Transitivity

Transitivity MUST NOT be assumed universally.

Например:

    A part-of B
    B part-of C

MAY support:

    A part-of C

under some mereological models.

But:

    A knows B
    B knows C

does not imply:

    A knows C

Следовательно:

    R(A,B) + R(B,C)
    ≠ R(A,C) automatically

unless defined Relation logic licenses it.

---

# 28. Relation composition ≠ transitivity

Composition MAY involve different Relation types.

Example:

    A parent-of B
    B parent-of C

may license:

    A grandparent-of C

This is not transitivity of `parent-of`.

Likewise:

    A located-in B
    B part-of C

MAY or MAY NOT license:

    A located-in C

depending on defined semantics.

Therefore:

    Relation composition
    ≠ transitivity

Heterogeneous composition rules MUST be explicitly defined when used.

---

# 29. Relation chaining

A chain of Relations MAY support Inference.

But:

    Relation chain
    ≠ implied direct Relation automatically

unless explicit logic licenses the Inference.

---

# 30. Relation closure

Closure operations MAY generate inferred Relations.

Generated Relations MUST preserve:

- derivation;
- rule used;
- source relations;
- uncertainty;
- distinction from directly asserted/observed Relations.

---

# 31. Reflexivity

Some Relation types MAY allow:

    R(A,A)

Others MAY forbid it.

Core MUST NOT assume reflexivity or irreflexivity universally.

---

# 32. Relation ≠ Claim

Claim отвечает:

> Что утверждается?

Relation отвечает:

> Какая связь представлена?

Следовательно:

    Claim about Relation
    ≠ Relation

Example:

    Source S claims:
    A caused B

The Claim MAY represent/support a causal Relation.

But:

    Claim exists
    ≠ causal Relation proven

---

# 33. Relation ≠ Evidence Use

Relation MAY connect Evidence to Claim.

Example:

    Evidence E supports Claim C

Но relation edge alone MUST NOT imply:

    Claim C true

Evidential strength, independence, relevance and reliability MAY require additional semantics.

---

# 34. Relation ≠ Inference

Inference MAY derive a Relation.

But:

    inferred Relation
    ≠ Inference itself

Need preserve when material:

- Relation;
- basis;
- rule/model;
- Inference provenance;
- uncertainty.

---

# 35. Relation ≠ Assessment

Assessment MAY evaluate Relation.

Example:

    causal relation is weakly supported

But:

    Assessment
    ≠ Relation itself

---

# 36. Relation ≠ Event

Some Relations change over time.

Example:

    Relation/State:
    A owns B

    Event:
    ownership transferred

The ownership Relation and transfer Event MUST remain distinct.

---

# 37. Relation ≠ State universally

Some persistent Relations MAY participate in State-like semantics.

Example:

    A owns B during T1–T2

MAY be represented as relational State.

But:

    Relation
    ≠ State universally

Relation describes semantic linkage.

State describes condition/configuration in applicable frame.

A relational State MAY reuse Relation instance semantics without requiring duplicate fundamental objects.

---

# 38. Relation ≠ Process

Process MAY contain changing Relations.

Example:

    negotiation Process

includes changing relations among participants.

But:

    Relation
    ≠ Process

Relation changing over time does not itself automatically become Process.

---

# 39. Relation ≠ Action

Action MAY establish, terminate or modify Relation.

Example:

    Action:
    sign contract

MAY be associated with establishment of institutional Relation.

But:

    Action
    ≠ Relation

---

# 40. Relation ≠ Result

Relation MAY occupy Result semantics relative to a reference frame.

Example:

    Result:
    connection established between A and B

But:

    Relation
    ≠ Result intrinsically

---

# 41. Relation temporal validity

Some Relations hold only during defined periods.

Example:

    A owned B
    from T1 to T2

Temporal validity MAY be:

- exact;
- approximate;
- inferred;
- open-ended;
- disputed;
- unknown.

---

# 42. Domain Relation validity ≠ representation time

Необходимо различать:

    when Relation held in represented domain/world
    ≠ when Relation was recorded
    ≠ when assertion was published
    ≠ when representation was created
    ≠ when representation was revised
    ≠ when Relation was epistemically accepted

Example:

    ownership held: 1800–1810
    archive record created: 1950
    interpretation revised: 2000

These temporal dimensions MUST NOT be collapsed.

---

# 43. Relation snapshot ≠ interval

Need distinguish:

    Relation observed at T
    ≠ Relation held continuously during interval automatically

Snapshot evidence MUST NOT silently expand into interval validity.

---

# 44. Open-ended Relation validity

Relation MAY have:

    start known
    end unknown

But:

    unknown end
    ≠ Relation still holds currently automatically

And:

    open-ended
    ≠ permanent

---

# 45. Relation persistence

Absence of evidence that Relation ended:

    ≠ evidence that Relation persisted

unless domain semantics or justified Inference supports continuity.

---

# 46. Relation establishment ≠ full Relation history

Event/Action associated with Relation establishment MAY be known.

But:

    establishment occurrence known
    ≠ exact Relation validity interval fully known

Likewise:

    Relation exists
    ≠ establishment Event known

---

# 47. Relation termination

Termination Event MAY end Relation.

But:

    Relation terminated
    ≠ Relation never re-established

And:

    termination
    ≠ permanent absence automatically

---

# 48. Current Relation ≠ historical Relation

Current Relation MUST NOT silently overwrite historical Relation.

Example:

    Country A borders Country B today

does not imply identical border Relation historically.

---

# 49. Relation history

Historical Relation representation MAY preserve:

- participants;
- participant roles;
- Relation type;
- qualifiers;
- temporal validity;
- Context;
- Scope;
- provenance;
- uncertainty;
- competing interpretations;
- applicable taxonomy/jurisdiction/model.

---

# 50. Relation revision

Need distinguish:

- Correction;
- new Evidence;
- revised interpretation;
- new historical reconstruction;
- Relation changed in represented domain;
- Relation type definition changed;
- ontology mapping changed;
- participant identity resolution changed.

Changed representation:

    ≠ represented Relation changed automatically

---

# 51. Relation representation identity ≠ Relation instance identity

Two records MAY describe the same Relation instance.

Likewise same participants and same Relation type MAY describe distinct Relation instances.

Therefore:

    representation identity
    ≠ Relation instance identity

---

# 52. Relation instance identity

Relation instance identity MAY depend on materially relevant:

- Relation type;
- semantic positions;
- participant identities;
- participant roles;
- qualifiers;
- reference object/contract;
- amount/value;
- temporal validity;
- continuity;
- Scope;
- Context;
- applicable frame.

Therefore:

    same participants
    +
    same Relation type
    ≠ same Relation instance automatically

Example:

    A owes B $100 under Contract C

and:

    A owes B $200 under Contract D

MUST NOT automatically collapse into one Relation instance.

---

# 53. Qualifier/value change ≠ automatic identity decision

Change in a materially relevant qualifier or value MUST NOT automatically determine either:

- continuity of the same Relation instance;
- replacement by a new Relation instance.

Example:

    A owns 30% of Company B

later:

    A owns 60% of Company B

This MAY represent:

- changing state of one broader ownership Relation;
- two temporal Relation instances;
- two snapshots of one relational State;
- another Profile/domain-defined structure.

Therefore:

    qualifier/value changed
    ≠ same Relation instance automatically

and:

    qualifier/value changed
    ≠ new Relation instance automatically

Relation continuity/identity depends on defined domain/Profile semantics.

---

# 54. Repeated Relation

Example:

    A connected-to B in 2020
    relation ended
    A connected-to B in 2025

Same participants/type:

    ≠ one continuous Relation automatically

Continuity requires semantic justification.

---

# 55. Different provenance ≠ different Relation instance automatically

Two Sources MAY independently represent/support the same Relation instance.

Different provenance MUST NOT force duplicate represented Relations.

---

# 56. Relation granularity

Relation MAY be represented broadly:

    A associated-with B

or more specifically:

    A inhibits B

    A causes B

    A physically-connected-to B

Specific Relation SHOULD be preferred when materially established.

But stronger specificity MUST NOT be invented.

---

# 57. Generic Relation

Generic Relations such as:

    related-to
    associated-with

MAY be used when more specific semantics unknown or unavailable.

But generic Relation MUST NOT silently inherit:

- causality;
- direction;
- dependency;
- support;
- equivalence;
- responsibility.

---

# 58. Specificity preservation

If exact Relation is known:

    A part-of B

representation SHOULD NOT degrade it to:

    A related-to B

when loss materially affects knowledge.

Thus:

    known specific Relation
    > unnecessarily generic Relation

---

# 59. Relation strengthening

Representation MUST NOT strengthen:

    associated-with
    → depends-on

    depends-on
    → caused-by

    correlated-with
    → caused-by

    similar-to
    → same-as

    precedes
    → causes

without independent justification.

---

# 60. Relation weakening

If evidence supports only:

    associated-with

system MUST NOT invent:

    caused-by

Uncertainty SHOULD remain explicit.

---

# 61. Part-whole Relation

Part-whole semantics MAY include:

- component-of;
- member-of;
- portion-of;
- structural-part-of;
- temporal-part-of;
- phase-of;
- material-part-of.

`part-of` MUST NOT be assumed to have one universal mereology.

---

# 62. Part-of ≠ member-of

Example:

    wheel part-of bicycle

vs:

    person member-of organization

These Relations MUST remain distinguishable when material.

---

# 63. Containment ≠ part-of

Example:

    water in bottle

does not necessarily mean:

    water part-of bottle

Spatial containment and structural part-of MUST remain distinguishable.

---

# 64. Temporal containment ≠ part-of

Event E occurs during Process P:

    ≠ Event E part-of Process P automatically

Temporal inclusion and structural/process decomposition are different relations.

---

# 65. Membership

Membership MAY be:

- institutional;
- set-theoretic;
- social;
- biological;
- classificatory.

External `member-of` labels MUST preserve domain semantics.

---

# 66. Spatial Relation

Spatial Relation MAY include:

- inside;
- outside;
- adjacent-to;
- north-of;
- intersects;
- overlaps;
- contains;
- near.

Spatial Relations MAY depend on coordinate/reference frame.

---

# 67. Spatial reference frame

Relation:

    A north-of B

requires applicable orientation/reference frame.

Frame MUST remain resolvable when materially relevant.

---

# 68. Near ≠ universal distance

`near` is context-dependent.

It MUST NOT receive universal distance threshold unless Profile/domain semantics defines one.

---

# 69. Temporal Relation

Temporal Relations MAY include:

- before;
- after;
- during;
- overlaps;
- starts;
- finishes;
- simultaneous-with;
- approximately-before.

Temporal precision and uncertainty MUST remain resolvable when material.

---

# 70. Before ≠ causes

Fundamental rule:

    A before B
    ≠ A caused B

Temporal order MUST NOT silently become causality.

---

# 71. Simultaneous ≠ associated

Two occurrences at the same time:

    ≠ meaningful association automatically

Temporal coincidence alone does not establish semantic linkage.

---

# 72. Causal Relation

Causal Relation is specialized Relation semantics.

It MUST NOT be inferred solely from:

- temporal order;
- correlation;
- proximity;
- sequence;
- co-occurrence;
- narrative order;
- shared Context.

Causal semantics requires separate support.

---

# 73. Causal direction

If causal direction is represented:

    A causes B

MUST remain distinct from:

    B causes A

and:

    A associated-with B

---

# 74. Causal contribution

Causal Relations MAY represent:

- necessary contribution;
- sufficient contribution;
- partial contribution;
- enabling cause;
- inhibiting cause;
- mediated influence;
- probabilistic contribution.

`013` does not define complete causal ontology.

---

# 75. Cause ≠ responsibility

Causal Relation MUST NOT automatically imply:

- legal responsibility;
- moral responsibility;
- blame;
- intention;
- negligence.

These are separate semantics.

---

# 76. Dependency Relation

Dependency MAY mean:

- logical dependency;
- operational dependency;
- causal dependency;
- resource dependency;
- software dependency;
- institutional dependency.

External label `depends-on` MUST preserve domain meaning.

---

# 77. Dependency ≠ causality universally

    A depends-on B
    ≠ B caused A automatically

Dependency may be structural, conditional or operational.

---

# 78. Enabling Relation

A MAY enable B.

But:

    enabled
    ≠ occurred

And:

    enabling condition
    ≠ sufficient cause

---

# 79. Inhibiting Relation

A MAY inhibit B.

But:

    inhibitor present
    ≠ B absent automatically

without defined domain semantics.

---

# 80. Evidential Relation

Evidence-related Relations MAY include:

- supports;
- contradicts;
- is-basis-for;
- derived-from;
- corroborates;
- weakens;
- consistent-with.

These Relations MUST NOT automatically assign truth.

---

# 81. Supports ≠ proves

Fundamental rule:

    Evidence E supports Claim C
    ≠ Claim C proven

Support MAY vary in:

- strength;
- relevance;
- independence;
- reliability;
- Scope;
- Context.

---

# 82. Multiple support edges ≠ independent evidence

Multiple supporting Relations MUST NOT automatically be interpreted as multiple independent evidence lines.

Example:

    Source B cites Source A
    Source C cites Source A
    Source D copies Source A

does not automatically provide three independent confirmations.

Evidence independence MAY itself require provenance/relation analysis.

---

# 83. Contradicts ≠ false

If Evidence E contradicts Claim C:

    ≠ Claim C necessarily false

Contradiction MAY depend on:

- interpretation;
- assumptions;
- Scope;
- timing;
- measurement validity.

---

# 84. Consistent-with ≠ confirms

A datum MAY be consistent with many hypotheses.

Thus:

    consistent-with
    ≠ confirms
    ≠ strongly supports automatically

---

# 85. Derived-from Relation

Derived-from MAY connect:

- Claim to Source;
- Result to Measurement;
- computed value to inputs;
- reconstruction to Evidence.

But:

    derived-from
    ≠ causally-produced-by automatically

---

# 86. Source Relation

Relations to Source MAY express:

- asserts;
- documents;
- records;
- mentions;
- contains;
- derived-from;
- cites.

These MUST remain semantically distinct when material.

---

# 87. Citation ≠ evidential support

A Source citing another Source:

    ≠ independent corroboration

Likewise:

    citation
    ≠ agreement
    ≠ truth

---

# 88. Reference Relation

A Record MAY refer-to another Record.

Reference relation MUST NOT automatically imply:

- endorsement;
- support;
- dependency;
- identity.

---

# 89. Identity-like semantics

Identity-like relations require special care.

Need distinguish:

    entity identity
    ≠ coreference
    ≠ Record identity
    ≠ representation identity
    ≠ semantic equivalence
    ≠ value equivalence

---

# 90. Coreference ≠ Record identity

Two Records MAY refer to the same real-world Entity.

Example:

    Record A:
    Alexander III

    Record B:
    Александр III

They MAY be coreferential.

But:

    same referent
    ≠ same Record

Therefore:

    coreference
    ≠ Record identity

---

# 91. `same-as` is not universal identity bucket

`same-as` MUST NOT be used as universal container for all identity-like semantics.

System SHOULD distinguish when material:

- same Entity;
- same referent;
- duplicate Record;
- equivalent representation;
- same value;
- same concept;
- coreference.

---

# 92. Identity Relation

Identity semantics is especially strong.

It MUST NOT be inferred solely from:

- same label;
- similar name;
- same value;
- same location;
- overlapping properties;
- likely match.

Identity resolution requires sufficient support.

---

# 93. Similarity ≠ identity

Fundamental rule:

    similar-to
    ≠ same-as

Similarity MAY be graded, contextual or feature-dependent.

---

# 94. Similarity basis

Similarity SHOULD preserve when materially relevant:

- comparison dimensions;
- selected features;
- metric;
- weights;
- threshold;
- comparison population;
- model/version.

Therefore:

    similarity
    ≠ intrinsic universal property automatically

Example:

    visually similar
    ≠ chemically similar
    ≠ functionally similar

---

# 95. Equivalence ≠ identity universally

Two things MAY be equivalent for a purpose without being identical.

Example:

    1000 mm
    equivalent-to 1 m

Different representations MAY encode equivalent quantity.

Likewise two Procedures MAY be functionally equivalent without being the same Procedure.

---

# 96. Version Relation

Version Relations MAY include:

- version-of;
- supersedes;
- revises;
- derived-version-of;
- translation-of.

These MUST NOT automatically imply full semantic identity.

---

# 97. Supersedes ≠ deletes history

If Record B supersedes Record A:

    ≠ Record A should disappear

Historical dependency and provenance MAY require preserving A.

---

# 98. Correction Relation

Correction MAY indicate later representation corrects earlier representation.

But:

    Correction
    ≠ underlying historical reality changed

---

# 99. Replacement Relation

`replaces` MAY mean:

- physical replacement;
- document replacement;
- institutional succession;
- semantic update;
- component replacement.

Domain semantics MUST remain defined.

---

# 100. Successor Relation

Successor MAY indicate sequence or institutional continuity.

But:

    successor-of
    ≠ same identity automatically

---

# 101. Parent/child Relation

`parent`, `child`, `ancestor`, `descendant` MAY have:

- biological;
- genealogical;
- taxonomic;
- data-tree;
- organizational meanings.

External vocabulary MUST NOT determine canonical semantics without domain frame.

---

# 102. Classification Relation

Classification MAY include:

    instance-of
    subclass-of
    type-of

These MUST remain distinguishable.

---

# 103. Instance-of ≠ subclass-of

Example:

    Dog A instance-of Dog

vs:

    Dog subclass-of Mammal

These are not interchangeable.

---

# 104. Class membership ≠ identity

Being instances of the same class:

    ≠ same Entity

---

# 105. Taxonomic Relation

Taxonomy MAY be:

- scientific;
- folk;
- historical;
- institutional;
- project-specific.

Taxonomic Relation MUST preserve taxonomy/version when material.

---

# 106. Taxonomy drift

Historical classification MUST NOT silently inherit current taxonomy.

Example:

    classification at T1
    ≠ modern classification automatically

---

# 107. Normative Relation

Relations MAY represent:

- requires;
- permits;
- prohibits;
- authorizes;
- obliges.

Normative Relation MUST NOT automatically become actual Action/State relation.

---

# 108. Authorization ≠ Action

    A authorizes B to do X
    ≠ B did X

Likewise:

    permission
    ≠ execution

---

# 109. Obligation ≠ compliance

    A obligated-to perform X
    ≠ X performed

Normative and actual layers MUST remain distinct.

---

# 110. Prohibition ≠ absence

Fundamental rule:

    X prohibited
    ≠ X did not occur

Likewise:

    prohibited Relation/Action
    ≠ absent Relation/Action automatically

Normative prohibition and empirical absence MUST remain distinct.

---

# 111. Institutional Relation

Institutional Relations MAY include:

- owns;
- governs;
- employs;
- appoints;
- represents;
- licenses;
- recognizes;
- controls.

Their semantics MAY depend on jurisdiction and time.

---

# 112. Legal Relation ≠ de facto Relation

Example:

    legal owner = A
    de facto controller = B

These MAY coexist.

They MUST NOT be collapsed.

---

# 113. Ownership Relation

Ownership MAY depend on:

- jurisdiction;
- time;
- legal system;
- type of property.

`owns` MUST NOT receive one universal cross-domain ontology without Profile semantics.

---

# 114. Control Relation

`controls` MAY mean:

- operational control;
- legal control;
- technical control;
- causal control;
- ownership influence.

External label MUST preserve intended domain meaning.

---

# 115. Participation Relation

Participation MAY connect Actor/Entity to:

- Event;
- Action;
- Process;
- organization;
- group.

But participation MUST NOT automatically imply:

- causation;
- responsibility;
- leadership;
- intention.

---

# 116. Actor Relation

Action MAY have:

    performed-by

But:

    participant-in
    ≠ performed-by automatically

And:

    present-at
    ≠ participated-in

---

# 117. Presence Relation

Being present at Event:

    ≠ participant
    ≠ witness
    ≠ cause
    ≠ responsible

unless separately established.

---

# 118. Witness Relation

Witnessing Event:

    ≠ causing Event
    ≠ participating in Event

---

# 119. Location Relation

An Entity MAY have:

    located-at
    located-in
    passes-through
    originated-in

These Relations MUST preserve role and temporal frame when material.

---

# 120. Origin Relation

`originated-in` MAY mean:

- physical origin;
- historical origin;
- conceptual origin;
- manufacturing origin;
- biological origin.

It MUST NOT automatically imply present location.

---

# 121. Derivation Relation

A MAY be derived from B.

This MAY mean:

- data derivation;
- textual derivation;
- material derivation;
- genealogical descent;
- logical inference.

Generic `derived-from` MUST preserve domain semantics.

---

# 122. Transformation Relation

A transformed-into B MAY involve:

- Process;
- Event;
- identity continuity;
- material continuity;
- semantic replacement.

Transformation Relation MUST NOT automatically establish same identity across transformation.

---

# 123. Identity through transformation

Whether A before transformation is same Entity as B after transformation MAY be domain-specific.

Core MUST NOT decide identity solely from transformation Relation.

---

# 124. Relation uncertainty

Uncertainty MAY apply to:

- existence of Relation;
- Relation type;
- participant identity;
- participant roles;
- direction;
- temporal validity;
- Scope;
- Context;
- strength;
- mechanism;
- qualifiers;
- quantification;
- provenance.

Core does not require universal:

    Relation.confidence

---

# 125. Unknown Relation

Unknown Relation between A and B:

    ≠ no Relation

Likewise:

    no recorded Relation
    ≠ Relation absent

---

# 126. Relation absence

Defined absence of Relation MAY be represented if Evidence/domain semantics supports it.

But:

    not observed
    ≠ absent

    not recorded
    ≠ absent

---

# 127. Negated Relation

Need distinguish:

    not-R
    ≠ unknown-R
    ≠ no-record-of-R
    ≠ incompatible-with-R
    ≠ prohibited-R

Statement:

    A does not own B

MAY be:

- Claim;
- absence semantics;
- logical assertion;
- Profile-defined negation.

It MUST NOT automatically create a special negative Relation Entity.

---

# 128. Incompatibility ≠ negation

A Relation MAY be incompatible with another Relation under defined constraints.

But:

    incompatible-with
    ≠ negation automatically

Likewise:

    disjoint-with
    ≠ absence of every other Relation

Formal incompatibility requires defined semantics.

---

# 129. Relation conflict

Different Sources MAY support conflicting Relations.

Examples:

    A caused B

vs:

    A did not cause B

or:

    A part-of B

vs:

    A independent-of B

System MUST allow competing representations with provenance.

---

# 130. Apparent conflict

Relations MAY appear conflicting but concern different:

- time periods;
- jurisdictions;
- Scopes;
- Relation types;
- participants;
- identity resolutions;
- Contexts;
- taxonomies;
- versions;
- qualifiers;
- quantifiers.

Alignment MUST precede contradiction judgment.

---

# 131. Relation comparison

Comparing Relations requires materially sufficient alignment.

Relevant alignment MAY include:

- participant identity;
- semantic positions;
- participant roles;
- Relation type;
- direction;
- temporal frame;
- Context;
- Scope;
- qualifiers;
- quantification;
- Profile;
- taxonomy/version.

---

# 132. Relation normalization

External systems MAY use different vocabularies.

Normalization MAY map external Relation labels to canonical semantics.

But normalization MUST NOT erase materially relevant distinctions.

---

# 133. External Relation label ≠ canonical Relation

Words such as:

- linked;
- connected;
- related;
- associated;
- tied;
- dependent;
- derived;
- based;
- influenced;

are often ambiguous.

External wording alone MUST NOT determine canonical Relation type.

---

# 134. Natural-language ambiguity

Natural language often leaves:

- direction;
- roles;
- causality;
- strength;
- temporality;
- Scope;
- quantification;
- modality;

implicit.

Representation MUST NOT invent missing semantics without basis.

---

# 135. Relation provenance

Relation provenance MAY include:

- assertion;
- direct Observation;
- Measurement;
- Claim;
- Source;
- Inference;
- computation;
- Model;
- reconstruction;
- imported relation;
- Assessment.

Multiple provenance dimensions MAY coexist.

---

# 136. Observed Relation

Some Relations MAY be directly observed.

Example:

    Object A physically touching B

But:

    observed Relation
    ≠ permanent Relation
    ≠ causal Relation
    ≠ complete Relation history

---

# 137. Measured Relation

Relations MAY derive from Measurements.

Example:

    distance(A,B) = 5 m

Measurement-derived Relation MUST preserve when material:

- method;
- units;
- uncertainty;
- time;
- reference frame.

---

# 138. Inferred Relation

Relation MAY be inferred.

Then:

    inferred
    ≠ observed

Inference basis and assumptions MUST remain resolvable when material.

---

# 139. Reconstructed Relation

Historical Relation MAY be reconstructed.

Examples:

- ownership;
- political alliance;
- trade relation;
- family relation.

Reconstruction MUST preserve provenance and uncertainty.

---

# 140. Modeled Relation

Model MAY include Relations.

But:

    modeled Relation
    ≠ observed/historical Relation automatically

Model identity and represented Relation instance identity MUST remain distinct.

---

# 141. Computed Relation

Some Relations MAY be computed.

Examples:

- similarity;
- network relation;
- spatial overlap;
- temporal overlap;
- statistical association.

Computation method SHOULD remain resolvable when material.

---

# 142. Provenance dimensions MAY overlap

Observed, measured, computed, inferred, modeled and reconstructed Relation provenance MAY overlap.

Core MUST NOT force one exclusive status if multiple are materially true.

---

# 143. Relation strength

Some Relation types MAY have strength.

Examples:

    strong correlation
    weak evidential support
    high dependency

Strength semantics is Relation-type-specific.

Core does not impose one universal Relation strength scale.

---

# 144. Relation probability

Some Relations MAY be probabilistic.

Example:

    A increases probability of B

Probability semantics MUST NOT be collapsed into deterministic Relation.

---

# 145. Statistical Relation

Statistical Relations MAY include:

- correlation;
- association;
- conditional association;
- probabilistic dependence;
- other defined structures.

They MUST preserve when materially relevant:

- variables;
- population;
- sample;
- period;
- method;
- conditioning variables;
- coefficient/effect representation;
- uncertainty;
- Context.

Statistical Relation MUST NOT silently generalize across population, period or conditioning frame.

---

# 146. Correlation Relation

Correlation is statistical Relation.

And:

    correlation
    ≠ causation

Also:

    marginal correlation
    ≠ conditional correlation automatically

---

# 147. Association Relation

Association MAY be:

- statistical;
- observational;
- semantic;
- operational;
- historical.

Generic association MUST NOT receive causal semantics automatically.

---

# 148. Similarity Relation

Similarity MUST preserve materially relevant comparison basis when necessary.

Thus:

    visually similar
    ≠ chemically similar
    ≠ functionally similar

---

# 149. Contradiction Relation

Contradiction MAY exist between Claims.

Need distinguish:

    Claim C1 contradicts Claim C2

from:

    represented world States are incompatible

Logical contradiction and empirical incompatibility MAY require different semantics.

---

# 150. Support Relation

Support Relation MAY exist:

    Evidence → Claim

    Claim → Inference

    Source → Claim

But exact support semantics MUST remain typed when material.

---

# 151. Basis Relation

`basis-for` MAY connect:

- Evidence to Decision;
- Claim to Inference;
- State knowledge to Action;
- Result to Assessment.

But:

    basis-for
    ≠ cause-of automatically

---

# 152. Decision Basis preservation

Later Relation MUST NOT be inserted retroactively into earlier Decision Basis.

If Relation was discovered at T2:

    ≠ available to Decision at T1 automatically

---

# 153. Relation historical drift

Current Relation MUST NOT silently alter earlier historical interpretation.

Examples:

- current ownership;
- current borders;
- current taxonomy;
- current organization membership.

Historical frame MUST remain preserved.

---

# 154. Relation versioning

Need distinguish:

- Relation instance changed;
- Relation representation changed;
- Relation type semantics changed;
- Relation model changed;
- ontology mapping changed;
- Source corrected;
- participant identity resolution changed.

Thus:

    Relation type/model revision
    ≠ represented historical Relation changed automatically

---

# 155. Ontology Relation ≠ domain Relation

Some Relations exist in ontology/meta-model:

    subclass-of
    defined-by
    compatible-with

Others describe domain/world:

    located-in
    owns
    causes

These layers SHOULD remain distinguishable when material.

---

# 156. Meta-Relation

A Relation MAY itself be referenced as participant in another Relation if representation permits reference to it.

Example:

    Relation R1:
    A causes B

    R1 disputed-by Source S

or:

    R1 valid-during Interval T

But:

    higher-order Relation support
    ≠ universal Relation reification requirement

Core MUST NOT require every Relation to become an Entity merely because some Relations require higher-order reference.

---

# 157. Relation representation as participant ≠ represented Relation itself

When a Relation representation is used as participant in another Relation, the system MUST preserve whether the higher-order Relation concerns:

- the representation/Record;
- the assertion;
- the semantic Relation instance;
- another referenceable layer.

Example:

    Source S disputes Record R1

does not necessarily mean:

    Source S disputes the existence
    of the underlying world Relation itself

Therefore:

    Relation representation as participant
    ≠ represented Relation itself automatically

Higher-order semantics MUST preserve the intended reference layer when materially relevant.

---

# 158. Relation about Relation

System MAY represent:

- provenance of Relation;
- uncertainty;
- contradiction;
- replacement;
- temporal validity;
- Relation between Relations.

Higher-order semantics SHOULD avoid unnecessary Entity Explosion.

---

# 159. Relation cardinality

A participant MAY have:

- zero;
- one;
- multiple;

Relations of a type.

Cardinality constraints MAY be Profile/domain-specific.

Core MUST NOT impose universal cardinality unless required by Relation definition.

---

# 160. Functional Relation

Some Relation types MAY be functional within a defined frame:

    each X has at most one Y

But functionality MUST be explicitly defined.

---

# 161. Exclusive Relation

Some Relation types MAY be mutually exclusive.

Example:

    married-to A
    married-to B

MAY or MAY NOT be allowed depending on jurisdiction/time.

Core MUST NOT impose universal exclusivity.

---

# 162. Relation Scope

Relation MAY apply only to:

- part of subject;
- subset of population;
- particular time;
- particular jurisdiction;
- specific variables;
- specific domain segment.

Scope MUST remain resolvable when materially relevant.

Scope specifies the extent/domain subset to which represented Relation applies and MUST NOT automatically be collapsed into applicable frame.

---

# 163. Local Relation ≠ global Relation

Relation observed in local subset:

    ≠ Relation holds globally automatically

Generalization requires Inference/Model.

---

# 164. Sample Relation ≠ population Relation

Statistical Relation observed in sample:

    ≠ population Relation automatically

---

# 165. Aggregate Relation

Aggregate Relation MAY differ from individual-level Relation.

Example:

    population-level correlation

does not imply identical individual relationship.

---

# 166. Ecological fallacy safeguard

Group-level Relation MUST NOT automatically become individual-level Relation.

Likewise individual-level Relation MUST NOT automatically generalize to aggregate level.

---

# 167. Context-dependent Relation

Relation MAY hold only under specific Context.

Example:

    material A reacts-with B
    only above temperature T

Context MUST remain resolvable when material.

---

# 168. Relation Context drift

Current Context MUST NOT silently replace historical/context-specific Relation semantics.

---

# 169. Relation and Action

Action MAY be linked to:

- Actor;
- Object;
- Instrument;
- target;
- Result;
- Event;
- Process.

Relations MUST preserve role distinctions.

Example:

    Actor participated-in Action
    ≠ Actor performed Action automatically

---

# 170. Relation and Event

Event MAY be linked through:

- occurred-at;
- affected;
- preceded-by;
- participated-in;
- caused-by;
- associated-with.

These Relations MUST NOT collapse into one generic Event relation if distinction materially matters.

---

# 171. Relation and State

State MAY use Relation semantics as content.

Example:

    A owns B

as relational State.

But Relation temporal validity and State semantics MUST remain distinguishable.

Relational State MAY reuse Relation instance without requiring duplicate canonical semantics.

---

# 172. Relation and Process

Process MAY have:

- participants;
- inputs;
- outputs;
- dependencies;
- phase Relations;
- interactions.

Temporal containment MUST NOT automatically become subprocess Relation.

---

# 173. Relation and Result

Result MAY relate to:

- reference frame;
- Comparison Reference;
- Measurement;
- population;
- Context;
- Objective.

Generic links MUST NOT erase role semantics.

---

# 174. Relation and Objective

Objective MAY relate to:

- target State;
- Action;
- Decision;
- Result;
- criteria.

Desired Relation:

    ≠ actual Relation automatically

---

# 175. Relation and Procedure

Procedure MAY define prescribed Relations:

    step A before step B

But:

    prescribed order
    ≠ actual historical order

---

# 176. Relation and Model

Model MAY define Relations among variables/entities.

But:

    modeled Relation
    ≠ directly observed Relation

---

# 177. Relation and Measurement

Measurement MAY quantify Relation.

Examples:

- distance;
- correlation;
- angle;
- overlap.

Measurement result MUST NOT automatically define stronger Relation semantics than measured.

---

# 178. Relation and Observation

Observation MAY identify Relation.

But:

    observed association
    ≠ causal Relation

---

# 179. Relation and Inference

Inference MAY derive Relation through:

- logical rule;
- statistical analysis;
- causal model;
- identity resolution;
- temporal reasoning.

Derived status MUST remain resolvable.

---

# 180. Relation and Assessment

Assessment MAY evaluate:

- relevance;
- reliability;
- strength;
- validity;
- importance;
- plausibility.

These are not intrinsic generic Relation properties unless Relation type defines them.

---

# 181. Relation representation fidelity

Representation MUST NOT materially alter:

- Relation type/model/instance role;
- semantic positions;
- participant identity;
- participant roles;
- arity;
- direction;
- formal properties when known;
- quantification;
- qualifiers;
- temporal validity;
- Scope;
- Context;
- applicable frame;
- uncertainty;
- provenance;
- strength;
- causal/epistemic status.

---

# 182. Translation Fidelity

Translation MUST preserve distinctions such as:

    associated-with
    ≠ caused-by

    part-of
    ≠ contained-in

    supports
    ≠ proves

    authorized
    ≠ performed

    similar-to
    ≠ same-as

    coreferential-with
    ≠ same Record

    before
    ≠ causes

    member-of
    ≠ part-of automatically

    prohibited
    ≠ absent

    generic
    ≠ universal

    instance pattern
    ≠ generic rule

---

# 183. Logical Fidelity

Representation SHOULD preserve:

- direction;
- negation;
- quantifiers;
- modality;
- semantic positions;
- participant roles;
- Relation Scope;
- temporal bounds;
- conditions;
- uncertainty;
- strength;
- formal logic where material.

---

# 184. Summary Fidelity

Summary MUST NOT convert:

    association
    → causality

    similarity
    → identity

    coreference
    → Record identity

    support
    → proof

    participation
    → responsibility

    temporal order
    → causality

    local Relation
    → universal Relation

    sample Relation
    → population Relation

    historical Relation
    → current Relation

    generic Relation
    → specific stronger Relation

    class-level Relation
    → universal instance-level Relation

    multiple Relation instances
    → generic/class-level Relation

    prohibition
    → empirical absence

    modeled Relation
    → observed Relation

    Relation representation
    → represented Relation itself

---

# 185. Relation compression

Relation representation MAY omit non-material metadata.

But compression MUST NOT erase materially relevant:

- Relation type/model/instance role;
- direction;
- roles;
- n-ary structure;
- qualifiers;
- quantification;
- temporal validity;
- uncertainty;
- causal status;
- Scope;
- Context;
- applicable frame;
- provenance;
- Relation specificity;
- reference layer in higher-order Relations.

---

# 186. Damaged archives

Historical Source MAY preserve partial Relation.

Example:

    "... allied with the northern kingdom ..."

Missing:

- exact counterpart identity;
- date;
- duration;
- type of alliance;
- legal status;

MUST NOT be invented.

Likewise missing quantification, direction or role MUST NOT be silently filled where ambiguity is material.

---

# 187. Relation reconstruction

Historical Relation reconstruction MUST preserve:

- Sources;
- assumptions;
- uncertainty;
- competing interpretations;
- temporal bounds;
- participant identity uncertainty;
- Context;
- applicable historical frame.

Reconstruction MUST NOT masquerade as direct Observation.

---

# 188. Offline preservation

Relation SHOULD be representable without dependence on modern platform.

Where materially relevant, preserve:

- Relation type/model/instance role;
- semantic positions;
- participants;
- participant roles;
- arity;
- direction;
- temporal validity;
- qualifiers;
- quantification;
- Scope;
- Context;
- applicable frame;
- provenance;
- uncertainty;
- formal properties where needed;
- higher-order reference layer where needed.

---

# 189. Carrier neutrality

Relation semantics does not depend on:

- database;
- graph database;
- RDF;
- JSON;
- Markdown;
- table;
- diagram;
- printed text;
- other durable carrier.

Carrier does not define Relation ontology.

Likewise:

    graph edge
    ≠ canonical Relation automatically

---

# 190. High-risk Profiles

High-risk Profiles MAY require stricter Relation representation.

Examples:

- medicine;
- engineering;
- law;
- chemistry;
- electrical systems;
- safety;
- historical reconstruction;
- survival procedures.

Profile MAY require:

- exact Relation type;
- participant roles;
- units;
- causal status;
- temporal validity;
- Scope;
- Context;
- quantification;
- qualifiers;
- provenance;
- uncertainty;
- Relation logic;
- formal constraints.

These are not universal Core requirements.

---

# 191. Relation quality

`013` does not introduce universal intrinsic Relation Quality.

Quality concepts MAY include:

- strong;
- weak;
- reliable;
- uncertain;
- valid;
- invalid;
- useful;
- significant.

These usually require Relation-type-specific semantics or Assessment.

---

# 192. Conformance and Integrity

Need distinguish:

    Core structural/semantic conformance
    ≠ Relation truth
    ≠ provenance integrity
    ≠ causal validity
    ≠ logical validity
    ≠ Relation quality
    ≠ Representation Fidelity

Validator PASS does not mean Relation objectively holds.

---

# 193. Profiles

Profile MAY strengthen Core.

Profile MUST NOT weaken Core while claiming compatibility with `013`.

---

# 194. Diagnostic families

## 194.1. Type / model / instance failures

Examples:

- Relation type → Relation instance;
- Relation model → Relation instance;
- enumeration of Relation types → Relation model;
- model edge → historical Relation;
- generic Relation knowledge → specific occurrence;
- Relation instance → Relation type.

## 194.2. Participant / role failures

Examples:

- participant roles omitted;
- subject/object reversed;
- n-ary Relation flattened incorrectly;
- one participant mistaken for another;
- arity confused with number of unique participants.

## 194.3. Directionality failures

Examples:

- A causes B → B causes A;
- contains → part-of reversed incorrectly;
- before/after inverted;
- role ordering treated as sufficient semantic definition.

## 194.4. Formal-property failures

Examples:

- symmetry assumed from label;
- transitivity assumed universally;
- property from Frame X transferred to Frame Y;
- composition treated as transitivity.

## 194.5. Specificity failures

Examples:

- associated-with → caused-by;
- supports → proves;
- related-to used despite known specific Relation;
- part-of → member-of.

## 194.6. Quantification/generalization failures

Examples:

- generic Relation → universal Relation;
- some → all;
- may → always;
- typical → necessary;
- class-level Relation → every instance pair;
- multiple instances → generic Relation;
- observed instance pattern → universal rule.

## 194.7. Frame / Scope failures

Examples:

- applicable frame collapsed into Scope;
- Scope collapsed into applicable frame;
- semantic/reference system confused with population subset;
- jurisdictional interpretation confused with empirical extent.

## 194.8. Temporal failures

Examples:

- snapshot → interval;
- historical Relation → current Relation;
- no end Evidence → persistence;
- observation time → domain Relation validity;
- publication time → Relation validity.

## 194.9. Relation identity failures

Examples:

- same participants/type → same Relation instance;
- qualifier change → automatically same Relation;
- qualifier change → automatically new Relation;
- interrupted Relations → one continuous Relation;
- representation identity → Relation instance identity.

## 194.10. Identity/equivalence failures

Examples:

- similar-to → same-as;
- coreference → Record identity;
- same label → same Entity;
- functional equivalence → identity;
- successor → same identity.

## 194.11. Causal failures

Examples:

- before → cause;
- correlation → causality;
- participation → causal responsibility;
- input → sufficient cause.

## 194.12. Evidential failures

Examples:

- supports → proves;
- multiple citations → independent corroboration;
- citation → evidential support;
- consistent-with → confirms;
- contradicts → automatically false.

## 194.13. Structural failures

Examples:

- containment → part-of;
- temporal containment → subprocess;
- membership → component relation.

## 194.14. Normative failures

Examples:

- authorization → Action;
- obligation → compliance;
- prohibition → absence;
- legal relation → de facto relation.

## 194.15. Negation / absence failures

Examples:

- unknown-R → not-R;
- no-record-R → absent-R;
- prohibited-R → not-R;
- incompatible-R → negated-R.

## 194.16. Scope / Context failures

Examples:

- sample → population;
- local → global;
- group → individual;
- Context X → Context Y;
- jurisdiction A → jurisdiction B.

## 194.17. Provenance/import failures

Examples:

- modeled Relation → observed Relation;
- inferred Relation → direct fact;
- external label mapped blindly;
- historical taxonomy → modern taxonomy.

## 194.18. Higher-order reference failures

Examples:

- dispute of Relation Record → dispute of underlying world Relation automatically;
- provenance of representation → provenance of represented Relation automatically;
- Relation representation → semantic Relation instance without layer distinction.

## 194.19. Implementation failures

Examples:

- storage edge → canonical Relation;
- property field → new Relation type automatically;
- graph structure → ontology semantics automatically.

Diagnostic label itself does not establish:

- fraud;
- negligence;
- blame;
- intent;
- responsibility.

---

# 195. Machine validation

Validator MAY check:

- participant references;
- semantic positions;
- required participant roles;
- arity;
- Relation type;
- direction;
- Profile-defined cardinality;
- temporal validity;
- Scope;
- applicable-frame presence/resolvability;
- qualifiers;
- quantification structure;
- formal constraints;
- reference integrity;
- higher-order reference layer where explicitly represented.

But:

    validator PASS
    ≠ Relation true
    ≠ causality established
    ≠ identity established
    ≠ evidential support sufficient
    ≠ historical accuracy proven

Validator has no truth privilege.

---

# 196. Cross-standard compatibility

`013-RELATION` MUST preserve neighboring semantic boundaries.

In compact form:

    Claim
    → что утверждается

    State
    → каким представлен condition/configuration
      в applicable frame

    Event
    → что произошло /
      какой occurrence или boundary возник

    Process
    → какая temporally extended
      activity/dynamics unfolds

    Action
    → что было сделано

    Result
    → какую downstream/result role
      phenomenon занимает

    Relation
    → как defined semantic positions/
      participants связаны
      в applicable frame

Therefore:

    Claim about Relation
    ≠ Relation

    Relation
    ≠ Event

    Relation
    ≠ Process

    Relation
    ≠ Action

    Relation
    ≠ Result intrinsically

    Relation
    ≠ causality automatically

    Relation
    ≠ State universally

    Relation type
    ≠ Relation model
    ≠ Relation instance

    property/predicate
    ≠ Relation automatically

    storage edge
    ≠ canonical Relation automatically

    generic Relation
    ≠ universal instance-level Relation

    multiple Relation instances
    ≠ generic/class-level Relation automatically

    applicable frame
    ≠ Scope automatically

    Relation representation
    ≠ represented Relation itself

---

# 197. Boundary concepts outside full 013 ontology

`013` uses neighboring concepts only to establish Relation boundaries.

These include:

- Claim;
- State;
- Event;
- Process;
- Action;
- Result;
- Observation;
- Measurement;
- Assessment;
- Inference;
- Source;
- Identity;
- Coreference;
- Classification;
- Causality;
- Membership;
- Part-whole;
- Dependency;
- Evidence Use;
- Quantification;
- Scope;
- Context.

`013` does not assert that their complete ontology belongs inside Relation standard.

---

# 198. Entity Explosion Test

`013` НЕ требует введения следующих fundamental Core Entities только ради Relations:

- RelationType;
- RelationModel;
- RelationInstance;
- RelationOccurrence;
- RelationParticipant;
- RelationPosition;
- RelationRole;
- RelationFrame;
- RelationContext;
- RelationScope;
- RelationQualifier;
- RelationInterval;
- RelationStrength;
- RelationConfidence;
- RelationProbability;
- BinaryRelation;
- NaryRelation;
- DirectedRelation;
- SymmetricRelation;
- CausalRelation;
- SpatialRelation;
- TemporalRelation;
- StatisticalRelation;
- EvidentialRelation;
- IdentityRelation;
- CoreferenceRelation;
- SimilarityRelation;
- MembershipRelation;
- PartOfRelation;
- DependencyRelation;
- NormativeRelation;
- InstitutionalRelation;
- RelationAssertion;
- RelationNegation;
- RelationAbsence;
- RelationConflict;
- RelationVersion;
- CompositionRule;
- RelationClosure.

These MAY be represented through:

- semantic roles;
- Relation definitions;
- generic Relation infrastructure;
- Records;
- Profiles;
- Claims;
- States;
- Models;
- temporal structures;
- provenance structures;
- future standards.

Absence of separate Core Entity does not mean absence of corresponding semantics.

---

# 199. Core invariants

Следующие положения образуют минимальное нормативное ядро `013-RELATION`.

### RL-01
Relation является semantic construct, representing a defined semantic linkage among resolvable semantic positions/participants within a resolvable applicable frame.

### RL-02
Relation semantics MAY be materialized as specialized Record when materially useful, but separate Relation Entity is not universally mandatory.

### RL-03
Relation representation existence MUST NOT automatically imply that represented Relation objectively holds.

### RL-04
Storage/graph implementation MUST NOT determine canonical Relation ontology.

### RL-05
Property, attribute or predicate MUST NOT automatically be treated as canonical Relation.

### RL-06
Co-occurrence, spatial proximity, temporal proximity or textual proximity MUST NOT automatically determine a specific Relation type.

### RL-07
Relation type, Relation model and Relation instance MUST remain semantically distinguishable.

### RL-08
Relation type MUST NOT automatically be treated as Relation model or Relation instance.

### RL-09
Relation model MUST NOT automatically be treated as Relation instance or Relation truth.

### RL-10
Mere enumeration, cataloguing or documentation of Relation types MUST NOT automatically be treated as Relation model.

### RL-11
Model edge MUST NOT automatically be treated as represented/historical Relation instance.

### RL-12
Generic Relation knowledge MUST NOT automatically establish a specific historical Relation instance.

### RL-13
Class-level/generic Relation MUST NOT automatically become universal instance-level Relation.

### RL-14
Multiple instance-level Relations MUST NOT automatically establish class-level/generic Relation.

### RL-15
Generalization from Relation instances MUST require explicit Inference, Model, aggregation rule or other justified semantics.

### RL-16
Materially relevant quantification and modality MUST remain resolvable.

### RL-17
Relation MUST have sufficiently defined Relation semantics.

### RL-18
Relation MUST have resolvable semantic positions and participants where applicable.

### RL-19
Relation MUST have a resolvable applicable frame.

### RL-20
Applicable frame and Scope MUST remain distinguishable where conflation would materially alter meaning.

### RL-21
Participant roles MUST remain resolvable when omission would materially alter meaning.

### RL-22
Relation attribution is semantic requirement and MUST NOT require dedicated Core Entity solely for conformance.

### RL-23
Relation arity MUST remain distinguishable from number of distinct participant identities.

### RL-24
Core MUST NOT force every Relation into binary representation when materially relevant n-ary semantics would be lost.

### RL-25
N-ary Relation MUST NOT be decomposed into binary edges if decomposition destroys materially relevant role/qualifier structure.

### RL-26
Participant role MUST remain distinct from participant identity.

### RL-27
Ordered/asymmetric participant roles MUST remain distinguishable from graph directionality when materially relevant.

### RL-28
Direction MUST be preserved when materially relevant.

### RL-29
Inverse Relation MUST NOT be invented unless Relation semantics defines it.

### RL-30
Symmetry, asymmetry, transitivity, reflexivity, functionality and other formal properties MUST NOT be assumed universally.

### RL-31
Formal Relation properties SHOULD be understood relative to defined Relation type/frame/model.

### RL-32
Formal property valid in Frame X MUST NOT automatically be transferred to Frame Y.

### RL-33
Relation chaining MUST NOT automatically establish a new direct Relation unless explicit logic licenses the Inference.

### RL-34
Relation composition MUST remain distinguishable from transitivity.

### RL-35
Heterogeneous composition MUST NOT be inferred without defined composition logic.

### RL-36
Inferred closure Relations MUST preserve derivation/provenance.

### RL-37
Claim about Relation MUST remain distinct from Relation.

### RL-38
Inferred Relation MUST remain distinct from Inference itself.

### RL-39
Relation MUST remain distinct from Event, Process, Action and Result.

### RL-40
Relation and State MAY overlap in relational-State semantics but MUST NOT collapse universally.

### RL-41
Relation temporal/domain validity MUST remain distinguishable from record time, assertion/publication time, representation history and epistemic acceptance interval.

### RL-42
Relation snapshot MUST NOT automatically expand into interval validity.

### RL-43
Open-ended Relation validity MUST NOT automatically imply current or permanent validity.

### RL-44
Absence of Evidence of Relation termination MUST NOT automatically establish persistence.

### RL-45
Current Relation MUST NOT silently overwrite historical Relation.

### RL-46
Changed Relation representation MUST NOT automatically imply represented Relation changed.

### RL-47
Identity of Relation representation MUST remain distinct from identity/continuity of represented Relation instance.

### RL-48
Relation instance identity MAY depend on complete materially relevant participant-role/qualifier/frame structure.

### RL-49
Same participants and same Relation type MUST NOT automatically imply same Relation instance.

### RL-50
Change in qualifier/value MUST NOT automatically determine either continuity or replacement of Relation instance.

### RL-51
Relation continuity/identity under qualifier/value change MUST depend on defined domain/Profile semantics.

### RL-52
Different provenance MUST NOT automatically imply different represented Relation instance.

### RL-53
Generic Relation MUST NOT silently inherit stronger Relation semantics.

### RL-54
Known specific Relation SHOULD NOT be degraded to generic Relation when specificity is materially relevant.

### RL-55
Association MUST NOT automatically become dependency or causality.

### RL-56
Similarity MUST NOT automatically become identity.

### RL-57
Similarity SHOULD preserve materially relevant comparison basis.

### RL-58
Temporal order MUST NOT automatically become causality.

### RL-59
Part-of, member-of, containment and temporal containment MUST remain distinguishable when materially relevant.

### RL-60
Causal Relation MUST NOT be inferred solely from correlation, temporal order, proximity, co-occurrence, sequence or narrative.

### RL-61
Causal Relation MUST NOT automatically imply responsibility, blame, intention or negligence.

### RL-62
Dependency MUST NOT automatically imply causality.

### RL-63
Enabling Relation MUST NOT automatically imply occurrence.

### RL-64
Evidence support MUST NOT automatically imply proof or truth.

### RL-65
Multiple supporting Relations MUST NOT automatically be treated as independent evidence lines.

### RL-66
Contradiction Relation MUST NOT automatically imply that one Claim is false without further epistemic analysis.

### RL-67
Consistent-with MUST NOT automatically imply confirmation or strong support.

### RL-68
Derived-from MUST NOT automatically imply causal production.

### RL-69
Citation MUST NOT automatically imply evidential support or independent corroboration.

### RL-70
Reference Relation MUST NOT automatically imply endorsement, dependency or identity.

### RL-71
Entity identity, coreference, Record identity, representation identity and semantic equivalence MUST remain distinguishable when materially relevant.

### RL-72
`same-as` MUST NOT be used as universal bucket for identity-like semantics.

### RL-73
Identity Relation MUST require stronger support than similarity, label equality or overlapping properties.

### RL-74
Equivalence MUST remain distinguishable from identity when materially relevant.

### RL-75
Version/supersession/replacement Relations MUST preserve historical provenance and MUST NOT automatically erase prior representations.

### RL-76
Classification Relations such as instance-of and subclass-of MUST remain distinguishable.

### RL-77
Normative Relation MUST NOT automatically become actual Action/State Relation.

### RL-78
Authorization MUST NOT automatically imply Action.

### RL-79
Obligation MUST NOT automatically imply compliance.

### RL-80
Prohibition MUST NOT automatically imply empirical absence.

### RL-81
Legal Relation and de facto Relation MUST remain distinguishable when materially relevant.

### RL-82
Participation MUST NOT automatically imply causation, responsibility, leadership or intention.

### RL-83
Presence-at MUST NOT automatically imply participation-in or witness-of.

### RL-84
Transformation Relation MUST NOT automatically establish identity continuity.

### RL-85
Unknown Relation, no-record-of-Relation and Relation absence MUST remain distinguishable.

### RL-86
Negated Relation MUST remain distinguishable from unknown, unrecorded, incompatible and prohibited Relation semantics.

### RL-87
Negation of Relation MUST NOT automatically require a special negative Relation Entity.

### RL-88
Relation conflict MUST NOT be asserted before materially sufficient participant, role, temporal, Context, Scope, qualifier, quantification and type alignment.

### RL-89
External Relation labels MUST NOT automatically determine canonical Relation type.

### RL-90
Natural-language ambiguity MUST NOT be resolved by inventing missing direction, causality, strength, quantification or role semantics.

### RL-91
Observed, measured, computed, inferred, modeled and reconstructed Relation provenance MAY overlap and MUST remain resolvable when materially relevant.

### RL-92
Relation strength MUST remain Relation-type-specific and MUST NOT receive universal scale semantics.

### RL-93
Probabilistic Relation MUST NOT silently become deterministic Relation.

### RL-94
Statistical Relation MUST preserve materially relevant population, period and conditioning frame.

### RL-95
Correlation MUST NOT automatically become causation.

### RL-96
Marginal association/correlation MUST NOT automatically be treated as conditional association/correlation.

### RL-97
Contradiction between Claims MUST remain distinguishable from incompatibility between represented world States.

### RL-98
Basis-for MUST NOT automatically be treated as cause-of.

### RL-99
Later-discovered Relation MUST NOT be inserted retroactively into earlier Decision Basis.

### RL-100
Historical Relation MUST NOT silently inherit current participants, taxonomy, jurisdiction, Context, model or Relation-type semantics.

### RL-101
Ontology/meta-model Relations SHOULD remain distinguishable from domain/world Relations when materially relevant.

### RL-102
Higher-order Relation semantics MUST NOT require universal reification of all Relations.

### RL-103
A Relation representation used as participant in a higher-order Relation MUST remain distinguishable from the represented Relation itself when materially relevant.

### RL-104
Higher-order Relation MUST preserve whether its target is representation, assertion, semantic Relation instance or another referenceable layer when this distinction materially affects meaning.

### RL-105
Cardinality and exclusivity constraints MUST NOT be assumed universally.

### RL-106
Relation Scope MUST remain resolvable when materially relevant.

### RL-107
Local/sample/aggregate Relation MUST NOT automatically become global/population/individual Relation.

### RL-108
Group-level Relation MUST NOT automatically become individual-level Relation, and vice versa.

### RL-109
Context-dependent Relation MUST NOT silently generalize across Contexts.

### RL-110
Relation role distinctions in Action/Event/Process/Result structures MUST remain explicit when material.

### RL-111
Modeled Relation MUST remain distinguishable from observed/historical Relation.

### RL-112
Representation MUST preserve materially relevant Relation type/model/instance role, semantic positions, participants, roles, arity, direction, qualifiers, quantification, temporal validity, Scope, Context, applicable frame, provenance and uncertainty.

### RL-113
Core structural/semantic conformance MUST remain distinct from Relation truth, provenance integrity, causal validity, logical validity, Relation quality and Representation Fidelity.

### RL-114
Profile MAY strengthen Core requirements but MUST NOT weaken Core while claiming compatibility with `013`.

### RL-115
Materially relevant uncertainty, provenance, participant identity, participant roles, quantification, temporal validity, Scope and applicable frame MUST remain resolvable.

---

# 200. Stress-test framework

Архитектура `013-RELATION` должна выдерживать как минимум следующие классы атак:

1. Relation representation vs truth;
2. storage edge vs canonical Relation;
3. property/predicate vs Relation;
4. co-occurrence vs Relation;
5. Relation type vs model;
6. Relation type vs instance;
7. Relation model vs instance;
8. Relation-type enumeration vs Relation model;
9. model edge vs historical Relation;
10. generic Relation knowledge vs historical instance;
11. class-level Relation vs instance-level Relation;
12. generic quantification;
13. all/some/most/typically/may distinctions;
14. multiple instances vs generic Relation;
15. instance aggregation/generalization;
16. binary Relation;
17. n-ary Relation;
18. n-ary flattening;
19. arity vs distinct participants;
20. participant-role ambiguity;
21. repeated participant in multiple positions;
22. ordered roles vs graph directionality;
23. directed Relation;
24. inverse Relation;
25. symmetric Relation;
26. asymmetric Relation;
27. transitive Relation;
28. non-transitive Relation;
29. formal property across different frames;
30. relation chaining;
31. transitivity vs heterogeneous composition;
32. closure/inferred Relations;
33. reflexive/irreflexive semantics;
34. Relation vs Claim;
35. Relation vs Inference;
36. Relation vs Assessment;
37. Relation vs Event;
38. Relation vs State;
39. relational State reuse;
40. Relation vs Process;
41. Relation vs Action;
42. Relation vs Result;
43. applicable frame vs Scope;
44. temporal Relation validity;
45. domain validity vs record time;
46. domain validity vs publication time;
47. domain validity vs epistemic acceptance;
48. Relation snapshot vs interval;
49. open-ended Relation;
50. Relation persistence;
51. Relation establishment;
52. Relation termination;
53. current vs historical Relation;
54. Relation revision;
55. representation identity vs Relation instance identity;
56. qualified/n-ary Relation identity;
57. qualifier drift;
58. qualifier change vs Relation continuity;
59. repeated Relation after interruption;
60. different provenance of same Relation;
61. generic vs specific Relation;
62. Relation strengthening;
63. Relation weakening;
64. part-of vs member-of;
65. containment vs part-of;
66. temporal containment vs part-of;
67. membership semantics;
68. spatial Relation;
69. orientation/reference frame;
70. near semantics;
71. temporal Relation;
72. before vs cause;
73. simultaneity vs association;
74. causal Relation;
75. causal direction;
76. causal contribution;
77. cause vs responsibility;
78. dependency;
79. dependency vs causality;
80. enabling Relation;
81. inhibiting Relation;
82. evidential Relation;
83. supports vs proves;
84. multiple support edges vs independent Evidence;
85. contradicts vs false;
86. consistent-with vs confirms;
87. derived-from vs caused-by;
88. Source Relation;
89. citation vs corroboration;
90. reference vs endorsement;
91. entity identity;
92. coreference;
93. Record identity;
94. representation identity;
95. same-as bucket failure;
96. similarity vs identity;
97. similarity metric/basis;
98. equivalence vs identity;
99. version Relation;
100. supersedes vs erase-history;
101. Correction;
102. replacement;
103. successor vs identity;
104. parent/child domain ambiguity;
105. instance-of vs subclass-of;
106. class membership vs identity;
107. taxonomy/version drift;
108. normative Relation;
109. authorization vs Action;
110. obligation vs compliance;
111. prohibition vs absence;
112. institutional Relation;
113. legal vs de facto;
114. ownership;
115. control;
116. participation;
117. present-at vs participated-in;
118. witness Relation;
119. location Relation;
120. origin Relation;
121. derivation Relation;
122. transformation Relation;
123. transformation vs identity continuity;
124. Relation uncertainty;
125. unknown vs absent Relation;
126. no-record vs absent Relation;
127. negated Relation;
128. incompatible vs negated Relation;
129. prohibited vs negated Relation;
130. Relation conflict;
131. apparent conflict due to time;
132. apparent conflict due to jurisdiction;
133. apparent conflict due to quantification;
134. Relation comparison;
135. Relation normalization;
136. lexical ambiguity;
137. Relation provenance;
138. observed Relation;
139. measured Relation;
140. inferred Relation;
141. reconstructed Relation;
142. modeled Relation;
143. computed Relation;
144. overlapping provenance statuses;
145. Relation strength;
146. probabilistic Relation;
147. statistical Relation;
148. marginal vs conditional association;
149. correlation;
150. association;
151. similarity dimensions;
152. Claim contradiction vs world incompatibility;
153. support Relation;
154. basis Relation;
155. later Relation vs earlier Decision Basis;
156. historical Relation drift;
157. Relation versioning;
158. ontology Relation vs domain Relation;
159. meta-Relation;
160. Relation representation as participant;
161. represented Relation vs representation target;
162. dispute of representation vs dispute of underlying Relation;
163. higher-order Relation without universal reification;
164. Relation composition;
165. cardinality constraints;
166. functional Relation;
167. exclusive Relation;
168. Relation Scope;
169. local vs global Relation;
170. sample vs population Relation;
171. aggregate vs individual Relation;
172. ecological fallacy;
173. Context-dependent Relation;
174. Relation and Action;
175. Relation and Event;
176. Relation and State;
177. Relation and Process;
178. Relation and Result;
179. Relation and Objective;
180. Relation and Procedure;
181. Relation and Model;
182. Relation and Measurement;
183. Relation and Observation;
184. Relation and Inference;
185. Relation and Assessment;
186. translation corruption;
187. summary corruption;
188. damaged archives;
189. historical reconstruction;
190. offline preservation;
191. high-risk Profiles;
192. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если новый test выявляет необходимое фундаментальное правило, оно должно быть внесено в соответствующий normative section.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 201. Принцип сохранения

При конфликте между полнотой и честностью representation предпочтение отдаётся честности.

    generic Relation
    > invented specific Relation

    association
    > invented causality

    similarity
    > invented identity

    coreference
    > invented Record identity

    support
    > invented proof

    temporal order
    > invented causal direction

    participant
    > invented responsibility

    snapshot
    > invented interval

    unknown Relation
    > false absence

    generic/class-level Relation
    > invented universal Relation

    observed instances
    > invented generic rule

    local Relation
    > false global Relation

    historical Relation
    > current-Relation substitution

    n-ary semantics
    > lossy binary flattening

    explicit uncertainty
    > invented certainty

    prohibition
    > invented empirical absence

    historical frame
    > modern-frame substitution

    explicit reference layer
    > ambiguous higher-order target

Цель стандарта — сохранить Relation настолько полно, насколько позволяют данные, **не превращая association в causality, similarity в identity, coreference в Record identity, support в proof, participation в responsibility, temporal order в causal chain, generic/class-level Relation в universal instance-level assertion, набор отдельных Relation instances в необоснованное generic rule, normative prohibition в empirical absence, storage edge в canonical ontology, Relation representation в сам represented Relation или incomplete historical Relation в modern reconstructed certainty**.

---

# 202. Итоговая формула

В наиболее компактной форме:

    Entity / Record / Value
    → что может занимать
      semantic position

    Relation type
    → какой reusable kind
      semantic linkage определён

    Relation model
    → какая model-level structure
      Relations/types определена

    Relation instance
    → какая конкретная linkage
      представлена между defined positions
      в applicable frame

    Applicable frame
    → в какой semantic/reference system
      Relation интерпретируется

    Scope
    → к какой части domain/population/
      participants Relation применяется

    Claim
    → что утверждается
      о Relation или других semantics

    State
    → каким представлен
      condition/configuration

    Event
    → что произошло

    Process
    → как dynamics unfolds

    Action
    → что было сделано

    Result
    → какую downstream/result role
      phenomenon занимает

Центральный принцип `013-RELATION`:

> **Сохранить Relation — значит сохранить максимально честное представление о semantic linkage между defined semantic positions/participants вместе с materially relevant Relation type/model/instance role, participant roles, arity, direction, qualifiers, quantification, applicable frame, Scope, temporal validity, provenance, uncertainty и reference layer.**

Факт Relation representation сам по себе не означает:

- что Relation истинна;
- что Relation causal;
- что Relation symmetric;
- что Relation transitive;
- что Relation permanent;
- что generic Relation универсальна для всех instances;
- что несколько instances образуют generic rule;
- что participant несёт responsibility;
- что similarity означает identity;
- что coreference означает Record identity;
- что support означает proof;
- что prohibition означает absence;
- что multiple support edges являются independent corroboration;
- что model edge является historical Relation;
- что storage edge является canonical Relation;
- что Relation representation и represented Relation являются одним объектом;
- что historical Relation совпадает с current Relation.

---

# 203. Статус версии

**013-RELATION v0.1**

Стандарт прошёл:

1. первичную архитектурную сборку;
2. сквозную архитектурную атаку;
3. исправление выявленных weaknesses;
4. повторную чистую сборку;
5. контрольный аудит;
6. финальную интеграцию audit corrections.

На момент фиксации:

    Critical architectural defects:       0
    Major architectural defects:          0
    Known blocking contradictions:        0
    New mandatory Core Entities:          0
    Entity Explosion Test:                PASS
    Cross-standard compatibility:         PASS
    Status:                               FIXED v0.1

Версия `0.1` является первой зафиксированной базовой версией стандарта.

Фиксация версии не означает окончательность или абсолютную полноту модели.

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.

---

**Чтобы знания пережили нас.**
