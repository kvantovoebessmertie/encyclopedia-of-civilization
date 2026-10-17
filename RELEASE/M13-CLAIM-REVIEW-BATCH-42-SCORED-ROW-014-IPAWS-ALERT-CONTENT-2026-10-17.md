# M13 Batch 42 — Scored row 014: sufficient content and temporal applicability in public alerts

Date: 2026-10-17  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-IPAWS-ALERT-CONTENT@1`  
Evidence Use version: `EU-IPAWS-ALERT-CONTENT@1`  
Source version: `SRC-PUBLIC-ALERT-GUIDANCE@1`

## Claim under review

> Публичное аварийное предупреждение должно содержать достаточно информации для понимания сообщения и его временной применимости.

## Current record linkage

The Claim and Evidence Use both reference `SRC-PUBLIC-ALERT-GUIDANCE@1`. The Source URI is FEMA's *IPAWS Tips — Tip 44: Best Practices for Alerting Authorities Using Wireless Emergency Alerts for Public Alert, Warning & Notification*:

https://www.fema.gov/sites/default/files/documents/fema_ipaws-tip-44-best-practices-wea.pdf

The linked PDF was accessible during this review. In section II, “Compose Effective WEA Messages,” subsection A says effective messages include sufficient information for the public to validate the incident and risk and guide protective action. Subsection B lists the trusted source sender, event description, incident location, protective action, guidance/expiration time or duration, and a URL or phone number for more information.

## Passage-level assessment

The linked official passage directly supports both parts of the Claim: sufficient content for understanding the incident and its risk, and an explicit time/expiration/duration element. The Claim is a concise summary rather than a complete message-writing specification. The cited guidance concerns U.S. Wireless Emergency Alerts and should not be generalized into a universal legal requirement for every warning channel or jurisdiction.

The canonical Evidence Use currently says only that the source describes the information function of public alerts; it does not preserve a section-level pinpoint. The passage is directly verified in this report, but the canonical linkage remains generic.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-IPAWS-ALERT-CONTENT` | 2 | 1 | 2 | **D=2:** emergency communication guidance can influence protective action. **E=1:** the exact linked FEMA PDF and relevant section were directly checked, but the canonical Evidence Use has no section-level pinpoint and the claim should be kept within WEA/U.S. scope. **B=2:** the statement is a reasonable summary of the source's sufficient-information and guidance/expiration-time elements; it does not claim to be exhaustive or jurisdiction-neutral. |

## Disposition

**HOLD pending independent Human View and the M13 high-consequence review gate.** The passage supports the Claim at summary level, but the canonical Evidence Use remains generic and the Claim is not cleared for public release.

No canonical Claim, Evidence Use, or Source record changed. Any source-link or Evidence Use correction requires separate authorization and a versioned regression.

This is row 014 of Batch 42, not a release decision.
