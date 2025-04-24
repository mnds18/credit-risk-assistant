import streamlit as st
import sys
import os
import json
import pandas as pd
import shap
import joblib
import numpy as np
import matplotlib.pyplot as plt


# Enable access to orchestrator module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from orchestrator import orchestrate_credit_assessment

MODEL_PATH = "app/model/random_forest_model.pkl"
rf = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Credit Risk Assistant", layout="centered")
st.title("🏦 Mrig's GenAI Credit Risk Assistant")

uploaded_file = st.file_uploader("Upload applicant JSON file", type="json")
if uploaded_file:
    with open("temp_applicant.json", "wb") as f:
        f.write(uploaded_file.read())

    with open("temp_applicant.json") as f:
        profile = json.load(f)

    result = orchestrate_credit_assessment("temp_applicant.json", "documents")
    if result is None:
        st.error("Failed to assess applicant.")
        st.stop()

    st.subheader("👤 Applicant")
    st.write(result["applicant_name"])

    st.subheader("✅ Eligibility")
    st.metric("Model Probability", f"{result['probability']*100:.1f}%")
    if result['eligible']:
        st.write("Eligible")
    else:
        st.write("Not Eligible")


    st.subheader("📝 Reasons")
    for reason in result['rules_failed']:
        rule_msg = f"❌ {reason['rule']} = {reason['value']}"
        if 'threshold' in reason:
            rule_msg += f" (threshold: {reason['threshold']})"
        if 'expected' in reason:
            rule_msg += f" (expected: {reason['expected']})"
        st.markdown(rule_msg)
    if not result['rules_failed']:
        st.success("All business rules passed.")

    st.subheader("📊 Financial Snapshot")
    df_metrics = pd.DataFrame({
        "Metric": ["Income", "Expenses", "Liabilities", "Loan Amount"],
        "Value": [
            profile["income"],
            profile["expenses"],
            profile["liabilities"],
            profile["loan_amount"]
        ]
    })
    st.bar_chart(df_metrics.set_index("Metric"))

    st.subheader("📘 Policy Summary (RAG)")
    st.code(result['policy_summary'], language="markdown")

    st.subheader("💬 LLM Explanation")
    # Clean up the LLM explanation to prevent word concatenation
    clean_llm_summary = result['llm_summary'].replace(" \n", " ")
    st.info(clean_llm_summary)

    st.subheader("🔍 SHAP Feature Importance")
    # SHAP Feature Importance
    
    dti = round(profile["liabilities"] / profile["income"], 2)
    # X_pred = pd.DataFrame([[
    #     profile["income"],
    #     profile["expenses"],
    #     profile["liabilities"],
    #     profile["loan_amount"],
    #     profile["loan_term"],
    #     profile["credit_score"],
    #     dti,
    #     1 if profile["employment_status"].lower() == "full-time" else 0
    # ]], columns=["income", "expenses", "liabilities", "loan_amount", "loan_term", "credit_score", "dti", "is_full_time"])

    X_pred = result["model_input"]


    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(X_pred)
    print("SHAP Values:", shap_values)
    print("data frame:", X_pred.head())
    print("X_pred columns:", X_pred.columns)

    # If shap_values has multiple outputs, use the second class for analysis
    if len(shap_values) > 1:
        shap_values_class_1 = shap_values[1]  # Select the SHAP values for class 1
    else:
        shap_values_class_1 = shap_values[0]  # Only class 0 is present

    print("SHAP shape:", shap_values_class_1.shape)
    print("X_pred shape:", X_pred.shape)
    
    # Ensure matching the shape of X_pred and shap_values
    assert shap_values_class_1.shape[1] == X_pred.shape[1], \
        f"Shape mismatch: {shap_values_class_1.shape[1]} != {X_pred.shape[1]}"

    # Create a figure for SHAP plot
    fig, ax = plt.subplots()

    # Plot SHAP summary
    shap.summary_plot(shap_values_class_1, X_pred, plot_type="bar", show=False)

    # Use the figure in st.pyplot
    st.pyplot(fig)
