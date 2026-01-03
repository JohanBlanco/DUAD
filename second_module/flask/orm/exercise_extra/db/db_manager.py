from sqlalchemy import MetaData, Engine
from sqlalchemy.orm import Session
class DbManager():
    def __init__(self, engine: Engine):
        self.engine = engine

    def add(self, object):
        # I know this can be done, using with begin, so it is less verbouse, im just 
        # trying to get used to the verbose structure of a transaction
        with Session(self.engine) as session:
            session.begin()
            try:
                session.add(object)
            except:
                session.rollback()
                raise
            else:
                session.commit()

    # CONTINUE HERE IN THE DOC Expiring / Refreshing
    # https://docs.sqlalchemy.org/en/20/orm/session_basics.html#what-does-the-session-do

    def delete(self, object):
            with Session(self.engine) as session:
                with session.begin():
                    session.delete(object)
                    # inner context calls session.commit(), if there were no exceptions
            # outer context calls session.close()