# M13 behavioral-biology source-fit correction checkpoint

Date: 2026-11-15  
Authorization: `M13-BEHAVIORAL-BIOLOGY-OPENSTAX-001`  
Basis: Package 06, 2026-11-14  
Current branch head at checkpoint creation: `805b145bda4b002d97f695e974bf76f019e7e6ea`

## Confirmed defect and correction

Package 06 identified that `SRC-BEHAVIORAL_BIOLOGY_BASICS@1` pointed to OpenStax Biology 2e Chapter 46 (Ecology of Ecosystems), not behavioural biology. The relevant source is OpenStax Biology 2e §45.7, “Behavioral Biology: Proximate and Ultimate Causes of Behavior”:

https://openstax.org/books/biology-2e/pages/45-7-behavioral-biology-proximate-and-ultimate-causes-of-behavior

Applied bounded, versioned correction:
- `SRC-BEHAVIORAL_BIOLOGY_BASICS@2` now identifies §45.7 and its exact URI.
- `EU-BEHAVIORAL_BIOLOGY_BASICS-A/B/C@2` now point to Source @2 and contain claim-specific passage descriptions.
- A is bounded to the source's definition of behaviour as activity change in response to a stimulus.
- B is bounded to the introductory distinction between innate behaviour with a strong genetic component and learned behaviour shaped by environmental conditioning.
- C is explicitly marked only partially supported: §45.7 does not establish the methodological rule against attributing untestable motives. No Claim wording was changed.
- Slice README and dedicated regression now assert source identity, URI, versioned lineage, claim-specific support boundaries, and the partial-support limitation for C.

## Integrity

- No Claim wording or version changed.
- No new or deleted canonical records; slice remains nine records.
- No coverage count or Relation changed.
- No D/E/B or risk metadata assigned.
- No publication clearance granted.
- `main` unchanged; PR #21 remains Draft/unmerged.

## Verification required

Run the dedicated behavioural-biology regression, Content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. This checkpoint records the correction, not successful CI or M13 closure.
