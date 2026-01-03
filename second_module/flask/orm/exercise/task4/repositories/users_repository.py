from task4.db.db_manager import DbManager
from sqlalchemy import Table, insert, select, update, delete

class UserRepository():
    def __init__(self, db_manager:DbManager, user_table:Table):
        self.db_manager = db_manager
        self.user_table = user_table

    def create(self, fullname, email):
        try:
            stmt = (
                insert(self.user_table)
                .values(fullname=fullname, email=email)
            )
            self.db_manager.execute_write(stmt=stmt)

            print("User inserted successfully")
        except Exception as error:
            raise Exception("Error creating the user: ", error)

    def get_all(self):
        try:
            stmt = (
                select(self.user_table)
            )
            results = self.db_manager.execute_read(stmt=stmt)
            return results
        except Exception as error:
            raise Exception("Error getting all users from the database: ", error)

    def update(self, id, fullname, email):
        try:
            stmt = (
                update(self.user_table)
                .where(self.user_table.c.id == id)
                .values(fullname = fullname, email = email)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("User updated successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a user status from the database: {error}")

    def delete(self, id):
        try:
            stmt = (
                delete(self.user_table)
                .where(self.user_table.c.id == id)
            )
            self.db_manager.execute_write(stmt=stmt)
            print("User deleted successfully")
            return True
        except Exception as error:
            raise Exception(f"Error updating a user status from the database: {error}")
