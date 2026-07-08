"""SOLUTIONS 03: Merging / joining"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])
products = pd.read_csv("datasets/products.csv")
tickets = pd.read_csv("datasets/support_tickets.csv", parse_dates=["created_date"])

# Q1 — one row PER ORDER (many-to-one), so len == len(orders), not len(customers)
q1 = len(orders.merge(customers, on="customer_id"))
print("Q1:", q1)

# Q2
left = customers.merge(orders, on="customer_id", how="left")
q2 = int(left["order_id"].isna().sum())
print("Q2:", q2)

# Q3
full = (orders.merge(customers, on="customer_id")
              .merge(products, on="product_id"))
q3 = (full[full["status"] == "completed"]
      .groupby("category")["amount"].sum().round(2)
      .sort_values(ascending=False))
print("Q3:\n", q3)

# Q4
p2 = products.rename(columns={"product_id": "pid"})
q4 = len(orders.merge(p2, left_on="product_id", right_on="pid"))
print("Q4 rows:", q4)

# Q5
spend = (orders[orders["status"] == "completed"]
         .groupby("customer_id")
         .agg(total_spend=("amount", "sum"), n_orders=("order_id", "count")))
n_tickets = tickets.groupby("customer_id").size().rename("n_tickets")
q5 = (customers[["customer_id", "customer_name"]]
      .merge(spend, on="customer_id", how="left")
      .merge(n_tickets, on="customer_id", how="left")
      .fillna(0)
      .head(5))
print("Q5:\n", q5)

# Q6 — many orders can share one product, but each order maps to exactly
# one product row. validate raises if product_id were duplicated in products.
q6 = len(orders.merge(products, on="product_id", validate="many_to_one"))
print("Q6 rows:", q6)
