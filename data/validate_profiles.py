import os
import json
from data_extractor import extract_financial_data

PROFILE_DIR = "synthetic_profiles"

failed_files = []

for file in os.listdir(PROFILE_DIR):
    if file.endswith(".json"):
        path = os.path.join(PROFILE_DIR, file)
        try:
            extract_financial_data(path)
        except Exception as e:
            failed_files.append((file, str(e)))

if not failed_files:
    print("✅ All profiles passed validation.")
else:
    print("❌ The following profiles failed validation:")
    for fname, error in failed_files:
        print(f"- {fname}: {error}")
