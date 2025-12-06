from app.db.pg_manager import PgManager
from app.dataclasses.user_dataclass import User

class UserRepository():
    def __init__(self, db_manager:PgManager):
        self.db_manager = db_manager

    def create(self, first_name, last_name, email, username, password, birthdate, status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users "
                "(first_name, last_name, email, username, password, birthdate, status) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                first_name, last_name, email, username, password, birthdate, status
                )

            print("User inserted successfully")
        except Exception as error:
            raise Exception("Error creating the user: ", error)

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, first_name, last_name, email, username, password, TO_CHAR(birthdate, 'YYYY-MM-DD') AS birthdate, status " \
                "FROM lyfter_car_rental.users;"
            )

            results = [User.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception("Error getting all users from the database: ", error)

    def get_by_column(self, column, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, first_name, last_name, email, username, password, TO_CHAR(birthdate, 'YYYY-MM-DD') AS birthdate, status " \
                "FROM lyfter_car_rental.users " \
                f"WHERE {column} = %s;",
                value
                )
            
            results = [User.from_dict(_dict) for _dict in results]

            return results
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")
        
    def get_by_id(self, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, first_name, last_name, email, username, password, TO_CHAR(birthdate, 'YYYY-MM-DD') AS birthdate, status " \
                "FROM lyfter_car_rental.users " \
                f"WHERE id = %s;",
                value
                )
            
            if results:
                user = User.from_dict(results[0])
            else:
                return None
            
            return user
        except Exception as error:
            return User()
        
    def get_by_email(self, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, first_name, last_name, email, username, password, TO_CHAR(birthdate, 'YYYY-MM-DD') AS birthdate, status " \
                "FROM lyfter_car_rental.users " \
                f"WHERE email = %s;",
                value
                )
            
            if results:
                user = User.from_dict(results[0])
            else:
                return None
            
            return user
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")

    def update_user_status(self, id, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users " \
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
                    "AND table_name   = 'users';"
            
            results = self.db_manager.execute_query(query)
            print("Got the columns successfuly")
            results = [item["columns"] for item in results]
            return results
        except Exception as error:
            raise Exception(f"Error getting the columns from the table {error}")
