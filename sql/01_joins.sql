-- ============================================================
-- 01: JOINs
-- Tables: customers, orders, products
-- Run with: python sql/run_query.py sql/01_joins.sql
-- Solutions: sql/solutions/01_joins.sql
-- ============================================================

-- Q1. List every customer's name and their order ids.
--     Include customers who have never placed an order (they should
--     appear with NULL order_id). Limit to 20 rows.
-- YOUR QUERY:



-- Q2. How many customers have NEVER placed an order?
--     (Hint: LEFT JOIN ... WHERE ... IS NULL, or NOT IN)
-- YOUR QUERY:



-- Q3. Show order_id, customer_name, product_name and amount for the
--     10 most expensive orders. (3-table join)
-- YOUR QUERY:



-- Q4. For each customer show name, city, and total amount spent on
--     'completed' orders. Customers with no completed orders should
--     show 0. Sort by total spent, highest first, top 15.
--     (Hint: COALESCE)
-- YOUR QUERY:



-- Q5. Self-join: using employees, show each employee's name next to
--     their manager's name. Managers themselves have NULL manager_id.
-- YOUR QUERY:

