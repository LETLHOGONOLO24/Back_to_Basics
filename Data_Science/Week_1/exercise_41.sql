/*

Tasks
-Assume table performance
-Compute efficiency score

-Rank employees within each department using RANK() or DENSE_RANK()
-Display employee name, department, and rank

*/

CREATE TABLE performance_day7 (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	department VARCHAR(50),
	units_processed NUMERIC,
	errors_made INTEGER
);

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('1', 'Thabo', 'Sales', '260', '5');

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('2', 'Naledi', 'Sales', '230', '9');

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('3', 'Amara', 'Operations', '410', '3');

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('4', 'Kabelo', 'Operations', '370', '2');

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('5', 'Lerato', 'Sales', '280', '4');

INSERT INTO performance_day7 (employee_id, employee_name, department, units_processed, errors_made)
VALUES ('6', 'Sipho', 'Operations', '390', '6');

SELECT * FROM performance_day7;


-- Compute efficiency score 

SELECT
	employee_name,
	units_processed / (errors_made + 1) AS efficiency_score
FROM performance_day7

-- Rank employees within each department using RANK() and DENSE_RANK()

SELECT
	employee_name,
	department,
	efficiency_score,
	DENSE_RANK() OVER (
		PARTITION BY department
		ORDER BY efficiency_score DESC
	) as dept_rank
FROM (
	-- Subquery to calculate efficiency_score first
	SELECT *,
	units_processed * 1.0 / (errors_made + 1) AS efficiency_score
	FROM performance_day7
) AS scored_data

/*

-Window functions use the OVER clause to define the group of rows the calculation should look at.
-PARTITION BY tells SQL to restart the ranking every time it hits a new department

-PARTITION BY creates a window for Sales and a seperate window for Operations
-Without this, everyone would be ranked 1 through 6. With this, you will see two "Rank 1s"
	(the best person in Sales and the best person in Operations).


*/
