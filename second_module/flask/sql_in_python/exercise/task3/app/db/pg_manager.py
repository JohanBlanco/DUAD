import psycopg2
from psycopg2.extras import RealDictCursor

class PgManager():
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.get_connection()
        
    def get_connection(self):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            print("Connection created succesfully")
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, args)

            if cursor.description:
                results =  cursor.fetchall()
                return results
            else:
                self.connection.commit()
