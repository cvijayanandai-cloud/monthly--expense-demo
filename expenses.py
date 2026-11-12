from pathlib import Path
import csv
from decimal import Decimal

with Path(__file__).with_name("expenses.csv").open(newline="", encoding="utf-8") as source:
    rows = list(csv.DictReader(source))
total = sum((Decimal(row["amount"]) for row in rows), Decimal("0"))
print(f"Monthly expenses: Rs. {total:,.2f}")
print(f"Expense categories: {len(rows)}")
