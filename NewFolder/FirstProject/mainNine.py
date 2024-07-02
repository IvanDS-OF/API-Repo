from fastapi import FastAPI, HTTPException, Body, Form, File, UploadFile, Path
from typing import Union, Optional, Annotated
from pydantic import BaseModel, Field
import asyncio

#We will know how to upload files in with FastAPI. 
#Remember all the dependencies from FastAPI - File and UploadFile - Noth uf them use Python Nutipart



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
    

@app.get("/async-endpoint")
async def async_example():
    print(f"Execution started at:", flush=True )
    await asyncio.sleep(2) 
    return {"message": "Async endpoint"}


@app.post("/support")
async def create_support_ticket(tittle: str = Form(), message: str = Form()): ##We need to define as Form type our arguments
    return {"tittle": tittle, 
            "message": message}



#From Here
#Create another Post method to upload a file: 
@app.post("/todo/{todo_id}/attachment")
async def upload_todo_file(todo_id: Annotated[int, Path()], file: Annotated[bytes, File()]):
    ##We should use a Try Except
    try:
        #Aqui se busca el elemento TODO de la lista teniendo en cuenta el ID que esta reciviendo el 
        # #endpoint a traves del path, en caso de que no lo encuentre, se va al Except
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        todo_data["file_size"] = len(file)
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="SOPO Padresanto - imposibile que jale el pdo")

##Esposible dar a un argumento dos tipos e valores de entrada. 
#Para ello tenemos que hacer uso de ANOTATED y luego escribir los tipod de variable deseados: 
#Anotated[TypoUno, TipoDos]



@app.post("/todo/{todo_id}/attachment_dos")
async def upload_todo_file_dos(todo_id: Annotated[int, Path()], file: UploadFile):
    ##We should use a Try Except
    try:
        #Aqui se busca el elemento TODO de la lista teniendo en cuenta el ID que esta reciviendo el 
        # #endpoint a traves del path, en caso de que no lo encuentre, se va al Except
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        todo_data["file_name"] = file.filename
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="SOPO Padresanto - imposibile que jale el pdo")

