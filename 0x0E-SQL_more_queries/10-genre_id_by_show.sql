--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title AS title, tv_shows_genres.genre_id AS genre_id
FROM tv_shows
JOIN tv_shows_genre ON tv_shows.id = tv_shows_genres.show_id
ORDER BY title, genre_id;
