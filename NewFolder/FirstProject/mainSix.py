from fastapi import FastAPI, HTTPException, Body
from typing import Union, Optional
from pydantic import BaseModel, Field

#Vamos a ver a detalle cómo funciona nuestro Path Operator Decorator y los parametros que 
#podemos usar para configurarlo


app = FastAPI()

class Todo(BaseModel):
    id : Optional[int] = None
    description : str = Field(min_length=5, max_length=15)
    completed : bool = Field(default=False) 


todo_list = [{"id": 1,"description": "Learning Python" ,"completed": True}, 
             {"id": 2,"description": "Learning FastAPI" ,"completed": False}, 
             {"id": 3,"description": "This is my third task xd" ,"completed": False}]


@app.get("/todo")
async def get_all(complete: bool):
    if complete is not None:
        filtered_todos = list(filter(lambda todo: todo["completed"] == complete , todo_list))
        return filtered_todos
    return todo_list


@app.get("/todo/{todo_id}")
async def get_todo(todo_id:int):
    try:
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="Sobres, no jaló, bai")

##Este es un decorador: Sintaxis. 
#@ nombre de la instancia . metodo HTTP ("/RUTA")
#La RUTA es un string que inicia con /, es a traves de este ENDPOINT que se crea un elemento
#de tipo todo
#   Ccon el parametro "esponse_model=" podemos definir de qué modelo seran los elementos que 
#retorna el endpoint, que tiene que ser el nombre de una clase,en este caso usaremos la que teneoms ya
#   El matametro "name= " sirve para agregar un nombre al endpoint - visible en la documentaicon
@app.post("/todo", response_model=Todo, name="Mi Endpoint Name", 
          summary="Create a Todo Element", 
          description="Creates a TODO element given an id, description, and complete status",
          status_code=201, deprecated=False)
        #Retorna un 201 porque es un endpoint Post
async def post_add_item(data: Todo): 
    try:
        todo_list.append(data) 
        return data
    except:
        raise HTTPException(status_code=404, detail="AYUDA DIOS PLOTS")
    






