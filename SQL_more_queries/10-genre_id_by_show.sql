--  lists all shows
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows NATURAL 
JOIN tv_show_genres NATURAL 
JOIN tv_genres 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
