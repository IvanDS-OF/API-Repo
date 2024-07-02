from sqlalchemy import Boolean, Column, Integer, String
from database import Base

#We creaate the model which will representate the TODO table within the database


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

