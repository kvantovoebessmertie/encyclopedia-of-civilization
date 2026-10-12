# M13 Web Systems Evidence Pinpoint Checkpoint — 2026-10-12

Status: **three Evidence Use records versioned with claim-specific MDN section pinpoints; exact-head CI pending**

## Authorized scope

Applied authorization `M13-WEB-SYSTEMS-EVIDENCE-001` in `RELEASE/M13-CORRECTION-AUTHORIZATION-WEB-SYSTEMS-2026-10-12.md`. The authorization is registered in `RELEASE/EDITORIAL-CORRECTION.json` for `web-systems-basics`.

Only the three existing Evidence Use records were versioned from @1 to @2. Claim wording, Source identity and URI, Claim/Source versions, Context/Scope, Relations, coverage counts, and the slice's nine-record count were not changed.

## Changes

| Evidence Use | Claim | MDN pinpoint | Boundary preserved |
|---|---|---|---|
| `EU-WEB_SYSTEMS_BASICS-A@2` | `CLM-WEB_SYSTEMS_BASICS-A@1` | “Clients and servers”; “The other parts of the toolbox” | High-level client/server model; no claim to cover all architectures or detailed browser rendering |
| `EU-WEB_SYSTEMS_BASICS-B@2` | `CLM-WEB_SYSTEMS_BASICS-B@1` | “The other parts of the toolbox”; “HTTP basics” | HTTP as an application protocol and resources beyond HTML; not a complete HTTP reference |
| `EU-WEB_SYSTEMS_BASICS-C@2` | `CLM-WEB_SYSTEMS_BASICS-C@1` | “DNS explained”; step 1 of “So what happens, exactly?” | DNS resolves domain name to IP address; this does not guarantee a successful connection or server availability |

Source remains `SRC-WEB_SYSTEMS_BASICS@1`, identifying MDN “How the Web Works”. A dedicated regression asserts Evidence Use version, exact Claim/Source refs, section markers, and stated boundaries.


## Claim-specific support boundary discovered during passage review

- **Claim A is only partially supported by the current Source as written.** MDN “How the Web Works” supports the high-level client/server and delivery model, but the page explicitly says that actual browser rendering is covered separately in “How browsers load websites”. The current Claim combines both propositions. Do not treat `EU-WEB_SYSTEMS_BASICS-A@2` as complete support for the rendering clause. A follow-up must either (a) add a separately authorized, versioned Source/Evidence Use pinpoint to MDN “How browsers load websites”, or (b) propose a narrowly scoped Claim correction after explicit authorization. Neither action is included in this checkpoint.
- **Claim B:** the named MDN sections support HTTP as an application protocol and the fact that web resources include more than HTML. Keep the claim limited to that high-level description; the page is not a comprehensive HTTP specification.
- **Claim C:** the named sections support DNS mapping a domain name to an IP address before the browser sends HTTP messages to the appropriate server. The text should not be interpreted as a guarantee that the later connection succeeds.

## Validation and disposition

- Change was limited to the three authorized Evidence Use descriptions/versions, the correction registry, the dedicated regression, and this checkpoint documentation.
- Exact-head Reference Tests, Release Conformance Gate, and Offline Edition must all complete successfully before this correction is treated as technically verified.
- No D/E/B score is assigned by this correction.
- Exact pinpointing is not independent evidence, proof of source independence, Human View, rights/attribution approval, or public-release approval.
- M13 remains open; keep PR #21 Draft/unmerged and `main` unchanged. No reader allowlist entry or publication decision is authorized.
