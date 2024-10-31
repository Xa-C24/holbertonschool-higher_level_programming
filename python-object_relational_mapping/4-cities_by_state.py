#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments fournis en ligne de commande
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

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Requête pour filtrer les états en fonction du nom
    query ="""
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
