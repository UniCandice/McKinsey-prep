-- SOLUTIONS 01: JOINs

-- Q1
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LIMIT 20;

-- Q2
SELECT COUNT(*) AS never_ordered
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Q3
SELECT o.order_id, c.customer_name, p.product_name, o.amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
ORDER BY o.amount DESC
LIMIT 10;

-- Q4
SELECT c.customer_name,
       c.city,
       COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id AND o.status = 'completed'
GROUP BY c.customer_id, c.customer_name, c.city
ORDER BY total_spent DESC
LIMIT 15;
-- Note: the status filter lives in the ON clause, not WHERE —
-- putting it in WHERE would silently turn the LEFT JOIN into an INNER JOIN.

-- Q5
SELECT e.employee_name AS employee,
       m.employee_name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
