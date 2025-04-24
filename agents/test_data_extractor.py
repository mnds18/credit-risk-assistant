import pytest
import os
import json
from agents.data_extractor import extract_financial_data

TEST_FILE = "test_applicant.json"

valid_profile = {
    "applicant_name": "Test User",
    "income": 80000,
    "expenses": 30000,
    "liabilities": 20000,
    "loan_amount": 400000,
    "loan_term": 25,
    "employment_status": "full-time",
    "credit_score": 710
}

def test_extract_valid_profile():
    with open(TEST_FILE, "w") as f:
        json.dump(valid_profile, f)

    result = extract_financial_data(TEST_FILE)
    assert result["applicant_name"] == valid_profile["applicant_name"]
    assert result["credit_score"] == valid_profile["credit_score"]
    assert isinstance(result["dti"], float)
    os.remove(TEST_FILE)

def test_zero_income_dti():
    profile = valid_profile.copy()
    profile["income"] = 0
    profile["liabilities"] = 10000
    with open(TEST_FILE, "w") as f:
        json.dump(profile, f)

    result = extract_financial_data(TEST_FILE)
    assert result["dti"] == 10000  # avoids division by zero due to max(income, 1)
    os.remove(TEST_FILE)

def test_negative_values():
    profile = valid_profile.copy()
    profile["income"] = -50000
    profile["liabilities"] = -10000
    with open(TEST_FILE, "w") as f:
        json.dump(profile, f)

    result = extract_financial_data(TEST_FILE)
    assert result["income"] == -50000
    assert result["liabilities"] == -10000
    os.remove(TEST_FILE)


def test_missing_field_raises():
    incomplete = valid_profile.copy()
    del incomplete["loan_amount"]
    with open(TEST_FILE, "w") as f:
        json.dump(incomplete, f)

    with pytest.raises(ValueError) as excinfo:
        extract_financial_data(TEST_FILE)

    assert "Missing required field" in str(excinfo.value)
    os.remove(TEST_FILE)
