# First Edition — Cross-Slice Relation Semantic Review Batch 1

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `bd1ab1e42310daef9aab0755d5082793f54be21d`  
Current PR head: `6368903f471b85d6e22e3962f58074bb95368eb4` (the intervening commit changed only the Batch 9 report; canonical records were unchanged)  
Status: **3/63 RELATIONS SEMANTICALLY REVIEWED; 6/6 PARTICIPANT CLAIMS AND 6/6 SOURCE REFERENCES MATCH EXACT VERSIONS; ALL LINKS CONTEXTUAL ONLY**

## 1. Scope

This bounded review covers three already-inventoried Relations whose endpoint records were recently versioned under existing R9 authorizations:

- `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2`
- `REL-CROSS-MATH-ENGINEERING-HISTORY@3`
- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3`

Each Relation, both participant Claims, both provenance Sources and the shared frame Context were fetched from canonical JSON. The review checks exact record identity/version/type and whether the declared relation type is a defensible navigation-level connection between the current Claim statements.

## 2. Exact reference checks

| Relation | Relation version/type | Participant Claim refs | Source refs | Frame |
|---|---|---|---|---|
| cartography ↔ settlement geography | `@2`, `shared_spatial_representation_context` | `CLM-CARTOGRAPHY-A@2`; `CLM-SETTLEMENT_GEOGRAPHY-A@1` | `SRC-CARTOGRAPHY@2`; `SRC-SETTLEMENT_GEOGRAPHY@1` | `CTX-CROSS-SLICE-LINKAGE@1` |
| history of mathematics ↔ history of engineering | `@3`, `shared_history_of_technical_knowledge_context` | `CLM-HISTORY_OF_MATHEMATICS-A@2`; `CLM-HISTORY_OF_ENGINEERING-A@2` | `SRC-HISTORY_OF_MATHEMATICS@2`; `SRC-HISTORY_OF_ENGINEERING@2` | `CTX-CROSS-SLICE-LINKAGE@1` |
| library science ↔ archival science | `@3`, `shared_information_preservation_context` | `CLM-LIBRARY_SCIENCE-A@2`; `CLM-ARCHIVAL_SCIENCE-A@2` | `SRC-LIBRARY_SCIENCE@2`; `SRC-ARCHIVAL_SCIENCE@2` | `CTX-CROSS-SLICE-LINKAGE@1` |

All six participant Claim records and six corresponding Source records match their exact declared IDs, versions and types. All three Relations have two participants, matching two `linked_record` roles, undirected direction and the exact shared Context frame. The frame itself is a Context record whose stated rule limits Relations to explicitly described semantic context and says they do not replace Claim, Scope or Evidence Use.

## 3. Semantic assessment

### REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2 — ACCEPT AS CONTEXTUAL NAVIGATION

Cartography Claim A concerns creating and using maps to represent spatial information. Settlement Geography Claim A concerns classifying inhabited territories along an urban–rural continuum for international comparison. Both concern spatial representation/classification, so the relation is a defensible discovery path.

Boundary: the settlement classification can exist independently of a map. The relation must not imply that the cited USGS map products define UN-Habitat settlement categories, that cartography validates the classification, or that either Claim evidences the other.

### REL-CROSS-MATH-ENGINEERING-HISTORY@3 — ACCEPT AS CONTEXTUAL NAVIGATION

History of Mathematics Claim A concerns the historical development and transmission of mathematical ideas, methods and notation. History of Engineering Claim A concerns studying engineering history through documented technologies, inventions, artifacts and collections. Both are historical approaches to technical knowledge and material/intellectual practices.

Boundary: the link does not assert a specific causal dependency between a mathematical discovery and an engineering invention, nor establish a complete shared chronology.

### REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3 — WEAK / HOLD FOR RELEASE USE

Library Science Claim A concerns equal access to information, knowledge, collections and public-library services. Archival Science Claim A concerns appraisal, arrangement, description and preservation in archival processing. The broad information-preservation relationship is plausible at domain level, but the selected library endpoint Claim A is access-focused and does not itself state a preservation proposition.

The current Relation is structurally valid and its version references are correct, but its semantic label is broader than the direct overlap of the two selected Claims. Do not use this Relation as evidence or as a strong instructional dependency. A future improvement could be a separately authorized relation to a library-preservation Claim, if the intended relation semantics and candidate graph justify it. No participant was changed here.

## 4. Decisions and boundaries

- Two Relations are accepted as contextual navigation links with explicit non-causal boundaries.
- One Relation is structurally valid but semantically weak for release navigation and remains HOLD for release use.
- All three Relations remain outside the vertical-slice record denominator.
- No Relation, Claim, Source, Context or Scope canonical JSON was changed.
- No publication state, first-edition allowlist or INCLUDE/HOLD/EXCLUDE decision was changed.
- This batch closes semantic review for 3 of 63 Relations only; it does not close the remaining 60 Relations or the 97 non-candidate endpoint review.
