# R7 Comparative Civilizations Basics — Bounded Diff Packet

Date: 2026-11-19
Target branch: `mvp-public-contribution-design-2026-10-11`
Inspection HEAD: `820125dc1b470b79f2d49eb3bee2be9af2383ef0`
Authorization: `REMAINING-R7-SOURCE-REMEDIATION-001` in `RELEASE/EDITORIAL-CORRECTION.json`
Status: **WITHIN EXISTING BOUNDED AUTHORIZATION — IMPLEMENTATION SPECIFICATION; NO CANONICAL JSON CHANGED**

## 1. Authorization and schema resolution

This packet covers only `comparative-civilizations-basics`, one of the four explicitly authorized slices. The authorization allows the existing Source, Claims A–C, Evidence Use A–C, Context and Scope to move from v1 to v2, with Claim statements and `claim_type` preserved. It further permits only a supplementary historical-method source reference in EU-C provenance for chronology versus causation.

The apparent schema blocker is resolved without changing the schema:
- `IMPLEMENTATION/005-RECORD-SCHEMA.json` defines `provenance.external_sources` as an array of `external_ref` objects.
- Each `external_ref` supports `uri` and `locator`.
- `record_type: evidence_use` still has exactly one canonical `content.source_ref`; this packet does not add a second canonical Source ID or alter the evidence-use profile.
- For EU-C only, the supplementary Singapore Ministry of Education source is recorded in `provenance.external_sources`, while the primary AHA source remains in `provenance.created_from` and `content.source_ref`.

This follows the authorization's exact instruction (“supplementary historical-method source reference in EU-C provenance”) and the existing schema. No validator or schema changes are required.

## 2. Exact nine-record inventory

All nine records were re-fetched at the inspection HEAD and are currently v1.

| Record | Current version | Proposed version | Current blob SHA |
|---|---:|---:|---|
| `SRC-COMPARATIVE_CIVILIZATIONS_BASICS` | 1 | 2 | `e2d2e0b55ff9155473ff56476fc508aeb6306d58` |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A` | 1 | 2 | `206579095d29f36db31cfd6e6590b15fb6368223` |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-B` | 1 | 2 | `93bef3d54badd5513192d26d5026cb0eb778970c` |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-C` | 1 | 2 | `8d5b601052a9cf2d57f98781cf5f326a575bc6b3` |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-A` | 1 | 2 | `a45befbe3bbcc60bf22d1fe2371790bfb650e32c` |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-B` | 1 | 2 | `e65591df3da968f90694bb06b78b3736b48743f9` |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-C` | 1 | 2 | `cf68bc5a0d19e9cec3cade4a5357f5c542ccb905` |
| `CTX-COMPARATIVE_CIVILIZATIONS_BASICS` | 1 | 2 | `ea4aea6d11cc45e4575cc71e3251468de80fa7b4` |
| `SCP-COMPARATIVE_CIVILIZATIONS_BASICS` | 1 | 2 | `8fa80b7b731000e3f19a604d5acb1620f9e3131a` |

If any blob SHA or version differs at implementation time, stop and regenerate this packet from the new frozen HEAD.

## 3. Proposed primary Source v2

**ID/version:** `SRC-COMPARATIVE_CIVILIZATIONS_BASICS@2`

**Source identity:**

> David Smith, “Introduction to Doing World History,” American Historical Association (AHA), AHA Resource: For the Classroom, published 4 October 1998.

**URI:**

`https://www.historians.org/resource/introduction-to-doing-world-history/`

**Locator:**
- Opening discussion: world history as cross-cultural study and comparison of societies in their historical context.
- Paragraph beginning “Most fundamentally, doing world history involves the study of cross cultural events or phenomena.”
- Paragraph beginning “They also stress connections between civilizations and how they influenced one another.”
- “Doing World History” list: Big Picture, Diffusion, Syncretism, Comparison and Common Phenomena.

