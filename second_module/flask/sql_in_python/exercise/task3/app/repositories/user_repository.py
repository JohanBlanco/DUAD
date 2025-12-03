class UserRepository():
    def __init__(self, db_manager):
        super.__init__(db_manager)

    def create(self, first_name, last_name, email, username, password, birthdate, status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (first_name, last_name, email, username, password, birthdate, status) VALUES (%s, %s, %s,%s, %s, %s,%s)",
                (first_name, last_name, email, username, password, birthdate, status),
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            return results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_column(self, column, value):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE %s = %s;",
                (column, value),
            )
            return results
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, id, first_name, last_name, email, username, password, birthdate, status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET (first_name, last_name, email, username, password, birthdate, status) = (%s, %s, %s,%s, %s, %s,%s) WHERE ID = %s",
                (first_name, last_name, email, username, password, birthdate, status, id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.users WHERE id = (%s)", (id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False
        
    def get_columns(self):
        try:
            results = self.db_manager.execute_query(
                ''''
                SELECT column_name as columns
                FROM information_schema.columns
                WHERE table_schema = 'lyfter_car_rental' AND table_name   = 'users';
                '''
            )
            print("Got the columns successfuly")
            return results
        except Exception as error:
            print("Error getting the columns from the table", error)
            return False