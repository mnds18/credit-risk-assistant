import os
from agents.data_extractor import extract_financial_data
from agents.risk_decision_agent import evaluate_credit_risk

def run_batch_evaluation(data_dir: str = "data"):
    profile_files = sorted([f for f in os.listdir(data_dir) if f.endswith(".json")])
    print("\n📊 Batch Credit Evaluation Results:\n" + "="*40)

    for file in profile_files:
        path = os.path.join(data_dir, file)
        metrics = extract_financial_data(path)
        decision = evaluate_credit_risk(metrics, "Policy constraints loaded via RAG")

        print(f"\n👤 Applicant: {decision['applicant_name']}")
        print(f"✅ Eligible: {decision['eligible']}")
        print("📝 Reasons:")
        for reason in decision["reasons"]:
            print(f"  - {reason}")

if __name__ == "__main__":
    run_batch_evaluation()
