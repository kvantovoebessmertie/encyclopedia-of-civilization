# Bounded Authorization Request — Library / Archival Preservation Relation

Date: 2026-11-19  
PR: #22  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **NOT AUTHORIZED — owner approval required**

## Exact target

- File: `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION.json`
- Current record ID/version: `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3`
- Current blob SHA at inspection head: `fddff535794460810f378ca6f13bc49bfd786ccc`
- Current participant 1: `CLM-LIBRARY_SCIENCE-A@2`
- Current participant 2: `CLM-ARCHIVAL_SCIENCE-A@2`

## Verified basis for the proposed correction

The semantic HOLD arose because Library Claim A is about equal access to information, collections and public-library services, while the Relation type is `shared_information_preservation_context`.

A stronger existing endpoint is available:

- `CLM-LIBRARY_SCIENCE-C@2` states that public libraries support preservation and access to local/Indigenous knowledge and heritage, including oral traditions and digital materials.
- `EU-LIBRARY_SCIENCE-C@2` exactly references Claim C@2 and `SRC-LIBRARY_SCIENCE@2`; its locator is IFLA-UNESCO Public Library Manifesto 2022, “Missions of the Public Library”, p. 2, on preservation/access of local and Indigenous data, knowledge and heritage and digitised/born-digital material.
- `CLM-ARCHIVAL_SCIENCE-A@2` describes appraisal, arrangement, description and preservation in archival processing; `EU-ARCHIVAL_SCIENCE-A@2` has exact section locators.
- The current Relation provenance already references `SRC-LIBRARY_SCIENCE@2` and `SRC-ARCHIVAL_SCIENCE@2`; no new Source identity is required for the proposed pair.

This pair is materially closer to the declared preservation relationship than the current access-focused Library Claim A.

## Requested authorized operation

If approved, authorize only the following operation:

1. Create `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@4`.
2. Change participant 1 from `CLM-LIBRARY_SCIENCE-A@2` to `CLM-LIBRARY_SCIENCE-C@2`.
3. Preserve participant 2 as `CLM-ARCHIVAL_SCIENCE-A@2`.
4. Preserve `provenance.created_from` exactly as the current two Source references:
   - `SRC-LIBRARY_SCIENCE@2`
   - `SRC-ARCHIVAL_SCIENCE@2`
5. Preserve `relation_type`, participant order, roles, direction, `frame_ref`, provenance method, all other fields, and all unrelated records.
6. Update the Relation inventory and semantic HOLD remediation register to record the new exact version and re-review result.
7. Keep the Relation on HOLD for publication unless and until its independent endpoint Claim, Evidence Use, rights, Context applicability, editorial and Human View gates are passed.

## Explicit exclusions

This authorization does **not** permit:
- changing either Claim or Evidence Use record;
- changing Source, Context or Scope records;
- changing the Relation type, roles, direction or frame reference;
- changing the allowlist or any publication state;
- promoting the Relation or either Claim to INCLUDE;
- inferring IFLA/UNESCO reuse rights. The rights screen for the Manifesto remains HOLD pending project-level rights and attribution decisions;
- modifying any other Relation or slice.

## Owner decision

- [ ] Approve exactly the operation above.
- [ ] Reject; retain current Relation on HOLD.
- [ ] Request a different bounded scope.

Approver identity, date and decision must be recorded by the project owner before any canonical edit. Until then, no change will be made.
