-- list all cities of California
SELECT cities.name ORDER BY cities.id ASC
FROM cities WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
);
