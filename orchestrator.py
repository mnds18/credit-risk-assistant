from langchain_community.chat_models import ChatOpenAI
from agents.credit_policy_retriever import load_and_index_policies, query_policy
from agents.data_extractor import extract_financial_data
import joblib
import os
import pandas as pd

# Load pre-trained ML model
MODEL_PATH = "app/model/random_forest_model.pkl"
ml_model = joblib.load(MODEL_PATH)

def orchestrate_credit_assessment(applicant_json_path, policy_docs_dir):
    try:
        print('Starting orchestrate_credit_assessment...')

        financials = extract_financial_data(applicant_json_path)
        print(f'Financials extracted: {financials}')

        dti = round(financials['liabilities'] / financials['income'], 2)
        is_full_time = 1 if financials['employment_status'].lower() == 'full-time' else 0

        print(f'Creating prediction input data...')
        X_pred = pd.DataFrame([[
            financials['income'],
            financials['expenses'],
            financials['liabilities'],
            financials['loan_amount'],
            financials['loan_term'],
            financials['credit_score'],
            dti,
            is_full_time
        ]], columns=["income", "expenses", "liabilities", "loan_amount", "loan_term", "credit_score", "dti", "is_full_time"])

        print(f'Predicting eligibility probability with model...')
        prob = ml_model.predict_proba(X_pred)[0][1]  # probability of being eligible

        rules_failed = []
        if financials['credit_score'] < 680:
            rules_failed.append({"rule": "credit_score", "passed": False, "value": financials['credit_score'], "threshold": 680})
        if dti > 0.4:
            rules_failed.append({"rule": "dti", "passed": False, "value": dti, "threshold": 0.4})
        if financials['loan_term'] > 30:
            rules_failed.append({"rule": "loan_term", "passed": False, "value": financials['loan_term'], "threshold": 30})
        if financials['employment_status'].lower() != "full-time":
            rules_failed.append({"rule": "employment_status", "passed": False, "value": financials['employment_status'], "expected": "full-time"})

        # Define eligibility tiers
        if prob > 0.75:
            eligible = True
        elif prob > 0.5:
            eligible = len(rules_failed) == 0  # override with rules
        else:
            eligible = False

        print(f'Loading and indexing policies from: {policy_docs_dir}')
        vectorstore = load_and_index_policies(policy_docs_dir)

        print('Querying policy summary...')
        queries = [
            "maximum DTI",
            "minimum credit score",
            "loan term limit",
            "employment requirement"
        ]
        policy_summary = []
        for query in queries:
            results = query_policy(vectorstore, query)
            # Append each query result as a single string
            policy_summary.append(" ".join(results))

        # Deduplicate the policy summary before joining
        unique_policy_summary = list(set(policy_summary))  # Convert to set to remove duplicates
        final_policy_summary = " ".join(unique_policy_summary)  # Join the unique summary results into one string


        print('Generating LLM summary...')
        user_input = f"Applicant profile: {financials}. Policy: {final_policy_summary}. Based on this, write a professional one-paragraph eligibility explanation."
        llm = ChatOpenAI(temperature=0.3)
        summary = llm.invoke(user_input)

        print('Returning result...')
        return {
            "applicant_name": financials["applicant_name"],
            "eligible": eligible,
            "rules_failed": rules_failed,
            "probability": prob,
            "policy_summary": final_policy_summary,
            "llm_summary": summary.content if hasattr(summary, 'content') else str(summary),
            "model_input": X_pred,  # <- for SHAP
            "features": X_pred.columns.tolist()  # <- to double-check shape match
        }


    except Exception as e:
        print(f'Error in orchestrator: {e}')
        return None
