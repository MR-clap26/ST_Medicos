CREATE DATABASE s_turnos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'yop@'@'localhost' IDENTIFIED BY 'no_tengo';
GRANT ALL PRIVILEGES ON s_turnos.* TO 'yop@'@'localhost';
FLUSH PRIVILEGES;