from repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> dict | None:
        """Returns user dict (without password) if credentials are valid, else None."""
        user = self.user_repository.get_by_username_and_password(username, password)
        if not user:
            return None
        return user.to_dict()

    def get_user_by_id(self, user_id: int) -> dict | None:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            return None
        return user.to_dict()

    def register(self, username: str, password: str, role: str = "user") -> dict | None:
        if self.user_repository.get_by_username(username):
            return None
        user = self.user_repository.create(username=username, password=password, role=role)
        return user.to_dict()
