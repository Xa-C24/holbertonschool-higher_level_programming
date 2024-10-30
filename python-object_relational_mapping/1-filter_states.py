#!/usr/bin/python3
"""Liste tous les états de la base de données dont le nom commence par N."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments fournis en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

# Connexion a la base de données MySQL
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
)

# Création d'un curseur pour excuter les requetes
cursor = db.cursor()

# Requete pour récupérer tous les états commençant par "N"
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ID ASC")

# Récupération et affichage des résultats
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fermeture du curseur et de la connexion
cursor.close()
db.close()
