from task4.db.db_manager import DbManager
from sqlalchemy import Table, insert, select, update, delete

class AddressRepository():
    def __init__(self, db_manager:DbManager, address_table:Table):
        self.db_manager = db_manager
        self.address_table = address_table

    def create(self, full_address, user_id):
        try:
            stmt = (
                insert(self.address_table)
                .values(full_address=full_address, user_id=user_id)
            )
            self.db_manager.execute_write(stmt=stmt)

            print("Address inserted successfully")
        except Exception as error:
            raise Exception("Error creating the address: ", error)

    def get_all(self):
        try:
            stmt = (
                select(self.address_table)
            )
            results = self.db_manager.execute_read(stmt=stmt)
            return results
        except Exception as error:
            raise Exception("Error getting all addresss from the database: ", error)

    def update(self, id, full_address):
        try:
            stmt = (
                update(self.address_table)
                .where(self.address_table.c.id == id)
                .values(full_address = full_address)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("Address updated successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a address status from the database: {error}")

    def delete(self, id):
        try:
            stmt = (
                delete(self.address_table)
                .where(self.address_table.c.id == id)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("Address deleted successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a address status from the database: {error}")
