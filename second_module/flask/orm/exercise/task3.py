from task1 import connect_to_db
from task2 import create_users_table, create_addresses_table, create_cars_table

if __name__ == '__main__':
    engine, metadata_obj, connection = connect_to_db()

    users_table = create_users_table(metadata_obj)
    addresses_table = create_addresses_table(metadata_obj)
    cars_table = create_cars_table(metadata_obj)

    metadata_obj.create_all(engine)
    
    print("Created the tables if they did not exist")