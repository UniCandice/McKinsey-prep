"""SOLUTIONS 02: Descriptive stats, correlation & confidence intervals"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)

orders = pd.read_csv("datasets/orders.csv")
churn = pd.read_csv("datasets/churn.csv").drop_duplicates()
amounts = orders.loc[orders["status"] == "completed", "amount"]

# Q1 — mean > median means the distribution is right-skewed:
# a long tail of large orders pulls the mean up.
print(f"Q1: mean={amounts.mean():.2f} median={amounts.median():.2f} "
      f"std={amounts.std():.2f}")

# Q2
n = len(amounts)
half = 1.96 * amounts.std() / np.sqrt(n)
ci = (amounts.mean() - half, amounts.mean() + half)
print(f"Q2 95% CI for mean amount: ({ci[0]:.2f}, {ci[1]:.2f})")
# Interpretation: if we repeated this sampling many times and built the
# interval the same way each time, about 95% of those intervals would
# contain the true mean order amount.

# Q3
boot_means = [amounts.sample(n, replace=True, random_state=None).mean()
              for _ in range(2000)]
# faster numpy version:
boot = rng.choice(amounts.to_numpy(), size=(10_000, n), replace=True).mean(axis=1)
boot_ci = (np.percentile(boot, 2.5), np.percentile(boot, 97.5))
print(f"Q3 bootstrap CI: ({boot_ci[0]:.2f}, {boot_ci[1]:.2f})")

# Q4 — support_calls has the strongest positive correlation with churn
cols = ["tenure_months", "monthly_bill", "support_calls", "churn"]
q4 = churn[cols].corr().round(3)
print("Q4:\n", q4)

# Q5 (correlation ≠ causation)
# Causal story: higher bills genuinely push customers to leave.
# Confounder story: heavy users both pay more AND have more problems
#   (e.g. more support calls), and it's the problems that drive churn.
# How to find out: run an experiment — e.g. randomly give a discount to
#   some high-bill customers and compare churn against a control group.

# Q6
g1 = churn.loc[churn["churn"] == 1, "support_calls"]
g0 = churn.loc[churn["churn"] == 0, "support_calls"]
z = (g1.mean() - g0.mean()) / np.sqrt(g1.var() / len(g1) + g0.var() / len(g0))
print(f"Q6 churners: {g1.mean():.2f} calls, non-churners: {g0.mean():.2f}, "
      f"z = {z:.1f}")
