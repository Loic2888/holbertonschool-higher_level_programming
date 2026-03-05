-- Create the force_name table with an auto-incrementing id and a name column
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
