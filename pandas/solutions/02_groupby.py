"""SOLUTIONS 02: GroupBy & aggregation"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])
completed = orders[orders["status"] == "completed"]

# Q1
q1 = completed.groupby("customer_id")["amount"].sum().nlargest(5)
print("Q1:\n", q1)

# Q2
q2 = orders.groupby("status")["amount"].agg(["count", "mean"]).round(2)
print("Q2:\n", q2)

# Q3
q3 = completed.groupby(completed["order_date"].dt.to_period("M"))["amount"].sum().round(2)
print("Q3:\n", q3)

# Q4
q4 = customers.groupby("city")["age"].mean().round(1).sort_values(ascending=False)
print("Q4:\n", q4)

# Q5
q5 = (completed.groupby("customer_id")
      .agg(n_orders=("order_id", "count"),
           total_spend=("amount", "sum"),
           avg_order_value=("amount", "mean"))
      .round(2)
      .nlargest(5, "total_spend"))
print("Q5:\n", q5)

# Q6
merged = completed.merge(customers, on="customer_id")
q6 = merged.groupby("city")["amount"].sum().idxmax()
print("Q6:", q6)

# Q7
completed = completed.copy()
completed["customer_total"] = completed.groupby("customer_id")["amount"].transform("sum")
q7 = completed[["customer_id", "amount", "customer_total"]].head(5)
print("Q7:\n", q7)
