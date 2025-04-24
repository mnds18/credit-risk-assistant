# 🧠 Automated Credit Risk Assistant (GenAI + Agentic AI)

This is a modular GenAI-powered application for automated creditworthiness evaluation. It simulates a loan underwriting assistant using OpenAI GPT, RAG over credit policy documents, and LLM agents.

## 🔧 Features
- Modular agent-based architecture
- Local run using VS Code + Python
- GPT-4/GPT-3.5-powered reasoning
- RAG for financial policy lookup
- Synthetic profile analysis
- Credit decision logic
- Batch evaluator for multiple profiles
- Interactive Streamlit dashboard (TBD)

## 🗂️ Project Structure
```
credit-risk-assistant/
├── agents/
│   ├── data_extractor.py
│   ├── credit_policy_retriever.py
│   └── risk_decision_agent.py
├── data/
│   ├── applicant_01.json → applicant_20.json
│   └── generate_synthetic_data.py
├── documents/
│   └── home_loan_policy.txt
├── batch_evaluator.py
├── app/                    # Streamlit frontend (TBD)
├── utils/                  # RAG utilities (TBD)
├── requirements.txt
└── README.md
```

## 🧪 Example Run
```bash
# Generate synthetic data
python data/generate_synthetic_data.py

# Evaluate a single profile
python agents/risk_decision_agent.py

# Evaluate all profiles in batch
python batch_evaluator.py
```

## 📬 Contact
Built by Mrig Debsarma – GenAI & Data Science Professional | Sydney