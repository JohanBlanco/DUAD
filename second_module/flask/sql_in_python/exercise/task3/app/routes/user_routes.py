from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

def user_routes(service:UserService):
    bp = Blueprint("users", __name__)

    @bp.post("/users")
    def create_user():
        body = request.json
        response = service.create_user(body)
        return jsonify(response), 201
    
    @bp.patch("/users/<int:id>")
    def update_user(id:int):
        body = request.json
        response = service.update_user(body, id)
        return jsonify(response), 200
    
    @bp.get("/users")
    def get_users():
        filters = request.args.to_dict()
        response = service.get_users(filters)
        return jsonify(response), 200

    return bp
