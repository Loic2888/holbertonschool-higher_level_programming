#!/usr/bin/python3
"""
Flask Authentication API - Basic Auth + JWT + Role-based Access Control
Complete authentication system with:
1. Basic HTTP Authentication (Flask-HTTPAuth)
2. JWT Token Authentication (Flask-JWT-Extended)
3. Role-based Access Control (admin/user)
Required packages:
pip install Flask Flask-HTTPAuth Flask-JWT-Extended Werkzeug
"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required,
    create_access_token, get_jwt_identity, \
    jwt_unauthorized_loader, jwt_invalid_token_loader,
    jwt_expired_token_loader, \
    jwt_revoked_token_loader, jwt_needs_fresh_token_loader
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-in-production'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

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


@auth.verify_password
def verify_password(username, password):
    """
    Basic HTTP Auth password verification callback.
    Args:
        username (str): Username from HTTP Basic Auth header
        password (str): Password from HTTP Basic Auth header
    Returns:
        str or None: Username if valid credentials, None otherwise
    """
    if username in users and
    check_password_hash(users[username]["password"], password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized(err):
    """
    JWT unauthorized error handler - missing token.
    Args:
        err: JWT error description
    Returns:
        tuple: JSON error response with 401 status
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    """
    JWT invalid token error handler.
    Args:
        err: JWT error description
    Returns:
        tuple: JSON error response with 401 status
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(err):
    """
    JWT expired token error handler.
    Args:
        err: JWT error description
    Returns:
        tuple: JSON error response with 401 status
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(err):
    """
    JWT revoked token error handler.
    Args:
        err: JWT error description
    Returns:
        tuple: JSON error response with 401 status
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh(err):
    """
    JWT fresh token required error handler.
    Args:
        err: JWT error description
    Returns:
        tuple: JSON error response with 401 status
    """
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Basic Auth protected endpoint.
    Requires:
        HTTP Basic Auth header with valid user1:password or admin1:password
    Returns:
        str: Success message
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    JWT Login endpoint - authenticate and return access token.
    Request Body (JSON):
        {
            "username": "user1",
            "password": "password"
        }
    Success Response (200):
        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }
    Error Responses:
        400: Invalid JSON
        401: Invalid credentials
    """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if username in users and
    check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": users[username]["role"]
        })
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT protected endpoint.
    Requires:
        Authorization: Bearer <valid_jwt_token>
    Returns:
        str: Success message
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only endpoint with role-based access control.
    Requires:
        Authorization: Bearer <valid_admin_jwt_token>
        User role must be 'admin' (admin1:password)
    Returns:
        str: Success message (admin only)
    Error Response (403):
        {"error": "Admin access required"}
    """
    current_user = get_jwt_identity()
    username = current_user["username"]

    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
