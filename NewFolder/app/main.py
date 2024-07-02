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


"""
#Este codigo sirve, pero los colocamos en comentario sporque vamos ahacer una version con el middleware afuera
#De este archivo
import time 

from fastapi import FastAPI, Request

from database import engine
from models import todo_model
from routers import todo_router

app = FastAPI()

#Lets to know the middleware here. We need to call the librery Request from fastApi
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    #Call_next - Encargada de hacer la peticipn a su respectiva ruta y retornar 
    #la respuesta generada por la petición 

    start = time.time()
    response = await call_next(request)
    total_time = time.time() - start
    response.headers["X-Process-Time"] = str(total_time)
    return response


todo_model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)

"""


import time 

from fastapi import FastAPI, Request

from starlette.middleware.base import BaseHTTPMiddleware
from middleware import add_process_time_header

from database import engine
from models import todo_model
from routers import todo_router

app = FastAPI(
    title="TODO Api"
)


app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)


async def add_process_time_header(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    total_time = time.time() - start
    response.headers["X-Process-Time"] = str(total_time)
    return response


todo_model.Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)





