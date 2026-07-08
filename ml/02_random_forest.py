"""02: Random forest + cross-validation + overfitting diagnosis.

Fill in each TODO, then run:  python ml/02_random_forest.py
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

df = pd.read_csv("datasets/churn_clean.csv")
X = pd.get_dummies(
    df.drop(columns=["customer_id", "churn"], errors="ignore")
      .drop(columns=["tenure_band"], errors="ignore"),
    drop_first=True)
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Q1. Fit RandomForestClassifier(n_estimators=200, random_state=42).
#     Print TRAIN accuracy and TEST accuracy. Is it overfitting?
#     (A big train-test gap = memorising the training data.)
...
print("Q1 train acc: ...  test acc: ...")

# Q2. Refit with max_depth=6. What happens to the train-test gap?
...
print("Q2 train acc: ...  test acc: ...")

# Q3. 5-fold cross-validation (cross_val_score) on the FULL X, y with
#     the depth-limited forest. Report mean and std of accuracy.
#     Why is this more trustworthy than a single split?
...
print("Q3 CV accuracy: mean ± std")

# Q4. Feature importances: top 5 via model.feature_importances_
#     paired with X.columns. Do they agree with the logistic
#     regression coefficients from exercise 01?
q4 = ...
print("Q4:\n", q4)

# Q5. Interview answer (write as a comment):
#     When would you pick logistic regression over a random forest,
#     even if the forest scores 2 points higher?
#     (Think: interpretability, monotonic effects, tiny data,
#      regulatory/explainability requirements, inference simplicity.)
