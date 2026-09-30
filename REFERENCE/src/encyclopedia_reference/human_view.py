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
MODES = {"FIND","UNDERSTAND","VERIFY","APPLY","DECIDE","ACT","CHECK","RECOVER"}
UNRESOLVED_STATUSES = {"unknown","not_applicable","unresolved","not_established","not_assessed","not_known"}

def _ref_key(ref: dict[str, Any]) -> tuple[str, str]:
    return (str(ref.get("record_id", "")), str(ref.get("version", "")))

def _label(status: str) -> str:
    return STATUS_LABELS.get(status, status.upper())

class HumanView:
    """Человеческое представление поверх канонических Record без изменения семантики."""

    def __init__(self, query: QueryInterface):
        self.query = query

    def _resolve(self, ref: Any, by_key: dict[tuple[str, str], dict[str, Any]]) -> dict[str, Any] | None:
        return by_key.get(_ref_key(ref)) if isinstance(ref, dict) and "record_id" in ref else None

    def _add_trace(self, view: dict[str, Any], ref: Any) -> None:
        if isinstance(ref, dict) and "record_id" in ref:
            view["traceability"].append({"record_id": ref["record_id"], "version": ref.get("version")})

    def _collect_unknowns(self, value: Any, field: str, view: dict[str, Any]) -> None:
        if isinstance(value, dict):
            status = value.get("status")
            status_text = str(status) if status is not None else ""
            unresolved = status in UNRESOLVED_STATUSES or any(marker in status_text for marker in ("unknown", "unresolved", "not_assessed", "not_known", "not_established"))
            if unresolved:
                view["unknown"].append({"field": field, "status": status, "label": _label(status)})
            for key, child in value.items():
                if isinstance(child, (dict, list)):
                    self._collect_unknowns(child, f"{field}.{key}", view)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                if isinstance(child, (dict, list)):
                    self._collect_unknowns(child, f"{field}[{i}]", view)

    def build(self, record_id: str, version: str | None = None, mode: str = "UNDERSTAND") -> dict[str, Any]:
        mode = str(mode).upper()
        if mode not in MODES:
            return {"status": "invalid_mode", "record_id": record_id, "mode": mode, "allowed_modes": sorted(MODES)}
        records = self.query.query()
        by_key = {(r["record_id"], str(r["record_version"])): r for r in records}
        record = next((r for r in records if r["record_id"] == record_id and (version is None or str(r["record_version"]) == version)), None)
        if record is None:
            return {"status": "not_found", "record_id": record_id, "mode": mode}

        content = record.get("content") or {}
        view: dict[str, Any] = {
            "status": "ok",
            "record": {"record_id": record["record_id"], "version": record["record_version"], "type": record["record_type"]},
            "mode": mode,
            "known": [], "basis": [], "inferred": [], "unknown": [],
            "applicability": {
                "status": "not_established",
                "label": "ПРИМЕНИМОСТЬ НЕ УСТАНОВЛЕНА",
                "reason": "Текущий пользовательский Context не задан; исторический Context/Scope не является текущей рекомендацией.",
                "context": None, "scope": None,
            },
            "changes": [], "constraints": [], "traceability": [],
            "safety": {
                "historical_action_is_not_current_instruction": True,
                "source_is_not_truth": True,
                "inference_is_not_observation": True,
                "temporal_sequence_is_not_causality": True,
            },
        }

        if isinstance(content.get("statement"), str) and content["statement"]:
            view["known"].append({
                "status": "known", "label": _label("known"), "text": content["statement"],
                "epistemic_note": "Наличие утверждения в записи само по себе не устанавливает его истинность.",
            })

        if record["record_type"] == "inference":
            conclusion = content.get("conclusion", {})
            if isinstance(conclusion, dict) and conclusion.get("statement"):
                view["inferred"].append({"status": "inferred", "label": _label("inferred"), "text": conclusion["statement"]})
        elif record["record_type"] == "assessment":
            result = content.get("result")
            if isinstance(result, dict):
                view["known"].append({"status": "assessed", "label": _label("assessed"), "text": result,
                                       "epistemic_note": "Результат оценки не равен автоматически установленной истине."})
        elif record["record_type"] in {"event", "result"}:
            key = "event_content" if record["record_type"] == "event" else "result_content"
            payload = content.get(key)
            if isinstance(payload, dict):
                status = "observed" if content.get("origin") == ["observed"] else "known"
                view["known"].append({"status": status, "label": _label(status), "text": payload,
                                       "epistemic_note": "Временное следование само по себе не устанавливает причинность."})

        if content.get("basis"):
            view["basis"].append({"status": "basis", "text": content["basis"]})
        if content.get("limitations"):
            view["constraints"].append(content["limitations"])
        self._collect_unknowns(content, "content", view)

        resolved_context = None
        resolved_scope = None
        for key, kind in (("target_ref","target"),("claim_ref","claim"),("source_ref","source"),
                          ("basis_ref","basis"),("decision_ref","decision"),("context_ref","context"),("scope_ref","scope")):
            ref = content.get(key)
            self._add_trace(view, ref)
            target = self._resolve(ref, by_key)
            if key == "context_ref" or key == "scope_ref":
                if target:
                    tc = target.get("content") or {}
                    payload = tc.get(f"{kind}_content", tc)
                    resolved = {"type": kind, "record_id": target["record_id"], "version": target["record_version"], "content": payload}
                    if key == "context_ref":
                        resolved_context = resolved
                    else:
                        resolved_scope = resolved
                elif isinstance(ref, dict):
                    view["unknown"].append({"field": key, "status": "unresolved", "label": _label("unresolved")})

        for key in ("premises","refs"):
            refs = content.get(key)
            if isinstance(refs, list):
                for ref in refs:
                    self._add_trace(view, ref)

        view["applicability"]["context"] = resolved_context
        view["applicability"]["scope"] = resolved_scope
        if resolved_context or resolved_scope:
            view["applicability"]["basis"] = {
                "record_context": bool(resolved_context), "record_scope": bool(resolved_scope),
                "current_user_context": False,
            }
            if resolved_context and resolved_scope:
                view["applicability"]["reason"] = (
                    "Context и Scope записи разрешены, но текущий пользовательский Context не задан; "
                    "текущая применимость остаётся неустановленной."
                )

        if record["record_type"] == "action":
            view["constraints"].append("Action не является текущей инструкцией без установленной применимости к текущему Context и Scope.")
        if record["record_type"] == "decision":
            view["constraints"].append("Decision описывает решение и его основания; он не превращается автоматически в универсальную рекомендацию.")
        if content.get("causal_attribution", {}).get("mode") == "not_attributed":
            view["constraints"].append("Причинная связь в этой записи не установлена.")

        if mode == "VERIFY":
            view["safety"]["verification_required"] = True
        elif mode == "ACT":
            view["safety"]["action_gate"] = "not_established_without_current_context"
        elif mode == "CHECK":
            view["safety"]["result_requires_observation"] = True
        elif mode == "RECOVER":
            view["safety"]["missing_data_must_remain_explicit"] = True
        return view

def build_human_view(query: QueryInterface, record_id: str, version: str | None = None, mode: str = "UNDERSTAND") -> dict[str, Any]:
    return HumanView(query).build(record_id, version, mode)
