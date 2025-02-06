--  1. List all unique cities where customers are located.
select distinct customer_city from customers;

-- 2. Count the number of orders placed in 2017.
select  count(order_id) from orders where year(order_purchase_timestamp) = '2017';

-- 3. Find the total sales per category.
SELECT p.product_category AS category, 
       SUM(py.payment_value) AS sales
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN payments py ON py.order_id = oi.order_id
GROUP BY category;