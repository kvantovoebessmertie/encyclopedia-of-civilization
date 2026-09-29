# 014 — IDENTITY
## Стандарт идентичности, различения и coreference

**Проект:** Энциклопедия цивилизации  
**Статус:** действующий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются и различаются:

- identity;
- sameness;
- distinctness;
- coreference;
- Record identity;
- representation identity;
- semantic identity/equivalence;
- value equality;
- identity criteria;
- identity frames;
- identity Scope;
- identity resolution;
- identity mappings;
- identity continuity;
- identity through change;
- aliases;
- identifiers;
- duplicates;
- versions;
- copies;
- transformations;
- mergers;
- splits;
- succession;
- uncertain identity;
- disputed identity;
- historical identity resolution.

Цель стандарта — не дать системе смешивать:

    один и тот же referent
    с
    одной и той же записью

    один Record
    с
    одной representation

    одинаковое значение
    с
    одной Entity

    similarity
    с
    identity

    equivalence
    с
    identity

    part-of
    с
    same-as

    representation-of
    с
    identity

    successor
    с
    identity continuity

    identity assertion
    с
    resolved identity

    identity continuity
    с
    unchanged State

Стандарт должен позволять честно отвечать:

- о каком именно объекте идёт речь;
- являются ли две references ссылками на один referent;
- являются ли две записи одной записью;
- описывают ли разные Records один объект;
- являются ли две representations одной representation;
- по какому критерию устанавливается identity;
- в какой frame действует identity judgment;
- к какому Scope он относится;
- действует ли identity mapping только в определённое время;
- является ли объект до и после изменения тем же объектом;
- кто и на каком основании утверждает identity;
- является ли identity resolved, probable, disputed или unknown;
- как исправить ошибочное слияние;
- как сохранить историческую неопределённость;
- как предотвратить ложное распространение свойств через identity.

`014` НЕ решает универсально философскую проблему абсолютной идентичности.

Он НЕ устанавливает один universal identity criterion для:

- людей;
- организмов;
- организаций;
- государств;
- территорий;
- материалов;
- документов;
- программ;
- Processes;
- States;
- Relations;
- цифровых объектов;
- понятий.

Identity criteria МОЖЕТ быть domain-, Profile-, time-, level-, purpose- или model-dependent.

---

# 1. Основное понятие

## 1.1. Identity

**Identity (Идентичность)** — semantics, согласно которой две или более references, representations или identity-bearing units рассматриваются как относящиеся к одному и тому же referent/object относительно определённого identity level, frame и, когда это существенно, identity criterion и Scope.

Identity отвечает не просто на вопрос:

> «Это одно и то же?»

а на более строгий вопрос:

> **Что именно считается одним и тем же, на каком уровне, в какой frame, по какому criterion, в каком Scope, в какое время и на каких основаниях?**

---

# 2. Identity не является одним universal same-as

Необходимо различать как минимум:

- Entity identity;
- referent identity;
- coreference;
- Record identity;
- representation identity;
- semantic equivalence;
- value equality;
- version continuity;
- State continuity;
- Process continuity;
- institutional continuity;
- legal continuity;
- material continuity.

Следовательно:

    same
    ≠ one universal semantics

---

# 3. Identity-bearing unit

Identity всегда относится к некоторой identity-bearing unit.

Такой unit МОЖЕТ быть:

- physical Entity;
- person;
- organism;
- organization;
- institution;
- territory;
- document;
- Source;
- Record;
- Claim;
- State;
- Event;
- Process;
- Relation instance;
- Action;
- Result;
- Model;
- Concept;
- dataset;
- software artifact;
- version;
- representation;
- other defined object.

Core НЕ ДОЛЖЕН предполагать один identity criterion для всех таких units.

---

# 4. Identity level

Identity ДОЛЖЕН быть interpreted relative to a defined level when ambiguity is materially relevant.

Например:

    Record A
    Record B

могут относиться к одному человеку.

Но:

    same person
    ≠ same Record

А:

    two scans of Record A

могут представлять один Record, оставаясь двумя carrier/representation instances.

Следовательно:

    Entity identity
    ≠ Record identity
    ≠ representation identity
    ≠ carrier identity

---

# 5. Identity frame

**Identity frame** — semantic/reference system, внутри которой интерпретируется identity judgment.

Frame МОЖЕТ включать:

- domain;
- ontology;
- jurisdiction;
- historical framework;
- temporal framework;
- representation layer;
- purpose;
- Profile;
- Model.

Identity assertion ДОЛЖЕН retain resolvable frame when изменение frame может изменить результат.

---

# 6. Identity criterion

**Identity criterion** — правило или совокупность правил, определяющих, что считается совпадением или сохранением identity внутри применимой frame.

Criteria МОЖЕТ включать:

- physical continuity;
- material continuity;
- organism continuity;
- legal continuity;
- institutional continuity;
- provenance continuity;
- identifier governance;
- structural continuity;
- functional continuity;
- archival continuity;
- formal equivalence;
- other domain-specific criteria.

Ни один criterion не получает универсального приоритета в Core.

Если выбор criterion materially affects identity judgment, criterion ДОЛЖЕН remain resolvable.

Следовательно:

    same frame
    ≠ necessarily same identity criterion

---

# 7. Identity Scope

**Identity Scope** определяет, к какому аспекту, уровню или ограниченной области объекта применяется identity judgment.

Например:

    same legal corporate entity

МОЖЕТ относиться к:

    corporate legal person

но не автоматически к:

- employees;
- assets;
- offices;
- physical materials;
- leadership;
- territory.

Следовательно:

    Identity frame
    ≠ Identity criterion
    ≠ Identity Scope

В компактной форме:

    frame
    → в какой semantic/reference system
      рассматривается identity

    criterion
    → по какому правилу
      определяется sameness/continuity

    Scope
    → к какому аспекту
      применяется judgment

---

# 8. Identity criterion ≠ identity evidence

Criterion определяет:

> что должно считаться identity или continuity.

Evidence определяет:

> на каких основаниях считается, что criterion выполнен.

Например:

    criterion:
    continuous legal registration

    Evidence:
    registry documents

Или:

    criterion:
    physical continuity

    Evidence:
    photographs
    serial numbers
    chain of custody

Следовательно:

    identity criterion
    ≠ identity evidence

---

# 9. Identity representation ≠ identity truth

Наличие representation:

    A same-as B

не означает автоматически:

    A and B objectively are the same Entity

Identity МОЖЕТ быть:

- asserted;
- observed indirectly;
- inferred;
- computed;
- reconstructed;
- resolved;
- modeled;
- disputed;
- provisional.

Следовательно:

    identity assertion
    ≠ identity certainty

---

# 10. Identity semantics ≠ mandatory Identity Entity

Identity МОЖЕТ быть represented through:

- Relation;
- Claim;
- Record;
- mapping;
- alias structure;
- identifier linkage;
- version history;
- provenance;
- qualified reference;
- Inference;
- Profile.

Если identity resolution требует:

- provenance;
- competing candidates;
- uncertainty;
- history;
- audit trail;

она МОЖЕТ быть materialized as Record.

Но:

    Identity semantics
    ≠ mandatory fundamental Identity Entity

---

# 11. Entity identity

**Entity identity** означает, что references относятся к одному и тому же Entity under applicable identity semantics.

Но:

    Entity identity
    ≠ name identity
    ≠ Record identity
    ≠ representation identity

---

# 12. Referent identity

Two expressions МОЖЕТ refer to one referent.

Different expressions:

    ≠ different referents automatically

Same expression:

    ≠ same referent automatically

---

# 13. Coreference

**Coreference** — semantics, согласно которой две или более references/expressions refer to the same referent.

Coreference:

    ≠ expression identity
    ≠ Record identity
    ≠ representation identity

Coreference МОЖЕТ be:

- resolved;
- probable;
- possible;
- disputed;
- unknown.

---

# 14. Record identity

Two references to the same Record:

    → Record identity

Two different Records describing one Entity:

    ≠ Record identity

Therefore:

    same referent
    ≠ same Record

И наоборот:

    different Records
    ≠ distinct referents automatically

---

# 15. Representation identity

Representation itself МОЖЕТ have identity distinct from represented content.

Example:

    original document
    scan
    transcription
    translation

may be related but remain distinct representations.

Thus:

    representation-of
    ≠ identity

---

# 16. Representation safeguard

A representation, description, model, photograph, biography or Record about an Entity НЕ ДОЛЖЕН automatically be treated as identical to the represented Entity.

Therefore:

    photo-of P
    ≠ P

    model-of X
    ≠ X

    Record-about X
    ≠ X

    description-of X
    ≠ X

---

# 17. Semantic equivalence

Two representations МОЖЕТ encode materially equivalent semantics.

But:

    semantic equivalence
    ≠ Record identity
    ≠ Entity identity automatically

---

# 18. Value equality

Example:

    Object A mass = 5 kg
    Object B mass = 5 kg

does not imply:

    A = B

Likewise:

    same State value
    ≠ same State identity

---

# 19. Attribute equality

Same:

- name;
- age;
- date;
- location;
- dimensions;
- identifier fragment;
- description;

НЕ ДОЛЖЕН automatically establish Entity identity.

---

# 20. Similarity

Fundamental rule:

    similar
    ≠ same

High similarity НЕ ДОЛЖЕН automatically become identity.

---

# 21. Equivalence

Two objects МОЖЕТ be equivalent for a purpose.

But:

    functional equivalence
    ≠ physical identity

    semantic equivalence
    ≠ Record identity

---

# 22. Qualified sameness

Expressions such as:

- legally the same;
- functionally the same;
- historically the same;
- materially the same;
- semantically the same;

МОЖЕТ represent qualified sameness, continuity or equivalence rather than strict identity.

Therefore:

    qualified sameness
    ≠ strict identity automatically

Relations such as:

    legally-same
    functionally-same
    historically-same
    materially-same

НЕ ДОЛЖЕН inherit strict identity properties unless their explicit semantics define them as strict identity under compatible frame, criterion and Scope.

---

# 23. Interchangeability

Different Entities МОЖЕТ be interchangeable.

One Entity МОЖЕТ cease to be interchangeable after State change.

Therefore:

    interchangeability
    ≠ identity

---

# 24. Classification

Two objects МОЖЕТ instantiate same class.

But:

    same class
    ≠ same instance

---

# 25. Naming

A name is not identity.

One Entity МОЖЕТ have:

- multiple names;
- aliases;
- titles;
- translations;
- transliterations;
- historical names.

One name МОЖЕТ refer to multiple Entities.

Thus:

    same name
    ≠ same Entity

    different name
    ≠ different Entity automatically

---

# 26. Lexical identity

Same word/string НЕ ДОЛЖЕН determine referent identity.

Example:

    "Москва"

МОЖЕТ refer, depending on Context, to different semantic objects.

Therefore:

    lexical identity
    ≠ referent identity

---

# 27. Alias

Alias is an alternative naming/reference relation.

Alias МОЖЕТ support identity resolution.

But:

    alias
    ≠ identity proof automatically

---

# 28. Homonymy

Same label МОЖЕТ refer to different Entities.

Name matching НЕ ДОЛЖЕН automatically merge them.

---

# 29. Renaming

Renaming МОЖЕТ change name/identifier while Entity identity persists.

Thus:

    name changed
    ≠ Entity changed automatically

---

# 30. Identifier ≠ Entity

Identifier identifies/refers within a defined system.

But:

    identifier
    ≠ identified Entity

Identifiers МОЖЕТ be:

- reused;
- reassigned;
- duplicated;
- corrupted;
- obsolete;
- namespace-specific.

---

# 31. Identifier namespace

Identifier ДОЛЖЕН be interpreted within resolvable namespace when ambiguity is material.

Thus:

    same identifier string
    across different namespaces
    ≠ same Entity automatically

---

# 32. Identifier uniqueness

Identifier МОЖЕТ be unique inside a declared system/frame.

But:

    locally unique
    ≠ globally unique

---

# 33. Persistent identifier

Persistent identifier aims to remain stable.

But:

    persistent identifier
    ≠ proof of unchanged referent

Governance failure, reassignment or corruption МОЖЕТ occur.

---

# 34. Identifier collision and reassignment

System ДОЛЖЕН permit representation of:

- identifier collision;
- identifier reuse;
- reassignment;
- duplicate identifiers;
- historical identifier changes.

Same identifier across time НЕ ДОЛЖЕН automatically establish identity if reassignment is possible.

---

# 35. Identity provenance

Identity resolution СЛЕДУЕТ preserve materially relevant provenance.

Possible bases include:

- Source;
- identifier;
- archival continuity;
- physical continuity;
- lineage;
- legal documentation;
- Observation;
- Inference;
- Model;
- expert resolution.

---

# 36. Identity evidence

Evidence МОЖЕТ include:

- unique identifier;
- continuous provenance;
- physical continuity;
- temporal compatibility;
- geographic continuity;
- matching attributes;
- lineage;
- archival references;
- direct documentation.

No single category is universally sufficient.

---

# 37. Weak matches

Several matching attributes МОЖЕТ increase plausibility.

But:

    name match
    + date match
    + location match
    ≠ identity automatically

unless explicit identity-resolution semantics supports conclusion.

---

# 38. Attribute mismatch

One mismatch:

    ≠ distinctness automatically

because mismatch МОЖЕТ result from:

- error;
- changed State;
- renaming;
- transcription;
- historical variation;
- uncertain data.

---

# 39. Identity resolution

**Identity resolution** — process, decision or inference evaluating whether references/objects should be considered same, distinct or unresolved under applicable semantics.

Identity resolution:

    ≠ identity relation itself

Possible outputs МОЖЕТ include:

- resolved same;
- resolved distinct;
- probable same;
- possible same;
- ambiguous;
- unresolved;
- disputed.

---

# 40. Resolved identity is scoped

Resolved identity ДОЛЖЕН be interpreted within its applicable:

- identity level;
- frame;
- criterion;
- Scope;
- Profile;
- Model;
- temporal validity;

when these are materially relevant.

Therefore:

    system-resolved identity
    ≠ universal identity truth

A resolution valid in one system or frame НЕ ДОЛЖЕН silently become globally valid.

---

# 41. Asserted identity vs resolved identity

A Source МОЖЕТ assert:

    A = B

without the system accepting that assertion as resolved identity.

Therefore:

    Source-asserted identity
    ≠ system-resolved identity

Identity assertions ДОЛЖЕН be representable as Claims without forcing canonical merge.

This permits simultaneous representation of:

    Source S1: A = B

    Source S2: A ≠ B

    current resolution: unresolved

---

# 42. Unknown identity

If identity cannot be determined:

    unknown
    ≠ same
    ≠ distinct

Unknown identity ДОЛЖЕН remain representable.

---

# 43. Distinctness

**Distinctness** means two identity-bearing units are different under applicable identity semantics.

But:

    failure to prove same
    ≠ proof of distinctness

Distinctness МОЖЕТ require its own evidence.

Distinctness ДОЛЖЕН preserve identity level, frame, criterion and Scope where materially relevant.

Therefore:

    distinct at one identity level
    ≠ distinct at another identity level automatically

and:

    different Records
    ≠ distinct referents automatically

---

# 44. Not-same ≠ unknown

Fundamental distinction:

    not same
    ≠ unknown whether same

Negation and uncertainty ДОЛЖЕН remain separate.

---

# 45. Candidate identity

System МОЖЕТ retain candidate matches without merging.

Example:

    A possibly-corefers B

Candidate identity:

    ≠ resolved identity

---

# 46. Multiple candidates

A reference МОЖЕТ have multiple possible referents:

    A → B1?
    A → B2?

System ДОЛЖЕН permit preservation of alternatives.

It НЕ ДОЛЖЕН arbitrarily select one candidate.

---

# 47. Identity conflict

Different Sources/Models МОЖЕТ disagree about identity.

System ДОЛЖЕН permit:

- competing Claims;
- competing mappings;
- distinctness Claims;
- unresolved identity.

Conflict НЕ ДОЛЖЕН be resolved by arbitrary merge.

---

# 48. Identity inconsistency

Identity data МОЖЕТ contain logically incompatible assertions.

Example:

    A same-as B
    B same-as C
    C distinct-from A

System МОЖЕТ detect this as identity inconsistency.

But:

    inconsistency detection
    ≠ automatic resolution

The conflicting assertions and provenance ДОЛЖЕН remain available.

---

# 49. False merge

False merge can combine unrelated:

- Claims;
- Events;
- States;
- Processes;
- Relations;
- Actions;
- Results;
- Sources;
- histories.

Therefore, when evidence is insufficient:

    unresolved identity
    > false merge

---

# 50. False split

False split can represent one Entity as many due to:

- aliases;
- spelling;
- transliteration;
- duplicate Records;
- historical naming.

System СЛЕДУЕТ permit later coreference resolution.

---

# 51. Merge operation ≠ identity truth

Database/data merge:

    ≠ semantic proof of identity

Operational action and identity judgment ДОЛЖЕН remain distinct.

---

# 52. Canonicalization ≠ epistemic resolution

System МОЖЕТ select:

- canonical Record;
- preferred label;
- golden record;

for operational or presentation purposes.

But:

    canonicalization
    ≠ identity truth

    preferred Record
    ≠ only valid Record

Canonicalization НЕ ДОЛЖЕН erase disagreement, uncertainty or provenance.

---

# 53. Duplicate Record ≠ duplicate Entity

Two Records МОЖЕТ be duplicates while referring to one Entity.

