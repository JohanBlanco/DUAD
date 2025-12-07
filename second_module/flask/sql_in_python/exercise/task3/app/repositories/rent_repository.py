from app.db.pg_manager import PgManager
from app.dataclasses.rent_dataclass import Rent

class RentRepository():
    def __init__(self, db_manager:PgManager):
        self.db_manager = db_manager

    def create(self, status, car_id, user_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rents "
                "(status, car_id, user_id) " \
                "VALUES (%s, %s, %s);", 
                status, car_id, user_id
                )

            print("User inserted successfully")
        except Exception as error:  
            raise Exception(f"Error creating the rent: {error}")

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.rents;"
            )

            results = [Rent.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception(f"Error getting all rents from the database: {error}")
    def get_by_column(self, column, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.rents " \
                f"WHERE {column} = %s;",
                value
                )
            
            results = [Rent.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")
        
    # CONTINUE HERE
    # need the filter function by combined filters
        
    def get_by_id(self, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.rents " \
                f"WHERE id = %s;",
                value
                )
            
            if results:
                user = Rent.from_dict(results[0])
            else:
                raise Exception(f"The rent with id {value} does not exist")
            
            return user
        except Exception as error:
            return None

    def update_rent_status(self, id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rents " \
                "SET status = %s " \
                "WHERE id = %s;",
                status, id
                )
            print("User updated successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a user status from the database: {error}")
        
    def get_columns(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT column_name as columns " \
                "FROM information_schema.columns " \
                "WHERE table_schema = 'lyfter_car_rental' " \
                "AND table_name   = 'rents';"
            )
            print("Got the columns successfuly")
            results = [item["columns"] for item in results]
            return results
        except Exception as error:
            raise Exception(f"Error getting the columns from the table {error}")
