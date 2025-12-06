from app.db.pg_manager import PgManager
from app.dataclasses.car_dataclass import Car

class CarRepository():
    def __init__(self, db_manager:PgManager):
        self.db_manager = db_manager

    def create(self, vin, make, model, year, status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars "
                "(vin, make, model, year, status) " \
                "VALUES (%s, %s, %s, %s, %s);", 
                vin, make, model, year, status
                )

            print("User inserted successfully")
        except Exception as error:  
            raise Exception(f"Error creating the car: {error}")

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.cars;"
            )

            results = [Car.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception(f"Error getting all cars from the database: {error}")
    def get_by_column(self, column, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.cars " \
                f"WHERE {column} = %s;",
                value
                )
            
            results = [Car.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")
        
    def get_by_id(self, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.cars " \
                f"WHERE id = %s;",
                value
                )
            
            if results:
                user = Car.from_dict(results[0])
            else:
                raise Exception(f"The car with id {value} does not exist")
            
            return user
        except Exception as error:
            return None
        
    def get_by_vin(self, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * " \
                "FROM lyfter_car_rental.cars " \
                f"WHERE vin = %s;",
                value
                )
            
            if results:
                user = Car.from_dict(results[0])
            else:
                return None
            
            return user
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")

    def update_car_status(self, id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars " \
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
            query = "SELECT column_name as columns " \
                    "FROM information_schema.columns " \
                    "WHERE table_schema = 'lyfter_car_rental' " \
                    "AND table_name   = 'cars';"
            
            results = self.db_manager.execute_query(query)
            print("Got the columns successfuly")
            results = [item["columns"] for item in results]
            return results
        except Exception as error:
            raise Exception(f"Error getting the columns from the table {error}")
