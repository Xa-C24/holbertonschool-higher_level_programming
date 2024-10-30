#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script to list all states from a MySQL database.

    This script connects to a MySQL database and retrieves all entries in
    the 'states' table, sorted in ascending order by the 'id' field.
    It takes three arguments:
        1. MySQL username
        2. MySQL password
        3. Database name

    Usage:
        ./0-select_states.py <mysql_username> <mysql_password> <database_name>

    Requirements:
        - MySQLdb module must be installed.
        - The MySQL server must be running on localhost, using port 3306.
        - The database must contain a table named 'states' with at least
          'id' and 'name' columns.

    Example output:
        (1, 'California')
        (2, 'Arizona')
        ...
    """
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
