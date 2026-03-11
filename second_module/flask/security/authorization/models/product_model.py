from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Date, Numeric

if TYPE_CHECKING:
    from models.invoice_model import InvoiceItem


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "authorization"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    entry_date: Mapped[date] = mapped_column(Date, nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False, default=0)

    invoice_items: Mapped[list["InvoiceItem"]] = relationship(
        "InvoiceItem", back_populates="product"
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": float(self.price),
            "entry_date": self.entry_date.isoformat() if self.entry_date else None,
            "quantity": self.quantity,
        }
