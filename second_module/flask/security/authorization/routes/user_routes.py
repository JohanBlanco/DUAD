from flask import Blueprint, g, jsonify, request

from auth_decorators import admin_only

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@admin_only
def list_users():
    """Get all users."""
    users = g.user_service.get_all()
    return jsonify(users)


@users_bp.route("/<int:user_id>", methods=["GET"])
@admin_only
def get_user_by_id(user_id):
    """Get user by ID."""
    user = g.user_service.get_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@users_bp.route("/by-username/<username>", methods=["GET"])
@admin_only
def get_user_by_username(username):
    """Get user by username."""
    user = g.user_service.get_by_username(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@users_bp.route("", methods=["POST"])
@admin_only
def create_user():
    """
    Create a new user.
    Body: { "username": str, "password": str, "role": str (optional, default "user") }
    """
    service = g.user_service
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400
    user = service.create(username=username, password=password, role=role)
    if not user:
        return jsonify({"error": "Username already exists"}), 409
    return jsonify(user), 201
