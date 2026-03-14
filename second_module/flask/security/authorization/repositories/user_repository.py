from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user_model import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int):
        return self.session.get(User, id)

    def get_all(self):
        stmt = select(User)
        return self.session.scalars(stmt).all()

    def get_by_username(self, username: str):
        stmt = select(User).where(User.username == username)
        return self.session.scalars(stmt).first()

    def get_by_username_and_password(self, username: str, password: str):
        """Returns user if credentials match, else None."""
        user = self.get_by_username(username)
        if not user or user.password != password:
            return None
        return user

    def create(self, username: str, password: str, role: str = "user") -> User:
        user = User(username=username, password=password, role=role)
        self.session.add(user)
        return user
