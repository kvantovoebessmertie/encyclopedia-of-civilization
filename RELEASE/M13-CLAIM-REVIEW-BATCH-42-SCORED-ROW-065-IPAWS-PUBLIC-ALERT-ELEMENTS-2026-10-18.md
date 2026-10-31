# M13 Batch 42 — Scored row 065: core elements of a public alert

Date: 2026-10-18  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-IPAWS-ALERT-ELEMENTS@1`  
Evidence Use version: `EU-IPAWS-ALERT-ELEMENTS@1`  
Source version: `SRC-PUBLIC-ALERT-GUIDANCE@1`

## Claim under review

> Официальное руководство по публичным предупреждениям рекомендует ясно указывать источник, событие, место и временную применимость сообщения.

## Evidence fit

The canonical Source is FEMA's IPAWS best-practices guidance PDF:
https://www.fema.gov/sites/default/files/documents/fema_ipaws-tip-44-best-practices-wea.pdf

The Evidence Use states that the source lists core structural elements of a public warning. This aligns with the Claim's source, event, location and time applicability fields, but the record has no page/section locator. Each listed element should be checked against the exact guidance and terminology before the Claim is accepted.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-IPAWS-ALERT-ELEMENTS` | 2 | 2 | 2 | **D=2:** public-alert content can affect safety-critical understanding. **E=2:** the FEMA guidance and Evidence Use align with the alert-element claim, though a page/section pinpoint is missing. **B=2:** the statement is bounded to recommended message content and does not prescribe a specific alert system implementation. |

## Disposition

**HOLD pending exact PDF page/section locator and independent Human View.** No canonical record changed.
