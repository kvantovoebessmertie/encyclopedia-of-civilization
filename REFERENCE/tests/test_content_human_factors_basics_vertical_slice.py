from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "human-factors-basics"
RECORDS = SLICE / "records"


def test_human_factors_basics_slice_is_complete_and_source_bounded():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in RECORDS.glob("*.json")]
    assert len(records) == 9
    assert {r["record_type"] for r in records} >= {"source", "claim", "evidence_use", "context", "scope"}

    by_id = {r["record_id"]: r for r in records}
    source = by_id["SRC-HUMAN_FACTORS_BASICS"]
    assert source["content"]["source_identity"] == "NASA Johnson Space Center — Human Factors & Performance"
    assert source["content"]["external_ref"]["uri"] == "https://www.nasa.gov/reference/jsc-human-factors-performance/"

    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(claims) == 3 and len(evidence) == 3
    assert all(r["provenance"]["created_from"][0]["record_id"] == source["record_id"] for r in claims)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence} == {r["record_id"] for r in claims}
    assert all(r["content"]["source_ref"]["record_id"] == source["record_id"] for r in evidence)
    assert all(r["content"]["evidence_role"] == "supports" for r in evidence)

    claim_text = {r["record_id"]: r["content"]["statement"] for r in claims}
    assert "возможности и ограничения человека" in claim_text["CLM-HUMAN_FACTORS_BASICS-A"]
    assert all(term in claim_text["CLM-HUMAN_FACTORS_BASICS-B"] for term in ("рабочая нагрузка", "утомление", "человеческие ошибки"))
    assert all(term in claim_text["CLM-HUMAN_FACTORS_BASICS-C"] for term in ("проектирования, разработки и эксплуатации", "Интеграция человеческих систем"))

    descriptions = {r["record_id"]: r["content"]["material"]["description"] for r in evidence}
    assert len(set(descriptions.values())) == 3
    assert "дисплеи, органы управления, рабочие места" in descriptions["EU-HUMAN_FACTORS_BASICS-A"]
    assert "потерю ситуационной осведомлённости" in descriptions["EU-HUMAN_FACTORS_BASICS-B"]
    assert "человека, оборудования и программного обеспечения" in descriptions["EU-HUMAN_FACTORS_BASICS-C"]

    readme = (SLICE / "README.md").read_text(encoding="utf-8")
    assert "Человеческий фактор рассматривает" in readme
    assert "иллюстративный пример" in readme
    assert "не универсальный стандарт" in readme
    assert "не сертифицирует интерфейс" in readme
    for suffix in ("A", "B", "C"):
        assert f"records/CLM-HUMAN_FACTORS_BASICS-{suffix}.json" in readme
        assert f"records/EU-HUMAN_FACTORS_BASICS-{suffix}.json" in readme
    assert "records/SRC-HUMAN_FACTORS_BASICS.json" in readme
