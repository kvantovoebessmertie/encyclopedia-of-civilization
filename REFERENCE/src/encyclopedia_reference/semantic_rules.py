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
    SemanticRule("SCP_ROLE_001", "L4", "scope.semantic_role"),
    SemanticRule("SCP_TARGET_001", "L4", "scope.target"),
    SemanticRule("SCP_UNIVERSE_001", "L4", "scope.universe"),
    SemanticRule("SCP_QUANTIFIER_001", "L4", "scope.quantifier_preservation"),
    SemanticRule("SCP_LEVEL_001", "L4", "scope.analysis_level"),
    SemanticRule("SCP_EPISTEMIC_001", "L4", "scope.epistemic_status"),
    SemanticRule("SCP_APPLICABILITY_001", "L4", "scope.applicability"),
    SemanticRule("SCP_UNKNOWN_001", "L4", "scope.unknown_discipline"),
    SemanticRule("SCP_CLOSURE_001", "L4", "scope.closure"),
    SemanticRule("SCP_OPENWORLD_001", "L4", "scope.open_world"),
    SemanticRule("SCP_BOUNDARY_001", "L4", "scope.boundary"),
    SemanticRule("SCP_FUZZY_001", "L4/L5", "scope.fuzzy_boundary"),
    SemanticRule("SCP_MEMBERSHIP_001", "L4", "scope.membership_status"),
    SemanticRule("SCP_DIMENSION_COUPLING_001", "L4/L5", "scope.dimension_coupling"),
    SemanticRule("SCP_TUPLE_001", "L5", "scope.tuple_integrity"),
    SemanticRule("SCP_TEMPORAL_001", "L5", "scope.temporal_role"),
    SemanticRule("SCP_TRANSFER_BASIS_001", "L4/L5", "scope.transfer_basis"),
    SemanticRule("SCP_OVERLAP_001", "L4", "scope.overlap"),
    SemanticRule("SCP_MISMATCH_001", "L4", "scope.mismatch"),
    SemanticRule("SCP_INHERIT_COMPAT_001", "L4/L5", "scope.inheritance_compatibility"),
    SemanticRule("SCP_DERIVED_001", "L5", "scope.derived_scope"),
    SemanticRule("SCP_PROVENANCE_001", "L4/L5", "scope.provenance"),
    SemanticRule("SCP_FIDELITY_001", "L5", "scope.fidelity_preservation"),
    SemanticRule("SCP_COMPOSITION_001", "L5", "scope.composition"),
    SemanticRule("SCP_ROLE_DRIFT_001", "L5", "scope.role_drift"),
    SemanticRule("ID_FRAME_001", "L4", "identity.frame"),
    SemanticRule("ID_CRITERION_001", "L4", "identity.criterion"),
    SemanticRule("ID_SCOPE_001", "L4", "identity.scope"),
    SemanticRule("ID_UNCERTAINTY_001", "L4/L5", "identity.uncertainty"),
    SemanticRule("ID_SIMILARITY_001", "L4", "identity.similarity"),
    SemanticRule("ID_ALIAS_001", "L4", "identity.alias"),
    SemanticRule("ID_HISTORY_001", "L5", "identity.history"),
    SemanticRule("CTX_INHERIT_001", "L4", "context.inheritance"),
    SemanticRule("CTX_PRECEDENCE_001", "L4", "context.precedence"),
    SemanticRule("CTX_CONFLICT_001", "L4", "context.conflict"),
    SemanticRule("CTX_TRANSFER_001", "L4/L5", "context.transferability"),
    SemanticRule("CTX_FIDELITY_001", "L5", "context.fidelity"),
    SemanticRule("CTX_DIMENSION_001", "L4", "context.dimension_dependency"),
    SemanticRule("CTX_ROLE_001", "L4", "context.semantic_role"),
    SemanticRule("CTX_ASSUMPTION_001", "L4", "context.assumption"),
    SemanticRule("CTX_TRANSFER_CONFLICT_001", "L4/L5", "context.transfer_conflict"),
    SemanticRule("SCOPE_QUANT_001", "L4", "scope.quantifier"),
    SemanticRule("SCOPE_TUPLE_001", "L4", "scope.multidimensional"),
    SemanticRule("SCOPE_TRANSFER_001", "L4/L5", "scope.transferability"),
    SemanticRule("SCOPE_SAMPLE_POP_001", "L4", "scope.sample_population"),
    SemanticRule("SCOPE_INHERIT_001", "L4/L5", "scope.inheritance"),
    SemanticRule("SCOPE_MEMBERSHIP_PROV_001", "L4", "scope.membership_provenance"),
    SemanticRule("SCOPE_FIDELITY_001", "L5", "scope.fidelity"),
    SemanticRule("SCOPE_HISTORY_001", "L5", "scope.history"),
    SemanticRule("SCOPE_ALGEBRA_001", "L4", "scope.algebra"),
    SemanticRule("PROV_TYPE_001", "L4", "provenance.relation_type"),
    SemanticRule("PROV_CYCLE_001", "L4", "provenance.cycle"),
    SemanticRule("PROV_INDEPENDENCE_001", "L4/L5", "provenance.independence"),
    SemanticRule("PROV_FIDELITY_001", "L5", "provenance.fidelity"),
    SemanticRule("PROV_SCOPE_001", "L4", "provenance.component_scope"),
    SemanticRule("PROV_OPERATION_001", "L4", "provenance.operation_semantics"),
    SemanticRule("PROV_JOINT_INPUT_001", "L4", "provenance.joint_inputs"),
    SemanticRule("AUTH_ROLE_001", "L4", "authorship.role"),
    SemanticRule("AUTH_PSEUDONYM_001", "L4", "authorship.pseudonym"),
    SemanticRule("AUTH_CONFLICT_001", "L4", "authorship.conflict"),
    SemanticRule("AUTH_HISTORY_001", "L5", "authorship.history"),
    SemanticRule("AUTH_TRANSLATION_001", "L4", "authorship.translation"),
    SemanticRule("AUTH_SYNTHESIS_001", "L4", "authorship.synthesis"),
    SemanticRule("AUTH_ORDER_001", "L4", "authorship.order_semantics"),
    SemanticRule("TRUST_GOAL_001", "L4", "trust.goal"),
    SemanticRule("TRUST_CYCLE_001", "L4", "trust.cycle"),
    SemanticRule("TRUST_INDEPENDENCE_001", "L4/L5", "trust.independence"),
    SemanticRule("TRUST_HISTORY_001", "L5", "trust.history"),
    SemanticRule("TRUST_TRANSFER_001", "L5", "trust.transferability"),
    SemanticRule("TRUST_AGGREGATION_001", "L5", "trust.aggregation"),
    SemanticRule("TRUST_REPUTATION_SIGNAL_001", "L4", "trust.signal"),
    SemanticRule("TRUST_AUTHORITY_001", "L5", "trust.authority"),
    SemanticRule("TRUST_EASY_CASES_001", "L5", "trust.selection_bias"),
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

    # Identity: explicit safeguards prevent names/similarity/aliases from silently
    # becoming resolved identity, and require material frame/criterion/scope.
    for record in records:
        if record.get("record_type") not in {"identity", "identity_assertion", "relation", "claim"}:
            continue
        rid = record.get("record_id")
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        ident = c.get("identity") if isinstance(c.get("identity"), dict) else c
        if not isinstance(ident, dict):
            continue
        if ident.get("assertion") is True and ident.get("resolved") is True and not ident.get("frame_ref"):
            findings.append(_finding("ID_FRAME_001", "L4", "resolved identity requires resolvable frame_ref", rid))
        if ident.get("judgment") is True and ident.get("resolved") is True and not ident.get("criterion"):
            findings.append(_finding("ID_CRITERION_001", "L4", "resolved identity requires explicit criterion", rid))
        if ident.get("judgment") is True and not ident.get("scope"):
            findings.append(_finding("ID_SCOPE_001", "L4", "identity judgment requires explicit scope", rid))
        if ident.get("status") in {"possible", "probable", "disputed", "uncertain"} and ident.get("resolved") is True:
            findings.append(_finding("ID_UNCERTAINTY_001", "L4/L5", "uncertain identity cannot be represented as resolved", rid))
        if ident.get("similarity") is not None and ident.get("resolved") is True and ident.get("identity_basis") == "similarity":
            findings.append(_finding("ID_SIMILARITY_001", "L4", "similarity alone cannot establish identity", rid))
        if ident.get("alias") is True and ident.get("resolved") is True and not ident.get("alias_basis"):
            findings.append(_finding("ID_ALIAS_001", "L4", "alias-based identity requires explicit basis", rid))
        if ident.get("historical") is True and not (record.get("valid_time") or ident.get("history_ref")):
            findings.append(_finding("ID_HISTORY_001", "L5", "historical identity requires temporal or history reference", rid))

    # Scope representation-integrity guards. They fire only for explicit semantic
    # representations; absent optional semantics remain non-applicable.
    for record in records:
        if record.get("record_type") != "scope":
            continue
        rid = record.get("record_id")
        c0 = record.get("content", {})
        sc = c0.get("scope_content") if isinstance(c0, dict) else None
        if not isinstance(sc, dict):
            continue
        if sc.get("semantic_role_required") is True and not sc.get("semantic_role"):
            findings.append(_finding("SCP_ROLE_001","L4","material Scope role is required but absent",rid))
        if sc.get("material_target") is True and not _ref_key(sc.get("target_ref")):
            findings.append(_finding("SCP_TARGET_001","L4","material Scope target must resolve",rid))
        if sc.get("universe_required") is True and sc.get("universe_status") == "unknown" and sc.get("universe_fabricated") is True:
            findings.append(_finding("SCP_UNIVERSE_001","L4","unknown universe cannot be replaced by fabricated universe",rid))
        if sc.get("quantifier_required") is True and sc.get("quantifier") is None:
            findings.append(_finding("SCP_QUANTIFIER_001","L4","material quantifier must remain represented",rid))
        if sc.get("analysis_level_required") is True and sc.get("analysis_level") is None:
            findings.append(_finding("SCP_LEVEL_001","L4","material analysis level must remain represented",rid))
        if sc.get("epistemic_status") == "unknown" and sc.get("epistemic_resolved") is True:
            findings.append(_finding("SCP_EPISTEMIC_001","L4","unknown Scope epistemic status cannot be silently resolved",rid))
        if sc.get("applicability_status") == "proven" and sc.get("declared_only") is True:
            findings.append(_finding("SCP_APPLICABILITY_001","L4","declared Scope cannot be represented as proven applicability",rid))
        if sc.get("status") == "unknown" and sc.get("universal") is True:
            findings.append(_finding("SCP_UNKNOWN_001","L4","unknown Scope cannot become universal Scope",rid))
        if sc.get("closure_mode") == "closed" and not sc.get("closure_basis"):
            findings.append(_finding("SCP_CLOSURE_001","L4","closed Scope requires closure basis",rid))
        if sc.get("open_world") is False and sc.get("closure_justified") is not True:
            findings.append(_finding("SCP_OPENWORLD_001","L4","closed-world Scope requires explicit justification",rid))
        if sc.get("boundary_mode") == "exact" and sc.get("boundary_uncertain") is True:
            findings.append(_finding("SCP_BOUNDARY_001","L4","uncertain boundary cannot be silently represented as exact",rid))
        if sc.get("boundary_mode") == "crisp" and sc.get("fuzzy") is True and sc.get("fuzzy_basis") is None:
            findings.append(_finding("SCP_FUZZY_001","L4/L5","fuzzy Scope cannot become crisp without basis",rid))
        if sc.get("membership_status") == "unknown" and sc.get("membership_resolved") is True:
            findings.append(_finding("SCP_MEMBERSHIP_001","L4","unknown membership cannot be silently resolved",rid))
        if sc.get("dimensions_coupled") is True and sc.get("cartesian_product") is True and sc.get("coupling_basis") is None:
            findings.append(_finding("SCP_DIMENSION_COUPLING_001","L4/L5","coupled dimensions cannot be flattened to Cartesian product without basis",rid))
        if sc.get("tuple_semantics") is True and sc.get("tuple_values") is None:
            findings.append(_finding("SCP_TUPLE_001","L5","tuple/configuration semantics require tuple_values",rid))
        if sc.get("temporal_role") is None and sc.get("temporal_validity_material") is True:
            findings.append(_finding("SCP_TEMPORAL_001","L5","material temporal Scope requires temporal role",rid))
        if sc.get("transferability") in {"transferable","conditional","partial"} and not sc.get("transfer_basis_refs"):
            findings.append(_finding("SCP_TRANSFER_BASIS_001","L4/L5","positive Scope transferability requires basis",rid))
        if sc.get("overlap") is True and sc.get("equivalent") is True and sc.get("equivalence_basis") is None:
            findings.append(_finding("SCP_OVERLAP_001","L4","Scope overlap does not establish equivalence",rid))
        if sc.get("mismatch") is True and sc.get("contradiction") is True and sc.get("reconciliation_basis") is None:
            findings.append(_finding("SCP_MISMATCH_001","L4","Scope mismatch alone does not establish contradiction",rid))
        if sc.get("inherited") is True and sc.get("inheritance_compatible") is False:
            findings.append(_finding("SCP_INHERIT_COMPAT_001","L4/L5","incompatible Scope inheritance cannot be accepted",rid))
        if sc.get("derived") is True and sc.get("source_scope_ref") is None:
            findings.append(_finding("SCP_DERIVED_001","L5","derived Scope requires source Scope reference",rid))
        if sc.get("provenance_required") is True and not sc.get("provenance_ref"):
            findings.append(_finding("SCP_PROVENANCE_001","L4/L5","material Scope provenance must remain resolvable",rid))
        if sc.get("fidelity") == "lost" and not sc.get("losses"):
            findings.append(_finding("SCP_FIDELITY_001","L5","Scope fidelity loss must remain explicit",rid))
        if sc.get("composition") in {"union","intersection","projection","mapping"} and sc.get("composition_justified") is False:
            findings.append(_finding("SCP_COMPOSITION_001","L5","Scope composition requires justified semantics",rid))
        if sc.get("role_drift") is True and sc.get("role_drift_detected") is False:
            findings.append(_finding("SCP_ROLE_DRIFT_001","L5","Scope role drift must remain detectable",rid))

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

    # Scope: explicit quantifier/tuple/transfer controls are validated when represented.
    for record in records:
        if record.get("record_type") != "scope":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        sc = c.get("scope_content")
        if isinstance(sc, dict):
            quantifier = sc.get("quantifier")
            if quantifier is not None and quantifier not in {"all", "some", "none", "exactly", "at_least", "at_most", "unknown"}:
                findings.append(_finding("SCOPE_QUANT_001", "L4", "неизвестный quantifier Scope", record.get("record_id")))
            dimensions = sc.get("dimensions")
            if dimensions is not None and not isinstance(dimensions, list):
                findings.append(_finding("SCOPE_TUPLE_001", "L4", "multidimensional Scope dimensions должен быть списком", record.get("record_id")))
            if sc.get("transferability") == "universal":
                findings.append(_finding("SCOPE_TRANSFER_001", "L5", "Scope не переносится универсально без явного основания", record.get("record_id")))

    # Scope extension: explicit sample/population, inheritance, membership provenance,
    # fidelity, history and composition controls. Missing optional representations are
    # non-applicable; they are never inferred.
    scope_edges: dict[str, set[str]] = {}
    allowed_scope_ops = {"union", "intersection", "projection", "mapping", "inheritance", "transfer"}
    for record in records:
        if record.get("record_type") != "scope":
            continue
        rid = record.get("record_id")
        c = record.get("content", {})
        sc = c.get("scope_content") if isinstance(c, dict) else None
        if not isinstance(sc, dict):
            continue

        sample_pop = sc.get("sample_to_population")
        if sample_pop is True and not sc.get("basis_refs"):
            findings.append(_finding("SCOPE_SAMPLE_POP_001", "L4", "sample-to-population generalization requires basis_refs", rid))

        inheritance = sc.get("inheritance")
        if isinstance(inheritance, dict):
            parents = inheritance.get("parent_refs", [])
            if not isinstance(parents, list):
                findings.append(_finding("SCOPE_INHERIT_001", "L4", "Scope inheritance parent_refs must be a list", rid))
            else:
                for parent in parents:
                    key = _ref_key(parent)
                    if key:
                        scope_edges.setdefault(rid, set()).add(key[0])
                        if key[0] not in by_id:
                            findings.append(_finding("SCOPE_INHERIT_001", "L4", "Scope inheritance parent does not resolve", rid))

        membership_prov = sc.get("membership_provenance")
        if isinstance(membership_prov, dict) and membership_prov.get("status") in {"stated", "observed", "tested", "validated", "reported", "inferred", "modeled"} and not membership_prov.get("basis_refs"):
            findings.append(_finding("SCOPE_MEMBERSHIP_PROV_001", "L4", "membership provenance status requires basis_refs", rid))

        fidelity = sc.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("SCOPE_FIDELITY_001", "L5", "Scope Fidelity loss must be recorded", rid))

        if sc.get("historical") is True and not (record.get("valid_time") or sc.get("history_ref")):
            findings.append(_finding("SCOPE_HISTORY_001", "L5", "historical Scope requires temporal or history reference", rid))

        operation = sc.get("operation")
        if operation is not None:
            if operation not in allowed_scope_ops:
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "unknown Scope composition operation", rid))
            elif operation in {"union", "intersection"} and not isinstance(sc.get("operands"), list):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "union/intersection requires operands list", rid))
            elif operation == "projection" and not isinstance(sc.get("dimensions"), list):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "projection requires dimensions list", rid))
            elif operation == "mapping" and not _ref_key(sc.get("mapping_ref")):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "mapping requires mapping_ref", rid))

    if _graph_cycle(scope_edges):
        findings.append(_finding("SCOPE_INHERIT_001", "L4", "обнаружен цикл наследования Scope"))

    # Provenance graph: cycles are invalid; common roots do not become independence.
    prov_edges: dict[str, set[str]] = {}
    allowed_provenance_relations = {
        "derived_from", "transformed_from", "copied_from", "translated_from",
        "summarized_from", "extracted_from", "aggregated_from",
        "generated_from", "reconstructed_from", "compiled_from",
    }
    for record in records:
        p = record.get("provenance")
        if not isinstance(p, dict):
            continue
        source = record.get("record_id")
        if not isinstance(source, str):
            continue
        relation = p.get("relation")
        if relation is not None and relation not in allowed_provenance_relations:
            findings.append(_finding("PROV_TYPE_001", "L4", "неизвестный тип provenance relation", source))
        fidelity = p.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("PROV_FIDELITY_001", "L5", "потеря provenance fidelity должна быть зафиксирована", source))
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
        if c.get("historical_attribution") is True and not (c.get("attribution_time") or c.get("history_ref")):
            findings.append(_finding("AUTH_HISTORY_001", "L5", "historical attribution должна иметь временную или историческую привязку", record.get("record_id")))

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
        if c.get("independence_status") == "independent" and c.get("common_root_ref"):
            findings.append(_finding("TRUST_INDEPENDENCE_001", "L4", "общий root не совместим с заявленной независимостью без отдельного основания", record.get("record_id")))
        if c.get("historical") is True and not (record.get("valid_time") or c.get("assessment_time") or c.get("history_ref")):
            findings.append(_finding("TRUST_HISTORY_001", "L5", "historical Trust/Reputation должна иметь временную или историческую привязку", record.get("record_id")))
    if _graph_cycle(trust_edges):
        findings.append(_finding("TRUST_CYCLE_001", "L4", "обнаружен цикл Trust/Reputation"))

    # Additional explicit semantic-role safeguards. These trigger only when the
    # corresponding representation is explicit; absent fields remain non-applicable.
    for record in records:
        rid = record.get("record_id")
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if record.get("record_type") == "context":
            cc = c.get("context_content", {})
            if isinstance(cc, dict):
                if cc.get("semantic_role") == "cause" and cc.get("context_only") is True:
                    findings.append(_finding("CTX_ROLE_001", "L4", "Context-only representation cannot simultaneously assert causal role", rid))
                if cc.get("assumption") is True and cc.get("epistemic_status") == "observed":
                    findings.append(_finding("CTX_ASSUMPTION_001", "L4", "assumption cannot be silently represented as observed", rid))
                if cc.get("transferability") == "transferable" and cc.get("conflict") is True:
                    findings.append(_finding("CTX_TRANSFER_CONFLICT_001", "L4/L5", "conflicting Context cannot be declared unconditionally transferable", rid))
        p = record.get("provenance")
        if isinstance(p, dict):
            if p.get("component_scope") is True and not p.get("scope"):
                findings.append(_finding("PROV_SCOPE_001", "L4", "component-scoped provenance requires scope", rid))
            if p.get("relation") in {"translated_from", "copied_from", "summarized_from"} and p.get("operation_semantics") == "unknown" and p.get("specific_operation") is True:
                findings.append(_finding("PROV_OPERATION_001", "L4", "specific operation cannot be simultaneously marked unknown", rid))
            if p.get("joint_inputs") is True and not isinstance(p.get("input_group"), list):
                findings.append(_finding("PROV_JOINT_INPUT_001", "L4", "joint provenance requires input_group", rid))
        if record.get("record_type") == "authorship_contribution":
            if c.get("translation") is True and c.get("original_authorship") is True:
                findings.append(_finding("AUTH_TRANSLATION_001", "L4", "translation does not establish original authorship", rid))
            if c.get("synthesis") is True and c.get("source_authorship") is True:
                findings.append(_finding("AUTH_SYNTHESIS_001", "L4", "synthesis authorship does not establish source authorship", rid))
            if c.get("author_order_semantics") == "importance" and c.get("order_basis") is None:
                findings.append(_finding("AUTH_ORDER_001", "L4", "author order semantics requires explicit basis", rid))
        if record.get("record_type") == "trust_reputation":
            if c.get("signal") is True and c.get("established_fact") is True:
                findings.append(_finding("TRUST_REPUTATION_SIGNAL_001", "L4", "reputation signal is not automatically an established fact", rid))
            if c.get("authority") is True and c.get("truth") is True and not c.get("truth_basis"):
                findings.append(_finding("TRUST_AUTHORITY_001", "L5", "authority cannot by itself establish truth", rid))
            if c.get("easy_case_selection") is True and c.get("competence") == "high" and not c.get("selection_basis"):
                findings.append(_finding("TRUST_EASY_CASES_001", "L5", "high success on selected easy cases does not establish competence", rid))

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
