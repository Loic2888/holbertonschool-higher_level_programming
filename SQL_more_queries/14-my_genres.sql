-- Lists all genres of the show Dexter
-- Uses database hbtn_0d_tvshows
-- Results sorted by genre name ASC

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows 
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter" AND tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_genres.name ASC;
