-- Write a SQL query to find the name and score of the students who scored 10 or more in the second table.
-- The result should be ordered by score in descending order.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC; 
