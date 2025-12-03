import os
from flask import Flask
from dotenv import load_dotenv
from app.db.pg_manager import PgManager

from app.routes.user_routes import user_routes
from app.services.user_service import UserService


# Load .env del directorio raíz del proyecto
load_dotenv()

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
#  Close DB conecction on each request
# ---------------------------
@app.teardown_appcontext
def close_db_connection(exception=None):
    db_manager.close_connection()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)