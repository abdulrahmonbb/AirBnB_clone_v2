-- This script prepares a MySQL Server for the project

-- Create a new database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privilege on performance schema  to the user
GRANT SELECT ON performace_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to ensure all changes take effect
FLUSH PRIVILEGES;
