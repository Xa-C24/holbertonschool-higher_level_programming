-- Import the database dump from hbtn_0d_tvshows
-- Select the title of each TV show and the associated genre ID
-- From the tables tv_shows and tv_show_genres
-- Link the two tables by matching the TV show ID in both tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
