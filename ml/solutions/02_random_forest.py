"""SOLUTIONS 02: Random forest + cross-validation + overfitting"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split

df = pd.read_csv("datasets/churn_clean.csv")
X = pd.get_dummies(
    df.drop(columns=["customer_id", "churn"], errors="ignore")
      .drop(columns=["tenure_band"], errors="ignore"),
    drop_first=True)
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Q1 — unconstrained forest: near-perfect train accuracy = overfitting
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
print("Q1 train acc:", round(accuracy_score(y_train, rf.predict(X_train)), 3),
      " test acc:", round(accuracy_score(y_test, rf.predict(X_test)), 3))

# Q2 — limiting depth shrinks the gap (less memorisation)
rf6 = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
rf6.fit(X_train, y_train)
print("Q2 train acc:", round(accuracy_score(y_train, rf6.predict(X_train)), 3),
      " test acc:", round(accuracy_score(y_test, rf6.predict(X_test)), 3))

# Q3 — CV averages over 5 different splits, so the estimate doesn't
# depend on one lucky/unlucky split
scores = cross_val_score(rf6, X, y, cv=5)
print(f"Q3 CV accuracy: {scores.mean():.3f} ± {scores.std():.3f}")

# Q4
q4 = (pd.Series(rf6.feature_importances_, index=X.columns)
      .sort_values(ascending=False).head(5).round(3))
print("Q4:\n", q4)

# Q5 (interview answer)
# Pick logistic regression over a slightly better forest when:
# - stakeholders/regulators must understand each feature's effect
#   (coefficients read as "one more support call multiplies churn odds by X")
# - you have little data (forests overfit small samples)
# - you need a simple, cheap, easily monitored model in production
# - the 2-point gap may not be real anyway — check CV std first.
