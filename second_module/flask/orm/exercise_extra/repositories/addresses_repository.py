from sqlalchemy import select
from sqlalchemy.orm import Session
from models.address_model import Address

class AddressRepository:
    def __init__(self, session):
        self.session:Session = session

    def get_all(self):
        stmt = select(Address)
        return self.session.scalars(stmt).all()

    def get_by_id(self, id: int):
        return self.session.get(Address, id)

    def create(self, fullname: str, email: str) -> Address:
        address = Address(fullname=fullname, email=email)
        self.session.add(address)
        return address

    def update(self, id: int, **fields) -> Address | None:
        address = self.session.get(Address, id)
        if not address:
            return None

        for key, value in fields.items():
            setattr(address, key, value)

        return address


    def delete(self, address: Address):
        self.session.delete(address)
