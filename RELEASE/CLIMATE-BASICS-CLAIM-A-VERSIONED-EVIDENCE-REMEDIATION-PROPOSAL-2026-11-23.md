# Climate Basics — Claim A Versioned Evidence Remediation Proposal

Date: 2026-11-23  
Target branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `00d503154bdd8ec33fdf5b1442c1f4b02921fb15`  
Status: PROPOSAL ONLY — NOT AUTHORIZED FOR CANONICAL WRITES

## 1. Purpose and strict boundary

This proposal prepares the smallest useful evidence repair for the existing Climate Basics Claim A subgraph. It does not change canonical JSON, Claim wording, record versions, publication/completion states, candidate registers, rights decisions, INCLUDE/HOLD/EXCLUDE dispositions, manifests, or release configuration.

The only intended future scope, if separately authorized, is a versioned Evidence Use and the minimum Source record(s) required to give the existing Claim a precise and inspectable locator. Context and Scope remain unchanged and continue to target Claim A v1. The whole Climate Basics slice is not certified by this subgraph review.

**Current disposition remains HOLD.** The word `published` in the canonical records is an existing record field; it is not a first-edition admission or release authorization.

## 2. Exact canonical baseline re-fetched

All five records below were re-fetched by immutable blob SHA and parsed as JSON during this review.

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| `CLM-CLIMATE_BASICS-A` | 1 | Claim | `83e86389e2c7e122ddce0b1e9d066c15147c9cec` |
| `EU-CLIMATE_BASICS-A` | 1 | Evidence Use | `7356d5b6c7c2c49f0fa119f60726135229d9033e` |
| `SRC-CLIMATE_BASICS` | 1 | Source | `a5bee4f54821f6e4163d917a9a85d9848118f065` |
| `CTX-CLIMATE_BASICS` | 1 | Context | `224e05a1b35b3bfc94545069685076b93e69fb2a` |
| `SCP-CLIMATE_BASICS` | 1 | Scope | `11e44bf4c54c433c5083a198bc213231e8e644a9` |

### Baseline content

- Claim v1: «Климат описывает долгосрочные характеристики и изменения погодных условий в системе Земли.»
- EU v1: `supports`; generic description only; points to Claim v1 and Source v1.
- Source v1: NASA — Climate Change; broad portal URI `https://science.nasa.gov/climate-change/`.
- Context v1: climate claims concern long timescales and must not be inferred from one short-term weather event; target is Claim A v1.
- Scope v1: basic educational climate slice, not a complete climate analysis of a specific territory; target is Claim A v1.

No target mismatch was found in Context or Scope. Their Claim-A-only target must be preserved.

## 3. Primary-source inspection

The following official NASA pages were inspected on 2026-11-23:

1. NASA Science, “What’s the difference between weather and climate?”  
   https://science.nasa.gov/climate-change/faq/whats-the-difference-between-weather-and-climate/  
   Relevant content: weather is described on short timescales; climate is described as longer-term averages, regional or global, and weather averaged over several decades. This is the cleanest direct support for the long-timescale distinction and the average-weather concept.

2. NASA Science, “What Is Climate Change?”  
   https://science.nasa.gov/climate-change/what-is-climate-change/  
   Relevant content: climate change is a long-term change in average weather patterns defining local, regional and global climates; NASA separately explains weather as short-term atmospheric conditions and climate as long-term regional/global averages, usually at least 30 years. The page also covers observed indicators, causes and effects, which are outside the narrow proposition being repaired.

These pages are suitable official explanatory references for the limited concepts above. The proposal uses only factual textual reference and does not require NASA imagery, logos, videos, visualizations, or other media. No blanket media licence or reuse permission is inferred.

## 4. Claim-to-source fit and limits

The Claim contains two linked ideas:

- climate concerns long-term characteristics of weather patterns;
- climate includes changes in those patterns within the Earth system.

NASA page 1 directly supports the long-term-average distinction. NASA page 2 directly supports long-term change in average weather patterns and the local/regional/global framing.

The phrase «в системе Земли» is broader than the narrow definitions quoted above. The NASA pages discuss Earth’s climate and multiple climate indicators, but this bounded review does not establish that every intended Earth-system component or interaction is covered by the current Claim. Do not silently broaden the evidence description to imply support for every Earth-system process.

No Claim rewrite is proposed here. If the owner/editor later concludes that the wording exceeds the selected source scope, that is a separate Claim-version decision requiring explicit authorization and its own review.

## 5. Minimal remediation design options

The current Evidence Use schema shown in EU v1 has a singular `source_ref`. Therefore, do not assume that two sources can be attached to one EU record without checking the governing schema and validator.

### Preferred minimal path — one primary source

