-- SOLUTIONS 04: Mixed business questions

-- Q1
SELECT c.customer_name, c.segment,
       COUNT(*) AS n_orders,
       ROUND(SUM(o.amount), 2) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY o.customer_id, c.customer_name, c.segment
ORDER BY revenue DESC
LIMIT 10;

-- Q2
SELECT c.segment, ROUND(AVG(o.amount), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.segment;

-- Q3
WITH spend AS (
    SELECT customer_id, SUM(amount) AS total
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
)
SELECT COUNT(*) AS big_spenders
FROM spend
WHERE total > 2 * (SELECT AVG(total) FROM spend);

-- Q4
WITH last_order AS (
    SELECT customer_id, MAX(order_date) AS last_date
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
)
SELECT c.customer_name, c.city, l.last_date
FROM last_order l
JOIN customers c ON l.customer_id = c.customer_id
WHERE julianday((SELECT MAX(order_date) FROM orders)) - julianday(l.last_date) > 90
ORDER BY l.last_date;

-- Q5
SELECT p.category,
       ROUND(100.0 * SUM(o.status = 'returned') / COUNT(*), 1) AS return_rate_pct
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY return_rate_pct DESC;

-- Q6
WITH spend AS (
    SELECT customer_id, SUM(amount) AS total
    FROM orders WHERE status = 'completed' GROUP BY customer_id
),
has_ticket AS (
    SELECT DISTINCT customer_id FROM support_tickets
)
SELECT CASE WHEN t.customer_id IS NULL THEN 'no ticket' ELSE 'has ticket' END AS grp,
       ROUND(AVG(s.total), 2) AS avg_spend,
       COUNT(*) AS n_customers
FROM spend s
LEFT JOIN has_ticket t ON s.customer_id = t.customer_id
GROUP BY grp;

-- Q7
WITH spend AS (
    SELECT c.city, c.customer_name, SUM(o.amount) AS total,
           ROW_NUMBER() OVER (PARTITION BY c.city ORDER BY SUM(o.amount) DESC) AS rk
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.status = 'completed'
    GROUP BY c.city, c.customer_id, c.customer_name
)
SELECT city, customer_name, ROUND(total, 2) AS total
FROM spend
WHERE rk = 1
ORDER BY total DESC;
