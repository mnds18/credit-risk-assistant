# 🏦 GenAI Credit Risk Assistant

This project is a Generative AI-powered credit risk evaluation tool that uses LLMs, SHAP explainability, and machine learning to assess loan eligibility in a transparent, policy-aware, and explainable way.

---

## 🔍 Features

- ✅ Upload JSON applicant profiles for auto-assessment
- 📘 Policy document retrieval using LangChain RAG
- 💬 GPT-based eligibility explanation (LLM summary)
- 📊 SHAP-based model transparency
- 📅 Streamlit UI for interaction and real-time analysis

---

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Train model (optional if already trained)
python train_model.py

# Run the app
streamlit run app/streamlit_app.py
```

---

## 📁 Folder Structure

```
genai-credit-risk-assistant/
├── app/
│   ├── streamlit_app.py
│   └── model/
├── agents/
│   ├── credit_policy_retriever.py
│   ├── data_extractor.py
├── documents/            # Policy docs
├── data/                 # Applicant JSONs
├── orchestrator.py       # Orchestration logic
├── train_model.py        # Training script
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📄 Example Output

![UI Screenshot](demo/demo_ui.png)

---

## 🙌 Credits

Built using:
- OpenAI (LLM)
- LangChain (agent + RAG)
- Scikit-learn (model)
- SHAP (interpretability)
- Streamlit (UI)

---

## 💡 Project Purpose

This project demonstrates how modern LLMs and classical ML can be combined in an **enterprise-grade AI pipeline** for financial services.

It's modular, explainable, and designed to make you stand out to hiring managers looking for:
- LLM use cases
- Agentic AI architecture
- Business impact from ML and GenAI
