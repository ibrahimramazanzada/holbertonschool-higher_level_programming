-- list genres of a specific show
SELECT tv_genres.name AS name WHERE tv_genres.id IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
);
ORDER BY name ASC;
