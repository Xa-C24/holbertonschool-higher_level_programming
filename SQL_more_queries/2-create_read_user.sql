-- script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder tous les privilèges sur le serveur MySQL à l'utilisateur
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;
