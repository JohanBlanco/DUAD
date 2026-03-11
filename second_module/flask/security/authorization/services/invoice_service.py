from repositories.invoice_repository import InvoiceRepository
from repositories.product_repository import ProductRepository


class InvoiceService:
    def __init__(
        self,
        invoice_repository: InvoiceRepository,
        product_repository: ProductRepository,
    ):
        self.invoice_repository = invoice_repository
        self.product_repository = product_repository

    def get_invoices_by_user(self, user_id: int) -> list[dict]:
        invoices = self.invoice_repository.get_by_user_id(user_id)
        return [inv.to_dict() for inv in invoices]

    def get_invoice_by_id(self, invoice_id: int) -> dict | None:
        invoice = self.invoice_repository.get_by_id(invoice_id)
        return invoice.to_dict() if invoice else None

    def purchase(self, user_id: int, items: list[dict]) -> tuple[dict | None, str | None]:
        """
        items: list of {"product_id": int, "quantity": int}.
        Returns (invoice_dict, None) on success or (None, error_message) on failure.
        """
        if not items:
            return None, "No items to purchase"

        line_items = []
        for it in items:
            product_id = it.get("product_id")
            quantity = it.get("quantity")
            if product_id is None or quantity is None or quantity <= 0:
                return None, "Invalid item: product_id and quantity required (quantity > 0)"
            product = self.product_repository.get_by_id(product_id)
            if not product:
                return None, f"Product {product_id} not found"
            if product.quantity < quantity:
                return None, f"Insufficient stock for product '{product.name}' (available: {product.quantity})"
            line_items.append({
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": float(product.price),
            })

        for it in line_items:
            product = self.product_repository.get_by_id(it["product_id"])
            product.quantity -= it["quantity"]

        invoice = self.invoice_repository.create(user_id=user_id, items=line_items)
        return invoice.to_dict(), None
