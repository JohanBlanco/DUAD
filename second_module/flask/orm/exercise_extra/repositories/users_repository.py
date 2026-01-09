from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user_model import User
from sqlalchemy import func
from models.car_model import Car

class UserRepository:
    def __init__(self, session):
        self.session:Session = session

    def get_all(self):
        stmt = select(User)
        users = self.session.scalars(stmt).all()
        return users

    def get_by_id(self, id: int):
        return self.session.get(User, id)

    def create(self, fullname: str, email: str) -> User:
        user = User(fullname=fullname, email=email)
        self.session.add(user)
        return user

    def update(self, id: int, **fields) -> User | None:
        user = self.session.get(User, id)
        if not user:
            return None

        for key, value in fields.items():
            setattr(user, key, value)

        return user


    def delete(self, user: User):
        # An address cannot live without its user, because of business rules
        for address in user.addresses:
            self.session.delete(address)

        self.session.delete(user)

    def get_users_with_more_than_one_car(self):
        stmt = (
            select(User)
            .join(Car, User.id == Car.user_id)
            .group_by(User.id)
            .having(func.count(Car.id) > 1)
        )
        return self.session.scalars(stmt).all()
