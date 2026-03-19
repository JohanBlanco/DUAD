import os

from flask import Flask, g, request, jsonify, current_app

from db import get_session, init_db
from auth_decorators import *
from repositories import ProductRepository, InvoiceRepository, UserRepository
from services.user_service import UserService
from routes.product_routes import products_bp
from routes.invoice_routes import invoices_bp
from routes.user_routes import users_bp
from jwt_manager import JWT_Manager


def create_app():
    app = Flask(__name__)
    init_db()
    app.jwt_manager = JWT_Manager(
        os.getenv("JWT_PRIVATE_KEY", "trespatitos"),
        algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
    )

    @app.before_request
    def inject_repos():
        session = get_session()
        g.session = session
        g.product_repository = ProductRepository(session)
        g.invoice_repository = InvoiceRepository(session)
        g.user_repository = UserRepository(session)
        g.user_service = UserService(g.user_repository)

    @app.teardown_appcontext
    def teardown_session(exception=None):
        session = g.pop("session", None)
        if session is not None:
            if exception is not None:
                session.rollback()
            else:
                session.commit()
            session.close()

    app.register_blueprint(products_bp)
    app.register_blueprint(invoices_bp)
    app.register_blueprint(users_bp)

    return app

app = create_app()

@app.route("/liveness")
@admin_only
def liveness():
    return "<p>Hello, World!</p>"

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400
    user = g.user_service.create(username=username, password=password, role=role)
    if not user:
        return jsonify({"error": "Username already exists"}), 409
    token = current_app.jwt_manager.encode({"id": user["id"]})
    if not token:
        return jsonify({"error": "Failed to generate token"}), 500
    return jsonify(token=token)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400
    user = g.user_repository.get_by_username_and_password(username, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 403
    token = current_app.jwt_manager.encode({"id": user.id})
    if not token:
        return jsonify({"error": "Failed to generate token"}), 500
    return jsonify(token=token)

@app.route('/me')
@user_and_admin_allowed
def me():
    """Returns the current authenticated user (requires valid token, role user or admin)."""
    return jsonify(g.current_user.to_dict())

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

    # TODO
    # 1. Connect the repos to routers  <- done
    # 2. Test Postman Collection <- done
    # 3. Implement Authorization <- in progress
    # 4. Create the decorators for admin_only and user_and_admin_allowed <- done
