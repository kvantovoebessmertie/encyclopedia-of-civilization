# Public MVP — Local Operator Runbook

Date: 2026-10-11
Status: implementation guide for private/local preview and contribution-form prototypes; **not a production deployment procedure**.

## 1. Current component map

- [Public MVP specification](MVP-PUBLIC-EDITION-SPEC-2026-10-11.md)
- [Professional contribution workflow](../CONTRIBUTIONS/PROFESSIONAL-CONTRIBUTION-WORKFLOW-SPEC-2026-10-11.md)
- [Pilot and release gates](PUBLIC-PILOT-AND-RELEASE-GATES-2026-10-11.md)
- [Architecture fit](MVP-ARCHITECTURE-FIT-2026-10-11.md)
- HTML escaping/security fix: PR #24
- Read-only preview builder: PR #25
- Intake JSON Schema and validator/tests: PR #26
- Local-only contribution form with JSON export: PR #27

All listed implementation PRs are Draft until their exact-head checks, review, and dependency order are satisfied. No public launch is implied.

## 2. Build a private preview

Run from the repository root:

```sh
PYTHONPATH=REFERENCE/src python REFERENCE/build_public_preview.py \
  --records REFERENCE/fixtures/public-preview-records.json \
  --manifest REFERENCE/fixtures/public-preview-manifest.json \
  --output /tmp/encyclopedia-public-preview
```

Then open `/tmp/encyclopedia-public-preview/index.html` in a browser. Keep `search.js` and `preview-manifest.json` beside `index.html`.

The committed fixtures are synthetic test data. They are for interface/security checks only and must not be presented or redistributed as an encyclopedia edition.

The builder requires an explicit allowlist of exact record IDs and versions, requires each selection to be marked `preview_only`, and refuses any edition state other than `preview`. Do not change that guard to make a release build. The generated manifest records the selection and hashes.

## 3. Local contribution form prototype

Open `CONTRIBUTIONS/intake-form-prototype.html` in a browser. Complete the form and select **Проверить и скачать JSON**.

- The form runs locally and exports a JSON file that follows the v1 payload shape.
- It has no server endpoint, no network submission, no contact fields, and no editorial inbox.
- A downloaded JSON file is a proposal, not an accepted contribution. Validate it against `CONTRIBUTIONS/contribution-submission-v1.schema.json` and route it to a designated editor using an approved channel.
- Do not ask contributors to put personal contact details into the public payload. If follow-up contact is needed, it must be stored separately under a defined privacy/retention policy.
- Do not integrate a submitted payload directly into canonical content. Preserve the original submission, assign receipt/workflow metadata separately, perform editorial/source/rights/risk review, then prepare a reviewable diff and run regression checks.

## 4. Pilot-corpus selection checklist

For every proposed pilot record, the editorial owner must verify:

- Claim statement and record type are appropriate and readable without repository knowledge.
- Source identity matches the actual destination; URI is specific enough to find the cited work.
- Evidence Use describes the exact passage/section/table/page supporting the complete proposition.
- Applicability, jurisdiction, date, uncertainty and limitations are visible where relevant.
- Material is legally publishable under a clearly documented license/permission basis.
- High-consequence claims have domain-appropriate review and escalation language.
- Related Claims, Evidence Uses, Sources and Relations are present in the selected package or explicitly marked as unavailable.
- The selected set is an explicit allowlist; unreviewed content is excluded rather than presumed acceptable.

Do not use the corpus-wide `publication_status` field alone as proof of editorial approval. A pilot requires a separate, claim-level release decision.

## 5. Release gates — do not bypass

1. **Security:** HTML escaping, restrictive CSP, no remote scripts/assets, no unsafe DOM insertion, and adversarial tests pass on the exact release candidate.
2. **Reader:** human-readable Claim/source/evidence/relation view is reviewed for missing references, mixed languages, long text, and inaccessible layouts.
3. **Content:** pilot allowlist is approved by a named editorial owner; high-consequence content receives additional review.
4. **Rights and privacy:** publication license/terms, attribution, takedown/correction path, contact-data separation, retention, and contributor consent are documented.
5. **Intake operations:** a real endpoint or approved manual channel exists; abuse handling, receipt IDs, duplicate detection, editorial states, and rejection/appeal paths are defined. The local form alone does not satisfy this gate.
6. **Operations:** hosting/domain, TLS, backups, monitoring, build reproducibility, rollback, and incident ownership are agreed and tested.
7. **Verification:** the full Reference tests, Release Conformance Gate, and Offline Edition checks all pass on the exact final commit; the generated artifact is inspected.
8. **Approval:** final release review is recorded. Draft PRs are not merged and no live deployment is performed by this runbook.

## 6. Current unresolved launch decisions

These are genuine release blockers rather than implementation details to guess:

- Public license/terms and attribution policy.
- Hosting/domain and the person responsible for operating the service.
- Editorial owner(s), review SLAs, escalation, correction/takedown and appeal process.
- Whether submissions are accepted through a secure hosted endpoint or an approved manual workflow.
- If contact details are needed, separate storage, lawful basis, access control and retention period.
- Pilot scope and languages to expose in the first public release.

Until these are resolved, keep all builds private/local and keep PRs as Draft.
