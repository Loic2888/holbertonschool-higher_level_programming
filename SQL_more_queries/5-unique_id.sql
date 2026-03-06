-- Create a table named unique_id with the following columns:
-- id: an integer that defaults to 1 and must be unique
-- name: a variable character string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
