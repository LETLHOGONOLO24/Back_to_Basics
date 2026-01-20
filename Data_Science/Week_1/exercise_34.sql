/*

Tasks
-Join employees and transactions
-Calculate per employee:
	-Total units processed
	-Total errors

	-Error rate
-Filter employees with Error rate > 3%

*/

CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	department VARCHAR(50)
);

INSERT INTO employees (employee_id, employee_name, department)
VALUES ('1', 'Thabo', 'Sales');

INSERT INTO employees (employee_id, employee_name, department)
VALUES ('2', 'Naledi', 'Sales');

INSERT INTO employees (employee_id, employee_name, department)
VALUES ('3', 'Amara', 'Operations');

INSERT INTO employees (employee_id, employee_name, department)
VALUES ('4', 'Kabelo', 'Operations');

SELECT * FROM employees;

CREATE TABLE transactions (
	transaction_id INT PRIMARY KEY,
	employee_id INT,
	date DATE,
	units_processed NUMERIC NULL,
	errors_made INT
)

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1001', '1','2024-01-01', '120', '2');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1002', '2','2024-01-01', '90', '5');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1003', '3','2024-01-01', '200', '1');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1004', '4','2024-01-01', '180', '0');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1005', '1','2024-01-02', '140', '3');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1006', '2','2024-01-02', NULL, '2');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1007', '3','2024-01-02', '210', '2');

INSERT INTO transactions (transaction_id, employee_id, date, units_processed, errors_made)
VALUES ('1008', '4','2024-01-02', '190', '1');

SELECT * FROM transactions

-- Calculare total units processed per employee 

SELECT
	e.employee_name,
	SUM(t.units_processed) AS total_units
FROM employees e
JOIN transactions t ON e.employee_id = t.employee_id
GROUP BY e.employee_name;

-- Total errors per employee

SELECT
	e.employee_name,
	SUM(t.errors_made) AS total_errors
FROM employees e
JOIN transactions t ON e.employee_id = t.employee_id
GROUP BY e.employee_name;

-- Calculating the error rate

SELECT
	e.employee_name,
	SUM(t.errors_made) * 1.0 / SUM(t.units_processed) AS error_rate
FROM employees e
JOIN transactions t ON e.employee_id = t.employee_id
GROUP BY e.employee_name;

-- Filtering for the high error threshold(> 3%)

SELECT
	e.employee_name,
	SUM(t.errors_made) * 1.0 / SUM(t.units_processed) AS error_rate
FROM employees e
JOIN transactions t ON e.employee_id = t.employee_id
GROUP BY e.employee_name
HAVING (SUM(t.errors_made) * 1.0 / SUM(t.units_processed)) > 0.03;
