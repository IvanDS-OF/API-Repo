from fastapi import FastAPI, HTTPException, Body

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

##Lets to know how to use the POST method
#In order to know how to use the body parameters. 

##First we need to import "body" from the FastApi library
#Define the decorator, methos and path
@app.post("/todo1")
async def post_add_item_1(id:int = Body(), description:str = Body(), completed:bool = Body()): 
    #We must ned to declare our arguments of the function as body parameters, therer could be confusion
    #with the path parameters
    try:
        #Initiali, lets to show the arguments typed
        return id, description, completed
    except:
        raise HTTPException(status_code=404, detail="AYUDA DIOS PLOTS")
    

##This add the new information to our dictionary and returns all the table updated
@app.post("/todo")
async def post_add_item(id:int = Body(), description:str = Body(), completed:bool = Body()): 
    try:
        #Add the informatio to my table: Add a new dictionary
        todo_list.append({
            "id": id, "description": description, "completed": completed
        })


        return todo_list
    except:
        raise HTTPException(status_code=404, detail="AYUDA DIOS PLOTS")
    

