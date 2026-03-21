from sqlalchemy import select
from sqlalchemy.orm import Session
from models.invoice_model import Invoice, InvoiceItem


class InvoiceRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        stmt = select(Invoice)
        return self.session.scalars(stmt).all()

    def get_by_id(self, id: int):
        return self.session.get(Invoice, id)

    def get_by_user_id(self, user_id: int):
        stmt = select(Invoice).where(Invoice.user_id == user_id)
        return self.session.scalars(stmt).all()

    def create(self, user_id: int, items: list[dict]) -> Invoice:
        """
        Create an invoice and its line items (for a sell).
        items: list of {"product_id": int, "quantity": int, "unit_price": float}.
        """
        invoice = Invoice(user_id=user_id)
        self.session.add(invoice)
        self.session.flush()  # get invoice.id for items

        for it in items:
            item = InvoiceItem(
                invoice_id=invoice.id,
                product_id=it["product_id"],
                quantity=it["quantity"],
                unit_price=it["unit_price"],
            )
            self.session.add(item)

        return invoice

    def delete(self, invoice: Invoice):
        self.session.delete(invoice)
