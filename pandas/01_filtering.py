"""01: Filtering & selecting — datasets/customers.csv, datasets/orders.csv

Fill in each TODO, then run:  python pandas/01_filtering.py
Check against: pandas/solutions/01_filtering.py
"""
import pandas as pd

customers = pd.read_csv("datasets/customers.csv", parse_dates=["signup_date"])
orders = pd.read_csv("datasets/orders.csv", parse_dates=["order_date"])

# Q1. How many customers are older than 50?
q1 = ...
print("Q1:", q1)

# Q2. Select only customer_name and city for customers in London,
#     sorted by name. Show the first 5.
q2 = ...
print("Q2:\n", q2)

# Q3. Customers in London OR Manchester who are under 30.
#     How many are there? (Careful with & | and parentheses)
q3 = ...
print("Q3:", q3)

# Q4. Orders with amount between 500 and 1000 (inclusive) that were
#     completed. How many rows? (Try .between())
q4 = ...
print("Q4:", q4)

# Q5. Orders placed in March 2024. How many?
#     (Hint: order_date.dt.year / .dt.month)
q5 = ...
print("Q5:", q5)

# Q6. Using .isin(): customers in the 'Corporate' or 'Small Business'
#     segment. What share of all customers are they? (one number, 0-1)
q6 = ...
print("Q6:", q6)

# Q7. The single oldest customer's name. (idxmax or sort_values)
q7 = ...
print("Q7:", q7)
