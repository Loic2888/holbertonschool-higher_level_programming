-- Create a new table named `second_table` with the following columns:
-- - `id` (integer)
-- - `name` (string, not null)
-- - `score` (integer, not null)
-- Insert the following records into `second_table`:
-- | id | name   | score |
-- |----|--------|-------|
-- | 1  | John   | 10    |
-- | 2  | Alex   | 3     |
-- | 3  | Bob    | 14    |
-- | 4  | George | 8     |

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
