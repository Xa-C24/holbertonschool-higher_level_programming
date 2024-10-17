#!/usr/bin/python3
"""
Ce fichier contient une API simple utilisant Flask pour gérer des utilisateurs.
Les utilisateurs sont stockés en mémoire sous forme de dictionnaire.

Il fournit des points d'extrémité pour : 
- Afficher un message de bienvenue à l'URL racine (`/`). 
- Retourner une liste de noms d'utilisateurs à `/data`. 
- Vérifier le statut de l'API à `/status`. 
- Récupérer les informations de l'utilisateur à `/users/<username>`. 
- Ajout d'un nouvel utilisateur via une requête POST à `/add_user`. Modules utilisés : 
- Flask : Un micro framework web pour construire des applications web et des API. 
- jsonify : Une fonction utilitaire pour convertir les structures de données Python au format JSON. 
- request : gère les requêtes entrantes et donne accès aux en-têtes et aux données. 
- Response (réponse) : Utilisé pour personnaliser les objets de réponse, y compris les en-têtes et les types MIME.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


"""Dictionnaire vide par défaut"""
users = {}


@app.route('/')
def home():
    """
    Route principale de l'API. Retourne un message de bienvenue.
    
    Méthode HTTP : GET
    
    Retour :
        - message : JSON contenant un message de bienvenue.
    """
    return "Welcome to the Flask API!", 200


@app.route('/data')
def get_users():
    """
    Retourne la liste des utilisateurs.

    Méthode HTTP : GET

    Retour :
        - Liste des clés (noms d'utilisateurs) du dictionnaire `users`.
    """
    return jsonify(list(users.keys())), 200


@app.route('/status')
def status():
    """
    Vérifie l'état de l'API.

    Méthode HTTP : GET

    Retour :
        - status : JSON avec le statut "OK".
    """
    return jsonify({"status": "OK"})


@app.route('/users/<username>')
def get_user(username):
    """
    Récupère les informations d'un utilisateur en fonction de son nom d'utilisateur.

    Méthode HTTP : GET

    Paramètre :
        - username : Le nom d'utilisateur dans l'URL.

    Retour :
        - JSON contenant les informations de l'utilisateur si trouvé.
        - Erreur 404 si l'utilisateur n'est pas trouvé.
    """
    user_data = users.get(username)
    if user_data:
        return jsonify({
            "username": username,
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        })
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Ajoute un nouvel utilisateur à la liste.

    Méthode HTTP : POST

    Corps de la requête (JSON) :
        - username : nom d'utilisateur (obligatoire)
        - name : nom complet (obligatoire)
        - age : âge (obligatoire, doit être un entier positif)
        - city : ville de résidence (obligatoire)

    Retour :
        - JSON confirmant l'ajout de l'utilisateur avec ses informations si réussi.
        - Erreur 400 si les champs requis ne sont pas présents ou mal formatés.
    """
    required_fields = ['username', 'name', 'age', 'city']
    for field in required_fields:
        if field not in request.json:
            return jsonify({"error": f"{field} is required"}), 400

    username = request.json.get('username')
    name = request.json.get('name')
    age = request.json.get('age')
    city = request.json.get('city')

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    if not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400
    if not isinstance(name, str) or not isinstance(city, str):
        return jsonify({"error": "Name and city must be strings"}), 400

    users[username] = {"name": name, "age": age, "city": city}

    return jsonify({
        "message": "User added successfully",
        "user": {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
