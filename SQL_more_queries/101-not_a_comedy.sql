--  lists all genre of show Dexter
SELECT DISTINCT tv_shows.title
FROM tv_genres
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title NOT IN (SELECT DISTINCT tv_shows.title
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title ASC;
