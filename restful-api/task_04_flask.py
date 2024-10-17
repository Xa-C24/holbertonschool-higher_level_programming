#!/usr/bin/python3
"""
Ce fichier contient une API simple utilisant Flask pour gérer des utilisateurs.
Les utilisateurs sont stockés en mémoire sous forme de dictionnaire.

Il fournit des points d'extrémité pour :
- Afficher un message de bienvenue à l'URL racine (`/`).
- Retourner une liste de noms d'utilisateurs à `/data`.
- Vérifier le statut de l'API à `/status`.
- Récupérer les informations de l'utilisateur à `/users/<username>`.
- Ajouter un nouvel utilisateur via une requête POST à `/add_user`.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

"""Dictionnaire vide par défaut"""
users = {}


@app.route('/')
def home():
    """
    Route principale de l'API. Retourne un message de bienvenue.
    """
    return "Welcome to the Flask API!", 200


@app.route('/data')
def get_users():
    """
    Retourne la liste des utilisateurs.
    """
    return jsonify(list(users.keys())), 200


@app.route('/status')
def status():
    """
    Vérifie l'état de l'API.
    """
    return "OK", 200


"""Retourne une chaîne de caractères OK"""


@app.route('/users/<username>')
def get_user(username):
    """
    Récupère les informations d'un utilisateur en fonction de son nom d'utilisateur.
    """
    user_data = users.get(username)
    if user_data:
        return jsonify({
            "username": username,
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Ajoute un nouvel utilisateur à la liste.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid request format: JSON required"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    """Vérification des champs requis avec messages spécifiques"""
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    if 'age' not in data:
        return jsonify({"error": "Age is required"}), 400
    if 'city' not in data:
        return jsonify({"error": "City is required"}), 400

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    try:
        age = int(age)
        if age <= 0:
            return jsonify({"error": "Age must be a positive integer"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a positive integer"}), 400

    """Vérification des types"""
    if not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400
    if not isinstance(name, str) or not isinstance(city, str):
        return jsonify({"error": "Name and city must be strings"}), 400

    """Ajout de l'utilisateur"""
    users[username] = {"name": name, "age": age, "city": city}

    """Message de succès correspondant à l'énoncé"""
    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
