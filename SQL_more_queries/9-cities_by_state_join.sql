-- Select city id, city name, and state name in a single query
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;