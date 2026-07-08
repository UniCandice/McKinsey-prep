-- ============================================================
-- 04: Mixed business questions (CTEs + everything so far)
-- These are shaped like real assessment questions.
-- Run with: python sql/run_query.py sql/04_practice_questions.sql
-- ============================================================

-- Q1. Top 10 customers by lifetime completed-order revenue.
--     Show name, segment, number of orders, total revenue.
-- YOUR QUERY:



-- Q2. Average order value (AOV) per customer segment.
-- YOUR QUERY:



-- Q3. Using a CTE: find customers whose total spend is above 2x the
--     average customer total spend. How many are there?
-- YOUR QUERY:



-- Q4. "At-risk" customers: customers whose LAST completed order was
--     more than 90 days before the latest order_date in the data.
--     Return name, city, last order date. (CTE + MAX + date math;
--     SQLite: julianday(a) - julianday(b) gives day difference)
-- YOUR QUERY:



-- Q5. Return rate per product category:
--     returned orders / all orders, as a percentage, sorted worst first.
-- YOUR QUERY:



-- Q6. Do customers who raised support tickets spend less?
--     Compare average total spend of customers WITH at least one
--     ticket vs customers WITHOUT any. (Two CTEs, or CASE WHEN)
-- YOUR QUERY:



-- Q7. For each city, find the single highest-spending customer.
--     (Classic "top-1 per group" — window function inside a CTE)
-- YOUR QUERY:

