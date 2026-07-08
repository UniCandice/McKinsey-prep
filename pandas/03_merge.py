"""03: Merging / joining — customers, orders, products, support_tickets

Fill in each TODO, then run:  python pandas/03_merge.py
"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])
products = pd.read_csv("datasets/products.csv")
tickets = pd.read_csv("datasets/support_tickets.csv", parse_dates=["created_date"])

# Q1. Inner-merge orders with customers on customer_id.
#     How many rows result, and why is it not len(customers)?
q1 = ...
print("Q1:", q1)

# Q2. LEFT-merge customers with orders. Which customers have never
#     ordered? Count them. (After a left merge, missing right-side
#     columns are NaN.)
q2 = ...
print("Q2:", q2)

# Q3. Three-way merge: orders + customers + products.
#     Then: revenue per product category from completed orders.
q3 = ...
print("Q3:\n", q3)

# Q4. Merge with different key names: rename products.product_id to
#     'pid' first, then merge orders onto it using left_on/right_on.
q4 = ...
print("Q4 rows:", q4)

# Q5. Per-customer summary table with one row per customer:
#     total_spend (completed only), n_orders, n_tickets.
#     Customers with no orders/tickets should show 0, not NaN.
#     Show 5 rows. (Build two small aggregates, then merge them onto
#     customers with how='left' and .fillna(0))
q5 = ...
print("Q5:\n", q5)

# Q6. Validate a merge: merge orders with products using
#     validate="many_to_one". Why is many_to_one correct here,
#     and when would it raise?
q6 = ...
print("Q6 rows:", q6)
