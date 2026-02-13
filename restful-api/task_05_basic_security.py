#!/usr/bin/python3
"""
Task 5: API Security and Authentication Techniques
- Basic Auth with Flask-HTTPAuth
- JWT Auth with Flask-JWT-Extended
- Role-based access control (admin-only)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)

# Use a strong secret key in real apps (env var). For this task, static is fine.
app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory as required
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# -----------------------------
# Basic Auth configuration
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    """
    Verify username/password for Basic Auth.
    Return username (truthy) if valid, otherwise False/None.
    """
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error():
    """
    Ensure Basic Auth failures return 401 Unauthorized.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Auth.
    """
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT error handlers (IMPORTANT for tests)
# All JWT auth errors must return 401
# -----------------------------
@jwt.unauthorized_loader
def jwt_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def jwt_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def jwt_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def jwt_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def jwt_needs_fresh(err):
    return jsonify({"error": "Fresh token required"}), 401


# -----------------------------
# JWT routes
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accept JSON: {"username": "...", "password": "..."}
    Returns: {"access_token": "<JWT_TOKEN>"} if valid, else 401
    """
    data = request.get_json(silent=True)
    if data is None:
        # Invalid JSON is a request error (not auth)
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        # Invalid credentials = auth error
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed identity info (username + role) inside token
    identity = {"username": user["username"], "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only route using JWT + role check.
    403 if not admin.
    """
    identity = get_jwt_identity()  # {"username": "...", "role": "..."}
    role = identity.get("role") if isinstance(identity, dict) else None

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
