from task4.repositories.users_repository import UserRepository
from task4.repositories.addresses_repository import AddressRepository
from task4.repositories.cars_repository import CarRepository
from task4.db.db_manager import DbManager
from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv
from task2 import create_users_table, create_addresses_table, create_cars_table
load_dotenv()

if __name__ ==  '__main__':
    # DB Connection setup
    DB_URI  = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(url=DB_URI, echo=True)
    metadata_obj = MetaData()

    # DB Manager
    db_manager = DbManager(engine=engine)

    # Tables
    user_table = create_users_table(metadata_obj=metadata_obj)
    address_table = create_addresses_table(metadata_obj=metadata_obj)
    cars_table = create_cars_table(metadata_obj=metadata_obj)
    metadata_obj.create_all(engine)

    # Repos
    user_repository = UserRepository(db_manager=db_manager, user_table=user_table)
    address_repository = AddressRepository(db_manager=db_manager, address_table=address_table)
    car_repository = CarRepository(db_manager=db_manager, car_table=cars_table)

    # Get All
    users = user_repository.get_all()
    addresses = address_repository.get_all()
    cars = car_repository.get_all()

    # Create
    next_user = users[-1]['id'] + 1 if users else 1
    user_repository.create(fullname=f'User {next_user}', email=f'user{next_user}@example.com')

    next_address = addresses[-1]['id'] + 1 if addresses else 1
    address_repository.create(full_address=f'Address {next_address}',user_id= next_user)
    
    next_car = cars[-1]['id'] + 1 if cars else 1
    ### Just to have some unassigned cars
    if len(users) < 3:
        car_repository.create(vin=f"000{next_car}", make=f"000{next_car} make", model=f"000{next_car} model", year=2000+next_car)
    else:
        car_repository.create(vin=f"000{next_car}", make=f"000{next_car} make", model=f"000{next_car} model", year=2000+next_car, user_id=next_user)
    
    # Update
    user_repository.update(id=next_user, fullname=f'User {next_user} updated', email=f'user{next_user}@example.updated.com')
    address_repository.update(id=next_address, full_address=f'Address {next_address}, updated')
    car_repository.update(id=next_car, vin=f"000{next_car}, updated", make=f"000{next_car} make, updated", model=f"000{next_car} model, updated", year=2000+next_car)

    # Delete
    if len(users) > 3:
        first_address = addresses[0]['id']
        address_repository.delete(id=first_address)

        first_car = cars[0]['id']
        car_repository.delete(id=first_car)

        first_user = users[0]['id']
        user_repository.delete(id=first_user)