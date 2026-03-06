-- Lists all the cities of California from hbtn_0d_usa
-- Sorted by cities.id ASC
-- No JOIN keyword used

SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
    SELECT `id`
    FROM `states`
    WHERE `name` = 'California'
)
ORDER BY `id`;