Two apparently duplicate Records МОЖЕТ also refer to different Entities.

Therefore:

    duplicate detection
    ≠ Entity identity automatically

---

# 54. Duplicate content

Two Records МОЖЕТ independently contain identical content.

But:

    same content
    ≠ same Record
    ≠ same provenance

---

# 55. Copy identity

A copy МОЖЕТ be:

- distinct physical Entity;
- same semantic work;
- same bit sequence;
- derived representation;
- distinct Record.

Identity depends on level.

---

# 56. Digital copy

Two bit-identical files:

    ≠ same storage/file instance automatically

They МОЖЕТ nevertheless have equivalent content.

---

# 57. Work / edition / version / copy

For documents:

    conceptual work
    ≠ edition
    ≠ version
    ≠ copy
    ≠ representation

These levels ДОЛЖЕН remain distinguishable when material.

---

# 58. Version identity

A newer version МОЖЕТ continue one artifact lineage.

But:

    version-of
    ≠ same representation

and:

    version continuity
    ≠ semantic identity automatically

---

# 59. Correction

Correction of a Record:

    ≠ creation of new underlying referent automatically

But Record/version identity МОЖЕТ change.

---

# 60. Translation

Translation МОЖЕТ represent the same conceptual work while being a distinct textual representation.

Thus:

    translation-of
    ≠ textual identity

---

# 61. Identity through change

Change in:

- State;
- properties;
- location;
- ownership;
- control;
- composition;

does not automatically destroy Entity identity.

Thus:

    changed
    ≠ different Entity automatically

---

# 62. Change does not prove continuity

Opposite safeguard:

    transformation occurred
    ≠ identity necessarily persisted

Identity continuity requires applicable criteria.

---

# 63. Identity persistence

Identity МОЖЕТ persist through change.

But:

    persistence of identity
    ≠ unchanged State

---

# 64. Ship-of-Theseus safeguard

Different criteria МОЖЕТ disagree about identity through gradual replacement.

Possible criteria:

- material;
- structural;
- functional;
- legal;
- historical;
- provenance.

Core НЕ ДОЛЖЕН impose one universal answer.

---

# 65. Material continuity

Material continuity МОЖЕТ support identity.

But:

    same material
    ≠ same Entity universally

    changed material
    ≠ new Entity universally

---

# 66. Spatial continuity

Continuous trajectory МОЖЕТ support identity.

But:

    spatial continuity
    ≠ universal identity proof

---

# 67. Temporal continuity

Temporal continuity МОЖЕТ support identity.

But:

    temporal continuity
    ≠ universal identity proof

---

# 68. Functional continuity

Maintained function МОЖЕТ support identity.

But:

    same function
    ≠ same Entity

---

# 69. Legal continuity

Legal continuity МОЖЕТ define identity within a legal frame.

But:

    legal identity
    ≠ universal physical/historical identity

---

# 70. Institutional identity

Institution МОЖЕТ preserve identity through changes in:

- members;
- leadership;
- address;
- name;
- charter;
- structure.

Criteria МОЖЕТ be domain- or jurisdiction-specific.

---

# 71. Membership continuity

Membership overlap or continuity МОЖЕТ support group identity under some criteria.

But:

    same members
    ≠ same group universally

and:

    changed members
    ≠ different group universally

Membership continuity receives no universal identity privilege.

---

# 72. Merger

Entities МОЖЕТ merge:

    A + B → C

Core НЕ ДОЛЖЕН automatically infer:

    C = A
    C = B

---

# 73. Split

Entity МОЖЕТ split:

    A → B + C

Core НЕ ДОЛЖЕН automatically infer:

    B = A
    C = A

---

# 74. Branching

Lineage МОЖЕТ branch into multiple descendants.

Descendant relation:

    ≠ identity

---

# 75. Successor

Fundamental rule:

    successor-of
    ≠ same-as

Succession МОЖЕТ preserve lineage without preserving identity.

---

# 76. Predecessor

A predecessor МОЖЕТ be a distinct Entity.

Therefore:

    predecessor
    ≠ previous State of same Entity automatically

---

# 77. Lineage

Lineage continuity:

    ≠ identity continuity

---

# 78. Part/whole identity

Part-whole relations ДОЛЖЕН remain distinct from identity.

Thus:

    part-of
    ≠ same-as

    component-of
    ≠ same-as

    fragment-of
    ≠ same-as

A fragment, organ, component or sample originating from an Entity НЕ ДОЛЖЕН automatically inherit whole-Entity identity.

---

# 79. Derived material

Derivative/sample/extract:

    ≠ source Entity

Derivation ДОЛЖЕН remain distinct from identity.

---

# 80. Cross-type identity safeguard

Closely associated objects of different semantic types НЕ ДОЛЖЕН be treated as identical merely because they correspond tightly.

Examples:

    person
    ≠ biography

    country
    ≠ government automatically

    disease
    ≠ pathogen

    software product
    ≠ deployment

    document
    ≠ scan

Different semantic types НЕ ДОЛЖЕН automatically prohibit identity where a domain model explicitly permits it.

But cross-type identity requires explicit semantics.

---

# 81. Biological identity

Biological continuity МОЖЕТ preserve organism identity through material change.

But Core does not impose one theory for all biological cases.

---

# 82. Genetic similarity

Genetic identity/similarity:

    ≠ organism identity

Clone/offspring НЕ ДОЛЖЕН be merged solely by genetic similarity.

---

# 83. Death

Death МОЖЕТ change State without destroying historical referent identity.

Thus:

    Person P alive @ T1
    Person P dead @ T2

МОЖЕТ refer to one historical Entity.

---

# 84. Historical identity

Historical identity resolution ДОЛЖЕН preserve materially relevant:

- names;
- titles;
- spellings;
- languages;
- jurisdictions;
- Sources;
- uncertainty;
- competing interpretations.

Modern standardization НЕ ДОЛЖЕН erase historical ambiguity.

---

# 85. Historical aliases

Historical aliases СЛЕДУЕТ preserve provenance and temporal/contextual frame when material.

---

# 86. Historical homonyms

Same historical name МОЖЕТ refer to different persons, places or institutions.

Label equality НЕ ДОЛЖЕН merge them automatically.

---

# 87. Transliteration

Different transliterations:

    ≠ different Entity automatically

But transliteration similarity alone:

    ≠ identity proof

---

# 88. Titles and offices

Title/office identity ДОЛЖЕН remain distinct from holder identity.

Thus:

    same title
    ≠ same person

    same office
    ≠ same holder

---

# 89. Geographic identity

Place identity МОЖЕТ persist despite:

- renaming;
- rebuilding;
- jurisdiction change;
- boundary change.

Criteria are domain/historically dependent.

---

# 90. Historical geography

Current geographic boundaries НЕ ДОЛЖЕН automatically define historical place/territory identity.

Competing historical mappings ДОЛЖЕН remain representable.

---

# 91. Event identity

Two reports МОЖЕТ refer to same Event.

But:

    same date
    + same place
    + similar description
    ≠ same Event automatically

---

# 92. Event granularity

One Source МОЖЕТ describe one broad Event while another describes several subevents.

Different granularity:

    ≠ contradiction automatically
    ≠ identity automatically

Possible semantics include:

- same broader Event;
- part-of;
- overlap;
- distinct Events.

---

# 93. Process identity

Same Process Content:

    ≠ same Process identity automatically

Process identity МОЖЕТ depend on:

- participants;
- continuity;
- Context;
- temporal structure;
- interruption;
- applicable criterion.

---

# 94. State identity

Same State value:

    ≠ same State identity/continuity automatically

---

# 95. Relation instance identity

Same participants + Relation type:

    ≠ same Relation instance automatically

Identity МОЖЕТ depend on:

- qualifiers;
- temporal frame;
- Scope;
- roles;
- continuity.

---

# 96. Action identity

Repeated performance of same Action type:

    ≠ same Action occurrence

---

# 97. Result identity

Same Result value/content:

    ≠ same Result instance automatically

---

# 98. Claim identity

Two Claims МОЖЕТ express equivalent propositions while remaining distinct Claim Records.

Thus:

    propositional equivalence
    ≠ Claim Record identity

---

# 99. Source identity

Copies, editions, translations and mirrors of a Source ДОЛЖЕН remain distinguishable when provenance matters.

Same content:

    ≠ same Source instance automatically

---

# 100. Observation identity

Two Observations of same phenomenon:

    ≠ same Observation

---

# 101. Measurement identity

Same measured value:

    ≠ same Measurement

Measurement identity МОЖЕТ depend on:

- procedure;
- time;
- sample;
- instrument;
- provenance.

---

# 102. Model identity

Same Model outputs:

    ≠ same Model

---

# 103. Concept identity

Same lexical label:

    ≠ same Concept across all times/domains

Different labels:

    ≠ different Concept automatically

