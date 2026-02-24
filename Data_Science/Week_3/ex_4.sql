
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    customer_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    sale_date DATE
);

-- Insert values into sales table
INSERT INTO sales (sale_id, order_id, product_id, customer_id, quantity, price, sale_date) VALUES
(1, 1020, 1, 20, 5, 625.00, '2024-01-14'),
(2, 1032, 2, 16, 5, 798.00, '2024-10-14'),
(3, 1075, 2, 13, 3, 1435.00, '2024-04-11'),
(4, 1057, 6, 18, 4, 982.00, '2024-11-28'),
(5, 1021, 7, 10, 5, 1130.00, '2024-12-25'),
(6, 1088, 5, 19, 4, 1126.00, '2024-10-06'),
(7, 1048, 1, 17, 3, 1746.00, '2024-08-02');

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    cost_price DECIMAL(10, 2)
);

-- Insert values into products table
INSERT INTO products (product_id, product_name, category, cost_price) VALUES
(1, 'Laptop', 'Electronics', 152.00),
(2, 'Phone', 'Electronics', 485.00),
(3, 'Tablet', 'Electronics', 910.00),
(4, 'Headphones', 'Accessories', 320.00),
(5, 'Monitor', 'Electronics', 156.00),
(6, 'Keyboard', 'Accessories', 121.00),
(7, 'Mouse', 'Accessories', 750.00),
(8, 'Printer', 'Electronics', 70.00),
(9, 'Camera', 'Electronics', 664.00),
(10, 'Smartwatch', 'Electronics', 171.00);

-----------------------------------------------
