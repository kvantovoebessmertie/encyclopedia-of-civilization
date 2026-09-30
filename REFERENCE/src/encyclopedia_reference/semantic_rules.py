from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class SemanticRule:
    rule_id: str
    owner: str
    family: str
    status: str = "ENFORCED"


# Stable machine-facing rule registry. Context-dependent rules are enforced
# only when their explicit machine representation is present; otherwise they
# remain non-applicable rather than being guessed.
RULES = (
    SemanticRule("CTX_INHERIT_001", "L4", "context.inheritance"),
    SemanticRule("CTX_PRECEDENCE_001", "L4", "context.precedence"),
    SemanticRule("CTX_CONFLICT_001", "L4", "context.conflict"),
    SemanticRule("CTX_TRANSFER_001", "L4/L5", "context.transferability"),
    SemanticRule("CTX_FIDELITY_001", "L5", "context.fidelity"),
    SemanticRule("CTX_DIMENSION_001", "L4", "context.dimension_dependency"),
    SemanticRule("SCOPE_QUANT_001", "L4", "scope.quantifier"),
    SemanticRule("SCOPE_TUPLE_001", "L4", "scope.multidimensional"),
    SemanticRule("SCOPE_TRANSFER_001", "L4/L5", "scope.transferability"),
    SemanticRule("PROV_TYPE_001", "L4", "provenance.relation_type"),
    SemanticRule("PROV_CYCLE_001", "L4", "provenance.cycle"),
    SemanticRule("PROV_INDEPENDENCE_001", "L4/L5", "provenance.independence"),
    SemanticRule("PROV_FIDELITY_001", "L5", "provenance.fidelity"),
    SemanticRule("AUTH_ROLE_001", "L4", "authorship.role"),
    SemanticRule("AUTH_PSEUDONYM_001", "L4", "authorship.pseudonym"),
    SemanticRule("AUTH_CONFLICT_001", "L4", "authorship.conflict"),
    SemanticRule("AUTH_HISTORY_001", "L5", "authorship.history"),
    SemanticRule("TRUST_GOAL_001", "L4", "trust.goal"),
    SemanticRule("TRUST_CYCLE_001", "L4", "trust.cycle"),
    SemanticRule("TRUST_INDEPENDENCE_001", "L4/L5", "trust.independence"),
    SemanticRule("TRUST_HISTORY_001", "L5", "trust.history"),
    SemanticRule("TRUST_TRANSFER_001", "L5", "trust.transferability"),
    SemanticRule("TRUST_AGGREGATION_001", "L5", "trust.aggregation"),
)


def registry() -> dict[str, dict[str, str]]:
    return {
        r.rule_id: {"owner": r.owner, "family": r.family, "status": r.status}
        for r in RULES
    }


def _finding(code: str, layer: str, message: str, subject: str | None = None):
    # Imported lazily to avoid a module cycle at import time.
    from .validator import Finding
    return Finding(code, "error", layer, message, subject=subject, rule=code)


def _ref_key(ref: Any) -> tuple[str, str | None] | None:
    if not isinstance(ref, dict) or not isinstance(ref.get("record_id"), str):
        return None
    return ref["record_id"], ref.get("version")


def _time_bounds(record: dict[str, Any]) -> tuple[datetime | None, datetime | None]:
    value = record.get("valid_time")
    if not isinstance(value, dict):
        return None, None
    start = value.get("start")
    end = value.get("end")
    def parse(v: Any) -> datetime | None:
        if not isinstance(v, str):
            return None
        try:
            return datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            return None
    return parse(start), parse(end)


def _overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    a0, a1 = _time_bounds(a)
    b0, b1 = _time_bounds(b)
    if a0 is None or b0 is None:
        # Without a complete temporal frame, conflict cannot be established.
        return False
    a1 = a1 or datetime.max.replace(tzinfo=a0.tzinfo)
    b1 = b1 or datetime.max.replace(tzinfo=b0.tzinfo)
    return max(a0, b0) <= min(a1, b1)


