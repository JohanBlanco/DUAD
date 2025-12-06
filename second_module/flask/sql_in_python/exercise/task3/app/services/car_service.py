from app.repositories.car_repository import CarRepository
from app.dataclasses.car_dataclass import Car
from app.helpers.exceptions import BadRequestError

class CarService:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def create_car(self, data):

        body_fields = set(data.keys())

        required_fields = set(self.repo.get_columns())
        required_fields.remove('id')

        if not (required_fields.issuperset(body_fields) and len(required_fields) == len(body_fields)):
            missing_fields  = required_fields.difference(body_fields)
            raise BadRequestError(f"The following fields missing: {', '.join(missing_fields)}")

        values = [str(value).strip() for value in data.values()]
        if "" in values:
            raise BadRequestError("There some empty fileds")
        
        car:Car = Car.from_dict(data)

        already_existing_car = self.repo.get_by_email(car.email)
        if already_existing_car.id:
            raise BadRequestError(f'Already exist the car with the vin {car.email}')
        
        self.repo.create(car.vin, car.make, car.model, car.year, car.status)
        
        car = self.repo.get_by_vin(car.vin)
        
        return car.__dict__
    
    def update_car_status(self, data, id):

        car = self.repo.get_by_id(id)
        if not car:
            raise BadRequestError(f'The car with the id {id} does not exist')

        if 'status' not in data:
            raise BadRequestError(f"The following fields are required in the body: status")

        if not car.status or str(car.status) == '':
            raise BadRequestError("The status cannot be empty or null")
        
        car.status = data['status']
        self.repo.update_car_status(car.id, car.status)
        car = self.repo.get_by_id(id)
        
        return car.__dict__
    
    def get_cars(self, filters:dict):
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

        return [car.__dict__ for car in results]
