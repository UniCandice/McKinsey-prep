"""02: Descriptive stats, correlation & confidence intervals — real data.

Uses datasets/orders.csv and datasets/churn.csv.

Fill in each TODO, then run:  python stats/02_confidence_intervals.py
"""
import numpy as np
import pandas as pd

orders = pd.read_csv("datasets/orders.csv")
churn = pd.read_csv("datasets/churn.csv").drop_duplicates()
amounts = orders.loc[orders["status"] == "completed", "amount"]

# Q1. Mean, median and standard deviation of completed order amounts.
#     Mean >> median here — what does that tell you about the shape
#     of the distribution? (Answer in a comment.)
...
print("Q1: mean=... median=... std=...")

# Q2. 95% confidence interval for the MEAN order amount:
#     mean ± 1.96 * std / sqrt(n)
#     Write, in a comment, the correct one-sentence interpretation
#     (it's about the procedure capturing the true mean, not
#     "95% chance the mean is in this interval").
ci = ...
print("Q2 95% CI for mean amount:", ci)

# Q3. Bootstrap the same interval: resample `amounts` with replacement
#     10,000 times (rng.choice), take each sample's mean, and report
#     the 2.5th and 97.5th percentiles. Compare with Q2.
boot_ci = ...
print("Q3 bootstrap CI:", boot_ci)

# Q4. Correlation matrix of tenure_months, monthly_bill,
#     support_calls, churn (use .corr()). Which feature correlates
#     most strongly with churn, and in which direction?
q4 = ...
print("Q4:\n", q4)

# Q5. Correlation ≠ causation drill (comment): monthly_bill correlates
#     positively with churn. Give one causal story, one confounder
#     story, and one way to find out which is true.

# Q6. Do churners make more support calls? Compare the mean support
#     calls of churners vs non-churners, and compute a quick z-score
#     for the difference in means:
#     z = (m1 - m0) / sqrt(s1²/n1 + s0²/n0)
q6 = ...
print("Q6 z =", q6)
