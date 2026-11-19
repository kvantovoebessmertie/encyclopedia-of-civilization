# R9 Evidence-Depth Remediation Addendum — 2026-11-19

Date: 2026-11-19  
Authorization: `R9-EVIDENCE-DEPTH-REMEDIATION-001`  
Audit: `RELEASE/R9-FIRST-EDITION-EVIDENCE-DEPTH-FOLLOWUP-2026-11-19.md`  
Register: `RELEASE/FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Scope

Three priority R9 slices were remediated under the bounded authorization:

1. `history-of-medicine-basics`
2. `history-of-engineering-basics`
3. `library-science-basics`

This work follows the R9 evidence-depth follow-up and does not repeat the prior structural/Claim audit. It uses factual paraphrase and pinpoint citation only. No source prose, tables, photographs, figures, diagrams or page layouts were copied.

## Exact record changes

| Slice | Source | Claims | Evidence Use | Context | Scope | Total |
|---|---:|---:|---:|---:|---:|---:|
| history-of-medicine-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| history-of-engineering-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| library-science-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| **Total** | **3** | **9** | **9** | **3** | **3** | **27** |

All 27 records were versioned v1→v2. Publication and completion states were preserved.

### history-of-medicine-basics

- Source v2 identifies the National Library of Medicine, *Collection Development Guidelines*, “History of Medicine” (updated 2022-09-30), with Definition, Discussion and Scope and emphasis locators.
- Claims A and B were versioned without wording changes to align provenance with Source v2.
- Claim C was narrowed from a general statement about primary and secondary sources to the NLM-supported proposition that historical study uses interpretive, analytical and biographical secondary literature.
- Evidence Use A–C now point to exact NLM sections and Claim/Source v2.
- Context and Scope now explicitly exclude clinical recommendations and medical guidance.

### history-of-engineering-basics

- Source v2 identifies the Smithsonian Institution, “Explore Technology & Innovation”, with exact featured-story and collection locators.
- Claims A–C were versioned and narrowed to documented objects and interpretive stories actually presented by the Smithsonian page:
  - technologies, inventions, artifacts and collections as historical material;
  - illustrative engineering/technology examples across roads, aviation, computing and communications;
  - Smithsonian presentation through both object collections and interpretive stories.
- Evidence Use A–C identify the relevant introduction, featured stories and “From the Collections” entries.
- Context and Scope now state that the page is a specific museum collection/story selection, not a complete or globally representative history and not evidence of causation.

### library-science-basics

- Source v2 identifies IFLA and UNESCO, *IFLA-UNESCO Public Library Manifesto 2022*, with page and section locators.
- Claims A–C were narrowed explicitly to public libraries:
  - equal access to information, knowledge, collections and services;
  - missions involving education, lifelong learning, literacy, scientific and community information;
  - preservation/access for local and Indigenous knowledge, heritage, oral tradition and digital materials.
- Evidence Use A–C cite “The Public Library” and “Missions of the Public Library”, pp. 1–3.
- Context and Scope clarify that the Manifesto is normative/advocacy guidance, not empirical proof of service effectiveness or a complete description of all library types.

## Rights and attribution boundary

- NLM: use is limited to independent factual paraphrase and citation; no NLM images, collection objects or third-party material are reproduced. Item-level rights and project distribution compatibility remain open.
- Smithsonian: the page contains links and images for individual objects/stories; no photographs, object images, expressive text or page design are copied. The rights status of the exact linked content and project-level reuse remains open.
- IFLA/UNESCO: the Manifesto is cited by title, organization, edition and page/section. No text, poster, image or layout is reproduced. Exact item-level reuse terms and project-licence compatibility remain open.
- Public accessibility is not treated as permission to reproduce source expression. This addendum does not grant rights clearance.

## Validation and disposition

- All 27 updated records preserve `publication_status` and `completion_status`.
- Claims and Evidence Use records point to current Source/Claim versions; Context and Scope target current Claim A v2.
- The changes are limited to the three authorized slices and their READMEs.
- All three slices remain **HOLD**.
- No INCLUDE/EXCLUDE decision or first-edition allowlist change was made.
- No main-branch change, merge, deployment, publication or release action was performed.

## Remaining work

1. Complete item-level rights review and project-owner licence/distribution decisions.
2. Obtain independent editorial review and Human View of the rendered reader presentation.
3. Continue R9 source-depth remediation in the remaining priority slices: hydraulic engineering, cultural heritage, archival science and other slices identified in the R9 follow-up.
4. Reconcile exact-version candidate register entries to v2 and rerun exact-head Reference Tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
5. Keep all three slices HOLD until every applicable gate is closed.


## Cross-slice relation reference alignment

The exact-head preflight after the three slice remediations identified four stale references in two existing cross-slice Relations. Under the explicit two-record extension to `R9-EVIDENCE-DEPTH-REMEDIATION-001`, the following relations were versioned v1→v2:

- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION`: updated only the Library Science Source and Claim A references to v2.
- `REL-CROSS-MATH-ENGINEERING-HISTORY`: updated only the History of Engineering Source and Claim A references to v2.

Both relation types, participant identities and order, roles, undirected direction, the other participants/source references, and `CTX-CROSS-SLICE-LINKAGE@1` frame references were preserved. These remain contextual links only; they do not establish evidence or causality. This adds two relation records to the 27 slice records corrected above; it does not change the 93-record R9 vertical-slice inventory or any slice decision.


## Next bounded R9 package — hydraulic engineering

Under the separate `R9-HYDRAULIC-ENGINEERING-REMEDIATION-001` authorization, `hydraulic-engineering-basics` was updated with a deliberate two-source profile:

- HEC-RAS Hydraulic Reference Manual v6.5 as `SRC-HYDRAULIC_ENGINEERING@2`.
- HEC-HMS Application Guide as the additional `SRC-HYDRAULIC_ENGINEERING-HMS@1`.
- Claims A/C and Evidence Use A/C reference HEC-HMS; Claim B and Evidence Use B reference HEC-RAS.
- All three Claims, all three Evidence Use records, Context and Scope are v2. The new Source adds one canonical record; the slice now contains ten records.
- No design equations, flood forecasting, dam/levee operations or site-specific engineering instructions were added. Rights remain unresolved; slice HOLD.

The ten-slice R9 inventory is now 94 records, not 93, because the hydraulic slice has two distinct Source branches. No record was removed to preserve the historical target count.
