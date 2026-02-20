"""
Flask RESTful User Management API - task_04_flask.py

Complete Flask API implementing CRUD operations for user management with in-memory storage.
Follows REST conventions with proper HTTP status codes, JSON responses, and input validation.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Welcome endpoint - Returns API greeting message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns list of all usernames as JSON array."""
    username_list = list(users.keys())
    return jsonify(username_list)


@app.route("/status")
def get_status():
    """Health check endpoint - Returns OK status."""
    return "OK"


@app.route("/user/<username>")
def get_user(username):
    """
    Retrieve specific user by username.
    
    Args:
        username (str): Username to lookup
        
    Returns:
        JSON user object (200) or error (404)
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Create new user from JSON request body.
    
    Request body example:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    Error responses:
    - 400: Invalid JSON or missing username
    - 409: Username already exists
    """
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)

