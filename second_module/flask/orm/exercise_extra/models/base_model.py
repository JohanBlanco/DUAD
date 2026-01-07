from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

    @classmethod
    def create_all(cls, bind):
        return cls.metadata.create_all(bind=bind)