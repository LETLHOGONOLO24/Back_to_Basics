CREATE TABLE sales (
    sale_id INT,
    order_id INT,
    product_id INT,
    customer_id INT,
    quantity INT,
    price INT,
    sale_date DATE
);

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('1', '1020', '1', '20', '5', '625', '2024-01-14');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('2', '1032', '2', '16', '5', '798', '2024-10-14');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('3', '1075', '2', '13', '3', '1435', '2024-04-11');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('4', '1057', '6', '18', '4', '982', '2024-11-28');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('5', '1021', '7', '10', '5', '1130', '2024-12-25');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('6', '1088', '5', '19', '4', '1126', '2024-10-06');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('7', '1048', '1', '17', '3', '1746', '2024-08-02');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('8', '1090', '1', '19', '3', '1018', '2024-04-22');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('9', '1058', '3', '5', '4', '849', '2024-08-17');

INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date)
VALUES ('10', '1041', '2', '9', '1', '462', '2024-10-28');

-- Retrieving all columns from the table

SELECT * FROM sales

-- Retrieve only product_id, quantity, price

SELECT
	product_id, quantity, price
FROM sales;

-- Find all sales where price is greater than 1000

SELECT * FROM sales WHERE price > 1000;

-- Sort all sales from newest to oldest

SELECT * FROM sales
ORDER BY sale_date DESC;

-- Create a calculated column showing total transaction value

SELECT
	order_id,
	quantity,
	(quantity * price) AS total_transaction_value
FROM sales

-- Show only the first 5 rows

SELECT * FROM sales
LIMIT 5;

-- Find the highest single transaction value

SELECT
	MAX(quantity * price) AS total_transaction_value
FROM sales

-- Find the lowest single transaction value

SELECT
	MIN(quantity * price) AS total_transaction_value
FROM sales

-- Find the average transaction value

SELECT
	ROUND(AVG(quantity * price), 2) AS total_transaction_value
FROM sales

-- Count how many transactions exist in the table

SELECT
	COUNT(*) AS num_of_transactions
FROM sales

