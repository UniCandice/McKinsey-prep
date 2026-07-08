-- SOLUTIONS 03: Window functions

-- Q1
SELECT employee_name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rk
FROM employees;

-- Q2
WITH ranked AS (
    SELECT employee_name, department, salary,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rk
    FROM employees
)
SELECT * FROM ranked WHERE rk <= 2;

-- Q3
SELECT employee_name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
       RANK()       OVER (PARTITION BY department ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rnk
FROM employees;
-- With tied salaries: ROW_NUMBER gives 1,2,3,4 arbitrarily.
-- RANK gives 1,2,2,4 (skips). DENSE_RANK gives 1,2,2,3 (no skip).

-- Q4
SELECT customer_id, order_date, amount,
       LAG(amount) OVER (ORDER BY order_date) AS prev_amount
FROM orders
WHERE customer_id = (SELECT customer_id FROM orders LIMIT 1);

-- Q5
SELECT order_date, amount,
       ROUND(SUM(amount) OVER (ORDER BY order_date, order_id), 2) AS running_total
FROM orders
WHERE status = 'completed'
LIMIT 20;

-- Q6
SELECT employee_name, department, salary,
       ROUND(AVG(salary) OVER (PARTITION BY department)) AS dept_avg,
       ROUND(salary - AVG(salary) OVER (PARTITION BY department)) AS diff_from_avg
FROM employees;