---

# 104. Definition drift

Lexical continuity:

    ≠ conceptual identity

Historical definitions НЕ ДОЛЖЕН silently inherit modern meanings.

---

# 105. Scope-limited identity

Identity МОЖЕТ be asserted only relative to a particular aspect.

Example:

    chemically identical
    ≠ same physical specimen

Scope-limited identity НЕ ДОЛЖЕН silently become unrestricted identity.

---

# 106. Temporal validity of identity mapping

An identity/coreference mapping МОЖЕТ itself be valid only during a defined temporal interval.

Example:

    identifier X → Entity A during T1
    identifier X → Entity B during T2

Therefore:

    identity mapping validity
    ≠ timeless identity automatically

Temporal validity ДОЛЖЕН remain resolvable when materially relevant.

---

# 107. Identity across time

Two temporal representations МОЖЕТ refer to one continuing Entity.

But:

    temporal succession
    ≠ identity continuity automatically

---

# 108. Interruption

Interruption in activity:

    ≠ identity break automatically

But:

    resumption
    ≠ identity continuity automatically

---

# 109. Reassembly

Disassembly and reassembly МОЖЕТ or МОЖЕТ NOT preserve identity.

Applicable criteria decide.

---

# 110. Replacement of components

Replacing components:

    ≠ new Entity automatically

Extensive replacement:

    ≠ guaranteed same Entity

---

# 111. Fusion

Fusion МОЖЕТ produce:

- new Entity;
- continued Entity;
- composite Entity;
- disputed identity.

No universal Core rule decides the outcome.

---

# 112. Fission

Fission МОЖЕТ produce multiple descendants.

Predecessor identity НЕ ДОЛЖЕН automatically propagate to every descendant.

---

# 113. Replica

Replica МОЖЕТ be highly similar to original.

But:

    replica
    ≠ original Entity automatically

---

# 114. Restoration and reconstruction

Restored/reconstructed object МОЖЕТ be:

- same artifact under one criterion;
- a reconstruction;
- a replica;
- disputed continuation.

Core ДОЛЖЕН preserve applicable semantics and uncertainty.

---

# 115. Creation and destruction

Creation Event МОЖЕТ establish identity beginning.

Destruction Event МОЖЕТ establish physical identity termination.

But:

- not every Entity has a discrete known creation Event;
- historical referent remains referenceable after destruction;
- legal/institutional identity МОЖЕТ use different boundaries.

---

# 116. Identity boundary

Identity boundary МОЖЕТ be:

- discrete;
- gradual;
- fuzzy;
- conventional;
- legal;
- disputed;
- unknown.

Identity boundary:

    ≠ Event automatically

---

# 117. State/Event/Process boundary safeguard

State, Event or Process boundaries НЕ ДОЛЖЕН automatically determine Entity identity boundaries.

---

# 118. Strict identity properties

Where a relation represents **strict identity under one compatible identity semantics**, it is normally expected to be:

    reflexive
    symmetric
    transitive

However, these logical properties apply only when:

- identity level is compatible;
- frame is compatible;
- criterion is compatible;
- Scope is compatible;
- temporal validity is compatible;
- semantics is genuinely strict identity rather than qualified sameness, similarity, succession, mapping, representation, derivation or uncertainty.

---

# 119. Reflexivity safeguard

A reference is trivially itself as a reference.

But:

    reference A = reference A

does not resolve what external referent A denotes.

Therefore:

    reference reflexivity
    ≠ resolved referent identity

---

# 120. Symmetry safeguard

Strict identity:

    A = B
    → B = A

under the same applicable semantics.

But symmetry НЕ ДОЛЖЕН automatically propagate to:

- successor-of;
- derived-from;
- resolves-to;
- canonicalizes-to;
- representation-of;
- part-of;
- version-of.

---

# 121. Transitivity safeguard

Strict identity МОЖЕТ support:

    A = B
    B = C
    → A = C

ONLY when relevant identity semantics are compatible.

Identity НЕ ДОЛЖЕН propagate transitively across incompatible:

- identity levels;
- criteria;
- frames;
- Scopes;
- temporal validity;
- uncertainty semantics.

Thus:

    A legally-same-as B
    B historically-same-as C

does NOT automatically establish:

    A = C

---

# 122. Probabilistic identity

Probability of identity:

    P(A = B) = x

НЕ ДОЛЖЕН automatically become deterministic same-as.

---

# 123. Probabilistic chain safeguard

Given:

    P(A=B)=x
    P(B=C)=y

system НЕ ДОЛЖЕН naively infer:

    P(A=C)=x*y

or any other probability without an explicit probabilistic Model and dependency assumptions.

Probabilistic coreference does not inherit strict identity transitivity automatically.

---

# 124. Identity laundering safeguard

A mixed relation chain containing:

- similarity;
- probabilistic coreference;
- qualified sameness;
- succession;
- mapping;
- representation;
- derivation;
- part-whole;
- versioning;
- lineage;

НЕ ДОЛЖЕН be compressed, summarized or inferred as strict identity unless an explicit valid identity inference establishes that result.

For example:

    A probably-corefers B
    B same-as C
    C successor-of D

НЕ ДОЛЖЕН become:

    A = D

merely through chaining or summarization.

Thus:

    chain of identity-adjacent relations
    ≠ strict identity

---

# 125. Algorithmic identity resolution

Algorithm МОЖЕТ propose matches.

But:

    algorithmic match
    ≠ identity truth

When material, resolution СЛЕДУЕТ preserve:

- Model/version;
- inputs;
- assumptions;
- threshold;
- confidence;
- conflicting evidence.

---

# 126. Threshold-based merge

Policy:

    score > X → merge

is an operational decision rule.

It:

    ≠ semantic proof of identity

Underlying uncertainty СЛЕДУЕТ remain recoverable where material.

---

# 127. Reversible identity resolution

Where feasible, identity resolution СЛЕДУЕТ preserve enough information for:

- unmerge;
- split;
- remap;
- reinterpretation;
- later correction.

---

# 128. Identity correction

Later Evidence МОЖЕТ show earlier resolution was wrong.

System ДОЛЖЕН permit correction without pretending the earlier state never existed.

---

# 129. Identity revision history

Material changes СЛЕДУЕТ preserve:

- previous mapping;
- new mapping;
- reason;
- Evidence;
- author/system;
- date/version.

---

# 130. Later resolution ≠ retroactive knowledge

A historically ambiguous reference МОЖЕТ later be resolved.

Example:

    original source: "Ivan"
    later research: Ivan B

Later resolution НЕ ДОЛЖЕН rewrite the original Source as though its author possessed that later knowledge.

Therefore:

    later referent resolution
    ≠ retroactive alteration of original reference semantics

Both МОЖЕТ coexist:

    original reference: ambiguous
    current interpretation: resolves to B

---

# 131. Identity and provenance

Coreference НЕ ДОЛЖЕН collapse provenance.

If Records A and B refer to one Entity:

    provenance(A)
    remains provenance(A)

    provenance(B)
    remains provenance(B)

Thus:

    same referent
    ≠ same provenance

---

# 132. Identity and contradictions

After coreference, conflicting attributes МОЖЕТ indicate:

- different times;
- changed State;
- bad data;
- different Context;
- false merge;
- real disagreement.

Identity resolution НЕ ДОЛЖЕН erase these conflicts.

---

# 133. Identity propagation

Resolved identity МОЖЕТ support reference propagation.

But propagation ДОЛЖЕН preserve:

- time;
- Context;
- Scope;
- role;
- provenance;
- uncertainty.

---

# 134. Unsafe identity propagation

Even strict Entity identity does not license copying every property across all times.

Example:

    P alive @ T1
    P dead @ T2

Same Entity is compatible with different States.

---

# 135. Uncertain identity propagation

If:

    A probably corefers B

knowledge attached to A НЕ ДОЛЖЕН silently become certain knowledge about B.

Uncertainty ДОЛЖЕН propagate or remain explicitly bounded where material.

---

# 136. Historical transfer safeguard

Historical identity/coreference НЕ ДОЛЖЕН automatically transfer across time or frames:

- properties;
- responsibility;
- guilt;
- rights;
- ownership;
- territorial claims;
- ancestry;
- achievements;
- obligations;
- authority.

Such transfers require their own Relations/Claims/rules.

Thus:

    identity
    ≠ responsibility inheritance

    identity
    ≠ ownership continuity

    identity
    ≠ entitlement

---

# 137. Authority-defined identity

Registry, court or institution МОЖЕТ define identity within a relevant frame.

But:

    authority-defined identity
    ≠ universal ontological truth

The authoritative frame СЛЕДУЕТ remain resolvable.

---

# 138. Competing identity systems

Different systems МОЖЕТ define incompatible identity boundaries.

Examples:

- legal;
- historical;
- biological;
- archival;
- technical.

