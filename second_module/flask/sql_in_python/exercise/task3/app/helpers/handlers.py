from flask import jsonify
from app.helpers.exceptions import *
from flask import jsonify, current_app

def register_error_handlers(app):

    @app.errorhandler(NotFoundError)
    def handle_not_found(error):
        return jsonify({"error": str(error)}), 404

    @app.errorhandler(BadRequestError)
    def handle_bad_request(error):
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(Exception)
    def handle_exception(error):
        return_value = jsonify({"error": "Internal server error"}), 500
        
        if current_app.debug:
            return jsonify({"error": str(error)}), 500
        
        # Production-safe message
        return return_value
