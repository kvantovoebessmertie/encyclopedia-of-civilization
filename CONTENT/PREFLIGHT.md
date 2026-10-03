# Content Preflight Rule

## Purpose

Before any content expansion is committed to `main`, the changed corpus MUST pass a deterministic preflight check.

The purpose is to catch predictable structural, schema, record-type, identity, slice-registration and coverage errors before the full CI / Release Gate cycle.

## Mandatory order

```text
authoring
  ↓
preflight
  ↓
commit
  ↓
CI
  ↓
Reference Tests / Release Gate
  ↓
checkpoint
```

A non-clean preflight blocks the commit.

## Preflight coverage

The preflight MUST check, at minimum:

1. JSON/schema validity for every corpus Record.
2. Record-type/profile requirements.
3. Required fields and forbidden/additional fields.
4. Known type-specific invariants, including Evidence Use and Scope contracts.
5. Duplicate `record_id + record_version` identities.
6. Vertical-slice structure and required regression registration.
7. Corpus record-count and slice-count synchronization with `RELEASE/CONTENT-COVERAGE.json`.
8. Any cross-record/reference checks already implemented by the Reference Validator.
9. Every previously discovered CI / Release Gate failure pattern that can be detected deterministically before CI.

## Regression rule

Every newly discovered failure that is caused by a deterministic, machine-checkable invariant MUST be converted into a permanent preflight or validator check after the immediate data fix.

The project MUST NOT rely on repeatedly discovering the same class of error through Release Gate failures.

## Wave rule

For every new wave:

- create the complete wave;
- run preflight;
- fix every preflight finding;
- only then commit/push;
- run the full CI / Release Gate;
- if CI discovers a new deterministic failure, fix it and add the corresponding guard before the next wave;
- declare the wave CLEAN only from a passing gate on the current commit.

## Current known failure classes

The preflight explicitly protects against the failure classes recently found in Wave 7:

- missing `content.material` in Evidence Use;
- invalid / forbidden `applies_to` in Scope;
- missing `content.target_ref` in Scope;
- missing `content.scope_content` in Scope;
- duplicate record identities;
- corpus coverage/count drift;
- slice registration drift.

This rule is part of the project's working content-authoring process and remains in force for subsequent waves.
