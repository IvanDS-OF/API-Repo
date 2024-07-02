from typing import Annotated

from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

#To connect to oour DB, we need to create a file at the same level of main

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo0db" #Define the UR where will be located the data base


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    #Create a dependency to the DB 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DB_DEPENDECY = Annotated[Session, Depends(get_db)]










