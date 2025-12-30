CREATE TABLE sales (
	date DATE NOT NULL,
	product VARCHAR(255),
	category VARCHAR(100),
	units_sold INTEGER,
	price NUMERIC(10, 2)
);

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-01', 'Laptop', 'Electronics', '5', '12000');

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-01', 'Mouse', 'Electronics', '20', '250');

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-02', 'Keyboard', 'Electronics', '10', '450');

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-02', 'Desk', 'Furniture', '8', '1500');

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-03', 'Chair', 'Furniture', '8', '1500');

INSERT INTO sales (date, product, category, units_sold, price)
VALUES ('2024-01-03', 'Monitor', 'Electronics', '6', '4200');

SELECT * FROM sales

SELECT * FROM sales WHERE category = 'Electronics'

SELECT SUM(units_sold)
FROM sales
WHERE category = 'Electronics'

SELECT SUM(units_sold)
FROM sales
WHERE category = 'Furniture'

SELECT SUM(price)
FROM sales
WHERE category = 'Electronics'

SELECT SUM(price)
FROM sales
WHERE category = 'Furniture'
