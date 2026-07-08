"""Generate all synthetic practice datasets into datasets/.

Run once:  python generate_data.py
Re-running always produces identical data (fixed random seed).
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
OUT = Path(__file__).parent / "datasets"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- customers
N_CUSTOMERS = 500
first = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael",
         "Linda", "David", "Elizabeth", "William", "Barbara", "Richard",
         "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
         "Priya", "Wei", "Fatima", "Carlos", "Aisha", "Yuki", "Omar", "Ingrid"]
last = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
        "Davis", "Rodriguez", "Martinez", "Patel", "Chen", "Khan", "Nguyen",
        "Kim", "Singh", "Lopez", "Wilson", "Anderson", "Taylor"]
cities = ["London", "Manchester", "Birmingham", "Leeds", "Glasgow",
          "Edinburgh", "Bristol", "Liverpool", "Dublin", "Cardiff"]
segments = ["Consumer", "Corporate", "Small Business"]

customers = pd.DataFrame({
    "customer_id": np.arange(1, N_CUSTOMERS + 1),
    "customer_name": [f"{rng.choice(first)} {rng.choice(last)}" for _ in range(N_CUSTOMERS)],
    "age": rng.integers(18, 75, N_CUSTOMERS),
    "city": rng.choice(cities, N_CUSTOMERS, p=[.25, .12, .1, .08, .08, .07, .08, .08, .07, .07]),
    "segment": rng.choice(segments, N_CUSTOMERS, p=[.6, .25, .15]),
    "signup_date": pd.to_datetime("2023-01-01")
                   + pd.to_timedelta(rng.integers(0, 900, N_CUSTOMERS), unit="D"),
})
customers.to_csv(OUT / "customers.csv", index=False)

# ---------------------------------------------------------------- products
categories = {"Electronics": (50, 900), "Home & Kitchen": (10, 250),
              "Sports": (15, 300), "Books": (5, 40), "Clothing": (10, 120),
              "Beauty": (5, 80)}
prod_rows = []
pid = 1
for cat, (lo, hi) in categories.items():
    for i in range(5):
        prod_rows.append({
            "product_id": pid,
            "product_name": f"{cat.split(' ')[0]} Item {i + 1}",
            "category": cat,
            "unit_price": round(float(rng.uniform(lo, hi)), 2),
        })
        pid += 1
products = pd.DataFrame(prod_rows)
products.to_csv(OUT / "products.csv", index=False)

# ---------------------------------------------------------------- orders
N_ORDERS = 5000
# ~12% of customers never order (needed for LEFT JOIN / anti-join questions)
active = rng.choice(customers.customer_id, int(N_CUSTOMERS * 0.88), replace=False)
# heavy-tail: some customers order a lot
weights = rng.pareto(1.5, len(active)) + 1
weights /= weights.sum()

order_customer = rng.choice(active, N_ORDERS, p=weights)
order_product = rng.choice(products.product_id, N_ORDERS)
qty = rng.integers(1, 5, N_ORDERS)
price = products.set_index("product_id").loc[order_product, "unit_price"].to_numpy()

orders = pd.DataFrame({
    "order_id": np.arange(10001, 10001 + N_ORDERS),
    "customer_id": order_customer,
    "product_id": order_product,
    "order_date": pd.to_datetime("2024-01-01")
                  + pd.to_timedelta(rng.integers(0, 550, N_ORDERS), unit="D"),
    "quantity": qty,
    "amount": np.round(price * qty * rng.uniform(0.9, 1.0, N_ORDERS), 2),
    "status": rng.choice(["completed", "completed", "completed", "returned", "cancelled"], N_ORDERS),
})
orders = orders.sort_values("order_date").reset_index(drop=True)
orders["order_id"] = np.arange(10001, 10001 + N_ORDERS)
orders.to_csv(OUT / "orders.csv", index=False)

# ---------------------------------------------------------------- support tickets
N_TICKETS = 800
ticket_cust = rng.choice(customers.customer_id, N_TICKETS)
tickets = pd.DataFrame({
    "ticket_id": np.arange(1, N_TICKETS + 1),
    "customer_id": ticket_cust,
    "created_date": pd.to_datetime("2024-01-01")
                    + pd.to_timedelta(rng.integers(0, 550, N_TICKETS), unit="D"),
    "issue_type": rng.choice(["delivery", "refund", "product_defect", "billing", "other"],
                             N_TICKETS, p=[.3, .25, .2, .15, .1]),
    "resolved": rng.choice([1, 1, 1, 0], N_TICKETS),
    "satisfaction_score": rng.choice([1, 2, 3, 4, 5, np.nan], N_TICKETS,
                                     p=[.05, .1, .2, .3, .25, .1]),
})
tickets.to_csv(OUT / "support_tickets.csv", index=False)

# ---------------------------------------------------------------- employees (classic SQL drills)
departments = ["Engineering", "Sales", "Marketing", "Finance", "HR", "Data Science"]
dept_size = [18, 14, 8, 7, 4, 9]
dept_salary = {"Engineering": (55000, 110000), "Sales": (35000, 80000),
               "Marketing": (38000, 75000), "Finance": (45000, 95000),
               "HR": (35000, 65000), "Data Science": (60000, 120000)}
emp_rows, eid = [], 1
for dept, n in zip(departments, dept_size):
    lo, hi = dept_salary[dept]
    for _ in range(n):
        emp_rows.append({
            "employee_id": eid,
            "employee_name": f"{rng.choice(first)} {rng.choice(last)}",
            "department": dept,
            "salary": int(rng.uniform(lo, hi) // 500 * 500),
            "hire_date": (pd.to_datetime("2015-01-01")
                          + pd.to_timedelta(int(rng.integers(0, 3600)), unit="D")).date(),
        })
        eid += 1
employees = pd.DataFrame(emp_rows)
# give each department a manager column (self-join practice)
employees["manager_id"] = employees.groupby("department")["employee_id"].transform("min")
employees.loc[employees.employee_id == employees.manager_id, "manager_id"] = np.nan
employees.to_csv(OUT / "employees.csv", index=False)

# ---------------------------------------------------------------- churn (telecom, for ML)
N = 2000
tenure = rng.integers(1, 73, N)
contract = rng.choice(["month-to-month", "one_year", "two_year"], N, p=[.5, .3, .2])
monthly_bill = np.round(rng.uniform(20, 110, N), 2)
support_calls = rng.poisson(1.2, N)
data_gb = np.round(rng.gamma(3, 4, N), 1)
is_senior = (rng.random(N) < 0.16).astype(int)

# churn probability: short tenure + month-to-month + many support calls + high bill
logit = (-1.2
         - 0.045 * tenure
         + 1.1 * (contract == "month-to-month")
         + 0.45 * support_calls
         + 0.012 * monthly_bill
         + 0.4 * is_senior)
churn = (rng.random(N) < 1 / (1 + np.exp(-logit))).astype(int)

churn_df = pd.DataFrame({
    "customer_id": np.arange(1, N + 1),
    "tenure_months": tenure,
    "contract_type": contract,
    "monthly_bill": monthly_bill,
    "data_used_gb": data_gb,
    "support_calls": support_calls,
    "is_senior": is_senior,
    "payment_method": rng.choice(["credit_card", "debit", "bank_transfer", "cheque"], N),
    "churn": churn,
})

# inject realistic mess: missing values + duplicates (cleaning practice)
churn_df.loc[rng.choice(N, 90, replace=False), "monthly_bill"] = np.nan
churn_df.loc[rng.choice(N, 60, replace=False), "data_used_gb"] = np.nan
churn_df = pd.concat([churn_df, churn_df.sample(25, random_state=42)]).sample(
    frac=1, random_state=42).reset_index(drop=True)
churn_df.to_csv(OUT / "churn.csv", index=False)

print("Wrote datasets/:")
for f in sorted(OUT.glob("*.csv")):
    print(f"  {f.name:22s} {len(pd.read_csv(f)):>6,} rows")
print(f"\nChurn rate: {churn.mean():.1%}")
