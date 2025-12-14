from dotenv import load_dotenv
from db.pg_manager import PgManager
import os
from classes.car_dataclass import Car
from classes.rent_dataclass import Rent
from classes.user_dataclass import User

from faker import Faker

load_dotenv()

db_manager = PgManager(
    db_name=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

fake = Faker()

def create_fake_user():
    return User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.unique.email(),
        username=fake.unique.user_name(),
        password = fake.password(),
        birthdate= fake.date_of_birth(),
        status = fake.random_element(elements=("Active", "Blocked"))
    )

def create_fake_car():
    cars_info = {
            "Toyota": ["Corolla", "Camry", "RAV4"],
            "Ford": ["Fiesta", "Focus", "F-150"],
            "Honda": ["Civic", "Accord", "CR-V"],
            "BMW": ["320i", "X3", "X5"],
        }
    make = fake.random_element(list(cars_info.keys()))
    return Car(
        vin = fake.unique.bothify(text='?' * 17).upper(),
        make = make,
        model = fake.random_element(cars_info[make]),
        year = fake.year(),
        status = fake.random_element(elements=("available", "rented", "maintenance"))
    )

def create_fake_rent():
    return Rent(
        status=fake.random_element(("Active", "Completed", "Cancelled")),
        car_id=fake.random_int(min=1, max=100),
        user_id=fake.random_int(min=1, max=200)
    )

def insert_user(user:User):
    try:
        db_manager.execute_query(
            "INSERT INTO lyfter_car_rental.users "
            "(first_name, last_name, email, username, password, birthdate, status) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s);", 
            user.first_name, user.last_name, user.email, user.username, user.password, user.birthdate, user.status
            )

        print("User inserted successfully")
    except Exception as error:
        raise Exception("Error creating the user: ", error)


def insert_car(car:Car):
    try:
        db_manager.execute_query(
            "INSERT INTO lyfter_car_rental.cars "
            "(vin, make, model, year, status) " \
            "VALUES (%s, %s, %s, %s, %s);", 
            car.vin, car.make, car.model, car.year, car.status
            )

        print("Car inserted successfully")
    except Exception as error:  
        raise Exception(f"Error creating the car: {error}")

def insert_rent(rent:Rent):
    try:
        db_manager.execute_query(
            "INSERT INTO lyfter_car_rental.rents "
            "(status, car_id, user_id) " \
            "VALUES (%s, %s, %s);", 
            rent.status, rent.car_id, rent.user_id
            )

        print("Rent inserted successfully")
    except Exception as error:  
        raise Exception(f"Error creating the rent: {error}")
    
if __name__ == '__main__':
    # Create 200 users
    for _ in range(200):
        user = create_fake_user()
        insert_user(user)

    # Create 100 cars
    for _ in range(100):
        car = create_fake_car()
        insert_car(car)

    # # # Create 150 rents
    for _ in range(150):
        rent = create_fake_rent()
        insert_rent(rent)
