-- List score and name of all records with non-empty name in second_table
-- Database name will be passed as an argument of the mysql command
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND name != ''
ORDER BY score DESC;
