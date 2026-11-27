# Groundwater / Soil Microbiology — authorized implementation and exact-head CI

Date: 2026-11-21  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Implementation HEAD before this report: `990086c73e76069175f664c8d5665be89a58ad43`  
PR #22: OPEN / DRAFT / NOT MERGED

## Owner-authorized scope completed

Implemented only the bounded operations authorized for the Groundwater / Soil Microbiology cross-slice Relation:

1. Added `SRC-GROUNDWATER-SOIL-MICROBIAL-TRANSPORT-2024@1`, based on Bagordo et al. (2024), “Factors Influencing Microbial Contamination of Groundwater: A Systematic Review of Field-Scale Studies,” *Microorganisms* 12(5), 913, DOI `10.3390/microorganisms12050913`. The Source records the article identity, DOI, publisher/full-text/PDF locators and the article-level CC BY 4.0 boundary (third-party materials excluded).
2. Versioned `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@3 → @4`. Added only the authorized Source reference in `provenance.created_from` and aligned `frame_ref` to Context @3. Relation semantics, participants, roles, direction and all other fields were preserved.
3. Versioned `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2 → @3`. Added only the authorized Source provenance reference and aligned `target_ref` to Relation @4. Context meaning, epistemic status and all other fields were preserved.
4. Applied the separately authorized derived-artifact correction to `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json`: synchronized corpus record count from 4,750 to 4,751 and updated the two descriptive 4,750-record strings to 4,751-record. No other fields were changed.

The Source review supports bounded, conditional microbial transport and groundwater/soil interaction; it does not support universal transport, identical soil/aquifer microbiomes, or a claim that microbial activity guarantees potable water.

## Preserved controls

- The Relation, Context, Source and affected slices remain HOLD.
- No Claim or Evidence Use was changed.
- No INCLUDE/EXCLUDE decision, allowlist, release selection, publication, deployment or merge was made.
- PR #22 remains OPEN / DRAFT / NOT MERGED.
- `main` was not changed.

## Exact-head CI verification

All four required pull-request workflows completed successfully on the same immutable implementation HEAD `990086c73e76069175f664c8d5665be89a58ad43`:

| Workflow | Run ID | Result |
|---|---:|---|
| Reference implementation tests | 44841276253 | PASS |
| Release Conformance Gate | 44841276012 | PASS |
| Offline Edition | 44841276032 | PASS |
| MVP Contribution Form Browser Tests | 44841276278 | PASS |

The Release Gate job completed successfully, including Content preflight and the release-gate step. This is a technical CI result for the named workflows and exact HEAD only; it is not scientific/editorial approval, rights clearance for the whole project, Human View, owner release approval or authorization to publish.

## Next controlled work

Continue WP1 → WP2 → WP3 in the established order. For WP1, continue only the remaining explicitly authorized first-edition screening/dependency-closure work; do not repeat the Groundwater / Soil Microbiology implementation or its CI diagnosis. Keep unresolved semantic Relations and all affected records HOLD. WP2 owner decisions R-01–R-10 remain open. Before any later canonical/implementation commit is treated as conforming, re-run all four required workflows on one exact immutable HEAD. No merge, deployment, public allowlist or publication is authorized by this checkpoint.