They МОЖЕТ coexist if frames/criteria remain explicit.

---

# 139. Cross-system mapping

Mapping:

    ID_A ↔ ID_B

МОЖЕТ mean:

- exact identity;
- probable coreference;
- version correspondence;
- broader/narrower mapping;
- administrative correspondence.

Therefore:

    mapped-to
    ≠ same-as automatically

---

# 140. One-to-many and many-to-one mapping

System ДОЛЖЕН permit:

    one → many
    many → one

mappings.

They НЕ ДОЛЖЕН be forced into one-to-one identity.

---

# 141. Identity clusters

Implementation МОЖЕТ cluster Records believed to corefer.

But:

    cluster membership
    ≠ identity truth automatically

Clusters МОЖЕТ be provisional.

---

# 142. Golden record

Synthesized `golden record` МОЖЕТ combine data from multiple Records.

But НЕ ДОЛЖЕН erase:

- provenance;
- disagreement;
- temporal differences;
- uncertain identity.

---

# 143. Normalization

Normalization МОЖЕТ standardize:

- capitalization;
- transliteration;
- whitespace;
- date format;
- identifier syntax.

But:

    normalization
    ≠ identity resolution

---

# 144. Geospatial identity resolution

Place resolution МОЖЕТ use:

- coordinates;
- names;
- boundaries;
- maps;
- jurisdiction;
- feature type;
- historical evidence.

No one field is universally sufficient.

---

# 145. Temporal identity resolution

Temporal compatibility МОЖЕТ be evidence for or against identity.

But:

    temporal gap
    ≠ distinctness universally

and:

    temporal overlap
    ≠ identity universally

---

# 146. Simultaneous incompatible histories

If two alleged identities have independently established simultaneous histories incompatible with one Entity under applicable semantics, this МОЖЕТ support distinctness.

But distributed/composite Entities require domain-aware interpretation.

---

# 147. Hashing and checksums

Hash/checksum equality МОЖЕТ support content equality under technical assumptions.

But:

    same hash
    ≠ same domain Entity universally

---

# 148. Physical labels and serial numbers

Serial/tag МОЖЕТ support identity.

But МОЖЕТ be:

- forged;
- replaced;
- duplicated;
- transferred;
- damaged.

Thus:

    label identity
    ≠ object identity automatically

---

# 149. Ownership and control

Ownership/control changes:

    ≠ Entity identity changes automatically

And Entity identity:

    ≠ ownership continuity automatically

---

# 150. Aggregate/group identity

Group identity ДОЛЖЕН remain distinct from member identity.

Same membership:

    ≠ same group universally

Different membership:

    ≠ different group universally

---

# 151. Dataset identity

Dataset lineage МОЖЕТ persist across versions.

But:

    same dataset lineage
    ≠ same dataset version

---

# 152. Software identity

Software identity МОЖЕТ refer to:

- product;
- codebase;
- version;
- build;
- deployment;
- process instance;
- logical service.

These ДОЛЖЕН remain distinguishable when material.

---

# 153. Abstract-object identity

Concepts, propositions, numbers and Models МОЖЕТ require different identity criteria from physical objects.

Physical continuity rules НЕ ДОЛЖЕН be blindly transferred to abstract objects.

---

# 154. Proposition identity

Two Claims МОЖЕТ express logically equivalent propositions.

But:

    proposition equivalence
    ≠ Claim Record identity

---

# 155. Ontology and taxonomy migration

Taxonomic/ontological change МОЖЕТ alter classification or identifiers without changing domain Entity identity.

Migration mapping НЕ ДОЛЖЕН automatically become identity assertion.

---

# 156. Serialization and carrier neutrality

Different serialization:

- JSON;
- RDF;
- Markdown;
- SQL;
- printed text;

does not determine semantic identity.

Carrier technology:

    ≠ identity semantics

---

# 157. Historical reconstruction

Historical identity reconstruction СЛЕДУЕТ preserve:

- Sources;
- aliases;
- chronology;
- location;
- relationships;
- assumptions;
- uncertainty;
- competing candidates.

Missing identity evidence НЕ ДОЛЖЕН be invented.

---

# 158. Damaged archives

Ambiguous historical references ДОЛЖЕН remain ambiguous when evidence is insufficient.

The system НЕ ДОЛЖЕН manufacture identity merely to obtain a clean graph.

---

# 159. Oral traditions

Names and lineages from oral traditions МОЖЕТ have uncertain mappings.

Modern normalization НЕ ДОЛЖЕН silently force them into one identity.

---

# 160. Archaeological fragments

Fragments МОЖЕТ or МОЖЕТ NOT belong to one original artifact.

Material/type similarity:

    ≠ same original object automatically

---

# 161. Samples and specimens

Sample/specimen identity ДОЛЖЕН remain distinct from source Entity identity.

Example:

    sample S from Person P

does not imply:

    S = P

---

# 162. Evidence identity

Evidence item:

    ≠ Entity it evidences

Evidence relation НЕ ДОЛЖЕН become identity.

---

# 163. Citation and Source identity

Two citations МОЖЕТ refer to:

- same work;
- different editions;
- different copies;
- same Source instance.

Citation matching ДОЛЖЕН preserve the relevant Source identity level.

---

# 164. Identity representation fidelity

Representation НЕ ДОЛЖЕН materially alter:

- identity level;
- frame;
- criterion;
- Scope;
- referent;
- Record identity;
- representation identity;
- coreference status;
- distinctness;
- temporal validity;
- uncertainty;
- provenance;
- competing candidates.

---

# 165. Translation Fidelity

Translation ДОЛЖЕН preserve distinctions such as:

    same Entity
    ≠ same Record

    same referent
    ≠ same expression

    equivalent
    ≠ identical

    qualified sameness
    ≠ strict identity

    part-of
    ≠ same-as

    representation-of
    ≠ same-as

    successor
    ≠ same Entity

    probably same
    ≠ same

    unknown identity
    ≠ distinct

---

# 166. Summary Fidelity

Summary НЕ ДОЛЖЕН convert:

    possible coreference
    → identity

    probable match
    → identity

    qualified sameness
    → strict identity

    same name
    → same Entity

    similarity
    → identity

    equivalence
    → identity

    successor
    → identity

    part
    → whole identity

    representation
    → represented Entity

    duplicate Record
    → duplicate Entity

    changed State
    → new Entity

    later resolution
    → historical certainty

Mixed chains ДОЛЖЕН obey the Identity Laundering Safeguard.

---

# 167. Identity compression

Compression МОЖЕТ omit non-material detail.

But НЕ ДОЛЖЕН erase materially relevant:

- level;
- frame;
- criterion;
- Scope;
- uncertainty;
- temporal validity;
- provenance;
- alternatives;
- historical ambiguity.

---

# 168. Offline preservation

Identity СЛЕДУЕТ remain resolvable without dependence on a live registry.

Where materially relevant preserve:

- local stable identifier;
- namespace;
- aliases;
- human-readable description;
- Source references;
- historical names;
- identity status;
- provenance;
- uncertainty.

---

# 169. Human-resolvable identity

Machine identifier alone МОЖЕТ be insufficient for long-term preservation.

High-value Records СЛЕДУЕТ preserve, where feasible:

- name;
- date;
- location;
- Context;
- lineage;
- distinguishing description.

---

# 170. High-risk Profiles

High-risk Profiles МОЖЕТ require stricter identity resolution.

Examples:

- medicine;
- engineering;
- hazardous materials;
- legal records;
- historical persons;
- chemical samples;
- survival procedures.

Profile МОЖЕТ require:

- strong identifiers;
- chain of custody;
- multiple-factor resolution;
- manual confirmation;
- explicit uncertainty.

---

# 171. Conformance ≠ truth

Need distinguish:

    structural conformance
    ≠ identity truth
    ≠ provenance integrity
    ≠ historical certainty
    ≠ semantic equivalence

Validator PASS does not prove identity.

---

# 172. Machine validation

Validator МОЖЕТ detect:

- identifier syntax errors;
- namespace absence;
- duplicate identifier constraints;
- Profile identity-key violations;
- temporal incompatibilities;
- contradictory strict identity graphs;
- incompatible same/distinct assertions;
- invalid mapping structure.

But:

    validator detection
    ≠ semantic resolution

Validator has no identity privilege.

---

# 173. Межстандартная совместимость

`014-IDENTITY` preserves boundaries with neighboring standards:

    Action identity
    → specific Action occurrence

    Event identity
    → specific Event occurrence

    Result identity
    → specific Result instance/role

    State identity
    → specific represented condition/continuity

    Process identity
    → specific temporally extended Process

    Relation identity
    → specific Relation instance

Therefore:

    same Action type
    ≠ same Action

    similar Events
    ≠ same Event

    same Result value
    ≠ same Result

    same State value
    ≠ same State

    same Process Content
    ≠ same Process

    same participants + Relation type
    ≠ same Relation instance

