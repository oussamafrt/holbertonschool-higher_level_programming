-- Select genres and the count of shows linked to each genre
SELECT 
    genres.name AS genre, 
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM 
    genres
LEFT JOIN 
    tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY 
    genres.id
HAVING 
    COUNT(tv_show_genres.show_id) > 0
ORDER BY 
    number_of_shows DESC;
