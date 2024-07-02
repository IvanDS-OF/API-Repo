from fastapi import FastAPI
from routers import todo, support

#We need to define an instance as APIRouter instead an FastAPI

app = FastAPI()

#We have separated all the endpoints, but we need to recognize them as oart or the application 
#to do that we must add the methosd include_router() 

app.include_router(todo.router)
app.include_router(support.router)

#but we need to include the methods within the same folder, in this case todo and support, and 
#use them as arguments of the method to call them. As shown up


@app.get("/")
async def home():
    return {
        "name": "TODO Rest API ", 
        "version": "1.0.0"
    }

#AT THE END WE CAN RUN THIS API FROM HERE, FROM THE INIT FILE