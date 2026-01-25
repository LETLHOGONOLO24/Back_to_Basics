/*

Tasks
-Calculate Avg processing time per department
-Compute difference between departments
-Interpret results descriptively

*/

-- Calculate Avg processing time per department  

SELECT
	department,
	ROUND(AVG(avg_processing_time), 2) AS dept_avg_time
FROM performance_day8
GROUP BY department;

-- Compute differences between departments and interpret results descriptively.

WITH DeptAverages AS (
	-- First, we get the average for each department
	SELECT
		department,
		AVG(avg_processing_time) AS avg_time
	FROM performance_day8
	GROUP BY department
)
SELECT
	-- We select the averages and subtract them
	(SELECT avg_time FROM DeptAverages WHERE department = 'Sales') AS sales_avg,
	(SELECT avg_time FROM DeptAverages WHERE department = 'Operations') AS ops_avg,
	(SELECT avg_time FROM DeptAverages WHERE department = 'Sales') - 
	(SELECT avg_time FROM DeptAverages WHERE department = 'Operations') AS time_difference;

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