---

# 174. Identity and Relation

Identity МОЖЕТ use Relation infrastructure.

But the following ДОЛЖЕН remain distinguishable:

- same-as;
- corefers-with;
- same-record-as;
- equivalent-to;
- similar-to;
- successor-of;
- version-of;
- part-of;
- representation-of.

`013-RELATION` provides Relation infrastructure.

`014` defines identity semantics and safeguards.

---

# 175. Identity and State

State change:

    ≠ Entity replacement automatically

State identity and Entity identity remain distinct.

---

# 176. Identity and Event

Event МОЖЕТ create, destroy, merge, split, rename or transform Entities.

But Event alone does not determine identity continuity unless applicable semantics supports it.

---

# 177. Identity and Process

Process continuity and Entity identity are independent dimensions.

---

# 178. Identity and Action

Repeated Action:

    ≠ same Action instance

Action affecting identity Records:

    ≠ underlying Entity changed automatically

---

# 179. Identity and Result

Result equivalence:

    ≠ Result identity

---

# 180. Identity and Claim

Identity assertion МОЖЕТ itself be represented as Claim.

Two identity Claims МОЖЕТ conflict while retaining independent provenance.

---

# 181. Identity and Source

Source assertions ДОЛЖЕН remain distinguishable from system resolution.

Source copies/editions ДОЛЖЕН preserve relevant identity level.

---

# 182. Identity and Observation/Measurement

Same subject:

    ≠ same Observation
    ≠ same Measurement

---

# 183. Identity and Decision

Identity information available at Decision time ДОЛЖЕН reflect what was available then.

Later identity resolution НЕ ДОЛЖЕН be inserted retroactively into historical Decision Basis.

---

# 184. Тест на разрастание сущностей

`014` does NOT require the following as new fundamental Core Entities merely to express identity:

- Identity;
- IdentityType;
- IdentityCriterion;
- IdentityFrame;
- IdentityScope;
- Coreference;
- IdentityResolution;
- IdentityCandidate;
- IdentityCluster;
- IdentityConflict;
- IdentityConfidence;
- IdentityEvidence;
- Alias;
- Identifier;
- IdentifierNamespace;
- Duplicate;
- CanonicalRecord;
- GoldenRecord;
- HistoricalIdentity;
- IdentityBoundary;
- IdentityMapping;
- DistinctnessEntity.

These МОЖЕТ be represented through:

- Relations;
- Claims;
- Records;
- Sources;
- Profiles;
- Models;
- Inferences;
- identifiers;
- provenance structures;
- mappings;
- existing Core infrastructure.

Absence of a separate Core Entity does not mean absence of semantics.

---

# 185. Core invariants

Следующие положения образуют нормативное ядро `014-IDENTITY`.

### ID-01
Identity ДОЛЖЕН remain resolvable relative to an identity-bearing level/frame when ambiguity is materially relevant.

### ID-02
Identity НЕ ДОЛЖЕН be treated as one universal undifferentiated `same-as`.

### ID-03
Identity criterion ДОЛЖЕН remain resolvable when choice of criterion materially affects identity judgment.

### ID-04
No identity criterion receives universal privilege across all domains.

### ID-05
Identity frame, identity criterion and Identity Scope ДОЛЖЕН remain distinguishable when materially relevant.

### ID-06
Identity criterion ДОЛЖЕН remain distinguishable from identity Evidence.

### ID-07
Entity identity, referent identity, coreference, Record identity, representation identity, semantic equivalence and value equality ДОЛЖЕН remain distinguishable when material.

### ID-08
Identity representation/assertion НЕ ДОЛЖЕН automatically be treated as identity truth.

### ID-09
Identity semantics НЕ ДОЛЖЕН require a dedicated fundamental Identity Entity.

### ID-10
Same referent НЕ ДОЛЖЕН automatically imply same Record.

### ID-11
Different Records НЕ ДОЛЖЕН automatically imply distinct referents.

### ID-12
Same Record НЕ ДОЛЖЕН automatically imply same carrier/representation instance.

### ID-13
Representation-of, description-of, model-of and record-about НЕ ДОЛЖЕН automatically imply identity with represented subject.

### ID-14
Semantic equivalence НЕ ДОЛЖЕН automatically imply Entity or Record identity.

### ID-15
Value equality НЕ ДОЛЖЕН automatically imply identity.

### ID-16
Attribute equality НЕ ДОЛЖЕН automatically imply identity.

### ID-17
Similarity НЕ ДОЛЖЕН automatically imply identity.

### ID-18
Equivalence НЕ ДОЛЖЕН automatically imply identity.

### ID-19
Qualified sameness НЕ ДОЛЖЕН automatically inherit strict identity semantics.

### ID-20
Interchangeability НЕ ДОЛЖЕН automatically imply identity.

### ID-21
Same classification НЕ ДОЛЖЕН imply same instance.

### ID-22
Lexical/name equality НЕ ДОЛЖЕН automatically establish referent identity.

### ID-23
Name difference НЕ ДОЛЖЕН automatically establish distinctness.

### ID-24
Alias НЕ ДОЛЖЕН automatically be treated as proven identity.

### ID-25
Renaming НЕ ДОЛЖЕН automatically imply new Entity.

### ID-26
Identifier ДОЛЖЕН remain distinguishable from Entity.

### ID-27
Identifier namespace ДОЛЖЕН remain resolvable when material.

### ID-28
Same identifier string across namespaces НЕ ДОЛЖЕН automatically imply identity.

### ID-29
Identifier uniqueness НЕ ДОЛЖЕН be generalized beyond declared governance/frame.

### ID-30
Persistent identifier НЕ ДОЛЖЕН automatically prove unchanged referent.

### ID-31
Identifier reuse/reassignment ДОЛЖЕН remain representable.

### ID-32
Identity resolution СЛЕДУЕТ preserve materially relevant provenance.

### ID-33
No individual identity signal is universally sufficient.

### ID-34
Multiple weak signals НЕ ДОЛЖЕН automatically establish identity.

### ID-35
Single mismatch НЕ ДОЛЖЕН automatically establish distinctness.

### ID-36
Identity resolution ДОЛЖЕН remain distinct from identity judgment/relation.

### ID-37
System-resolved identity ДОЛЖЕН remain scoped to applicable semantics and НЕ ДОЛЖЕН automatically become universal identity truth.

### ID-38
Source-asserted identity ДОЛЖЕН remain distinguishable from system-resolved identity.

### ID-39
Identity assertion МОЖЕТ remain a Claim without forcing merge.

### ID-40
Unknown identity ДОЛЖЕН remain distinct from sameness and distinctness.

### ID-41
Failure to prove identity НЕ ДОЛЖЕН establish distinctness automatically.

### ID-42
Distinctness МОЖЕТ require independent evidence/provenance.

### ID-43
Distinctness ДОЛЖЕН preserve applicable identity level/frame/criterion/Scope where materially relevant.

### ID-44
Competing identity resolutions ДОЛЖЕН remain representable.

### ID-45
Identity inconsistency detection НЕ ДОЛЖЕН automatically resolve inconsistency.

### ID-46
Uncertain identity НЕ ДОЛЖЕН silently become hard merge.

### ID-47
Data merge/canonicalization ДОЛЖЕН remain distinguishable from semantic identity resolution.

### ID-48
Canonical Record ДОЛЖЕН remain distinguishable from underlying Entity.

### ID-49
Canonicalization/golden-record synthesis НЕ ДОЛЖЕН erase provenance, uncertainty or disagreement.

### ID-50
Duplicate Record ДОЛЖЕН remain distinguishable from duplicate Entity.

### ID-51
Duplicate content НЕ ДОЛЖЕН imply same Record or same provenance automatically.

### ID-52
Work, edition, version, copy and representation identity ДОЛЖЕН remain distinguishable where material.

### ID-53
Bit/content equality НЕ ДОЛЖЕН automatically imply domain Entity identity.

### ID-54
Version-of НЕ ДОЛЖЕН automatically imply same representation.

### ID-55
Correction НЕ ДОЛЖЕН automatically imply new underlying referent.

### ID-56
Translation-of НЕ ДОЛЖЕН automatically imply textual identity.

### ID-57
State/property/location/ownership/control change НЕ ДОЛЖЕН automatically imply new Entity.

### ID-58
Transformation НЕ ДОЛЖЕН automatically establish identity persistence.

### ID-59
Identity persistence ДОЛЖЕН remain distinguishable from unchanged State.

### ID-60
Material, spatial, temporal, functional and legal continuity receive no universal identity privilege.

### ID-61
Membership continuity receives no universal group-identity privilege.

### ID-62
Merger НЕ ДОЛЖЕН automatically identify successor with every predecessor.

