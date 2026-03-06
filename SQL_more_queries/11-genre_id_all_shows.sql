-- Lists all shows in hbtn_0d_tvshows
-- Format: tv_shows.title - tv_show_genres.genre_id
-- Shows without genre => NULL
-- Sorted by tv_shows.title, then tv_show_genres.genre_id

SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
