from flask import Flask, g

from db import get_session, init_db
from repositories import ProductRepository, InvoiceRepository, UserRepository
from services.user_service import UserService
from routes.product_routes import products_bp
from routes.invoice_routes import invoices_bp
from routes.user_routes import users_bp


def create_app():
    app = Flask(__name__)
    init_db()

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

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

    # TODO
    # 1. Connect the repos to routers  <- done
    # 2. Test Postman Collection <- done
    # 3. Implement Authorization <- in progress
    # 4. Create the decorators for admin_only and user_only <- to do