**Support boundary:** This is a 1998 teaching-method resource, not a comprehensive theory of civilization, a current historiographical consensus statement, or evidence that all societies follow a particular universal sequence. It directly supports cross-cultural comparison, historical context, interaction, diffusion and syncretism. Its educational framing and date must remain visible.

## 4. Supplementary historical-method source for Claim C

**No new canonical Source record is created.**

Use the existing schema field `provenance.external_sources` on `EU-COMPARATIVE_CIVILIZATIONS_BASICS@2`:

```json
"external_sources": [
  {
    "uri": "https://www.moe.gov.sg/-/media/files/secondary/syllabuses/humanities/archive---2021-history-lower-secondary-syllabus.pdf",
    "locator": "2021 Lower Secondary History Teaching and Learning Syllabus, Table 1.1 “Historical Concepts”, p. 5: “Chronology” and “Cause and Effect (Causation)”."
  }
]
```

**Why this locator is direct:** the official Singapore Ministry of Education syllabus defines chronology as listing dates/events in the order they occurred and defines causation as examining reasons why and how events happened. These are distinct analytical questions: sequence is not itself an explanation of cause.

**Support boundary:** The syllabus is a lower-secondary educational framework from Singapore. It is used only as a clear, official pedagogical distinction between chronological order and causal explanation, not as a universal legal/academic standard or proof that any particular historical causal explanation is correct.

## 5. Claim-by-claim mapping

All Claim statements and `claim_type` values remain unchanged. Each Claim moves v1→v2 only to align `provenance.created_from` with `SRC-COMPARATIVE_CIVILIZATIONS_BASICS@2`.

### Claim A — comparison in historical/cultural context

Current statement retained:

> Сравнительное изучение цивилизаций сопоставляет общества в их историческом и культурном контексте, не предполагая единой универсальной траектории развития.

Primary EU v2 locator:
- AHA “Introduction to Doing World History,” opening discussion of cross-cultural study and comparisons between societies.
- Paragraph beginning “Most fundamentally…” describing cross-cultural events/phenomena, historical development and comparison of patterns where interaction is limited.

Support boundary: directly supports cross-cultural comparison and contextualized comparison of differing patterns. The final clause (“not assuming a single universal trajectory”) is a methodological limit consistent with the source's comparison of differing patterns, but is not a direct quotation or a universal law asserted by AHA. Retain it as a non-teleological scope constraint, not as a separate empirical fact.

### Claim B — contacts, exchange and mutual influence

Current statement retained:

> История цивилизаций требует учитывать контакты, обмены и взаимное влияние между различными обществами.

Primary EU v2 locator:
- AHA paragraph beginning “They also stress connections between civilizations and how they influenced one another.”
- Discussion of diffusion and syncretism in the “Doing World History” methods list.

Support boundary: directly supports the importance of inter-societal connections, diffusion and mutual influence. It does not imply that every society was continuously connected to every other society or that influence was equal in all directions.

### Claim C — sequence versus causation

Current statement retained:

> Историческое сравнение должно различать наблюдаемую последовательность событий и доказанную причинность.

Primary EU v2 locator:
- AHA resource: “Big Picture” method, which uses timelines of important events and an accompanying explanation of their significance. This supports chronological organization but does not, by itself, prove causal relationships.

Supplementary `provenance.external_sources` locator:
- Singapore MOE 2021 Lower Secondary History Syllabus, Table 1.1, p. 5: “Chronology” and “Cause and Effect (Causation)”.

Support boundary: the MOE source distinguishes temporal order from causal explanation. “Доказанная причинность” should be understood as requiring evidence and an argument beyond temporal succession; neither source establishes a particular causal claim about any historical event.

## 6. Exact per-record field changes

