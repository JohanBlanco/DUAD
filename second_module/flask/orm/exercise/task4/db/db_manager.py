from sqlalchemy import MetaData, Engine
class DbManager():
    def __init__(self, engine: Engine):
        self.engine = engine
        self.metadata = MetaData()

    def execute_read(self, stmt):
        with self.engine.connect() as conn:
            return conn.execute(stmt).mappings().all()

    def execute_write(self, stmt):
        with self.engine.begin() as conn:
            conn.execute(stmt)
