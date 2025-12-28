from task4.db.db_manager import DbManager
from sqlalchemy import Table, insert, select, update, delete

class CarRepository():
    def __init__(self, db_manager:DbManager, car_table:Table):
        self.db_manager = db_manager
        self.car_table = car_table

    def create(self, vin, make, model, year, user_id=None):
        try:
            stmt = (
                insert(self.car_table)
                .values(vin = vin, make=make, model=model, year=year, user_id=user_id)
            )
            self.db_manager.execute_write(stmt=stmt)

            print("Car inserted successfully")
        except Exception as error:
            raise Exception("Error creating the car: ", error)

    def get_all(self):
        try:
            stmt = (
                select(self.car_table)
            )
            results = self.db_manager.execute_read(stmt=stmt)
            return results
        except Exception as error:
            raise Exception("Error getting all cars from the database: ", error)

    def update(self, id, vin, make, model, year, user_id=None):
        try:
            stmt = (
                update(self.car_table)
                .where(self.car_table.c.id == id)
                .values(vin = vin, make=make, model=model, year=year, user_id=user_id)
            ) if user_id else (
                update(self.car_table)
                .where(self.car_table.c.id == id)
                .values(vin = vin, make=make, model=model, year=year)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("Car updated successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a car status from the database: {error}")

    def delete(self, id):
        try:
            stmt = (
                delete(self.car_table)
                .where(self.car_table.c.id == id)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("Car deleted successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a car status from the database: {error}")