- Create a new version of the existing Source identity, if the project’s source-versioning rules permit a changed locator under that identity, pointing to NASA “What Is Climate Change?”:
  `https://science.nasa.gov/climate-change/what-is-climate-change/`
- Create `EU-CLIMATE_BASICS-A@2` with an exact locator to the page’s definition of climate change and its “Weather vs. Climate” section.
- Preserve `claim_ref = CLM-CLIMATE_BASICS-A@1`, `evidence_role = supports`, and the existing evidence relationship.
- Keep the evidence description narrow: NASA defines climate change as a long-term change in average weather patterns defining local, regional and global climates; the cited section distinguishes short-term weather from long-term climate averages.
- Do not claim that the page independently validates every Earth-system component or every climate mechanism.

This path is preferred only if Source versioning permits the same source identity to receive a new version with a changed precise locator and if the existing record model permits a pinpoint field in EU v2. Verify both before implementation.

### Alternative — two explicit source records

If the source model requires one URI per Source and the editor wants both definition components independently cited:

- retain the existing Source v1 unchanged;
- propose two new NASA Source records, one for the weather/climate FAQ and one for “What Is Climate Change?”;
- propose an Evidence Use structure that conforms to the actual current schema and validator, rather than inventing a plural-source field;
- if one Claim requires two Evidence Use records or a Relation, inspect the Standard/Implementation requirements and dependency closure before seeking authorization.

This alternative is more explicit but has a larger dependency footprint. It must not be implemented by adding undocumented fields or by changing the Claim’s source provenance implicitly.

## 6. Proposed pinpoint descriptions (draft text, not canonical content)

For a single-source EU v2 using NASA “What Is Climate Change?”:

> NASA’s section “What Is Climate Change?” defines climate change as a long-term change in average weather patterns that characterize local, regional and global climates. Its “Weather vs. Climate” section distinguishes short-term atmospheric conditions from long-term averages (usually at least 30 years). This supports the Claim’s long-timescale and long-term-change concepts; it does not by itself establish every Earth-system component or mechanism implied by broader readings of the Claim.

For a two-source implementation, the FAQ would be used specifically for the long-term-average distinction, while “What Is Climate Change?” would be used for long-term change in average weather patterns. Exact field placement must follow the verified schema.

## 7. Required pre-write checks

Before any canonical write, an authorized implementation must:

1. Re-fetch the governing Source, Evidence Use, versioning and provenance standards at the intended implementation HEAD.
2. Confirm whether an existing Source identity may be versioned when its locator is narrowed, or whether a new Source ID is required.
3. Confirm the Evidence Use schema’s exact locator/pinpoint fields and whether multiple Source records are supported directly or only through multiple EU records.
4. Validate exact Claim/EU/Source references and all required provenance fields.
5. Check source availability and the exact section headings on the implementation date.
6. Preserve Context v1 and Scope v1 as Claim-A-only dependencies; do not retarget them to the slice or other Claims.
7. Run the repository’s relevant record schema, reference, coverage and release-conformance tests after any authorized change.
8. Keep every affected record HOLD. A successful technical check is not an editorial, rights, or release approval.

## 8. Authorization request — exact proposed scope

A separate owner authorization is required before canonical writes. The requested decision should select one of these bounded alternatives:

- **Option A:** permit only a versioned Source locator update/new Source version plus `EU-CLIMATE_BASICS-A@2`, with no Claim, Context, Scope, Relation, Decision, status, manifest, or allowlist changes; or
- **Option B:** permit only the minimum new Source record(s) and EU record(s) required by the verified schema, with the exact IDs and fields enumerated after schema inspection.

The authorization must identify the selected option, exact record IDs, permitted fields, and prohibited changes. This proposal itself grants no authority.

## 9. Explicitly not included

- No canonical JSON changed.
- No record version was created.
- No Claim wording or provenance was changed.
- No Context or Scope change.
- No Relation, Assessment, Inference, or Decision change.
- No candidate register, denominator, coverage manifest, or allowlist change.
- No INCLUDE decision; HOLD remains.
- No rights or licence conclusion beyond the limited factual-text reference assessment above.
- No public preview, hosting, distribution, merge, deployment, or main-branch update.

## 10. Review conclusion

Climate Basics Claim A is a credible low-consequence explanatory candidate for bounded remediation, but its current Evidence Use is too generic for a release-quality evidence trail. NASA’s two inspected official pages provide a precise path to repair the long-term-average and long-term-change components. The safest next step is a schema-checked, owner-authorized versioned EU/Source correction, with no Claim rewrite and no change to HOLD.

**Disposition: HOLD — remediation proposal prepared; canonical implementation not authorized.**
