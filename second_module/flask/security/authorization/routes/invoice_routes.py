from flask import Blueprint, g, jsonify, request

from auth_decorators import user_and_admin_allowed

invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")


@invoices_bp.route("/user/<int:user_id>", methods=["GET"])
@user_and_admin_allowed
def get_invoices_by_user(user_id):
    """Get all invoices for a single customer (user_id)."""
    repo = g.invoice_repository
    invoices = repo.get_by_user_id(user_id)
    return jsonify([inv.to_dict() for inv in invoices])


@invoices_bp.route("/purchase", methods=["POST"])
@user_and_admin_allowed
def purchase():
    """
    Make a sale: purchase products, generate an invoice, and persist it in the DB.
    Body: { "user_id": int, "items": [ {"product_id": int, "quantity": int}, ... ] }
    """
    invoice_repo = g.invoice_repository
    product_repo = g.product_repository
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    user_id = data.get("user_id")
    items = data.get("items")
    if user_id is None:
        return jsonify({"error": "user_id is required"}), 400
    user = g.user_repository.get_by_id(int(user_id))
    if not user:
        return jsonify({"error": f"User {user_id} not found"}), 404
    if not items or not isinstance(items, list):
        return jsonify({"error": "items must be a non-empty list"}), 400

    line_items = []
    for it in items:
        product_id = it.get("product_id")
        quantity = it.get("quantity")
        if product_id is None or quantity is None or quantity <= 0:
            return jsonify({"error": "Each item must have product_id and quantity (quantity > 0)"}), 400
        product = product_repo.get_by_id(product_id)
        if not product:
            return jsonify({"error": f"Product {product_id} not found"}), 404
        if product.quantity < quantity:
            return jsonify({
                "error": f"Insufficient stock for product '{product.name}' (available: {product.quantity})"
            }), 400
        line_items.append({
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": float(product.price),
        })

    for it in line_items:
        product = product_repo.get_by_id(it["product_id"])
        product.quantity -= it["quantity"]

    invoice = invoice_repo.create(user_id=int(user_id), items=line_items)
    return jsonify(invoice.to_dict()), 201