### ID-63
Split/fission НЕ ДОЛЖЕН automatically identify every descendant with predecessor.

### ID-64
Successor-of НЕ ДОЛЖЕН automatically imply identity.

### ID-65
Lineage continuity ДОЛЖЕН remain distinguishable from identity continuity.

### ID-66
Part-of, component-of and fragment-of НЕ ДОЛЖЕН automatically imply identity with whole.

### ID-67
Sample/specimen/derived material НЕ ДОЛЖЕН automatically inherit source Entity identity.

### ID-68
Cross-type correspondence НЕ ДОЛЖЕН automatically establish identity.

### ID-69
Cross-type identity, where valid, requires explicit applicable semantics.

### ID-70
Genetic similarity/identity НЕ ДОЛЖЕН automatically imply organism identity.

### ID-71
Historical identity resolution ДОЛЖЕН preserve materially relevant historical names, Sources, frames and uncertainty.

### ID-72
Historical homonyms НЕ ДОЛЖЕН be merged solely by label equality.

### ID-73
Role/title/office identity ДОЛЖЕН remain distinct from holder identity.

### ID-74
Current geographic boundaries НЕ ДОЛЖЕН automatically determine historical geographic identity.

### ID-75
Event coreference НЕ ДОЛЖЕН be established solely from date/place/description similarity.

### ID-76
Different Event granularity НЕ ДОЛЖЕН automatically imply identity or contradiction.

### ID-77
Same Process Content НЕ ДОЛЖЕН automatically imply same Process.

### ID-78
Same State value НЕ ДОЛЖЕН automatically imply same State identity.

### ID-79
Same participants + Relation type НЕ ДОЛЖЕН automatically imply same Relation instance.

### ID-80
Repeated Action type НЕ ДОЛЖЕН imply same Action instance.

### ID-81
Same Result value/content НЕ ДОЛЖЕН automatically imply same Result instance.

### ID-82
Propositional equivalence НЕ ДОЛЖЕН imply Claim Record identity.

### ID-83
Same Source content НЕ ДОЛЖЕН automatically imply same Source instance when provenance matters.

### ID-84
Same measured value НЕ ДОЛЖЕН imply same Measurement.

### ID-85
Same Model output НЕ ДОЛЖЕН imply same Model.

### ID-86
Lexical continuity НЕ ДОЛЖЕН automatically imply Concept identity across time/domains.

### ID-87
Scope-limited identity НЕ ДОЛЖЕН silently become unrestricted identity.

### ID-88
Qualified identity language ДОЛЖЕН preserve its qualifier.

### ID-89
Temporal validity of identity mapping ДОЛЖЕН remain resolvable when material.

### ID-90
Temporal succession НЕ ДОЛЖЕН automatically establish identity continuity.

### ID-91
Identity boundary МОЖЕТ be fuzzy, conventional, legal, disputed or unknown.

### ID-92
Identity boundary НЕ ДОЛЖЕН automatically be modeled as Event.

### ID-93
State/Event/Process boundaries НЕ ДОЛЖЕН automatically determine Entity identity boundaries.

### ID-94
Strict identity logical properties apply only under compatible level, frame, criterion, Scope, temporal validity and semantics.

### ID-95
Reference reflexivity НЕ ДОЛЖЕН be treated as resolved referent identity.

### ID-96
Symmetry of strict identity НЕ ДОЛЖЕН be inherited by directional mappings, succession, derivation, part-whole or representation relations.

### ID-97
Identity НЕ ДОЛЖЕН propagate transitively across incompatible identity levels, criteria, frames, Scopes, temporal validity or uncertainty semantics.

### ID-98
Probabilistic/uncertain coreference НЕ ДОЛЖЕН automatically inherit strict identity transitivity.

### ID-99
Identity probabilities НЕ ДОЛЖЕН be naively composed without explicit probabilistic Model and dependency assumptions.

### ID-100
Mixed chains of identity-adjacent relations НЕ ДОЛЖЕН be laundered into strict identity without an explicit valid identity inference.

### ID-101
Algorithmic match НЕ ДОЛЖЕН automatically be treated as identity truth.

### ID-102
Threshold merge policy ДОЛЖЕН remain distinguishable from semantic identity judgment.

### ID-103
Identity resolution СЛЕДУЕТ remain reversible where materially feasible.

### ID-104
Identity correction СЛЕДУЕТ preserve prior materially relevant mappings and provenance.

### ID-105
Later referent resolution НЕ ДОЛЖЕН retroactively alter original Source/reference semantics.

### ID-106
Coreference НЕ ДОЛЖЕН collapse independent provenance.

### ID-107
Identity resolution НЕ ДОЛЖЕН automatically erase factual conflicts.

### ID-108
Identity-based propagation ДОЛЖЕН preserve time, Context, Scope, role, provenance and uncertainty.

### ID-109
Uncertain identity НЕ ДОЛЖЕН silently propagate linked Claims as certain knowledge.

### ID-110
Historical identity/coreference НЕ ДОЛЖЕН automatically transfer responsibility, rights, ownership, territory, ancestry, achievements, obligations or authority.

### ID-111
Identity ДОЛЖЕН remain distinguishable from responsibility inheritance, entitlement and ownership continuity.

### ID-112
Authority-defined identity ДОЛЖЕН remain scoped to relevant authoritative frame.

### ID-113
Competing identity systems МОЖЕТ coexist when frames/criteria are explicit.

### ID-114
Cross-system mapping НЕ ДОЛЖЕН automatically imply exact identity.

### ID-115
One-to-many and many-to-one mappings ДОЛЖЕН remain representable.

### ID-116
Identity-cluster membership НЕ ДОЛЖЕН automatically imply identity truth.

### ID-117
Normalization ДОЛЖЕН remain distinguishable from identity resolution.

### ID-118
Hash/checksum equality НЕ ДОЛЖЕН automatically determine domain Entity identity.

### ID-119
Physical label/serial identity НЕ ДОЛЖЕН automatically determine object identity outside defined governance assumptions.

### ID-120
Aggregate/group identity ДОЛЖЕН remain distinguishable from member identity.

### ID-121
Dataset lineage ДОЛЖЕН remain distinguishable from dataset-version identity.

### ID-122
Software product/codebase/version/build/deployment/process identity ДОЛЖЕН remain distinguishable when material.

### ID-123
Physical identity criteria НЕ ДОЛЖЕН be blindly transferred to abstract objects.

### ID-124
Ontology/taxonomy migration НЕ ДОЛЖЕН automatically imply domain Entity change.

### ID-125
Carrier/serialization technology НЕ ДОЛЖЕН determine semantic identity.

### ID-126
Historical reconstruction ДОЛЖЕН preserve materially relevant alternatives, Sources and assumptions.

### ID-127
Missing identity evidence НЕ ДОЛЖЕН be invented to produce a clean graph.

### ID-128
Evidence item ДОЛЖЕН remain distinguishable from Entity it evidences.

### ID-129
Identity structure conformance ДОЛЖЕН remain distinct from identity truth and historical certainty.

### ID-130
Profile МОЖЕТ strengthen Core identity requirements but НЕ ДОЛЖЕН weaken Core while claiming compatibility.

### ID-131
Materially relevant identity level, frame, criterion, Scope, temporal validity, uncertainty, provenance and competing candidates ДОЛЖЕН remain resolvable.

---

# 186. Diagnostic families

## 186.1. Level collapse

Examples:

- same Entity → same Record;
- coreference → Record identity;
- same Record → same carrier;
- semantic equivalence → Entity identity.

## 186.2. Name/identifier collapse

Examples:

- same name → same Entity;
- different name → different Entity;
- same identifier across namespaces → same Entity;
- identifier reuse ignored.

## 186.3. Similarity/equivalence collapse

Examples:

- similar → same;
- equivalent → identical;
- interchangeable → identical;
- qualified sameness → strict identity.

## 186.4. Representation collapse

Examples:

- photo → person;
- Record → referent;
- model → modeled Entity;
- digital twin → physical Entity.

## 186.5. Part/whole collapse

Examples:

- fragment → artifact;
- sample → source Entity;
- component → whole.

## 186.6. Version/copy collapse

Examples:

- copy → original;
- translation → same text;
- version → same representation;
- duplicate content → same Record.

## 186.7. Continuity collapse

Examples:

- changed State → new Entity;
- same function → same Entity;
- transformation → guaranteed continuity;
- component continuity → universal identity.

## 186.8. Succession collapse

Examples:

- successor → same Entity;
- merger → successor identical to all predecessors;
- split → descendants identical to predecessor.

## 186.9. Historical collapse

Examples:

- modern name → historical certainty;
- same title → same person;
- modern boundary → historical territory identity;
- modern identity → inherited historical rights/responsibility.

## 186.10. Resolution collapse

Examples:

- Source assertion → system identity;
- local resolution → universal truth;
- probable → certain;
- candidate → resolved;
- unknown → distinct;
- algorithmic score → truth.