| Record group | Permitted field changes | Preserve |
|---|---|---|
| Source v1→v2 | Replace generic identity with David Smith/AHA title, resource type and date; set external URI to AHA page | Record ID/type, statuses; no copied source prose |
| Claims A–C v1→v2 | Update only `provenance.created_from` to Source v2 | Exact Claim statement and `claim_type`; all other semantics |
| EU A/B v1→v2 | Update `provenance.created_from`, `content.source_ref` and `content.claim_ref` to exact v2 references; add claim-specific locator and bounded description | `evidence_role: supports`; no extra source reference |
| EU C v1→v2 | Same v2 reference alignment; add AHA locator and bounded description; add the one MOE external reference under `provenance.external_sources` | Single canonical `content.source_ref` to AHA; no new canonical Source ID |
| Context v1→v2 | Update `provenance.created_from` to Source v2; update `target_ref` to Claim A v2; clarify educational/methodological limits | Context's editorial role; no new Claim/Source IDs |
| Scope v1→v2 | Update `provenance.created_from` to Source v2; update `target_ref` to Claim A v2; state scope and exclusions | No allowlist or publication-state change |

### Proposed Context v2 text

> Срез представляет сравнительное изучение цивилизаций как ограниченный историко-аналитический подход: общества сопоставляются с учётом времени, места, культурных и институциональных условий, контактов и возможных различий траекторий. Материал AHA 1998 года используется как образовательное введение в cross-cultural/world-history methods, включая сравнение, diffusion и syncretism. Для Claim C отдельный методологический ориентир MOE 2021 различает хронологическую последовательность событий и анализ причин/следствий. Эти источники не устанавливают универсальную модель цивилизации и не доказывают причинность конкретного исторического процесса.

### Proposed Scope v2 text

> Срез ограничен вводными понятиями сравнительного изучения цивилизаций, межобщественных контактов и методологического различения хронологии и причинного объяснения. Он не является исчерпывающей историографией, универсальной стадийной теорией цивилизаций или доказательством конкретных причин исторических событий. AHA resource (1998) используется как образовательное описание world-history methods; MOE syllabus (2021) — только как методологический пример различия chronology и causation. Выводы по отдельным обществам, периодам и причинным связям требуют самостоятельных первичных и научных источников.

## 7. Rights and attribution boundary

- The AHA page is publicly accessible, but the page does not establish an open reuse licence. Use only source identity, bibliographic locator metadata and independently worded factual paraphrase. Do not copy or translate its prose, teaching materials, tables or graphics.
- The MOE syllabus carries a reproduction notice limiting reproduction to personal or non-commercial educational use and reserving other rights. This packet does not reproduce any syllabus text beyond the source title/concept labels needed to identify the locator; do not copy/translate its definitions, tables, layout or graphics into the corpus.
- Item-level rights review and the Encyclopedia's distribution/content-licensing model remain open. No blanket rights clearance is inferred.
- Keep this slice HOLD pending rights review, independent historical/editorial review and Human View.

## 8. Explicit non-actions

This packet does not authorize or perform:
- changes to Claim statements or `claim_type`;
- creation of a second canonical Source ID;
- changes to `content.source_ref` to a second source or changes to the evidence-use profile;
- any schema, validator, reference implementation or release-gate change;
- publication/completion status changes, allowlist changes or INCLUDE/EXCLUDE decisions;
- copying, translation or reproduction of source expression, teaching handouts, tables, graphics or page layouts;
- deployment, publication or merge to `main`.

## 9. Validation contract after implementation

1. Freeze a new exact PR HEAD and re-fetch all nine records; verify every current SHA/version in §2. Abort and regenerate if any differs.
2. Apply Source v2; then Claims A–C provenance-only increments; then EU A–C reference/locator updates; then Context and Scope alignment.
3. On EU-C, validate `provenance.external_sources` as a list of `external_ref` objects containing non-empty `uri` and `locator`; preserve the single canonical `content.source_ref` to AHA Source v2.
4. Re-fetch all nine records and validate the three Claim→EU→Source canonical chains plus EU-C's supplementary external source metadata.
5. Confirm all three Claim statements and `claim_type` values are byte-for-byte semantically unchanged.
6. Run affected-slice schema/graph/reference tests and then exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one immutable final HEAD.
7. Preserve HOLD until rights review, independent editorial review and Human View are closed.

**Status:** existing bounded authorization covers this packet. The schema-valid supplementary reference is specified; no canonical record has been edited.
