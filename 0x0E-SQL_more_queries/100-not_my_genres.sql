-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN
(
SELECT tv_genres.id, name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.id
) AS d ON d.id = tv_genres.id
WHERE d.id is NULL
ORDER BY name;
