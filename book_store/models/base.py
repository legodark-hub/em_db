from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    metadata = MetaData(schema="book_store")
    
    def __repr__(self):
        return f"{self.__class__.__name__}, {self.__dict__}"
