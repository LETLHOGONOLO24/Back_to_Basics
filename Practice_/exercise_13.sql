/*

Tasks
-Calculate total revenue per category
-Show only categories where total revenue > 5000
-Order results by total revenue descending

*/

CREATE TABLE sales_day3 (
	date DATE NOT NULL,
	product VARCHAR(255) NOT NULL,
	category VARCHAR(100) NOT NULL,
	units_sold INTEGER,
	price NUMERIC NOT NULL
);

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-01', 'Laptop', 'Electronics', '2', '12000');

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-01', 'Mouse', 'Electronics', NULL, '250');

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-02', 'Keyboard', 'Electronics', '3', '450');

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-02', 'Desk', 'Furniture', '1', '1500');

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-03', 'Chair', 'Furniture', '2', '1500');

INSERT INTO sales_day3 (date, product, category, units_sold, price)
VALUES ('2024-01-03', 'Monitor', 'Electronics', NULL, '4200');

SELECT * FROM sales_day3

-- Calculate total revenue per category

SELECT
	category,
	SUM(COALESCE(units_sold, 0) * price) AS total_revenue -- COALESCE() says if units_sold has a NULL value, use 0 instead
FROM sales_day3
GROUP BY category
ORDER BY total_revenue DESC;

-- Lets show only categories where total revenue > 5000

SELECT
	category,
	SUM(
		CASE
			WHEN units_sold IS NOT NULL AND price IS NOT NULL
			THEN units_sold * price
			ELSE 0
		END
	) AS total_revenue
FROM sales_day3
GROUP BY category
HAVING SUM(
	CASE
		WHEN units_sold IS NOT NULL AND price IS NOT NULL
		THEN units_sold * price
		ELSE 0
	END
) > 5000
ORDER BY total_revenue DESC;


