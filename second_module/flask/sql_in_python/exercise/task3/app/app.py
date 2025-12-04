import os
from flask import Flask
from dotenv import load_dotenv

from app.db.pg_manager import PgManager
from app.routes.user_routes import user_routes
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.helpers.handlers import register_error_handlers
from app.helpers.db_hooks import register_db_hooks

load_dotenv()

def create_app():
    app = Flask(__name__)

    # ---------------------------
    #  Db Manager
    # ---------------------------
    db_manager = PgManager(
        db_name=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    # ---------------------------
    #  Repositories
    # ---------------------------
    user_repository = UserRepository(db_manager)

    # ---------------------------
    #  Services
    # ---------------------------
    user_service = UserService(user_repository)

    # ---------------------------
    #  Blueprints / Routes
    # ---------------------------
    user_blueprint = user_routes(user_service)

    # ---------------------------
    #  Register Blueprints/Routes
    # ---------------------------
    app.register_blueprint(user_blueprint)

    # ---------------------------
    #  Error Handlers & Teardowns
    # ---------------------------
    register_error_handlers(app)
    register_db_hooks(app=app, db_manager=db_manager)

    return app