from flask import Blueprint, request, jsonify
from app.services.car_service import CarService

def car_routes(service:CarService):
    bp = Blueprint("cars", __name__)

    @bp.post("/cars")
    def create_car():
        body = request.json
        response = service.create_car(body)
        return jsonify(response), 201
    
    
    @bp.patch("/cars/<int:id>/status")
    def update_car_status(id:int):
        body = request.json
        response = service.update_car_status(body, id)
        return jsonify(response), 200
    
    @bp.get("/cars")
    def get_cars():
        filters = request.args.to_dict()
        response = service.get_cars(filters)
        return jsonify(response), 200

    return bp
