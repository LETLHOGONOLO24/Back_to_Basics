/*

Tasks
-Compute average processing time per department
-Compute Min and Max
-Explain what SQL can and cannot do for inference

*/

CREATE TABLE performance_day10 (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	department VARCHAR(50),
	units_processed NUMERIC,
	errors_made INT,
	avg_processing_time DECIMAL(5, 4)
);

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('1', 'Thabo', 'Sales', '260', '5', '4.2');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('2', 'Naledi', 'Sales', '230', '9', '5.1');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('3', 'Lerato', 'Sales', '280', '4', '4.0');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('4', 'Amara', 'Operations', '410', '3', '3.8');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('5', 'Kabelo', 'Operations', '370', '2', '3.5');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('6', 'Sipho', 'Operations', '390', '6', '4.6');

INSERT INTO performance_day10 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('7', 'Zanele', 'Operations', '360', '4', '3.9');

-- Compute average processing time per department  

SELECT
	department,
	AVG(avg_processing_time) AS avg_time
FROM performance_day10
GROUP BY department;

-- Compute Min and Max

SELECT
	department,
	MIN(avg_processing_time) AS fastest_time,
	MAX(avg_processing_time) AS slowest_time,
	MAX(avg_processing_time) - MIN(avg_processing_time) AS time_gap
FROM performance_day10
GROUP BY department;

