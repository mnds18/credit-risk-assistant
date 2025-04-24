import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import json

MODEL_PATH = "app/model/random_forest_model.pkl"
METADATA_PATH = "app/model/model_metadata.json"

# Ensure model directory exists
os.makedirs("app/model", exist_ok=True)

# Step 1: Create synthetic training data with 8 features
X_train = pd.DataFrame([
    [70000, 30000, 20000, 400000, 25, 720, 0.28, 1],
    [80000, 25000, 45000, 500000, 30, 690, 0.56, 0],
    [55000, 40000, 15000, 300000, 20, 700, 0.27, 1],
    [95000, 35000, 38000, 600000, 25, 710, 0.40, 1]
], columns=[
    "income", "expenses", "liabilities", "loan_amount",
    "loan_term", "credit_score", "dti", "is_full_time"
])

y_train = [1, 0, 1, 1]  # Binary targets: 1 = eligible, 0 = not eligible

# Step 2: Train model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Step 3: Save model to file
joblib.dump(rf, MODEL_PATH)

# Step 4: Save training metadata
metadata = {
    "model_name": "RandomForestClassifier",
    "features": list(X_train.columns),
    "n_estimators": 100,
    "random_state": 42,
    "trained_on": "synthetic data (8 features)",
    "notes": "Used for GenAI Credit Risk Assistant with SHAP support"
}
with open(METADATA_PATH, "w") as f:
    json.dump(metadata, f, indent=2)

print("✅ Model training complete and saved.")
