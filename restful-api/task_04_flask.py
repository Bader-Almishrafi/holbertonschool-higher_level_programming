#!/usr/bin/python3
"""
Task 4: Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: Do not include testing data when pushing your code
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """
    Return a list of all usernames stored in the API.
    Example output: ["jane", "john"]
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return the full user object for the provided username.
    If not found, return 404 with {"error": "User not found"}
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user from JSON body.
    Expected JSON:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    Errors:
    - Invalid JSON -> 400 {"error": "Invalid JSON"}
    - Missing username -> 400 {"error": "Username is required"}
    - Duplicate username -> 409 {"error": "Username already exists"}
    """
    data_json = request.get_json(silent=True)

    if data_json is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data_json.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # store the whole object using username as key
    users[username] = data_json

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
