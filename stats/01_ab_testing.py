"""01: A/B testing — run a full test from scratch with numpy only.

Scenario: an e-commerce site tests a new checkout flow.
  Control (A):   5,000 visitors, 400 conversions  (8.0%)
  Treatment (B): 5,000 visitors, 460 conversions  (9.2%)
Is B actually better, or could this be noise?

Fill in each TODO, then run:  python stats/01_ab_testing.py
Solutions: stats/solutions/01_ab_testing.py
"""
import numpy as np

rng = np.random.default_rng(0)

n_a, conv_a = 5000, 400
n_b, conv_b = 5000, 460
p_a, p_b = conv_a / n_a, conv_b / n_b

# Q1. What are the two conversion rates and the absolute lift
#     (percentage points) and relative lift (%)?
...
print("Q1: ...")

# Q2. State the null and alternative hypothesis in a comment.

# Q3. Two-proportion z-test by hand:
#     pooled p = (conv_a + conv_b) / (n_a + n_b)
#     se = sqrt(pooled_p * (1-pooled_p) * (1/n_a + 1/n_b))
#     z = (p_b - p_a) / se
#     Compute z. (|z| > 1.96 means p < 0.05, two-sided.)
z = ...
print("Q3 z =", z)

# Q4. Simulation instead of formulas (this often impresses more):
#     Under the null (no difference), pool all the data. Simulate
#     10,000 experiments: draw n_a and n_b conversions from the pooled
#     rate (rng.binomial) and record the rate difference. The p-value
#     is the share of simulated |differences| >= the observed one.
p_value = ...
print("Q4 simulated p-value:", p_value)

# Q5. 95% confidence interval for the difference in conversion rates:
#     diff ± 1.96 * sqrt(p_a(1-p_a)/n_a + p_b(1-p_b)/n_b)
#     Does the interval contain 0, and what does that mean?
ci = ...
print("Q5 95% CI:", ci)

# Q6. Business communication (write as a comment):
#     Summarise this result for a non-technical stakeholder in 2-3
#     sentences: what happened, is it real, what to do next.
#     Mention: randomisation, significance, and that you'd also check
#     revenue per visitor, not just conversion.
