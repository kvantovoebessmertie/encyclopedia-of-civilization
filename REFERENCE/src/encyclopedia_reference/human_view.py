from __future__ import annotations

from typing import Any

from .query import QueryInterface


STATUS_LABELS = {
    "known": "ИЗВЕСТНО",
    "unknown": "НЕИЗВЕСТНО",
    "observed": "НАБЛЮДАЛОСЬ",
    "supported": "ПОДДЕРЖАНО",
    "assessed": "ОЦЕНЕНО",
    "inferred": "ВЫВЕДЕНО",
    "disputed": "ОСПАРИВАЕТСЯ",
    "unresolved": "НЕ РАЗРЕШЕНО",
    "not_applicable": "НЕ ПРИМЕНИМО",
}


def _ref_key(ref: dict[str, Any]) -> tuple[str, str]:
    return (str(ref.get("record_id", "")), str(ref.get("version", "")))


class HumanView:
    """Человеческое представление поверх канонических Record без изменения семантики."""

    def __init__(self, query: QueryInterface):
        self.query = query

    def build(self, record_id: str, version: str | None = None, mode: str = "UNDERSTAND") -> dict[str, Any]:
        records = self.query.query()
        by_key = {(r["record_id"], str(r["record_version"])): r for r in records}
        record = next((r for r in records if r["record_id"] == record_id and (version is None or str(r["record_version"]) == version)), None)
        if record is None:
            return {"status": "not_found", "record_id": record_id}

        content = record.get("content") or {}
        view = {
            "status": "ok",
            "record": {"record_id": record["record_id"], "version": record["record_version"], "type": record["record_type"]},
            "mode": mode,
            "known": [],
            "basis": [],
            "inferred": [],
            "unknown": [],
            "applicability": [],
            "constraints": [],
            "traceability": [],
        }

        if content.get("statement"):
            view["known"].append({"status": "known", "text": content["statement"]})

        if content.get("basis"):
            view["basis"].append(content["basis"])
        if content.get("limitations"):
            view["constraints"].append(content["limitations"])

        for key, value in content.items():
            if isinstance(value, dict) and value.get("status") in {"unknown", "not_applicable", "unresolved"}:
                view["unknown"].append({"field": key, "status": value["status"], "label": STATUS_LABELS.get(value["status"], value["status"])})
            if key == "uncertainty" and isinstance(value, dict) and value.get("status"):
                view["unknown"].append({"field": key, "status": value["status"], "label": STATUS_LABELS.get(value["status"], value["status"])})

        if record["record_type"] == "inference":
            conclusion = content.get("conclusion", {})
            if isinstance(conclusion, dict) and conclusion.get("statement"):
                view["inferred"].append({"status": "inferred", "text": conclusion["statement"]})

        for key in ("context_ref", "scope_ref"):
            ref = content.get(key)
            if isinstance(ref, dict):
                target = by_key.get(_ref_key(ref))
                if target:
                    tc = target.get("content") or {}
                    view["applicability"].append({
                        "type": key[:-4],
                        "record_id": target["record_id"],
                        "version": target["record_version"],
                        "content": tc.get("context_content", tc.get("scope_content", {})),
                    })
                else:
                    view["unknown"].append({"field": key, "status": "unresolved", "label": "НЕ РАЗРЕШЕНО"})

        for key in ("target_ref", "claim_ref", "source_ref", "basis_ref", "decision_ref", "context_ref", "scope_ref"):
            ref = content.get(key)
            if isinstance(ref, dict) and "record_id" in ref:
                view["traceability"].append({"record_id": ref["record_id"], "version": ref.get("version")})
        for key in ("premises", "refs"):
            refs = content.get(key)
            if isinstance(refs, list):
                for ref in refs:
                    if isinstance(ref, dict) and "record_id" in ref:
                        view["traceability"].append({"record_id": ref["record_id"], "version": ref.get("version")})

        return view


def build_human_view(query: QueryInterface, record_id: str, version: str | None = None, mode: str = "UNDERSTAND") -> dict[str, Any]:
    return HumanView(query).build(record_id, version, mode)
