#!/usr/bin/python
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa, safe from injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments fournis en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Requête pour filtrer les états en fonction du nom
    query = ("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC")
    cursor.execute(query, (state_name,))
    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for state in rows:
        print(state)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
