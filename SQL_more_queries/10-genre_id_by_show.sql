-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked
-- Format: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title ASC, then tv_show_genres.genre_id ASC

SELECT s.title, g.genre_id
FROM tv_shows AS s
INNER JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
