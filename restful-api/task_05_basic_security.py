#!/usr/bin/python3
"""Ce script montre comment utiliser l'authentification HTTP de base et JWT dans Flask"""

"""Importer les modules nécessaires à l'authentification et à la gestion des mots de passe"""

""" Initialiser l'application Flask"""
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
app = Flask(__name__)

"""Configurer la clé secrète pour JWT. Cette clé est utilisée pour signer les jetons."""
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

"""Initialiser l'authentification JWT et HTTP Basic"""
jwt = JWTManager(app)
auth = HTTPBasicAuth()

"""Dictionnaire pour simuler une base de données d'utilisateurs"""
users = {
    "user1": {
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("adminpassword1"),
        "role": "admin"
    }
}


""" Auth. de base : Vérifie le nom d'utilisateur et le mot de passe de la demande"""


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


"""Itinéraire protégé par l'authentification de base : Uniquement accessible avec un nom d'utilisateur et un mot de passe corrects"""


@app.route('/basic-auth-protected', methods=['GET'])
@auth.login_required
def basic_auth_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


"""Route de connexion pour authentifier les utilisateurs et renvoyer un jeton JWT"""


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    """Vérifier si le nom d'utilisateur existe et si le mot de passe est correct"""

    if username not in users or not check_password_hash(users[username], password):
        return jsonify({"msg": "Bad username or password"}), 401

    """Créer un jeton JWT contenant le nom d'utilisateur et le rôle de l'utilisateur"""
    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]})
    return jsonify(access_token=access_token)


"""Route protégée par JWT : accessible uniquement aux utilisateurs disposant d'un jeton JWT valide"""


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    """current_user = get_jwt_identity()"""

    """Check if the user has the role 'admin'"""
    if current_user["role"] != "admin":
        return jsonify({"msg": "Admin access required"}), 403

    return jsonify({"message": f"Admin Access Granted"})


"""Voie générale protégée par JWT : accessible à tout utilisateur authentifié"""


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    """Obtenir l'identité de l'utilisateur actuel à partir du jeton JWT"""
    return jsonify({"message": "JWT Auth: Access Granted"})


"""Fonction principale pour exécuter l'application Flask"""
if __name__ == "__main__":
    app.run(debug=True)
