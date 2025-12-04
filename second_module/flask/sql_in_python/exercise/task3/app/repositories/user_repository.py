from app.db.pg_manager import PgManager

class UserRepository():
    def __init__(self, db_manager:PgManager):
        self.db_manager = db_manager

    def create(self, first_name, last_name, email, username, password, birthdate, status):
        query = """
            INSERT INTO lyfter_car_rental.users 
            (first_name, last_name, email, username, password, birthdate, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (first_name, last_name, email, username, password, birthdate, status)

        self.db_manager.execute_query(query, values)

        print("User inserted successfully")
        return True

    def get_all(self):
        try:
            query = "SELECT id, first_name, last_name, email, username, birthdate, status FROM lyfter_car_rental.users;"
            results = self.db_manager.execute_query(query)
            return results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_column(self, column, value):
        try:
            query = f"SELECT id, first_name, last_name, email, username, birthdate, status FROM lyfter_car_rental.users WHERE {column} = %s;"
            values = (value,)
            results = self.db_manager.execute_query(query, values)
            return results
        except Exception as error:
            raise Exception(f"Error getting a user from the database: {error}")

    def update(self, id, first_name, last_name, email, username, password, birthdate, status):
        try:
            query = "UPDATE lyfter_car_rental.users SET (first_name, last_name, email, username, password, birthdate, status) = (%s, %s, %s,%s, %s, %s,%s) WHERE ID = %s"
            values = (first_name, last_name, email, username, password, birthdate, status, id,)
            self.db_manager.execute_query(query, values)
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, id):
        try:
            query = "DELETE FROM lyfter_car_rental.users WHERE id = (%s)"
            values = (id,)
            self.db_manager.execute_query(query, values)
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False
        
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
            print("Error getting the columns from the table", error)
            return []
        
    def get_last_record(self):
        try:
            query = "Select * from lyfter_car_rental.users where id in (SELECT max(id) id FROM lyfter_car_rental.users);"
            results = self.db_manager.execute_query(query)
            return results
        except Exception as error:
            print("Error getting last user created: ", error)
            return False
