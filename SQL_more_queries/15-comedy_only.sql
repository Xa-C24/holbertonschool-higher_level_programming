-- Script qui liste tous les shows de genre Comedy dans la base de données
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = (
    SELECT id FROM tv_genres WHERE name = 'Comedy'
)
ORDER BY tv_shows.title ASC
