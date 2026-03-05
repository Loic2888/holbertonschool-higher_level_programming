-- Create a table named `id_not_null` with an `id` column that has a default value of 1 and cannot be NULL,
-- and a `name` column that can hold variable character strings up to 256 characters long.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 NOT NULL,
    name VARCHAR(256)
);
