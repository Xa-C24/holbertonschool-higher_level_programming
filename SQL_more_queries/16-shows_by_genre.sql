-- script that lists all shows, and all genres linked to that show
SELECT tv_show.title, tv_genre.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show.id = tv_show_genres_show.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_show_genres.id
ORDER BY tv_shows_title ASC, tv_genres.name ASC;
