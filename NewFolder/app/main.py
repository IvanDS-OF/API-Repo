"""
from fastapi import FastAPI

from sqlalchemy import engine
from models import todo_model
from routers import todo_router 

app = FastAPI()

#todo_model.Base.metadata.create_all(bind=engine)
todo_model.Base.metadata.create_all(bind=engine)


app.include_router(todo_router.router)

"""

from fastapi import FastAPI

from database import engine
from models import todo_model
from routers import todo_router

app = FastAPI()

todo_model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)