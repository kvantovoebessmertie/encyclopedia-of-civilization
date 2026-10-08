from __future__ import annotations

from typing import Any

from .storage import FileStorage, StorageError
from .validator import Finding


class ReferenceResolver:
    """Проверяет локальные versioned references без молчаливого fallback."""

    def __init__(self, storage: FileStorage):
        self.storage = storage

    def validate(self, record: dict[str, Any]) -> list[Finding]:
        findings: list[Finding] = []

        def check(ref: Any, path: str, expected_type: str | None = None) -> None:
            if not isinstance(ref, dict):
                return
            record_id = ref.get("record_id")
            version = ref.get("version")
            if not isinstance(record_id, str):
                return
            try:
                target = (
                    self.storage.latest(record_id)
                    if version is None
                    else self.storage.read_version(record_id, version)
                )
                if target.get("record_id") != record_id:
                    findings.append(
                        Finding(
                            code="VAL-L3-REFERENCE-TARGET-IDENTITY",
                            severity="error",
                            layer="L3",
                            message=f"{path}: target record_id не совпадает с идентификатором ссылки",
                            subject=path,
                            rule="VAL-L3-REFERENCE-TARGET-IDENTITY",
                        )
                    )
                if version is not None and target.get("record_version") != version:
                    findings.append(
                        Finding(
                            code="VAL-L3-REFERENCE-HISTORICAL-VERSION",
                            severity="error",
                            layer="L3",
                            message=f"{path}: target record_version не совпадает с запрошенной исторической версией",
                            subject=path,
                            rule="VAL-L3-REFERENCE-HISTORICAL-VERSION",
                        )
                    )
                if expected_type is not None and target.get("record_type") != expected_type:
                    findings.append(
                        Finding(
                            code="VAL-L3-REFERENCE-TARGET-TYPE",
                            severity="error",
                            layer="L3",
                            message=(
                                f"{path}: ожидается Record типа {expected_type}, "
                                f"получен {target.get('record_type')}"
                            ),
                            subject=path,
                            rule="VAL-L3-REFERENCE-TARGET-TYPE",
                        )
                    )
            except StorageError as exc:
                findings.append(
                    Finding(
                        code="VAL-L3-REFERENCE-VERSION",
                        severity="error",
                        layer="L3",
                        message=f"{path}: ссылка не разрешается: {exc}",
                        subject=path,
                        rule="VAL-L3-REFERENCE-VERSION",
                    )
                )

        typed_paths: dict[str, str] = {
            "content.scope_ref": "scope",
            "content.context_ref": "context",
            "content.relation_refs": "relation",
            "content.source_state_ref": "state",
            "content.resolution_context": "context",
            "content.decision_ref": "decision",
            "content.process_ref": "process",
            "content.procedure_ref": "process",
            "content.observation_scope_ref": "scope",
        }

        def expected_type_for(path: str) -> str | None:
            if path in typed_paths:
                return typed_paths[path]
            for prefix, expected in typed_paths.items():
                if path.startswith(prefix + "["):
                    return expected
            return None

        def walk(value: Any, path: str) -> None:
            if isinstance(value, dict):
                # A canonical record_ref is identified by record_id. Extension
                # payloads are intentionally opaque to the canonical graph.
                if isinstance(value.get("record_id"), str):
                    check(value, path, expected_type_for(path))
                    return
                for key, child in value.items():
                    if key == "extensions":
                        continue
                    if (
                        path == "content"
                        and record.get("record_type") == "evidence_use"
                        and key in {"claim_ref", "source_ref"}
                    ):
                        continue
                    walk(child, f"{path}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{path}[{index}]")

        walk(record.get("provenance", {}), "provenance")
        for key in ("scope", "context"):
            if key in record:
                walk(record[key], key)

        content = record.get("content", {})
        if isinstance(content, dict) and record.get("record_type") == "evidence_use":
            if "claim_ref" in content:
                check(content["claim_ref"], "content.claim_ref", "claim")
            if "source_ref" in content:
                check(content["source_ref"], "content.source_ref", "source")
        walk(content, "content")

        return findings