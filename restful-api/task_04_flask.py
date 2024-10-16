#!/usr/bin/python3
"""import flask and jsonify module"""


""" Importation des modules nécessaires de Flask"""
"""Importation de OrderedDict pour garantir l'ordre des clés"""

"""Création d'une instance de l'application Flask"""

from flask import Flask, jsonify, request, Response
from collections import OrderedDict
app = Flask(__name__)

"""Dictionnaire contenant des utilisateurs"""
users = {
    "jane": {
        ("name", "Jane"),
        ("age", 28),
        ("city", "Los Angeles")
    },
    "john": {
        ("name", "John"),
        ("age", 30),
        ("city", "New York")
    }
}


"""Route principale"""


@app.route('/')
def home():
    return Response("Welcome to the Flask API!", mimetype='text/plain')


"""Route pour obtenir la liste des utilisateurs"""


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


"""Route pour vérifier l'état de l'API"""


@app.route('/status')
def status():
    return jsonify({"status": "OK"})


"""Route pour obtenir les informations d'un utilisateur"""


@app.route('/users/<username>')
def get_user(username):
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


"""Route pour ajouter un nouvel utilisateur"""


@app.route('/add_user', methods=['POST'])
def add_user():
    """Vérification des données JSON et des champs requis"""
    if not request.json or not 'username' in request.json:
        return jsonify({"error": "Username is required"}), 400

    """Amélioration de la gestion des champs requis en utilisant une boucle"""
    required_fields = ['username', 'name', 'age', 'city']
    for field in required_fields:
        if field not in request.json:
            return jsonify({"error": f"{field} is required"}), 400

    username = request.json.get('username')
    name = request.json.get('name')
    age = request.json.get('age')
    city = request.json.get('city')

    """Vérifie si l'utilisateur existe déjà"""
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    """Validation supplémentaire : s'assurer que l'âge est un entier positif"""
    if not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    """Validation supplémentaire : s'assurer que name et city sont des chaînes"""
    if not isinstance(name, str) or not isinstance(city, str):
        return jsonify({"error": "Name and city must be strings"}), 400

    """Ajoute le nouvel utilisateur au dictionnaire users"""
    users[username] = {
        ("name", name),
        ("age", age),
        ("city", city),
    }

    """Retourne un message de confirmation et les informations de l'utilisateur"""
    return jsonify({
        "message": "User added successfully",
        "user": {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
    }), 201


"""Lance l'application Flask en mode debug sur le port 5000"""
if __name__ == '__main__':
    app.run()
