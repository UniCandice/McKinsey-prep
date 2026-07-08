-- SOLUTIONS 02: GROUP BY / HAVING

-- Q1
SELECT department, ROUND(AVG(salary)) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Q2
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
HAVING COUNT(*) > 8;

-- Q3
SELECT p.category, ROUND(SUM(o.amount), 2) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;

-- Q4
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(amount), 2) AS revenue
FROM orders
WHERE status = 'completed'
GROUP BY month
ORDER BY month;

-- Q5
SELECT c.customer_name,
       COUNT(*) AS n_orders,
       ROUND(SUM(o.amount), 2) AS total_spend
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY o.customer_id, c.customer_name
HAVING COUNT(*) >= 20
ORDER BY total_spend DESC;
-- Remember: WHERE filters rows BEFORE grouping, HAVING filters groups AFTER.

-- Q6
SELECT issue_type,
       ROUND(AVG(resolved) * 100, 1) AS pct_resolved,
       COUNT(*) AS n_tickets
FROM support_tickets
GROUP BY issue_type
ORDER BY pct_resolved;
