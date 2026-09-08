import json
from pathlib import Path

import tools.schemes as schemes_module
from tools.schemes import (
    check_scheme_eligibility,
    get_scheme_details,
    search_schemes,
)


def test_search_filters():
    education_andhra = json.loads(search_schemes("education", "Andhra Pradesh"))
    education_anywhere = json.loads(search_schemes("education", None))
    andhra_any_category = json.loads(search_schemes(None, "Andhra Pradesh"))
    all_schemes = json.loads(search_schemes(None, None))
    no_matches = json.loads(search_schemes("nonexistent", "Andhra Pradesh"))

    assert education_andhra
    assert education_anywhere
    assert andhra_any_category
    assert len(all_schemes) >= len(andhra_any_category)
    assert "message" in no_matches

    case_insensitive = json.loads(search_schemes("EDUCATION", "andhra pradesh"))
    assert len(case_insensitive) == len(education_andhra)
    assert {
        "scheme_id",
        "name",
        "category",
        "state",
        "description",
        "benefits",
        "source",
    } <= case_insensitive[0].keys()


def test_existing_scheme_tools_use_json_source():
    details = json.loads(get_scheme_details("SCH001"))
    eligibility = json.loads(check_scheme_eligibility("SCH001", {"state": "Andhra Pradesh"}))

    assert details["source"].startswith("https://")
    assert eligibility["verification_required"] is True
    assert eligibility["preliminary_status"] == "MORE_INFORMATION_NEEDED"


def test_invalid_data_returns_useful_errors(tmp_path: Path, monkeypatch):
    data_path = tmp_path / "schemes.json"
    monkeypatch.setattr(schemes_module, "SCHEMES_PATH", data_path)

    missing = json.loads(search_schemes())
    assert "error" in missing

    data_path.write_text("not json", encoding="utf-8")
    invalid_json = json.loads(search_schemes())
    assert "invalid JSON" in invalid_json["error"]

    data_path.write_text(json.dumps(["not a scheme object"]), encoding="utf-8")
    malformed_records = json.loads(search_schemes())
    assert "only scheme objects" in malformed_records["error"]
