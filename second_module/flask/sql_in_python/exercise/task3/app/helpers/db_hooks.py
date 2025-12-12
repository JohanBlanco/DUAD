def register_db_hooks(db_manager,app):

    @app.before_request
    def open_db_connection():
        db_manager.create_connection()

    @app.teardown_appcontext
    def close_db_connection(exception=None):
        db_manager.close_connection()