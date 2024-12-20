#!/usr/bin/env python3
"""
This script sets up a simple Flask web application to demonstrate API routing,
JSON data handling, and basic request-response cycles.

It provides endpoints for:

- Displaying a welcome message at the root URL (`/`).
- Returning a list of usernames at `/data`.
- Checking the API status at `/status`.
- Retrieving user information at `/users/<username>`.
- Adding a new user via a POST request to `/add_user`.

Modules used:

- Flask: A micro web framework for building web applications and APIs.
- jsonify: A utility function to convert Python data structures to JSON format.
- request: Handles incoming requests, providing access to headers and data.
- Response: Used to customize response objects,
  including headers and MIME types.
"""

from typing import Dict, Any
# Importation du module `Dict` et `Any` depuis `typing` pour définir des types génériques.
# `Dict` est utilisé pour indiquer que certaines variables seront des dictionnaires,
# et `Any` permet de représenter des valeurs de tout type.

from flask import Flask, jsonify, request, Response
# Importation des fonctions `Flask`, `jsonify`, `request`, et `Response` depuis le module `flask`.
# `Flask` est utilisé pour créer une application web.
# `jsonify` est utilisé pour convertir des objets Python en format JSON dans les réponses HTTP.
# `request` permet d'accéder aux données envoyées dans une requête HTTP (par exemple, les données JSON).
# `Response` permet de créer une réponse HTTP personnalisée, y compris avec des en-têtes spécifiques.

app = Flask(__name__)

# Dictionnaire en mémoire pour stocker les utilisateurs
users: Dict[str, Dict[str, Any]] = {}


@app.route('/')
def home():
    """
    Handles the root endpoint and returns a welcome message.

    Returns:
        Response: A plain text welcome message.
    """
    return Response("Welcome to the Flask API!", mimetype='text/plain')


@app.route('/data')
def get_users():
    """
    Returns a JSON response with a list of all usernames.

    Returns:
        Response: A JSON array of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns the API status.

    Returns:
        Response: A plain text message indicating the API status.
    """
    return Response("OK", mimetype='text/plain')


@app.route('/users/<username>')
def get_user(username):
    """
   Renvoie l'objet utilisateur complet correspondant au nom d'utilisateur fourni. 
   Args : nom d'utilisateur (str) : Le nom d'utilisateur à récupérer.
   Retourne : Réponse : Un objet JSON contenant les détails de l'utilisateur s'il a été trouvé,
    sinon un message d'erreur JSON avec un code d'état 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Gère les requêtes POST pour ajouter un nouvel utilisateur. 
    Attend des données JSON contenant 'username', 'name', 'age', et 'city'. 
    Retourne : Réponse : Un message de confirmation avec les données de l'utilisateur ajouté, ou un message d'erreur si 'username' 
    est manquant ou s'il existe un doublon avec les mêmes détails.
    """
    data = request.get_json()
    username = data.get(username)
    if not username:
        return jsonify({"error": "Username is required"}), 400
    # Update or add the user
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201  # Use 201 Created for successful POST requests


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles undefined endpoints and returns a custom error message.

    Args:
        e (Exception): The raised exception.

    Returns:
        Response: A JSON error message with a 404 status code.
    """
    return jsonify({"error": "Not found"}), 404


# Run the application
if __name__ == '__main__':
    app.run()