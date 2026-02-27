-- Inserts a new row into the table first_table.
INSERT INTO `first_table` (`id`, `name`) VALUES (89, "Holberton School");-- Inserts or updates a row in first_table
INSERT INTO first_table (id, name)
VALUES (89, 'Best School')
ON DUPLICATE KEY UPDATE name = 'Best School';