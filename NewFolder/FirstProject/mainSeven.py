from fastapi import FastAPI, HTTPException, Body
from typing import Union, Optional
from pydantic import BaseModel, Field
import asyncio

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

#To run this exercise go to the bash "sh" file within this folder

