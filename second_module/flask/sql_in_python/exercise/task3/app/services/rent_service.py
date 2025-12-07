from app.repositories.rent_repository import RentRepository
from app.dataclasses.rent_dataclass import Rent
from app.helpers.exceptions import BadRequestError
from datetime import date

class RentService:
    def __init__(self, repo: RentRepository):
        self.repo = repo

    def create_rent(self, data):

        body_fields = set(data.keys())

        required_fields = set(self.repo.get_columns())
        required_fields.remove('id')

        if not (required_fields.issuperset(body_fields) and len(required_fields) == len(body_fields)):
            missing_fields  = required_fields.difference(body_fields)
            raise BadRequestError(f"The following fields missing: {', '.join(missing_fields)}")

        values = [str(value).strip() for value in data.values()]
        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        rent:Rent = Rent.from_dict(data)

        if not isinstance(rent.car_id, int) or not isinstance(rent.car_id, int):
            raise BadRequestError('The car id and user id must be integer values')

        # Validate the car is not in use
        
        self.repo.create(rent.status, rent.car_id, rent.user_id)
        
        rent = self.repo.get_by_email(rent.car_id, rent.user_id, date.today())
        
        return rent.__dict__
    
    def update_rent_status(self, data, id):

        rent = self.repo.get_by_id(id)
        if not rent:
            raise BadRequestError(f'The rent with the id {id} does not exist')

        if 'status' not in data:
            raise BadRequestError(f"The following fields are required in the body: status")

        if not rent.status or str(rent.status) == '':
            raise BadRequestError("The status cannot be empty or null")
        
        rent.status = data['status']
        self.repo.update_rent_status(rent.id, rent.status)
        rent = self.repo.get_by_id(id)
        
        return rent.__dict__
    
    def get_rents(self, filters:dict):
        results = {}

        if filters:
            column, value = next(iter(filters.items()))    
            results = self.repo.get_by_column(column, value)        
        else:
            results = self.repo.get_all()

        return [rent.__dict__ for rent in results]
