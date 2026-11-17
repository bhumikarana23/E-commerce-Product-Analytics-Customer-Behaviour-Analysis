-- MySQL 8.0+ analysis queries
USE ecommerce_analytics;

-- 1. Dataset counts
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL SELECT 'products', COUNT(*) FROM products
UNION ALL SELECT 'events', COUNT(*) FROM events
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'order_items', COUNT(*) FROM order_items;

-- 2. Event counts
SELECT event_type, COUNT(*) AS events, COUNT(DISTINCT session_id) AS sessions
FROM events GROUP BY event_type ORDER BY FIELD(event_type,'view_product','add_to_cart','begin_checkout','purchase');

-- 3. Shopping funnel: distinct sessions reaching each stage
WITH stages AS (
  SELECT
    COUNT(DISTINCT CASE WHEN event_type='view_product' THEN session_id END) AS view_sessions,
    COUNT(DISTINCT CASE WHEN event_type='add_to_cart' THEN session_id END) AS cart_sessions,
    COUNT(DISTINCT CASE WHEN event_type='begin_checkout' THEN session_id END) AS checkout_sessions,
    COUNT(DISTINCT CASE WHEN event_type='purchase' THEN session_id END) AS purchase_sessions
  FROM events
)
SELECT 'Product views' AS stage, view_sessions AS sessions, 100.0 AS pct_of_viewers FROM stages
UNION ALL SELECT 'Add to cart', cart_sessions, ROUND(100.0*cart_sessions/NULLIF(view_sessions,0),2) FROM stages
UNION ALL SELECT 'Begin checkout', checkout_sessions, ROUND(100.0*checkout_sessions/NULLIF(view_sessions,0),2) FROM stages
UNION ALL SELECT 'Purchase', purchase_sessions, ROUND(100.0*purchase_sessions/NULLIF(view_sessions,0),2) FROM stages;

-- 4. Cart abandonment rate by session
WITH cart_sessions AS (
 SELECT session_id, MAX(event_type='purchase') AS purchased
 FROM events
 GROUP BY session_id
 HAVING MAX(event_type='add_to_cart')=1
)
SELECT COUNT(*) AS cart_sessions,
       SUM(purchased) AS converted_sessions,
       ROUND(100*(1-AVG(purchased)),2) AS cart_abandonment_pct
FROM cart_sessions;

-- 5. Checkout abandonment rate
WITH checkout_sessions AS (
 SELECT session_id, MAX(event_type='purchase') AS purchased
 FROM events
 GROUP BY session_id
 HAVING MAX(event_type='begin_checkout')=1
)
SELECT COUNT(*) AS checkout_sessions,
       SUM(purchased) AS converted_sessions,
       ROUND(100*(1-AVG(purchased)),2) AS checkout_abandonment_pct
FROM checkout_sessions;

-- 6. Conversion by device
WITH session_level AS (
 SELECT session_id, MAX(device_type) AS device_type,
        MAX(event_type='purchase') AS purchased
 FROM events GROUP BY session_id
)
SELECT device_type, COUNT(*) AS sessions, SUM(purchased) AS purchases,
       ROUND(100*AVG(purchased),2) AS session_conversion_pct
FROM session_level GROUP BY device_type ORDER BY session_conversion_pct DESC;

-- 7. Conversion by traffic source
WITH session_level AS (
 SELECT session_id, MAX(traffic_source) AS traffic_source,
        MAX(event_type='purchase') AS purchased
 FROM events GROUP BY session_id
)
SELECT traffic_source, COUNT(*) AS sessions, SUM(purchased) AS purchases,
       ROUND(100*AVG(purchased),2) AS session_conversion_pct
FROM session_level GROUP BY traffic_source ORDER BY session_conversion_pct DESC;

