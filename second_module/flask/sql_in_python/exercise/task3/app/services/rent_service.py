from app.repositories.rent_repository import RentRepository
from app.dataclasses.rent_dataclass import Rent
from app.helpers.exceptions import BadRequestError
from datetime import date
from app.services.car_service import CarService
from app.services.user_service import UserService

class RentService:
    def __init__(self, repo: RentRepository, car_service:CarService, user_service:UserService):
        self.repo = repo
        self.car_service = car_service
        self.user_service = user_service

    def create_rent(self, data):

        body_fields = set(data.keys())

        required_fields = set(self.repo.get_columns())
        required_fields.remove('id')
        required_fields.remove('rent_date')
        required_fields.remove('status')

        if not (required_fields.issuperset(body_fields) and len(required_fields) == len(body_fields)):
            missing_fields  = required_fields.difference(body_fields)
            raise BadRequestError(f"The following fields missing: {', '.join(missing_fields)}")

        values = [str(value).strip() for value in data.values()]
        if "" in values:
            raise BadRequestError("The are some empty fileds")
        
        rent:Rent = Rent.from_dict(data)

        if not isinstance(rent.car_id, int) or not isinstance(rent.car_id, int):
            raise BadRequestError('The car id and user id must be integer values')

        rented_cars = self.repo.get_rented_cars()
        if rent.car_id in rented_cars:
            raise BadRequestError('The car is already rented')
        
        if not rent.status:
            rent.status = 'Active'
        
        self.repo.create(status=rent.status, car_id=rent.car_id, user_id=rent.user_id)
        rent_id = self.repo.get_last_record_id()
        rent:Rent = self.repo.get_by_id(rent_id)

        self.car_service.update_car_status({'status': 'rented'}, rent.car_id)
        
        return rent.to_dict()
    
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
        
        return rent.to_dict()
    
    def get_rents(self, filters:dict):
        results = {}

        if filters:
            column, value = next(iter(filters.items()))  

            allowed_columns:dict = self.repo.get_columns()
            if column not in allowed_columns:
                raise BadRequestError(f"The filter {column} is not valid")

            results = self.repo.get_by_column(column, value)        
        else:
            results = self.repo.get_all()

        return Rent.convert_list_to_dict(results)
    

    def mark_rent_as_completed(self, rent_id):
        rent = self.repo.get_by_id(rent_id)

        self.update_rent_status(id=rent_id, data={'status': 'Completed'})
        self.car_service.update_car_status(id=rent.car_id, data={'status': 'available'})

        return self.repo.get_by_id(rent_id).to_dict()

