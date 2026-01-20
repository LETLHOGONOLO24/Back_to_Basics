/*

Tasks
-Calculate daily revenue
-Compute a 3-day moving average using a window function
-Display date, daily revenue, and moving average

*/

CREATE TABLE sales_day4 (
	date DATE NOT NULL,
	product VARCHAR(255) NOT NULL,
	category VARCHAR(100) NOT NULL,
	units_sold INTEGER,
	price NUMERIC NOT NULL
);

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-01', 'Laptop', 'Electronics', '2', '12000');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-02', 'Laptop', 'Electronics', '3', '12000');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-03', 'Laptop', 'Electronics', '1', '12000');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-04', 'Monitor', 'Electronics', '2', '4200');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-05', 'Monitor', 'Electronics', '3', '4200');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-06', 'Chair', 'Furniture', '4', '1500');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-07', 'Chair', 'Furniture', '2', '1500');

INSERT INTO sales_day4 (date, product, category, units_sold, price)
VALUES ('2024-01-08', 'Desk', 'Furniture', '1', '3500');

SELECT * FROM sales_day4

-- Calculate daily revenue 

SELECT
	date,
	SUM(units_sold * price) AS daily_revenue 
FROM sales_day4
GROUP BY date
ORDER BY date;

-- Compute a 3-day moving average using a window function
-- Display date, daily_revenue, and moving average

SELECT
	date,
	daily_revenue,
	AVG(daily_revenue) OVER (
		ORDER BY date
		ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
	) AS moving_avg_3day
FROM (
	SELECT
		date,
		SUM(units_sold * price) AS daily_revenue
	FROM sales_day4
	GROUP BY date
) AS daily_sales
ORDER BY date;

