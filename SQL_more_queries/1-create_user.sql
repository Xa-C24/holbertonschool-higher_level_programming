-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1' @localhost IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges sur le serveur MySQL à l'utilisateur
GRANT ALL PRIVILEGES on *.* TO  'user_0d_1'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;