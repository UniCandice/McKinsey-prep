"""SOLUTIONS 04: Missing values, duplicates & cleaning"""
import pandas as pd

df = pd.read_csv("datasets/churn.csv")

# Q1
q1 = df.isna().sum()
q1 = q1[q1 > 0]
print("Q1:\n", q1)

# Q2
q2 = int(df.duplicated().sum())
df = df.drop_duplicates(keep="first").reset_index(drop=True)
print("Q2 duplicates removed:", q2)

# Q3 — median is robust to outliers; a few huge bills would drag the mean up
df["monthly_bill"] = df["monthly_bill"].fillna(df["monthly_bill"].median())
print("Q3 remaining NaNs in monthly_bill:", int(df["monthly_bill"].isna().sum()))

# Q4
df["data_used_gb"] = df["data_used_gb"].fillna(
    df.groupby("contract_type")["data_used_gb"].transform("median"))
print("Q4 remaining NaNs in data_used_gb:", int(df["data_used_gb"].isna().sum()))

# Q5
df["tenure_band"] = pd.cut(df["tenure_months"],
                           bins=[0, 12, 24, 48, 999],
                           labels=["0-12", "13-24", "25-48", "49+"])
q5 = df.groupby("tenure_band", observed=True)["churn"].mean().round(3)
print("Q5:\n", q5)

# Q6
q6 = df.groupby("contract_type")["churn"].mean().round(3).sort_values(ascending=False)
print(f"Q6: overall churn {df['churn'].mean():.1%}\n", q6)

# Q7
df.to_csv("datasets/churn_clean.csv", index=False)
print("Q7: wrote datasets/churn_clean.csv")
