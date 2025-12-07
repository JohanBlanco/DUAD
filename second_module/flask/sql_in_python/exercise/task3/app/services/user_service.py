from app.repositories.user_repository import UserRepository
from app.dataclasses.user_dataclass import User
from app.helpers.exceptions import BadRequestError

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, data):

        body_fields = set(data.keys())

        required_fields = set(self.repo.get_columns())
        required_fields.remove('id')

        if not (required_fields.issuperset(body_fields) and len(required_fields) == len(body_fields)):
            missing_fields  = required_fields.difference(body_fields)
            raise BadRequestError(f"The following fields missing: {', '.join(missing_fields)}")

        values = [str(value).strip() for value in data.values()]
        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        user:User = User.from_dict(data)

        already_existing_user = self.repo.get_by_email(user.email)
        if already_existing_user:
            raise BadRequestError(f'Already exist the user with the email {user.email}')
        
        self.repo.create(user.first_name, user.last_name, user.email,
                                user.username, user.password, user.birthdate, user.status)
        
        user = self.repo.get_by_email(user.email)
        
        return user.__dict__
    
    def update_user_status(self, data, id):

        user = self.repo.get_by_id(id)
        if not user:
            raise BadRequestError(f'The user with the id {id} does not exist')

        if 'status' not in data:
            raise BadRequestError(f"The following fields are required in the body: status")

        if not user.status or str(user.status) == '':
            raise BadRequestError("The status cannot be empty or null")
        
        user.status = data['status']
        self.repo.update_user_status(user.id, user.status)
        user = self.repo.get_by_id(id)
        
        return user.__dict__
    
    def get_users(self, filters:dict):
        results = {}

        if filters:
            column, value = next(iter(filters.items()))
            
            allowed_columns:dict = self.repo.get_columns()
            if column not in allowed_columns and column != 'password':
                raise BadRequestError(f"The filter {column} is not valid")
                
            results = self.repo.get_by_column(column, value)
                
        else:
            results = self.repo.get_all()

        return [user.__dict__ for user in results]
