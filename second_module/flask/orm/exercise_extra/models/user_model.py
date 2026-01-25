from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import *

if TYPE_CHECKING:
    from models.car_model import Car
    from models.address_model import Address

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'sqlalchemy'}
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    
    cars: Mapped[list["Car"]] = relationship("Car", back_populates="user")
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user")