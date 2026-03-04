-- List number of records with the same score in second_table
-- Database name will be passed as an argument of the mysql command
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
