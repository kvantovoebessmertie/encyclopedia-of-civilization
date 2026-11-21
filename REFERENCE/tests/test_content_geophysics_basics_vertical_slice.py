from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "geophysics-basics" / "records"


def load(record_id: str) -> dict:
    return json.loads((SLICE / f"{record_id}.json").read_text(encoding="utf-8"))


def test_geophysics_basics_slice_resolves_all_claim_evidence_and_sources():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 10
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"] for r in records if r["record_type"] == "claim"}
    evidence = [r for r in records if r["record_type"] == "evidence_use"]
    assert len(sources) == 2
    assert len(claims) == 3
    assert len(evidence) == 3
    for claim_id in claims:
        assert any(e["content"]["claim_ref"]["record_id"] == claim_id and e["content"]["source_ref"]["record_id"] in sources for e in evidence)


def test_geophysics_claim_c_has_exact_usgs_project_locator_and_scope_limit():
    source = load("SRC-USGS-GEOPHYSICAL-MAPPING-SOUTHERN-MIDCONTINENT")
    evidence = load("EU-GEOPHYSICS_BASICS-C")
    assert source["record_version"] == "1"
    assert source["content"]["external_ref"]["uri"].startswith("https://www.usgs.gov/centers/gggsc/science/geophysical-mapping-geologic-systems-host-critical-mineral-deposits-southern")
    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {"record_id": "CLM-GEOPHYSICS_BASICS-C", "version": "1"}
    assert evidence["content"]["source_ref"] == {"record_id": source["record_id"], "version": "1"}
    assert evidence["provenance"]["created_from"] == [{"record_id": source["record_id"], "version": "1"}]
    description = evidence["content"]["material"]["description"].casefold()
    for term in ["airborne", "ground", "models", "drill-core", "not a universal workflow"]:
        assert term in description
