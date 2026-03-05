-- 2-create_read_user.sql
-- Creates the database hbtn_0d_2 

CREATE DATABASE
IF NOT EXISTS `hbtn_0d_2`;

-- Create the user user_0d_2 with password user_0d_2_pwd

CREATE USER
IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd

GRANT SELECT
ON `hbtn_0d_2`.*
TO 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

FLUSH PRIVILEGES;
