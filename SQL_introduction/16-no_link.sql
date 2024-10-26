-- script that lists all records of the table 
SELECT name, score
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
