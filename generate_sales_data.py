"""
generate_sales_data.py
-----------------------
Generates a realistic-but-messy retail sales dataset (Superstore-style)
for the EDA notebook to clean and analyze:
    data/raw/sales_raw.csv

The messiness (duplicates, missing values, inconsistent casing,
occasional negative sales/quantity from returns) is intentional -- it
gives the "Data Cleaning" section of the notebook real work to do.

Run once before opening the notebook:
    python generate_sales_data.py
"""

import random
import csv
import os

random.seed(7)

RAW_DIR = os.path.join(os.path.dirname(__file__), "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

REGIONS = ["North", "South", "East", "West"]
SEGMENTS = ["Consumer", "Corporate", "Home Office"]
CATEGORY_MAP = {
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art"],
    "Technology": ["Phones", "Accessories", "Machines", "Copiers"],
}
MONTHS = [f"2024-{m:02d}" for m in range(1, 13)]

def messy_case(text):
    """Randomly mess up the casing to simulate inconsistent data entry."""
    r = random.random()
    if r < 0.15:
        return text.upper()
    if r < 0.3:
        return text.lower()
    return text


rows = []
order_id = 5001
for _ in range(900):
    category = random.choice(list(CATEGORY_MAP.keys()))
    sub_category = random.choice(CATEGORY_MAP[category])
    region = messy_case(random.choice(REGIONS))
    segment = random.choice(SEGMENTS)
    month = random.choice(MONTHS)
    day = random.randint(1, 28)
    order_date = f"{month}-{day:02d}"

    quantity = random.choice([1, 1, 2, 2, 3, 4, 5])
    unit_price = round(random.uniform(10, 800), 2)
    sales = round(unit_price * quantity, 2)
    discount = random.choice([0, 0, 0, 0.1, 0.15, 0.2, 0.3])
    profit = round(sales * random.uniform(-0.15, 0.35) * (1 - discount), 2)

    rows.append([order_id, order_date, category, sub_category, region,
                 segment, quantity, sales, discount, profit])
    order_id += 1

# inject data-quality issues
rows[20][7] = ""      # missing sales
rows[45][9] = ""      # missing profit
rows[60][6] = ""      # missing quantity
rows[100][4] = ""     # missing region
rows.append(rows[10])  # exact duplicate row
rows.append(rows[200])  # another duplicate

with open(os.path.join(RAW_DIR, "sales_raw.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["order_id", "order_date", "category", "sub_category",
                "region", "segment", "quantity", "sales", "discount",
                "profit"])
    w.writerows(rows)

print(f"Generated {len(rows)} rows -> {os.path.abspath(os.path.join(RAW_DIR, 'sales_raw.csv'))}")
