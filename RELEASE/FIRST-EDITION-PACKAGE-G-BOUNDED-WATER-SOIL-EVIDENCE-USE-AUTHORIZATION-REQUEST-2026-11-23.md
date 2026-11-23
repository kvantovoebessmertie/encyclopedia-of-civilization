# First Edition — Package G: bounded versioned-Evidence-Use authorization packet

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Prepared against HEAD: `21545ac9476b8d0888c6c665796b5e27969c055d`  
PR #22: OPEN / DRAFT / NOT MERGED  
Status: REQUEST FOR OWNER AUTHORIZATION; no canonical changes performed.

## 1. Requested decision

Authorize only the versioned metadata/evidence-locator operations listed below. This request does not ask to rewrite Claims, approve publication, remove HOLD, create a production allowlist, adopt a project licence, or authorize release.

The operations are intentionally narrow:
- four existing Emergency Water Evidence Use records, each v1 → v2, adding an exact locator in the already-supported `content.material.locator` field;
- one existing Soil Basics Source record, v1 → v2, changing its external URI from a broad NRCS soils landing page to the exact NRCS “What is Soil?” page;
- one existing Soil Basics Evidence Use record, v1 → v2, pointing to Source@2 and adding an exact locator.

No new record IDs are requested. Record counts and coverage denominators therefore remain unchanged.

## 2. Schema basis

The current canonical record schema is `IMPLEMENTATION/005-RECORD-SCHEMA.json`. The `evidence_use` profile requires `claim_ref`, `source_ref`, `material` and `evidence_role`. The `material` object supports a non-empty `locator` and optional `description`; it does not require an invented field or extension.

The Source profile supports `external_ref.uri`. The proposed URI change is versioned and must not overwrite Source@1.

## 3. Exact requested operations

### 3.1 Emergency Water — four Evidence Use version bumps

All existing Claim references, Source references, evidence roles and provenance method remain unchanged. Only the record version and material locator/description are updated.

| Record | Current → proposed | Exact source locator |
|---|---|---|
| EU-WATER-BOILING-EFFECTIVE | @1 → @2 | CDC “How to Make Water Safe in an Emergency” → “Boil” / “Steps for boiling water” |
| EU-WATER-BOILING-TIME | @1 → @2 | CDC same page → “Steps for boiling water”, step 1; CDC-specific 1 minute / above 6,500 feet 3 minutes |
| EU-WATER-CHEMICAL-LIMIT | @1 → @2 | CDC same page → “Water with fuel or toxic chemicals in it” |
| EU-WATER-INDEPENDENT-CORROBORATION | @1 → @2 | EPA “Emergency Disinfection of Drinking Water” → opening warning and first boiling instruction |

Exact source URLs:
- CDC: https://www.cdc.gov/water-emergency/about/
- EPA: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

Required preserved boundaries:
- The CDC-specific 6,500-foot threshold remains attached only to the CDC Claim/EU.
- EPA's page uses a different 5,000-foot threshold. Do not copy that value into the CDC-specific Claim.
- The chemical/radioactive warning remains adjacent to the boiling recommendation in any reader presentation.
- These four updates do not authorize new bleach, iodine, chlorine-dioxide, filtration or chemical-dosing instructions.

### 3.2 Soil Basics — one Source version bump and one Evidence Use version bump

**Requested Source operation**

- `SRC-SOIL_BASICS@1 → @2`
- Preserve source identity as USDA NRCS, representation, availability and preservation note.
- Update only `content.external_ref.uri` to:
  `https://www.nrcs.usda.gov/resources/education-and-teaching-materials/what-is-soil`

Reason: the existing Source@1 URI points to a broad NRCS soils landing page, while the reviewed direct definitional and functional passages are on the “What is Soil?” page. A versioned URI correction is necessary before the EU locator can truthfully point to that page.

**Requested Evidence Use operation**

- `EU-SOIL_BASICS-B@1 → @2`
- Update `source_ref` and `provenance.created_from` to `SRC-SOIL_BASICS@2`.
- Add the locator: “What is Soil?” opening functional summary and the Soil Science Society of America definition immediately below it.
- Preserve Claim B@1 and the existing `supports` role.

Claim B wording: “Свойства почвы влияют на движение воды, доступность питательных веществ и условия роста растений.”

The opening functional summary supports water-flow regulation and nutrient cycling; the SSSA definition describes soil as a natural medium for the growth of land plants. The EU must not imply that all soils have identical water or nutrient behaviour.

**No Source/EU update is requested for Soil Claims A or C in this packet.**
- Claim A includes living organisms as components; the NRCS Soil Taxonomy definition distinguishes solids, liquid and gases, while organism detail requires an additional exact source and careful wording. A separate source/dependency proposal is needed.
- Claim C's “place and depth” wording requires a narrower editorial interpretation and additional exact support. An EU-only locator patch must not be used to make an overbroad statement appear supported.

## 4. Explicit exclusions from this authorization request

The following remain outside the requested scope:
- all Shelter Basics records and wording;
- Soil Claims A and C, and all their Evidence Use/Source records;
- any Claim wording changes, including changes to high-consequence guidance;
- Context, Scope, Relation, Assessment, Inference or Decision changes;
- rights/licence determinations, asset reuse or legal permissions;
- any INCLUDE/HOLD/EXCLUDE disposition or public selection manifest;
- production reader, deployment, public preview or public release.

## 5. Validation required if and only if authorization is granted

Before applying any write:
1. Re-fetch the exact current branch head and all six affected files; abort if any blob SHA has changed from the reviewed baseline.
2. Construct complete versioned records without changing unrelated fields.
3. Validate all records against `IMPLEMENTATION/005-RECORD-SCHEMA.json`.
4. Run exact-version dependency/reference tests for each affected slice.
5. Verify the water chemical/radioactive warning remains adjacent to boiling guidance in the rendered reader.
6. Verify the CDC altitude value and EPA altitude value remain distinct and correctly attributed.
7. Verify the Soil B EU targets Claim B@1 and Source@2 exactly.
8. Re-fetch every changed record and compare intended fields against the authorization.
9. Run all required PR workflows on the resulting exact HEAD; report only actual completed conclusions.

If authorization is not granted, no canonical write is performed and all current versions/dispositions remain unchanged.

## 6. Baseline and record-level identity

Emergency Water exact record IDs, versions and blob SHAs were re-fetched at HEAD `9711fa0ea8e0275c71f358e986f0713ee35658df` and are recorded in Package F. Soil Basics records were also re-fetched at that HEAD; the Source@1 blob SHA was `e09d755f7590476c0ebe4ac4dec40d562e1c2e5b`. The five requested EU baselines are listed in Package F's current-head audit inventory.

The next implementation pass must re-fetch again at the actual write head `21545ac9476b8d0888c6c665796b5e27969c055d`; the earlier SHAs are an audit baseline, not a substitute for the required write-time concurrency check.

## 7. Release status

All affected Claims remain HOLD. This packet does not change the zero-INCLUDE state, the production manifest remains absent, R-01–R-10 remain owner decisions, and the first edition is not approved for publication. PR #22 remains OPEN / DRAFT / NOT MERGED. `main` is not modified.
