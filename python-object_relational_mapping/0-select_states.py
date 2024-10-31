#!/usr/bin/python3
"""Script qui liste tous les états depuis la base de données spécifiée."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    # argv[1] : nom d'utilisateur MySQL
    # argv[2] : mot de passe MySQL
    # argv[3] : nom de la base de données
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    # Création d'un curseur pour exécuter les requêtes SQL
    cur = conn.cursor()

    # Exécution de la requête SQL pour récupérer tous les états,
    # triés par id croissant
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Récupération et affichage des résultats de la requête
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    conn.close()
