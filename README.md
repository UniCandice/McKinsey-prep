# Data Science HackerRank Prep — McKinsey / QuantumBlack DS II

Hands-on practice repo. One coherent fake business (an e-commerce company)
powers the SQL and pandas exercises; a telecom churn dataset powers the ML
and stats exercises. Every exercise file has TODOs; every folder has a
`solutions/` directory with verified, runnable answers.

## Setup (one time)

```bash
source venv/bin/activate        # venv already created; else: python3 -m venv venv && pip install -r requirements.txt
python generate_data.py         # regenerate datasets/ (deterministic, seed 42)
python sql/setup_db.py          # build sql/practice.db (SQLite)
```

Run everything from the repo root.

## The data

| File | Rows | What it is |
|---|---|---|
| `datasets/customers.csv` | 500 | customer_id, name, age, city, segment, signup_date (~12% never order — for LEFT JOIN drills) |
| `datasets/orders.csv` | 5,000 | order_id, customer_id, product_id, date, quantity, amount, status |
| `datasets/products.csv` | 30 | product_id, name, category, unit_price |
| `datasets/support_tickets.csv` | 800 | ticket_id, customer_id, issue_type, resolved, satisfaction |
| `datasets/employees.csv` | 60 | the classic dept/salary/manager table for GROUP BY & window functions |
| `datasets/churn.csv` | 2,025 | telecom churn for ML — **deliberately messy**: NaNs + duplicate rows |

## How to practise

**SQL** — write your query under each question, then run the whole file:

```bash
python sql/run_query.py sql/01_joins.sql
python sql/run_query.py "SELECT * FROM customers LIMIT 5"   # ad-hoc
```

1. `01_joins.sql` — LEFT/INNER/self joins, anti-joins, COALESCE
2. `02_groupby_having.sql` — GROUP BY, HAVING, WHERE-vs-HAVING
3. `03_window_functions.sql` — ROW_NUMBER / RANK / DENSE_RANK / LAG / running totals
4. `04_practice_questions.sql` — CTEs + assessment-style business questions

**pandas** — fill the `...` TODOs, then `python pandas/01_filtering.py`:

1. filtering & selecting · 2. groupby/agg/transform · 3. merges · 4. missing values & duplicates (run 04 before the ML section — it writes `churn_clean.csv`)

**python** — implement each function until the asserts pass:

```bash
python python/01_strings.py     # prints "All string exercises pass ✔"
```

**ml** — the full assessment workflow on churn data:

1. logistic regression (features → split → baseline → fit → coefficients → business framing)
2. random forest (overfitting diagnosis, cross-validation, feature importance)
3. evaluation (confusion matrix, precision/recall/F1/AUC, precision@k, threshold tuning)

**stats** — A/B test from scratch (z-test + simulation), confidence intervals (formula + bootstrap), correlation ≠ causation.

## Suggested 2-hour session

| Time | Do |
|---|---|
| 0–30 | `sql/01`–`03`, then as much of `04` as you can |
| 30–60 | `pandas/01`–`04` |
| 60–90 | `ml/01`–`03` |
| 90–110 | `stats/01`–`02` |
| 110–120 | `python/` drills, speed-run the asserts |

Then take `mock_exam.md` under timed conditions (90 min).

## Rules that make this work

- Type every answer yourself — no copy-paste from solutions.
- Only open `solutions/` after a real attempt (or 5 minutes stuck).
- Say your answer to the "business framing" questions **out loud** — the
  communication questions are where candidates actually differentiate.

## Final checklist

- [ ] SQL query with JOIN + GROUP BY + HAVING + ROW_NUMBER in one go (sql/03 Q2, sql/04 Q7)
- [ ] Merge two DataFrames and compute grouped stats (pandas/03 Q5)
- [ ] Logistic Regression vs Random Forest — when and why (ml/02 Q5)
- [ ] Precision, recall, F1, ROC AUC — one sentence each (ml/03 Q2)
- [ ] Overfitting and how cross-validation catches it (ml/02 Q1–Q3)
- [ ] Clean data: NaNs, duplicates, filtering (pandas/04)
- [ ] Lists/dicts/loops under time pressure (python/)
- [ ] Explain a model choice to a non-technical client (ml/03 Q5, stats/01 Q6)
