from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy import Integer, String

def create_users_table(metadata_obj:MetaData):
    users_table = Table(
        'users',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('fullname', String(50)),
        Column('email', String(100)),
        schema='sqlalchemy'
    )
    print("Table users created succesfully")
    return users_table

def create_addresses_table(metadata_obj:MetaData):
    addresses_table = Table(
        'addresses',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('full_address', String(500)),
        user_id = Column("user_id", ForeignKey("users.id"), nullable=False),
        schema='sqlalchemy'
    )
    print("Table addresses created succesfully")
    return addresses_table

def create_cars_table(metadata_obj:MetaData):
    cars_table = Table(
        'cars',
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('vin', String(50)),
        Column('make', String(50)),
        Column('model', String(50)), 
        Column('year', Integer),
        user_id = Column("user_id", ForeignKey("users.id")),
        schema='sqlalchemy'
    )
    print("Table cars created succesfully")
    return cars_table