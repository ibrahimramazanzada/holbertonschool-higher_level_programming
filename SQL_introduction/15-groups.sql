-- find the number of students in each score group
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
