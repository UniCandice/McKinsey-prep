-- ============================================================
-- 03: Window functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, running totals)
-- Tables: employees, orders
-- Run with: python sql/run_query.py sql/03_window_functions.sql
-- ============================================================

-- Q1. Rank employees by salary WITHIN each department (highest = 1)
--     using ROW_NUMBER(). Show name, department, salary, rank.
-- YOUR QUERY:



-- Q2. The classic: return only the TOP 2 earners per department.
--     (Hint: wrap Q1 in a subquery or CTE, then filter rank <= 2)
-- YOUR QUERY:



-- Q3. Same as Q1 but with RANK() and DENSE_RANK() side by side.
--     Find a department where the outputs differ and explain why.
-- YOUR QUERY:



-- Q4. For each customer's orders, show order_date, amount, and the
--     PREVIOUS order's amount (LAG). Do it for customer_id = 1
--     if they have orders, otherwise pick any active customer.
-- YOUR QUERY:



-- Q5. Running total of company revenue by order_date
--     (SUM(...) OVER (ORDER BY order_date)). Completed orders only,
--     limit 20 rows.
-- YOUR QUERY:



-- Q6. Each employee's salary vs their department's average salary,
--     and the difference — WITHOUT a self-join.
--     (Hint: AVG(salary) OVER (PARTITION BY department))
-- YOUR QUERY:

