from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"emergency-alert-warning"/"records"
def test_emergency_alert_warning_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==10
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    ids={r["record_id"] for r in records}
    assert {"CLM-IPAWS-ALERT-CONTENT","CLM-IPAWS-ALERT-ELEMENTS"}<=ids
