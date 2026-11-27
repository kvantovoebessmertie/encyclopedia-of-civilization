# Owner Authorization Request — Groundwater / Soil Microbiology Relation Evidence

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Inspection HEAD: `251cccbdf3f39c62591c2f0856ccd4c04c622dd0`  
Status: **REQUEST ONLY — NO CANONICAL CHANGE AUTHORIZED OR MADE**

## 1. Decision requested

Approve or reject the following bounded, relation-level evidence addition for `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@3`.

The proposal does not alter either endpoint Claim or its Evidence Use. It adds one source that directly documents microbial transport from soil through the unsaturated subsurface into groundwater, while retaining the Relation as contextual navigation only.

## 2. Exact current records verified at the inspection HEAD

- `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@3`
  - Participants: `CLM-GROUNDWATER_BASICS-A@1` and `CLM-SOIL_MICROBIOLOGY_BASICS-A@1`.
  - Existing provenance Sources: `SRC-GROUNDWATER_BASICS@1`, `SRC-SOIL_MICROBIOLOGY_BASICS@1`, `SRC-USGS-GROUNDWATER-SOIL-MICROBIAL-INTERACTIONS@1`.
  - Frame: `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2`.
- `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2`
  - Exact `target_ref` → Relation @3.
  - Condition: the connection is represented only within the explicitly stated Relation type and does not replace the underlying Claim, Scope or Evidence Use.
- Endpoint statements:
  - Groundwater Claim A@1: groundwater occurs in saturated pores and fractures of soils and rocks.
  - Soil Microbiology Claim A@1: soil contains a complex community of microorganisms and other organisms.

Both endpoint Claims and their existing Evidence Use records remain unchanged under this proposal.

## 3. Direct evidence found

**Proposed new Source identity**

Francesco Bagordo et al. (2024), “Factors Influencing Microbial Contamination of Groundwater: A Systematic Review of Field-Scale Studies,” *Microorganisms*, 12(5), 913. DOI: 10.3390/microorganisms12050913.

Official publisher page:  
https://www.mdpi.com/2076-2607/12/5/913

Open full text:  
https://pmc.ncbi.nlm.nih.gov/articles/PMC11124417/

Exact useful locators:
- §1, Introduction — describes microorganisms released onto soil being transported by rainfall/infiltration through subsoil and the unsaturated zone into groundwater.
- §3.3.3, Hydraulic Properties — discusses soil moisture and hydraulic conditions affecting microbial mobilization and transport through the unsaturated zone.
- §3.3.4, Geological and Hydrogeological Settings — discusses the role of soil/subsoil, vadose-zone thickness, macropores, fractures and aquifer setting.
- §4, Discussion and Conclusions — summarizes the pathway from surface soil through the unsaturated zone to the saturated groundwater zone and the factors affecting transport and survival.

The review synthesizes 24 field-scale studies. It directly supports a limited soil–subsurface–groundwater microbial transport connection. It does **not** establish that all soil microorganisms move into groundwater, that groundwater microbiomes are identical to soil microbiomes, or that transport occurs under all environmental conditions.

**Rights boundary**

The article's publication page and full text state © 2024 by the authors and identify the work as open access under the Creative Commons Attribution (CC BY) licence. The proposed record should identify the exact work, DOI, publisher URI and CC BY 4.0 notice, require attribution and indication of changes where applicable, and exclude third-party material not covered by the article licence. This is a source-specific rights statement, not a project-wide licence decision.

The existing USGS source remains a distinct source and is not replaced. It supports microbial processes affecting groundwater chemistry and aquifer properties; the proposed 2024 review adds the soil-to-groundwater transport pathway.

## 4. Proposed bounded canonical operations — approval required

If approved, authorize exactly these three canonical record operations:

1. Create `SRC-GROUNDWATER-SOIL-MICROBIAL-TRANSPORT-2024@1` in `CONTENT/vertical-slices/cross-slice-linkage/records/`, identifying the 2024 systematic review, DOI, exact official URI, pinpoint locators and source-specific CC BY 4.0 / third-party-material boundary.
2. Version `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@3 → @4`:
   - add only the new Source @1 to `provenance.created_from`;
   - update `frame_ref` to Context @3;
   - preserve participant identities, versions and order; `relation_type`; roles; direction; all existing provenance references and method; all other fields and statuses.
3. Version `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@2 → @3`:
   - add only the new Source @1 to `provenance.created_from`;
   - update `target_ref` to Relation @4;
   - preserve condition, epistemic status, existing provenance references and method; all other fields and statuses.

The exact reciprocal result would be Relation @4 → Context @3 and Context @3 → Relation @4.

If approved, derived bookkeeping may be updated only after exact re-fetch and reconciliation:
- coverage manifest: total records +1 and Source count +1; all other counts unchanged;
- Part II exact-version master: add the new Source @1 as one dependency row, preserving the candidate-key denominator and all HOLD decisions;
- relation-dependency inventory / implementation report: record Relation @4 and Context @3 as current exact versions.

No count or register change is made by this request.

## 5. Explicit exclusions

This request does not authorize:
- any change to either endpoint Claim, any endpoint Evidence Use, or the existing Groundwater / Soil Microbiology Sources;
- any new Claim, Evidence Use, Context, Scope or Relation identity;
- any change to Relation semantics, participant pair, role, direction or condition;
- a causal, quantitative, universal or safety claim about groundwater contamination;
- any publication-status or completion-status change;
- candidate membership changes, INCLUDE/EXCLUDE, allowlists, release approval, publication, deployment, merge or changes to `main`.

The Relation and both vertical slices remain **HOLD**. The proposed source addition would not itself clear independent scientific/editorial review, project distribution rights, Human View or any first-edition release gate.

## 6. Validation required if approved

- Re-fetch all three current records and confirm the exact starting versions before writing.
- Verify the new Source identity, DOI, URI, licence notice and locators.
- Verify both reciprocal Relation/Context references and preservation of every non-authorized field.
- Verify that no Claim or Evidence Use changed.
- Run the relevant Relation/Context reference tests, content preflight, Reference Tests, Release Conformance Gate, Offline Edition and browser checks on one immutable final PR HEAD.
- Keep all affected records and slices HOLD regardless of CI outcome.

## 7. Owner response

A response must explicitly approve or reject the three-record scope in §4. Silence, a general instruction to continue WP1, or a successful CI run does not authorize these canonical changes.
