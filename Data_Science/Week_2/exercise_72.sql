/*

Tasks
-Group data by training hours buckets:
	Low (<= 10)
	Medium (11 - 18)
	High (> 18)

-Compute avg error rate per bucket
-Interpret trend

*/

CREATE TABLE performance_day11 (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	department VARCHAR(50),
	units_processed NUMERIC,
	errors_made INT,
	avg_processing_time DECIMAL(5, 4),
	training_hours INT
);

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('1', 'Thabo', 'Sales', '260', '5', '4.2', '12');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('2', 'Naledi', 'Sales', '230', '9', '5.1', '8');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('3', 'Lerato', 'Sales', '280', '4', '4.0', '15');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('4', 'Amara', 'Operations', '410', '3', '3.8', '20');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('5', 'Kabelo', 'Operations', '370', '2', '3.5', '22');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('6', 'Sipho', 'Operations', '390', '6', '4.6', '14');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('7', 'Zanele', 'Operations', '360', '4', '3.9', '18');

INSERT INTO performance_day11 (employee_id, employee_name, department, units_processed, errors_made, avg_processing_time, training_hours)
VALUES ('8', 'Mpho', 'Sales', '250', '6', '4.4', '10');

-- Group data by training_hours buckets  

SELECT 
	CASE
		WHEN training_hours <= 10 THEN 'Low'
		WHEN training_hours BETWEEN 11 AND 18 THEN 'Medium'
		ELSE 'High'
	END AS training_bucket,
	COUNT(*) AS employee_count,
	AVG(errors_made / units_processed) AS avg_error_rate,
	AVG(avg_processing_time) AS avg_speed
FROM performance_day11
GROUP BY training_bucket
ORDER BY avg_error_rate DESC;

-- Computing avg error rate per bucket

SELECT 
    CASE 
        WHEN training_hours <= 10 THEN 'Low'
        WHEN training_hours BETWEEN 11 AND 18 THEN 'Medium'
        ELSE 'High' 
    END AS training_bucket,
    -- We calculate error_rate for each row, then take the average
    AVG(errors_made * 1.0 / units_processed) AS avg_error_rate
FROM performance_day11
GROUP BY 1 -- Shorthand for "Group by the first column"
ORDER BY avg_error_rate DESC;

/*
Interpreting trend

🔍 3 Key Insights from the Trend

1. The "Double-Dividend" of TrainingThe most significant trend is that training improves two metrics at once. Usually,
in business, there is a trade-off: if you go faster, you make more mistakes. Here, the "High" training group is both
the fastest and the most accurate. This suggests that training isn't just teaching people to be careful; it’s building
"fluency" or "muscle memory."

2. Diminishing Returns? Not Yet.Often, trends flatten out (e.g., the jump from 50 to 60 hours might not matter). However,
in this data, the jump from "Medium" to "High" training still resulted in a massive 60% reduction in errors (1.63% to 0.64%).
This indicates the company has not yet reached the "ceiling" of how much training can help.

3. Identifying the "Danger Zone"
The trend shows a "performance cliff" at the Low level. Employees with 10 or fewer hours (Naledi and Mpho) are significant
outliers in terms of errors. The trend suggests that 10 hours is likely insufficient for the complexity of the tasks being
performed.


