from functools import wraps
import os

from flask import request, jsonify, g

from jwt_manager import JWT_Manager


_JWT_SECRET = os.getenv("JWT_PRIVATE_KEY", "trespatitos")
_JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
_jwt_manager = JWT_Manager(_JWT_SECRET, algorithm=_JWT_ALGORITHM)

# TODO:
# - [ ] Check why the token is not allowed to access the endpoint
def _require_user_from_token():
    """
    Helper that:
    - Lee el header Authorization: Bearer <token>
    - Decodifica el token
    - Obtiene el user_id del payload
    - Verifica que el usuario exista en la BD
    Devuelve (user, None) si todo OK, o (None, (response, status_code)) si hay error.
    """
    auth_header = request.headers.get("Authorization", "")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None, (jsonify({"error": "Missing or invalid Authorization header"}), 401)

    token = auth_header.split(" ", 1)[1].strip()
    payload = _jwt_manager.decode(token)
    if not payload:
        return None, (jsonify({"error": "Invalid or expired token"}), 401)

    user_id = payload.get("user_id") or payload.get("id") or payload.get("sub")
    if user_id is None:
        return None, (jsonify({"error": "Token missing user identifier"}), 401)

    # Usamos el UserRepository ya inyectado en g por la app
    user_repo = getattr(g, "user_repository", None)
    if user_repo is None:
        return None, (jsonify({"error": "User repository not available"}), 500)

    user = user_repo.get_by_id(int(user_id))
    if not user:
        return None, (jsonify({"error": f"User {user_id} not found"}), 404)

    return user, None


def admin_only(fn):
    """
    Decorator que:
    - Valida el token JWT
    - Verifica que el usuario exista
    - Verifica que el rol del usuario sea 'admin'
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        user, error = _require_user_from_token()
        if error is not None:
            return error

        if getattr(user, "role", None) != "admin":
            return jsonify({"error": "Admin role required"}), 403

        g.current_user = user
        return fn(*args, **kwargs)

    return wrapper


def user_and_admin_allowed(fn):
    """
    Decorator que:
    - Valida el token JWT
    - Verifica que el usuario exista
    - Verifica que el rol del usuario sea 'user' o 'admin'
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        user, error = _require_user_from_token()
        if error is not None:
            return error

        role = getattr(user, "role", None)
        if role not in ("user", "admin"):
            return jsonify({"error": "User or admin role required"}), 403

        g.current_user = user
        return fn(*args, **kwargs)

    return wrapper

