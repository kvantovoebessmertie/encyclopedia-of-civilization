# M11 Initial Candidate Gap Audit — 2026-10-09

## Baseline and method

Read-only candidate verification was performed against M10 CLEAN HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`. The actual tree contains 483 registered vertical-slice directories and 4,831 record JSON files across 19 record types. The current coverage baseline records 617 Sources, 1,669 Evidence Use records, and 64 Relations.

The review inspected the candidate READMEs, all Claims, Sources, Evidence Use, Context and Scope records, and dedicated regression tests for `accessibility-basics`, `ergonomics-basics`, and `human-factors-basics`. The 58 dedicated cross-slice Relation records were also scanned for these candidate endpoints. This is a desk audit, not a live novice usability study or external peer review.

## Candidate findings

### 1. `accessibility-basics` — INCLUDE

- The slice has 9 records: 1 Source, 3 Claims, 3 Evidence Use, 1 Context and 1 Scope.
- The existing UN Convention on the Rights of Persons with Disabilities is a relevant international framing source for equality, participation and accessibility. Its identity and canonical URL are preserved.
- The three Claims are introductory and bounded, but Claim C says concrete accessibility requirements depend on the object, users and applicable jurisdiction. The substantive audit must ensure this is framed as an applicability boundary and not imply that the Convention itself specifies every local technical requirement.
- All three Evidence Use descriptions use the same generic formula and do not state the specific contribution or limitation of the source for each Claim.
- The README is English-only while the Claims and Context/Scope are Russian-facing; it offers no clear Russian introduction for an ordinary reader.
- The dedicated regression checks record counts, types and source/claim linkage only. It does not protect source-specific explanatory content, applicability boundaries or the human-facing introduction.
- Decision: include for claim-specific Evidence Use and Human View maturation. Do not add a second source or Relation merely to increase a count.

### 2. `ergonomics-basics` — INCLUDE

- The slice has 9 records: 1 NIOSH Source, 3 Claims, 3 Evidence Use, 1 Context and 1 Scope.
- The Claims concern ergonomic task design, physical risk factors and the risk-control/evaluation cycle. At the candidate-screen level, these are plausible introductory topics for the recorded NIOSH source; claim-by-claim support and limits remain for the substantive/evidence audit.
- All three Evidence Use descriptions are identical generic text and do not identify which source material supports the corresponding Claim or what it does not establish.
- The README is primarily English and does not provide a useful Russian-facing introduction or an explicit reader-oriented example.
- The dedicated regression checks shape and linkage but not claim-specific Evidence Use, content boundaries or Human View.
- Decision: include for claim-specific Evidence Use and Human View maturation. Preserve the source identity and URL; do not add sources by quota.

### 3. `human-factors-basics` — INCLUDE

- The slice has 9 records: 1 NASA Source, 3 Claims, 3 Evidence Use, 1 Context and 1 Scope.
- The Claims cover interaction between people and systems, effects of human perception/attention/decision limits, and whole-system design. Their exact source fit and limitations require claim-by-claim review.
- All three Evidence Use descriptions use generic “without extending beyond the material” wording and do not name the contribution or limitation for each Claim.
- The README is English-only while the Claims and Context/Scope are Russian-facing.
- The dedicated regression checks shape and linkage but does not assert explanatory or source-boundary quality.
- One existing cross-slice Relation, `REL-CROSS-MANUFACTURING-HUMAN-FACTORS`, links manufacturing-processes Claim B to human-factors Claim A. Preserve its record, participants, direction and frame. No new Relation is justified by the candidate scan.

## Prior-maturation and overlap check

The M3–M10 scope/audit records and relevant R-wave gap maps were reviewed. `accessibility-basics` was introduced in R18; `human-factors-basics` was introduced in R11, whose creation audit explicitly carried forward non-blocking debt on depth, independent-source triangulation and Human View. No separate later controlled maturation scope for these three slices was identified in the reviewed records. `ergonomics-basics` is conceptually adjacent but distinct: occupational task/risk design should not be conflated with disability rights/accessibility or the broader human-factors field.

The cluster is coherent because all three concern how people interact with environments or systems, while retaining distinct subject boundaries and sources. This does not imply that the three subjects are interchangeable.

## Confirmed candidate-level gap

The strongest confirmed common gap is not “one Source per slice”; it is that the existing Evidence Use descriptions and regressions do not preserve claim-specific explanation and limits. Human-facing READMEs also fail to provide a consistent Russian orientation. Claim/source fit and applicability boundaries will be assessed individually during the next audit; no unverified claim is pre-labelled false.

## Candidate decision

Proceed to a narrow M11 scope lock for the three existing slices only:

1. `accessibility-basics`
2. `ergonomics-basics`
3. `human-factors-basics`

No content correction is authorized by this audit alone. Next: lock the scope, perform claim-by-claim substantive/evidence review, Human View/adversarial review and Relation-delta review, then consolidate only confirmed findings in one M11 Unified Debt Map.
