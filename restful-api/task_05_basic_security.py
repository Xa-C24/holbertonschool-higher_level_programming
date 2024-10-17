#!/usr/bin/python3
"""Script démontrant l'authentification HTTP de base et JWT dans Flask"""

# Importation des bibliothèques nécessaires
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Création de l'application Flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

# Initialisation des gestionnaires JWT et Basic Auth
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Dictionnaire des utilisateurs avec des rôles et des mots de passe chiffrés
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Fonction de vérification des informations d'identification pour Basic Auth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user  # Retourne l'objet utilisateur
    return None


# Gestionnaire d'erreur pour l'authentification Basic Auth
@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized access"}), 401


# Route protégée par Basic Auth
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Route pour authentifier un utilisateur et générer un token JWT
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 401

    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    # Vérifie si l'utilisateur existe et si le mot de passe est correct
    if (
        username not in users or
        not check_password_hash(users[username]['password'], password)
    ):
        return jsonify({"error": "Bad username or password"}), 401

    # Crée un token JWT avec le nom d'utilisateur et le rôle de l'utilisateur
    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]}
    )
    return jsonify(access_token=access_token)


"""Gestionnaires d'erreurs JWT"""


@jwt.unauthorized_loader
def unauthorized_callback(error_string):
    """
    Gère les cas où un token JWT est manquant ou invalide.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    """
    Gère les tokens JWT invalides (signature incorrecte, etc.).
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """
    Gère les tokens JWT expirés.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    """
    Gère les tokens JWT révoqués.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    """
    Gère les cas où un token JWT frais est nécessaire.
    """
    return jsonify({"error": "Fresh token required"}), 401


# Route protégée par JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Route réservée aux administrateurs (protégée par JWT)
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
