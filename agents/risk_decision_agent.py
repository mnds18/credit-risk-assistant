# credit-risk-assistant/agents/risk_decision_agent.py

from typing import Dict

def evaluate_credit_risk(metrics: Dict, policy_summary: str) -> Dict:
    """
    Evaluates credit risk based on extracted metrics and policy constraints from RAG.
    """
    decision = {
        "applicant_name": metrics["applicant_name"],
        "eligible": True,
        "reasons": []
    }

    if metrics["debt_to_income_ratio"] > 0.4:
        decision["eligible"] = False
        decision["reasons"].append(f"DTI ratio too high: {metrics['debt_to_income_ratio']}")

    if metrics["credit_score"] < 680:
        decision["eligible"] = False
        decision["reasons"].append(f"Credit score too low: {metrics['credit_score']}")

    if metrics["loan_term"] > 30:
        decision["eligible"] = False
        decision["reasons"].append(f"Loan term exceeds 30 years: {metrics['loan_term']}")

    if metrics["employment_status"].lower() != "full-time":
        decision["eligible"] = False
        decision["reasons"].append(f"Employment status not full-time: {metrics['employment_status']}")

    if not decision["reasons"]:
        decision["reasons"].append("Eligible under policy criteria")

    return decision

# Example usage
if __name__ == "__main__":
    from agents.data_extractor import extract_financial_data
    profile = "../data/applicant_01.json"
    metrics = extract_financial_data(profile)
    policy = "See policy document summary above"
    print(evaluate_credit_risk(metrics, policy))
