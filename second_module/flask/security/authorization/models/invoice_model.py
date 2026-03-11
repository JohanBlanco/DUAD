from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Numeric
from datetime import datetime

if TYPE_CHECKING:
    from models.user_model import User
    from models.product_model import Product


class Invoice(Base):
    __tablename__ = "invoices"
    __table_args__ = {"schema": "authorization"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("authorization.users.id"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="invoices")
    items: Mapped[list["InvoiceItem"]] = relationship(
        "InvoiceItem", back_populates="invoice", cascade="all, delete-orphan"
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "items": [item.to_dict() for item in self.items],
        }


class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    __table_args__ = {"schema": "authorization"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("authorization.invoices.id"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("authorization.products.id"), nullable=False
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="invoice_items")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "invoice_id": self.invoice_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "unit_price": float(self.unit_price),
        }
