🧠 Credit Risk Assistant
Enterprise AI for Automated Credit Risk Assessment and Explainable Decisioning

<details> <summary>📖 Executive Summary (click to expand)</summary>
Credit Risk Assistant is an enterprise-grade AI system designed to automate the loan approval process by combining machine learning predictions, policy document validation, and explainable AI.
It accelerates credit decisions while ensuring transparency, compliance, and trust — vital for financial institutions operating under regulatory scrutiny.

</details>
📌 Project Overview
Credit Risk Assistant automates applicant evaluation and enforces lending policies dynamically, ensuring fast and transparent credit decision-making.

🎯 Business Objective
Automate loan eligibility assessments end-to-end.

Deliver explainable, regulator-friendly model outputs.

Ensure lending policy compliance dynamically.

🔥 Key Features
Applicant financial data ingestion.

ML-driven credit risk prediction.

Policy document querying via LangChain.

SHAP-based model explainability.

Streamlit UI for end-user interaction.

Dockerized deployment for scalable environments.

## 📊 Demo
![Demo](docs/credit_app_1.jpg)

<details> <summary>🏗️ System Architecture (click to expand)</summary>
css
Copy
Edit
[User Input] → [ML Prediction Engine] → [Policy Validator (LangChain)] → [Explainability Layer (SHAP)] → [Streamlit UI]

Component	Technology
Frontend (UI)	Streamlit
ML Model	Scikit-learn
Explainability Module	SHAP
Policy Validator	LangChain, PyMuPDF
Storage and Data	Pandas, Pickle
Deployment	Docker, Streamlit Cloud (Optional Hugging Face)
</details>
🛠️ Technology Stack
Python 3.10+

Streamlit

Scikit-learn

SHAP

LangChain

PyMuPDF

Pandas, Numpy, Matplotlib

Docker

📦 Folder Structure
Copy
Edit
credit-risk-assistant/
├── app/
│   └── streamlit_app.py
├── orchestrator.py
├── documents/
│   └── home_loan_policy.txt
├── model/
│   └── trained_model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
🚀 Deployment Guide
Local Setup
bash
Copy
Edit
git clone https://github.com/mnds18/credit-risk-assistant.git
cd credit-risk-assistant
python -m venv venv
source venv/bin/activate    # (Windows: venv\\Scripts\\activate)
pip install -r requirements.txt
streamlit run app/streamlit_app.py
Docker Setup
bash
Copy
Edit
docker build -t credit-risk-assistant .
docker run -p 8501:8501 credit-risk-assistant
<details> <summary>📈 Application Workflow (click to expand)</summary>
Enter applicant financials via UI.

ML model predicts probability of loan approval.

Policy validator checks against documented eligibility criteria.

SHAP explainability highlights feature impact.

User views final decision and contributing factors.

</details>
🚧 Limitations and Future Roadmap

Current Scope	Future Enhancements
Static user input	OCR-based automatic document extraction
Single policy document	Multi-document retrieval (Vector Search)
Static models	AutoML and dynamic retraining pipeline
Single session	Authentication and session management
🎯 Impact
Credit Risk Assistant bridges the gap between traditional credit decision-making and modern AI automation —
providing speed, compliance, transparency, and trustworthiness for financial services operations.


## ✍️ Author

Built by [Mrig](https://www.linkedin.com/in/mrigendranath/)  

📬 Open to feedback, collaborations, and enterprise solutions consulting.

⭐ If you found this project insightful, please consider starring ⭐ the repository and sharing it!
⚡ Final Note
Credit Risk Assistant is more than an AI project —
it is a demonstration of building real-world, production-ready GenAI-powered decisioning systems for enterprise environments.