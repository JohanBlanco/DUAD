import psycopg2
from psycopg2.extras import RealDictCursor

class PgManager():
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.create_connection()
        
    def create_connection(self):
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        print("Connection created succesfully")
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, args)

                if cursor.description:
                    return cursor.fetchall()
                else:
                    self.connection.commit()
                    return None

        except Exception as e:
            self.connection.rollback()
            print(e)
            raise e

