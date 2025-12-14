from db.pg_manager import PgManager
import os
from dotenv import load_dotenv
import pandas
from datetime import date
from pathlib import Path
load_dotenv()

db_manager = PgManager(
    db_name=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

def get_backup_path(table_name:str):
    BASE_DIR = Path(__file__).resolve().parent
    backup_dir = BASE_DIR / "db_backups"
    backup_dir.mkdir(exist_ok=True)

    return backup_dir / f"{table_name}_backup_{date.today():%Y-%m-%d}.csv"

def backup_table(table_name:str):
    results = db_manager.execute_query(
        f"SELECT * FROM lyfter_car_rental.{table_name};"
    )
    df:pandas.DataFrame = pandas.DataFrame(results)
    path = get_backup_path(table_name)
    df.to_csv(path, index=False)
    print(f'The backup for {table_name} table is ready')

def backup_db():
    backup_table('cars')
    backup_table('users')
    backup_table('rents')


if __name__ == '__main__':
    backup_db()
