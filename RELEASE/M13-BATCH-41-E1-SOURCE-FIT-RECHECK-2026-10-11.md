# M13 Batch 41 — E=1 Source-Fit Recheck

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **diagnostic recheck only; Batch 41 and M13 remain open**

## Purpose and limits

This pass re-opened the eight distinct E=1 Claim IDs listed in the post-score checkpoint plus the agricultural-engineering separator variants (nine scored rows total, eight Claim families/IDs if aliases are counted together). It inspected Claim, primary Evidence Use, Source records and any obvious additional Evidence Use records in the same slice, and checked relevant official/public source pages. It is not a final D/E/B rescore, a full semantic duplicate review, or authorization to modify content JSON.

The Batch 41 post-score checkpoint already records that the candidate eligibility/source-fit gate was not completed before the six score blocks were authored. Therefore every Batch 41 score remains provisional. This recheck does not retroactively satisfy that gate.

## Findings by scored row

| Score row | Claim | Confirmed source-fit finding | Disposition |
|---:|---|---|---|
| 5 | `CLM-ACOUSTICS_BASICS-B` | Claim: noise sources and levels differ by place, time and activity. The WHO Environmental Noise Guidelines source covers named exposure sources and health-oriented exposure guidance, but the stored EU is generic and gives no passage/indicator locator. The current source supports parts of the context, not a precise demonstration of the whole general statement. | Keep E=1 provisional; add a pinpoint section/table or narrow the claim during authorized correction. |
| 10 | `CLM-AGRICULTURAL_ENGINEERING_BASICS-A` | Claim says agricultural engineering applies engineering principles to agricultural production and resource management. The stored FAO land/soil/water page is relevant to resource management, but is not a direct definition of the engineering discipline. EU text is generic. The file name uses hyphens while the internal Claim and EU IDs use underscores; the EU reference matches the internal ID, so this is an identity/alias reconciliation issue rather than a broken pointer. | Keep provisional; use a direct agricultural-engineering definition or narrow the statement. Preserve all stored IDs. |
| 12 | `CLM-AGRICULTURAL_ENGINEERING_BASICS-C` | Claim lists crops, soils, water, climate, energy, labor and operating conditions. The same FAO land/water source directly covers only part of this factor list; EU text is generic. Filename/internal-ID separator variant is present, while the EU claim_ref matches the internal ID. | Keep provisional; map each factor to a source or narrow the list during authorized correction. |
| 23 | `CLM-ANALYTICAL_CHEMISTRY_BASICS-A` | The score rationale considered the NIST tutorial landing page indirect. However, a second stored EU record, `EU-ANALYTICAL-CHEMISTRY-IUPAC-CORROBORATION`, directly references this same Claim and IUPAC Gold Book term 08003. IUPAC defines analytical chemistry in terms of strategies, instruments and procedures to obtain information about the composition and nature of matter in space and time. That is materially closer to the Claim than the NIST landing page and was omitted from the row's rationale. | **Confirmed score-rationale reconciliation defect.** Re-adjudicate E using both EU records and the IUPAC definition; do not automatically set a replacement score without applying the locked rubric. |
| 28 | `CLM-ANATOMY_BASICS-C` | Claim: organ systems unite organs that interact to perform related functions. The primary NIGMS EU is generic and its stored legacy URL was not confirmed by this search pass. The additional OpenStax EU in this slice points to Claim A, not Claim C, so it must not be counted as evidence for C. | Keep E=1 provisional; locate a direct organ-system definition/source and update only in the authorized correction phase. |
| 46 | `CLM-ARCHIVAL_DESCRIPTION_BASICS-C` | Claim links descriptive/management information to lifecycle, retention requirements and responsible organization. DACS is explicitly an archival-description standard, not direct authority for the full records-management/retention proposition. | Confirmed source-scope mismatch. During authorized correction, replace/add a suitable records-management/retention source or narrow the Claim to archival description. |
| 62 | `CLM-ASTRONOMY_OBSERVATION_BASICS-A` | NASA's stored Universe overview discusses the universe's history and components, but the Claim's phrase “accessible to study by astronomical methods” is not directly established by that overview. A separate NASA “What is the Universe?” page directly describes the universe as including space, time, matter and energy, but still does not by itself substantiate the methods/accessibility clause. | Keep E=1 provisional; cite a suitable astronomy/cosmology source for the methods clause or narrow it. |
| 85 | `CLM-BIODIVERSITY_BASICS-C` | Claim asserts biodiversity assessment depends on spatial scale, time and observation method. The OpenStax page supports biodiversity measurement and method limitations in part, but the stored EU is generic and does not map the three-part rule to specific text. Separately, the Source record's `source_identity` is a descriptive sentence (“Биоразнообразие описывает…”) rather than the actual identity/title of the OpenStax source linked by its URI. | **Confirmed Source metadata quality defect** plus incomplete claim-specific evidence mapping. Correct source identity only in the authorized correction phase; retain E as provisional until the three factors are supported. |
| 97 | `CLM-CARTOGRAPHY-C` | Claim defines map scale as the relation between map distance and corresponding ground distance. The stored USGS “Mapping 101” source is broadly relevant but the EU is generic; this pass did not confirm a direct scale definition in the linked page. | Keep E=1 provisional; add a direct USGS map-scale locator or an authoritative cartography definition. |

## Source checks consulted

- WHO, *Environmental noise guidelines for the European Region*: https://www.who.int/publications/i/item/9789289053563
- FAO, *Agricultural water management*: https://www.fao.org/land-water/water/agricultural-water-management/en
- NIST, *Tutorials in Analytical Chemistry*: https://www.nist.gov/programs-projects/tutorials-analytical-chemistry
- IUPAC Gold Book, *analytical chemistry* (08003): https://goldbook.iupac.org/terms/view/08003
- NIGMS, *Cells, tissues, organs and systems* (stored legacy URL): https://www.nigms.nih.gov/education/fact-sheets/Pages/cells-tissues-organs-and-systems.aspx
- SAA, *Describing Archives: A Content Standard*: https://saa-ts-dacs.github.io/
- NASA, *Universe overview*: https://science.nasa.gov/universe/overview/
- NASA, *What is the Universe?*: https://science.nasa.gov/exoplanets/what-is-the-universe/
- OpenStax, *Preserving Biodiversity*: https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity
- USGS, *Mapping 101*: https://www.usgs.gov/science/science-explorer/maps-and-mapping/mapping-101

## Required follow-up

1. Reconcile the analytical-chemistry E rationale against the additional direct IUPAC Evidence Use before any score is finalized.
2. Add the biodiversity Source identity mismatch to the inventory-wide Source metadata defect ledger.
3. Preserve the agricultural filename/internal-ID variants and verify all pointers against internal IDs, never by filename alone.
4. Keep the other E=1 dispositions open until a pinpoint locator or better-matched authority is recorded.
5. Finish the inventory-wide candidate exclusion/overlap gate before replacing provisional Batch 41 scores with final scores.

## Protected-state boundary

No Claim, Evidence Use, Source or Relation JSON was changed. No IDs, references, or provenance were rewritten. `main` and M12 remain outside the edit scope. PR #21 remains draft/open/unmerged. This report does not certify Batch 41 or M13 as complete.
