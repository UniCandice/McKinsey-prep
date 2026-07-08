"""SOLUTIONS 01: A/B testing"""
import numpy as np

rng = np.random.default_rng(0)

n_a, conv_a = 5000, 400
n_b, conv_b = 5000, 460
p_a, p_b = conv_a / n_a, conv_b / n_b

# Q1
abs_lift = p_b - p_a
rel_lift = abs_lift / p_a
print(f"Q1: A={p_a:.1%}  B={p_b:.1%}  "
      f"absolute lift={abs_lift * 100:.1f}pp  relative lift={rel_lift:.1%}")

# Q2
# H0 (null): the new checkout has the same conversion rate as the old one.
# H1: the conversion rates differ (two-sided).

# Q3
pooled = (conv_a + conv_b) / (n_a + n_b)
se = np.sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
z = (p_b - p_a) / se
print(f"Q3 z = {z:.2f}  (|z| > 1.96 → significant at 5%)")

# Q4
sims = 10_000
diff_sim = (rng.binomial(n_b, pooled, sims) / n_b
            - rng.binomial(n_a, pooled, sims) / n_a)
p_value = float(np.mean(np.abs(diff_sim) >= abs(p_b - p_a)))
print("Q4 simulated p-value:", round(p_value, 4))

# Q5
se_unpooled = np.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
ci = (abs_lift - 1.96 * se_unpooled, abs_lift + 1.96 * se_unpooled)
print(f"Q5 95% CI for difference: ({ci[0] * 100:.2f}pp, {ci[1] * 100:.2f}pp)")
# If the CI excludes 0, the difference is statistically significant at 5%.

# Q6 (stakeholder summary)
# "We randomly split visitors between the old and new checkout. The new
# flow converted 9.2% of visitors vs 8.0% — a 15% relative improvement
# that is statistically significant (p ≈ 0.04), so it's unlikely to be
# luck. I'd recommend rolling it out, after confirming revenue per
# visitor and refund rates also look healthy, since a higher conversion
# rate alone doesn't guarantee more profit."
