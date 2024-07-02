from fastapi import HTTPException, Path, File, UploadFile, APIRouter
from pydantic import BaseModel, Field
from typing import Optional, Annotated

#Following the change of creating an instance called router, we need to bring all the database created
#to this file

router = APIRouter()


todo_list = [{"id": 1,"description": "Learning Python" ,"completed": True}, 
             {"id": 2,"description": "Learning FastAPI" ,"completed": False}, 
             {"id": 3,"description": "This is my third task xd" ,"completed": False}]


class Todo(BaseModel):
    id : Optional[int] = None
    description : str = Field(min_length=5, max_length=15)
    completed : bool = Field(default=False) 


@router.get("/todo")
async def get_all(complete: bool):
    if complete is not None:
        filtered_todos = list(filter(lambda todo: todo["completed"] == complete , todo_list))
        return filtered_todos
    return todo_list


@router.get("/todo/{todo_id}")
async def get_todo(todo_id:int):
    try:
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="Sobres, no jaló, bai")


@router.post("/todo", response_model=Todo, name="Mi Endpoint Name", 
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
    

@router.post("/todo/{todo_id}/attachment")
async def upload_todo_file(todo_id: Annotated[int, Path()], file: Annotated[bytes, File()]):
    ##We should use a Try Except
    try:
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        todo_data["file_size"] = len(file)
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="SOPO Padresanto - imposibile que jale el pdo")


@router.post("/todo/{todo_id}/attachment_dos")
async def upload_todo_file_dos(todo_id: Annotated[int, Path()], file: UploadFile):
    ##We should use a Try Except
    try:
        todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
        todo_data["file_name"] = file.filename
        return todo_data
    except:
        raise HTTPException(status_code=404, detail="SOPO Padresanto - imposibile que jale el pdo")
