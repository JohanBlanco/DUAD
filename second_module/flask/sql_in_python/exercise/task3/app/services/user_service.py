from app.repositories.user_repository import UserRepository
from app.models.user_dto import CreateUserDto, UpdateUserDto
from app.helpers.exceptions import BadRequestError

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, data):
        # raises an exception if a field is missing
        user = CreateUserDto(**data)

        values = [str(value).strip() for value in user.__dict__.values()]

        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        self.repo.create(user.first_name, user.last_name, user.email,
                                user.username, user.password, user.birthdate, user.status)
        
        user = self.repo.get_last_record()
        
        return user
    
    def update_user(self, data):
        # validate business rules
        user = UpdateUserDto(**data)

        
        return self.repo.update(user.first_name, user.last_name, user.email,
                                user.username, user.password, user.birthdate, user.status)
    
    def get_users(self, filters:dict):
        # validate business rules
        results = {}

        if filters:
            column, value = next(iter(filters.items()))
            
            allowed_columns:dict = self.repo.get_columns()
            if column not in allowed_columns and column != 'password':
                # change this for a better exception
                raise BadRequestError(f"The filter {column} is not valid")
                
            results = self.repo.get_by_column(column, value)
                
        else:
            results = self.repo.get_all()

        return results
    
    
