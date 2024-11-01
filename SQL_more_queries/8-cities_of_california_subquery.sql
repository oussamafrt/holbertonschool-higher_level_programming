-- Get the ID of the state 'California'
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- Select all cities that belong to California, ordered by cities.id
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
