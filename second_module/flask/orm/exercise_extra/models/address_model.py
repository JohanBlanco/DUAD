from __future__ import annotations
from models.base_model import *
from models.user_model import User

class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {'schema': 'sqlalchemy'}
    
    id: Mapped[int] = mapped_column(primary_key=True)
    full_address: Mapped[str] = mapped_column(nullable=False)
    
    user_id = mapped_column(
        ForeignKey("sqlalchemy.users.id"),
        nullable=False
    )
    user: Mapped[User] = relationship(back_populates="addresses")