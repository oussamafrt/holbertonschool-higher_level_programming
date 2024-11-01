-- Select genres and the count of shows linked to each genre
SELECT 
    tg.name AS genre, 
    COUNT(tsg.show_id) AS number_of_shows
FROM 
    tv_genres AS tg
JOIN 
    tv_show_genres AS tsg ON tg.id = tsg.genre_id
GROUP BY 
    tg.name
HAVING 
    COUNT(tsg.show_id) > 0
ORDER BY 
    number_of_shows DESC;