-- Lists all cities contained in hbtn_0d_usa
-- Format: cities.id - cities.name - states.name
-- Sorted ASC by cities.id
-- Single SELECT statement with INNER JOIN

SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
ORDER BY `cities`.`id`;
