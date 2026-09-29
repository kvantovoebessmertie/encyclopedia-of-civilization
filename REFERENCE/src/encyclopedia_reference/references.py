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

        def check(ref: Any, path: str) -> None:
            if not isinstance(ref, dict):
                return
            record_id = ref.get("record_id")
            version = ref.get("version")
            if not isinstance(record_id, str):
                return
            try:
                if version is None:
                    self.storage.latest(record_id)
                else:
                    self.storage.read_version(record_id, version)
            except StorageError as exc:
                findings.append(
                    Finding(
                        code="VAL-L3-REFERENCE-VERSION",
                        severity="error",
                        layer="L3",
                        message=f"{path}: ссылка не разрешается: {exc}",
                    )
                )

        provenance = record.get("provenance", {})
        if isinstance(provenance, dict):
            for key in ("agent_refs", "created_from", "transformed_from"):
                for index, ref in enumerate(provenance.get(key, [])):
                    check(ref, f"provenance.{key}[{index}]")

        content = record.get("content", {})
        if not isinstance(content, dict):
            return findings

        if record.get("record_type") == "claim":
            for key in ("scope_ref", "context_ref"):
                if key in content:
                    check(content[key], f"content.{key}")
            for index, ref in enumerate(content.get("referents", [])):
                check(ref, f"content.referents[{index}]")
            for index, ref in enumerate(content.get("relation_refs", [])):
                check(ref, f"content.relation_refs[{index}]")

        elif record.get("record_type") == "evidence_use":
            for key in ("claim_ref", "source_ref", "resolution_context", "source_state_ref"):
                if key in content:
                    check(content[key], f"content.{key}")

        elif record.get("record_type") == "assessment":
            for key in ("target", "assessor_ref", "method_ref", "scale_ref", "profile_ref"):
                if key in content:
                    check(content[key], f"content.{key}")
            for index, ref in enumerate(content.get("inputs", [])):
                check(ref, f"content.inputs[{index}]")

        elif record.get("record_type") == "inference":
            for key in ("decision_ref", "method_ref", "rule_ref", "model_ref", "procedure_ref"):
                if key in content:
                    check(content[key], f"content.{key}")
            for key in ("premises", "assumptions"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")
            attribution = content.get("attribution", {})
            if isinstance(attribution, dict) and "agent_ref" in attribution:
                check(attribution["agent_ref"], "content.attribution.agent_ref")

        elif record.get("record_type") == "decision":
            for key in ("decision_maker", "context_ref", "scope_ref", "authority_ref", "process_ref"):
                if key in content:
                    check(content[key], f"content.{key}")

        elif record.get("record_type") == "action":
            for key in ("context_ref", "scope_ref", "decision_ref", "procedure_ref"):
                if key in content:
                    check(content[key], f"content.{key}")
            for key in ("performer_refs", "target_refs"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")

        elif record.get("record_type") == "event":
            for key in ("context_ref", "scope_ref"):
                if key in content:
                    check(content[key], f"content.{key}")
            for key in ("participants", "observation_refs", "cause_refs"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")

        elif record.get("record_type") == "result":
            for key in ("scope_ref", "observation_scope_ref", "comparison_reference"):
                if key in content:
                    check(content[key], f"content.{key}")
            frame = content.get("reference_frame", {})
            if isinstance(frame, dict):
                for index, ref in enumerate(frame.get("refs", [])):
                    check(ref, f"content.reference_frame.refs[{index}]")
            causal = content.get("causal_attribution", {})
            if isinstance(causal, dict) and "basis_ref" in causal:
                check(causal["basis_ref"], "content.causal_attribution.basis_ref")

        elif record.get("record_type") == "state":
            for key in ("subject_ref", "frame_ref"):
                if key in content: check(content[key], f"content.{key}")
            for index, ref in enumerate(content.get("observation_refs", [])):
                check(ref, f"content.observation_refs[{index}]")

        elif record.get("record_type") == "process":
            for key in ("context_ref", "start_ref", "end_ref"):
                if key in content: check(content[key], f"content.{key}")
            for key in ("participants", "phase_refs"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")

        elif record.get("record_type") == "relation":
            if "frame_ref" in content: check(content["frame_ref"], "content.frame_ref")
            for index, ref in enumerate(content.get("participants", [])):
                check(ref, f"content.participants[{index}]")

        elif record.get("record_type") == "identity":
            if "scope_ref" in content: check(content["scope_ref"], "content.scope_ref")
            for key in ("targets", "evidence_refs"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")

        elif record.get("record_type") == "context":
            for key in ("target_ref", "scope_ref"):
                if key in content: check(content[key], f"content.{key}")
            for index, ref in enumerate(content.get("precondition_refs", [])):
                check(ref, f"content.precondition_refs[{index}]")

        elif record.get("record_type") == "scope":
            for key in ("target_ref", "universe_ref"):
                if key in content: check(content[key], f"content.{key}")

        elif record.get("record_type") == "provenance":
            for key in ("target_ref", "agent_ref", "method_ref"):
                if key in content: check(content[key], f"content.{key}")
            for key in ("inputs", "outputs"):
                for index, ref in enumerate(content.get(key, [])):
                    check(ref, f"content.{key}[{index}]")

        elif record.get("record_type") == "authorship_contribution":
            for key in ("target_ref", "contributor_ref", "rights_ref"):
                if key in content: check(content[key], f"content.{key}")

        elif record.get("record_type") == "trust_reputation":
            for key in ("target_ref", "scope_ref", "context_ref"):
                if key in content: check(content[key], f"content.{key}")
            for index, ref in enumerate(content.get("basis_refs", [])):
                check(ref, f"content.basis_refs[{index}]")

        return findings