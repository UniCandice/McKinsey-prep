"""SOLUTIONS 03: Model evaluation"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/churn_clean.csv")
X = pd.get_dummies(
    df.drop(columns=["customer_id", "churn"], errors="ignore")
      .drop(columns=["tenure_band"], errors="ignore"),
    drop_first=True)
y = df["churn"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

# Q1
cm = confusion_matrix(y_test, pred)
print("Q1 confusion matrix:\n", cm)
# [[TN FP]     FN (bottom-left) = actual churner predicted as staying —
#  [FN TP]]    the churner we missed, usually the most expensive mistake.

# Q2
print("Q2 accuracy :", round(accuracy_score(y_test, pred), 3))
print("   precision:", round(precision_score(y_test, pred), 3))
print("   recall   :", round(recall_score(y_test, pred), 3))
print("   F1       :", round(f1_score(y_test, pred), 3))
print("   ROC AUC  :", round(roc_auc_score(y_test, proba), 3))
# Precision: of the customers we flagged as churners, the share that
#            actually churned.
# Recall:    of all customers who actually churned, the share we caught.

# Q3 — precision@k / recall@k, how targeting budgets actually work
k = int(0.2 * len(y_test))
top_idx = np.argsort(proba)[::-1][:k]
top_actual = y_test.to_numpy()[top_idx]
print(f"Q3 precision@20%: {top_actual.mean():.3f}   "
      f"recall@20%: {top_actual.sum() / y_test.sum():.3f}")

# Q4 — threshold trades precision against recall
for t in (0.3, 0.5, 0.7):
    p = (proba >= t).astype(int)
    print(f"Q4 threshold {t}: precision {precision_score(y_test, p):.3f}  "
          f"recall {recall_score(y_test, p):.3f}")
# Cheap offer (£5): missing a churner costs far more than a wasted offer,
#   so LOWER the threshold (0.3) and maximise recall.
# Expensive offer (£200): false positives are costly, so RAISE the
#   threshold (0.7) and prioritise precision.

# Q5 — "95% vs 90% accuracy, which model?"
# Strong answer: accuracy alone can't decide it.
# - Base rate: if only 5% churn, predicting "nobody churns" is 95% accurate
#   and useless. Compare against that baseline.
# - Costs: what do false positives vs false negatives cost the business?
#   Compare precision/recall (or expected cost) at the real operating point.
# - Also weigh interpretability, inference speed, maintenance, robustness
#   and fairness. Recommend the model that maximises business value, not
#   the accuracy number.
