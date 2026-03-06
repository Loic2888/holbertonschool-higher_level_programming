-- Create a database named hbtn_0d_usa if it does not already exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the hbtn_0d_usa database.
 USE `hbtn_0d_usa`;
-- Create a table named cities with the following columns:
-- id: an integer that is the primary key and auto-increments with each new record
-- state_id: an integer that cannot be null and is a foreign key referencing the id column of the states table
-- name: a variable character string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS `cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `state_id` INT NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
