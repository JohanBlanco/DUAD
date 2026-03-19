from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.invoice_model import Invoice


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "authorization"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False, default="user")  # 'admin' | 'user'

    invoices: Mapped[list["Invoice"]] = relationship("Invoice", back_populates="user")

    def to_dict(self) -> dict:
        # Never expose password
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "password": self.password
        }
