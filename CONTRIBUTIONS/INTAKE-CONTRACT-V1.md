# Contribution Intake Contract v1.0

## Purpose and boundary

`contribution-submission-v1.schema.json` validates the user-submitted proposal payload. It is not the internal workflow envelope and does not create a canonical Record. Receipt ID, server timestamp, queue state, review history, decision, and release reference must be generated/stored by the intake service in a separate controlled layer.

## Privacy boundary

The payload intentionally rejects unknown properties. Do not add email, phone, private profile details, IP address, or other contact fields to this public content payload. If follow-up contact is needed, collect it through a separate access-controlled contact record with an explicit retention policy. Avoid collecting sensitive personal data.

## Validation semantics

- Schema validity means only that the payload has the expected shape.
- It does not establish source quality, independence, or truth.
- Conditional rules require related IDs for corrections and contradictions, at least one source for source submissions, and a proposed relation for relation submissions.
- High-consequence submissions must be routed to the additional human review path regardless of schema validity.
- Accepted submissions still require editorial approval, controlled integration, regression checks, and a versioned release.

## Implementation status

This contract and its tests are a local repository implementation step. It is not a hosted intake form, queue, identity system, or public submission endpoint. Do not open public intake until licensing, privacy, retention, abuse controls, and review ownership are approved.
