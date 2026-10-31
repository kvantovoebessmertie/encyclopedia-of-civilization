# M13 Correction Authorization — Web Systems Evidence Pinpoints — 2026-10-12

Authorization ID: `M13-WEB-SYSTEMS-EVIDENCE-001`

Status: **bounded editorial authorization; does not authorize publication**

## Purpose

Replace generic Evidence Use descriptions with source-specific section pinpoints for the three existing Claims in `web-systems-basics`, using the existing MDN “How the Web Works” Source @1. The inspected source page explicitly covers clients/servers, DNS, HTTP, and website files; it also states that browser rendering details are treated in a separate article.

## Authorized scope

Only the following existing records may be versioned from Evidence Use @1 to @2:

- `EU-WEB_SYSTEMS_BASICS-A`: pinpoint to “Clients and servers” and “The other parts of the toolbox”; describe only the high-level client/server and resource delivery model.
- `EU-WEB_SYSTEMS_BASICS-B`: pinpoint to “The other parts of the toolbox” and “HTTP basics”; preserve HTTP as an application protocol and note that the source describes website files/assets beyond HTML.
- `EU-WEB_SYSTEMS_BASICS-C`: pinpoint to “DNS explained” and the first step in “So what happens, exactly?”; preserve that DNS lookup maps a domain name to an IP address and does not itself establish the subsequent connection.

Allowed edits are limited to the three Evidence Use records' `record_version` and claim-specific `content.material.description`, plus the dedicated regression test and this authorization/checkpoint documentation. Claim wording, Source identity/URI, Claim and Source versions, Context/Scope, Relations, slice record count, coverage manifest, and all other records remain outside scope.

## Validation

- Preserve exact Claim and Source references.
- Add regression assertions for version 2, the exact Claim/Source IDs, section pinpoints, and scope limits.
- Run content preflight, Reference tests, Release Conformance Gate, and Offline Edition on the exact resulting HEAD.
- Keep M13 open and Draft/unmerged. Do not add any public-reader allowlist entry or authorize publication.

## Evidence boundary

This authorization permits metadata-level pinpointing based on the named MDN sections. It does not itself assign D/E/B scores, prove source independence, complete Human View, resolve licensing/attribution, or approve public release.
