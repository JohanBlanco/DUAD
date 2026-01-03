# Realice el setup de SQLAlchemy, adjunte un screenshot de la validación de la versión de la biblioteca.
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

print(sqlalchemy.__version__)

def connect_to_db():
    # postgresql://<username>:<password>@<host>:<port>/<database>
    DB_URI  = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(url=DB_URI, echo=True)
    metadata_obj = MetaData()

    try:
        connection = engine.connect()
        print("Connection successful!")

        return engine, metadata_obj, connection
    except Exception as e:
        print("Connection failed:", e)

if __name__ == '__main__':
    connect_to_db()