from faker import Faker
import random
from models.user_model import User
from models.address_model import Address
from models.car_model import Car
from models.base_model import Base

MAKES = [
    "Toyota", "Ford", "Honda", "Chevrolet", "BMW", "Audi", "Mercedes", "Nissan", "Kia", "Hyundai"
]

# Global Faker instance for the module
faker = Faker()


def create_user(fullname: str | None = None, email: str | None = None) -> User:
    """Return a `User` instance (not persisted). Uses module-level `faker` by default."""
    fullname = fullname or faker.name()
    email = email or faker.unique.email()

    return User(fullname=fullname, email=email)


def create_address(full_address: str | None = None, user: User | None = None) -> Address:
    """Return an `Address` instance (not persisted). Uses module-level `faker` by default."""
    full_address = full_address or faker.address().replace("\n", ", ")
    addr = Address(full_address=full_address)

    if user is not None:
        addr.user = user

    return addr


def create_car(vin: str | None = None, make: str | None = None, model: str | None = None, user: User | None = None) -> Car:
    """Return a `Car` instance (not persisted). Uses module-level `faker` by default."""
    vin = vin or faker.unique.bothify(text="??######??######").upper()
    make = make or random.choice(MAKES)
    model = model or faker.word().capitalize()

    car = Car(vin=vin, make=make, model=model)

    if user is not None:
        car.user = user

    return car