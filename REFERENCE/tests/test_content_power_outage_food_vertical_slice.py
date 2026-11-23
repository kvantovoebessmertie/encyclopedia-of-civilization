from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "power-outage-food" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_power_outage_food_slice_validates():
    records = _records()
    assert len(records) == 24
    validator = Validator(SCHEMA)
    assert all(validator.validate(record).passed for record in records)
    assert validate_semantic_dataset(records) == []


def test_power_outage_food_publication_preserves_evidence(tmp_path):
    records = _records()
    report = build_content_package(
        records,
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="power-outage-food-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    claims = [entry for entry in publication["entries"] if entry["record_type"] == "claim"]
    assert len(claims) == 5
    assert all(entry["evidence"] for entry in claims)
    assert publication["citations_preserved"] is True


def test_power_outage_food_human_view_boundary_is_evidenced():
    records = _records()
    claims = {r["record_id"]: r for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert claims["CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY"]["scope"]["record_id"] == "SCP-FOOD-POWER-OUTAGE"
    assert any(e["content"]["claim_ref"]["record_id"] == "CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY" and e["content"]["source_ref"]["record_id"] == "SRC-FDA-POWER-OUTAGE-2026" for e in evidence)

def test_food_target_temperature_has_direct_fda_freezer_locator():
    records=_records()
    by_id={r["record_id"]:r for r in records}
    source=by_id["SRC-FDA-POWER-OUTAGE-FLOODS-2026"]
    evidence=by_id["EU-FOOD-TARGET-TEMP-FDA-FREEZER-0F"]
    assert source["content"]["external_ref"]["uri"] == "https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods"
    assert source["content"]["external_ref"]["locator"] == "Prepare Yourself Before Power Emergencies"
    assert evidence["content"]["claim_ref"] == {"record_id":"CLM-FOOD-TARGET-TEMP","version":"1"}
    assert evidence["content"]["source_ref"] == {"record_id":"SRC-FDA-POWER-OUTAGE-FLOODS-2026","version":"1"}
    assert "0 °F" in evidence["content"]["material"]["description"]
