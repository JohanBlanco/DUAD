from db.pg_manager import PgManager
import os
from dotenv import load_dotenv
load_dotenv()

db_manager = PgManager(
    db_name=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

def validate_the_table_exists_and_has_records(table_name:str):
    table_name = table_name.capitalize()
    message = "Database OK. Operating system functioning normally."

    try:
        results = db_manager.execute_query(
            f"SELECT * FROM lyfter_car_rental.{table_name};"
        )
        
        if not results:
            message = f"DB ERROR. No {table_name} available."
    except Exception as e:
        print(e)
        message = f"DB ERROR. No {table_name} available."

    print(message)
    return message

def check_db():
    validate_the_table_exists_and_has_records('cars')
    validate_the_table_exists_and_has_records('users')
    validate_the_table_exists_and_has_records('rents')


if __name__ == '__main__':
    check_db()