import json
import random
import os

APPLICANT_NAMES = [
    "Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Lee", "Ethan Kim",
    "Fiona Davis", "George Clark", "Hannah White", "Ian Lewis", "Julia Adams",
    "Kevin Hall", "Laura Young", "Michael Scott", "Nina Harris", "Owen Bell",
    "Paula King", "Quentin Ford", "Rachel Green", "Steve Martin", "Tina Brooks"
]

EMPLOYMENT_STATUSES = ["full-time", "part-time", "casual", "contract"]

os.makedirs("synthetic_profiles", exist_ok=True)

for i, name in enumerate(APPLICANT_NAMES):
    profile = {
        "applicant_name": name,
        "income": random.randint(40000, 120000),
        "expenses": random.randint(20000, 60000),
        "liabilities": random.randint(10000, 50000),
        "loan_amount": random.randint(200000, 600000),
        "loan_term": random.choice([15, 20, 25, 30, 35]),
        "credit_score": random.randint(550, 800),
        "employment_status": random.choice(EMPLOYMENT_STATUSES)
    }

    with open(f"synthetic_profiles/applicant_{i+1:02}.json", "w") as f:
        json.dump(profile, f, indent=2)

print("✅ 20 synthetic applicant profiles generated in ./synthetic_profiles/")
