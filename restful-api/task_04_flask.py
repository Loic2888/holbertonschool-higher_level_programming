#!/usr/bin/python3
"""Task 4: Flask API"""


from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data")
def get_data():
    """Data endpoint"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Get user information"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = data
    return jsonify({"message": f"User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
