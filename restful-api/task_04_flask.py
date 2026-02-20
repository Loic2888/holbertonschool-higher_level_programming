from flask import Flask, jsonify, request
"""
Flask RESTful User Management API

A simple REST API built with Flask for managing users stored in an in-memory dictionary.
Supports CRUD operations with proper HTTP status codes and JSON responses.

Endpoints:
---------
GET    /                 - Welcome message
GET    /data             - List all usernames (array of strings)
GET    /status           - Health check ("OK")
GET    /user/<username>  - Get user details by username (404 if not found)
POST   /add_user         - Create new user (400 invalid JSON/missing username, 409 if exists)

Request format for POST /add_user:
{
    "username": "john",
    "name": "John",
    "age": 30,
    "city": "New York"
}

User data structure:
{
    "name": str,
    "age": int/float,
    "city": str
}

Status Codes:
-------------
201 - Created
200 - OK  
400 - Bad Request
404 - Not Found
409 - Conflict

Example usage:
    curl http://localhost:5000/data
    curl -X POST http://localhost:5000/add_user \\
        -H "Content-Type: application/json" \\
        -d '{"username":"john","name":"John","age":30,"city":"NYC"}'

Note: Data is stored in memory only. Restarting the server clears all users.
For production, replace with persistent storage (database).
"""


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    username_list = list(users.keys())
    return jsonify(username_list)


@app.route("/status")
def get_status():
    return "OK"


@app.route("/user/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
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
