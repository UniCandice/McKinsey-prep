"""03: Model evaluation — precision, recall, F1, ROC AUC, thresholds.

This is the part McKinsey probes hardest: not "can you fit a model"
but "do you know what the numbers mean for the business".

Fill in each TODO, then run:  python ml/03_model_evaluation.py
"""
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
proba = model.predict_proba(X_test)[:, 1]  # P(churn)

# Q1. Print the confusion matrix and label its four cells in a comment
#     (TN / FP / FN / TP). Which cell is a "churner we missed"?
...

# Q2. Compute accuracy, precision, recall, F1 and ROC AUC.
#     Then, in a comment, define precision and recall in ONE sentence
#     each, in terms of churners.
...

# Q3. The retention team can only call 20% of customers. Take the 20%
#     of test customers with the highest predicted churn probability.
#     What fraction of them actually churned (precision@20%), and what
#     fraction of ALL churners did we capture (recall@20%)?
...

# Q4. Threshold tuning: default is 0.5. Compute precision and recall
#     at thresholds 0.3, 0.5 and 0.7. Which threshold would you use
#     if a retention offer is CHEAP (say £5)? If it's EXPENSIVE (£200)?
...

# Q5. The business question you WILL get, answer in a comment:
#     "Model A has 95% accuracy, Model B has 90%. Which do you pick?"
#     Sketch the strong answer: base rates (a 95%-accurate model on a
#     5%-churn base is the do-nothing model), cost of FP vs FN,
#     precision/recall at the operating point, interpretability,
#     inference/maintenance cost, business impact.
