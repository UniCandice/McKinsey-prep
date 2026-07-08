"""04: Missing values, duplicates & cleaning — datasets/churn.csv

churn.csv is deliberately messy: it has NaNs AND duplicated rows.
Fill in each TODO, then run:  python pandas/04_missing_values.py
"""
import pandas as pd

df = pd.read_csv("datasets/churn.csv")

# Q1. How many missing values per column? (Only show columns that
#     actually have missing values.)
q1 = ...
print("Q1:\n", q1)

# Q2. How many fully duplicated rows are there? Drop them, keeping
#     the first occurrence. Store the cleaned frame as df.
q2 = ...
print("Q2 duplicates removed:", q2)

# Q3. Fill missing monthly_bill with the MEDIAN monthly_bill.
#     Why median rather than mean? (Think outliers.)
...
print("Q3 remaining NaNs in monthly_bill:", int(df["monthly_bill"].isna().sum()))

# Q4. Fill missing data_used_gb with the median WITHIN each
#     contract_type (groupby + transform).
...
print("Q4 remaining NaNs in data_used_gb:", int(df["data_used_gb"].isna().sum()))

# Q5. Create tenure_band: '0-12', '13-24', '25-48', '49+' from
#     tenure_months (pd.cut). Show churn rate per band.
q5 = ...
print("Q5:\n", q5)

# Q6. One-line sanity report: overall churn rate, and churn rate by
#     contract_type. Which contract type churns most?
q6 = ...
print("Q6:\n", q6)

# Q7. Save the cleaned data to datasets/churn_clean.csv (no index).
#     The ML exercises use this file.
...
print("Q7: wrote datasets/churn_clean.csv")
