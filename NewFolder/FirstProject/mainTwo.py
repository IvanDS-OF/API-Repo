#We will create many files with the same structure just to practice

from fastapi import FastAPI

app = FastAPI()

TODO_LIST = [
    {"id": 1, "description": "Aprender Python", "completed": True},
    {"id": 2, "description": "Aprender FasApi", "completed": False},
    {"id": 3, "description": "Tarea 3 xd", "completed": False}, 
]

def return_values(todo_list, completed):
    return list(filter(lambda todo: todo["completed"] == completed, TODO_LIST))

print(return_values(TODO_LIST, True))

#Creation of the instance
@app.get("/todo") 
async def get_all(completed:bool): #This parameter is shown in the FastAPI GUI
    filtered_todos = list(filter(lambda todo: todo["completed"] == completed, TODO_LIST))
    return filtered_todos



##Existen los Query parameter
#Que nos van a servir como filtro


##Remember . Lambda es una forma pequeña de definir funciones 
##lambda argumentos: expresion





