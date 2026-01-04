from sqlalchemy import MetaData, Engine, Result
from sqlalchemy.orm import Session
class DbManager():
    def __init__(self, session: Session):
        self.session = session

    def execute_write(self, stmt, return_):
            try:
                result:Result = self.session.execute(stmt)
                if return_:
                    return result.all()
            except:
                self.session.rollback()
                raise

    def delete(self, object):
            with Session(self.engine) as session:
                with session.begin():
                    session.delete(object)
                    # inner context calls session.commit(), if there were no exceptions
            # outer context calls session.close()