from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def test_adversarial_full_corpus_is_schema_and_semantically_clean():
    rs = records()
    assert len(rs) == 2547
    assert len({r["record_id"] for r in rs}) == 2547
    validator = Validator(SCHEMA)
    for r in rs:
        result = validator.validate(r)
        assert result.passed, (r["record_id"], [(f.code, f.message) for f in result.findings])
    assert validate_semantic_dataset(rs) == []


def test_adversarial_every_claim_has_source_and_evidence_path():
    rs = records()
    by_id = {r["record_id"]: r for r in rs}
    claims = [r for r in rs if r["record_type"] == "claim"]
    evidence = [r for r in rs if r["record_type"] == "evidence_use"]
    for claim in claims:
        assert claim.get("provenance", {}).get("created_from"), claim["record_id"]
        links = [e for e in evidence if e.get("content", {}).get("claim_ref", {}).get("record_id") == claim["record_id"]]
        assert links, claim["record_id"]
        for e in links:
            source_id = e["content"]["source_ref"]["record_id"]
            assert by_id[source_id]["record_type"] == "source"


def test_adversarial_cross_slice_relations_do_not_reference_relations_as_participants():
    rs = records()
    relation_ids = {r["record_id"] for r in rs if r["record_type"] == "relation"}
    for relation in (r for r in rs if r["record_id"].startswith("REL-CROSS-")):
        assert all(p["record_id"] not in relation_ids for p in relation["content"]["participants"])


def test_adversarial_new_slices_use_existing_types_only():
    allowed = {"record","claim","source","evidence_use","assessment","inference","decision","action","event","result","state","process","relation","identity","context","scope","provenance","authorship_contribution","trust_reputation"}
    for slug in ("algebra-basics", "geometry-basics", "trigonometry-basics", "calculus-basics", "linear-algebra-basics", "number-theory-basics", "combinatorics-basics", "numerical-methods-basics", "measurement-uncertainty-basics", "scientific-method-basics", "hydrology-basics", "meteorology-basics", "volcanology-basics", "seismology-basics", "paleontology-basics", "geomorphology-basics", "mineralogy-basics", "petrology-basics", "atmospheric-science-basics", "remote-sensing-basics", "zoology-basics", "conservation-biology-basics", "developmental-biology-basics", "virology-basics", "parasitology-basics", "microbiome-basics", "behavioral-biology-basics", "plant-physiology-basics", "biodiversity-basics", "ecophysiology-basics", "databases-basics", "programming-languages-basics", "software-engineering-basics", "cybersecurity-basics", "cryptography-basics", "human-computer-interaction-basics", "distributed-systems-basics", "cloud-computing-basics", "computer-architecture-basics", "artificial-intelligence-basics", "accounting-basics", "macroeconomics-basics", "microeconomics-basics", "finance-basics", "organizational-behavior-basics", "education-science-basics", "public-administration-basics", "demographic-methods-basics", "urban-planning-basics", "history-methods-basics", "game-theory-basics", "optimization-basics", "control-systems-basics", "compiler-basics", "signal-processing-basics", "metrology-basics", "queueing-theory-basics", "graph-theory-basics", "formal-methods-basics", "software-testing-basics", "statistics-basics", "thermodynamics-basics", "optics-basics", "quantum-physics-basics", "astronomy-basics", "geophysics-basics", "neuroscience-basics", "archaeology-basics", "art-history-basics", "music-theory-basics"):
        files = list((CONTENT / slug / "records").glob("*.json"))
        assert len(files) == 9
        assert {json.loads(p.read_text(encoding="utf-8"))["record_type"] for p in files} <= allowed


def test_adversarial_core_reference_targets_resolve():
    rs = records()
    ids = {r["record_id"] for r in rs}
    for r in rs:
        content = r.get("content", {})
        for key in ("claim_ref","source_ref","target_ref","context_ref","scope_ref","decision_ref"):
            ref = content.get(key)
            if isinstance(ref, dict) and "record_id" in ref:
                assert ref["record_id"] in ids, (r["record_id"], key, ref)
