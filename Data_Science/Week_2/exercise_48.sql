/*

Tasks
-Calculate normalized features using
	MIN() OVER()
	MAX() OVER()
-Compute composite score in SQL
-Rank employees by score

*/

CREATE TABLE performance_day8 (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	department VARCHAR(50),
	units_processed NUMERIC,
	errors_made INT,
	avg_processing_time DECIMAL(5, 4)
);

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('1', 'Thabo', 'Sales', '260', '5', '4.2');

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('2', 'Naledi', 'Sales', '230', '9', '5.1');

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('3', 'Amara', 'Operations', '410', '3', '3.8');

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('4', 'Kabelo', 'Operations', '370', '2', '3.5');

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('5', 'Lerato', 'Sales', '280', '4', '4.0');

INSERT INTO performance_day8 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time)
VALUES ('6', 'Sipho', 'Operations', '390', '6', '4.6');

SELECT * FROM performance_day8

-- Calculate normalized features  

SELECT
	employee_name,
	-- Normalized Units: (units - min) / (max - min)
	(units_processed - MIN(units_processed) OVER()) * 1.0 /
	NULLIF(MAX(units_processed) OVER() - MIN(units_processed) OVER(), 0) AS units_norm,

	-- Normalized Speed: (speed - min) / (max - min)
	(speed_score - MIN(speed_score) OVER()) * 1.0 / 
    NULLIF(MAX(speed_score) OVER() - MIN(speed_score) OVER(), 0) AS speed_norm,

	-- Normalized Error Rate: (rate - min) / (max - min)
	(error_rate - MIN(error_rate) OVER()) * 1.0 / 
    NULLIF(MAX(error_rate) OVER() - MIN(error_rate) OVER(), 0) AS error_norm
FROM (
	-- Subquery to prepare the raw features first
	SELECT
		employee_name,
		units_processed,
		(1.0 / avg_processing_time) AS speed_score,
		(errors_made * 1.0 / units_processed) AS error_rate
	FROM performance_day8
) AS raw_features

-- Compute composite score in SQL and rank employees by score.

WITH NormalizedData AS (
    SELECT 
        employee_name,
        department, -- <== Added here so it passes the first gate
        (units_processed - MIN(units_processed) OVER()) * 1.0 / 
        NULLIF(MAX(units_processed) OVER() - MIN(units_processed) OVER(), 0) AS u_norm,
        
        ((1.0/avg_processing_time) - MIN(1.0/avg_processing_time) OVER()) * 1.0 / 
        NULLIF(MAX(1.0/avg_processing_time) OVER() - MIN(1.0/avg_processing_time) OVER(), 0) AS s_norm,
        
        ((errors_made*1.0/units_processed) - MIN(errors_made*1.0/units_processed) OVER()) * 1.0 / 
        NULLIF(MAX(errors_made*1.0/units_processed) OVER() - MIN(errors_made*1.0/units_processed) OVER(), 0) AS e_norm
    FROM performance_day8
),
ScoredData AS (
    SELECT 
        employee_name,
        department, -- <== Added here so it passes the second gate
        (0.5 * u_norm) + (0.3 * s_norm) + (0.2 * (1 - e_norm)) AS composite_score
    FROM NormalizedData
)
SELECT 
    employee_name,
    department,
    ROUND(composite_score, 4) as score,
    RANK() OVER(ORDER BY composite_score DESC) as performance_rank
FROM ScoredData
ORDER BY performance_rank;

/*

Normally, MIN() looks for the smallest value in a group and gives you one row. By adding OVER(),
you tell SQL: "Find the minimum of the whole table, but keep all my rows visible." * Every single
row now "knows" that the table minimum is 230 and the maximum is 410.

SQL (especially PostgreSQL or SQL Server) often does "Integer Division." If you divide $30 / 180$,
SQL might give you 0. Multiplying by 1.0 forces SQL to treat the numbers as decimals (Floats),
so you get 0.1666.

If the Max and Min are the same (e.g., everyone processed exactly 100 units), the denominator becomes
0. In math, dividing by zero breaks the universe. NULLIF prevents your query from crashing by turning
a zero-denominator into a NULL.

The reason why we divide 1.0 by avg_processing_time is because if we used raw numbers, the ones with
large numbers would get a higher score and we want it to be the other way around. By dividing 1.0 by
avg_processing_time, the ones with a smaller number would get a higher score and that is what we want

*/