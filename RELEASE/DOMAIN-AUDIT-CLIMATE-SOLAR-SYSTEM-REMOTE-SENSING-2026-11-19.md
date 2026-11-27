# Domain audit — climate science, Solar System and remote sensing (Part II Earth, climate and space)

Date: 2026-11-19  
Branch: mvp-public-contribution-design-2026-10-11  
PR workstream: #22, Work Package 1  
Audited revision: 71a30f318a4dfbe4bbb6edad294c75281c428f9f  
Disposition: **HOLD — three slices / 27 records screened; no canonical records changed**

## Plan and duplicate-control

This is the next Part II Earth/climate/space batch. Previously screened climate-basics, geology-basics, oceanography-basics, astronomy-observation-basics and the earlier solar-system orbit material were not reopened. Virology-basics was also skipped because its exact-record audit is already present in the controlling candidate register.

## Scope

- climate-science-basics — 9 records
- solar-system-basics — 9 records
- remote-sensing-basics — 9 records

Total: **27 records** (9 Claims, 9 Evidence Use, 3 Sources, 3 Context, 3 Scope).

## 1. climate-science-basics — 9 records

Claims:
- A: the slice introduces basic concepts and relations needed to orient the reader in the subject area.
- B: interpretation depends on source, context and claim applicability boundaries.
- C: basic knowledge does not replace specialized checking when conclusions depend on conditions, measurements or professional assessment.

Source: NASA, “Climate Change: Evidence”  
https://science.nasa.gov/climate-change/evidence/

Findings:
- All three Claims are editorial descriptions of the slice and its evidence limits, not falsifiable propositions about climate science.
- NASA's source page provides substantive evidence about observed warming, long-term climate indicators and human influence, but none of those propositions appears in the current Claims.
- All three EUs use generic descriptions without passage locators.
- Context and Scope target Claim A only.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires owner/editor-authorized replacement with substantive climate propositions and corresponding pinpoint EUs. Do not include the current editorial statements as climate-science facts.

## 2. solar-system-basics — 9 records

Claims:
- A: the Solar System includes the Sun, eight planets, dwarf planets, moons, asteroids and comets.
- B: the Sun is the star of the Solar System.
- C: the Solar System is located in the Milky Way galaxy.

Source: NASA, “Solar System Facts”  
https://science.nasa.gov/solar-system/solar-system-facts/

Findings:
- NASA directly states that the Solar System includes the Sun, eight planets, five officially named dwarf planets, hundreds of moons and thousands of comets and asteroids. This directly supports Claim A.
- NASA explicitly identifies the Sun as the system's star. This directly supports Claim B.
- NASA explicitly locates the Solar System in the Milky Way. This directly supports Claim C.
- The existing Context correctly warns that object catalogues/classifications may change with new observations and classifications. It targets Claim A only; Scope also targets A only.
- All three EUs remain generic and lack claim-specific page-section pinpoints.
- The source is maintained by NASA and contains changing catalogue quantities. The Claim avoids fixed moon/comet counts, but the educational rendering should preserve the Context's temporal/catalogue boundary.

Decision: **HOLD — strong direct source fit.** All three Claims are supported by the current NASA page; precise EU locators and Claim-specific Context/Scope coverage remain. Retain the catalogue-currentness warning.

## 3. remote-sensing-basics — 9 records

Claims:
- A: remote sensing uses measurements acquired at a distance, for example from airborne or space platforms.
- B: measured radiation or reflection is related to physical properties of the observed object.
- C: interpretation requires accounting for resolution, spectral characteristics and observation conditions.

Current Source: USGS, “Landsat Missions”  
https://www.usgs.gov/landsat-missions

Additional authoritative USGS source discovered:
- “Remote sensing systems – Platforms and sensors: Aerial, satellites, UAVs, optical, radar, and LiDAR”: https://www.usgs.gov/publications/remote-sensing-systems-platforms-and-sensors-aerial-satellites-uavs-optical-radar-and

Findings:
- The current Landsat page confirms that satellites acquire Earth-surface images and that Landsat data are used for natural-resource/environmental analysis. It does not provide a sufficiently complete general definition of remote sensing or the measurement physics in Claims A/B.
- The additional USGS publication gives a direct definition of remote sensing as acquiring information without physical contact and describes measurement of reflected/transmitted electromagnetic radiation from aerial/satellite platforms. This is a better direct source for Claim A and part of B, but it is not currently linked in the slice.
- Claim B's relationship between measured radiation and object physical properties needs a precise source passage on spectral signatures/reflectance/emittance.
- Claim C's resolution, spectral characteristics and observation conditions are not all established by the current Landsat landing page; they require specific sensor/remote-sensing source passages.
- All three EUs are generic and lack claim-specific locators.
- Context and Scope target Claim A only.

Decision: **HOLD — source fit incomplete.** Add or replace the source through an authorized versioned correction using the USGS remote-sensing definition and specific sensor/spectral/resolution references. Do not treat the broad Landsat mission landing page as complete evidence for all three Claims.

## Cross-slice and integrity checks

- All 27 inventory-listed files were read at version 1; local Claim/EU/Source references resolve to the corresponding listed records.
- No new Relation was created; proximity among climate science, solar-system science and remote sensing is not sufficient to justify a typed Relation.
- Prior climate-basics, geology, oceanography and astronomy-observation screens were not repeated.
- Prior virology screen was not repeated.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was edited.
- No INCLUDE decision, allowlist, preview or publication status was changed.
- main was not changed; PR #22 remains Draft.

## Group result

| Slice | Records | Main finding | Decision |
|---|---:|---|---|
| climate-science-basics | 9 | All Claims are editorial metadata; NASA source contains facts not asserted by current Claims | HOLD |
| solar-system-basics | 9 | All three Claims directly supported by NASA; EUs lack pinpoints | HOLD |
| remote-sensing-basics | 9 | USGS Landsat landing page is too broad; better USGS definition source found but not linked | HOLD |
| **Total** | **27** | **No public INCLUDE decisions** | **HOLD** |

Next Part II family: continue with engineering/computing only after excluding already reviewed civil engineering, software/computer networks and infrastructure candidates. Do not repeat closed reviews or start new M13 batches.
