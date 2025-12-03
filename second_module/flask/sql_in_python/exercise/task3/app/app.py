import os
from flask import Flask
from dotenv import load_dotenv

from app.db.pg_manager import PgManager
from app.routes.user_routes import user_routes
from app.services.user_service import UserService
from app.helpers.handlers import register_error_handlers
from app.helpers.teardown_appcontext import register_teardowns

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
    #  Services
    # ---------------------------
    user_service = UserService(db_manager)

    # ---------------------------
    #  Blueprints
    # ---------------------------
    user_blueprint = user_routes(user_service)

    # ---------------------------
    #  Register Blueprints
    # ---------------------------
    app.register_blueprint(user_blueprint, url_prefix="/users")

    # ---------------------------
    #  Error Handlers & Teardowns
    # ---------------------------
    register_error_handlers(app)
    register_teardowns(app=app, db_manager=db_manager)

    return app