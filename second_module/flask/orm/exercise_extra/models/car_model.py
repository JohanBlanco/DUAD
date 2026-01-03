from base_model import *
from user_model import User

class Car(Base):
    __tablename__ = 'cars'
    __table_args__ = {'schema': 'lyfter_car_rental'}
    
    id: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(nullable=False, unique=True)
    make: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    
    user_id = mapped_column(
        ForeignKey("lyfter_car_rental.users.id"),
        nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="cars")