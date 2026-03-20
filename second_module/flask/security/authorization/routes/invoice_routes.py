from flask import Blueprint, g, jsonify, request

from auth_decorators import user_and_admin_allowed

invoices_bp = Blueprint("invoices", __name__, url_prefix="/invoices")


@invoices_bp.route("/user/<int:user_id>", methods=["GET"])
@user_and_admin_allowed
def get_invoices_by_user(user_id):
    """Get all invoices for a single customer (user_id)."""
    if g.current_user.role != "admin" and user_id != g.current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
    invoices = g.invoice_service.get_invoices_by_user(user_id)
    return jsonify(invoices)


@invoices_bp.route("/purchase", methods=["POST"])
@user_and_admin_allowed
def purchase():
    """
    Make a sale: purchase products, generate an invoice, and persist it in the DB.
    Body: { "items": [ {"product_id": int, "quantity": int}, ... ] }
    The buyer is the authenticated user (g.current_user).
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    items = data.get("items")
    if not items or not isinstance(items, list):
        return jsonify({"error": "items must be a non-empty list"}), 400

    user_id = g.current_user.id
    invoice, err = g.invoice_service.purchase(user_id, items)
    if err:
        status = 404 if "not found" in err.lower() else 400
        return jsonify({"error": err}), status
    return jsonify(invoice), 201
