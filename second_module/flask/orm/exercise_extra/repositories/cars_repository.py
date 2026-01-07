from sqlalchemy import select
from sqlalchemy.orm import Session
from models.car_model import Car
class CarRepository:
    def __init__(self, session):
        self.session:Session = session

    def get_all(self):
        stmt = select(Car)
        return self.session.scalars(stmt).all()

    def get_by_id(self, id: int):
        return self.session.get(Car, id)

    def create(self, vin: str, make: str, model: str, user = None) -> Car:
        car = Car(vin=vin, make=make, model=model, user=user)
        self.session.add(car)
        return car

    def update(self, id: int, **fields) -> Car | None:
        car = self.session.get(Car, id)
        if not car:
            return None

        for key, value in fields.items():
            setattr(car, key, value)

        return car


    def delete(self, car: Car):
        self.session.delete(car)

    def get_unassigned_cars(self):
        """Return list of cars that have no assigned user (user_id IS NULL)."""
        stmt = select(Car).where(Car.user_id.is_(None))
        return self.session.scalars(stmt).all()