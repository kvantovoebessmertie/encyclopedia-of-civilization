import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/wastewater-treatment-basics")
def test_content_wastewater_treatment_basics_vertical_slice():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    assert len(records)==11
    types=[r["record_type"] for r in records]
    assert types.count("source")==2
    assert types.count("claim")==3
    assert types.count("evidence_use")==4
    assert types.count("context")==1
    assert types.count("scope")==1
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}

def test_wastewater_treatment_has_epa_primer_edge():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    by_id={r["record_id"]:r for r in records}
    source=by_id["SRC-EPA-WASTEWATER-PRIMER-2015"]
    evidence=by_id["EU-WASTEWATER-TREATMENT-BASICS-A-EPA-PRIMER"]
    assert source["content"]["external_ref"]["uri"] == "https://www.epa.gov/sites/production/files/2015-09/documents/primer.pdf"
    assert source["content"]["external_ref"]["locator"] == "Basic Wastewater Treatment Processes, printed page 10: Physical; Biological; Chemical"
    assert evidence["content"]["claim_ref"] == {"record_id":"CLM_WASTEWATER_TREATMENT_BASICS_A","version":"1"}
    assert evidence["content"]["source_ref"] == {"record_id":"SRC-EPA-WASTEWATER-PRIMER-2015","version":"1"}
