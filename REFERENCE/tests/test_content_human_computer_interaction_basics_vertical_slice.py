from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "human-computer-interaction-basics" / "records"
SOURCE_URI = "https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design"

def test_human_computer_interaction_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"]: r for r in records if r["record_type"] == "source"}
    assert len(sources) == 1
    source = sources["SRC-HUMAN_COMPUTER_INTERACTION_BASICS"]
    assert source["record_version"] == "2"
    assert source["content"]["source_identity"] == "National Institute of Standards and Technology (NIST), Human Centered Design (HCD)"
    assert source["content"]["external_ref"]["uri"] == SOURCE_URI
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(claims) == 3
    assert all(c["record_version"] == "2" for c in claims.values())
    for claim in claims.values():
        assert claim["provenance"]["created_from"] == [{"record_id": source["record_id"], "version": "2"}]
        assert any(e["content"]["claim_ref"] == {"record_id": claim["record_id"], "version": "2"} and e["content"]["source_ref"] == {"record_id": source["record_id"], "version": "2"} for e in evidence)
    descriptions = {e["record_id"]: e["content"]["material"]["description"] for e in evidence}
    assert all(e["record_version"] == "2" for e in evidence)
    assert "не устанавливает напрямую" in descriptions["EU-HUMAN_COMPUTER_INTERACTION_BASICS-A"]
    assert "не обновляемая" in descriptions["EU-HUMAN_COMPUTER_INTERACTION_BASICS-B"]
    assert "Evaluating the Design" in descriptions["EU-HUMAN_COMPUTER_INTERACTION_BASICS-C"]
    context = next(r for r in records if r["record_type"] == "context")
    scope = next(r for r in records if r["record_type"] == "scope")
    assert context["record_version"] == "2" and context["content"]["target_ref"]["version"] == "2"
    assert scope["record_version"] == "2" and scope["content"]["target_ref"]["version"] == "2"
