def register_teardowns(db_manager,app):

    @app.teardown_appcontext
    def close_db_connection():
        db_manager.close_connection()