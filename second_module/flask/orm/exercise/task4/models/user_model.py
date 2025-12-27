from base_model import *
from car_model import Car
from address_model import Address

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'lyfter_car_rental'}
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    
    cars: Mapped[list["Car"]] = relationship(back_populates="user")
    addresses: Mapped[list["Address"]] = relationship(back_populates="user")