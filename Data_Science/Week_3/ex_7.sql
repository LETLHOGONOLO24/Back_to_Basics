/*

*Find all sales where:
-quantity is greater than 3
-AND price is greater than 800

*Find sales where:
-product_id is either 1,3, or 5

*Find sales between:
-2024-01-15 and 2024-02-15

*Find sales where:
-price is between 500 and 1000
*Count how many transactions happened in each month

*/



SELECT * from sales WHERE quantity > 3 AND price > 800;

SELECT * FROM sales WHERE Product_id BETWEEN 1 AND 5;

SELECT * FROM sales WHERE sale_date BETWEEN '2024-01-15' AND '2024-02-15';

SELECT * FROM sales WHERE price BETWEEN 500 AND 1000;

SELECT * ,
	CASE
		WHEN price > 3000 THEN 'High'
		WHEN price BETWEEN 1500 AND 3000 THEN 'Medium'
		ELSE 'Low'
	END AS transaction_classification
FROM sales

----------------------------------------------------------------

SELECT 
    CASE 
        WHEN price > 3000 THEN 'High'
        WHEN price BETWEEN 1500 AND 3000 THEN 'Medium'
        ELSE 'Low'
    END AS transaction_class,
    COUNT(*) AS number_of_transactions
FROM sales
GROUP BY 
    CASE 
        WHEN price > 3000 THEN 'High'
        WHEN price BETWEEN 1500 AND 3000 THEN 'Medium'
        ELSE 'Low'
    END
ORDER BY 
    MIN(price) DESC;  -- Optional: orders by High → Medium → Low