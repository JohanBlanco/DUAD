from app.repositories.user_repository import UserRepository
from app.dataclasses.user_dataclass import User
from app.helpers.exceptions import BadRequestError

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, data):
        # raises an exception if a field is missing
        user:User = User.from_dict(data)

        already_existing_user = self.repo.get_by_email(user.email)
        if already_existing_user.id:
            raise BadRequestError(f'Already exist an user with the email {user.email}')

        values = [str(value).strip() for value in user.__dict__.values()]
        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        self.repo.create(user.first_name, user.last_name, user.email,
                                user.username, user.password, user.birthdate, user.status)
        
        user = self.repo.get_by_email(user.email)
        
        return user.__dict__
    
    #CONTINUE
    def update_user(self, data, id):
        # validate business rules
        user:User = User.from_dict(data)

        if user.id:
            raise BadRequestError(f'The id cannot be updated')

        values = [str(value).strip() for value in user.__dict__.values()]
        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        self.repo.update(user.first_name, user.last_name, user.email,
                                user.username, user.password, user.birthdate, user.status)
        
        user = self.repo.get_by_email(user.email)
        
        return user.__dict__
    
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

        return [user.__dict__ for user in results]
    
    
