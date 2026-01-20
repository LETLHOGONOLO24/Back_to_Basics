/*

Tasks

- Join customers and orders
- Show customer name, city, and total revenue per customer
- Order results by total revenue (descending)

*/

CREATE TABLE customers (
	customer_id INTEGER NOT NULL,
	customer_name VARCHAR(255),
	city VARCHAR(100),
	PRIMARY KEY (customer_id)
);

INSERT INTO customers (customer_id, customer_name, city)
VALUES ('1', 'Alice', 'Johannesburg');

INSERT INTO customers (customer_id, customer_name, city)
VALUES ('2', 'Bongani', 'Pretoria');

INSERT INTO customers (customer_id, customer_name, city)
VALUES ('3', 'Chipo', 'Cape Town');

INSERT INTO customers (customer_id, customer_name, city)
VALUES ('4', 'David', 'Durban');

SELECT * FROM customers

CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY,
	customer_id INTEGER NOT NULL,
	order_date DATE NOT NULL,
	product VARCHAR(255),
	units_sold INTEGER,
	price NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('101', '1', '2024-01-01', 'Laptop', '1', '12000');

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('102', '2', '2024-01-02', 'Mouse', '2', '250');

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('103', '2', '2024-01-02', 'Keyboard', '1', '450');

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('104', '3', '2024-01-03', 'Chair', '2', '1500');

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('105', '4', '2024-01-04', 'Desk', '1', '3500');

INSERT INTO orders (order_id, customer_id, order_date, product, units_sold, price)
VALUES ('106', '3', '2024-01-04', 'Monitor', '1', '4200');

SELECT * FROM orders

SELECT 
	c.customer_name,
	c.city,
	SUM(o.units_sold * o.price) AS total_revenue
FROM customers c
INNER JOIN orders o ON c.customer_id=o.customer_id
GROUP BY c.customer_name, c.city
ORDER BY total_revenue DESC


