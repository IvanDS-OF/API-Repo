from fastapi import FastAPI, HTTPException

app = FastAPI()

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


