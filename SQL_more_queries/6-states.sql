-- Create a database named hbtn_0d_usa if it does not already exist, and use it.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Create a table named states with the following columns:
-- id: an integer that is the primary key and auto-increments with each new record
-- name: a variable character string with a maximum length of 256 characters that cannot be null
CREATE TABLE IF NOT EXISTS states (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL
);
