##Lets to see ho to manage the information with the models. 
from fastapi import FastAPI, HTTPException, Body
from typing import Union, Optional
from pydantic import BaseModel, Field

#To work with models, we need to import BaseModel from pydantic. 

app = FastAPI()

#Then, we need to crate a class to define our model
class Todo(BaseModel):
    #Cuando definimos la clase, realmente es una definicion de la clase con atributos
    #En donde cada atrubisot en uno de los elementos que queremos representar 
    #Parecido a un constructo
    id : Optional[int] = None ##Asi creamos un atributo opcional, Optional de typing
    description : str = Field(min_length=5, max_length=15) ##Asi garantizamos una estructura al atributo Field de pydantic
    completed : bool = Field(default=False) ##Igualmente podemos definir el valor por defecto de un bool
    #Mientras usamos Pydantric, cada atributo puede tener un tipo de dato lo que permite que
    #al tratar de crear un objeto del modelo cada uno de los atributos sea validado 
    #Igualmente vamos a poder hacer que el llenado de los atributos sea opcional con Optional de typing






todo_list = [{"id": 1,"description": "Learning Python" ,"completed": True}, 
             {"id": 2,"description": "Learning FastAPI" ,"completed": False}, 
             {"id": 3,"description": "This is my third task xd" ,"completed": False}]


@app.get("/todo/{todo_id}")
async def get_todo_2(todo_id:int):
    try:
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="Sobres, no jaló, bai")


@app.post("/todo")
async def post_add_item(data: Todo):
    #Para hacer uso de nuestra clase modelo, vamos a quitar los argumentos y a colocar solamente la clase 
    try:
        todo_list.append(data) #Y en vez de agregar el diccionario completo, solamente agregamos al argumento
        #de nuestra async function

        return data
        #Como primer ejemplo solamente vamos a imprimir nuestra data recibida en el argumento
    except:
        raise HTTPException(status_code=404, detail="AYUDA DIOS PLOTS")
    






