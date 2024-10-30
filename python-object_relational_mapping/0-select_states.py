#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments passés en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Création d'un curseur pour exécuter la requête
    cursor = db.cursor()

    # Requête pour sélectionner tous les états triés par id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Récupérer et afficher les résultats
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
