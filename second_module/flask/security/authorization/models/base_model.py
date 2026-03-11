from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

    @classmethod
    def create_all(cls, bind):
        return cls.metadata.create_all(bind=bind)
