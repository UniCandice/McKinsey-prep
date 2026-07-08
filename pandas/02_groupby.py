"""02: GroupBy & aggregation — datasets/orders.csv, datasets/customers.csv

Fill in each TODO, then run:  python pandas/02_groupby.py
"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])
completed = orders[orders["status"] == "completed"]

# Q1. Total completed revenue per customer_id. Show top 5.
q1 = ...
print("Q1:\n", q1)

# Q2. For each order status: number of orders AND average amount,
#     in one groupby using .agg().
q2 = ...
print("Q2:\n", q2)

# Q3. Revenue per calendar month (use order_date.dt.to_period('M')).
q3 = ...
print("Q3:\n", q3)

# Q4. Average customer age per city, rounded to 1 decimal, sorted
#     descending.
q4 = ...
print("Q4:\n", q4)

# Q5. Per customer: number of completed orders, total spend, and
#     average order value — all in one .agg() with named aggregations:
#     .agg(n_orders=("order_id", "count"), ...)
#     Show the 5 biggest spenders.
q5 = ...
print("Q5:\n", q5)

# Q6. Which city generates the most revenue? You'll need to merge
#     completed orders with customers first. (One city name)
q6 = ...
print("Q6:", q6)

# Q7. transform: add a column 'customer_total' to the completed
#     orders frame holding each customer's total spend, so every row
#     shows the order amount AND that customer's overall total.
#     Print the first 5 rows of [customer_id, amount, customer_total].
q7 = ...
print("Q7:\n", q7)
