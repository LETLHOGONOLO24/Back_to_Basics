/*

Tasks
-Calculate total revenue
-Calculate total marketing spend

-Compute revenue per rand of marketing spend
-Show KPIs per category

*/

CREATE TABLE sales_day5 (
	date DATE NOT NULL,
	product VARCHAR(255) NOT NULL,
	category VARCHAR(100) NOT NULL,
	units_sold INTEGER,
	price NUMERIC NOT NULL,
	marketing_spend NUMERIC NOT NULL
);

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-01', 'Laptop', 'Electronics', '2', '12000', '5000');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-02', 'Laptop', 'Electronics', '3', '12000', '6000');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-03', 'Monitor', 'Electronics', '1', '4200', '2000');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-04', 'Monitor', 'Electronics', '2', '4200', '2500');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-05', 'Chair', 'Furniture', '4', '1500', '1500');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-06', 'Chair', 'Furniture', '3', '1500', '1200');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-07', 'Desk', 'Furniture', '1', '3500', '1800');

INSERT INTO sales_day5 (date, product, category, units_sold, price, marketing_spend)
VALUES ('2024-01-08', 'Desk', 'Furniture', '2', '3500', '2200');

SELECT * FROM sales_day5

-- Calculate total revenue
-- Calculate total marketing spend
-- Compute Revenue per Rand of marketing spend

SELECT
	category,
	SUM(units_sold * price) AS total_revenue,

	SUM(marketing_spend) AS total_marketing_spend,
	
	-- We multiply by 1.0 to ensure decimal precision (avoiding integer division)
	ROUND(SUM(units_sold * price) * 1.0 / SUM(marketing_spend), 2) AS rev_per_rand_spent

FROM sales_day5
GROUP BY category
ORDER BY rev_per_rand_spent DESC;

