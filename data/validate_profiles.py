import os
import sys
import json
import csv
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.data_extractor import extract_financial_data

PROFILE_DIR = "synthetic_profiles"
REPAIRED_DIR = "repaired_profiles"
CSV_EXPORT = "profile_summary.csv"

os.makedirs(REPAIRED_DIR, exist_ok=True)

required_fields = [
    "applicant_name", "income", "expenses", "liabilities",
    "loan_amount", "loan_term", "employment_status", "credit_score"
]

failed_files = []
success_profiles: List[dict] = []

for file in os.listdir(PROFILE_DIR):
    if file.endswith(".json"):
        path = os.path.join(PROFILE_DIR, file)
        try:
            data = json.load(open(path))
            repaired = False

            for field in required_fields:
                if field not in data:
                    repaired = True
                    if field == "employment_status":
                        data[field] = "full-time"
                    elif field == "applicant_name":
                        data[field] = file.replace(".json", "")
                    else:
                        data[field] = 0

            if repaired:
                repaired_path = os.path.join(REPAIRED_DIR, file)
                with open(repaired_path, "w") as f:
                    json.dump(data, f, indent=2)
                print(f"🛠️ Repaired: {file} → saved to {repaired_path}")
                path = repaired_path

            profile = extract_financial_data(path)
            success_profiles.append(profile)

        except Exception as e:
            failed_files.append((file, str(e)))

# Export to CSV for inspection
if success_profiles:
    with open(CSV_EXPORT, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=success_profiles[0].keys())
        writer.writeheader()
        writer.writerows(success_profiles)
    print(f"📄 Exported {len(success_profiles)} profiles to {CSV_EXPORT}")

if not failed_files:
    print("✅ All profiles processed successfully.")
else:
    print("❌ Some profiles could not be processed:")
    for fname, error in failed_files:
        print(f"- {fname}: {error}")
