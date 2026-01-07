from repositories.users_repository import UserRepository
from repositories.addresses_repository import AddressRepository
from repositories.cars_repository import CarRepository
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
import random
from dotenv import load_dotenv
import fake_data as fd
load_dotenv()

"""
I want to simultae transactions, so im doing the session stuff here in main
just to put everything together in one file for the exercise
"""

if __name__ ==  '__main__':
    # DB Connection setup
    DB_URI  = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(url=DB_URI, echo=True)

    # Tables
    Base.create_all(engine)

    # Task1
    with Session(engine) as session:
        user_repo = UserRepository(session=session)
        car_repo = CarRepository(session=session)
        address_repo = AddressRepository(session=session)

        # print(car_repo.get_unassigned_cars())
        # print(user_repo.get_users_with_more_than_one_car())
        print(address_repo.filter_addresses(search="Calle"))

    # Task2
    # with Session(engine) as session:
    #     user_repo = UserRepository(session=session)

    #     users = user_repo.get_all()
    #     for user in users:
    #         print(f"user id {user.id} \n cars: {len(user.cars)} \n addresses: {len(user.addresses)}\n\n")
    
    # Task3
    with Session(engine) as session:
        user_repo = UserRepository(session)
        car_repo = CarRepository(session)
        address_repo = AddressRepository(session)

        for _ in range(20):
            fake_user = fd.create_user()
            user = user_repo.create(
                fullname=fake_user.fullname,
                email=fake_user.email
            )

            session.flush()

            for index in range(2):
                fake_address = fd.create_address()
                address_repo.create(
                    full_address=fake_address.full_address,
                    user=user
                )

            fake_car = fd.create_car()
            car_repo.create(
                vin=fake_car.vin,
                make=fake_car.make,
                model=fake_car.model,
                user=user
            )

            # car without user
            fake_car = fd.create_car()
            car_repo.create(
                vin=fake_car.vin,
                make=fake_car.make,
                model=fake_car.model
            )

            if index // 5 == 0:
                # another car for the user
                fake_car = fd.create_car()
                car_repo.create(
                    vin=fake_car.vin,
                    make=fake_car.make,
                    model=fake_car.model,
                    user=user
                )

        session.commit()
