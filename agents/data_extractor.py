import json
import os
from typing import Dict

def extract_financial_data(profile_path: str) -> Dict:
    """
    Extracts financial metrics from a synthetic applicant profile (JSON format).
    Validates required fields.
    """
    with open(profile_path, 'r') as f:
        data = json.load(f)

    required_fields = [
        "applicant_name", "income", "expenses", "liabilities",
        "loan_amount", "loan_term", "employment_status", "credit_score"
    ]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    metrics = {
        "applicant_name": data["applicant_name"],
        "income": data["income"],
        "expenses": data["expenses"],
        "liabilities": data["liabilities"],
        "loan_amount": data["loan_amount"],
        "loan_term": data["loan_term"],
        "employment_status": data["employment_status"],
        "credit_score": data["credit_score"],
        "dti": round(data["liabilities"] / max(data["income"], 1), 2),
    }
    return metrics

# Example usage
if __name__ == "__main__":
    path = os.path.join("..", "data", "applicant_01.json")
    print(extract_financial_data(path))
