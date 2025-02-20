SELECT AVG(sales) AS average_order_value FROM sales;


SELECT 
    EXTRACT(MONTH FROM order_date) AS month, 
    AVG(sales) AS average_revenue
FROM sales
GROUP BY month
ORDER BY month;
