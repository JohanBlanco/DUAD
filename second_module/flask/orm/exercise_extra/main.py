from db.db_manager import DbManager
from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ ==  '__main__':
    # DB Connection setup
    DB_URI  = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(url=DB_URI, echo=True)

    # DB Manager
    db_manager = DbManager(engine=engine)

    # Tables

    # Repos

    # Get All

    # Create
    
    # Update

    # Delete