-- 8. Category performance
SELECT p.category, COUNT(DISTINCT e.event_id) AS product_views,
       COUNT(DISTINCT oi.order_item_id) AS order_lines,
       COALESCE(SUM(oi.quantity),0) AS units_sold,
       COALESCE(SUM(oi.line_total_inr),0) AS item_revenue_inr
FROM products p
LEFT JOIN events e ON p.product_id=e.product_id AND e.event_type='view_product'
LEFT JOIN order_items oi ON p.product_id=oi.product_id
GROUP BY p.category ORDER BY item_revenue_inr DESC;

-- 9. Top 20 products by revenue
SELECT p.product_id, p.product_name, p.category,
       SUM(oi.quantity) AS units_sold,
       SUM(oi.line_total_inr) AS item_revenue_inr
FROM order_items oi JOIN products p ON oi.product_id=p.product_id
GROUP BY p.product_id,p.product_name,p.category
ORDER BY item_revenue_inr DESC LIMIT 20;

-- 10. Average order value by order status
SELECT order_status, COUNT(*) AS orders,
       ROUND(AVG(total_amount_inr),2) AS avg_order_value_inr,
       SUM(total_amount_inr) AS total_order_value_inr
FROM orders GROUP BY order_status;

-- 11. Monthly order trend
SELECT DATE_FORMAT(order_date,'%Y-%m') AS order_month,
       COUNT(*) AS orders,
       COUNT(DISTINCT customer_id) AS customers,
       SUM(total_amount_inr) AS gross_order_value_inr
FROM orders GROUP BY DATE_FORMAT(order_date,'%Y-%m')
ORDER BY order_month;

-- 12. New vs repeat buyers (based on number of placed orders)
WITH customer_orders AS (
 SELECT customer_id, COUNT(*) AS order_count,
        SUM(total_amount_inr) AS lifetime_order_value
 FROM orders GROUP BY customer_id
)
SELECT CASE WHEN order_count>1 THEN 'Repeat buyer' ELSE 'One-time buyer' END AS buyer_type,
       COUNT(*) AS customers, SUM(lifetime_order_value) AS order_value_inr
FROM customer_orders GROUP BY buyer_type;

-- 13. Customer purchase frequency and spend
SELECT c.customer_id, c.age_group, c.city,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.total_amount_inr),0) AS total_spend_inr,
       MAX(o.order_date) AS latest_order_date
FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id
GROUP BY c.customer_id,c.age_group,c.city
ORDER BY total_spend_inr DESC;

-- 14. Discount vs order value
SELECT CASE
         WHEN discount_inr=0 THEN 'No discount'
         WHEN discount_inr<100 THEN '1-99'
         WHEN discount_inr<200 THEN '100-199'
         ELSE '200+'
       END AS discount_band,
       COUNT(*) AS orders,
       ROUND(AVG(total_amount_inr),2) AS avg_order_value_inr
FROM orders GROUP BY discount_band ORDER BY orders DESC;

-- 15. Returns and cancellations
SELECT order_status, COUNT(*) AS orders,
       ROUND(100*COUNT(*)/(SELECT COUNT(*) FROM orders),2) AS share_of_orders_pct
FROM orders GROUP BY order_status;

-- 16. Product views and cart additions by product
SELECT p.product_id,p.product_name,p.category,
       COUNT(DISTINCT CASE WHEN e.event_type='view_product' THEN e.session_id END) AS view_sessions,
       COUNT(DISTINCT CASE WHEN e.event_type='add_to_cart' THEN e.session_id END) AS cart_sessions
FROM products p LEFT JOIN events e ON p.product_id=e.product_id
GROUP BY p.product_id,p.product_name,p.category
ORDER BY view_sessions DESC;

-- 17. Customer acquisition cohort by signup month
SELECT DATE_FORMAT(c.signup_date,'%Y-%m') AS signup_month,
       COUNT(DISTINCT c.customer_id) AS customers,
       COUNT(DISTINCT o.customer_id) AS customers_with_orders
FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id
GROUP BY signup_month ORDER BY signup_month;
