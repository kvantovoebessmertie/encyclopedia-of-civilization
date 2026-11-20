# Selection-aware offline edition builder

This is an implementation note for the opt-in selection build path. It does not approve any corpus record, create a project allowlist, or change publication decisions.

## Selection manifest format

The builder accepts a JSON object with `schema_version` set to `"1.0"` and a non-empty `records` array. Each entry pins an exact canonical identity and carries an explicit decision:

```json
{
  "schema_version": "1.0",
  "records": [
    {
      "record_id": "SYNTHETIC-CLAIM-A",
      "record_version": "1",
      "decision": "INCLUDE",
      "dependencies": [
        {
          "record_id": "SYNTHETIC-SOURCE-A",
          "record_version": "1"
        }
      ]
    },
    {
      "record_id": "SYNTHETIC-SOURCE-A",
      "record_version": "1",
      "decision": "INCLUDE",
      "dependencies": []
    }
  ]
}
```

The identifiers above are illustrative synthetic values, not real selection decisions.

## Fail-closed checks

- Every selected identity must exist exactly once in the canonical input and match its pinned version.
- Duplicate canonical identities and duplicate selection entries are rejected.
- Only an explicit `INCLUDE` decision is accepted; `HOLD`, `EXCLUDE`, missing, and unknown decisions fail.
- Record references represented as nested `record_id` + `version` objects or exact `ID@version` strings are checked against the canonical input.
- Every detected in-corpus dependency must be declared in the entry and included in the same selection. Declared dependencies must also be selected.
- Missing or stale referenced dependencies fail. Dependencies are never silently added.
- Empty or unsupported manifests fail.

The builder does not infer approval from `publication_status`, `completion_status`, historical evaluations, or CI results.

## Invocation

From the repository root, with a separately prepared and approved manifest:

```bash
python REFERENCE/build_offline_edition.py \
  --selection-manifest /path/to/selection.json \
  --source-commit EXACT_SOURCE_COMMIT \
  --edition-id first-edition-preview \
  --output selected-offline-edition
```

The source commit is mandatory in selection mode. The resulting `edition-manifest.json` records the selection-manifest SHA-256, source commit, builder version, and exact selected identities. The existing command without `--selection-manifest` continues to build the full corpus for diagnostic/offline testing.

No real first-edition manifest is included in this repository change. Rights clearance, editorial approval, release ownership, and explicit owner authorization remain separate gates.
