# Mock Assessment — 90 minutes, timed

Simulates a QuantumBlack-style HackerRank round. Set a timer. No solutions
folder until the timer ends. Everything uses `datasets/` and `sql/practice.db`.

**Scenario:** You're advising an online retailer. Leadership wants to know
who their best customers are, whether support problems drive customers
away, and whether you can predict churn.

---

## Part 1 — SQL (25 min)

1. Top 10 customers by completed-order revenue: name, segment, order
   count, revenue.
2. Monthly revenue for 2024 only. In one sentence: is revenue growing?
3. For each product category: revenue, number of orders, and return rate
   (% of orders with status 'returned').
4. Using a CTE and ROW_NUMBER(): the single top-spending customer **per
   segment**.
5. Customers with 2+ unresolved support tickets AND at least one completed
   order — name, city, number of unresolved tickets.

## Part 2 — pandas (25 min)

6. Load orders + customers. Build a one-row-per-customer table:
   `n_orders`, `total_spend`, `avg_order_value`, `n_tickets`,
   `days_since_last_order` (relative to the max order_date in the data).
   No NaNs allowed in the output.
7. Which customer segment has the highest average order value, and is the
   difference big enough to care about? (Show the numbers that justify
   your answer.)
8. Flag "at-risk" customers: no completed order in the last 90 days but
   total_spend in the top 25%. How many are there?

## Part 3 — ML (30 min)

9. Load `datasets/churn.csv`. Clean it (duplicates, NaNs — justify your
   imputation choice in a comment).
10. Train a model to predict churn. Report accuracy **against the
    majority-class baseline**, plus precision, recall and ROC AUC on a
    held-out test set.
11. The retention team can contact 300 customers. Which 300 do you give
    them, and what churn-capture rate should they expect?
12. Three-sentence summary for the client: biggest churn driver, what you
    recommend, and one caveat.

## Part 4 — Communication (10 min, answer in plain text)

13. "Your model is 88% accurate. Our old rule-of-thumb (flag anyone with
    3+ support calls) was 85%. Why should we pay for yours?" — answer in
    under 100 words, no jargon.

---

**Marking yourself:** correctness first, but also — did you check the churn
base rate before quoting accuracy? Did every SQL answer use the `completed`
filter where it mattered? Did Part 4 mention costs/recall rather than just
"ML is better"?
