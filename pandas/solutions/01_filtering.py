"""SOLUTIONS 01: Filtering & selecting"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])

# Q1
q1 = len(customers[customers["age"] > 50])
print("Q1:", q1)

# Q2
q2 = (customers[customers["city"] == "London"][["customer_name", "city"]]
      .sort_values("customer_name").head(5))
print("Q2:\n", q2)

# Q3
q3 = len(customers[(customers["city"].isin(["London", "Manchester"]))
                   & (customers["age"] < 30)])
print("Q3:", q3)

# Q4
q4 = len(orders[orders["amount"].between(500, 1000)
                & (orders["status"] == "completed")])
print("Q4:", q4)

# Q5
q5 = len(orders[(orders["order_date"].dt.year == 2024)
                & (orders["order_date"].dt.month == 3)])
print("Q5:", q5)

# Q6
q6 = customers["segment"].isin(["Corporate", "Small Business"]).mean()
print("Q6:", round(q6, 3))

# Q7
q7 = customers.loc[customers["age"].idxmax(), "customer_name"]
print("Q7:", q7)
