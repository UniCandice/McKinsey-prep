"""01: Logistic regression on churn — the full basic ML workflow.

Prereq: run pandas/solutions/04_missing_values.py first (creates
datasets/churn_clean.csv), or clean churn.csv yourself.

Fill in each TODO, then run:  python ml/01_logistic_regression.py
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/churn_clean.csv")

# Q1. Build the feature matrix X and target y.
#     - target: churn
#     - drop: customer_id (it's an ID, not a feature) and tenure_band
#       if present
#     - one-hot encode contract_type and payment_method with
#       pd.get_dummies(..., drop_first=True)
X = ...
y = ...
print("Q1 X shape:", X.shape)

# Q2. Split 80/20 with random_state=42, stratified on y.
#     Why stratify? So both splits keep the same churn rate.
X_train, X_test, y_train, y_test = ...
print("Q2 train churn rate:", round(y_train.mean(), 3),
      "test churn rate:", round(y_test.mean(), 3))

# Q3. Baseline first! What accuracy do you get by always predicting
#     'no churn'? Any model must beat this number.
baseline = ...
print("Q3 baseline accuracy:", round(baseline, 3))

# Q4. Fit LogisticRegression(max_iter=1000) on the training data and
#     report test accuracy.
model = ...
acc = ...
print("Q4 test accuracy:", round(acc, 3))

# Q5. Which features push churn UP the most? Look at model.coef_
#     paired with X.columns, sorted. (Positive coefficient = increases
#     churn probability.) Print the top 5.
q5 = ...
print("Q5:\n", q5)

# Q6. Business framing (write your answer as a comment):
#     The model says month-to-month contracts and support calls drive
#     churn. What would you tell the client to DO about it, and what
#     caveat applies? (correlation vs causation)
