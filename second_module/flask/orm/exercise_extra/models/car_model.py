from __future__ import annotations
from typing import TYPE_CHECKING
from models.base_model import *

if TYPE_CHECKING:
    from models.user_model import User

class Car(Base):
    __tablename__ = 'cars'
    __table_args__ = {'schema': 'sqlalchemy'}
    
    id: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(nullable=False, unique=True)
    make: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    
    user_id = mapped_column(
        ForeignKey("sqlalchemy.users.id")
    )
    user: Mapped["User"] = relationship("User", back_populates="cars")