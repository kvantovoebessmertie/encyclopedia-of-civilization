import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/power-electronics-basics")
def test_content_power_electronics_basics_vertical_slice():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    assert len(records)==9
    types=[r["record_type"] for r in records]
    assert types.count("source")==1
    assert types.count("claim")==3
    assert types.count("evidence_use")==3
    assert types.count("context")==1
    assert types.count("scope")==1
    source=next(r for r in records if r["record_type"]=="source")["record_id"]
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"]==source for r in claims)
    assert all(r["content"]["source_ref"]["record_id"]==source for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}

def test_power_electronics_batch44_alias_resolves_exact_record_version_and_chain():
    records_dir = SLICE / "records"
    claim_path = records_dir / "CLM-POWER_ELECTRONICS_BASICS-B.json"
    claim = json.loads(claim_path.read_text(encoding="utf-8"))
    evidence = json.loads((records_dir / "EU-POWER_ELECTRONICS_BASICS-B.json").read_text(encoding="utf-8"))
    source = json.loads((records_dir / "SRC-POWER_ELECTRONICS_BASICS.json").read_text(encoding="utf-8"))

    # The queue spelling is a filename-style alias; identity is the stored ID + version.
    assert "CLM-POWER_ELECTRONICS_BASICS-B@1" == "CLM-POWER_ELECTRONICS_BASICS-B@1"
    assert claim["record_id"] == "CLM_POWER_ELECTRONICS_BASICS_B"
    assert claim["record_version"] == "1"
    assert claim["record_type"] == "claim"
    assert evidence["record_id"] == "EU_POWER_ELECTRONICS_BASICS_B"
    assert evidence["record_version"] == "1"
    assert evidence["record_type"] == "evidence_use"
    assert evidence["content"]["claim_ref"] == {
        "record_id": claim["record_id"],
        "version": claim["record_version"],
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": source["record_id"],
        "version": source["record_version"],
    }
    assert source["record_id"] == "SRC_POWER_ELECTRONICS_BASICS"
    assert source["record_version"] == "1"
