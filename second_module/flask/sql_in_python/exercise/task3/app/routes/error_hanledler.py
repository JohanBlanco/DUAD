# @app.errorhandler(NotFoundError)
# def handle_not_found_error(error):
#     app.logger.error(error)
#     return jsonify({"error": str(error)}), 404

# @app.errorhandler(BadRequestError)
# def handle_bad_request_error(error):
#     app.logger.error(error)
#     return jsonify({"error": str(error)}), 400

# @app.errorhandler(Exception)
# def handle_general_exception(error):
#     app.logger.error(f"Unhandled Exception: {error}")
#     return jsonify({"error": "Internal server error"}), 500