def _walk_refs(value: Any, path: str = ""):
    if isinstance(value, dict):
        if isinstance(value.get("record_id"), str):
            yield path, value
            return
        for key, child in value.items():
            if key == "extensions":
                continue
            yield from _walk_refs(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from _walk_refs(child, f"{path}[{i}]")


def _graph_cycle(edges: dict[str, set[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for child in edges.get(node, set()):
            if visit(child):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(n) for n in edges)


def validate_semantic_dataset(records: list[dict[str, Any]]) -> list:
    findings = []
    by_id = {r.get("record_id"): r for r in records if isinstance(r.get("record_id"), str)}

    # Context: explicit inheritance/precedence/conflict/transfer/fidelity controls.
    context_edges: dict[str, set[str]] = {}
    contexts = [r for r in records if r.get("record_type") == "context"]
    for record in contexts:
        content = record.get("content", {})
        cc = content.get("context_content", {}) if isinstance(content, dict) else {}
        if not isinstance(cc, dict):
            continue
        inheritance = cc.get("inheritance")
        if inheritance is not None:
            parents = inheritance.get("parent_refs", []) if isinstance(inheritance, dict) else []
            for parent in parents if isinstance(parents, list) else []:
                key = _ref_key(parent)
                if key:
                    context_edges.setdefault(record["record_id"], set()).add(key[0])
                    if key[0] not in by_id:
                        findings.append(_finding("CTX_INHERIT_001", "L4", "parent Context не разрешается", record["record_id"]))
            if isinstance(inheritance, dict) and inheritance.get("effective") is not None and not isinstance(inheritance.get("effective"), dict):
                findings.append(_finding("CTX_INHERIT_001", "L4", "effective Context должен быть объектом", record["record_id"]))
        precedence = cc.get("precedence")
        if precedence is not None and not isinstance(precedence, (int, float)):
            findings.append(_finding("CTX_PRECEDENCE_001", "L4", "precedence должен быть числом", record["record_id"]))
        transfer = cc.get("transferability")
        if isinstance(transfer, dict) and transfer.get("status") in {"transferable", "conditional", "partial"} and not transfer.get("basis_refs"):
            findings.append(_finding("CTX_TRANSFER_001", "L4", "положительная transferability требует basis_refs", record["record_id"]))
        fidelity = cc.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("CTX_FIDELITY_001", "L5", "потеря Context Fidelity должна быть зафиксирована", record["record_id"]))
        deps = cc.get("dimension_dependencies")
        if deps is not None and not isinstance(deps, list):
            findings.append(_finding("CTX_DIMENSION_001", "L4", "dimension_dependencies должен быть списком", record["record_id"]))

    if _graph_cycle(context_edges):
        findings.append(_finding("CTX_INHERIT_001", "L4", "обнаружен цикл наследования Context"))

    for i, left in enumerate(contexts):
        for right in contexts[i + 1:]:
            lc, rc = left.get("content", {}), right.get("content", {})
            if not isinstance(lc, dict) or not isinstance(rc, dict):
                continue
            if _ref_key(lc.get("target_ref")) != _ref_key(rc.get("target_ref")):
                continue
            if not _overlap(left, right):
                continue
            lv = lc.get("context_content", {})
            rv = rc.get("context_content", {})
            if isinstance(lv, dict) and isinstance(rv, dict):
                common = set(lv) & set(rv) - {"inheritance", "precedence", "transferability", "fidelity", "dimension_dependencies"}
                if any(lv[k] != rv[k] for k in common):
                    lp = lv.get("precedence")
                    rp = rv.get("precedence")
                    if lp == rp:
                        findings.append(_finding("CTX_CONFLICT_001", "L4", "конфликт Context без однозначного precedence", left.get("record_id")))

    # Provenance graph: cycles are invalid; common roots do not become independence.
    prov_edges: dict[str, set[str]] = {}
    for record in records:
        p = record.get("provenance")
        if not isinstance(p, dict):
            continue
        source = record.get("record_id")
        if not isinstance(source, str):
            continue
        for key in ("created_from", "transformed_from"):
            for ref in p.get(key, []) if isinstance(p.get(key), list) else []:
                k = _ref_key(ref)
                if k:
                    prov_edges.setdefault(source, set()).add(k[0])
    if _graph_cycle(prov_edges):
        findings.append(_finding("PROV_CYCLE_001", "L4", "обнаружен цикл provenance lineage"))
    for record in records:
        p = record.get("provenance")
        if isinstance(p, dict) and p.get("independent") is True and (p.get("created_from") or p.get("transformed_from")):
            findings.append(_finding("PROV_INDEPENDENCE_001", "L4", "зависимое происхождение не может быть помечено как независимое", record.get("record_id")))

    # Authorship: role boundaries are explicit and history cannot be overwritten.
    for record in records:
        if record.get("record_type") != "authorship_contribution":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if c.get("attribution_status") == "disputed" and c.get("confirmed") is True:
            findings.append(_finding("AUTH_CONFLICT_001", "L4", "disputed attribution не может быть одновременно confirmed", record.get("record_id")))
        if c.get("contributor_kind") == "pseudonymous" and c.get("resolved_person_ref"):
            findings.append(_finding("AUTH_PSEUDONYM_001", "L4", "pseudonym не должен молча становиться resolved person", record.get("record_id")))
        if c.get("tool_use") is True and c.get("contribution") == "author":
            findings.append(_finding("AUTH_ROLE_001", "L4", "использование инструмента не является автоматически авторством", record.get("record_id")))

    # Trust/Reputation: explicit goal/subject, no cycles, no aggregation-to-truth.
    trust_edges: dict[str, set[str]] = {}
    for record in records:
        if record.get("record_type") != "trust_reputation":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        subject = _ref_key(c.get("subject_ref"))
        if subject and isinstance(record.get("record_id"), str):
            trust_edges.setdefault(record["record_id"], set()).add(subject[0])
        if c.get("assessment_type") in {"trust", "trust_assessment"}:
            if not _ref_key(c.get("subject_ref")):
                findings.append(_finding("TRUST_GOAL_001", "L4", "Trust требует subject_ref", record.get("record_id")))
            if not _ref_key(c.get("goal_ref")):
                findings.append(_finding("TRUST_GOAL_001", "L4", "Trust требует goal_ref", record.get("record_id")))
        if c.get("aggregation") and c.get("truth") is True:
            findings.append(_finding("TRUST_AGGREGATION_001", "L5", "агрегация Trust/Reputation не доказывает truth", record.get("record_id")))
        if c.get("transferability") == "universal":
            findings.append(_finding("TRUST_TRANSFER_001", "L5", "Trust не переносится универсально без явного основания", record.get("record_id")))
    if _graph_cycle(trust_edges):
        findings.append(_finding("TRUST_CYCLE_001", "L4", "обнаружен цикл Trust/Reputation"))

    # Cross-cutting anti-inference.
    for record in records:
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if record.get("publication_status") == "published" and c.get("truth") is True:
            findings.append(_finding("VAL-L4-PUBLICATION-TRUTH", "L4", "publication не доказывает truth", record.get("record_id")))
        if c.get("provenance_strength") == "independent" and c.get("created_from"):
            findings.append(_finding("PROV_INDEPENDENCE_001", "L4", "lineage dependency contradicts independence", record.get("record_id")))

    return findings
