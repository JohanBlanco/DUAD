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

    def create(self, fullname: str, email: str) -> Car:
        car = Car(fullname=fullname, email=email)
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
