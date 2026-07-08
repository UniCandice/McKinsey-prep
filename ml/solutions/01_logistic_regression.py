"""SOLUTIONS 01: Logistic regression on churn"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/churn_clean.csv")

# Q1
X = pd.get_dummies(
    df.drop(columns=["customer_id", "churn"], errors="ignore")
      .drop(columns=["tenure_band"], errors="ignore"),
    drop_first=True)
y = df["churn"]
print("Q1 X shape:", X.shape)

# Q2
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print("Q2 train churn rate:", round(y_train.mean(), 3),
      "test churn rate:", round(y_test.mean(), 3))

# Q3 — always predicting the majority class (no churn)
baseline = max(y_test.mean(), 1 - y_test.mean())
print("Q3 baseline accuracy:", round(baseline, 3))

# Q4
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print("Q4 test accuracy:", round(acc, 3))

# Q5
q5 = (pd.Series(model.coef_[0], index=X.columns)
      .sort_values(ascending=False).head(5).round(3))
print("Q5:\n", q5)

# Q6 (business framing)
# Recommendation: target month-to-month customers with incentives to move
# to annual contracts, and treat repeated support calls as an early-warning
# trigger for proactive outreach.
# Caveat: these are correlations from observational data — support calls may
# be a symptom of an underlying problem, not the cause of churn. To prove a
# retention action works, run a controlled experiment (A/B test) rather than
# assuming the model's drivers are causal levers.
