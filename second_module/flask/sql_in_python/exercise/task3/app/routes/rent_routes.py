from flask import Blueprint, request, jsonify
from app.services.rent_service import RentService

def rent_routes(service:RentService):
    bp = Blueprint("rents", __name__)

    @bp.post("/rents")
    def create_rent():
        body = request.json
        response = service.create_rent(body)
        return jsonify(response), 201
    
    
    @bp.patch("/rents/<int:id>/status")
    def update_rent_status(id:int):
        body = request.json
        response = service.update_rent_status(body, id)
        return jsonify(response), 200
    
    @bp.get("/rents")
    def get_rents():
        filters = request.args.to_dict()
        response = service.get_rents(filters)
        return jsonify(response), 200

    return bp
