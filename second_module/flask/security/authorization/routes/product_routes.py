from datetime import datetime
from flask import Blueprint, g, jsonify, request

from auth_decorators import admin_only

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.route("", methods=["GET"])
@admin_only
def list_products():
    repo = g.product_repository
    products = repo.get_all()
    return jsonify([p.to_dict() for p in products])


@products_bp.route("/<int:product_id>", methods=["GET"])
@admin_only
def get_product(product_id):
    repo = g.product_repository
    product = repo.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict())


@products_bp.route("", methods=["POST"])
@admin_only
def create_product():
    repo = g.product_repository
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    name = data.get("name")
    price = data.get("price")
    entry_date_str = data.get("entry_date")
    quantity = data.get("quantity", 0)


    if repo.get_by_name(name):
        return jsonify({"error": "Product already exists"}), 400

    if name is None or price is None or entry_date_str is None:
        return jsonify({"error": "name, price and entry_date are required"}), 400
    try:
        entry_date = datetime.strptime(entry_date_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "entry_date must be YYYY-MM-DD"}), 400
    if quantity < 0:
        return jsonify({"error": "quantity must be >= 0"}), 400
    product = repo.create(name=name, price=float(price), entry_date=entry_date, quantity=int(quantity))
    return jsonify(product.to_dict()), 201


@products_bp.route("/<int:product_id>", methods=["PUT"])
@admin_only
def update_product(product_id):
    repo = g.product_repository
    product = repo.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    fields = {}
    if "name" in data:
        fields["name"] = data["name"]
    if "price" in data:
        fields["price"] = data["price"]
    if "entry_date" in data:
        try:
            fields["entry_date"] = datetime.strptime(data["entry_date"], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "entry_date must be YYYY-MM-DD"}), 400
    if "quantity" in data:
        q = data["quantity"]
        if not isinstance(q, int) or q < 0:
            return jsonify({"error": "quantity must be a non-negative integer"}), 400
        fields["quantity"] = q
    if not fields:
        return jsonify(product.to_dict())
    updated = repo.update(product_id, **fields)
    return jsonify(updated.to_dict())


@products_bp.route("/<int:product_id>", methods=["DELETE"])
@admin_only
def delete_product(product_id):
    repo = g.product_repository
    product = repo.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    repo.delete(product)
    return "", 204
