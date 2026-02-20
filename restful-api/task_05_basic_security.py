#!/usr/bin/python3
"""
Flask Authentication API
"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    jwt_unauthorized_loader,
    jwt_invalid_token_loader,
    jwt_expired_token_loader,
    jwt_revoked_token_loader,
    jwt_needs_fresh_token_loader
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-in-production'

auth = HTTPBasicAuth()
jwt = JWTManager(app)
gph = generate_password_hash
cph = check_password_hash

users = {
    "user1": {
        "username": "user1",
        "password": gph("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": gph("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    if username in users and cph(users[username]["password"], password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh(err):
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if username in users and cph(users[username]["password"], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": users[username]["role"]
        })
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    username = current_user["username"]

    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
