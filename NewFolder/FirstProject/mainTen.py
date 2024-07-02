from fastapi import FastAPI
from routers import todo, support

from enum import Enum

#We need to define an instance as APIRouter instead an FastAPI

app = FastAPI(
    title="Aprendiendi a hacer APIs con Python"
)

#We have separated all the endpoints, but we need to recognize them as oart or the application 
#to do that we must add the methosd include_router() 

app.include_router(todo.router)
app.include_router(support.router)

#but we need to include the methods within the same folder, in this case todo and support, and 
#use them as arguments of the method to call them. As shown up

##In this file, we will consider as well, the topic of Tags
#The tags are defined as lists
#Just like in Java, we can create an Enum class, to have a starndard in the mane of the Tags

class Tags(Enum):
    home: str = "Home"


#@app.get("/", tags=["Home"]) #This is one way to name our tag. But it is recommensable to 
                            #Name them with an enum class as follow
@app.get("/", tags=[Tags.home])
async def home():
    return {
        "name": "TODO Rest API ", 
        "version": "1.0.0"
    }

#AT THE END WE CAN RUN THIS API FROM HERE, FROM THE INIT FILE