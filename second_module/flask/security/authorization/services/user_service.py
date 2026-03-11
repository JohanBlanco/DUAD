from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> dict | None:
        user = self.user_repository.get_by_id(id)
        return user.to_dict() if user else None

    def get_all(self) -> list[dict]:
        users = self.user_repository.get_all()
        return [u.to_dict() for u in users]

    def get_by_username(self, username: str) -> dict | None:
        user = self.user_repository.get_by_username(username)
        return user.to_dict() if user else None

    def create(self, username: str, password: str, role: str = "user") -> dict | None:
        if self.user_repository.get_by_username(username):
            return None
        user = self.user_repository.create(username=username, password=password, role=role)
        return user.to_dict()