## 186.11. Logical-property failure

Examples:

- transitivity across incompatible criteria;
- symmetry applied to successor relation;
- reflexive reference treated as resolved referent;
- probabilistic identity chain multiplied without Model.

## 186.12. Identity laundering

Examples:

- probable coreference + strict identity → universal identity;
- identity + succession → strict identity with successor;
- versioning chain → same Entity without criterion;
- part-of chain → whole identity;
- mapping chain → exact identity without semantics.

## 186.13. Provenance collapse

Examples:

- same referent → same provenance;
- canonical Record → only valid Record;
- identity correction erases old resolution.

## 186.14. Propagation failure

Examples:

- identity → all properties copied across time;
- uncertain coreference → certain Claim propagation;
- historical identity → ownership/responsibility transfer.

Diagnostic label does not itself establish:

- fraud;
- negligence;
- intent;
- blame;
- responsibility.

---

# 187. Stress-test framework

`014-IDENTITY` ДОЛЖЕН remain robust against at least:

1. Entity vs Record identity;
2. referent vs expression identity;
3. coreference vs Record identity;
4. representation vs represented Entity;
5. semantic equivalence vs identity;
6. value equality vs identity;
7. similarity vs identity;
8. qualified sameness vs strict identity;
9. same class vs same instance;
10. names and aliases;
11. homonyms;
12. transliteration;
13. identifier namespace;
14. identifier reuse;
15. identifier collision;
16. criterion vs Evidence;
17. frame vs criterion vs Scope;
18. asserted vs resolved identity;
19. local resolution vs universal identity;
20. unknown vs distinct;
21. distinctness across levels;
22. competing identity Claims;
23. identity inconsistency;
24. false merge;
25. false split;
26. duplicates;
27. copies;
28. versions;
29. translations;
30. correction;
31. Ship of Theseus;
32. material continuity;
33. functional continuity;
34. legal continuity;
35. institutional continuity;
36. membership replacement;
37. merger;
38. split;
39. succession;
40. lineage;
41. part vs whole;
42. sample vs source;
43. cross-type identity;
44. digital twin vs physical object;
45. biological continuity;
46. genetic similarity;
47. historical identity;
48. historical homonyms;
49. titles/offices;
50. historical geography;
51. Event coreference;
52. Event granularity;
53. Process identity;
54. State identity;
55. Relation instance identity;
56. Action identity;
57. Result identity;
58. Claim identity;
59. Source identity;
60. Measurement identity;
61. Model identity;
62. Concept drift;
63. Scope-limited identity;
64. temporal mapping validity;
65. identity through interruption;
66. reassembly;
67. reconstruction;
68. replica;
69. identity boundary;
70. reflexivity;
71. symmetry;
72. transitivity;
73. cross-frame transitivity;
74. cross-criterion transitivity;
75. probabilistic coreference;
76. probabilistic chains;
77. identity laundering;
78. algorithmic resolution;
79. threshold merge;
80. reversible resolution;
81. later identity correction;
82. retroactive resolution;
83. provenance after merge;
84. contradiction after merge;
85. unsafe property propagation;
86. uncertain identity propagation;
87. historical responsibility transfer;
88. ownership transfer;
89. competing identity systems;
90. cross-system mapping;
91. one-to-many mapping;
92. many-to-one mapping;
93. identity clusters;
94. canonical Records;
95. golden records;
96. normalization vs resolution;
97. geospatial resolution;
98. temporal resolution;
99. hashing;
100. serial numbers;
101. aggregate identity;
102. dataset lineage;
103. software identity;
104. abstract objects;
105. ontology migration;
106. damaged archives;
107. oral traditions;
108. archaeological fragments;
109. specimens;
110. Evidence vs Entity;
111. offline preservation;
112. high-risk Profiles;
113. translation corruption;
114. summary corruption;
115. cross-standard collision;
116. Entity Explosion.

Stress tests do not create Core requirements by themselves.

If a test reveals a necessary fundamental rule, that rule ДОЛЖЕН be incorporated into the normative architecture.

---

# 188. Принцип сохранения

При конфликте между удобством объединения и честностью representation предпочтение отдаётся честности.

    unresolved identity
    > false merge

    probable coreference
    > invented certainty

    qualified sameness
    > invented strict identity

    same name
    > invented same Entity

    similarity
    > invented identity

    equivalence
    > invented identity

    part-of
    > invented same-as

    representation-of
    > invented same-as

    same referent
    > false Record identity

    different Records
    > invented distinct referents

    duplicate Record
    > invented duplicate Entity

    successor
    > invented identity continuity

    historical ambiguity
    > modern forced identity

    separate provenance
    > flattened provenance

    candidate matches
    > arbitrary resolution

    reversible resolution
    > irreversible false merge

    explicit criterion
    > hidden identity assumption

    explicit Scope
    > unrestricted identity assumption

    unresolved conflict
    > fabricated consistency

Цель стандарта — сохранить identity настолько точно, насколько позволяют данные, не превращая similarity в sameness, qualified continuity в strict identity, aliases в proof, identifiers в Entities, parts в wholes, representations в represented objects, succession в identity, algorithmic matching в truth или современную интерпретацию в историческую определённость.

---

# 189. Итоговая формула

В компактной форме:

    Entity identity
    → тот ли это domain object

    Coreference
    → относятся ли references
      к одному referent

    Record identity
    → та ли это запись

    Representation identity
    → та ли это representation

    Semantic equivalence
    → эквивалентно ли содержание
      относительно defined semantics

    Identity frame
    → внутри какой semantic/reference system
      рассматривается judgment

    Identity criterion
    → по какому правилу
      определяется sameness/continuity

    Identity Scope
    → к какому аспекту
      относится judgment

    Identity Evidence
    → на каких основаниях считается,
      что criterion выполнен

    Identity resolution
    → насколько и на каких основаниях
      sameness/distinctness установлены

И:

    frame
    ≠ criterion
    ≠ Scope
    ≠ Evidence

    same referent
    ≠ same Record

    different Records
    ≠ distinct referents

    same Record
    ≠ same carrier

    same value
    ≠ same Entity

    similarity
    ≠ identity

    equivalence
    ≠ identity

    qualified sameness
    ≠ strict identity automatically

    part-of
    ≠ same-as

    representation-of
    ≠ same-as

    successor-of
    ≠ same-as

    asserted identity
    ≠ resolved identity

    resolved identity
    ≠ universal identity truth

    unknown
    ≠ distinct

    identity
    ≠ responsibility

    identity
    ≠ ownership continuity

А для логического распространения:

    A = B
    B = C

не даёт автоматически:

    A = C

если отличаются:

    level
    criterion
    frame
    Scope
    temporal validity
    uncertainty semantics

И цепочка:

    probable coreference
    → mapping
    → succession
    → similarity

не может быть сжата до:

    strict identity

без отдельного валидного identity inference.

---

# 190. Центральный принцип

> **Сохранить identity — значит сохранить не только ответ «одно это или разное», но и уровень идентичности, frame, criterion, Scope, временную применимость, основания, uncertainty и provenance этого ответа, не позволяя системе превратить сходство, квалифицированную эквивалентность, связь, представление, часть, преемственность, техническое сопоставление или позднейшую интерпретацию в ложное тождество.**

---

# 191. Статус версии

**014-IDENTITY v0.1**

Версия включает результаты:

- первоначальной архитектурной сборки;
- полной adversarial attack;
- чистовой пересборки;
- контрольного аудита;
- финального hardening.

В финальную версию встроены:

- identity level;
- identity frame;
- identity criterion;
- Identity Scope;
- criterion/Evidence separation;
- qualified sameness safeguard;
- temporal validity identity mappings;
- scoped system resolution;
- strict identity logical properties;
- reflexivity safeguards;
- symmetry safeguards;
- transitivity safeguards;
- probabilistic-chain safeguards;
- identity laundering safeguard;
- distinctness safeguards;
- part/whole identity boundary;
- cross-type identity safeguard;
- representation-of boundary;
- Source-asserted vs system-resolved identity;
- identity inconsistency;
- later-resolution safeguard;
- historical transfer safeguard;
- responsibility/ownership boundary;
- provenance preservation;
- Entity Explosion protection.

Контрольный аудит:

    Critical defects: 0
    Major defects: 0
    Требуется архитектурная перестройка: NO
    Новые обязательные Core-сущности: 0
    Межстандартная совместимость: PASS
    Тест на разрастание сущностей: PASS

`014-IDENTITY v0.1` считается действующим стандартом проекта.

Финальный hardening-аудит: PASS.
Выбранные adversarial barrier checks: PASS.
Критических архитектурных противоречий: 0.
Новых обязательных Core Entities: 0.
Невнесённых обязательных изменений: 0.
Статус: CLOSED.

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
